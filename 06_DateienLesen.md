<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Dateien lesen: Die DWD-Rohdatei mit Bordmitteln einlesen — Zeilen zerlegen, Fehlwerte behandeln, Ergebnisse schreiben.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md)

# Dateien lesen

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `open, with, readline, Zeilen zerlegen mit split, Fehlwerte, Lücken, Dictionary, Dateien schreiben`                                                |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie kommen 48.000 Zeilen in mein Programm?_

**Fragen an die heutige Veranstaltung ...**

* Wie öffnet und liest man eine Textdatei?
* Wie zerlegt man eine Zeile in ihre Spalten?
* Was tut man mit Kopfzeile, Fehlwerten und Lücken?
* Wie schreibt man ein Ergebnis in eine neue Datei?

> Die Beispiele heute laufen auf einem Server, genau wie Python auf Ihrem Rechner — einschließlich echter Dateien. Der erste Klick auf "Ausführen" kann einige Sekunden dauern, bis der Server bereit ist.

--------------------------------------------------------------------------------

## Rückblick

In den Vorlesungen 03 bis 05 kamen die Werte vorbereitet an: eine Spalte, ein Wert pro Zeile, geholt mit `open_url` — und das funktioniert nur im Browser.

Heute nehmen wir die Datei, wie der DWD sie liefert:

```text produkt_klima_tag_18900801_20251231_01358.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18900801;-999;-999;-999;    1;   0.0;   0;-999;-999;   2.0;  13.2;    -999;   15.6;   67.00;   19.6;   10.0;-999;eor
```

Ihre Vorbereitungsaufgabe war, die Schritte zu beschreiben, mit denen man aus einer Zeile das Datum und das Tagesmaximum `TXK` gewinnt. Genau diese Schritte setzen wir heute um:

1. Datei öffnen und Zeile für Zeile lesen
2. Kopfzeile überspringen
3. Zeile an den Semikolons zerlegen
4. Die richtigen Spalten auswählen und in Zahlen umwandeln
5. Fehlwerte erkennen

## Eine Datei öffnen

Für die ersten Schritte genügt ein Ausschnitt aus sieben echten Zeilen. Beide Dateien gehören zu einem Projekt: `ausschnitt.txt` liegt neben `main.py`, genau wie auf Ihrem Rechner.

```text ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930310;-999;-999;-999;    1;   3.0;   7;-999;-999;   8.0;   5.1;  868.50;   -2.3;   99.00;   -0.4;   -3.8;-999;eor
       1358;18930311;-999;-999;-999;    1;   1.5;   7;-999;-999;  -999;  -999;    -999;   -999;-999;   -999;   -999;-999;eor
       1358;19101209;-999;-999;-999;    1;   2.7;   1;-999; 100;   7.0;   5.9;  863.90;    1.4;   89.00;    4.3;   -2.8;-999;eor
       1358;19101210;-999;-999;-999;    1;   0.0;   0;-999;  90;   3.3;   7.2;  863.60;    3.8;   90.00;    5.4;    1.0;-999;eor
       1358;19151001;-999;-999;-999;    1;   2.0;   1;-999;   0;   8.0;   7.1;  873.70;    2.0;  100.00;    2.8;    1.0;-999;eor
       1358;19151002;-999;-999;-999;    1;   2.1;   8;-999;   0;   8.0;   6.5;  877.60;    1.0;  100.00;    2.5;    0.4;-999;eor
```
```python main.py
with open("ausschnitt.txt") as f:
    for zeile in f:
        print(zeile)
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

* `open("ausschnitt.txt")` öffnet die Datei zum **Lesen**.
* `with ... as f:` sorgt dafür, dass die Datei nach dem eingerückten Block wieder geschlossen wird — auch wenn unterwegs ein Fehler auftritt.
* `for zeile in f:` liefert die Datei **Zeile für Zeile**, jede als Text.

**Warum ist nach jeder Zeile eine Leerzeile?** Jede Zeile endet mit einem unsichtbaren Zeilenumbruch `\n`. `print` hängt einen zweiten an. Abhilfe: `print(zeile.strip())` — `strip()` entfernt Leerzeichen und Zeilenumbrüche am Anfang und Ende.

## Eine Zeile zerlegen

```text -ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930310;-999;-999;-999;    1;   3.0;   7;-999;-999;   8.0;   5.1;  868.50;   -2.3;   99.00;   -0.4;   -3.8;-999;eor
```
```python main.py
with open("ausschnitt.txt") as f:
    kopf = f.readline()
    zeile = f.readline()

