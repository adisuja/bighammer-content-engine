"""Render asset HTML -> PNG (and carousel PDF).

Usage:
  python3 pipeline/render.py assets/C1            # renders every slide-*.html / image.html in the folder
Each HTML is a 1080x1350 canvas that links ../../pipeline/brand.css. Output: <folder>/out/*.png
(rendered at 2x, downsampled to 1080x1350 for crisp type) and <folder>/out/carousel.pdf when
there is more than one slide. A contact sheet (<folder>/out/_sheet.png) is written for review.
"""
from __future__ import annotations

import glob
import os
import sys

from PIL import Image
from playwright.sync_api import sync_playwright

W, H = 1080, 1350


def render(folder: str) -> list[str]:
    pages = sorted(glob.glob(os.path.join(folder, "slide-*.html"))) or sorted(glob.glob(os.path.join(folder, "image.html")))
    if not pages:
        raise SystemExit(f"no slide-*.html or image.html in {folder}")
    out = os.path.join(folder, "out")
    os.makedirs(out, exist_ok=True)
    pngs = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        ctx = b.new_context(viewport={"width": W, "height": H}, device_scale_factor=2)
        pg = ctx.new_page()
        for html in pages:
            pg.goto("file://" + os.path.abspath(html))
            pg.evaluate("document.fonts.ready")
            # typographic apostrophes/quotes in visible text (never inside code/pre)
            pg.evaluate("""() => { const w = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
              let n; while ((n = w.nextNode())) { if (n.parentElement.closest('code,pre,.mono,script,style')) continue;
                n.nodeValue = n.nodeValue.replace(/(\\w)'(\\w)/g, '$1’$2').replace(/(^|[\\s(])'/g, '$1‘').replace(/'/g, '’'); } }""")
            pg.wait_for_timeout(450)
            # canvas height can be overridden per asset: <body data-h="1500">
            h = int(pg.evaluate("document.body.dataset.h || 0") or H)
            pg.set_viewport_size({"width": W, "height": h})
            pg.wait_for_timeout(150)
            overflow = pg.evaluate("""() => [...document.querySelectorAll('[data-fit]')]
                .filter(e => e.scrollHeight > e.clientHeight + 1 || e.scrollWidth > e.clientWidth + 1)
                .map(e => e.dataset.fit)""")
            if overflow:
                print(f"  OVERFLOW in {os.path.basename(html)}: {overflow}")
            dashes = pg.evaluate("() => (document.body.innerText.match(/.{0,25}[\u2013\u2014].{0,25}/g) || [])")
            if dashes:
                raise SystemExit(f"EM/EN DASH in {html}: {dashes}  (owner rule: never use them)")
            raw = os.path.join(out, os.path.basename(html).replace(".html", "@2x.png"))
            pg.screenshot(path=raw, clip={"x": 0, "y": 0, "width": W, "height": h})
            final = raw.replace("@2x", "")
            Image.open(raw).convert("RGB").resize((W, h), Image.LANCZOS).save(final, optimize=True)
            os.remove(raw)
            pngs.append(final)
        b.close()
    if len(pngs) > 1:
        ims = [Image.open(x).convert("RGB") for x in pngs]
        ims[0].save(os.path.join(out, "carousel.pdf"), save_all=True, append_images=ims[1:], resolution=144)
    sheet(pngs, os.path.join(out, "_sheet.png"))
    return pngs


def sheet(pngs: list[str], path: str, w: int = 360) -> None:
    first = Image.open(pngs[0])
    h = int(w * first.height / first.width)
    cols = min(len(pngs), 4)
    rows = (len(pngs) + cols - 1) // cols
    s = Image.new("RGB", (cols * w + (cols + 1) * 12, rows * h + (rows + 1) * 12), (60, 60, 66))
    for i, x in enumerate(pngs):
        im = Image.open(x).convert("RGB").resize((w, h), Image.LANCZOS)
        s.paste(im, (12 + (i % cols) * (w + 12), 12 + (i // cols) * (h + 12)))
    s.save(path)


if __name__ == "__main__":
    for f in sys.argv[1:]:
        print("\n".join(render(f)))
