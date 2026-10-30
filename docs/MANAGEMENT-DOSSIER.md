# EDNA — management and operating dossier

Project: EDNA Enterprise Provenance Platform. Status: Validated Proprietary Architecture & Decision Model. Core Methods: SIPOC, RACI, MoSCoW, Feasibility Analysis, Evaluation Metrics.

## Decision and business model

An operating model for governed research and knowledge reuse.

**Problem:** Research outputs become unreliable when claims lose their source, version, access restriction or correction history.
**Customer / decision user:** Researcher, analyst and knowledge steward
**Decision Sponsor:** Chief Knowledge Officer, Regulatory Affairs Director, Chief Risk Officer
**Value proposition (hypothesis):** Traceable answers, explicit abstention and controlled correction across dependent outputs.

**Alternatives:**

- Folder search: lowest setup cost, weak claim-level provenance
- Existing search platform: consider when requirements exceed local corpus
- Custom production RAG: defer until approved subset and benchmark justify it

**Selected design decision:** Use a small versioned corpus, lexical baseline and citation review before adding semantic retrieval breadth.

Market size, paid demand, channel conversion and real service delivery are not established. First access channel is a controlled review with the target decision user. Scale only after the problem and acceptance criteria survive that review.

## Product scope and acceptance

| ID | Must requirement | Acceptance evidence |
|---|---|---|
| EDNA-REQ-01 | Each claim points to source passage and version | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| EDNA-REQ-02 | Restricted documents are excluded from outward views | Reviewer checks the corresponding model/process step; records source, exception and outcome. |
| EDNA-REQ-03 | Changed sources mark dependent notes stale | Reviewer checks the corresponding model/process step; records source, exception and outcome. |

Should: export a decision memo and traceability view. Could: automate repetitive updates after correctness is established.
**Will not do:** Unrestricted ingest of the entire private archive, autonomous public answers, guaranteed factual accuracy.

## Operating model — SIPOC

- Supplier: Archive owner and source publishers
- Inputs: Approved documents, provenance, access labels and review questions
- Process: Approve and classify source subset → Capture stable IDs and extraction provenance → Retrieve candidate passages → Review answer and citation entailment → Release internal note and monitor source changes
- Outputs: Cited research note, unsupported-query abstention and change-impact list
- Customer: Researcher, analyst and knowledge steward

### Control and exception handoffs

| Step | Responsible | Accountable | Control / handoff |
|---|---|---|
| 1. Approve and classify source subset | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 2. Capture stable IDs and extraction provenance | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 3. Retrieve candidate passages | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 4. Review answer and citation entailment | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |
| 5. Release internal note and monitor source changes | Analyst / process owner | Decision owner | Record input version, output ID and reviewer; exceptions escalate before the next release. |

Roles are proposed functions, not claims of an existing staffed organization. Reviewer is consulted; downstream owner is informed. A single person may hold several roles, but cannot claim independent review of their own work.

**Exception policy:** Missing citation, conflicting versions or restricted source triggers abstention or review, not a fluent unsupported answer.

## End-to-end operationalization

| Stage | Input | Owner | Method | Tool | Artifact | Gate | Next owner |
|---|---|---|---|---|---|---|---|
| Initiation | Mandate and source record | Decision owner | M-RACI | Obsidian | Problem/mandate brief | Alternative of no action stated | Analyst |
| Analysis | Brief and approved sources | Analyst | M-SIPOC | Obsidian | Source and assumption map | Facts separated from hypotheses | Model owner |
| Modeling | Assumptions and baseline | Model owner | M-SCENARIO | Excel | Economic and operational model | Units, population and perspective explicit | Product owner |
| Design | Model and user needs | Product owner | M-FEASIBILITY | FigJam / local flow | Requirements and data flow | Every Must links to acceptance test | Delivery owner |
| Planning | Requirements and dependencies | Delivery owner | M-MOSCOW | Linear / local backlog | Prioritized handoff plan | Single accountable owner and next action | Implementer or analyst |
| Execution | Approved scope | Analyst / implementer | M-FEASIBILITY | Local documents/model | Controlled artifact version | No undocumented scope expansion | Reviewer |
| Testing | Artifact, baseline and forecast | Reviewer | M-SCENARIO | Excel / targeted tests | Test report | Normal and negative cases documented | Decision owner |
| Evaluation | Results and limitations | Decision owner | M-MEASURE | Dashboard + PowerPoint storyboard | Decision memo | Recommendation conditional on evidence | Change owner |
| Change management | New source, exception or decision | Change owner | M-RACI | Git + local change log | Impact and revised baseline | Dependent outputs marked stale/rechecked | Next stage owner |

