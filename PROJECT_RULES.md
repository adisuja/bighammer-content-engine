# BH.ai Content — project rules

> **Staged.** This is the intended `CLAUDE.md` for the project. The `protect-rules-files` hook
> blocked writing it directly (ask-first tier, by design). Say the word and I'll promote it
> with `CLAUDE_ALLOW_RULES_EDIT=1`.

Content engine for BigHammer.ai. Extends the global `~/.claude/CLAUDE.md`; never overrides it.

## Non-negotiables

1. **No claim without a corpus row.** Every number, percentage, customer name or dollar figure
   in generated content must resolve to a row in `corpus/facts.md`. If it isn't there, it
   doesn't ship - research it into the corpus first, with its source.
2. **No draft without a matched format.** Element 2 is a gate, not a suggestion. An idea goes
   `Matched` before `Drafted`, and the match reason is written into the queue item.
3. **Voice belongs to Srinath Reddy.** Copy is signed by him. Concede the tool is good before
   naming the cost problem; blame absent guardrails, never engineers. See `brand/tokens.json`
   → `voice`.
4. **No em dashes.** Use `SEP` (" - "), matching the five existing preview sites.
5. **Research goes through Agent Reach.** Never curl/playwright LinkedIn, X, Reddit et al.
6. **Links are verified visually, not by status code.** `dataopsmasterclass.com` returns 200
   while serving a stale June date. 200 is not proof.

## Layout

```
corpus/    ground truth - facts.md is the gate; deck + blogs are voice samples
brand/     tokens.json (deck-derived palette/type), render CSS
ideas/     element 1 - NNN-slug.json, idea + research + hooks
formats/   element 2 - library.json, skeletons extracted from good samples
queue/     element 3 - queue.json, one entry per item with stage + history
studio/    the visual interface, published to GitHub Pages
pipeline/  scripts: extract, match, draft, render, verify, export
```

## Reused code

The iPhone-frame shell and the LinkedIn iOS renderer come from
`~/BigHammer Misc/_shared/` (`core.js`, `core.css`, `linkedin.js`, `linkedin.css`). They are
**copied** into `studio/`, not symlinked - same convention as the five channel preview sites.
Edit in `_shared`, re-copy, bump `?v=` in `index.html`.

## Publishing

`studio/` publishes to GitHub Pages from a public repo under `adisuja`. After any change:
rebuild, re-copy shared files, bump `?v=`, commit, push, then open the **cache-busted** URL
myself and verify visually before handing it over. The owner's only job is clicking the link.
