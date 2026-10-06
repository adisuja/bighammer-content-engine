"""Build the review site (studio/) from queue/posts.json + rendered assets.

    python3 pipeline/publish.py            # rebuild studio/data.js + media, bump ?v=
Copies assets/<media.src>/out/*.png -> studio/media/<media.src>/*.jpg (Batch 2 used bare IDs like "C1";
batch 3 onwards MUST use batch-scoped folders like "b3/C1" so IDs never collide), writes studio/data.js, stamps a cache-busting
version into index.html. The JPGs are on-screen previews only; every image/carousel post also gets a full-quality
upload file (original PNG, or a lossless carousel PDF) behind the studio's Download button. A ready post without
one fails the build. Sample creatives are linked (original post URL), never re-hosted.
"""
from __future__ import annotations

import glob
import json
import os
import re
import shutil
import sys
import time

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STUDIO = os.path.join(ROOT, "studio")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import taxonomy  # noqa: E402


def sample_urls() -> dict:
    try:
        return {r["id"]: r["Post URL"] for r in taxonomy.load()}
    except Exception as e:  # offline: the site still builds, sample links are just omitted
        print(f"  (taxonomy unavailable: {e}; sample links omitted)")
        return {}


def lossless_pdf(pngs: list[str], path: str) -> None:
    """Carousel PDF for LinkedIn document posts: one page per slide, PNG pixels embedded Flate (lossless) at
    full resolution. PIL's PDF writer re-encodes to JPEG, which softens type, so it is not used for uploads."""
    import fitz  # PyMuPDF

    doc = fitz.open()
    for p in pngs:
        w, h = Image.open(p).size
        page = doc.new_page(width=w / 2, height=h / 2)  # 144 dpi: 1080x1350 px -> 540x675 pt
        page.insert_image(page.rect, filename=p)
    doc.set_metadata({"title": os.path.basename(path), "producer": "BigHammer publish.py"})  # no dates: same input, same bytes
    doc.save(path, deflate=True, garbage=3, no_new_id=True)
    doc.close()


def download_for(post: dict, m: dict, src: str, pngs: list[str]) -> dict | None:
    """Full-quality upload file shown under the review box: the PNG byte-for-byte for images, a lossless PDF
    for carousels. Written next to the preview JPGs; kept as-is on fresh clones where renders are absent."""
    dst = os.path.join(STUDIO, "media", src)
    ext = "pdf" if m["type"] == "carousel" else "png"
    name = f"BigHammer-b{post.get('batch', '2')}-{post['id']}-{post['date']}-{post['profile']}.{ext}"
    path = os.path.join(dst, name)
    # only this post's own files: a media folder may one day be shared by two posts (e.g. a repost)
    mine = [f for f in glob.glob(os.path.join(dst, f"BigHammer-b{post.get('batch', '2')}-{post['id']}-*.{ext}")) if f != path]
    if pngs:
        for old in mine:
            os.remove(old)
        if ext == "pdf":
            lossless_pdf(pngs, path)
        else:
            shutil.copyfile(pngs[0], path)
    elif not os.path.exists(path) and len(mine) == 1:
        os.replace(mine[0], path)  # fresh clone after a date/profile change: keep the committed file, new name
    if not os.path.exists(path):
        return None
    if ext == "pdf":
        import fitz  # PyMuPDF
        with fitz.open(path) as doc:  # read from the file itself so the button label can never drift from it
            pages = doc.page_count
            first = doc.extract_image(doc[0].get_images()[0][0])
            w, h = first["width"], first["height"]
    else:
        pages, (w, h) = 1, Image.open(path).size
    return {"href": f"media/{src}/{name}?v={V}", "name": name, "ext": ext, "bytes": os.path.getsize(path),
            "pages": pages, "w": w, "h": h}


