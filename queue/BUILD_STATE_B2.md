# BUILD STATE: LinkedIn Batch 2 (24 posts)

Started 2026-09-30. Owner brief: 24 posts = 6 company, 6 Srinath, 6 Richard, 6 Terry. >=40% webinar CTA
(carousel last slide = CTA) + first comment with personalised CTA line + https://webinar.bighammerai.com/.
Each post matched to a UNIQUE sample from the LinkedIn Creator Taxonomy tab (Tantra <> Work Tracker sheet,
gid 349467685, CSV-exportable). Copy from the prompt doc (1adrCJ_..., 7 templates) or the sample's own copy
structure if better. Media on-brand (brand/brand-guidelines.md) at the sample's design sophistication.
Richard + Terry via kie.ai avatars (nano-banana-pro, 8 reference photos per generation); Srinath real photo.
Review site: GitHub Pages, LinkedIn iOS style (reuse ~/BigHammer Misc/_shared), 3 phones side by side,
profile order Company > Srinath > Richard > Terry, sidebar, swipe/zoom/See more, approvals (Glenn,
BigHammer team) + feedback persisted without backend, publish date/time (10:00 UK; Terry 10:00 ET - assumed).

## Post map (idea -> sample). CTA = webinar CTA + first comment.
| # | Profile | Idea | Sample | Format | CTA |
|---|---|---|---|---|---|
| C1 | Company | W3 7 system tables | AV44 dashboard (8 panels) | single infographic | yes |
| C2 | Company | W7 "which jobs?" 5 outcomes | AV35 true 2x2 quadrant | single infographic | yes |
| C3 | Company | W12 day-of webinar | AV08 webinar promo, cutout speaker | promo graphic | yes |
| C4 | Company | N6 legacy ETL map | AV28 masonry strategy cards w/ status bands | single infographic | no |
| C5 | Company | N8 three people do DE | AV40 3-circle Venn | single infographic | no |
| C6 | Company | N9 budgets + tags (moved to Fri 2 Oct) | AV26 vertical flowchart -> tiers | single infographic | no |
| S1 | Srinath | W1 Azure Standard tier auto-upgrade | AV19 editorial article stack | news mimicry image | yes |
| S2 | Srinath | W4 4 questions for any savings claim | AB21 fake-tweet quote card | quote card | yes |
| S3 | Srinath | W10 AirPods story | AB35 editorial founder photo | photo story | yes |
| S4 | Srinath | N1 layoffs fear (leadership) | HD49 hand-drawn crossing-curves chart | illustrated chart | no |
| S5 | Srinath | N4 Snowflake Gen2 math | AV20 comparison data table | infographic | no |
| S6 | Srinath | W8 Spark 4.0 silent bugs | AB34 dark tutorial carousel + UI/code shots | carousel | yes |
| R1 | Richard | W6 renewal = expansion opportunity | AB03 tweet card over lifestyle photo | quote/photo | yes |
| R2 | Richard | N5 Talend Open Studio retired | AB43 news-article screenshot mimicry | proof image | no |
| R3 | Richard | N2 two kinds of engineers | AB17 fake-tweet comparison carousel | carousel | no |
| R4 | Richard | N7 logic walks out the door | HD50 iceberg infographic | illustrated concept | no |
| R5 | Richard | N11 price all four bills | PC21 2-col masonry numbered cards | infographic | yes |
| R6 | Richard | W11 don't come if... | AV41 portrait carousel w/ avatar chip | carousel | yes |
| T1 | Terry | W2 cost-per-job report missing jobs | AB33 dark numbered carousel, green callout | carousel | yes |
| T2 | Terry | W5 15% CPU costs same as 90% | AV11 data-graphic-as-hero bar | infographic | yes |
| T3 | Terry | W9 poll | PC31 event-promo text + native poll | poll | yes |
| T4 | Terry | N10 serverless modes | PC34 two stacked comparison panels | infographic | no |
| T5 | Terry | N12 Genie free until 31 Jan 2027 | PC24 3-phase timeline | infographic | no |
| T6 | Terry | N3 AI benchmark honesty | HD40 surreal cover + % breakdown | carousel | no |
Dropped: N13 (needs Srinath story input). CTA count 12/24 = 50%.

## Status
- [x] Samples downloaded + studied (/tmp/bh/samples; taxonomy CSV at /tmp/bh/tax/tax.json)
- [x] Render kit: pipeline/brand.css, dark.css, light.css, render.py (HTML->PNG 2x, 1080 wide, overflow check)
- [x] Company 6/6 copy + media + critique loop (round 1 critic: C1 8/10, others 5.5-7 -> all fixes applied)
- [x] Review site live: https://adisuja.github.io/bighammer-content-studio/ (deploy dir ~/BigHammer Misc/content-studio-site, push = rsync studio/ + commit + push)
- [x] Srinath 6/6 (critic round applied: S3 re-matched AB35->HD05 phone-screen photo; S6 accuracy fixes; S4 chart recomputed; S5 wording)
- [~] Avatars: create-once library pipeline/avatars.py (manifest brand/avatars/manifest.json, files .private/avatars). Richard 8 poses DONE. Terry headshot DONE, other 7 poses pending. Terry role/voice still UNKNOWN.
- [x] Richard 6/6 (R4 Oct2, R2 Oct3, R3 Oct4, R1 Oct5 CTA, R5 Oct6 CTA, R6 Oct7 CTA)
- [x] Terry 6/6 (T4 Oct2, T5 Oct3, T6 Oct4, T1 Oct5 CTA, T2 Oct6 CTA, T3 Oct7 CTA poll). Terry = Terry Dhariwal, neutral practitioner voice, no employer, no BigHammer title claimed.
- [~] Final critic pass (R+T running) + all links verified

## Next
Richard R1-R6: samples AB03 AB43 AB17 HD50 PC21 AV41. Use avatars.path("richard", pose) only; never call kie for Richard again.

## Cadence (owner, 2026-10-01)
One post per day per profile, consecutive days from Fri 2 Oct to Wed 7 Oct. Srinath 10:00 ET; company, Richard, Terry 10:00 UK. Webinar posts land last in each run. No approval pauses. Introduce people on first mention in any caption or comment.

## Review panel v2 (owner, 2026-10-01)
Multi-person feedback feed + approvals as an append-only event log (studio/app.js). LIVE: shared Google Sheet store (see memory review-studio-shared-store); sync_url set in queue/posts.json. Verified two separate browsers see each other's notes.

## Next: Terry T1-T6 (UK 10:00, Oct 2-7). Samples AB33 AV11 PC31 PC34 PC24 HD40. Use .private/avatars/terry (headshot exists; create remaining poses once via pipeline/avatars.py create terry).
