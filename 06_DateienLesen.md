<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.1.0
language: de
narrator: Deutsch Female

comment:  Dateien lesen: Die DWD-Rohdatei mit Bordmitteln einlesen — Zeilen zerlegen, Fehlwerte und Lücken erkennen, mit einem Dictionary ein Ergebnis pro Jahr sammeln.

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
| **Inhalte:**             | `open, with, Arbeitsordner, readline, strip, split, Kopfzeile, Fehlwerte, Lücken, Dictionary, KeyError, Dateien schreiben`                         |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Gibt es auf dem Fichtelberg heute weniger Frosttage als vor 100 Jahren?_

**Fragen an die heutige Veranstaltung ...**

* Wie öffnet und liest man eine Textdatei — auch auf dem eigenen Rechner?
* Wie zerlegt man eine Zeile in ihre Spalten?
* Was tut man mit Kopfzeile, Fehlwerten und Lücken?
* Wie sammelt man in einem Durchlauf ein Ergebnis pro Jahr?
* Wie schreibt man ein Ergebnis in eine neue Datei?

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=6" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

> Die Beispiele heute laufen auf einem Server, genau wie Python auf Ihrem Rechner — einschließlich echter Dateien. Der erste Klick auf „Ausführen“ kann einige Sekunden dauern, bis der Server bereit ist.

--{{0}}--
In Vorlesung 03 haben wir die Frosttage eines einzigen Jahres gezählt: 127 im Jahr 2024. Heute zählen wir sie für alle Jahre seit 1890 und vergleichen drei Zeiträume von je 30 Jahren. Dafür brauchen wir die Datei, wie der Deutsche Wetterdienst sie liefert, mit allen ihren Eigenheiten.

--------------------------------------------------------------------------------

## Rückblick

In den Vorlesungen 03 bis 05 kamen die Werte vorbereitet an: eine Spalte, ein Wert pro Zeile, geholt mit `open_url` — und das funktioniert nur im Browser.

Heute nehmen wir die Datei, wie der DWD sie liefert:

```text produkt_klima_tag_18900801_20251231_01358.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18900801;-999;-999;-999;    1;   0.0;   0;-999;-999;   2.0;  13.2;    -999;   15.6;   67.00;   19.6;   10.0;-999;eor
```

Ihre Vorbereitungsaufgabe war, die Schritte zu beschreiben, mit denen man aus einer Zeile Datum und Tagesmaximum gewinnt. Genau diese Schritte setzen wir heute um:

1. Datei öffnen und Zeile für Zeile lesen
2. Kopfzeile überspringen
3. Zeile an den Semikolons zerlegen
4. Die richtigen Spalten auswählen und in Zahlen umwandeln
5. Fehlwerte erkennen

--{{0}}--
Wer in der ersten Vorbereitungsaufgabe das Programm aus „Ergebnis“ um die Liste `jahrestage` erweitert hat, führt jetzt zwei Listen nebeneinander, `jahreshoechst` und `jahrestage`, die über den Index zusammengehören. Das geht, wird aber bei jedem weiteren Wert unübersichtlicher. Heute lernen Sie mit dem Dictionary einen Behälter kennen, in dem jedes Ergebnis direkt unter seinem Jahr liegt.

## Eine Datei öffnen

Für die ersten Schritte genügen fünf aufeinanderfolgende Tage aus dem März 1893. `ausschnitt.txt` liegt neben `main.py`, genau wie auf Ihrem Rechner.

