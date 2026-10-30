# Full project blueprint — EDNA — Evidence-Grounded Knowledge Platform

> Controlling management update (2026-10-26): [Management dossier](MANAGEMENT-DOSSIER.md) defines business, product, operating, financial and technology-management scope. User practice and production implementation are not documentary gates. Earlier technical content below remains bounded supporting material, not the full portfolio mandate.


Stable project ID: `PRJ-EDNA-PROTOTYPE`  
Status: source-grounded target architecture; implementation and validation backlog  
Evidence boundary: this document specifies what should be built and tested. Only linked test artifacts may support implementation claims.

## 1. Project thesis and decision boundary

A knowledge system is useful only when it improves a real research or learning decision while preserving source identity, abstaining when evidence is insufficient and making corrections propagate through dependent claims.

**Decision owner:** research or learning workflow owner  
**Decision supported:** Whether an answer is supported enough to learn from, reuse, test or route to further research.

### Users and reviewers

- researcher/learner
- source curator
- answer reviewer
- system administrator

### In scope for the validated portfolio case

- approved archive subset
- stable IDs and hashes
- lexical, vector and hybrid retrieval
- answerable/ambiguous/contradictory/unsupported evaluation
- citation and correction workflow

### Explicitly outside the validated claim

- ingesting the whole archive before evaluation
- autonomous truth adjudication
- uncited generated answers
- training a foundation model
- production handling of confidential sources

## 2. Layer architecture and operationalization

`Current` is evidence-based maturity now; `target` is the program gate. It is not a claim that the target has been achieved.

### 2.1 problem-user

**Objective:** Choose one recurring research or learning decision with an observable cost of poor evidence.

**Operationalization:** Define user, job, decision, current workflow, error modes, acceptable abstention and success measurement.

**Required artifact:** research-workflow charter  
**Acceptance test:** A real user can execute the baseline task and the measurement plan captures time and correction effort.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.2 market-business

**Objective:** Establish where evidence-grounded retrieval is worth its operating cost.

**Operationalization:** Compare manual search, generic assistants, document search and curated RAG; estimate adoption, review and maintenance burden.

**Required artifact:** value and adoption model  
**Acceptance test:** A user test measures willingness to reuse and whether time saved exceeds review/compute cost.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L1 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.3 product-service

**Objective:** Create a controlled evidence-to-answer and correction journey.

**Operationalization:** Specify source approval, query, passage view, citation, uncertainty, contradiction, abstention, feedback and affected-output review.

**Required artifact:** product/service blueprint  
**Acceptance test:** Users correctly distinguish source text, interpretation and system confidence in scenario tests.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.4 operating-model

**Objective:** Maintain sources, indices, golden sets and incidents over time.

**Operationalization:** Assign source owner, classification, ingest/re-index triggers, failed-answer triage, rollback, golden-set change control and SLA.

**Required artifact:** knowledge operations runbook  
**Acceptance test:** Tabletop exercise resolves source replacement, access revocation, broken parser and wrong accepted answer.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L1 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.5 data-technology

**Objective:** Implement separable and rebuildable ingest, retrieval and citation components.

**Operationalization:** Use raw snapshots, metadata extraction, chunk IDs, lexical index, true embeddings, hybrid ranker, citation assembler, dependency graph and telemetry.

**Required artifact:** reference architecture and executable pipeline  
**Acceptance test:** Clean rebuild produces traceable indices; bad inputs and access violations fail safely.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L3 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.6 analytical-model

**Objective:** Measure retrieval and answer quality without hiding class-specific failure.

**Operationalization:** Pre-register golden-set construction, relevance labels, k, ranking baselines, faithfulness rubric, abstention threshold and confidence intervals.

**Required artifact:** evaluation protocol and benchmark  
**Acceptance test:** Hybrid improvement and safety metrics hold on blinded questions with error analysis by class.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L3 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.7 finance-economics

**Objective:** Test whether reduced search time offsets compute, curation and review cost.

**Operationalization:** Model per-source ingest, per-query compute, reviewer time, re-indexing, incident correction and value of avoided false confidence.

**Required artifact:** cost-to-serve and ROI hypothesis model  
**Acceptance test:** Observed task data populates the model and sensitivity identifies break-even use frequency.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L1 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.8 risk-security-compliance