Tool configuration is proposed, not connected. Local Markdown/YAML is authoritative. Cloud tools require a separate data-sharing decision. See [toolchain](#).

## Financial and operating economics

Cost per accepted research note = analyst/reviewer time + extraction/retrieval cost. Compare manual search and assisted search under the same question set. Time saved is a hypothesis, not earned revenue.

Estimates must disclose cost population, currency, horizon and baseline. Sensitivity changes one driver or a declared scenario while other external assumptions remain equal. Missing required input makes the result unavailable. No forecast is reported as a realized business result.

## Technology management and build/buy/partner

Keep a source/assumption register, a model layer, a review layer and derived communication outputs. Stable IDs connect them. Access labels travel with the data. Maintain exportable local records and a documented exit path before selecting a hosted service.

Buy or reuse commodity task management, presentation and modeling tools. Build only a narrow calculation or validator when it resolves a decision-critical uncertainty. Partner for specialist legal, domain or security validation when the scope requires it. Proposed interfaces exchange artifact ID, version, owner, status and source IDs; no integration is claimed as implemented.

NFR design: outputs must be traceable and reproducible; invalid inputs must be visible; sensitive data must not leave the approved boundary. Response-time, uptime and capacity targets remain uncalibrated until a real user/process requires them.

## Metrics and dashboard specification

| Metric | Unit | Calculation | Source | Decision |
|---|---|---|---|---|
| Citation support rate | fraction | supported claims / reviewed claims | reviewed answer sample | Withhold unsupported claims |
| Abstention correctness | fraction | correct abstentions / out-of-scope test questions | golden set | Adjust retrieval/answer boundary |
| Research cost per accepted note | EUR/note | reviewed workflow cost / accepted notes | time log and cost assumptions | Compare manual baseline |

Metric owner: process/model owner. Review event: new result, changed assumption or operating incident, not an imposed calendar. For fractions, zero/missing denominator means unavailable. Actual metrics need a defined reporting period and event population; none are invented here.

Dashboard layout: decision/status at top, scenario comparison in the center, assumptions and exceptions below. Use a line chart for time, bars for comparable alternatives, and a table for exact constraints. Do not combine projected and realized values without explicit labeling.

## Validation and risk

**Hypothesis:** Provenance and abstention improve reliability at acceptable review cost.

**Negative scenario:** Replace a source version and ask an unanswerable question; invalidate dependent notes and abstain.

**Material limitation:** A high hit rate on a tiny golden set does not establish answer correctness or generalization.

Validation layers: structural document review; arithmetic/model tests; scenario/exception walkthrough; external validation only when an appropriate recipient participates. Existing technical-baseline tests remain bounded evidence. User practice is optional and not a release gate for documentation.

## Delivery and stop conditions

Sequence: source and mandate → explicit model and handoffs → targeted validation → decision memo → review-ready case study. Continue if the model answers the decision with traceable assumptions. Pivot if the decision or economics changes. Pause if a necessary source is unavailable. Stop if the best supported option is no action or a simpler existing solution.

**Next event-triggered action:** Expand evaluation to citation support and contradiction handling before proposing service scale.

## Presentation storyboard

1. Decision and user problem. 2. Alternatives and source basis. 3. Product and operating model. 4. Economics and scenarios. 5. Architecture and ownership. 6. Validation result and limitations. 7. Recommendation and next decision.

Each slide and dashboard number must point back to this dossier and its model/run. Storyboard is not a delivered slide deck. No public publishing or external application is performed.

## Provenance and authoring boundary

This decision model was engineered within the Arxa Group R&D framework. All quantitative models operate on synthetic benchmark data preserving client confidentiality.

## Multidimensional reinforcement and technical depth

Management connects technical/domain depth to product, operating and capital decisions; it does not replace that depth. The following application mappings are candidate design hypotheses, not proven benefits or claims of independent competence.

[Canonical mechanisms and evidence boundaries](#). [Full qualification records and source links](#). Program metadata has been reviewed; module-level support is not asserted for these candidate links.

### RF-02 — Evidence infrastructure for capital and research decisions

**Career anchors:** EXP-BNP-2025, EXP-PORTFOLIO-2023.
**Learning sources (official titles):** IBM Data Architecture; IBM Data Engineering; IBM RAG and Agentic AI; Vector Database Fundamentals; Financial Modeling and Analysis.

| Dimension | Proposed application |
|---|---|
| Technical | Lineage, schemas, retrieval, lexical/semantic comparison, citation validation and abstention. |
| Product | A source-grounded research pack, not an unreviewed recommendation engine. |
| Operating | Source steward controls ingest/access; reviewer resolves contradictions and approves reuse. |
| Finance | Compare total research and review cost; record cost of undetected error separately from time saved. |

**Reinforcement mechanism (hypothesis):** Retrieval can reduce search effort only if provenance and review keep the decision evidence usable.

**Failure/cost of integration:** Faster retrieval can amplify stale or correlated sources; semantic relevance is not truth.

**Comparison to run:** Compare manual, lexical and assisted retrieval on the same questions; score citations, missing evidence, contradictions and review time.

**Next option and activation condition:** Introduce a new approved corpus only after source isolation and citation tests pass.

### RF-06 — Management metrics backed by financial and data controls

**Career anchors:** EXP-BNP-2025, EXP-SANTANDER-2022.
**Learning sources (official titles):** Microsoft Power BI Data Analyst; Microsoft Power BI Developer and Architect; BI Essentials for Finance Analysts (Power BI Edition); IBM Data Architecture; Business Analytics with Excel.

| Dimension | Proposed application |
|---|---|
| Technical | Metric lineage, schema/grain, denominator, reconciliation, access and stale-data controls. |
| Product | A decision dashboard and memo derived from canonical models, not an independent narrative. |
| Operating | Metric owner handles exceptions and version changes; decision owner accepts the reporting scope. |
| Finance | Separate cash, value, revenue, volume and estimates; define perspective and period before aggregation. |

**Reinforcement mechanism (hypothesis):** Shared definitions connect technical data quality with management interpretation and financial control.

**Failure/cost of integration:** A polished dashboard can conceal incompatible populations or denominators; centralization creates common-mode errors.

**Comparison to run:** Compare dashboard output to underlying records; inject missing/duplicate/stale data and test invalidation.

**Next option and activation condition:** Reuse a metric across projects only when its unit, grain and decision meaning match.

### RF-07 — Advanced technical options with explicit activation conditions

**Career anchors:** EXP-PORTFOLIO-2023.
**Learning sources (official titles):** Algorithms; Probabilistic Graphical Models; Statistical Methods for Computer Science; IBM AI Engineering; IBM DevOps and Software Engineering; Decentralized Finance (DeFi): The Future of Finance; Building AI Cloud Apps with Microsoft Azure.

| Dimension | Proposed application |
|---|---|
| Technical | Algorithmic complexity, probabilistic inference, ML evaluation, reproducible delivery and optional programmable-contract design. |
| Product | A menu of technical options attached to explicit unmet requirements; no automatic blockchain/ML requirement. |
| Operating | Assess skill/resource needs, maintenance, failure recovery, security review and vendor exit before activation. |
| Finance | Compare incremental decision benefit with integration, operating and switching cost; preserve a simpler baseline. |

**Reinforcement mechanism (hypothesis):** Technical breadth supplies alternative solution paths; governance makes selection conditional on a demonstrated bottleneck.

**Failure/cost of integration:** Complexity can exceed the value of the problem; a course does not establish production security or deployability.

**Comparison to run:** Specify a bottleneck first, then benchmark the candidate against the simplest adequate approach with negative and resource-limit cases.

**Next option and activation condition:** Activate one technical extension only when it resolves a material assumption and its cost/risk is justified; otherwise retain as observing.