```text ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930309;-999;-999;-999;    1;   2.3;   7;-999;-999;   7.3;   4.9;  877.20;   -2.7;   97.00;   -2.2;   -6.2;-999;eor
       1358;18930310;-999;-999;-999;    1;   3.0;   7;-999;-999;   8.0;   5.1;  868.50;   -2.3;   99.00;   -0.4;   -3.8;-999;eor
       1358;18930311;-999;-999;-999;    1;   1.5;   7;-999;-999;  -999;  -999;    -999;   -999;-999;   -999;   -999;-999;eor
       1358;18930312;-999;-999;-999;    1;   0.0;   0;-999;-999;   3.7;   5.7;  877.90;   -0.6;   96.00;    0.9;   -6.6;-999;eor
       1358;18930313;-999;-999;-999;    1;   0.5;   1;-999;-999;   3.0;   5.6;  872.30;    3.6;   69.00;    5.3;   -1.3;-999;eor
```
```python main.py
dateiname = "ausschnitt.txt"
with open(dateiname) as datei:
    for zeile in datei:
        print(zeile)
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

* `open(dateiname)` öffnet die Datei zum **Lesen**, `with ... as datei:` schließt sie nach dem eingerückten Block wieder. Was Sie gelesen haben, bleibt in Variablen erhalten.
* `for zeile in datei:` liefert die Datei **Zeile für Zeile**, jede als **Text**.
* Die Leerzeilen in der Ausgabe: Jede Zeile endet mit einem Zeilenumbruch `\n`, `print` hängt einen zweiten an. Abhilfe: `print(zeile.strip())`.

> **Auf Ihrem Rechner:** Enthält eine Datei Umlaute, schreiben Sie `open(dateiname, encoding="utf-8")`. Windows liest bis Python 3.14 sonst mit einer anderen Zeichentabelle, und aus „ü“ wird „Ã¼“. Die DWD-Messdateien enthalten nur einfache Zeichen.

--{{0}}--
`with` sorgt dafür, dass die Datei auch dann geschlossen wird, wenn unterwegs ein Fehler auftritt. Ohne `with` müsste man am Ende `datei.close()` schreiben und dürfte es nie vergessen. `strip()` entfernt Leerzeichen und Zeilenumbrüche am Anfang und am Ende eines Texts, nicht in der Mitte. Die Angabe `encoding` nennt die Zeichentabelle, mit der Python die Bytes der Datei in Buchstaben übersetzt. Auf Linux und macOS ist UTF-8 ohnehin Standard, auf Windows erst ab Python 3.15. Mit `encoding="utf-8"` läuft Ihr Programm überall gleich.

### Typische Fehlvorstellung: Die Datei liegt doch daneben

> **Typische Fehlvorstellung:** _„Die Datei liegt im selben Ordner wie mein Programm, also findet Python sie.“_

In Visual Studio Code ist der Ordner `EAVD` geöffnet. Darin liegen Programm und Datei im Unterordner `vl06`:

```text
EAVD/                       ← in VS Code geöffneter Ordner
└── vl06/
    ├── main.py             ← enthält open("ausschnitt.txt")
    └── ausschnitt.txt
```

Der **Arbeitsordner** ist der Ordner, in dem das Terminal gerade steht. Das Terminal zeigt ihn vor dem `>` an.

Im Terminal steht `EAVD>`, und Sie starten `python vl06/main.py`. Legen Sie sich fest, **bevor** Sie weiterlesen: Was passiert?

[( )] Das Programm gibt die fünf Zeilen aus.
[(X)] `FileNotFoundError: [Errno 2] No such file or directory: 'ausschnitt.txt'`
[( )] Python legt eine leere Datei `ausschnitt.txt` an.
***
Ein Dateiname ohne Ordner gilt ab dem **Arbeitsordner** (`EAVD`). Wo das Programm liegt, spielt keine Rolle. Python sucht also `EAVD/ausschnitt.txt`, und die gibt es nicht.

Abhilfe: im Terminal erst `cd vl06` (wechselt in den Unterordner), dann `python main.py`. Oder in VS Code gleich den Ordner `vl06` öffnen.
***

                                     {{1}}
*******************************************************************************

<!-- style="max-width: 560px; display: block; margin: auto" -->
```ascii
+---------------------------------------------------+
| EAVD                 ← Arbeitsordner (Terminal)   |
|                        Python sucht hier ✗        |
|                                                   |
|   +-------------------------------------------+   |
|   | vl06                                      |   |
|   |   main.py                                 |   |
|   |   ausschnitt.txt   ← hier liegt die Datei |   |
|   +-------------------------------------------+   |
+---------------------------------------------------+
```

*******************************************************************************

--{{0}}--
Auch der Knopf „Python-Datei ausführen“ oben rechts in VS Code startet das Programm im geöffneten Ordner, nicht im Ordner des Programms. Wer das ändern möchte, setzt in den Einstellungen `python.terminal.executeInFileDir`. Den aktuellen Arbeitsordner zeigt `import os` und `print(os.getcwd())`. Die Fehlermeldung nennt den Namen so, wie er im Programm steht, also ohne Ordner. Wo Python tatsächlich gesucht hat, verrät erst `os.getcwd()`.

## Eine Zeile zerlegen

```text -ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930309;-999;-999;-999;    1;   2.3;   7;-999;-999;   7.3;   4.9;  877.20;   -2.7;   97.00;   -2.2;   -6.2;-999;eor
```
```python main.py
dateiname = "ausschnitt.txt"
with open(dateiname) as datei:
    kopf = datei.readline()
    zeile = datei.readline()

teile = zeile.split(";")
print(len(teile), "Teile")
print(teile)
print("Datum:", teile[1], "Minimum:", teile[16])
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

`datei.readline()` liest genau **eine** Zeile. `split(";")` zerlegt sie an jedem Semikolon in eine **Liste von Texten**. Welcher Index welche Spalte ist, verrät die Kopfzeile:

