# Interview narrative

**Problem:** Can a small, approved local corpus answer control questions with traceable citations and abstain when the corpus does not support an answer?

**Choice:** I selected a narrow vertical slice with an explicit baseline and falsification criterion instead of treating existing documentation as implementation evidence.

**Execution:** TF-IDF cosine retrieval plus a deterministic concept-expansion layer, evaluated with hit@1, hit@3, reciprocal rank, citation coverage and an abstention test.

**Mistake risk:** the fixture can overstate generality. I address that by labeling provenance, keeping alternative explanations and separating technical from external validation.

**Result:** the repository produces a reproducible, hashed technical result. Exact metrics are discussed only with the machine-readable evidence open.

**Next step:** seek user interpretation, then test on an approved external or public dataset where appropriate.