teile = zeile.split(";")
print(len(teile), "Teile")
print(teile)
print("Datum:", teile[1], "Maximum:", teile[15])
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

`f.readline()` liest genau **eine** Zeile. `split(";")` zerlegt sie an jedem Semikolon in eine Liste von Texten. Welche Spalte welchen Index hat, verrät die Kopfzeile:

<!-- data-type="none" -->
| Index | Spalte       | Bedeutung                    |
| ----: | :----------- | :--------------------------- |
| 1     | `MESS_DATUM` | Datum, `JJJJMMTT`            |
| 13    | `TMK`        | Tagesmittel der Temperatur   |
| 15    | `TXK`        | Tagesmaximum                 |
| 16    | `TNK`        | Tagesminimum                 |

> `float("   -0.4")` funktioniert trotz der Leerzeichen — `float` ignoriert sie am Rand. Beim Datum gibt es keine Leerzeichen. Aber bei der Stations-ID (`teile[0]`) schon: Dort wäre `strip()` nötig.

### Typische Fehlvorstellung: Die Zeile ist schon eine Tabelle

> **Typische Fehlvorstellung:** _„Eine Zeile aus der Datei besteht schon aus Spalten.“_

Was liefert `zeile[1]` — **ohne** vorheriges `split`?

[( )] `"18930310"`, die zweite Spalte
[(X)] `" "`, ein einzelnes Leerzeichen
[( )] eine Fehlermeldung
***
Für Python ist die Zeile ein **Text** wie jeder andere. `zeile[1]` ist das zweite **Zeichen** — und die Zeile beginnt mit sieben Leerzeichen. Spalten entstehen erst durch `split(";")`. Genau wie in der Tabellenkalkulation beim Import: Ohne Angabe des Trennzeichens landet die ganze Zeile in einer Zelle.
***

## Kopfzeile und Fehlwerte

```text -ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930310;-999;-999;-999;    1;   3.0;   7;-999;-999;   8.0;   5.1;  868.50;   -2.3;   99.00;   -0.4;   -3.8;-999;eor
       1358;18930311;-999;-999;-999;    1;   1.5;   7;-999;-999;  -999;  -999;    -999;   -999;-999;   -999;   -999;-999;eor
       1358;19101209;-999;-999;-999;    1;   2.7;   1;-999; 100;   7.0;   5.9;  863.90;    1.4;   89.00;    4.3;   -2.8;-999;eor
       1358;19101210;-999;-999;-999;    1;   0.0;   0;-999;  90;   3.3;   7.2;  863.60;    3.8;   90.00;    5.4;    1.0;-999;eor
       1358;19151001;-999;-999;-999;    1;   2.0;   1;-999;   0;   8.0;   7.1;  873.70;    2.0;  100.00;    2.8;    1.0;-999;eor
       1358;19151002;-999;-999;-999;    1;   2.1;   8;-999;   0;   8.0;   6.5;  877.60;    1.0;  100.00;    2.5;    0.4;-999;eor
```
```python main.py
with open("ausschnitt.txt") as f:
    f.readline()                      # Kopfzeile überspringen
    for zeile in f:
        teile = zeile.split(";")
        datum = teile[1]
        maximum = float(teile[15])
        if maximum == -999:
            print(datum, "kein Wert")
        else:
            print(datum, maximum)
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

Probieren Sie aus, was ohne die Zeile `f.readline()` passiert — und lesen Sie die Fehlermeldung.

### Typische Fehlvorstellung: Jeder Tag hat eine Zeile

> **Typische Fehlvorstellung:** _„In einer Tagesreihe steht jeder Tag — fehlende Messungen sind als `-999` markiert.“_

Schauen Sie auf die Ausgabe oben. Wie viele Tage liegen zwischen der vierten und der fünften Datenzeile?

[( )] einer
[( )] keiner — die Zeilen folgen direkt aufeinander
[(X)] fast fünf Jahre
***
Auf den 10. Dezember 1910 folgt direkt der 1. Oktober 1915. Die Tage dazwischen sind nicht mit `-999` markiert — sie **fehlen ganz**. Der DWD kennt also zwei Arten fehlender Daten: Zeilen mit `-999` (18930311) und Zeilen, die es gar nicht gibt.

Die zweite Art bemerkt kein Programm von selbst. Man muss das Datum der Folgezeile prüfen — oder zählen, wie viele Tage ein Jahr hat.
***

## Das Dictionary

In Vorlesung 05 haben wir für jedes Jahr alle Tage erneut durchlaufen. Bei 48.000 Zeilen und 135 Jahren wären das über sechs Millionen Durchläufe. Besser: **ein** Durchlauf, und für jedes Jahr ein Fach, in das wir das Ergebnis legen.

Genau das ist ein **Dictionary** (Wörterbuch): Es ordnet jedem **Schlüssel** einen **Wert** zu.

``` ascii
          Schlüssel      Wert
        +----------+----------+
        |  "1900"  |   24.9   |
        |  "1950"  |   26.0   |
        |  "2024"  |   26.9   |
        +----------+----------+