<!-- data-type="none" -->
| Index | Spalte       | Bedeutung                    |
| ----: | :----------- | :--------------------------- |
| 1     | `MESS_DATUM` | Datum, `JJJJMMTT`            |
| 13    | `TMK`        | Tagesmittel der Temperatur   |
| 15    | `TXK`        | Tagesmaximum                 |
| 16    | `TNK`        | Tagesminimum                 |

--{{0}}--
Die Teile behalten ihre Leerzeichen: `teile[16]` ist `"   -6.2"`. Für `float` ist das kein Problem, es ignoriert Leerzeichen am Rand. Bei Texten, die Text bleiben, etwa der Stations-ID in `teile[0]`, braucht man `strip()`. Das letzte Teil heißt `"eor\n"`, „end of record“, mit dem Zeilenumbruch.

### Typische Fehlvorstellung: Die Zeile ist schon eine Tabelle

> **Typische Fehlvorstellung:** _„Eine Zeile aus der Datei besteht schon aus Spalten.“_

Legen Sie sich fest, **bevor** Sie weiterlesen: Was liefert `zeile[1]` — **ohne** vorheriges `split`?

[( )] `"18930309"`, die zweite Spalte
[(X)] `" "`, ein einzelnes Leerzeichen
[( )] eine Fehlermeldung
***
Für Python ist die Zeile ein **Text** wie jeder andere. `zeile[1]` ist das zweite **Zeichen**, und die Zeile beginnt mit sieben Leerzeichen. Spalten entstehen erst durch `split(";")`.
***

--{{0}}--
Dasselbe kennen Sie aus der Tabellenkalkulation beim Import: Ohne Angabe des Trennzeichens landet die ganze Zeile in einer Zelle. Probieren Sie es im Programm oben aus, indem Sie `print(zeile[1])` ergänzen.

## Kopfzeile und Fehlwerte

```text -ausschnitt.txt
STATIONS_ID;MESS_DATUM;QN_3;  FX;  FM;QN_4; RSK;RSKF; SDK;SHK_TAG;  NM; VPM;  PM; TMK; UPM; TXK; TNK; TGK;eor
       1358;18930309;-999;-999;-999;    1;   2.3;   7;-999;-999;   7.3;   4.9;  877.20;   -2.7;   97.00;   -2.2;   -6.2;-999;eor
       1358;18930310;-999;-999;-999;    1;   3.0;   7;-999;-999;   8.0;   5.1;  868.50;   -2.3;   99.00;   -0.4;   -3.8;-999;eor
       1358;18930311;-999;-999;-999;    1;   1.5;   7;-999;-999;  -999;  -999;    -999;   -999;-999;   -999;   -999;-999;eor
       1358;18930312;-999;-999;-999;    1;   0.0;   0;-999;-999;   3.7;   5.7;  877.90;   -0.6;   96.00;    0.9;   -6.6;-999;eor
       1358;18930313;-999;-999;-999;    1;   0.5;   1;-999;-999;   3.0;   5.6;  872.30;    3.6;   69.00;    5.3;   -1.3;-999;eor
```
```python main.py
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
```
@LIA.eval(`["ausschnitt.txt", "main.py"]`, `none`, `python3 main.py`)

* Die Kopfzeile ist keine Messung: `datei.readline()` vor der Schleife liest sie und wirft sie weg.
* `-999` heißt beim DWD **„kein Wert“**. Für Python ist es eine ganz normale Zahl, prüfen müssen wir selbst.

Probieren Sie aus, was ohne die Zeile `datei.readline()` passiert, und lesen Sie die Fehlermeldung.

--{{0}}--
Ohne `readline` versucht `float`, aus dem Text `" TNK"` eine Zahl zu machen, und bricht mit `ValueError` ab. Wie man solche Fehler abfängt, statt abzubrechen, lernen Sie in Vorlesung 07. Darf man `minimum == -999` schreiben? Ja, das ist Regel 3 aus Vorlesung 04: Werte direkt aus der Datei darf man vergleichen, ungenau werden Kommazahlen erst beim Rechnen.

### Typische Fehlvorstellung: Jeder Tag hat eine Zeile

> **Typische Fehlvorstellung:** _„In einer Tagesreihe steht jeder Tag — fehlende Messungen sind als `-999` markiert.“_

Hier sind fünf Zeilen, die in der Fichtelberg-Datei **direkt aufeinander folgen** (Zeile 7.324 bis 7.328):

```text produkt_klima_tag_18900801_20251231_01358.txt
       1358;19101208;-999;-999;-999;    1;   0.0;   0;-999; 100;   2.0;   6.9;  868.00;    3.1;   89.00;    5.4;    0.5;-999;eor
       1358;19101209;-999;-999;-999;    1;   2.7;   1;-999; 100;   7.0;   5.9;  863.90;    1.4;   89.00;    4.3;   -2.8;-999;eor
       1358;19101210;-999;-999;-999;    1;   0.0;   0;-999;  90;   3.3;   7.2;  863.60;    3.8;   90.00;    5.4;    1.0;-999;eor
       1358;19151001;-999;-999;-999;    1;   2.0;   1;-999;   0;   8.0;   7.1;  873.70;    2.0;  100.00;    2.8;    1.0;-999;eor
       1358;19151002;-999;-999;-999;    1;   2.1;   8;-999;   0;   8.0;   6.5;  877.60;    1.0;  100.00;    2.5;    0.4;-999;eor
```

