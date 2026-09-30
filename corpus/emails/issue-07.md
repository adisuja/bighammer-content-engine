# Email series - Issue 7 (source: ~/Downloads/Email_07.pdf, added 2026-09-30)

Issue 7, Which of your jobs should stay on Databricks?
Hi {{first_name}},
"Should we move off Databricks?" is the wrong question. It forces an all-or-nothing answer, and neither
answer is right.
The better question is: which jobs?
Why everything ends up in one place
Databricks is usually adopted for the work it's best at: machine learning, streaming, complex large-scale
processing. Then the simple nightly ETL lands there too, because that's where the data is. Then the
next batch job, because the pipelines are already there. Over time, everything runs on the same
platform at the same rates, whether it needs to or not.
The number
[APPROVED EXAMPLE: e.g. "In one assessment, X of Y jobs were classified as migration
candidates."]
Check it yourself this week
For your 20 most expensive jobs, note:
 Task types: notebook, Python, JAR, SQL, DLT pipeline, ML.
 Shape: how many tasks, and how many dependencies between them.
 Platform features in use: Photon, serverless, GPUs, streaming.
 Databricks-only code: dbutils, Databricks SDK calls, or other APIs that only exist on Databricks.
How we sort them
We score every job on two things: how complex it is, and how dependent it is on Databricks-specific
features. That gives five outcomes:
 Keep on Databricks: heavily dependent (ML, DLT and similar). It's where they belong.
 Migrate: simple and low-dependency. A candidate to run elsewhere.
 Optimize, then evaluate: complex but low-dependency. Tune it first, decide later.
 Evaluate: in between, or not enough information yet.
 Defer: too small in cost to be worth moving now.
Every classification comes with its scores and the reasons behind them.
What good looks like
 Decisions made job by job, never platform-wide.
 ML and deeply integrated work stays where it earns its price.
 Simple, low-dependency batch jobs are reviewed as candidates to move.
How the assessment shows this
The connected assessment classifies each job into one of the five groups, with its complexity and
dependency scores and the reasons. For jobs that should move, BigHammer Migrate converts Scala
JAR and PySpark wheel jobs to run on GCP Dataproc, replacing Databricks-specific code such as

dbutils widgets and table-name-based Delta access.
[SCREENSHOT: complexity vs. dependency quadrant from the connected dashboard]
[Run the offline assessment]  ·  [Book a 30-minute walkthrough]
Next issue: how to prove a migrated job matches the original before you switch anything off., The BigHammer team
---
