"""Frosttage im Vergleich: Fichtelberg, Chemnitz und Freiberg.

Programm aus dem Live Hacking von Vorlesung 07. Starten Sie es in diesem
Ordner, die Daten liegen in ../../data/.
"""

MINDESTTAGE = 300          # weniger Messtage: Jahr zählt nicht

STATIONEN = {
    "Fichtelberg": ("../../data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "Chemnitz": ("../../data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
    "Freiberg": ("../../data/freiberg/"
                 "produkt_klima_tag_19450701_19930430_01441.txt"),
}


def auswerten(dateiname):
    """Frosttage und Messtage pro Jahr aus einer DWD-Datei."""
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
    return frost, messtage


def mittel_frost(frost, messtage, start):
    """Mittlere Frosttage über 30 Jahre ab start, None ohne Daten."""
    summe = 0
    anzahl = 0
    for jahr in range(start, start + 30):
        schluessel = str(jahr)
        if schluessel in frost and messtage[schluessel] >= MINDESTTAGE:
            summe = summe + frost[schluessel]
            anzahl = anzahl + 1
    if anzahl == 0:
        return None
    return round(summe / anzahl, 1)


for name in STATIONEN:
    frost, messtage = auswerten(STATIONEN[name])
    for start in [1961, 1995]:
        print(name, start, "bis", start + 29, "→",
              mittel_frost(frost, messtage, start), "Frosttage")
