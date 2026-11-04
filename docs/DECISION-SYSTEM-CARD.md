# EDNA — karta systemu decyzyjnego

ID: `PXP-PRJ-EDNA`  
Status: prywatne studium projektu z ograniczoną walidacją; nie produkcyjny RAG ani niezależny silnik prawdy.

## Znaczenie dla decyzji

EDNA organizuje pochodzenie, retrieval, review i sprzeczności tak, aby model
lub decyzja mogły wskazać źródło, lukę i ograniczenie. Główny wektor: dane,
dowód, modelowanie i workflow AI; wzmacniające: operacje/produkt i kapitał/ryzyko.

## Mapa systemu

`źródło → identyfikator i provenance → retrieval → cytowanie/abstention →
review sprzeczności → zatwierdzona informacja dla decyzji → rewizja`.

## Dowód i wkład

Pakiet zawiera ograniczony korpus, specyfikację, test report, source map i
dossier. Wkład formalizuje zasady użycia źródeł i kontroli błędów; nie dowodzi
skali, jakości dla nieznanego korpusu ani produkcyjnego wdrożenia.

## Model i hipoteza integracji

Mechanizm odróżnia relewancję retrieval od wsparcia cytowaniem i nie pozwala
automatyzacji usunąć ludzkiego review. Hipoteza: wobec manualnego lub prostego
leksykalnego baseline'u może obniżyć koszt weryfikacji przy zachowaniu jakości
proweniencji. Koszt review i ryzyko skorelowanych/starych źródeł są częścią testu.

## Test i następna opcja

Najtańszy test porównuje manual, lexical i assisted retrieval na tych samych
pytaniach: citation support, missing evidence, contradictions i review time.
Następna opcja to wyłącznie zatwierdzony lokalny korpus z testem source change
i access control.

## Rdzeń biznesowy i standard architektury

**Wizja ze źródła (koncepcja historyczna):** A project-based learning and knowledge ecosystem for learners, creators and institutions, with structured instructions and reusable materials.

**Pierwsze ograniczone zastosowanie:** An approved local corpus: compare manual, lexical and assisted retrieval for citation support, correction handling and review cost.

**Model komercyjny (hipoteza):** An institutional knowledge/learning workspace subscription with curation and review cost explicit; creator monetization is a later option and demand is unvalidated.

**Jednostki i czynniki ekonomiczne:** curation and ingest cost per source; search and compute cost per query; review time per accepted note; correction and reindex cost; adoption and reuse frequency.

**Wykonany zakres:** A small local retrieval demonstration with lexical matching and concept expansion proxy; no production neural retrieval.

**Architektura referencyjna (projekt, bez wdrożenia):** Document ingestion, stable source IDs, metadata and permissions, search, citations, human review, change tracking and audit trail.

**Opcje odroczone:** Production RAG, enterprise integrations, full learning marketplace and autonomous recommendations.

| Model | Zastosowanie w tym przypadku |
|---|---|
| Techniczny | Source-versioned ingestion and inspectable retrieval/review components. |
| Biznesowy i produktowy | Institutional learning and knowledge subscription hypothesis rooted in project-based education. |
| Operacyjny | Source steward, reviewer and learning owner govern intake, correction and reuse. |
| Finansowy | Compare cost per accepted research/learning unit with manual workflow. |
| Ryzyko i governance | Enforce access, citation support, abstention and source-change review. |

**Źródła rozwoju:** IBM — IBM Data Architecture (`recorded_completed`); IBM — IBM RAG and Agentic AI (`recorded_completed`); Microsoft — Microsoft Data Architecture for Modern Data Stacks (`recorded_completed`); Johns Hopkins University — Advanced Statistics for Data Science (`recorded_completed`); Stanford Online — From Product Strategy to Product Leadership (`recorded_completed`). Są to odnotowane ukończenia programów i kandydackie połączenia zastosowań; nie stanowią samodzielnego dowodu wdrożenia lub biegłości. **Metody z zapisanym zakresem odczytu:** `M-SIPOC`, `M-RACI`, `M-MOSCOW`, `M-FEASIBILITY`, `M-MEASURE`.

## Granice i źródła

Nie przedstawiać jako wdrożonej platformy danych, AI-performance claim ani
automatycznej rekomendacji. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[test report](TEST-REPORT.md), [source map](SOURCE-MAP.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
