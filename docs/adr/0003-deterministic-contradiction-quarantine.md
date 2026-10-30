# ADR 0003: Deterministic Contradiction Quarantine & Conflict Matrices

- **Status:** Accepted
- **Date:** 2026-10-28
- **Context:** Policy Conflict Governance & Regulatory Compliance
- **Deciders:** Igor Grybek (Systems Architect, Arxa Group)

## Context & Problem Statement
Multinational corporations and regulated institutions frequently operate with conflicting regulatory guidelines (e.g. EU GDPR vs US CLOUD Act, local jurisdictional labor laws, or transitioning clinical trial amendments). Standard vector search aggregates semantically similar documents, which often causes opposing rules to be merged into a single blended recommendation, obscuring critical policy contradictions.

## Decision Drivers
1. **Collision Visibility:** Opposing rules must never be silently reconciled by an automated system.
2. **Explicit Abstention:** The system must freeze generation and surface the conflicting document IDs.
3. **Compliance Escalation:** Mandates formal human compliance sign-off to resolve conflicting regulatory interpretations.

## Decision Outcome
Chosen Option: **Deterministic Policy Conflict Matrix & Quarantine Protocol**.
When the query traversal detects documents with registered mutually exclusive regulatory vectors:
1. Automated synthesis is immediately aborted.
2. The query status transitions to `CONTRADICTION_ABSTAIN`.
3. An audit payload containing both opposing clause hashes, jurisdiction tags, and timestamps is delivered to the designated Compliance Reviewer in the RACI matrix.

### Positive Consequences
- Guarantees zero silent merging of mutually exclusive legal and compliance obligations.
- Fully aligns with **EU AI Act Article 14 (Human Oversight)** for high-risk AI decision systems.