```

<!-- data-type="none" -->
| Was                    | Code                    | Bei einer Liste wäre das ...   |
| :--------------------- | :---------------------- | :----------------------------- |
| leer anlegen           | `hoechst = {}`          | `[]`                           |
| Wert eintragen/ändern  | `hoechst["2024"] = 26.9` | `liste[3] = 26.9`             |
| Wert nachschlagen      | `hoechst["2024"]`       | `liste[3]`                     |
| Gibt es den Schlüssel? | `"2024" in hoechst`     | –                              |
| alle Schlüssel durchlaufen | `for jahr in hoechst:` | `for wert in liste:`        |
| Anzahl der Einträge    | `len(hoechst)`          | `len(liste)`                   |

```python main.py
frost = {}
frost["1947"] = 119
frost["1949"] = 97
print(frost)
print("1948" in frost)
print(frost["1948"])
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Die letzte Zeile scheitert mit `KeyError`: Nach einem Schlüssel, der nicht existiert, kann man nicht fragen. Deshalb prüfen die Programme unten vorher mit `in`, ob ein Jahr schon einen Eintrag hat.

## Die ganze Datei

Jetzt die Leitfrage aus Vorlesung 05 — für **alle** Jahre, in einem einzigen Durchlauf mit einem Dictionary.

Die Datei liegt im Repository unter `data/fichtelberg/`. Auf Ihrem Rechner öffnen Sie sie dort direkt. Hier auf dem Server holt die eingeklappte Datei `hole_daten.py` sie vorher aus dem Repository.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
datei = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(datei), exist_ok=True)
urllib.request.urlretrieve(basis + datei, datei)
```
```python main.py
datei = ("data/fichtelberg/"
         "produkt_klima_tag_18900801_20251231_01358.txt")
hoechst = {}
tag = {}
with open(datei) as f:
    f.readline()
    for zeile in f:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
                tag[jahr] = teile[1]

print(len(hoechst), "Jahre")
for jahr in ["1900", "1950", "2000", "2024"]:
    print(jahr, tag[jahr], hoechst[jahr])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Die Bedingung `jahr not in hoechst or maximum > hoechst[jahr]` fasst zwei Fälle zusammen: Das Jahr taucht zum ersten Mal auf — oder der neue Wert ist höher als der bisherige.

Die Messreihe beginnt 1890 und endet 2025. Die Ausgabe nennt aber nur [[132]] Jahre.
[[?]] Denken Sie an die Lücke aus dem Ausschnitt.
***
1890 bis 2025 wären 136 Jahre. Die Jahre 1911 bis 1914 fehlen vollständig — für sie gibt es keinen einzigen Eintrag im Dictionary. 1910 und 1915 sind enthalten, aber nur teilweise gemessen.
***

**Ausprobieren:** Ergänzen Sie das Programm so, dass es den wärmsten Tag der gesamten Messreihe ausgibt. (Zur Kontrolle: 30,8 °C am 27. Juli 1983.)

### Typische Fehlvorstellung: Kein Wert heißt null

> **Typische Fehlvorstellung:** _„Wenn für ein Jahr nichts gezählt wurde, war da auch nichts.“_

