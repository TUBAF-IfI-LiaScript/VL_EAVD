"""Frosttage pro Jahr auf dem Fichtelberg und Mittelwerte für drei Zeiträume
(Abschnitt „Ergebnis“).
Aus Vorlesung 06 „Dateien lesen“. Starten im Ordner examples/06_DateienLesen."""

dateiname = ("../../data/fichtelberg/"
             "produkt_klima_tag_18900801_20251231_01358.txt")
frost = {}
messtage = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        minimum = float(teile[16])
        if jahr not in frost:
            frost[jahr] = 0
            messtage[jahr] = 0
        if minimum != -999:
            messtage[jahr] = messtage[jahr] + 1
            if minimum < 0:
                frost[jahr] = frost[jahr] + 1

for start in [1891, 1961, 1995]:
    summe = 0
    anzahl = 0
    for jahr in range(start, start + 30):
        schluessel = str(jahr)
        if schluessel in frost and messtage[schluessel] >= 300:
            summe = summe + frost[schluessel]
            anzahl = anzahl + 1
    print(start, "bis", start + 29, "→", round(summe / anzahl, 1),
          "Frosttage aus", anzahl, "Jahren")
