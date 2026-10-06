# BigHammer.ai LinkedIn content engine: team playbook

Everything a teammate (or a Claude Code session) needs to produce a batch of LinkedIn posts at the
Batch 2 quality bar and publish it to the shared review site. Every rule here came from explicit owner
or Srinath feedback. None is a stylistic preference, so none is optional.

- **Review site (all batches, one URL):** https://adisuja.github.io/bighammer-content-studio/
- **Engine repo (this repo):** https://github.com/adisuja/bighammer-content-engine
- **Weekly batch prompt:** [prompts/new-batch.md](prompts/new-batch.md) (paste it into Claude Code, fill the inputs block)

---

## 1. What a batch is

A batch is N posts (typically 24 to 50) spread across four LinkedIn profiles, reviewed together on the
studio site under a collapsible "Batch N" dropdown in the sidebar, one link per profile.

| Profile id | Who | Publish time | Voice |
|---|---|---|---|
| `company` | BigHammer.ai company page | 10:00 UK | "Data engineer's best friend": friendly, expert, authoritative, measured-first honesty |
| `srinath` | Srinath Reddy, Founder & CEO | 10:00 ET (New York) | Primary author. See corpus/voice.md (hard rules below) |
| `richard` | Richard Lawrence | 10:00 UK | Ex Talend / Pentaho / StreamSets sales. British spelling. Measured, warm, plain, buyer-side honesty |
| `terry` | Terry Dhariwal | 10:00 UK | Neutral practitioner voice. Never mention his current employer or claim a BigHammer title. Posts promote BigHammer's product, positioning and the webinar |

- Batch 1 was the 9 blogs (corpus/blogs-batch1.md). **Batch 2** = 24 posts, 2 to 7 Oct 2026. Batch 3 onwards follow the same structure.
- **Cadence: one post per profile per day, consecutive days, weekends included.** A batch of 40 = 10 days × 4 profiles. A new batch starts the day after the previous batch's last post for that profile.
- **No approval pauses mid-build.** Build the whole batch, then the owner reviews everything at once on the site.

## 2. Non-negotiable content rules

1. **No em dashes or en dashes (the long Unicode dashes U+2014 and U+2013). Anywhere.** Not in copy, first comments, slide text, image text, UI copy or docs. Use a full stop, comma, colon, parentheses, or "to" for ranges. `render.py` and `publish.py` hard-fail on them.
2. **Srinath's hard rules** (from his review comments):
   - no dashes as punctuation and no tick/check-mark lists;
   - every number needs sign-off from Varadha (Head of Engineering), so list them in `numbers_for_signoff`;
   - always "up to" before savings/TCO claims;
   - say "your platform bill", never "the Databricks bill is impossible to predict" (legal);
   - no client naming or tagging;
   - no AI-generated image of Srinath (use his real photo);
   - name line on images: **"Srinath Reddy - Founder & CEO"**;
   - story-first, very simple English, problem → how we fix it → result;
   - kind, never attacks a person or a product;
   - nothing that reads like pasted ChatGPT.
3. **No filler furniture in media ("AI slop").** Remove:
   - kicker tags ("CHEAT SHEET", "A SMALL CONFESSION");
   - category/byline strips ("Data engineering leadership | Srinath Reddy");
   - "save this / share / swipe" footers;
   - slide numbers;
   - repeated "BigHammer.ai" sub-lines.

   Allowed: logo top right, the required name line, the content, the webinar CTA, and a source line only where a number is cited.
4. **Cold-reader rule.** Introduce every person on first mention in captions and first comments ("BigHammer.ai founder and CEO Srinath Reddy"). On Srinath's own profile use "I". No internal names (Varadha, Glenn), no internal jargon, and no relative dates ("tomorrow") unless they're true on the publish date.
5. **No claim without a source.** Every number, product fact or date must trace to `corpus/facts.md` or a dated `corpus/research/YYYY-MM-DD-verified-facts.md` file with URLs. Mark anything unverifiable UNVERIFIED and don't use it (e.g. the "$207B" agentic spend stat).
6. **No duplicate angles.** Check `corpus/used-content-registry.md` AND every `idea` in `queue/posts.json` (all previous batches). A fact may be reused only with a new hook, argument and takeaway.
7. **Webinar share.** At least 40% of every batch promotes the current webinar/CTA:
   - a carousel's last slide is the CTA;
   - the post has a first comment with a personalised CTA line and the link;
   - order CTA posts as a countdown to the event;
   - a post dated after the event must not promote it.

   Current: "Reduce your Databricks costs up to 75%" live masterclass, Srinath Reddy, **Thu 15 Oct 2026, 12:00 PM ET / 5 PM UK**, https://webinar.bighammerai.com/. There is no replay URL yet. Other CTAs: book a demo https://bighammer.ai/book-demo/.