Legen Sie sich fest, **bevor** Sie weiterlesen: Wie viele Tage liegen zwischen der dritten und der vierten Zeile?

[( )] keiner, es sind aufeinanderfolgende Tage
[( )] ein paar Tage mit `-999`, die hier nicht gezeigt sind
[(X)] fast fünf Jahre, ohne eine einzige Zeile
***
Auf den 10. Dezember 1910 folgt direkt der 1. Oktober 1915. Die 1.755 Tage dazwischen sind nicht mit `-999` markiert — sie **fehlen ganz**. Der DWD kennt also zwei Arten fehlender Daten: Zeilen mit `-999` (11. März 1893) und Zeilen, die es gar nicht gibt.
***

                                     {{1}}
*******************************************************************************

<!-- style="max-width: 640px; display: block; margin: auto" -->
```ascii
  Zeile  7.324  7.325  7.326                            7.327  7.328
           |      |      |                                |      |
   --------+------+------+~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~+------+------>
          8.12.  9.12.  10.12.1910                    1.10.1915  2.10.
                              1.755 Tage ohne eine Zeile
```

*******************************************************************************

--{{0}}--
Die zweite Art bemerkt kein Programm von selbst. Man muss das Datum der Folgezeile prüfen oder zählen, wie viele Tage für ein Jahr vorliegen. Eine zweite, kürzere Lücke gibt es gleich am Anfang: Vom 11. Dezember 1890 bis zum 31. März 1891 fehlen 111 Tage. Nach dem Grund fragt man den DWD oder die Stationsbeschreibung, die Datei selbst sagt dazu nichts.

## Das Dictionary

In Vorlesung 05 haben wir für jedes Jahr alle Tage erneut durchlaufen. Bei rund 47.600 Zeilen und 136 Jahren wären das über sechs Millionen Durchläufe. Besser: **ein** Durchlauf, und für jedes Jahr ein Fach, in das wir das Ergebnis legen.

Genau das ist ein **Dictionary** (Wörterbuch): Es ordnet jedem **Schlüssel** einen **Wert** zu.

<!-- style="max-width: 320px; display: block; margin: auto" -->
``` ascii
     Schlüssel (Text)   Wert (Zahl)
        +----------+----------+
        |   1900   |   192    |
        +----------+----------+
        |   1950   |   176    |
        +----------+----------+
        |   2024   |   127    |
        +----------+----------+
```

<!-- data-type="none" -->
| Was                    | Code                    | Bei einer Liste wäre das ...   |
| :--------------------- | :---------------------- | :----------------------------- |
| leer anlegen           | `frost = {}`            | `[]`                           |
| Wert eintragen/ändern  | `frost["2024"] = 127`   | `liste[3] = 127`               |
| Wert nachschlagen      | `frost["2024"]`         | `liste[3]`                     |
| Gibt es den Schlüssel? | `"2024" in frost`       | –                              |
| alle Schlüssel durchlaufen | `for jahr in frost:` | `for wert in liste:`          |
| Anzahl der Einträge    | `len(frost)`            | `len(liste)`                   |

