# External research - verified facts (2026-09-30)

Gathered by research subagents via WebSearch/WebFetch (docs, vendor pages, press) and a LinkedIn
scan via Agent Reach (li-harvest). Confidence: VERIFIED = read on primary page; LIKELY = secondary
or primary blocked; UNVERIFIED = do not publish. **Every number still needs Varadha's sign-off
before it ships (Srinath's rule).** Prices are list prices, US East, as of 2026-09-30.

## Databricks platform
| Fact | Conf. | Source |
|---|---|---|
| Azure Databricks Standard tier: remaining workspaces **auto-upgraded to Premium on 2026-10-01**; new Standard workspaces blocked since 2026-04-01; upgraded workspaces have ACLs disabled by default | VERIFIED | https://learn.microsoft.com/en-us/azure/databricks/admin/account-settings/standard-tier (dated 2026-09-11), .../account |
| AWS/GCP Standard tier ended 2025-10-01 | LIKELY | search summaries of Databricks docs |
| Community claim: upgrade = "at least 35%+ cost increase" for interactive | LIKELY (do not cite as fact) | community.databricks.com/t5/community-articles/the-end-of-an-era-azure-databricks-is-retiring-the-standard-tier/td-p/144848 |
| AWS per-DBU list: Jobs Classic $0.15 (Premium) / $0.20 (Ent); All-Purpose Classic $0.55 / $0.65; Jobs Serverless $0.35 / $0.45; ratio All-Purpose:Jobs **3.67x** Premium, 3.25x Enterprise | VERIFIED | https://www.databricks.com/product/pricing/lakeflow-jobs , https://www.databricks.com/product/pricing/datascience-ml |
| Photon: pricing pages say DBU emission 2.9x (Jobs page) vs 2x (Interactive page) - inconsistent, do not publish a single multiplier | VERIFIED text, conflicting | same |
| `usage_metadata.job_id` / `job_run_id` populated for serverless jobs and job compute, **not for jobs on all-purpose compute**; cost per job on all-purpose "not possible with 100% accuracy"; all-purpose and SQL warehouse runs "excluded from cost attribution" in cost-per-job queries | VERIFIED | https://docs.databricks.com/aws/en/admin/system-tables/billing , /jobs , /jobs-cost |
| System tables: billing.usage (365 d), billing.list_prices (indefinite), lakeflow.jobs, job_run_timeline, job_task_run_timeline, compute.clusters (365 d), **compute.node_timeline (90 d, minute granularity)**; compute tables exclude serverless + SQL warehouses | VERIFIED | https://docs.databricks.com/aws/en/admin/system-tables/ |
| New (2026-09-09, Beta): account-wide system table retention 30-3,650 days | VERIFIED | https://docs.databricks.com/aws/en/release-notes/product/2026/september |
| Jobs `timeout_seconds` default 0 = no timeout; `max_retries` default 0, -1 = retry forever; retries immediate unless interval set | VERIFIED | https://docs.databricks.com/api/workspace/jobs/create |
| Cluster policy can require a `COST_CENTER` tag "for the compute to launch"; can fix auto-termination | VERIFIED | https://docs.databricks.com/aws/en/admin/clusters/policy-definition |
| Serverless jobs: Standard mode startup 4-6 min, "up to 70% cheaper for some workloads" than Performance optimized (<1 min); same SKU/list price; configurable since 2025-04-14, GA 2025-06-10; API one-time runs 2026-09-11 | VERIFIED | https://docs.databricks.com/aws/en/jobs/run-serverless-jobs , release notes |
| **Budgets GA 2026-07-06**; Genie moved to pay-as-you-go 2026-07-08; **Genie One + Genie Agents billing paused, free through 2027-01-31** (2026-07-15) | VERIFIED | https://docs.databricks.com/aws/en/release-notes/product/2026/july |
| Databricks raised $5bn at $190bn valuation (2026-08-13), run-rate >$7bn | LIKELY | thenextweb.com/news/databricks-closes-5-billion-round-at-190-billion-valuation |

## Market / surveys
| Fact | Conf. | Source |
|---|---|---|
| Flexera State of the Cloud 2026: estimated wasted IaaS/PaaS spend **29%**; **85%** say managing cloud cost is top challenge | VERIFIED | https://www.flexera.com/blog/finops/cloud-cost-management-trends/ |
| State of FinOps 2026: **98%** of respondents manage AI spend (63% in 2025); n=1,192, $83B+ spend | VERIFIED | https://data.finops.org/ |
| Gartner: through 2026, orgs will abandon 60% of AI projects unsupported by AI-ready data (2025-02-26) | LIKELY | gartner.com newsroom 2025-02-26 |
| Gartner: >40% of agentic AI projects cancelled by end of 2027 (2025-06-25) | LIKELY | gartner.com newsroom 2025-06-25 |
| Gartner VP Analyst: by 2029 agentic data management will have automated **75% of data engineering workflows** (reported 2026-09-24) | VERIFIED | https://www.cioandleader.com/gartner-data-analytics-summit-2026-india-day-2-highlights/ |
| **"$207B agentic AI spend 2026, up 139%" (on the webinar page) - NOT traceable to Gartner.** Closest: Gartner $201.9B, +141% (2026-01-15) | UNVERIFIED / LIKELY | see research notes; **fix the landing page** |
| Uber CTO: AI coding budget "blown away already" (The Information, Apr 2026) | LIKELY | https://cio.com/article/4226223/the-wrong-million-tokens.html |
| Microsoft reportedly cancelled most internal Claude Code licences in one division (2026-05-14); officially "consolidation" | LIKELY | thenextweb.com/news/microsoft-claude-code-retreat-ai-cost |
| Fivetran 2026 benchmark: fragile pipelines + manual ops consume **53%** of engineering time (n=500, vendor survey) | VERIFIED | https://www.fivetran.com/blog/the-enterprise-data-infrastructure-benchmark-report-2026 |
| dbt State of Analytics Engineering 2026: 71% concerned about incorrect data reaching stakeholders; 72% prioritise AI coding vs 24% AI pipeline mgmt; 57% report rising warehouse/compute spend (n=363) | VERIFIED | https://www.getdbt.com/resources/state-of-analytics-engineering-2026 |
| Stack Overflow 2025: 84% use/plan AI; 33% trust accuracy, 46% distrust; 66% "almost right, but not quite" | VERIFIED | https://survey.stackoverflow.co/2025/ai |
| Spider 2.0 DBT track (68 tasks) best **65.6%** | VERIFIED (leaderboard read 2026-09-30) | https://spider2-sql.github.io/ |
| ELT-Bench-Verified (2026-03-31): extract/load **96%**, transformation **32.51%** (Claude Sonnet 4.5 + SWE-agent); original ELT-Bench baseline 37% / 1% | VERIFIED (paper HTML, 2026-10-01) | https://arxiv.org/html/2603.29399 |

## Legacy ETL, Snowflake, migration
| Fact | Conf. | Source |
|---|---|---|
| Salesforce completed Informatica acquisition **2025-11-18** | VERIFIED | salesforce.com/news/press-releases/2025/11/18/... |
| PowerCenter 10.5 standard support ended **2026-03-31**; paid extended support to 2027-03-31 | LIKELY - confirm in Informatica lifecycle guide | https://dataladder.com/informatica-powercenter-end-of-life-migration-strategy/ |
| Talend Open Studio retired **2024-01-31** (Qlik: "diminishing community adoption") | VERIFIED | https://www.qlik.com/us/products/talend-open-studio |
| IBM completed StreamSets + webMethods acquisition **2024-07-01**; StreamSets now part of IBM watsonx.data integration | VERIFIED / LIKELY | newsroom.ibm.com 2024-07-01 |
| Cloudera: CDH and HDP past end of support; Cloudera on-prem 7.3.1 EoS Dec 2026, 7.1.9 LTS Oct 2028 | VERIFIED (page partly stale) | https://www.cloudera.com/services-and-support/support-lifecycle-policy.html |
| Snowflake: billed per second with **60-second minimum on every resume**; default AUTO_SUSPEND 600 s; cloud services free up to 10% of daily warehouse credits | VERIFIED | Snowflake Credit Consumption Table (eff. 2026-09-30); docs.snowflake.com cost pages |
| Snowflake **Gen2 warehouses: 1.35x credits/hr on AWS/GCP, 1.25x on Azure**; not default | VERIFIED | same |
| Spark 4.0: `spark.sql.ansi.enabled` **on by default** (invalid cast throws instead of NULL); Databricks Runtime default ANSI only from 17.0 | VERIFIED | spark.apache.org/docs/latest/sql-migration-guide.html ; docs.databricks.com ANSI pages |
| Timestamp default TIMESTAMP_LTZ; session time zone differences shift values | VERIFIED / LIKELY | Spark + Databricks docs |
| Declarative pipelines donated to Apache Spark (ships in 4.1 as `pyspark.pipelines`); old `dlt` module needs porting | VERIFIED | Databricks docs/blog |
| EMR 8.0 (Spark 4.0) GA 2026-06-09; Dataproc image 3.0 GA 2026-07-15 | VERIFIED | AWS big-data blog; Google Dataproc versioning |
| Dataproc fee **$0.010 per vCPU-hour** on top of Compute Engine; EMR uplift e.g. **$0.048/hr** on m5.xlarge (us-east-1) | VERIFIED | cloud.google.com/dataproc/pricing ; aws.amazon.com/emr/pricing |

## LinkedIn niche scan (Agent Reach, ~75 posts, last 6 months)
- Top performers: hard-number case studies; first-person bill-forensics stories; pricing-change
  news-jacking (Genie billing drew bursts); "myth/trap" framing; unit-economics corrections.
- **Oversaturated:** idle-cluster tip lists, DBU 101 explainers, Snowflake auto-suspend "quick wins",
  vendor Informatica->X success stories.
- **Under-covered:** system-table queries (zero posts found), chargeback/tagging/unit cost per job
  (zero), trusting migration cost estimates, cross-platform TCO maths, AI/Genie spend governance.
- No dominant voice on enterprise-scale Databricks cost + migration economics.
