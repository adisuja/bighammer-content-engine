# BigHammer.ai - General overview (origin story + product philosophy)

Source: Google Doc 1jWJRyEjBfnTlTfRFyo0_Pt_TwtM_H2GLiz99f3BYdjw "general overview" (owner: Richard Lawrence), fetched 2026-09-30.
This file is a FAITHFUL KEY-POINT EXTRACT, not the full text. Re-read the Doc before quoting at length.

## Claims / facts stated in the doc (usable as sourced statements)
- Founders lived the problem at **Dun & Bradstreet**; D&B's business is commercial data (companies, ownership, risk). Getting data wrong has consequences "well beyond a broken report".
- Srinath's team at D&B: **more than 600 people across data engineering, governance and data quality**.
- Data engineering was long described as "the plumbing" - everyone needed it, attention went to the dashboard at the other end.
- Small example used: a business team asks for something that looks simple; the data lives across several systems with different definitions and quality gaps; a chain of engineering work must happen before the question can be answered.
- AI changed two things at once: people with deep domain experience can build software faster, AND AI can improve the workflows inside that software.
- "Adding a chatbot to an existing product" was NOT the ambition; agents, context and engineering processes designed together from the beginning.
- As AI moves into business decisions, data quality underneath gets attention: **"An AI system can produce a convincing answer from incomplete information."** The user sees confidence, not the weakness in the data behind it.
- **Three audiences** BigHammer was designed for:
  1. Data engineers - want to deliver faster, keep control of what reaches production. Some see the opportunity immediately; others worry about their role.
  2. **Citizen data engineers** - analysts / business roles who end up doing data engineering (combining sources, working out why two sources disagree) before they can start their actual job. They describe what they need in natural language.
  3. **Application builders** - product teams (e.g. a recruitment app, trading) whose app depends on data plumbing; BigHammer was designed to be **embedded inside another application** and called directly.
- Business reasons are familiar: reduce cost, get to market sooner, simplify, manage risk; priorities shift over a project (speed first, then operating cost, reliability, audit).
- Scope: from ingesting and cataloguing, through preparing and moving, to reporting and running the processes.
- Agents focused on pipelines, governance, reporting, operations; an **orchestration agent** coordinates multi-step work like migration; a focused **data quality** capability.
- **Context engine**: keeps the business meaning of a field consistent as data moves through pipelines into reports/apps.
- **AI where useful, deterministic behaviour where the workflow requires it.** Established rules must behave consistently; owners must understand how results are reached.
- **LLM flexibility**: teams can change the model they use.
- **Customer owns the knowledge**: pipeline logic and business knowledge sit in the **customer's GitHub repository**; portability designed in from the start so customers can choose where processing runs.
- Deployment: runs in the customer's own environment, including inside their own application. Early customer work on **Azure and Google Cloud, alongside AWS**.
- Uses **Airflow** for orchestration; **auditing** a major focus. Early customers included **banking, financial services and healthcare**.