```python main.py
frost = {}                # Frosttage in Freiberg
frost["1947"] = 119
frost["1949"] = 97
print(frost)
print("1948" in frost)
print(frost["1948"])
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Die letzte Zeile scheitert mit `KeyError: '1948'`: Nach einem Schlüssel, den es nicht gibt, kann man nicht fragen. Deshalb prüft man vorher mit `in`, ob ein Jahr schon einen Eintrag hat.

--{{0}}--
Die Zahlen im Bild sind die Frosttage auf dem Fichtelberg, die wir heute ausrechnen; 127 kennen Sie aus Vorlesung 03. Das Programm darunter nimmt Werte aus Freiberg, die uns gleich wieder begegnen. Ein Dictionary hat keine Positionen 0, 1, 2 wie eine Liste, man greift immer über den Schlüssel zu. Jeder Schlüssel kommt höchstens einmal vor: Wer `frost["2024"]` ein zweites Mal etwas zuweist, überschreibt den alten Wert. `for jahr in frost:` liefert die Schlüssel in der Reihenfolge, in der sie eingetragen wurden.

## Die ganze Datei

Jetzt das Versprechen aus Vorlesung 05: der wärmste Tag für **alle** Jahre, in einem einzigen Durchlauf mit einem Dictionary.

Die Datei liegt im Repository unter `data/fichtelberg/`. Auf Ihrem Rechner hängt der Pfad vom Arbeitsordner ab: vom Hauptordner des Repositorys aus `data/fichtelberg/…`, aus `examples/06_DateienLesen/` heraus `../../data/fichtelberg/…` (`..` heißt „eine Ebene höher“). Hier auf dem Server holt die eingeklappte Datei `hole_daten.py` sie vorher aus dem Repository.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/fichtelberg/"
             "produkt_klima_tag_18900801_20251231_01358.txt")
hoechst = {}
datum = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
                datum[jahr] = teile[1]
print(len(hoechst), "Jahre")
print("2024:", datum["2024"], hoechst["2024"])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

`jahr not in hoechst or maximum > hoechst[jahr]` fasst zwei Fälle zusammen: Das Jahr taucht zum ersten Mal auf — oder der neue Wert ist höher als der bisherige. Kein `KeyError`, weil Python `or` von links liest und aufhört, sobald eine Seite wahr ist: Bei einem neuen Jahr wird `hoechst[jahr]` gar nicht nachgeschlagen.

Die Messreihe beginnt 1890 und endet 2025. Die Ausgabe nennt aber nur [[132]] Jahre.
[[?]] Denken Sie an die Lücke.
***
1890 bis 2025 wären 136 Jahre. Die Jahre 1911 bis 1914 fehlen vollständig — für sie gibt es keinen einzigen Eintrag im Dictionary. 1910 und 1915 sind enthalten, aber nur teilweise gemessen.
***

--{{0}}--
Kein `hoechst = -100` mehr wie in Vorlesung 05: Das erste Maximum eines Jahres wird einfach eingetragen, weil das Jahr noch nicht `in hoechst` ist. Das Dictionary übernimmt die Rolle der parallelen Listen aus Vorlesung 05, `hoechst` und `datum` haben dieselben Schlüssel. Zum Ausprobieren: Ergänzen Sie das Programm so, dass es den wärmsten Tag der gesamten Messreihe ausgibt. Zur Kontrolle: 30,8 °C am 27. Juli 1983.

## Live Hacking: Frosttage seit 1890

> [!NOTE] ❓ Aufgabe
>
> _Gibt es auf dem Fichtelberg heute weniger Frosttage als vor 100 Jahren?_
>
> Zählen Sie die Frosttage (Tagesminimum unter 0 °C) für jedes Jahr und vergleichen Sie die Mittelwerte von 1891–1920, 1961–1990 und 1995–2024.

> **Live Hacking (≈ 20 min).** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam. Die Schritte unten zeigen die typischen Irrwege.

--{{0}}--
Dreißig Jahre sind die international vereinbarte Länge für einen Klimavergleich, weil sich darin einzelne besonders kalte oder warme Jahre ausgleichen. 1961 bis 1990 ist die Vergleichsperiode, an der man den Klimawandel misst; als aktueller Referenzzeitraum gilt 1991 bis 2020. Ein Frosttag ist ein Tag, an dem die Temperatur wenigstens einmal unter 0 °C fällt, also ein Tagesminimum `TNK` unter 0.

### Pseudocode

> **Wie würden Sie vorgehen?** Beschreiben Sie den Ablauf in eigenen Worten, noch ohne Python.
>
> * Was steht im Dictionary, was sind Schlüssel, was Werte?
> * Was passiert, wenn ein Jahr zum ersten Mal auftaucht?
> * Wie bildet man aus den Jahreswerten einen Mittelwert für 30 Jahre? Denken Sie an `range` aus Vorlesung 05.

                                     {{1}}
*******************************************************************************

```text
Für jede Zeile der Datei:
    Hole Jahr und Tagesminimum.
    Ist das Minimum unter 0, erhöhe frost[jahr] um 1.
Für jeden Zeitraum mit Startjahr 1891, 1961, 1995:
    Für jedes Jahr von start bis start + 29:
        Addiere frost[jahr] zur Summe und zähle das Jahr.
    Gib Summe geteilt durch Anzahl aus.
```

Die zweite Frage lässt der Pseudocode bewusst offen. Schritt 1 zeigt, warum sie wichtig ist.

*******************************************************************************

### Schritt 1 - Zählen pro Jahr

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/fichtelberg/"
             "produkt_klima_tag_18900801_20251231_01358.txt")
frost = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        minimum = float(teile[16])
        if minimum < 0:
            frost[jahr] = frost[jahr] + 1

print(frost["2024"])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert beim ersten Frosttag im Jahr 1890?

[( )] `frost["1890"]` wird 1.
[(X)] Das Programm bricht mit einer Fehlermeldung ab.
[( )] Python überspringt das Jahr, weil es noch kein Fach hat.
***
`KeyError: '1890'`: Beim ersten Frosttag 1890 gibt es noch kein Fach `frost["1890"]`, zu dem man 1 addieren könnte. Wie beim Zählen in Vorlesung 03 braucht jedes Fach einen **Startwert 0** — aber erst, wenn das Jahr auftaucht:

```python
if jahr not in frost:
    frost[jahr] = 0
