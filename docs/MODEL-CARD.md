# Model / mechanism card

## Method

Term-frequency cosine retrieval plus deterministic concept expansion (not TF-IDF or neural semantic embeddings). Evaluated with hit@1, hit@3, reciprocal rank, measured citation coverage, exact-summary support and abstention cases. Corpus entries are curated summaries with source paths; they are not verified quotations from the original documents. Metadata excludes non-approved records; registered contradictions trigger abstention, but the system does not discover contradictions automatically.

## Intended use

Transparent technical demonstration and discussion aid.

## Non-intended use

Production decisions, regulated decisions, investment advice, autonomous operation or claims about client impact.

## Validation

Unit tests, deterministic reproduction, baseline comparison and negative cases. Optional user interpretation does not block documentary work. External validation is required before claiming external impact, not before presenting a bounded design study.
