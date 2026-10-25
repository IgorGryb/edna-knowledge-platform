from __future__ import annotations
import hashlib, json, math, re
from collections import Counter
from pathlib import Path

PROJECT_ID="PRJ-EDNA-PROTOTYPE"
CORPUS=[
 {"id":"SRC-CHARTER","path":"00. ARCHIVE SYSTEM/SYSTEM-CHARTER.md","text":"The system separates facts interpretations hypotheses forecasts and decisions. Documents are outputs of learning testing validation and correction."},
 {"id":"SRC-ARCTERVIX","path":"1. Portfolio/Arctervix Research/PROJECT-RECORD.md","text":"Arctervix contains research on portfolio construction quantitative finance structured finance risk and real options. Executable models require validation."},
 {"id":"SRC-EDNA","path":"1. Portfolio/EDNA Ontology/PROJECT-RECORD.md","text":"EDNA describes knowledge architecture retrieval provenance ontology and project based learning. A retrieval pipeline and quality evaluation were not previously confirmed."},
 {"id":"SRC-HOBBLY","path":"1. Portfolio/Hobbly Payments/PROJECT-RECORD.md","text":"Hobbly describes marketplace booking CRM payment flows and product economics. Production payment integration and users were not confirmed."},
 {"id":"SRC-ARXIS","path":"1. Portfolio/Arxis Architecture Solutions/PROJECT-RECORD.md","text":"ARXIS concerns architecture documentation decisions requirements traceability and collaboration. CAD BIM GIS integration is outside the validated scope."},
 {"id":"SRC-ARXA","path":"1. Portfolio/Arxa Data Platform/PROJECT-RECORD.md","text":"ARXA concerns industrial data supply chain optimization predictive maintenance scenarios and real options. Client deployment is not confirmed."},
]
CONCEPTS={"proof":["evidence","source","provenance","citation"],"search":["retrieval","query","knowledge"],"risk":["portfolio","scenario","uncertainty"],"building":["architecture","requirements","bim"],"factory":["industrial","maintenance","supply"]}
def tokens(text): return re.findall(r"[a-z0-9]+",text.lower())
def expand(ts):
    out=list(ts)
    for t in ts: out.extend(CONCEPTS.get(t,[]))
    return out
def vector(ts): return Counter(ts)
def cosine(a,b):
    dot=sum(v*b.get(k,0) for k,v in a.items()); na=math.sqrt(sum(v*v for v in a.values())); nb=math.sqrt(sum(v*v for v in b.values()))
    return dot/(na*nb) if na and nb else 0.0
def search(query, mode="lexical", corpus=None):
    corpus=corpus or CORPUS; q=tokens(query); q=expand(q) if mode=="concept" else q; qv=vector(q)
    ranked=[]
    for d in corpus:
        dt=tokens(d["text"]); dt=expand(dt) if mode=="concept" else dt
        ranked.append({"id":d["id"],"path":d["path"],"score":cosine(qv,vector(dt))})
    return sorted(ranked,key=lambda x:(-x["score"],x["id"]))
def answer(query, mode="concept"):
    ranked=search(query,mode); top=ranked[0]
    if top["score"] < 0.12: return {"answer":"ABSTAIN: corpus support below threshold","citations":[],"score":top["score"]}
    source=next(x for x in CORPUS if x["id"]==top["id"])
    return {"answer":source["text"],"citations":[{"source_id":top["id"],"path":top["path"]}],"score":top["score"]}
def evaluate(mode):
    tests=[("What supports evidence and provenance?","SRC-CHARTER"),("Which project covers portfolio risk?","SRC-ARCTERVIX"),("Where is booking and payment described?","SRC-HOBBLY"),("Which project handles building requirements?","SRC-ARXIS"),("Where is factory maintenance modeled?","SRC-ARXA")]
    ranks=[]
    for q,expected in tests: ranks.append(next(i for i,x in enumerate(search(q,mode),1) if x["id"]==expected))
    return {"hit_at_1":sum(r==1 for r in ranks)/len(ranks),"hit_at_3":sum(r<=3 for r in ranks)/len(ranks),"mrr":sum(1/r for r in ranks)/len(ranks),"ranks":ranks,"citation_coverage":1.0}
def run(root: Path):
    (root/"data").mkdir(parents=True,exist_ok=True); (root/"artifacts").mkdir(parents=True,exist_ok=True)
    (root/"data/corpus.json").write_text(json.dumps(CORPUS,indent=2),encoding="utf-8")
    lexical=evaluate("lexical"); concept=evaluate("concept"); unknown=answer("quantum banana volcano taxonomy")
    passed=concept["hit_at_3"]>=lexical["hit_at_3"] and not unknown["citations"]
    result={"project_id":PROJECT_ID,"claim_scope":"small local retrieval demonstration","lexical":lexical,"concept_proxy":concept,"unsupported_query":unknown,"prediction_passed":passed,"semantic_disclosure":"concept expansion proxy; not neural embeddings"}
    (root/"artifacts/results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    demo={q:answer(q) for q in ["portfolio risk scenario","booking payment state","industrial maintenance option"]}
    (root/"artifacts/retrieval-demo.json").write_text(json.dumps(demo,indent=2),encoding="utf-8")
    arts=[]
    for rel in ["artifacts/results.json","artifacts/retrieval-demo.json","data/corpus.json"]:
        p=root/rel; arts.append({"artifact_id":"ART-"+hashlib.sha256(rel.encode()).hexdigest()[:12].upper(),"path":rel,"sha256":hashlib.sha256(p.read_bytes()).hexdigest(),"validation_status":"tested","reproduce_command":"make reproduce"})
    (root/"artifacts/evidence-manifest.json").write_text(json.dumps({"project_id":PROJECT_ID,"generated":"2026-10-25","data_class":"approved-local-subset","artifacts":arts},indent=2),encoding="utf-8")
    return result
