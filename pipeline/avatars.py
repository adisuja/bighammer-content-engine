"""Create-once avatar library for Richard and Terry (kie.ai nano-banana-pro, likeness from 8 real
reference photos). Every post reuses these files; nothing is regenerated.

    python3 pipeline/avatars.py create richard          # generate any MISSING poses only
    python3 pipeline/avatars.py path richard headshot   # -> absolute path of a stored pose
    python3 pipeline/avatars.py list

Images live in .private/avatars/<person>/<pose>.png (git-ignored: real people's likeness).
The manifest (no images) is committed at brand/avatars/manifest.json: pose, file, prompt, kie task,
credits, date. A pose that already exists is never sent to kie.ai again.
"""
from __future__ import annotations

import glob
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kie  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST = os.path.join(ROOT, "brand", "avatars", "manifest.json")
STORE = os.path.join(ROOT, ".private", "avatars")
REFS = os.path.join(ROOT, ".private", "refs")

PEOPLE = {
    "richard": "a bald man in his late fifties with fair skin, a narrow long face, deep-set eyes, a long straight nose, a high forehead, thin lips, visible forehead and eye wrinkles, a faint grey shadow of shaved hair at the sides, wearing a light blue business shirt",
    "terry": "a man in his late forties with medium-brown skin, thick dark-grey hair swept back, strong dark eyebrows, a full salt-and-pepper beard that is grey at the chin, a broad face and warm dark eyes, wearing a light blue business shirt",
}
BASE = ("Photorealistic professional photograph of the exact same real person shown in the reference photos "
        "({who}). IDENTITY LOCK: reproduce his real face exactly as in the references: same face shape and width, "
        "same nose length and shape, same eye spacing and depth, same ears, same age and wrinkles. Do not beautify, "
        "do not make him younger, do not widen the jaw or smooth the skin. Natural skin texture, sharp focus on the "
        "eyes, shot on a full-frame camera, 85mm lens. ")
POSES = {
    "headshot": ("1:1", "Head and shoulders LinkedIn profile headshot, looking straight at the camera with a warm, confident closed-mouth smile, soft studio light, plain light grey backdrop."),
    "portrait": ("4:5", "Editorial waist-up portrait, arms loosely crossed, slight smile, standing in front of a plain warm grey studio wall, soft window light from the left, calm and credible."),
    "thoughtful": ("4:5", "Waist-up, one hand resting on his chin, thoughtful expression looking slightly off camera, plain light grey studio backdrop, soft light."),
    "presenting": ("4:5", "Waist-up, gesturing with an open palm as if explaining an idea to a small audience, engaged friendly expression, plain light grey studio backdrop."),
    "laptop": ("4:5", "Sitting at a clean modern office desk with a laptop, looking up at the camera mid-conversation with a relaxed smile, bright contemporary office with soft daylight, shallow depth of field."),
    "office": ("4:5", "Standing in a bright modern open-plan office with large windows, holding a coffee mug, natural candid smile towards the camera, soft background blur, lifestyle editorial photo."),
    "speaking": ("4:5", "Speaking at a small industry meetup, holding a microphone, mid-sentence, warm stage light, blurred audience silhouettes in the background, candid event photography."),
    "wide": ("4:5", "Wide lifestyle photo, full body, standing relaxed and leaning on a railing of a bright modern office atrium, looking slightly off camera with a calm smile. He is small in the frame, occupying only the lower 40% of the image; the upper 55% of the frame is open, softly blurred bright architecture and daylight, leaving clean empty space above him. Natural light, editorial photography."),
    "cutout": ("4:5", "Half-body, facing the camera, neutral friendly expression, arms relaxed, evenly lit on a perfectly plain flat white background with no shadows, suitable for cutting out."),
}


def load() -> dict:
    return json.load(open(MANIFEST)) if os.path.exists(MANIFEST) else {}


def save(m: dict) -> None:
    os.makedirs(os.path.dirname(MANIFEST), exist_ok=True)
    json.dump(m, open(MANIFEST, "w"), indent=1)


def path(person: str, pose: str) -> str:
    e = load().get(person, {}).get(pose)
    if not e:
        raise SystemExit(f"no stored pose {person}/{pose}. Run: python3 pipeline/avatars.py create {person}")
    return os.path.join(ROOT, e["file"])


def create(person: str, only: list[str] | None = None) -> None:
    m = load()
    m.setdefault(person, {})
    refs = sorted(glob.glob(os.path.join(REFS, person, "*.jpg")))[:8]
    if len(refs) < 4:
        raise SystemExit(f"need reference photos in {REFS}/{person}")
    os.makedirs(os.path.join(STORE, person), exist_ok=True)
    for pose, (ar, desc) in POSES.items():
        if only and pose not in only:
            continue
        out = os.path.join(STORE, person, f"{pose}.png")
        if pose in m[person] and os.path.exists(out):
            print(f"skip {person}/{pose} (already created)")
            continue
        prompt = BASE.format(who=PEOPLE[person]) + desc
        r = kie.generate(prompt, out, ar=ar, refs=refs)
        m[person][pose] = {"file": os.path.relpath(out, ROOT), "aspect": ar, "prompt": prompt,
                           "kie_task": r.get("task"), "credits": r.get("credits"),
                           "refs": [os.path.basename(x) for x in refs], "created": time.strftime("%Y-%m-%d")}
        save(m)
        print(f"created {person}/{pose} ({r.get('credits')} credits{', cached' if r.get('cached') else ''})")


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "create":
        create(sys.argv[2], sys.argv[3:] or None)
    elif cmd == "path":
        print(path(sys.argv[2], sys.argv[3]))
    else:
        for p, poses in load().items():
            print(p, ", ".join(f"{k} ({v['credits']} cr)" for k, v in poses.items()))