Dasselbe Zählmuster für die Station **Freiberg** — wie viele Frosttage gab es 1947 bis 1949?

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
datei = "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"
os.makedirs(os.path.dirname(datei), exist_ok=True)
urllib.request.urlretrieve(basis + datei, datei)
```
```python main.py
datei = "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"
frost = {}
with open(datei) as f:
    f.readline()
    for zeile in f:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        minimum = float(teile[16])
        if jahr not in frost:
            frost[jahr] = 0
        if minimum != -999 and minimum < 0:
            frost[jahr] = frost[jahr] + 1

for jahr in ["1947", "1948", "1949"]:
    print(jahr, frost[jahr], "Frosttage")
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Ein Winter ohne einen einzigen Frosttag in Freiberg? Was ist die wahrscheinlichste Erklärung?

[( )] 1948 war ein außergewöhnlich milder Winter.
[( )] Das Programm hat einen Fehler in der Bedingung.
[(X)] 1948 wurde das Tagesminimum nicht gemessen.
***
Im ganzen Jahr 1948 steht in der Spalte `TNK` nur `-999`. Das Programm überspringt die Fehlwerte korrekt — und zählt deshalb null. Das Ergebnis ist **rechnerisch richtig und inhaltlich falsch**: "null Frosttage" und "keine Messung" sind zwei verschiedene Aussagen.

Abhilfe: Zählen Sie in einem zweiten Dictionary mit, an wie vielen Tagen überhaupt gemessen wurde — und geben Sie das Ergebnis nur aus, wenn genügend Tage vorliegen.
***

## Ergebnisse schreiben

Ein Ergebnis, das nur auf dem Bildschirm steht, ist nach dem nächsten Programmlauf weg. Schreiben wir es in eine Datei:

```python main.py
hoechst = {"1900": 24.9, "1950": 26.0, "2024": 26.9}

with open("jahreshoechst.csv", "w") as f:
    f.write("jahr;maximum\n")
    for jahr in hoechst:
        f.write(jahr + ";" + str(hoechst[jahr]) + "\n")

with open("jahreshoechst.csv") as f:
    print(f.read())
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

* `open(..., "w")` öffnet zum **Schreiben**. Existiert die Datei schon, wird sie **überschrieben**.
* `f.write` erwartet einen Text und hängt — anders als `print` — **keinen** Zeilenumbruch an. Das `"\n"` muss man selbst anfügen.
* Die Datei `jahreshoechst.csv` können Sie mit der Tabellenkalkulation öffnen. Damit schließt sich der Kreis zu Vorlesung 01.

## Live Hacking: Das lange Skript

> **Live Hacking.** In der Vorlesung setzen wir alles zusammen: wärmster Tag **und** Frosttage pro Jahr, für den Fichtelberg **und** für Freiberg, mit Ergebnisdatei. Das Ergebnis finden Sie unten eingeklappt.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
for datei in ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
              "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"]:
    os.makedirs(os.path.dirname(datei), exist_ok=True)
    urllib.request.urlretrieve(basis + datei, datei)
```
```python -auswertung.py
# ---- Fichtelberg ----------------------------------------------------------
hoechst = {}
frost = {}
with open("data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt") as f:
    f.readline()
    for zeile in f:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        minimum = float(teile[16])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
        if jahr not in frost:
            frost[jahr] = 0
        if minimum != -999 and minimum < 0:
            frost[jahr] = frost[jahr] + 1

with open("fichtelberg_jahre.csv", "w") as f:
    f.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        f.write(jahr + ";" + str(hoechst[jahr]) + ";" + str(frost[jahr]) + "\n")

# ---- Freiberg -------------------------------------------------------------
hoechst = {}
frost = {}
with open("data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt") as f:
    f.readline()
    for zeile in f:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        minimum = float(teile[16])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
        if jahr not in frost:
            frost[jahr] = 0
        if minimum != -999 and minimum < 0:
            frost[jahr] = frost[jahr] + 1

with open("freiberg_jahre.csv", "w") as f:
    f.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        f.write(jahr + ";" + str(hoechst[jahr]) + ";" + str(frost[jahr]) + "\n")

# ---- Kontrolle ------------------------------------------------------------
for name in ["fichtelberg_jahre.csv", "freiberg_jahre.csv"]:
    with open(name) as f:
        zeilen = f.readlines()
    print(name, len(zeilen) - 1, "Jahre, erste Zeile:", zeilen[1].strip())
```
@LIA.eval(`["hole_daten.py", "auswertung.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 auswertung.py"`)