8. **Healthcare case numbers conflict** ($2.74M vs $3M+/yr vs ~50% TCO). Don't use them until reconciled.
9. **Srinath's mix:** 1 leadership post to 1 BigHammer/technical post. Pillars:
   - Databricks and Snowflake cost;
   - consolidating point solutions;
   - legacy ETL to cloud;
   - AI agents building data products;
   - no lock-in.

   Never position against the public cloud providers.

## 3. Design rules (the top quality milestone)

- **Source of truth:** `brand/brand-guidelines.md` (website palette and type, measured from bighammer.ai). Ink #141414, dark #0D0D14, neon green #00FF89, violet #5600EF, magenta #FE0079 (yellow #FCFF00 is disputed, so avoid it). Axiforma 700 to 800 display, Poppins body, Geist on dark, mono for code/labels.
- Logo **top right** on every image (`brand/assets/bighammer-logo-{dark,light}.svg`).
- **Match the sample's sophistication.** Every post is matched to one unique sample from the LinkedIn Creator Taxonomy. The asset must reach that sample's craft level: layout archetype, hierarchy, imagery, density. It must not become a generic template.
- **Loop until it passes:** render, view the contact sheet at phone size, critique against the sample, fix, re-render. Then get a second-model critique (Codex `critic` subagent if available, else a fresh model session given only the sample breakdown and the PNGs). Fix everything it finds that's real.
- Canvas 1080×1350 (override with `<body data-h="...">`), rendered at 2x. `[data-fit]` elements are overflow-checked; no overflow may ship.
- **People imagery:**
  - Srinath: real photo only, `brand/assets/photos/` (private kit).
  - Richard and Terry: kie.ai avatars are **created once and reused forever**. Run `python3 pipeline/avatars.py list`, then `path <person> <pose>`. Poses: headshot, portrait, thoughtful, presenting, laptop, office, speaking, wide (Richard only), cutout.
  - Never regenerate an existing pose. `create` only fills missing ones and costs kie credits.
- Non-person illustrations (3D icons, scenes) may use `pipeline/kie.py` (nano-banana-pro). Requests are cached in `.private/kie_cache.json`, so repeats are free.

## 4. Copy templates

