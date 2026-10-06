# Email series - Issue 2 (source: ~/Downloads/Email_02.pdf, added 2026-09-30)

Issue 2, Most of your Databricks spend can't be traced to
 a job
Hi {{first_name}},
The bill went up this quarter. Someone asks which team or pipeline caused it. The room goes quiet.
That's not a people problem. It's a visibility problem, and it's more common than most teams expect.
Why so much spend has no job attached
Every row in system.billing.usage carries metadata. When work runs as a Databricks job, that
metadata includes a job ID and a job run ID. When it doesn't, the link is missing.
The usual reasons:
 Scheduled work running on interactive (All-Purpose) clusters instead of job clusters.
 Shared clusters used by several teams at once.
 Notebooks and ad-hoc analysis that never became jobs.
 Clusters with no owner or cost-centre tags.
 Usage rows that don't match a published list price, so they can't be priced cleanly.
The result is a large slice of spend you can see but can't explain.
The number · Measured
[APPROVED EXAMPLE: e.g. "X% of 90-day spend traced to a job in one workspace we
assessed."]
Untraced does not mean wasted. It means nobody can say what it bought.
Check it yourself this week
 What share of your billing usage rows have usage_metadata.job_run_id set.
 Which scheduled jobs run on All-Purpose clusters rather than job clusters.
 How many clusters have no owner or cost-centre tag.
 How many usage rows have no matching list price.
What good looks like
 Scheduled production work runs on Jobs compute, so every run is traceable (and billed at a lower
rate than All-Purpose).
 A small required tag set (owner, cost centre, environment) enforced by cluster policy.
 A coverage target, such as "most spend traceable to a job", reviewed monthly.
How the assessment shows this
The offline report shows spend traced to jobs, in dollars and as a percentage, right next to your total
cost. The connected assessment goes further and shows untraced spend and missing-price rows as
separate visibility items. We never count them as savings, because they aren't proven waste.
[Run the offline assessment]  ·  [Book a 30-minute walkthrough]
Next issue: some of the spend you can trace went to jobs that failed. We'll show you how to add it up., The BigHammer team
---