Klappen Sie `auswertung.py` auf. Das Programm funktioniert — aber:

* Der Block für Freiberg ist eine **Kopie** des Blocks für den Fichtelberg. Nur der Dateiname ist anders.
* Findet man einen Fehler (etwa den mit 1948), muss man ihn an **zwei** Stellen beheben. Für eine dritte Station an drei.
* Um zu verstehen, was das Programm tut, muss man alle 50 Zeilen lesen.

> Dieses Skript ist absichtlich so geschrieben. Nächste Woche zerlegen wir es in Funktionen.

## Zwischenbilanz: Datentypen

Mit dieser Vorlesung haben Sie alle Datentypen kennengelernt, die Sie für die erste Hälfte des Kurses brauchen:

<!-- data-type="none" -->
| Typ     | Beispiel                     | Woher er im Datensatz kommt              | Typische Falle                                  |
| :------ | :--------------------------- | :--------------------------------------- | :---------------------------------------------- |
| `int`   | `1358`, `2024`               | Stations-ID, Jahr nach `int(...)`        | `int("2024") == 2024`, aber `"2024" != 2024`    |
| `float` | `-14.1`                      | Temperaturen nach `float(...)`           | nicht exakt: kein `==` (VL 04)                  |
| `str`   | `"18930310"`                 | alles, was aus einer Datei gelesen wird  | `"9.5" > "28.1"` (VL 05)                        |
| `bool`  | `True`                       | Ergebnis jedes Vergleichs                | `=` statt `==` (VL 02)                          |
| `list`  | `[-1.9, -2.4, 0.1]`          | `zeile.split(";")`, gesammelte Ergebnisse | Index ab 0, `IndexError` (VL 05)              |
| `range` | `range(2015, 2025)`          | Jahre, Indizes                           | Endwert nicht enthalten (VL 05)                 |
| `dict`  | `{"1947": 119}`              | ein Ergebnis pro Jahr                    | `KeyError`, fehlender Eintrag ≠ 0 (VL 06)       |

> **Ausblick:** In Vorlesung 10 kommt mit dem NumPy-**Array** ein Typ hinzu, der aussieht wie eine Liste, aber elementweise rechnet. In Vorlesung 11 lernen Sie `NaN` kennen — die Art, wie pandas "kein Wert" darstellt.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
zeile = "  1358;20240813;26.9\n"
teile = zeile.split(";")
print(len(teile), teile[1][4:6], float(teile[2]) + 1)
```

[( )] `3 20 27.9`
[(X)] `3 08 27.9`
[( )] `2 08 27.9`
[( )] eine Fehlermeldung, weil `"26.9\n"` keine Zahl ist
***
Drei Teile. `teile[1]` ist `"20240813"`, davon die Zeichen 4 und 5: `"08"`. `float` ignoriert den Zeilenumbruch am Ende, genau wie Leerzeichen.
***

**Welche Aussagen stimmen?**

[[X]] `with open(...) as f:` schließt die Datei automatisch am Ende des Blocks.
[[ ]] `f.write("abc")` beginnt danach automatisch eine neue Zeile.
[[X]] `open("x.csv", "w")` löscht den bisherigen Inhalt von `x.csv`.
[[ ]] Fehlende Tage stehen in DWD-Dateien immer als `-999` in der Datei.
[[X]] `f.readline()` vor der Schleife sorgt dafür, dass die Schleife mit der zweiten Zeile beginnt.

## Nächste Woche

Das lange Skript funktioniert, ist aber schwer zu lesen, zu ändern und zu erweitern. Nächste Woche lernen Sie **Funktionen** — und zerlegen es live in handliche, benannte Teile.

**Zur Vorbereitung**

- [ ] Klonen oder laden Sie das Repository herunter und führen Sie das Programm aus _Die ganze Datei_ auf Ihrem Rechner aus (ohne `hole_daten.py`).
- [ ] Beheben Sie im langen Skript den 1948-Fehler: Jahre mit weniger als 300 gemessenen Tagen sollen in der Ergebnisdatei keinen Frostwert bekommen. An wie vielen Stellen müssen Sie ändern?
- [ ] Markieren Sie im langen Skript alle Zeilen, die in beiden Blöcken gleich sind.
