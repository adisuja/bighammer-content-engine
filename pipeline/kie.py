"""Minimal kie.ai client (nano-banana-pro) for hero images and likeness avatars.

    python3 pipeline/kie.py "<prompt>" out.png [--ar 4:5] [--ref a.jpg --ref b.jpg ...]

The API key is read from .private/kie.env (git-ignored). Reference photos are uploaded per call
(kie deletes uploaded inputs after ~3 days). Endpoints mirror ~/content-engine/backend/app/ai/kie_ai.py.
"""
from __future__ import annotations

import argparse
import base64
import json
import os
import sys
import time
import ssl
import urllib.request

import certifi

CTX = ssl.create_default_context(cafile=certifi.where())

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://api.kie.ai"
UPLOAD = "https://kieai.redpandaai.co/api/file-base64-upload"


def key() -> str:
    for line in open(os.path.join(ROOT, ".private", "kie.env")):
        if line.startswith("KIE_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("no KIE_API_KEY in .private/kie.env")


def _req(url: str, body: dict | None = None) -> dict:
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method="POST" if body is not None else "GET",
                               headers={"Authorization": f"Bearer {key()}", "Content-Type": "application/json"})
    with urllib.request.urlopen(r, timeout=120, context=CTX) as resp:
        return json.loads(resp.read())


def upload(path: str) -> str:
    mime = "image/jpeg" if path.lower().endswith((".jpg", ".jpeg")) else "image/png"
    b64 = base64.b64encode(open(path, "rb").read()).decode()
    res = _req(UPLOAD, {"base64Data": f"data:{mime};base64,{b64}", "uploadPath": "images/refs",
                        "fileName": os.path.basename(path)})
    url = (res.get("data") or {}).get("downloadUrl")
    if not url:
        raise RuntimeError(f"upload failed: {res}")
    return url


CACHE = os.path.join(ROOT, ".private", "kie_cache.json")


def _cache_key(prompt: str, ar: str, refs: list[str] | None, res: str) -> str:
    import hashlib
    h = hashlib.sha256()
    h.update(f"{prompt}|{ar}|{res}".encode())
    for p in refs or []:
        h.update(hashlib.sha256(open(p, "rb").read()).hexdigest().encode())
    return h.hexdigest()


def generate(prompt: str, out: str, ar: str = "4:5", refs: list[str] | None = None, res: str = "2K",
             max_wait: int = 420, force: bool = False) -> dict:
    """Generate once. An identical request (same prompt, aspect, resolution and reference bytes)
    returns the stored file from .private/kie_cache.json instead of spending credits again."""
    import shutil
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    k = _cache_key(prompt, ar, refs, res)
    hit = cache.get(k)
    if hit and os.path.exists(hit["out"]) and not force:
        if os.path.abspath(hit["out"]) != os.path.abspath(out):
            shutil.copyfile(hit["out"], out)
        return {**hit, "cached": True}
    r = _generate(prompt, out, ar, refs, res, max_wait)
    cache[k] = {**r, "out": os.path.abspath(out), "prompt": prompt[:300], "ar": ar,
                "at": time.strftime("%Y-%m-%d %H:%M")}
    json.dump(cache, open(CACHE, "w"), indent=1)
    return r


def _generate(prompt: str, out: str, ar: str = "4:5", refs: list[str] | None = None, res: str = "2K",
              max_wait: int = 420) -> dict:
    inp = {"prompt": prompt[:10000], "aspect_ratio": ar, "resolution": res, "output_format": "png"}
    if refs:
        inp["image_input"] = [upload(p) for p in refs[:8]]
    sub = _req(f"{BASE}/api/v1/jobs/createTask", {"model": "nano-banana-pro", "input": inp})
    tid = (sub.get("data") or {}).get("taskId")
    if not tid:
        raise RuntimeError(f"submit rejected: {sub}")
    t0 = time.time()
    while time.time() - t0 < max_wait:
        time.sleep(6)
        d = (_req(f"{BASE}/api/v1/jobs/recordInfo?taskId={tid}").get("data") or {})
        st = (d.get("state") or "").lower()
        if st == "success":
            rj = d.get("resultJson")
            rj = json.loads(rj) if isinstance(rj, str) else rj
            url = (rj or {}).get("resultUrls", [None])[0]
            with urllib.request.urlopen(url, timeout=120, context=CTX) as rr, open(out, "wb") as fh:
                fh.write(rr.read())
            return {"task": tid, "url": url, "credits": d.get("creditsConsumed"), "out": out}
        if st == "fail":
            raise RuntimeError(f"generation failed: {d.get('failMsg') or d.get('failCode')}")
    raise TimeoutError(f"task {tid} not done after {max_wait}s")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("prompt"); ap.add_argument("out")
    ap.add_argument("--ar", default="4:5"); ap.add_argument("--ref", action="append", default=[])
    ap.add_argument("--res", default="2K")
    a = ap.parse_args()
    print(json.dumps(generate(a.prompt, a.out, a.ar, a.ref, a.res)))
