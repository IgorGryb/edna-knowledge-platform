"""Bounded EDNA evidence and full-cost review; no external retrieval."""
import hashlib
import json
from pathlib import Path
from edna.core import answer, evaluate

ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT.parents[1]

def main():
    source=ARCHIVE/'standards/validation-cases.yaml'
    case=next(x for x in json.loads(source.read_text())['cases'] if x['project']=='EDNA')
    p=case['inputs']
    manual=p['manual_minutes']/60*p['hourly_cost']
    base=(p['assisted_minutes']+p['review_minutes'])/60*p['hourly_cost']+p['tool_cost']
    negative=(p['assisted_minutes']+case['negative_change']['review_minutes'])/60*p['hourly_cost']+p['tool_cost']
    threshold=p['manual_minutes']-p['assisted_minutes']-60*p['tool_cost']/p['hourly_cost']
    lexical=evaluate('lexical'); concept=evaluate('concept')
    checks=dict(empty=not answer('risk',corpus=[])['citations'],
                unknown=not answer('quantum banana volcano taxonomy')['citations'],
                withdrawn=not answer('risk',corpus=[dict(id='X',path='x',text='risk',status='withdrawn')])['citations'],
                conflict=not answer('risk',corpus=[dict(id='X',path='x',text='risk',contradiction_ids=['C1'])])['citations'])
    assert all(checks.values())
    assert base==case['expected_base'] and negative==case['expected_negative']
    r=dict(id='EDNA-MANAGEMENT-REVIEW-001',data_status='curated-fixture-and-synthetic-costs',
           lexical=lexical,concept_proxy=concept,negative_checks=checks,
           costs=dict(manual=manual,base=base,negative=negative,review_break_even_minutes=threshold,unit=case['unit']),
           source_hashes={'src/edna/core.py':hashlib.sha256((ROOT/'src/edna/core.py').read_bytes()).hexdigest(),
                          str(source.relative_to(ARCHIVE)):hashlib.sha256(source.read_bytes()).hexdigest()},
           limitations=['Not a semantic embedding benchmark','Citation existence is not factual accuracy','Review time assumed, not measured','Registered contradictions only'])
    (ROOT/'artifacts/management-review.json').write_text(json.dumps(r,indent=2)+'\n')
    lines=['# EDNA — validation and decision memo','',
           'Private bounded design study. Five authored retrieval questions, six curated summaries and synthetic cost assumptions; no external market or user trial.','',
           '## Evidence quality','',
           f"Both lexical and concept-expansion modes achieve hit@1 {lexical['hit_at_1']:.0%}, hit@3 {lexical['hit_at_3']:.0%} and MRR {lexical['mrr']:.2f} on this fixture. There is no demonstrated ranking improvement.",
           f"Measured citation coverage is {lexical['citation_coverage']:.0%} for lexical and {concept['citation_coverage']:.0%} for concept expansion. Exact-summary support has the same rates. This measures extracted summary support, not correctness against the original documents or relevance of every answer.",
           'The original no-worse-at-three prediction passes, but it is a weak acceptance condition and does not justify investing in a semantic platform.',
           'Empty corpus, unsupported query, withdrawn source and registered conflict all produce abstention. Duplicate IDs and unsupported modes are rejected in regression tests. Novel contradictions are not detected automatically.','',
           '## Economics and decision boundary','',
           f"At the declared synthetic cost assumptions, manual review costs EUR {manual:.2f} per accepted note; assisted preparation plus review and tools costs EUR {base:.2f}. With 60 review minutes the assisted cost becomes EUR {negative:.2f}.",
           f"The break-even review time is {threshold:.2f} minutes at the same acceptance quality. Time beyond that threshold eliminates the assumed saving. Ingestion and maintenance are not measured; allocate them before claiming net benefit.",
           'The pre-recorded cost forecast matches arithmetic, not observed productivity. A higher cited-answer rate can simply mean less abstention; it is not automatically a quality improvement.','',
           '## Recommendation','',
           'Continue with a controlled local evidence workflow and explicit review; do not scale or buy a hosted retrieval service on this result. For the next supplied corpus, define approved passages and expected answers before running the comparison, record manual and assisted review time, and include stale, conflicting and out-of-scope questions.',
           'Pause a note when required evidence or permission is missing. Prefer manual review if the full assisted cost exceeds it at the same quality. Preserve advanced retrieval techniques as options conditional on a demonstrated bottleneck.','',
           '## Post-mortem and handoff','',
           'Corrected the inaccurate TF-IDF label, hard-coded citation coverage and empty-list fallback. Added explicit source-summary scope, excerpt hashes, withdrawn-source filtering and conflict abstention. These changes improve auditability within this narrow reference.',
           'Handoff: DELIVERY-SPECIFICATION.md, MODEL-CARD.md, core.py, tests and artifacts/management-review.json. Roles and external integrations are proposed. No original course material is copied into an outward-facing case study.']
    (ROOT/'docs/MODEL-VALIDATION-MEMO.md').write_text('\n'.join(lines)+'\n')
    print(json.dumps(r,indent=2))

if __name__=='__main__': main()