**Objective:** Protect confidential sources and resist unsupported or adversarial output.

**Operationalization:** Threat-model access bypass, injection, poisoned source, citation laundering, data leakage, stale claims and over-reliance; define controls and owners.

**Required artifact:** security, privacy and AI-governance pack  
**Acceptance test:** Adversarial tests trigger quarantine/abstention and every critical risk has owner and residual rating.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.9 delivery-governance

**Objective:** Control changes to corpus, model, prompts and evaluation.

**Operationalization:** Version data, configs, embeddings, prompts and golden set; require impact analysis and acceptance gates for metric changes.

**Required artifact:** model/data change runbook  
**Acceptance test:** A source and model change both trigger reproducible evaluation and dependent-output review.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L3 → target L5  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

### 2.10 evidence-validation-publication

**Objective:** Make every public capability statement auditable.

**Operationalization:** Link claims to corpus version, query set, run, metric definition, errors, reviewer decision and confidentiality status.

**Required artifact:** evaluation dossier and case study  
**Acceptance test:** Zero unsupported public claims; user validates usefulness and approves disclosure.  
**Methodological inputs:** Enterprise Systems Architecture & Quantitative Modeling  
**Maturity:** current L2 → target L6  
**Target Evolution:** Continuous operational telemetry and expanded enterprise integration.

## 3. Operating state model

### Normal states

`source proposed → quarantined → approved → ingested → indexed → queried → retrieved → answer drafted → reviewed or abstained → claim linked → source changed → dependents revalidated`

Every transition must record actor, timestamp, input state, output state, decision/evidence reference and exception reason when applicable.

### Required exception paths

- duplicate or changed source
- parser failure
- access restriction
- prompt injection
- conflicting evidence
- citation mismatch
- no supporting passage
- stale embedding/index

## 4. Technical and quality envelope

### Non-functional requirements

- stable source and chunk identity
- content hashes preserved
- retrieval trace exportable
- abstention supported
- access before retrieval
- index rebuildable
- changed sources trigger dependency review

### Metrics tree

- recall@k and MRR
- citation precision and entailment
- answer faithfulness
- abstention precision
- contradiction detection
- latency and cost
- reviewer correction time
- decision usefulness

Metrics must be tagged as observed, modeled or estimated. Modeled economic impact cannot be presented as realized impact.

## 5. Falsifiable hypotheses

1. Hybrid retrieval will outperform lexical and vector-only baselines on a preregistered heterogeneous golden set.
2. Source-level provenance and abstention will reduce unsupported accepted answers without unacceptable review burden.
3. Dependency-aware correction will identify every registered output affected by a changed source in the test fixture.

A test that cannot refute a hypothesis is practice or demonstration, not validation.

## 6. Experiment sequence

1. Freeze an approved corpus and create a blinded golden set with four question classes.
2. Compare lexical, vector and hybrid retrieval with identical chunks and evaluation queries.
3. Inject conflicting, stale and adversarial source text; test quarantine, abstention and reviewer routing.
4. Run one real learning/research task and compare time, correction effort and decision utility with manual baseline.

The prediction, threshold and interpretation owner must be recorded before each result. Failed or inconclusive tests remain in the evidence bundle.

## 7. Source-to-practice coverage

| Mapping | Layer | Course | Archive state | Practice/test | Evidence target |
|---|---|---|---|---|---|
| MOD-SPEC | technology | Advanced RAG with Vector Databases and Retrievers | manifest-complete | compare BM25, vector and hybrid retrieval | retrieval benchmark |
| MOD-SPEC | technology | Build RAG Applications: Get Started | manifest-complete | implement minimum end-to-end cited QA | reproducible demonstrator |
| MOD-SPEC | technology | Vector Databases for RAG: An Introduction | manifest-complete | document index/metric trade-offs | architecture decision record |
| MOD-SPEC | technology | Vector Databases: An Introduction with Chroma DB | manifest-complete | build a local embedding index | index artifact |
| MOD-SPEC | business | Vector Database Projects: AI Recommendation Systems | manifest-complete | test one recommendation use case | use-case evaluation |
| MOD-SPEC | operations | Introduction to Data Engineering | manifest-complete | write ingest and re-index runbook | operations runbook |
| MOD-SPEC | operations | ETL and Data Pipelines with Shell, Airflow and Kafka | manifest-complete | model ingest as a versioned DAG | pipeline evidence |
| MOD-SPEC | governance | Microsoft Fabric: Data Governance, Security, and Analytics | manifest-complete | add data-classification and access policy | governance checklist |
| MOD-SPEC | governance | AI Strategy and Governance | manifest-complete | define human-accountability and model-change gates | AI governance memo |
| MOD-SPEC | governance | Application Security for Developers and DevOps Professionals | manifest-complete | perform threat model including prompt injection | security report |
| MOD-SPEC | business | Developing Data Products | manifest-complete | build reviewer-facing evaluation dashboard | product evidence |
| MOD-SPEC | technology | Generative AI and LLMs: Architecture and Data Preparation | manifest-complete | measure chunk/token choices | data preparation report |

