# Hypotheses, prediction and falsification

## Primary hypothesis

Lexical and concept-expanded retrieval are benchmarked on a golden set; every returned answer includes source IDs; unsupported questions trigger abstention.

## Prediction recorded before test

Concept-expanded retrieval will achieve hit@3 no worse than lexical retrieval on the fixed golden set, and an out-of-domain question will trigger abstention.

## Falsification criterion

The prediction is falsified if concept hit@3 is lower than lexical hit@3 or if the unsupported question returns a confident source.

## Alternative explanation

A passing result may follow from the deliberately narrow fixture or chosen assumptions rather than general capability. External validity therefore remains unconfirmed.
