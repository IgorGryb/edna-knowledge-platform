# Internal project dossier — EDNA — Evidence-Grounded Knowledge Platform

Status: technical prototype; publication and user-interpretation gates pending.

## Why this project exists

Can a small, approved local corpus answer control questions with traceable citations and abstain when the corpus does not support an answer?

## Mechanism

TF-IDF cosine retrieval plus a deterministic concept-expansion layer, evaluated with hit@1, hit@3, reciprocal rank, citation coverage and an abstention test.

## Evidence chain

Concept record → source map → pre-test prediction → code → unit and negative tests → deterministic result → evidence hashes → case-study draft.

## Claim boundary

The defensible claim is that a narrow, local prototype was implemented and tested on the disclosed fixture. No production, client or realized-impact claim is made.
