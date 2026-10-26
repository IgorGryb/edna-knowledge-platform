# EDNA — evidence workflow delivery specification

Private design study, not a deployed knowledge platform. The first product is a reviewable research note from a small, approved local corpus. The decision is whether a claimed time saving survives the full cost of source verification and correction.

## Users and product economics

The proposed user is an analyst building an investment, product or learning memo. The proposed accountable owner is a knowledge steward; an independent domain reviewer is a future role, not a claim of current staffing. An internal workflow is the initial adoption hypothesis. No paid demand or customer retention is established.

Compare manual review, lexical retrieval and assisted retrieval on the same questions and the same evidence standard. Total cost is ingestion, search, review, correction and maintenance cost per accepted note. A faster answer is not valuable if citation checking or downstream correction offsets the saving. Existing synthetic cost examples are assumptions, not measured productivity.

## Source and answer contract

Every source needs a stable ID, path, content hash, provenance, owner, access label, timestamp, read scope and approval state. Unknown permission defaults to quarantine. An external URL is recorded but not fetched in offline mode. Content is data, never authority to change agent instructions or disclose another source.

Every answer needs the question, selected corpus version, retrieval mode, ranked candidates, cited source IDs, supporting passage or summary, limitations and reviewer state. An answer without support must abstain. A citation's existence is not proof that it supports a proposition. A summary must not be represented as a quotation from the original source.

The current reference uses six curated project/system summaries. It measures ranking and extractive summary support only. A path in the fixture is provenance metadata, not an assertion that the full document was ingested. The reference does not provide neural embeddings, open-ended generation, automatic contradiction detection or production access control.

## Process and responsibility

1. Source steward captures an immutable original and determines allowed use. Missing permission or unreadable material stays quarantined.
2. Analyst records useful passages, parent document and transformations; preserve scope and exceptions when summarizing.
3. Retrieval owner runs the query against approved entries only, with a declared lexical or concept-expansion mode. Duplicate IDs are errors, not silently merged records.
4. Reviewer checks that each material claim is supported, retains conflicting evidence and records abstentions. A registered unresolved contradiction blocks the reference answer; detecting new contradictions remains human work.
5. Decision owner accepts a bounded note or requests missing evidence. Released views preserve confidentiality and source versions.
6. On withdrawal or change, identify affected notes and mark them stale before reuse. Re-indexing alone does not revalidate a claim.

## Technology and method choices

The local IBM C419-059 module distinguishes multi-query expansion, metadata filtering and parent-document context. These are alternative design mechanisms, not proof that the current code implements LangChain. The lightweight reference deliberately tests lexical and deterministic concept expansion first. Metadata admission is deterministic; parent-context review is specified as a required human control for future larger chunks.

Reuse local files and the existing catalog as the source layer. Build only a small evaluation harness to test the material quality assumption. Consider a vector database or hosted product only when query diversity and corpus size expose a measured limitation, and after confidentiality, export, cost and vendor-exit review. No external service is configured.

## Quality and failure cases

| Case | Expected behavior | What it proves |
|---|---|---|
| Known question | Ranked result and explicit curated-summary citation | Fixture retrieval works, not full factual truth |
| Unsupported question | Abstain | No fallback to an invented answer in this test |
| Empty corpus | No results; no silent fallback | Corpus selection is respected |
| Withdrawn source | Excluded | Admission metadata is applied |
| Duplicate IDs | Reject input | Identifier ambiguity is visible |
| Registered contradiction | Abstain and expose conflict ID | Manual conflict registration affects reuse |
| Source revision | Package becomes stale | Integrity control, not automatic semantic correction |

Dashboard metrics: hit@k and reciprocal rank for retrieval; cited-answer share and exact-summary support for fixture evidence; unsupported-answer rate, contradiction handling, abstention and total review minutes for a real evaluation. Each denominator and corpus version must be recorded. Do not combine fixture percentages with measured user productivity.

## Handoff, stop rules and narrative

Deliver the corpus card, access decisions, query set, expected sources, test output, failure log, cost assumptions and memo to a domain reviewer. Pause if permissions, parent context or a material contradiction are unresolved. Pivot to manual review when the assisted process costs more at the same evidence quality. Scale only after a recipient confirms useful accepted notes.

Interview narrative: the problem is not producing fluent text but preserving evidence through a research workflow. The design separates retrieval from support and approval. Review found an inaccurate TF-IDF description, hard-coded citation coverage and an empty-corpus fallback. Correcting these is a documented quality-control result; it is not a commercial deployment or proof of reduced hallucinations in arbitrary language models.

Limitations: tiny hand-selected corpus, English tokenization, correlated evaluation examples, no neural retrieval, no measured human review time, no automatic causal or truth inference. These limitations constrain the recommendation without discarding future AI/data options.