Use the matching template from [corpus/prompt-templates.md](corpus/prompt-templates.md) (a copy of the owner's Google Doc `1adrCJ_QqaiKJJPXAogVz45OJfES-EtoZa4Yg6DyYUhM`, so no Doc access is needed):
- Experiential Story
- Carousel
- Thought Leadership
- Repurposed Slidepost
- News Post
- Case Study
- Viral Quotes

If the sample's own copy structure is stronger, use that instead (`python3 pipeline/taxonomy.py show <ID>` prints its copy). Record which one in `copy_basis`.

## 5. Repo map

```
PLAYBOOK.md                 this file
prompts/new-batch.md        the weekly batch prompt
queue/posts.json            SOURCE OF TRUTH: batches[] + posts[] for every batch
queue/BUILD_STATE_B<N>.md   per-batch resume file (post map, status, decisions)
corpus/voice.md             voice rules per profile
corpus/prompt-templates.md  the 7 copy templates (owner's prompt doc)          corpus/facts.md  sourced claims
corpus/used-content-registry.md   no-duplication gate        corpus/research/  dated verified facts
ideas/ideas-YYYY-MM-DD*.md  idea lists with hooks + sources
brand/brand-guidelines.md   palette, type, logo, no-filler rule
brand/avatars/manifest.json avatar poses + prompts (images are in the private kit)
assets/<ID>/                Batch 2 media (bare IDs)
assets/b<N>/<ID>/           Batch 3+ media (MUST be batch-scoped). image.html or slide-01.html... or build.py
pipeline/render.py          HTML -> PNG (2x, overflow check, curly quotes, dash guard, contact sheet)
pipeline/taxonomy.py        fetch | unused | show: the sample library
pipeline/avatars.py         create-once avatar library        pipeline/kie.py  kie.ai client
pipeline/publish.py         posts.json + renders -> studio/ (data.js, media, cache-bust) + full-quality downloads
                            (original PNG per image, lossless PDF per carousel); fails if a ready post has none
pipeline/deploy.sh          publish + push studio/ to GitHub Pages
pipeline/review-sync.gs     Apps Script behind the shared feedback store
studio/                     the review site (LinkedIn iOS phones, approvals, feedback feed)
```

**Asset paths for Batch 3+:** an asset at `assets/b3/C1/image.html` is one level deeper than Batch 2, so it links `../../../pipeline/brand.css`, `../../../brand/assets/...` and `../../../.private/avatars/...`. Its post has `"media": {"type": "image", "src": "b3/C1"}`. Render with `python3 pipeline/render.py assets/b3/C1`.

## 6. Post record (queue/posts.json)

```json
{"id": "S1", "batch": "3", "profile": "srinath", "status": "ready", "date": "2026-10-08", "time": "10:00",
 "short": "6-word label", "idea": "the angle in one line", "format": "Carousel · 8 slides, ...",
 "sample": {"id": "AB34", "creator": "Austin Belcak", "what": "what we borrowed from it"},
 "copy_basis": "which template / sample structure and why", "cta": true,
 "media": {"type": "image|carousel|poll", "src": "b3/S1", "title": "..."},
 "text": "the full post copy", "first_comment": "CTA line + link (CTA posts), else a value-add comment or \"\"",
 "sources": ["..."], "numbers_for_signoff": ["every number in a Srinath post"]}
```
Also append `{"id": "3", "title": "Batch 3", "dates": "Thu 8 Oct to Sat 17 Oct 2026"}` to `batches[]`. IDs (C1, S1, R1, T1 …) only need to be unique within a batch; the site keys everything as `b<batch>-<id>`. A poll uses `"media": {"type": "poll", "question": "...", "options": ["...", "..."]}` (max 4 options, each 30 chars max).

## 7. Review site behaviour (don't break these)

- Sidebar: one collapsible dropdown per batch, exactly one link per profile with an approval count. The newest batch opens by default, and only the selected batch renders.
- Approvals (Glenn, BigHammer team) and multi-person feedback notes are an append-only event log. It's stored in the browser AND in the shared Google Sheet (via the Apps Script web app in `sync_url`). An item shows "✓ Saved" only after it's been read back from the sheet. Anything unconfirmed is retried, sent on page close, and the page warns before closing.
- **Never delete rows in the sheet.** Open browsers re-send missing items (that's the durability guarantee). To remove a note or approval, append a retract event: POST `{"id":"rx-<id>","t":"<iso>","post":"_retract","kind":"comment","name":"<who>","text":"<event id>"}` to `sync_url`.
- Header controls: tally, sync badge, All / Needs review / Approved filter, 3 per row, 100/85/70%. Don't add buttons that do nothing.

## 8. Research and tools rules

- LinkedIn, X, Reddit, Instagram, YouTube and other social sites: **Agent Reach only** (`li-harvest search|read`, `curl https://r.jina.ai/<url>`). Never scrape them directly and never use anyone's LinkedIn account. `/in/` profile pages are login-walled.
- Links are verified visually, not by HTTP status (a 200 can serve stale content).
- Secrets: `.private/kie.env` holds the kie.ai key. Never print, commit or paste it. `.private/` is git-ignored.

## 9. Private team kit (not in git)

Ask the owner for the private kit and unzip it into the repo root:
- `.private/avatars/` (Richard and Terry pose library)
- `.private/refs/` (reference photos)
- `.private/kie.env` (key, shared separately)
- `brand/assets/photos/` (Srinath's real photos)
- `brand/assets/fonts/axiforma-*` (licensed)

`pipeline/taxonomy.py fetch` recreates `.private/taxonomy.json`.

Setup: `pip install playwright pillow pymupdf certifi && python3 -m playwright install chromium`, plus `gh auth login` (push access to both repos).

Access checklist for a new teammate:
- GitHub collaborator on `adisuja/bighammer-content-engine` (to push batch branches) AND `adisuja/bighammer-content-studio` (to deploy the review site).
- The private kit.
- Nothing else: the taxonomy sheet and the review store need no login.

## 10. Definition of done for a batch

- [ ] N posts in `queue/posts.json` with `batch`, a `batches[]` entry, dates consecutive per profile, correct times
- [ ] ≥40% CTA posts, each with a first comment + link; no post promotes an event that's already past on its publish date
- [ ] Every post matched to a sample unused by any batch (`taxonomy.py unused`), recorded in `sample`
- [ ] Every claim sourced; `numbers_for_signoff` filled for Srinath posts; no registry duplicates
- [ ] Every asset rendered with no overflow, passes the self-critique loop and a second-model critique
- [ ] 0 em/en dashes, 0 filler labels, logo top right, correct name lines, cold-reader check passed
- [ ] Deployed with `pipeline/deploy.sh`. On the live, cache-busted URL: the batch dropdown shows 4 profile links, N posts render, 0 broken images, sync badge "✓ All saved", and every card shows the strip under the feedback box: Download PNG (images) or Download PDF (carousels) at full 1080 × 1350, plus Copy post copy and Copy first comment
- [ ] `corpus/used-content-registry.md` gains a "Batch N" section; `queue/BUILD_STATE_B<N>.md` complete; engine repo committed and pushed
