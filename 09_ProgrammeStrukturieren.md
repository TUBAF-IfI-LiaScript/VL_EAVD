<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Programme strukturieren: Eigene Module, import, die Standardbibliothek und externe Pakete — die Brücke zu fremden Bibliotheken.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
          https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md)

# Programme strukturieren

| Parameter                | Kursinformationen                                                                                                                                                |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                  |
| **Semester**             | @config.semester                                                                                                                                                 |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                |
| **Inhalte:**             | `Module, import, __name__, Standardbibliothek (statistics, datetime), Lücken finden, externe Pakete, pip, Pfade`                                                                |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md) |
| **Autoren**              | @author                                                                                                                                                          |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie organisiere ich Code, der wächst?_

**Fragen an die heutige Veranstaltung ...**

* Wie verteilt man Funktionen auf mehrere Dateien?
* Was passiert genau bei `import`?
* Was bringt Python schon mit — und wie kommt man an mehr?
* Warum findet mein Programm seine Datei nicht?

> Die Beispiele mit mehreren Dateien laufen auf einem Server. Der erste Klick auf "Ausführen" kann einige Sekunden dauern.

--------------------------------------------------------------------------------

## Rückblick

Willkommen zurück nach der Weihnachtspause. Vor der Demonstration in Vorlesung 08 haben wir das lange Skript in Funktionen zerlegt:

```python
for station, datei in [("fichtelberg", DATEI_FICHTELBERG),
                       ("freiberg", DATEI_FREIBERG)]:
    hoechst, frost, gemessen = auswerten(datei)
    schreibe_ergebnis(station + "_jahre.csv", hoechst, frost, gemessen)
```

Das Hauptprogramm ist kurz. Aber die Funktionen stehen noch in derselben Datei. Wer morgen eine **andere** Auswertung schreibt — etwa nur Frosttage im Januar —, muss `zerlege_zeile` und `auswerten` wieder hineinkopieren. Kopieren war genau das, was wir vermeiden wollten.

## Ein eigenes Modul

Ein **Modul** ist eine gewöhnliche Python-Datei, deren Funktionen andere Programme benutzen können. Wir legen die Hilfsfunktionen in `dwd.py` ab:

```python dwd.py
def ist_fehlwert(wert):
    return wert == -999


def zerlege_zeile(zeile):
    teile = zeile.split(";")
    return teile[1][0:4], float(teile[15]), float(teile[16])
```
```python auswertung.py
import dwd

zeile = "  1358;19101209;-999;-999;-999; 1; 2.7; 1;-999; 100; 7.0; 5.9; 863.90; 1.4; 89.00; 4.3; -2.8;-999;eor"
jahr, maximum, minimum = dwd.zerlege_zeile(zeile)
print(jahr, maximum, minimum)
print("Fehlwert?", dwd.ist_fehlwert(minimum))
```
@LIA.eval(`["dwd.py", "auswertung.py"]`, `none`, `python3 auswertung.py`)

* `import dwd` sucht eine Datei `dwd.py` — zuerst im selben Ordner wie das Programm.
* Die Funktionen des Moduls ruft man mit vorangestelltem Modulnamen auf: `dwd.zerlege_zeile(...)`.
* Alternativ holt `from dwd import zerlege_zeile` einen einzelnen Namen direkt herein. Dann entfällt das `dwd.` — man sieht beim Lesen aber nicht mehr, woher die Funktion stammt.

> Der Modulname ist der Dateiname **ohne** `.py`. Deshalb gelten für Dateinamen dieselben Regeln wie für Variablen: keine Leerzeichen, keine Bindestriche, nicht mit einer Ziffer beginnen.

### Typische Fehlvorstellung: `import` kopiert nur Funktionen

> **Typische Fehlvorstellung:** _„Bei `import` holt sich Python die Funktionen — der Rest der Datei spielt keine Rolle.“_

