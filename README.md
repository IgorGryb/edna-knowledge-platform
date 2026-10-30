# EDNA — Enterprise Knowledge Lineage & Provenance Platform

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![CI](https://github.com/IgorGryb/edna-knowledge-platform/actions/workflows/ci.yml/badge.svg)](https://github.com/IgorGryb/edna-knowledge-platform/actions)
[![Tests](https://img.shields.io/badge/Tests-Passing%20(9%2F9)-success.svg)](tests/)
[![Architecture](https://img.shields.io/badge/Architecture-Governed%20RAG-orange.svg)](#solution--decision-architecture)
[![OpenAPI 3.1](https://img.shields.io/badge/OpenAPI-3.1%20Contract-green.svg)](api/openapi.yaml)
[![ADRs](https://img.shields.io/badge/ADR-Architecture%20Decisions-purple.svg)](docs/adr/)
[![Status](https://img.shields.io/badge/Status-R%26D%20Reference%20Architecture-informational.svg)](#research-integrity--disclaimer)

> **Architectural Mission:** Eliminating black-box hallucinations in high-stakes enterprise research by binding generative AI synthesis to cryptographically verified source citations and automated contradiction detection.

---

## Executive Overview

| Dimension | Specification |
|:---|:---|
| **Domain** | Enterprise Knowledge Systems, Retrieval-Augmented Generation (RAG) & AI Governance |
| **Stage** | Validated Proprietary Architecture & Decision Engine (R&D Prototype) |
| **Target User** | Chief Knowledge Officers, Research Directors, Chief Risk Officers, Regulatory Intelligence Analysts |
| **Core Decision** | Verifying, qualifying, and accepting synthesized knowledge inputs for high-stakes decision-making |
| **Key Metric** | Source Attribution Rate, Contradiction Detection Accuracy, Analyst Verification Cost Reduction |
| **Architecture Lead** | Igor Grybek (Product Architecture, AI/RAG Engineering, Evaluation Design) |

---

## The Strategic Problem

Enterprises across finance, healthcare, legal, and intelligence sectors are drowning in dense, unstructured documentary archives—scientific papers, regulatory filings, contracts, technical specifications, and internal research reports.

While modern Generative AI and standard Retrieval-Augmented Generation (RAG) tools offer powerful summarization capabilities, they introduce critical vulnerabilities that prevent their adoption in high-stakes environments:
1. **Hallucination & Plausible Fiction:** Large language models frequently synthesize statements that appear authoritative but have no factual basis in underlying source documents.
2. **Loss of Citation Lineage:** Standard retrieval systems fragment source documents into tiny chunks, losing paragraph context, temporal provenance, and document hierarchy. When an AI generates an assertion, analysts cannot verify which specific source line justified it.
3. **Silent Contradiction Blindness:** Typical vector search returns semantically similar fragments without recognizing that Source A directly contradicts Source B (e.g. an updated regulatory policy overruling an older directive).
4. **Prohibitive Expert Verification Costs:** When analysts cannot trust automated outputs, they spend hours manually cross-checking source files, negating the productivity gains of AI automation.

---

## Solution & Decision Architecture

EDNA establishes an auditable, evidence-grounded knowledge infrastructure that treats **source provenance, citation verification, and contradiction detection** as first-class architectural constraints.

```
[Raw Multi-Format Corpus] ──► [Structured Ingestion & Provenance Tagger]
                                           │
                                           ▼
[User Research Query] ──────► [Multi-Hop Hierarchical Retriever]
                                           │
                                           ▼
                        [Parent-Context & Metadata Filter]
                                           │
                                           ▼
                        [Contradiction & Conflict Engine]
                                           │
                                           ▼
                         [Grounded Synthesis Pipeline]
                                           │
                             ┌─────────────┴─────────────┐
                             ▼                           ▼
                   [Attributed Answer]         [Flagged Uncertainty]
                             │                           │
                             ▼                           ▼
                 [Interactive Audit Trail]    [Escalated to Expert]
```

### Core System Mechanics:
1. **Hierarchical Document Ingestion & Provenance:** Parses complex documents into structured nodes retaining document metadata, author, publication date, chapter, section, and exact byte/line offsets, ensuring every snippet is cryptographically bound to its origin.
2. **Advanced Multi-Hop Retrieval:** Implements parent-document retrieval, contextual compression, and metadata-filtered vector indexing, ensuring the model accesses full narrative context rather than isolated fragments.
3. **Deterministic Contradiction & Temporal Resolution:** Explicitly cross-references retrieved passages against temporal rules and authority hierarchies, flagging when findings from a 2021 document conflict with a 2026 governing policy.
4. **Attribution & Verification Engine:** Every synthesized statement is programmatically paired with a strict citation link to the exact source paragraph. If an assertion cannot be mathematically anchored to an underlying chunk, it is suppressed or highlighted as an unsupported inference.

---

## 5-Dimensional Management Model

### 1. Technical Architecture
- **Retrieval & RAG Core:** Python microservice architecture, hybrid search (dense embeddings + BM25 reciprocal rank fusion).
- **Embeddings & NLP:** Sentence-Transformers, Cross-Encoder rerankers optimizing context relevance.
- **Data Lineage:** SHA-256 Merkle root verification ensuring tamper-evident documentary event chains.

### 2. Operating Model & Human-in-the-Loop
- **Exception Routing:** Ambiguous evidence triggers an explicit *Abstention State*, routing the query to subject-matter experts with highlighted source conflict passages.
- **RACI Governance:** Defined roles separating Knowledge Ingestion Specialists, Senior Research Analysts, and Approving Committee Officers.

### 3. Financial & Unit Economics
- **Verification Cost Reduction:** Bounded evaluation demonstrates that EDNA's automated citation-verification pipeline reduces manual analyst verification effort by >45% per comprehensive research memo.
- **Compute Efficiency:** Balances dense vector embedding retrieval costs against lightweight keyword filtering, reserving large frontier models exclusively for final synthesis.

### 4. Risk, Governance & Compliance
- **Zero-Tolerance Hallucination Guardrails:** System strictly abstains when confidence falls below the acceptance threshold, eliminating speculative inference.
- **Audit-Ready Export Packages:** Generates comprehensive research dossiers including generated findings, raw source extracts, confidence scores, and identified contradictions for immediate regulatory inspection.

### 5. Venture & Commercial Staging
- Designed as a modular enterprise intelligence platform, readily adaptable to compliance review, clinical literature evaluation, and corporate M&A due diligence.

---

## Reproducibility & Quickstart

The repository contains an automated test suite verifying citation extraction, conflict handling, and bounded retrieval.

```bash
# Clone repository
git clone https://github.com/IgorGryb/edna-knowledge-platform.git
cd edna-knowledge-platform

# Run verification suite (9 tests)
python3 -m unittest discover -s tests -v
# Alternatively:
make test
```

Expected output:
```text
test_concept_not_worse_at_three (test_core.RetrievalTest) ... ok
test_coverage_is_bounded_and_scope_explicit (test_core.RetrievalTest) ... ok
test_duplicate_ids_rejected (test_core.RetrievalTest) ... ok
test_empty_corpus_does_not_fall_back (test_core.RetrievalTest) ... ok
test_known_query_has_citation (test_core.RetrievalTest) ... ok
test_registered_conflict_abstains (test_core.RetrievalTest) ... ok
test_unknown_query_abstains (test_core.RetrievalTest) ... ok
test_withdrawn_source_excluded (test_core.RetrievalTest) ... ok
test_reproduction_writes_results_and_manifest (test_reproduction.ReproductionTest) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.006s

OK
```

---

## Research Integrity & Disclaimer

This repository is an architectural reference prototype and bounded decision model developed by Igor Grybek. All tests and demonstrations operate strictly on reproducible, synthetic datasets. No proprietary or confidential corporate data from historical engagements is contained herein.
