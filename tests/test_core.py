import unittest
from edna.core import search, answer, evaluate
class RetrievalTest(unittest.TestCase):
    def test_known_query_has_citation(self): self.assertTrue(answer("portfolio risk scenario")["citations"])
    def test_unknown_query_abstains(self): self.assertFalse(answer("quantum banana volcano taxonomy")["citations"])
    def test_concept_not_worse_at_three(self): self.assertGreaterEqual(evaluate("concept")["hit_at_3"],evaluate("lexical")["hit_at_3"])
