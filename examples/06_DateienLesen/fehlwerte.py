"""Liest ausschnitt.txt, überspringt die Kopfzeile und erkennt den Fehlwert -999.
Aus Vorlesung 06 „Dateien lesen“. Starten im Ordner examples/06_DateienLesen."""

dateiname = "ausschnitt.txt"
with open(dateiname) as datei:
    datei.readline()                  # Kopfzeile überspringen
    for zeile in datei:
        teile = zeile.split(";")
        datum = teile[1]
        minimum = float(teile[16])
        if minimum == -999:
            print(datum, "kein Wert")
        else:
            print(datum, minimum)
