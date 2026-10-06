# BigHammer brand + design guidelines (working version, 2026-09-30)

Status: **provisional.** The owner will walk through specific design examples next. The Figma file
(TD9z8ciTPCECHOm8FffX6c "BigHammer Webiste_Glenn") opens view-only but its canvas did not render
in the headless browser pane; it contains pages **Website**, **Remarketing banners**,
**Databricks pdf** and frames incl. Assets, Healthcare Page, Cost Page_revamped, Databricks page,
Migration & Healthcare, Pop up design, Final Screens. Re-derive from Figma once readable.

## 1. Source of truth, in order
1. Srinath's explicit review comments (below) - these win.
2. The live website bighammer.ai (Srinath: "use our standard colors which we use on website").
   Extracted from computed styles on 2026-09-30.
3. Figma file (pending - see above).
4. "Architect's Notebook" design system in the Consolidated doc - partially conflicts (see 5).
5. brand/tokens.json (deck-derived, 2026-09-21) - **superseded** for colour + type.

## 2. Srinath's rules for images (from comments on rejected posts)
- **BigHammer.ai logo on every image, top right.** Asset: `brand/assets/bighammer-logo.svg`.
- Name line: **"Srinath Reddy - Founder & CEO"** (never "Data Architect").
- Use the **website's standard colours**.
- No AI-generated image of Srinath ("obviously no good" - Glenn, Batch post 5).
- Glenn signed off Srinath posts "bar the yellow & colour scheme" -> treat yellow as disputed.

## 3. Website palette (live, measured)
| Role | Hex | Where seen |
|---|---|---|
| Ink (text) | #141414 | headings/body on light |
| Dark surface | #0D0D14 (gradient #16161F -> #0B0B11) | dark sections |
| Light surface | #FFFFFF / #F0F4FA / #E8EAEE | sections, cards |
| Neon green | #00FF89 (also 5-20% tints) | accents, highlights on dark |
| Electric violet | #5600EF (gradient #6A16FF -> #5600EF -> #3D00AD) | CTA/feature blocks |
| Magenta | #FE0079 | accent text |
| Yellow | #FCFF00 | highlight blocks (disputed - see 2) |
| Lime | #B7FF6E | small highlight |
| Red | #E2231A | warning accent |
| Muted grey | #7A7A85 | secondary text |

## 4. Website type
- Display/headings: **Axiforma** 700-800 (H1 ~75px, H2 40px).
- Body/UI: **Poppins** 400/500/600.
- Secondary headings on dark: **Geist** 700. Code/labels: monospace.

## 5. Open conflicts to resolve with the owner
- Architect's Notebook says warm paper #FCFBF8, IBM Plex, muted accents, logo small bottom corner
  in mono; Srinath says website colours + logo top right. Website wins on colour + logo until told
  otherwise; Architect's Notebook ideas (blueprint lines, mono labels, whitespace, system-diagram
  frameworks) may still apply as layout language.
- tokens.json magenta #FE0178 vs website #FE0079 (use website).

## 6. No filler furniture (owner rule, 2026-10-01)
Never add decorative header/footer labels inside images or carousel slides: no kicker tags
("CHEAT SHEET", "NEW IN DATABRICKS", "A SMALL CONFESSION"), no category/byline strips
("Data engineering leadership | Srinath Reddy"), no "save this / share with your team / swipe"
footers, no slide numbers, no repeated "BigHammer.ai" sub-lines under names.
Allowed: logo top right, the required name line, the content itself, the webinar CTA, and a
source line only where the image cites a number.
