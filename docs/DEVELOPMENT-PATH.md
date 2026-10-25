# Source-grounded development path — EDNA

> Status: enrichment specification. The current executable prototype is a technical baseline, not the finished portfolio case.

## Verified inputs

- canonical concept record: `1. Portfolio/EDNA Ontology/PROJECT-RECORD.md`
- representative internal project documents:
  - `1. Portfolio/EDNA Ontology/EDNA Data Ontology Platform (1) 39be5c6f32dc807190f9efae73868c3b.md`
  - `1. Portfolio/EDNA Ontology/PRODUCT/DOCUMENTATION/Technology/architecture 24696a7dab614ccd9f5140fab892f2d4.md`
  - `1. Portfolio/EDNA Ontology/PRODUCT/DOCUMENTATION/Technology/data structure d13ff1b52b1549b4a67cdc5d5869d48f.md`
  - `1. Portfolio/EDNA Ontology/PRODUCT/DOCUMENTATION/Technology/data source 1b766dab21ca4bc580433b315bdac417.md`
- archived courses below were checked for an existing directory and reviewed at syllabus level; selected module materials exist where `materials_state` is complete.
- a certificate record confirms completion provenance only. It does not independently prove the project capability.

## Layers to develop

### Business

Choose one costly research or learning workflow, identify the decision it improves, define user roles and adoption friction, and measure time-to-evidence, answer utility and correction rate rather than document volume.

### Technology

Develop ingestion, stable IDs, content hashes, metadata extraction, chunking, lexical retrieval, real embeddings, reranking, citation assembly, contradiction detection, evaluation and observability as separable components.

### Operations

Specify source approval, quarantine, access classification, re-indexing, stale-source handling, golden-set maintenance, failed-answer triage and rollback of changed claims.

### Finance Risk

Model storage/compute/review cost, value of reduced research time and the cost of false confidence. Treat automation ROI as a hypothesis requiring observed task data.

### Governance

Enforce provenance, privacy, access control, prompt-injection boundaries, abstention, human review and evidence retention. Distinguish retrieved text from generated interpretation.

## Course-to-practice map

| Layer | Course | Archive state | How it changes the project | Required evidence |
|---|---|---|---|---|
| technology | C419-059 — Advanced RAG with Vector Databases and Retrievers | manifest-complete; platform-listed | compare BM25, vector and hybrid retrieval | retrieval benchmark |
| technology | C419-067 — Build RAG Applications: Get Started | manifest-complete; platform-listed | implement minimum end-to-end cited QA | reproducible demonstrator |
| technology | C419-118 — Vector Databases for RAG: An Introduction | manifest-complete; platform-listed | document index/metric trade-offs | architecture decision record |
| technology | C419-119 — Vector Databases: An Introduction with Chroma DB | manifest-complete; platform-listed | build a local embedding index | index artifact |
| business | C419-117 — Vector Database Projects: AI Recommendation Systems | manifest-complete; platform-listed | test one recommendation use case | use-case evaluation |
| operations | C419-213 — Introduction to Data Engineering | manifest-complete; platform-listed | write ingest and re-index runbook | operations runbook |
| operations | C419-214 — ETL and Data Pipelines with Shell, Airflow and Kafka | manifest-complete; platform-listed | model ingest as a versioned DAG | pipeline evidence |
| governance | C419-163 — Microsoft Fabric: Data Governance, Security, and Analytics | manifest-complete; platform-listed | add data-classification and access policy | governance checklist |
| governance | C419-190 — AI Strategy and Governance | manifest-complete; platform-listed | define human-accountability and model-change gates | AI governance memo |
| governance | C419-063 — Application Security for Developers and DevOps Professionals | manifest-complete; platform-listed | perform threat model including prompt injection | security report |
| business | C419-131 — Developing Data Products | manifest-complete; platform-listed | build reviewer-facing evaluation dashboard | product evidence |
| technology | C419-216 — Generative AI and LLMs: Architecture and Data Preparation | manifest-complete; platform-listed | measure chunk/token choices | data preparation report |

## Execution sequence

1. Expand the approved corpus with stable snapshots and a documented inclusion/exclusion decision.
2. Replace the current concept proxy with a true embedding baseline while preserving lexical retrieval.
3. Build a larger golden set containing answerable, ambiguous, contradictory and unsupported questions.
4. Measure retrieval, citation correctness, answer faithfulness, latency and reviewer correction effort.
5. Run a real research or learning task with a human reviewer and record whether EDNA changed the decision.

## Readiness rule

The project may return to `productize` only when the selected learning sources have been converted into executed practice, the new test evidence is in the manifest, the limitations are updated and the user has interpreted the result. Unused course material remains provenance, not a portfolio claim.
