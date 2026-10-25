# EDNA — management and operating dossier

Project: `PRJ-EDNA-PROTOTYPE`. Authored 2026-10-26. Status: internally specified design; not a deployed service. Source concept: `SRC-PRJ-EDNA-DOC`. Methods: M-SIPOC, M-RACI, M-MOSCOW, M-FEASIBILITY, M-MEASURE.

## Decision and business model

An operating model for governed research and knowledge reuse.

**Problem:** Research outputs become unreliable when claims lose their source, version, access restriction or correction history.
**Customer / decision user:** Researcher, analyst and knowledge steward
**Payer:** Internal research team; external willingness to pay is unvalidated
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

Tool configuration is proposed, not connected. Local Markdown/YAML is authoritative. Cloud tools require a separate data-sharing decision. See [toolchain](../../../00.%20ARCHIVE%20SYSTEM/portfolio/TOOLCHAIN-AND-HANDOFF.md).

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

This management model was authored with an AI agent from existing project sources, course materials and the approved user direction. It demonstrates the documented design and review process, not independent proof that the user performed every implementation step. All economic sample cases are synthetic.