```
***

--{{0}}--
Kürzer geht es mit `frost[jahr] = frost.get(jahr, 0) + 1`: `get` liefert den Wert zum Schlüssel oder, wenn es ihn nicht gibt, die angegebene 0. `get` lernen Sie in Vorlesung 09 kennen, heute schreiben wir den Fall ausdrücklich hin.

### Schritt 2 - Fächer anlegen

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/fichtelberg/"
             "produkt_klima_tag_18900801_20251231_01358.txt")
frost = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        minimum = float(teile[16])
        if jahr not in frost:
            frost[jahr] = 0
        if minimum < 0:
            frost[jahr] = frost[jahr] + 1

for jahr in ["1900", "1950", "2024"]:
    print(jahr, frost[jahr], "Frosttage")
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Die 127 für 2024 kennen wir aus Vorlesung 03. Läuft das Programm auch für eine zweite Station? Wir ändern nur den Dateinamen und nehmen **Freiberg** 1947 bis 1949.

                                     {{1}}
*******************************************************************************

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/freiberg/"
             "produkt_klima_tag_19450701_19930430_01441.txt")
frost = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        minimum = float(teile[16])
        if jahr not in frost:
            frost[jahr] = 0
        if minimum < 0:
            frost[jahr] = frost[jahr] + 1

for jahr in ["1947", "1948", "1949"]:
    print(jahr, frost[jahr], "Frosttage")
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

1948 mit **366 Frosttagen**, jeder Tag des Schaltjahres? `-999` ist kleiner als 0 und zählt mit.

> **KI und Fehlwerte:** Code wie diesen liefert auch eine KI, wenn man ihr nicht sagt, dass `-999` „kein Wert“ bedeutet. Er läuft ohne Fehlermeldung. Ob das Ergebnis stimmt, müssen Sie selbst prüfen — am besten an einem Wert, den Sie kennen.

*******************************************************************************

--{{0}}--
Auf dem Fichtelberg fällt der Fehler kaum auf: Dort sind in der Spalte `TNK` nur zehn Tageswerte als `-999` markiert, neun davon 1903. Das Programm zählt für 1903 deshalb 177 statt 168 Frosttage, und das sieht niemand. Erst die zweite Station macht den Fehler sichtbar. Ein Programm an anderen Daten zu prüfen, ist deshalb eine gute Gewohnheit.

### Schritt 3 - Fehlwerte auslassen

Wir lassen die Fehlwerte aus: `minimum != -999 and minimum < 0`.

> **Typische Fehlvorstellung:** _„Wenn für ein Jahr nichts gezählt wurde, war da auch nichts.“_

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/freiberg/"
             "produkt_klima_tag_19450701_19930430_01441.txt")
frost = {}
with open(dateiname) as datei:
    datei.readline()
    for zeile in datei:
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

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Wie viele Frosttage meldet es jetzt für 1948?

[( )] etwa 100, wie 1947 und 1949
[( )] 366, wie vorher
[(X)] 0
***
Im ganzen Jahr 1948 steht in der Spalte `TNK` nur `-999`, das Tagesminimum wurde nicht gemessen; den Grund nennt die Datei nicht. Das Programm überspringt die Fehlwerte korrekt und zählt deshalb null. Das Ergebnis ist **rechnerisch richtig und inhaltlich falsch**: „null Frosttage“ und „keine Messung“ sind zwei verschiedene Aussagen.

Abhilfe in Schritt 4: In einem zweiten Dictionary `messtage` mitzählen, an wie vielen Tagen überhaupt gemessen wurde.
***

### Schritt 4 - Messtage zählen

Ein zweites Dictionary `messtage` zählt für jedes Jahr die Tage **mit** Messwert. Zurück zum Fichtelberg:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/fichtelberg/"
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
for jahr in ["1890", "1891", "1915", "2024"]:
    print(jahr, frost[jahr], "Frosttage an", messtage[jahr], "Messtagen")
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

1891 und 1915 sind nur teilweise gemessen, 1890 beginnt erst im August. Solche Jahre haben zwangsläufig weniger Frosttage.

--{{0}}--
Dieselbe Falle wie bei Freiberg 1948, nur leiser: Ein Jahr mit 92 Messtagen hat natürlich weniger Frosttage als eines mit 365. Wer solche Jahre in einen Mittelwert mischt, vergleicht Äpfel mit Birnen. `messtage` sagt uns, welchen Jahren wir trauen können.

### Ergebnis

Der obere Teil ist Schritt 4. Neu ist nur der untere Teil, das **Mittelwertmuster** aus Vorlesung 04:

* Für jeden Zeitraum läuft `range` über 30 Jahre, `str(jahr)` macht daraus den Schlüssel (Vorlesung 05: `"2015"` ist nicht `2015`).
* Es zählen nur Jahre mit mindestens 300 Messtagen. Das schließt die lückenhaften Jahre 1891 (275) und 1915 (92) aus.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
dateiname = ("data/fichtelberg/"
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
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Lesen Sie das Ergebnis ab: 1995–2024 gab es im Mittel rund [[28]] Frosttage weniger als 1891–1920.
***
182,5 gegen 154,7 Frosttage, also knapp vier Wochen weniger Frost pro Jahr. 1961–1990 lag mit 171,2 dazwischen. Für 1891–1920 gehen nur 24 Jahre ein: 1911 bis 1914 fehlen, 1891 und 1915 haben zu wenige Messtage.
***

--{{0}}--
`schluessel in frost` fängt die fehlenden Jahre 1911 bis 1914 ab, `messtage[schluessel] >= 300` die unvollständigen. Die Grenze 300 ist eine Festlegung: Sie hält stark lückenhafte Jahre heraus und lässt Jahre mit einzelnen Fehltagen drin. Wer sie ändert, sollte prüfen, ob sich das Ergebnis verschiebt. Die Antwort auf die Leitfrage ist also ja, und zwar deutlich. Ob das ein Trend ist oder Zufall, lässt sich mit drei Mittelwerten nicht entscheiden. Dafür zeichnen wir in Vorlesung 13 die ganze Reihe.

## Ergebnisse schreiben

Ein Ergebnis, das nur auf dem Bildschirm steht, ist nach dem nächsten Programmlauf weg. Schreiben wir es in eine Datei:

```python main.py
frost = {"1900": 192, "1950": 176, "2024": 127}

