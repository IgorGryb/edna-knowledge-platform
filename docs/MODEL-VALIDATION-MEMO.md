# EDNA — validation and decision memo

Private bounded design study. Five authored retrieval questions, six curated summaries and synthetic cost assumptions; no external market or user trial.

## Evidence quality

Both lexical and concept-expansion modes achieve hit@1 80%, hit@3 100% and MRR 0.90 on this fixture. There is no demonstrated ranking improvement.
Measured citation coverage is 80% for lexical and 100% for concept expansion. Exact-summary support has the same rates. This measures extracted summary support, not correctness against the original documents or relevance of every answer.
The original no-worse-at-three prediction passes, but it is a weak acceptance condition and does not justify investing in a semantic platform.
Empty corpus, unsupported query, withdrawn source and registered conflict all produce abstention. Duplicate IDs and unsupported modes are rejected in regression tests. Novel contradictions are not detected automatically.

## Economics and decision boundary

At the declared synthetic cost assumptions, manual review costs EUR 60.00 per accepted note; assisted preparation plus review and tools costs EUR 42.00. With 60 review minutes the assisted cost becomes EUR 87.00.
The break-even review time is 33.00 minutes at the same acceptance quality. Time beyond that threshold eliminates the assumed saving. Ingestion and maintenance are not measured; allocate them before claiming net benefit.
The pre-recorded cost forecast matches arithmetic, not observed productivity. A higher cited-answer rate can simply mean less abstention; it is not automatically a quality improvement.

## Recommendation

Continue with a controlled local evidence workflow and explicit review; do not scale or buy a hosted retrieval service on this result. For the next supplied corpus, define approved passages and expected answers before running the comparison, record manual and assisted review time, and include stale, conflicting and out-of-scope questions.
Pause a note when required evidence or permission is missing. Prefer manual review if the full assisted cost exceeds it at the same quality. Preserve advanced retrieval techniques as options conditional on a demonstrated bottleneck.

## Post-mortem and handoff

Corrected the inaccurate TF-IDF label, hard-coded citation coverage and empty-list fallback. Added explicit source-summary scope, excerpt hashes, withdrawn-source filtering and conflict abstention. These changes improve auditability within this narrow reference.
Handoff: DELIVERY-SPECIFICATION.md, MODEL-CARD.md, core.py, tests and artifacts/management-review.json. Roles and external integrations are proposed. No original course material is copied into an outward-facing case study.
