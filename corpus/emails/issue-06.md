# Email series - Issue 6 (source: ~/Downloads/Email_06.pdf, added 2026-09-30)

Issue 6, Your clusters' CPU tells a story
Hi {{first_name}},
Somebody sized a cluster for a peak load months ago. Maybe during an incident, maybe for a one-off
backfill. The peak passed. The cluster size didn't.
It still runs at that size every night.
Why oversized clusters stay oversized
Cluster size and autoscaling settings get set once and rarely revisited. Classic compute is billed on
nodes and hours, not on how busy those nodes are. A cluster at 15% CPU costs the same as one at
90%.
The good news: Databricks already records what your clusters were doing. It's in
system.compute.node_timeline.
The number · Measured
[APPROVED EXAMPLE: e.g. "Average worker CPU across assessed job clusters: X%."]
Any dollar figure attached to right-sizing is Estimated.
Check it yourself this week
 CPU busy percentage per cluster: add cpu_user_percent and cpu_system_percent from
system.compute.node_timeline.
 Clusters that ran 30 minutes or more, averaged under 20% CPU, and stayed under 40% even at
their 95th percentile. Those aren't busy, they're oversized.
 Clusters where autoscale minimum equals maximum, which means autoscaling is effectively off.
 Interactive clusters with no auto-termination set.
Why the 95th percentile matters
An average can hide a spike. A cluster that averages 18% because it hit 95% for four minutes needs
better autoscaling. A cluster that never goes above 30% needs a smaller size. They're different fixes.
What good looks like
 Right-size from real utilisation, not from the size someone picked last year.
 Give autoscaling a real range.
 Auto-terminate interactive clusters.
 Review your top 10 clusters by cost every quarter.
How the assessment shows this
The offline report shows average worker CPU. The connected assessment applies utilisation thresholds
per run, flags workloads that are consistently under-used, and estimates a right-sizing opportunity for
each.
[Run the offline assessment]  ·  [Book a 30-minute walkthrough]
Next issue: which of your jobs should stay on Databricks, and which don't need to., The BigHammer team

---
