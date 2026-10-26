# EDNA — Evidence-Grounded Knowledge Platform

> Private case-study draft. Technical validation does not equal production validation.

## Context

Can a small, approved local corpus answer control questions with traceable citations and abstain when the corpus does not support an answer?

## Decision

I reduced a broad platform concept to one falsifiable vertical slice and selected a transparent implementation that can be reproduced without external services.

## Implementation

Term-frequency cosine retrieval with deterministic concept expansion; measured fixture ranking and summary-citation support, not neural semantic retrieval or original-source truth verification.

## Validation

The repository records a prediction before the test, compares against a baseline or control, executes a negative test and hashes the resulting evidence. Exact metrics come from `artifacts/results.json` and must not be copied into public material without claim review.

## What this demonstrates

Problem framing, explicit assumptions, executable modeling, test design, evidence discipline and the ability to communicate limitations.

## Limitations

Small curated corpus, deterministic token vectors and hand-built concept map. The semantic mode is a local proxy, not a neural embedding model or production RAG system.
