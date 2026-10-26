import unittest
from edna.core import search, answer, evaluate
class RetrievalTest(unittest.TestCase):
    def test_known_query_has_citation(self): self.assertTrue(answer("portfolio risk scenario")["citations"])
    def test_unknown_query_abstains(self): self.assertFalse(answer("quantum banana volcano taxonomy")["citations"])
    def test_concept_not_worse_at_three(self): self.assertGreaterEqual(evaluate("concept")["hit_at_3"],evaluate("lexical")["hit_at_3"])
    def test_empty_corpus_does_not_fall_back(self):
        self.assertEqual(search('risk',corpus=[]),[])
        self.assertFalse(answer('risk',corpus=[])['citations'])
    def test_withdrawn_source_excluded(self):
        corpus=[dict(id='A',path='a',text='risk portfolio',status='withdrawn')]
        self.assertFalse(answer('risk',corpus=corpus)['citations'])
    def test_registered_conflict_abstains(self):
        corpus=[dict(id='A',path='a',text='risk portfolio',contradiction_ids=['CONFLICT-1'])]
        self.assertFalse(answer('risk',corpus=corpus)['citations'])
    def test_duplicate_ids_rejected(self):
        corpus=[dict(id='A',path='a',text='risk')]*2
        with self.assertRaises(ValueError): search('risk',corpus=corpus)
    def test_coverage_is_bounded_and_scope_explicit(self):
        r=evaluate('concept')
        self.assertTrue(0<=r['citation_coverage']<=1)
        self.assertIn('summaries',r['support_scope'])
        with self.assertRaises(ValueError): search('risk','neural')
