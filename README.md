# BigHammer.ai LinkedIn content engine

Builds weekly batches of LinkedIn posts (company page, Srinath Reddy, Richard Lawrence, Terry Dhariwal):
research and ideas, creator-sample matching, copy, on-brand media, and a LinkedIn-iOS review site with
shared approvals and feedback.

- **Review site (all batches):** https://adisuja.github.io/bighammer-content-studio/
- **Start here:** [PLAYBOOK.md](PLAYBOOK.md), the binding rules and the definition of done
- **Make a new batch:** paste [prompts/new-batch.md](prompts/new-batch.md) into Claude Code and fill the inputs
- **Status:** Batch 2 (24 posts, 2 to 7 Oct 2026) is built and in review. See [queue/BUILD_STATE_B2.md](queue/BUILD_STATE_B2.md)

Quick commands:

    python3 pipeline/taxonomy.py unused          # creator samples not used by any batch yet
    python3 pipeline/render.py assets/b3/C1      # render an asset to PNG (dash + overflow guarded)
    bash pipeline/deploy.sh "Batch 3: ready"     # rebuild the studio and publish to GitHub Pages

Real-person photos, avatars, licensed fonts and API keys are not in git: see PLAYBOOK §9 (private team kit).
