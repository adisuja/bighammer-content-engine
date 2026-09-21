# BH.ai Content

Content ideation → research → creation engine for **BigHammer.ai**. LinkedIn first.

**Status: grounding + spec complete. Build not started.** This repo currently holds the
verified source corpus, brand tokens, the spec, and the imported format research. The queue,
the matcher, the renderer and the studio interface are specified but not yet written.

Read [SPEC.md](SPEC.md) first, then [PROJECT_RULES.md](PROJECT_RULES.md).

---

## The three elements

| # | Element | Where | State |
|---|---|---|---|
| 1 | Content idea + the research on it | `ideas/` | Schema specified; idea bank imported to `corpus/sheet/idea-bank.md` |
| 2 | Format-skeleton extraction + idea↔format matching | `formats/` | **Skeletons largely already exist** in `~/content-engine` (56 measured `FORMAT_DNA.json`). The *matcher* is the missing piece |
| 3 | Creation queue + visual preview interface | `queue/`, `studio/` | Specified, not built. Target: GitHub Pages, iPhone-frame LinkedIn iOS preview |

## Layout

```
SPEC.md              the spec - goal, gates, verification plan, slice 1
PROJECT_RULES.md     intended CLAUDE.md (see note inside)
corpus/              GROUND TRUTH - nothing ships unless it is sourced here
  facts.md           every publishable claim + its source. The anti-hallucination gate
  blogs-batch1.md    9 LinkedIn blogs by Srinath Reddy - the voice reference
  deck-masterclass-v3.md   45-slide webinar deck, text per slide
  sheet/             extracts from the research spreadsheet:
    design-dna.md        11 Craft Laws + archetype library, from a 155-carousel audit
    format-analysis.md   76 per-post teardowns, 29 cols incl. 8 Design dimensions
    idea-bank.md         titled idea list with clusters and sources
    research-radar.md    ranked trending-topic table
    content-ideation.md  founder-interview framework for story mining
brand/tokens.json    palette, type, canvas sizes, voice rules
ideas/ formats/ queue/ studio/ pipeline/     (scaffolded, empty)
```

## Non-negotiables

1. **No claim without a row in `corpus/facts.md`.** Numbers must be traceable.
2. **No draft without a matched format.** Element 2 is a gate, not a suggestion.
3. **Voice is Srinath Reddy's** - concede the tool is good, then name the cost problem; blame
   absent guardrails, never engineers. See `brand/tokens.json` → `voice`.
4. **No em dashes** - use `" - "`, matching the existing BigHammer preview sites.
5. **Links are verified visually, not by status code.** `dataopsmasterclass.com` returns HTTP
   200 while serving a stale June date.

## Key facts pinned

- Next webinar: **Thursday 15 October 2026, 12:00 PM ET** (owner-confirmed 2026-09-21). The
  registration site still serves an old June date - every link unfurl shows it. Fix at source.
- Brand: Garet Bold/Regular + DM Sans; magenta `#FE0178` primary, violet `#5312D5`, orange
  `#FF6A36`, lavender `#BA99FF`, green `#00AF4E` **reserved for savings/positive only**.
  Derived from the deck - the Figma file was not readable (view-only access).

## Prior work this builds on

- `~/content-engine` - 56 format DNA directories, `INDEX.json`, a render engine and 49 carousel
  components, 450+ exemplar images, 106KB of post-copy templates. **Import, do not rebuild.**
- `~/BigHammer Misc/_shared/` - iPhone-frame shell and LinkedIn iOS renderer used by the five
  existing channel preview sites. The studio reuses these.

Not in this repo: a target-brand list that lives in the source spreadsheet but is unrelated to
content work.
