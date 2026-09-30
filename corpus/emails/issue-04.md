# Email series - Issue 4 (source: ~/Downloads/Email_04.pdf, added 2026-09-30)

Issue 4, What a Databricks assessment actually involves
Hi {{first_name}},
Most teams we speak to want a Databricks cost assessment. Many of them stall before they start.
Security wants to know what gets accessed. Procurement wants to know what's being installed. And
nobody has time for weeks of workshops.
So here is exactly what our offline assessment involves.
The short version
1 notebook · 7 system tables read · 90-day window · 0 credentials shared
How it works
1. Import one notebook into your Databricks workspace.
2. Attach a small classic cluster. A single-node cluster is enough (about 4 cores and 16 GB RAM).
Serverless and SQL warehouses aren't used.
3. Set two values: your workspace ID and a folder the cluster can write to.
4. Run all. The notebook first checks it can read the system tables it needs and write to your folder. If a
permission is missing, it tells you which one.
5. Send us the zip. It contains CSV extracts only. No SQL, no secrets, no credentials.
What it reads
Read-only access to seven system tables covering jobs, job runs, task runs, billing usage, list prices,
clusters, and cluster utilisation. Nothing is written to your workspace except the output folder you
choose.
What your security team will ask
 Does BigHammer get access to our workspace? No. The notebook runs under your own cluster
identity.
 Is anything installed? No. It's a single notebook.
 What data leaves our environment? Aggregated usage, run and cost data in CSV form, which you
can inspect before sending.
 Can it change anything? No. It only reads system tables.
What you get back
 Total Databricks cost over 90 days, at published list prices.
 Cost by billing product.
 Spend traced to jobs versus untraced.
 Failed-job cost, measured.
 Per-job and per-run cost tables.
 Average worker CPU and Photon usage share.
[SCREENSHOT: offline assessment overview from a real upload run]
If you'd rather not run it yourself, book a walkthrough and we'll do it with you on a call.

[Run the offline assessment]  ·  [Book a 30-minute walkthrough]
Next issue: why we lead with measured numbers, and how to read any savings claim, including ours., The BigHammer team
---
