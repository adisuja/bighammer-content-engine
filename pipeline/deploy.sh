#!/usr/bin/env bash
# Publish the review studio to GitHub Pages (https://adisuja.github.io/bighammer-content-studio/).
#   bash pipeline/deploy.sh "Batch 3: 30 posts"
# Rebuilds studio/ from queue/posts.json + rendered assets, syncs it into a checkout of
# adisuja/bighammer-content-studio (cloned on first run), commits and pushes. Pages rebuilds in ~1 minute.
# Needs push access to adisuja/bighammer-content-studio (gh auth login).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SITE="${BH_SITE_DIR:-$HOME/BigHammer Misc/content-studio-site}"
MSG="${1:-Update review studio}"

python3 "$ROOT/pipeline/publish.py"
if [ ! -d "$SITE/.git" ]; then
  mkdir -p "$(dirname "$SITE")"
  git clone -q https://github.com/adisuja/bighammer-content-studio.git "$SITE"
fi
git -C "$SITE" pull -q --rebase
rsync -a --delete --exclude .git --exclude CNAME --exclude README.md "$ROOT/studio/" "$SITE/"
git -C "$SITE" add -A
if git -C "$SITE" diff --cached --quiet; then echo "nothing to deploy"; exit 0; fi
git -C "$SITE" commit -qm "$MSG"
git -C "$SITE" push -q
V="$(grep -o 'app.js?v=[0-9]*' "$ROOT/studio/index.html" | cut -d= -f2)"
echo "deployed. Wait ~60s, then verify: https://adisuja.github.io/bighammer-content-studio/?v=$V"