Jemand hat ans Ende von `dwd.py` noch einen schnellen Test geschrieben:

```python dwd.py
def ist_fehlwert(wert):
    return wert == -999

print("Test:", ist_fehlwert(-999))
```
```python auswertung.py
import dwd

print("Auswertung beginnt")
print(dwd.ist_fehlwert(3.5))
```
@LIA.eval(`["dwd.py", "auswertung.py"]`, `none`, `python3 auswertung.py`)

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was erscheint als Erstes?

[(X)] `Test: True`
[( )] `Auswertung beginnt`
[( )] `False`
***
`import dwd` **führt die ganze Datei `dwd.py` aus** — einmal, von oben nach unten. Die `def`-Zeilen legen dabei die Funktionen an; das `print` am Ende wird ebenfalls ausgeführt.

Soll Testcode nur laufen, wenn man `dwd.py` **direkt** startet, gehört er in einen besonderen Block:

```python
if __name__ == "__main__":
    print("Test:", ist_fehlwert(-999))
```

`__name__` ist `"__main__"`, wenn die Datei selbst gestartet wird, und `"dwd"`, wenn sie importiert wird.
***

## Live Hacking: Das Modul `dwd.py`

> **Live Hacking.** In der Vorlesung verschieben wir die Funktionen aus Vorlesung 07 in `dwd.py` und schreiben ein neues, kurzes Auswerteprogramm. Als Beleg, dass sich der Umbau lohnt, kommt eine dritte Station hinzu: **Chemnitz**.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
for datei in ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
              "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt",
              "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt"]:
    os.makedirs(os.path.dirname(datei), exist_ok=True)
    urllib.request.urlretrieve(basis + datei, datei)
```
```python -dwd.py
"""Hilfsfunktionen für Klima-Tageswerte des Deutschen Wetterdienstes."""

FEHLWERT = -999
MINDESTTAGE = 300          # weniger gemessene Tage: kein Frostwert


def zerlege_zeile(zeile):
    """Liefert Jahr, Tagesmaximum und Tagesminimum einer DWD-Zeile."""
    teile = zeile.split(";")
    return teile[1][0:4], float(teile[15]), float(teile[16])


def auswerten(datei):
    """Höchstwert, Frosttage und gemessene Tage pro Jahr."""
    hoechst = {}
    frost = {}
    gemessen = {}
    with open(datei) as f:
        f.readline()
        for zeile in f:
            jahr, maximum, minimum = zerlege_zeile(zeile)
            if jahr not in frost:
                frost[jahr] = 0
                gemessen[jahr] = 0
            if maximum != FEHLWERT:
                if jahr not in hoechst or maximum > hoechst[jahr]:
                    hoechst[jahr] = maximum
            if minimum != FEHLWERT:
                gemessen[jahr] = gemessen[jahr] + 1
                if minimum < 0:
                    frost[jahr] = frost[jahr] + 1
    return hoechst, frost, gemessen


def schreibe_ergebnis(name, hoechst, frost, gemessen):
    """Eine Zeile pro Jahr; ohne Frostwert, wenn zu wenig gemessen wurde."""
    with open(name, "w") as f:
        f.write("jahr;maximum;frosttage\n")
        for jahr in hoechst:
            if gemessen[jahr] >= MINDESTTAGE:
                f.write(jahr + ";" + str(hoechst[jahr]) + ";" + str(frost[jahr]) + "\n")
            else:
                f.write(jahr + ";" + str(hoechst[jahr]) + ";\n")


if __name__ == "__main__":
    assert zerlege_zeile(" 1;20240813;" + "0;" * 13 + "26.9;12.0;0;eor") == ("2024", 26.9, 12.0)
    print("dwd.py: Selbsttest bestanden")
```
```python auswertung.py
import dwd

STATIONEN = {
    "fichtelberg": "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
    "freiberg":    "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt",
    "chemnitz":    "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt",
}