with open("frosttage.csv", "w") as datei:
    datei.write("jahr;frosttage\n")
    for jahr in frost:
        datei.write(jahr + ";" + str(frost[jahr]) + "\n")

with open("frosttage.csv") as datei:
    print(datei.read())
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

* `open(..., "w")` öffnet zum **Schreiben**. Existiert die Datei schon, wird sie **überschrieben**.
* `datei.write` erwartet einen **Text** und hängt — anders als `print` — **keinen** Zeilenumbruch an.

--{{0}}--
Deshalb `str(frost[jahr])`: `write` nimmt nur Text, und `+` zwischen Text und Zahl scheitert. `jahr` ist schon Text. Das `"\n"` am Ende beginnt die nächste Zeile. Die Datei `frosttage.csv` können Sie mit der Tabellenkalkulation öffnen. Damit schließt sich der Kreis zu Vorlesung 01. `datei.read()` liest übrigens die ganze Datei auf einmal als einen Text.

## Das lange Skript

Für zwei Stationen, den wärmsten Tag **und** die Frosttage, mit Ergebnisdatei, entsteht schnell ein langes Skript. Klappen Sie `auswertung.py` auf:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python -auswertung.py
# ---- Fichtelberg ----------------------------------------------------------
hoechst = {}
frost = {}
with open("data/fichtelberg/"
          "produkt_klima_tag_18900801_20251231_01358.txt") as datei:
    datei.readline()
    for zeile in datei:
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

with open("fichtelberg_jahre.csv", "w") as datei:
    datei.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        datei.write(jahr + ";" + str(hoechst[jahr]) + ";"
                    + str(frost[jahr]) + "\n")

# ---- Freiberg -------------------------------------------------------------
hoechst = {}
frost = {}
with open("data/freiberg/"
          "produkt_klima_tag_19450701_19930430_01441.txt") as datei:
    datei.readline()
    for zeile in datei:
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

with open("freiberg_jahre.csv", "w") as datei:
    datei.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        datei.write(jahr + ";" + str(hoechst[jahr]) + ";"
                    + str(frost[jahr]) + "\n")

# ---- Kontrolle ------------------------------------------------------------
for name in ["fichtelberg_jahre.csv", "freiberg_jahre.csv"]:
    with open(name) as datei:
        zeilen = datei.readlines()
    print(name, len(zeilen) - 1, "Jahre, erste Zeile:", zeilen[1].strip())