def media_for(post: dict) -> dict:
    m = dict(post.get("media") or {})
    src = m.get("src")
    if m.get("type") in ("image", "carousel") and src:
        out = os.path.join(ROOT, "assets", src, "out")
        pngs = sorted(glob.glob(os.path.join(out, "slide-*.png"))) or sorted(glob.glob(os.path.join(out, "image.png")))
        if not pngs:
            # fresh clone: renders (assets/*/out) are git-ignored, but the published JPGs in studio/media are
            # committed, so keep serving those instead of blanking a live post
            kept = sorted(glob.glob(os.path.join(STUDIO, "media", src, "p*.jpg"))) or sorted(glob.glob(os.path.join(STUDIO, "media", src, "image.jpg")))
            if not kept:
                return {"type": "pending"}
            m["files"] = [f"media/{src}/{os.path.basename(k)}?v={V}" for k in kept]
            if m["type"] == "image":
                im = Image.open(kept[0])
                m["tall"] = im.height / im.width > 1.26
            m["download"] = download_for(post, m, src, [])
            return m
        dst = os.path.join(STUDIO, "media", src)
        os.makedirs(dst, exist_ok=True)
        files = []
        for i, p in enumerate(pngs, 1):
            name = f"p{i:02d}.jpg" if m["type"] == "carousel" else "image.jpg"
            im = Image.open(p).convert("RGB")
            im.save(os.path.join(dst, name), quality=90, optimize=True, progressive=True)
            files.append(f"media/{src}/{name}?v={V}")
            if m["type"] == "image":
                m["tall"] = im.height / im.width > 1.26
        m["files"] = files
        m["download"] = download_for(post, m, src, pngs)
    return m


def no_dashes(obj, path="") -> None:
    """Owner rule (global CLAUDE.md): no em or en dashes anywhere in published content."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            no_dashes(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            no_dashes(v, f"{path}[{i}]")
    elif isinstance(obj, str) and re.search("[\u2013\u2014]", obj):
        raise SystemExit(f"EM/EN DASH in queue/posts.json{path}: {obj[:80]!r}")


def main() -> None:
    global V
    V = time.strftime("%Y%m%d%H%M")
    q = json.load(open(os.path.join(ROOT, "queue", "posts.json")))
    no_dashes(q)
    urls = sample_urls()
    for pr in q["profiles"]:
        pr["avatar_ok"] = os.path.exists(os.path.join(STUDIO, pr["avatar"]))
    posts = []
    for p in q["posts"]:
        p = dict(p)
        declared = dict(p.get("media") or {})  # media_for may downgrade it to "pending"
        p["media"] = media_for(p)
        p["key"] = f"b{p.get('batch', '2')}-{p['id']}"
        if declared.get("type") in ("image", "carousel") and p.get("status") == "ready" and not p["media"].get("download"):
            raise SystemExit(f"{p['key']}: no full-quality download (render assets/{declared.get('src')} first: pipeline/render.py)")
        if p.get("sample", {}).get("id") in urls:
            p["sample"]["url"] = urls[p["sample"]["id"]]
        posts.append(p)
    data = {"batches": q.get("batches", []), "profiles": q["profiles"], "posts": posts, "webinar_url": q["webinar_url"], "sync_url": q.get("sync_url", "")}
    core = {"campaigns": [], "linkChecks": [], "linkCheckedAt": "", "tokens": {}, "people": {}, "socialDefault": {"reactors": "", "comments": 0, "reposts": 0}}
    with open(os.path.join(STUDIO, "data.js"), "w") as f:
        f.write("/* generated by pipeline/publish.py from queue/posts.json - do not edit */\n")
        f.write("window.PREVIEW_DATA = " + json.dumps(core) + ";\n")
        f.write("window.STUDIO = " + json.dumps(data, ensure_ascii=False, indent=1) + ";\n")
    v = V
    idx = os.path.join(STUDIO, "index.html")
    html = open(idx).read()
    html = re.sub(r"\?v=[\w_]+", f"?v={v}", html)
    open(idx, "w").write(html)
    print(f"published {len(posts)} posts, v={v}")


if __name__ == "__main__":
    main()
