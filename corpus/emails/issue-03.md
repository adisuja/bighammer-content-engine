# Email series - Issue 3 (source: ~/Downloads/Email_03.pdf, added 2026-09-30)

Issue 3, What your failed jobs really cost
Hi {{first_name}},
A nightly job fails at 3 AM. It retries. It fails again. Eventually it succeeds, the incident closes, and
everyone moves on.
The compute from the failed attempts is still on the bill.
Why failure cost stays invisible
Failed, timed-out and retried runs consume compute until they stop. A job with no timeout can run for
hours before it gives up. A job with generous retries can repeat that several times in one night.
Reliability tooling tracks the failure. It almost never tracks the cost of the failure. So the number that
matters to finance never reaches the people who could fix it.
The number · Measured
[APPROVED EXAMPLE: e.g. "Failed-run cost over 90 days: $X, or Y% of traceable job spend."]
This is one of the few Databricks cost figures that needs no assumptions. The runs happened, they
failed, and they were billed.
Check it yourself this week
 Runs with a result state of FAILED or TIMED_OUT in system.lakeflow.job_run_timeline
over the last 90 days.
 The cost of those runs, by joining them to billing usage.
 The jobs with the most repairs or retries.
 Which of your jobs have no timeout set at all.
What good looks like
 Task timeouts set relative to normal runtime, so a stuck job stops early.
 Retries capped, with a clear rule for when a failure needs a human.
 Fail fast on bad or missing inputs, before the expensive work starts.
 Alerts that include what the failure cost, not just that it happened.
How the assessment shows this
Failed-job cost over 90 days is a measured figure in both the offline and the connected assessment.
The runs table lets you drill into individual failed runs and see exactly what each one cost.
It's usually the easiest finding to act on, because the fix is configuration, not migration.
[Run the offline assessment]  ·  [Book a 30-minute walkthrough]
Next issue: what running the assessment actually involves, and the questions your security team will
ask., The BigHammer team
---
