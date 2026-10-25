# EDNA — Evidence-Grounded Knowledge Platform

## A bounded prototype with an auditable evidence chain

Can a small, approved local corpus answer control questions with traceable citations and abstain when the corpus does not support an answer?

The project turns a broad platform concept into one deterministic vertical slice. TF-IDF cosine retrieval plus a deterministic concept-expansion layer, evaluated with hit@1, hit@3, reciprocal rank, citation coverage and an abstention test.

**Evidence available:** source map, pre-test prediction, code, unit and negative tests, machine-readable result and SHA-256 evidence manifest.

**Publication boundary:** private draft. The defensible statement is that the disclosed mechanism was implemented and tested on the disclosed fixture. Small curated corpus, deterministic token vectors and hand-built concept map. The semantic mode is a local proxy, not a neural embedding model or production RAG system.