for station in STATIONEN:
    hoechst, frost, gemessen = dwd.auswerten(STATIONEN[station])
    dwd.schreibe_ergebnis(station + "_jahre.csv", hoechst, frost, gemessen)
    print(station, len(hoechst), "Jahre, 2024:", frost.get("2024"), "Frosttage")
```
@LIA.eval(`["hole_daten.py", "dwd.py", "auswertung.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 auswertung.py"`)

* `auswertung.py` enthält nur noch, **was** ausgewertet wird. **Wie** eine DWD-Datei gelesen wird, steht in `dwd.py`.
* Die Stationen stehen in einem Dictionary: Name → Datei. Eine vierte Station ist eine Zeile.
* `frost.get("2024")` liefert `None` statt eines `KeyError`, wenn es den Schlüssel nicht gibt — Freiberg hat 2024 nicht gemessen.
* Der Selbsttest am Ende von `dwd.py` läuft nur, wenn man `python3 dwd.py` startet.

## Die Standardbibliothek

Python bringt über 200 Module mit — die **Standardbibliothek**. Sie sind auf jedem Rechner mit Python vorhanden; `import` genügt.

<!-- data-type="none" -->
| Modul        | Wofür                                   | Beispiel                            |
| :----------- | :-------------------------------------- | :---------------------------------- |
| `math`       | mathematische Funktionen                | `math.sqrt(2)`, `math.pi`           |
| `statistics` | Mittelwert, Median, Standardabweichung  | `statistics.median(werte)`          |
| `datetime`   | Datum und Uhrzeit                       | Abstand zwischen zwei Tagen          |
| `os`         | Dateien und Ordner                      | `os.path.exists("data")`            |
| `csv`        | CSV-Dateien lesen und schreiben         | (wir haben es von Hand gemacht)     |

**Statistik** — die Jahreshöchstwerte 2015 bis 2024 aus Vorlesung 05:

```python
import statistics

hoechst = [28.1, 24.8, 26.8, 26.7, 29.5, 26.9, 24.5, 29.1, 28.4, 26.9]
print("Mittel:", statistics.mean(hoechst))
print("Median:", statistics.median(hoechst))
print("Standardabweichung:", round(statistics.stdev(hoechst), 2))
```
@Pyodide.eval

**Datum** — wie groß ist die Lücke aus Vorlesung 06 wirklich?

```python
from datetime import datetime

vorher = datetime.strptime("19101210", "%Y%m%d")
nachher = datetime.strptime("19151001", "%Y%m%d")
luecke = nachher - vorher
print("Lücke:", luecke.days, "Tage")
```
@Pyodide.eval

> `strptime` übersetzt einen Text anhand eines Formats in ein Datum: `%Y` Jahr, `%m` Monat, `%d` Tag. Mit Daten kann man rechnen — mit Texten wie `"19101210"` nicht. So lassen sich Lücken in jeder Messreihe automatisch finden: Wenn der Abstand zweier Folgezeilen größer als ein Tag ist, fehlt etwas.

## Live Hacking: Lücken finden

In Vorlesung 06 haben wir eine Lücke in den Fichtelberg-Daten **zufällig** im Ausschnitt entdeckt. Gibt es weitere — und wie steht es um Freiberg und Chemnitz? Durchsehen kann man 48.000 Zeilen nicht. Ein Programm schon.

> **Live Hacking.** In der Vorlesung erweitern wir `dwd.py` um eine Funktion, die alle Lücken meldet. Die Versuche unten zeigen den typischen Irrweg.

### Typische Fehlvorstellung: Ein Datum ist eine Zahl

> **Typische Fehlvorstellung:** _„`19101231` ist eine Zahl — also kann ich zwei Daten einfach voneinander abziehen.“_

```python
vorher = 19101231
nachher = 19110101
print(nachher - vorher)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[( )] `1`
[(X)] `8870`
[( )] eine Fehlermeldung
***
Python rechnet mit der Zahl neunzehn Millionen hunderteinunddreißigtausend… — nicht mit einem Datum. Silvester und Neujahr liegen einen Tag auseinander, die Zahlen aber 8870. Monatslängen, Schaltjahre und Jahreswechsel kennt nur ein echter Datumstyp. Deshalb `datetime`.
***

### Die Funktion `finde_luecken`

```python dwd.py
from datetime import datetime


def finde_luecken(datei):
    """Liefert (vorher, nachher, fehlende Tage) für jede Lücke."""
    luecken = []
    vorher = None
    with open(datei) as f:
        f.readline()
        for zeile in f:
            datum = datetime.strptime(zeile.split(";")[1], "%Y%m%d")
            if vorher is not None and (datum - vorher).days > 1:
                luecken.append((vorher, datum, (datum - vorher).days - 1))
            vorher = datum
    return luecken
```
```python auswertung.py
import dwd

STATIONEN = {
    "fichtelberg": "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
    "freiberg":    "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt",
    "chemnitz":    "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt",
}

for station in STATIONEN:
    for vorher, nachher, tage in dwd.finde_luecken(STATIONEN[station]):
        print(station, vorher.date(), "bis", nachher.date(), "— fehlende Tage:", tage)
```
```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
for datei in ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
              "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt",
              "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt"]:
    os.makedirs(os.path.dirname(datei), exist_ok=True)
    urllib.request.urlretrieve(basis + datei, datei)
```
@LIA.eval(`["dwd.py", "auswertung.py", "hole_daten.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 auswertung.py"`)

Drei Ideen stecken darin:

* **`vorher = None`** — beim ersten Datum gibt es noch kein vorheriges. `None` kennen Sie aus Vorlesung 07.
* **`(datum - vorher).days`** — die Differenz zweier Daten ist eine Zeitspanne; `.days` liefert sie in Tagen.
* **Eine Liste von Tupeln** — jede Lücke besteht aus drei zusammengehörigen Werten, die die Schleife unten mit `vorher, nachher, tage` wieder auspackt (Vorlesung 07: mehrere Rückgabewerte).

**Was das Programm findet**

Sieben Lücken in drei Stationen. Zwei davon kennen wir, eine ist spektakulär, eine ist winzig:

* Chemnitz: von Juni 1901 bis Ende 1934 fehlen **33 Jahre** — 12.267 Tage.
* Freiberg: am 30. August 1977 fehlt **ein einziger Tag**. Unter 17.000 Zeilen hätte ihn niemand mit bloßem Auge gefunden.

Zwischen dem 10.12.1910 und dem 01.10.1915 liegen 1756 Tage Abstand. Wie viele Tage fehlen in der Datei?

[[1755]]
[[?]] Der 10.12.1910 und der 01.10.1915 sind selbst in der Datei enthalten.
***
Der Abstand zweier Tage ist um eins größer als die Zahl der Tage dazwischen — deshalb `(datum - vorher).days - 1`. Derselbe Fehler um eins wie bei `range` und Slices in Vorlesung 05.
***

## Externe Pakete

Was nicht in der Standardbibliothek steht, installiert man als **Paket** aus dem Python Package Index (PyPI). Im Terminal:

```bash
pip install numpy
```

Danach funktioniert `import numpy` genau wie `import dwd` — nur dass die Dateien nicht im eigenen Ordner liegen, sondern dort, wohin `pip` sie installiert hat.

<!-- data-type="none" -->
| Woher kommt das Modul? | Beispiel         | Was ist zu tun?                          |
| :--------------------- | :--------------- | :--------------------------------------- |
| eigene Datei           | `import dwd`     | Datei in den Ordner des Programms legen   |
| Standardbibliothek     | `import datetime` | nichts                                   |
| externes Paket         | `import pandas`  | einmalig `pip install pandas`            |

> Fehlt ein Paket, meldet Python `ModuleNotFoundError: No module named 'pandas'`. Die Lösung ist fast immer `pip install ...` — nicht, den Code zu ändern.

## Typische Fehlvorstellung: Pfade

> **Typische Fehlvorstellung:** _„Ein Dateiname im Programm bezieht sich auf den Ordner, in dem das Programm liegt.“_

Ihr Projekt sieht so aus:

``` ascii
VL_EAVD/
├── auswertung.py          ← enthält open("data/fichtelberg/...")
├── dwd.py
└── data/
    └── fichtelberg/
        └── produkt_klima_tag_18900801_20251231_01358.txt
```

Sie öffnen ein Terminal in Ihrem Home-Verzeichnis und starten `python VL_EAVD/auswertung.py`. Was passiert?

[( )] Das Programm läuft, weil `data/` neben `auswertung.py` liegt.
[(X)] `FileNotFoundError` — Python sucht `data/...` im Home-Verzeichnis.
[( )] `ModuleNotFoundError` für `dwd`.
***
Relative Pfade wie `"data/fichtelberg/..."` beziehen sich auf das **aktuelle Arbeitsverzeichnis** — den Ordner, in dem das Terminal gerade steht —, nicht auf den Ordner des Programms. `import dwd` dagegen funktioniert, weil Python Module im Ordner des gestarteten Programms sucht. Deshalb kann ein Programm seine Module finden und trotzdem an seinen Daten scheitern.

Abhilfe: Das Terminal im Projektordner öffnen (`cd VL_EAVD`), oder in Visual Studio Code den Projektordner öffnen, bevor Sie auf ▷ klicken.
***

## Kontrollfragen

**Welche Aussagen über `import dwd` stimmen?**

[[X]] Python sucht zuerst eine Datei `dwd.py` im Ordner des gestarteten Programms.
[[X]] Der Code in `dwd.py` wird beim Import einmal vollständig ausgeführt.
[[ ]] Danach kann man `auswerten(...)` ohne Vorsilbe aufrufen.
[[X]] Code unter `if __name__ == "__main__":` läuft beim Import nicht.
[[ ]] `import dwd.py` ist die korrekte Schreibweise.

**Was gibt dieses Programm aus?**

```python
stationen = {"fichtelberg": 1213, "freiberg": 380}
print(stationen.get("chemnitz"), stationen.get("freiberg"))
```

[( )] eine Fehlermeldung (`KeyError`)
[(X)] `None 380`
[( )] `0 380`
***
`get` liefert `None`, wenn der Schlüssel fehlt — anders als `stationen["chemnitz"]`, das einen `KeyError` auslöst. Und `None` ist nicht `0`: "kein Eintrag" ist etwas anderes als "null" (Vorlesung 06).
***

**Ordnen Sie zu: Was ist nötig, damit der Import funktioniert?**

[ [nichts] [Datei ins Projekt legen] [pip install] ]
[   (X)          ( )                     ( )     ] `import statistics`
[   ( )          (X)                     ( )     ] `import dwd`
[   ( )          ( )                     (X)     ] `import numpy`
[   (X)          ( )                     ( )     ] `from datetime import datetime`

## Nächste Woche

Mit dieser Vorlesung endet Phase 1. Ab nächster Woche arbeiten wir mit Paketen, die andere für genau unsere Art von Aufgaben geschrieben haben — weiter in Visual Studio Code, ergänzt um Zellen für die schrittweise Datenanalyse.

**Zur Vorbereitung**

- [ ] Legen Sie `dwd.py` und `auswertung.py` im Repository-Ordner an und bringen Sie das Programm auf Ihrem Rechner zum Laufen.
- [ ] Ändern Sie `finde_luecken` so, dass nur Lücken von mehr als 30 Tagen gemeldet werden. Wie viele Tage fehlen bei Chemnitz insgesamt?
- [ ] Installieren Sie mit `pip install numpy pandas matplotlib` die Pakete für Phase 2.
