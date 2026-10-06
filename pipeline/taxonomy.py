"""LinkedIn Creator Taxonomy: the sample library every post is matched to.

    python3 pipeline/taxonomy.py fetch              # refresh the local cache from the Google Sheet
    python3 pipeline/taxonomy.py unused             # samples not yet used by ANY batch in queue/posts.json
    python3 pipeline/taxonomy.py unused --creator AV
    python3 pipeline/taxonomy.py show AV44          # full design + copy breakdown of one sample

Source: sheet 1I0vs3k4Wz-xsvMaeGd-9t4VhaFzW2v7lvUI2Mg3Iyvc, tab "LinkedIn Creator Taxonomy" (gid 349467685).
The cache lives in .private/taxonomy.json (git-ignored: it holds other creators' full post copy).
Sample IDs are creator initials + 2-digit post number, e.g. HD05 (Harry Dry, post 5).
"""
from __future__ import annotations

import csv
import io
import json
import os
import ssl
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CACHE = os.path.join(ROOT, ".private", "taxonomy.json")
URL = "https://docs.google.com/spreadsheets/d/1I0vs3k4Wz-xsvMaeGd-9t4VhaFzW2v7lvUI2Mg3Iyvc/export?format=csv&gid=349467685"
KNOWN = {"Harry Dry": "HD", "Austin Belcak": "AB", "Alex Vacca": "AV", "Patrick James Cumming": "PC"}


def abbr(creator: str) -> str:
    return KNOWN.get(creator) or "".join(w[0] for w in creator.split()[:2]).upper()


def sample_id(row: dict) -> str:
    return f"{abbr(row['Creator'])}{int(row['Post #']):02d}"


def fetch() -> list[dict]:
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = ssl.create_default_context()
    raw = urllib.request.urlopen(URL, context=ctx, timeout=60).read().decode("utf-8")
    rows = [r for r in csv.DictReader(io.StringIO(raw)) if r.get("Creator") and r.get("Post #")]
    for r in rows:
        r["id"] = sample_id(r)
    os.makedirs(os.path.dirname(CACHE), exist_ok=True)
    json.dump(rows, open(CACHE, "w"), ensure_ascii=False, indent=1)
    return rows


def load() -> list[dict]:
    if not os.path.exists(CACHE):
        return fetch()
    rows = json.load(open(CACHE))
    for r in rows:
        r.setdefault("id", sample_id(r))
    return rows


def used() -> dict:
    q = json.load(open(os.path.join(ROOT, "queue", "posts.json")))
    return {p["sample"]["id"]: f"batch {p.get('batch', '2')} {p['id']}" for p in q["posts"] if p.get("sample", {}).get("id")}


def main(argv: list[str]) -> None:
    cmd = argv[0] if argv else "unused"
    if cmd == "fetch":
        print(f"cached {len(fetch())} samples -> {os.path.relpath(CACHE, ROOT)}")
    elif cmd == "unused":
        only = argv[argv.index("--creator") + 1] if "--creator" in argv else None
        u = used()
        rows = [r for r in load() if r["id"] not in u and (not only or r["id"].startswith(only))]
        for r in rows:
            print(f"{r['id']:6} {r.get('Content Format', '')[:22]:22} | {r.get('Media Format Detail', '')[:44]:44} | {r.get('Design · Layout Archetype', '')[:60]}")
        print(f"\n{len(rows)} unused of {len(load())} (used so far: {len(u)})")
    elif cmd == "show":
        r = next((x for x in load() if x["id"] == argv[1].upper()), None)
        if not r:
            raise SystemExit(f"no sample {argv[1]}")
        for k, v in r.items():
            if v and k not in ("Raw Media Links (all)", "Sidecars Skipped"):
                print(f"{k}: {v}")
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv[1:])
