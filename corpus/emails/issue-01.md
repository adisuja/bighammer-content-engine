# Email series - Issue 1 (source: ~/Downloads/Email_01.pdf, added 2026-09-30)

Issue 1, Your Databricks renewal is coming. Do you have
 evidence?
Hi {{first_name}},
At some point in the next few months, someone will ask your team a simple question: what are we
getting for our Databricks spend?
Usually that question arrives just before a renewal or a commit discussion. And usually the only answer
on the table is the invoice total.
A total is not evidence. It tells you what you spent. It doesn't tell you which jobs drove it, what's growing,
what's failing, or what could run somewhere cheaper. Without that, the conversation is about the price.
With it, the conversation is about your workloads, and that's a much stronger position.
Why the invoice can't answer it
Databricks rolls usage up by SKU on the invoice. The link between spend and the jobs and runs behind
it lives in your workspace's system tables: billing usage, list prices, and the job run timeline. Most teams
never join them, so the detail is there but unused.
The number · Measured
[APPROVED EXAMPLE: e.g. "In one workspace we assessed, the top 10 jobs accounted for X% of
spend traceable to jobs over 90 days."]
Check it yourself this week
 Your 90-day list cost broken down by billing product and SKU (system.billing.usage joined to
system.billing.list_prices, matched on the price's valid time range).
 Your top 10 jobs by cost over the same window.
 How much of that window's spend went to runs that failed or timed out.
 What share of total spend you can actually trace to a job at all.
What a strong renewal position looks like
 A 90-day baseline you can defend line by line.
 A short list of your most expensive jobs, each with an owner.
 The cost of failed runs, stated separately.
 A view of which jobs genuinely need Databricks and which don't. That last point is your leverage.
How the assessment shows this
Our offline assessment gives you the first three in one report: total 90-day cost, cost by billing product,
spend traced to jobs versus untraced, failed-job cost, and per-job and per-run cost tables. Connecting
your workspace adds a classification of each job, from "keep on Databricks" to "migration candidate".
You run one read-only notebook in your own workspace and send us a zip. No credentials leave your
environment.
[Run the offline assessment]  ·  [Book a 30-minute walkthrough]

Next issue: most Databricks spend can't be traced to any job. We'll look at why that matters, and why it
isn't the same as waste., The BigHammer team
---