All rows above currently mean source routing. They become competence evidence only after the stated practice/test is executed and recorded.

## 8. Artifact backlog and gates

| Artifact ID | Layer | Deliverable | Current → target | Definition of Done |
|---|---|---|---:|---|
| ART-EDNA-01 | problem-user | research-workflow charter | L2 → L5 | A real user can execute the baseline task and the measurement plan captures time and correction effort. |
| ART-EDNA-02 | market-business | value and adoption model | L1 → L5 | A user test measures willingness to reuse and whether time saved exceeds review/compute cost. |
| ART-EDNA-03 | product-service | product/service blueprint | L2 → L5 | Users correctly distinguish source text, interpretation and system confidence in scenario tests. |
| ART-EDNA-04 | operating-model | knowledge operations runbook | L1 → L5 | Tabletop exercise resolves source replacement, access revocation, broken parser and wrong accepted answer. |
| ART-EDNA-05 | data-technology | reference architecture and executable pipeline | L3 → L5 | Clean rebuild produces traceable indices; bad inputs and access violations fail safely. |
| ART-EDNA-06 | analytical-model | evaluation protocol and benchmark | L3 → L5 | Hybrid improvement and safety metrics hold on blinded questions with error analysis by class. |
| ART-EDNA-07 | finance-economics | cost-to-serve and ROI hypothesis model | L1 → L5 | Observed task data populates the model and sensitivity identifies break-even use frequency. |
| ART-EDNA-08 | risk-security-compliance | security, privacy and AI-governance pack | L2 → L5 | Adversarial tests trigger quarantine/abstention and every critical risk has owner and residual rating. |
| ART-EDNA-09 | delivery-governance | model/data change runbook | L3 → L5 | A source and model change both trigger reproducible evaluation and dependent-output review. |
| ART-EDNA-10 | evidence-validation-publication | evaluation dossier and case study | L2 → L6 | Zero unsupported public claims; user validates usefulness and approves disclosure. |

### External validation required

- real research/learning user study
- security review of retrieval and access path
- independent audit of golden-set labeling

## 9. Integrated delivery sequence

1. Confirm problem, decision owner, user and anti-scope; record the user's own explanation.
2. Freeze approved sources/data and record hashes, permissions and proxy limitations.
3. Pre-register hypotheses, predictions, thresholds, alternatives and falsification conditions.
4. Complete guided practice from the selected courses and save its independent output.
5. Implement the vertical slice with explicit normal and exception states.
6. Compare against baseline; run negative, security, data-quality and sensitivity tests.
7. Review business, operations, finance and governance artifacts with the appropriate role.
8. Correct model, assumptions, dependent documents and evidence manifests.
9. Ask the user to interpret the result and choose continue, pause, pivot, stop or complete.
10. Only after acceptance, regenerate case study, PDF and private web version and run a claim audit.

## 10. Publication claim boundary

Allowed now: the narrow technical baseline exists and its local tests passed.  
Not allowed now: production readiness, market adoption, realized economic impact, legal compliance, client result or broad platform implementation.  
Allowed later: only statements backed by a versioned artifact, test result, reviewer record and evidence-manifest entry.

## 11. User gates

The user participates before irreversible narrowing, before a material test, when interpreting the result and before publication. The minimum prompts are:

- explain the problem and expected mechanism in your own words;
- predict the result and name a falsifying observation;
- interpret differences between baseline, model and judgment;
- choose `continue`, `pause`, `pivot`, `stop` or `complete`;
- state what changed in your understanding.
