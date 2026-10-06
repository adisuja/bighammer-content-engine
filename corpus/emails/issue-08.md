# Email series - Issue 8 (source: ~/Downloads/Email_08.pdf, added 2026-09-30)

Issue 8, Proving parity before you switch anything off
Hi {{first_name}},
The migrated job passes its tests. The code looks right. And still, nobody wants to be the person who
turns off the original.
That hesitation is reasonable. Code conversion is the visible part of a migration. Proving that the new
job produces the same data as the old one is the part that gets skipped, and it's exactly where trust
breaks.
Why "it ran successfully" isn't enough
A job can complete on time and still produce different results. A changed join, a different null handling
rule, a timezone shift. None of these fail the run. All of them fail the business.
The parity checklist
Row and column counts · schema match · null rates · numeric aggregates · key-based or
hash-based row comparison
Check it yourself: your parity checklist
Before any cutover, compare the old and new outputs on:
 Row and column counts: the fastest signal that something is off.
 Schema: same columns, same types.
 Null rates per column: catches silent handling changes.
 Numeric aggregates: sums, minimums and maximums on key measures.
 Row-level comparison: by business key, or by hash when there's no clean key.
What good looks like
 Run the old and new jobs side by side on cloned data, so production is never touched.
 Agree the checks and tolerances with the business owner before the migration starts.
 Cut over in small groups of jobs, not all at once.
 Keep the comparison results as evidence for sign-off.
How BigHammer does this
BigHammer Migrate runs the migrated job alongside the original and compares the outputs using these
checks, so the cutover decision is based on evidence rather than confidence.
Where this series leaves you
Over eight issues we've covered the path we see work best:
1. See it: a 90-day baseline.
2. Trace it: how much spend belongs to a job.
3. Measure it: what failures cost.
4. Assess it: one read-only notebook.
5. Report it honestly: measured first, estimates with their method.

6. Right-size it: from real utilisation.
7. Classify it: keep, evaluate, or move, job by job.
8. Prove it: parity before cutover.
You can start with step 4 today.
[Run the offline assessment]  ·  [Book a 30-minute walkthrough], The BigHammer team
---
