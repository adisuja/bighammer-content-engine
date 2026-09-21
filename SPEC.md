# BH.ai Content — Spec v0.1

**Status:** awaiting owner confirmation on 3 open decisions (bottom of file).
**Written:** 2026-09-21.

---

## The goal (not the task)

The task is "a content engine." The **goal** is: *Srinath and Glenn approve and ship
platform-ready content without a design or copy round-trip, and every claim in it survives
scrutiny from a Databricks-literate data leader.*

Everything below is judged against that, not against "did we generate posts."

**Definition of done for the whole system:** the owner opens one URL on a phone, swipes
through a queue of finished posts rendered exactly as the audience will see them, taps
Approve or Reject with a reason, and the approved item is publishable as-is - copy, carousel
images, hashtags, link - with zero further work.

---

## The three elements (owner's words, made concrete)

### Element 1 — Idea + research
One file per idea: `ideas/NNN-slug.json`.

```
id, slug, title, angle, audience, funnel_stage, source_refs[], research[], hooks[], status
```

- `source_refs[]` — every factual claim points at a row in `corpus/facts.md`. A claim with no
  ref cannot enter the queue. This is the anti-hallucination gate.
- `research[]` — external signal gathered per idea (competitor posts on the theme, Databricks
  pricing/docs changes, what's landing in the niche right now). Fetched via the Agent Reach
  path, never direct-scraped.
- `hooks[]` — 3-5 candidate opening lines, scored, one selected.

Idea supply, in priority order: (a) the 45-slide deck - each waste pattern, poll and metaphor
is an idea; (b) gaps against the 9 batch-1 blogs; (c) research-surfaced timely angles.

### Element 2 — Format skeleton extraction + matching
`formats/library.json`. A **format** is a *structure stripped of its content*, extracted from a
sample you rate as good:

```
id, name, type (carousel | single-image | text | video-script),
platform, panels[ { role, char_budget, visual_rule } ],
when_to_use, evidence (link to the sample it came from)
```

Two jobs:
1. **Extract** — given a sample, reverse-engineer its skeleton into the schema above.
2. **Match** — every idea is scored against every format on angle, proof density, funnel stage
   and panel count. The engine proposes a ranked top 3 and commits to one, with the reason
   written into the queue item. *No idea ever gets drafted without a matched format.*

> **Element 2 already substantially exists — we import, we do not rebuild.** Verified
> 2026-09-21 in `~/content-engine`:
>
> | Asset | What it is |
> |---|---|
> | `research/world-class/formats/` | **56 format directories**, each with a `FORMAT_DNA.json` measured from real decks — `role_sequence`, `ground`, `devices`, `field_relationships`, `whitespace`, `skeleton_law_audit`, plus an explicit `confidence` block that names its own defects |
> | `research/world-class/formats/INDEX.json` | 11,723-line master index across all 56 |
> | `research/formats-factory/taxonomy.json` | 52 varieties with tier, lane, exemplar, prompt variables |
> | `backend/app/formats/craft.py` + `recipes/components/` | 39,941-line render engine + 49 carousel components |
> | `research/formats-factory/media/` | 450+ exemplar images |
> | `research/world-class/postcopy/OWNER_PROMPT_DOC.md` | 106KB of hook formulas and copy templates |
>
> Plus the **Design DNA playbook** in your sheet (`corpus/sheet/design-dna.md`): 11 Craft Laws,
> an archetype library, repeating micro-structures, and four per-creator house systems,
> distilled from a 155-carousel audit. And the **LinkedIn Creator Taxonomy** tab: 76 per-post
> teardowns (Harry Dry 48, Austin Belcak 28) across 29 columns including 8 `Design ·`
> dimensions — extracted to `corpus/sheet/format-analysis.md`.
>
> **So the real element-2 work is not extraction. It is (a) selecting the subset of the 56 that
> fit a B2B data-leader audience, (b) re-skinning them to BigHammer brand tokens — the source
> DNA is ColdIQ navy / Harry's acid-green, not BigHammer magenta — and (c) building the
> idea→format matcher, which does not exist yet.**

### Element 3 — Creation queue + visual interface
`studio/` — a static site, published free on GitHub Pages, sibling to the five existing
channel preview sites.

Queue stages: `Idea → Researched → Matched → Drafted → Designed → Review → Approved → Scheduled`

The interface:
- **Queue board** on the left - every item, its stage, its matched format, blockers.
- **Phone preview** in the centre - an iPhone frame rendering the post exactly as the platform
  shows it, reusing `_shared/linkedin.js` from the existing sites (same fidelity as
  `adisuja.github.io/bighammer-email-sequences`): collapsed feed card, "…see more" expansion,
  swipeable carousel with real rendered panels, hashtag styling, link unfurl.
- **Evidence drawer** - for any highlighted claim, the corpus row backing it.
- **Approve / Reject with reason** - captured in the browser and exported as a JSON patch the
  pipeline merges back into the repo.

---

## Pipeline, with the gate at each stage

| # | Stage | Gate to pass (fails = stays put) |
|---|---|---|
| 1 | Ideate | Has an angle, an audience and ≥1 corpus-backed claim |
| 2 | Research | ≥3 external signals; claims re-verified against source |
| 3 | Match format | Fit score ≥ threshold; reason recorded |
| 4 | Draft | Every number traceable; banned-phrase list clean; hook chosen from scored set |
| 5 | Design | Panels render at brand tokens; no text overflow; contrast ≥ 4.5:1 |
| 6 | Verify | Automated: link health, claim-to-corpus, voice check. Then the `critic` subagent |
| 7 | Review | Owner approves in the studio |
| 8 | Ship | Exported as platform-ready bundle (copy.txt + panels/*.png + metadata) |

---

## Decisions I have already made (tell me if any is wrong)

- **Host = GitHub Pages**, new public repo `adisuja/bighammer-content-studio`, matching the five
  existing preview sites. Free, no infra, you already review this way.
- **Review state = browser-local + export.** A static host can't persist writes; approvals live
  in `localStorage` and export as JSON I merge. No account, no backend, no cost.
- **Brand tokens derived from the deck, not Figma.** The Figma file `TD9z8ciTPCECHOm8FffX6c`
  returned *"you don't have edit access"* - the MCP cannot read its variables. I extracted the
  real palette and type from the 45-slide deck instead (see `brand/tokens.json`): Garet
  Bold/Regular + DM Sans, magenta `#FE0178` primary, violet `#5312D5`, orange `#FF6A36`,
  lavender `#BA99FF`, green `#00AF4E` reserved for savings. Grant editor access and I'll
  re-derive from source.
- **Carousel panels rendered as HTML→PNG**, not Figma. Reproducible, diffable, regenerable when
  copy changes. Figma stays the design reference.
- **Research goes through Agent Reach**, per standing rule - never direct scraping.

## Verification plan (Layer 2)

Eval criteria fixed *before* building:
1. **Fidelity** - a screenshot of the studio preview is indistinguishable from the real
   LinkedIn iOS app at the same width. Checked visually, both widths, console clean.
2. **Traceability** - 100% of numbers in any drafted post resolve to a `corpus/facts.md` row.
   Automated check; a miss fails the build.
3. **Voice** - drafts pass the banned-list and carry ≥2 of the 5 signature moves in
   `brand/tokens.json`.
4. **Format discipline** - no queue item reaches Drafted without a matched format and a
   recorded reason.
5. **Independent critic** - the `critic` subagent (Codex) reviews the skeleton schema and the
   first 3 finished posts adversarially before you see them.
6. **External signal** - every link curl-tested *and* opened visually. HTTP 200 is not proof;
   the webinar page proves it - it returns 200 while serving a stale date.

## Slice 1 (what I build first, end to end, before scaling)

Three ideas → three formats → three finished LinkedIn posts (1 carousel, 1 single-image,
1 text) → live in the studio at a URL you open on your phone. Narrow on purpose: it proves
the whole spine before I mass-produce.

---

## OPEN — needs your call

1. **Platforms.** LinkedIn is the only channel with existing content and a built renderer.
   "Different social platforms" - which else, and in what order?
2. **Format library.** You said you'd hand me a list of good formats. Send it and I extract
   skeletons from it; otherwise I seed the library from your own 9 carousels plus a set of
   proven B2B structures, and you prune.
3. **The webinar date is broken three ways.** Served HTML says *Thu 18 Jun 2026 11:00 ET*, the
   deck cover says *1 PM EST*, and the prior build used *Thu 15 Oct 2026 12:00 ET*. Every link
   unfurl shows the stale one. No CTA content can ship until this is settled.
