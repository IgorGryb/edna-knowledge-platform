# ADR 0001: Immutable SHA-256 Content-Addressed Chunking

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Regulated Knowledge Infrastructure (FDA 21 CFR Part 11 / EU AI Act Compliance)
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
In enterprise compliance and regulatory research, text retrieval pipelines often suffer from citation drift. When underlying regulatory guidance, standard operating procedures (SOPs), or clinical protocols are updated, standard RAG vector stores frequently return cached embeddings referencing stale or superseded clauses. Furthermore, regulatory auditors require tamper-evident proof that a cited excerpt was identical to the approved document at the moment the decision memo was compiled.

## Decision Drivers
1. **Verifiable Lineage:** Every retrieved clause must link to an immutable content digest.
2. **Deterministic Version Sunset:** Superseded documents must be invalidated across all downstream active references instantly.
3. **Auditable Non-Repudiation:** Strict compliance with FDA 21 CFR Part 11 requirements for electronic records integrity.

## Considered Options
1. *Sequential Auto-Increment Database IDs:* High write throughput, but zero cryptographic binding to the underlying text content.
2. *Mutable File Paths with Last-Modified Timestamps:* Vulnerable to filesystem manipulation and race conditions.
3. *Cryptographic SHA-256 Content-Addressed Chunking (Selected):* Every chunk's identifier is mathematically derived from its normalized UTF-8 text and canonical metadata headers.

## Decision Outcome
Chosen Option: **Cryptographic SHA-256 Content-Addressed Storage**.
Every ingested chunk receives a deterministic unique identifier:
$$\text{Chunk ID} = \text{SHA256}(\text{DocID} \,\|\, \text{Version} \,\|\, \text{NormalizedText} \,\|\, \text{AccessTier})$$

### Positive Consequences
- **Absolute Idempotency:** Duplicate ingestion attempts of identical text are detected and rejected at zero storage cost.
- **Tamper Evidence:** Modifying a single character invalidates the hash, immediately failing integrity checks.
- **Instant Stale Invalidation:** Updating an SOP creates a new distinct hash, automatically flagging all prior decision memos citing the old hash as requiring re-audit.

### Negative Consequences / Trade-offs
- Text normalization rules (whitespace trimming, UTF-8 canonical decomposition) must remain 100% deterministic across all platforms.
