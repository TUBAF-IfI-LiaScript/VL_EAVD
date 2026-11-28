"""Prüfungen an den Grenzen für die Funktionen aus Vorlesung 07.

Kleine, von Hand gebaute Werte statt der echten Dateien: So weiß man das
richtige Ergebnis, bevor man rechnet.
"""

MINDESTTAGE = 300


def ist_frosttag(minimum):
    return minimum != -999 and minimum < 0


def mittel_frost(frost, messtage, start):
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


# ist_frosttag: knapp unter 0, genau 0, Fehlwert
assert ist_frosttag(-0.1) == True
assert ist_frosttag(0.0) == False
assert ist_frosttag(-999) == False

# mittel_frost: genau 300 Messtage zählt, 299 nicht, ganz ohne Daten None
assert mittel_frost({"1961": 100}, {"1961": 300}, 1961) == 100
assert mittel_frost({"1961": 100}, {"1961": 299}, 1961) == None
assert mittel_frost({}, {}, 1995) == None
# Jahre außerhalb des Zeitraums zählen nicht mit
frost = {"1990": 80, "1991": 200}
messtage = {"1990": 365, "1991": 365}
assert mittel_frost(frost, messtage, 1961) == 80

print("Alle Prüfungen bestanden.")