```
@LIA.eval(`["hole_daten.py", "auswertung.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 auswertung.py"`)

Das Programm funktioniert — aber:

* Der Block für Freiberg ist eine **Kopie** des Blocks für den Fichtelberg. Nur der Dateiname ist anders.
* Jede Korrektur muss an **zwei** Stellen erfolgen, bei einer dritten Station an drei. Die Messtage aus Schritt 4 fehlen hier zum Beispiel noch.
* Um zu verstehen, was das Programm tut, muss man alle 50 Zeilen lesen.

> Dieses Skript ist absichtlich so geschrieben. Nächste Woche zerlegen wir es in Funktionen.

--{{0}}--
Längere Programme wie dieses schreibt man nicht mehr in den Browser, sondern in Visual Studio Code. Das Skript liegt mit allen Beispielen dieser Vorlesung im Repository unter `examples/06_DateienLesen/`.

## Zwischenbilanz: Datentypen

Mit dieser Vorlesung haben Sie alle Datentypen kennengelernt, die Sie für die erste Hälfte des Kurses brauchen:

<!-- data-type="none" -->
| Typ     | Beispiel                     | Woher er im Datensatz kommt              | Typische Falle                                  |
| :------ | :--------------------------- | :--------------------------------------- | :---------------------------------------------- |
| `int`   | `1358`, `2024`               | Stations-ID, Jahr nach `int(...)`        | `int("2024") == 2024`, aber `"2024" != 2024`    |
| `float` | `-14.1`                      | Temperaturen nach `float(...)`           | gerechnet nicht exakt: kein `==` (VL 04)        |
| `str`   | `"18930310"`                 | alles, was aus einer Datei gelesen wird  | `"9.5" > "28.1"` (VL 05)                        |
| `bool`  | `True`                       | Ergebnis jedes Vergleichs                | `=` statt `==` (VL 02)                          |
| `list`  | `[-1.9, -2.4, 0.1]`          | `zeile.split(";")`, gesammelte Ergebnisse | Index ab 0, `IndexError` (VL 05)              |
| `range` | `range(2015, 2025)`          | Jahre, Indizes                           | Endwert nicht enthalten (VL 05)                 |
| `dict`  | `{"1947": 119}`              | ein Ergebnis pro Jahr                    | `KeyError`, fehlender Eintrag ≠ 0 (VL 06)       |

> **Ausblick:** In Vorlesung 10 kommt mit dem NumPy-**Array** ein Typ hinzu, der aussieht wie eine Liste, aber elementweise rechnet. In Vorlesung 11 lernen Sie `NaN` kennen — die Art, wie pandas „kein Wert“ darstellt.

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

[[X]] `with open(...) as datei:` schließt die Datei automatisch am Ende des Blocks.
[[ ]] `datei.write("abc")` beginnt danach automatisch eine neue Zeile.
[[X]] `open("x.csv", "w")` löscht den bisherigen Inhalt von `x.csv`.
[[ ]] Fehlende Tage stehen in DWD-Dateien immer als `-999` in der Datei.
[[X]] `datei.readline()` vor der Schleife sorgt dafür, dass die Schleife mit der zweiten Zeile beginnt.
[[ ]] `open("daten.txt")` sucht die Datei im Ordner des Programms.
***
`write` hängt keinen Zeilenumbruch an. Fehlende Tage können auch ganz fehlen (1911 bis 1914). Und ein Dateiname ohne Ordner gilt relativ zum Arbeitsordner, nicht zum Ordner des Programms.
***

**Welche Zeilen gehören an die Stelle `???`, damit kein `KeyError` auftritt?**

```python
for zeile in datei:
    jahr = zeile.split(";")[1][0:4]
    ???
    frost[jahr] = frost[jahr] + 1
```

[( )] `frost = {}`
[(X)] `if jahr not in frost:` und eingerückt `frost[jahr] = 0`
[( )] `frost[jahr] = 0`
***
`frost = {}` in der Schleife leert das Dictionary bei jeder Zeile, `frost[jahr] = 0` setzt den Zähler bei jeder Zeile zurück. Nur das Anlegen beim ersten Auftreten zählt richtig.
***

## Nächste Woche

Das lange Skript funktioniert, ist aber schwer zu lesen, zu ändern und zu erweitern. Nächste Woche lernen Sie **Funktionen** — und zerlegen es live in handliche, benannte Teile.

**Zur Vorbereitung**

- [ ] Laden Sie das Repository herunter, öffnen Sie in VS Code den Ordner `examples/06_DateienLesen/` und führen Sie `frosttage.py` aus. Kommt `FileNotFoundError`, prüfen Sie den Arbeitsordner.
- [ ] Ergänzen Sie im langen Skript die Messtage aus Schritt 4: Jahre mit weniger als 300 gemessenen Tagen sollen in der Ergebnisdatei keinen Frostwert bekommen. An wie vielen Stellen müssen Sie ändern?
- [ ] Markieren Sie im langen Skript alle Zeilen, die in beiden Blöcken gleich sind.

**Zur Übung**

Blatt 6 steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 07.12.

**Zum Wiederholen:** Die Begriffe dieser Vorlesung finden Sie in der [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=6).
