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

## Granice i źródła

Nie przedstawiać jako wdrożonej platformy danych, AI-performance claim ani
automatycznej rekomendacji. Źródła: [dossier zarządcze](MANAGEMENT-DOSSIER.md),
[test report](TEST-REPORT.md), [source map](SOURCE-MAP.md) i
[rejestr pozycji](../../../00.%20ARCHIVE%20SYSTEM/portfolio/CONVEX-POSITION-REGISTER.yaml).
