Paste everything inside the fence below into a new Claude Code session opened in the
`bighammer-content-engine` repo folder. Fill in the INPUTS block first. Blank fields use the defaults.

```text
You are building the next batch of BigHammer.ai LinkedIn content, end to end, at world-class quality,
and publishing it to the shared review site. Work autonomously until the definition of done is met.
Do not stop for approvals mid-build: the owner reviews the whole batch at the end.

==================================== INPUTS ====================================
BATCH_NUMBER:        3
TOTAL_POSTS:         30
SPLIT:               auto            # auto = equal across company/srinath/richard/terry, remainder to
                                     # company then srinath. Or explicit: company 8, srinath 8, richard 7, terry 7
START_DATES:         auto            # auto = the day after each profile's last scheduled post in queue/posts.json
CTA_SHARE:           40%             # minimum share of posts that promote the CTA below
CTA:                 Webinar "Reduce your Databricks costs up to 75%", Srinath Reddy,
                     Thu 15 Oct 2026, 12:00 PM ET / 5 PM UK, https://webinar.bighammerai.com/
FALLBACK_CTA:        Book a demo https://bighammer.ai/book-demo/   # for CTA posts dated after the event
IDEA_APPROVAL:       no              # yes = show me the idea list and wait before building media
MUST_COVER:          (topics, news, launches, stories or angles that must be in this batch)
IDEATION_INPUTS:     (links, docs, transcripts, customer questions, competitor moves, notes)
EXTRA_CONTEXT:       (anything else: new positioning, new proof points, things to avoid, new people)
FORMAT_WISHES:       (optional: e.g. "more carousels", "2 polls", "one video-style cover per profile")
PROFILE_CHANGES:     (optional: add/remove a profile, change a time zone, change a headline)
================================================================================

## 0. Boot and resume (always first)
1. Read PLAYBOOK.md in full. It holds the binding rules (content, design, cadence, review site, tools,
   definition of done). Then read, in this order: corpus/voice.md, corpus/used-content-registry.md,
   corpus/facts.md, the newest corpus/research/*-verified-facts.md, brand/brand-guidelines.md,
   queue/posts.json (every batch so far: ideas, samples, dates, CTA share), and the previous
   queue/BUILD_STATE_B<N-1>.md.
2. If queue/BUILD_STATE_B<BATCH_NUMBER>.md exists, RESUME from it: never redo finished work.
   Otherwise create it with the inputs, the computed split and schedule, and a status checklist.
   Update it after every milestone so any session can pick up where this one stopped.
3. Environment check, and fix what you can yourself:
   - git pull;
   - python3 pipeline/taxonomy.py fetch;
   - python3 pipeline/avatars.py list (Richard and Terry poses must exist);
   - brand/assets/photos/ and the Axiforma fonts are present;
   - .private/kie.env exists (never print it);
   - Playwright + Chromium installed;
   - `gh auth status`.

   If the private kit is missing, say exactly which files are missing in one line and continue with
   everything that doesn't need them.
4. Date sanity: compute every post's publish date and time first (1 post per profile per day,
   consecutive, weekends included; Srinath 10:00 ET; company, Richard, Terry 10:00 UK). A post dated
   after the CTA event must use FALLBACK_CTA, and nothing may promote a past event. If CTA_SHARE can't
   be met with a still-future event, flag it once at the top of your first report and use FALLBACK_CTA.

## 1. Research and ideation
- Produce exactly TOTAL_POSTS ideas. Give MUST_COVER items first priority, then IDEATION_INPUTS and
  EXTRA_CONTEXT. Then fresh research: current Databricks / Snowflake / cloud cost and platform news from
  the last 30 days, release notes, pricing changes, benchmarks, analyst data, and practitioner pain
  points.
- For social sources use Agent Reach only (li-harvest, r.jina.ai). Verify every fact at its primary
  source and save it with its URL to corpus/research/<today>-verified-facts.md. Mark weak facts
  UNVERIFIED and don't use them.
- Every idea gets:
  - the profile;
  - the hook (first line as it will read);
  - 1 to 2 lines on what's inside;
  - the format;
  - CTA yes/no;
  - its sources.

  Fit each profile's voice (PLAYBOOK §1, corpus/voice.md). Srinath: 1 leadership to 1 technical.
- No duplicate angles: check the registry AND every idea in queue/posts.json. Ideas must be sharper
  and more specific than the previous batch: a real number, a real mechanism, a real story.
- At least CTA_SHARE are CTA posts, ordered as a countdown within each profile.
- Save to ideas/ideas-<today>-b<BATCH_NUMBER>.md. If IDEA_APPROVAL = yes, show the list and wait.
  Otherwise continue.

## 2. Sample matching (one unique creator sample per post)
- Run `python3 pipeline/taxonomy.py unused`. Match each idea to the sample whose format, layout
  archetype and copy structure fit it best (`taxonomy.py show <ID>` for the full breakdown). No sample
  may be used twice in this batch or reused from any earlier batch while unused samples remain.
- Study each matched sample's media and copy closely (open its Post URL through Agent Reach /
  r.jina.ai, and its preview links). Write what you're borrowing into the post's sample.what.
- Put the post map (id, profile, date, idea, sample, format, CTA) in the BUILD_STATE file.

## 3. Copy
- Write each post with the matching template from the owner's prompt doc (Experiential Story,
  Carousel, Thought Leadership, Repurposed Slidepost, News Post, Case Study, Viral Quotes) or the
  sample's own structure if that's stronger. Record which in copy_basis.
- Apply every rule in PLAYBOOK §2:
  - no em/en dashes;
  - Srinath's hard rules ("up to", "platform bill", no client names, no tick lists);
  - numbers_for_signoff lists every number in Srinath's posts;
  - the cold-reader rule (introduce people, no internal names, no relative dates that are wrong on
    the publish date).
- CTA posts: carousel last slide = CTA. The first comment has a personalised CTA line that fits the
  post, plus the link. Non-CTA posts: first comment adds value or is "".
- British spelling for company, Richard and Terry. Srinath: simple, story-first, kind, technical.

## 4. Media (the most important quality milestone)
- Build each asset in assets/b<BATCH_NUMBER>/<ID>/ as image.html, slide-01.html... or a build.py
  that writes them. Paths are 3 levels up: ../../../pipeline/brand.css,
  ../../../brand/assets/..., ../../../.private/avatars/...
- Brand per PLAYBOOK §3:
  - website palette and fonts;
  - logo top right;
  - the "Srinath Reddy - Founder & CEO" name line where Srinath appears;
  - his real photo only;
  - Richard and Terry only from the stored avatar poses (never regenerate);
  - no filler furniture;
  - a source line only where a number is cited.
- Match the sample's design sophistication, not just its layout. Custom illustrations may use
  pipeline/kie.py (cached). Carousels: one idea per slide, a strong cover, the CTA slide last for
  CTA posts.
- Render: python3 pipeline/render.py assets/b<N>/<ID>. Open out/_sheet.png and each PNG, and
  critique it against the sample:
  - hierarchy, legibility at phone size, density, alignment, colour, craft;
  - overflow, typos, dashes, filler, accuracy vs sources.

  Fix and re-render until it's genuinely at the sample's level.
- After each profile's assets pass your own loop, run a second-model critique (the `critic`
  subagent, or a fresh model given the PNGs + sample breakdown + copy). Fix every real issue.

## 5. Assemble and publish, one profile at a time
- Add the batch to queue/posts.json:
  - a batches[] entry {id, title "Batch N", dates "Thu 8 Oct to Sat 17 Oct 2026"};
  - one post record per post (schema in PLAYBOOK §6), batch "<N>", media.src "b<N>/<ID>".
- After each profile (company, then srinath, richard, terry):
  - run `bash pipeline/deploy.sh "Batch <N>: <profile> ready"`;
  - wait ~60s;
  - verify the live cache-busted URL with Playwright: the Batch N dropdown with 4 profile links,
    that profile's posts render, 0 broken images, 0 em/en dashes, sync badge "✓ All saved";
  - look at the screenshot yourself;
  - post the link in chat with a one-line status, and continue without waiting.

## 6. Final verification (all must pass before you say done)
Run the PLAYBOOK §10 checklist item by item and report each as pass/fail with evidence. It covers:
- post count and split;
- dates and times;
- CTA share and event dates;
- sample uniqueness;
- sources;
- numbers_for_signoff;
- dashes (posts.json + rendered media);
- filler;
- name lines;
- overflow;
- the second-model critique;
- the live site check.

Never delete rows in the review sheet. Remove test items with retract events (PLAYBOOK §7).

## 7. Close out
- Add a "Batch <N>" section to corpus/used-content-registry.md (every angle).
- Mark BUILD_STATE_B<N>.md complete.
- Commit the engine repo on a branch `batch-<N>` and push it. Never commit .private/, photos or
  fonts. Scan the staged diff for secrets and dashes first. Open a PR.
- Final message to the owner:
  - the cache-busted review URL;
  - posts per profile, the CTA count and %;
  - numbers awaiting Varadha's sign-off;
  - any UNVERIFIED items dropped;
  - anything that needs a human (one line each).

Only the review URL is for the owner to click; do everything else yourself.
```
