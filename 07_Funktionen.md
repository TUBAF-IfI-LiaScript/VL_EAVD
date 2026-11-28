<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.1.0
language: de
narrator: Deutsch Female

comment:  Funktionen: Wiederkehrende Schritte benennen, Parameter und Rückgabewerte, lokale Variablen, Fehler abfangen — das lange Skript aus Vorlesung 06 wird zerlegt und auf eine zweite Station angewandt.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
          https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md)

# Funktionen

| Parameter                | Kursinformationen                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                              |
| **Inhalte:**             | `def, Parameter, return, None, lokale Variablen, mehrere Rückgabewerte, try und except, assert`                                                |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md) |
| **Autoren**              | @author                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Ist der Rückgang der Frosttage auf dem Fichtelberg eine Ausnahme, oder zeigt Chemnitz dasselbe?_

**Fragen an die heutige Veranstaltung ...**

* Wie gibt man wiederkehrenden Schritten einen Namen?
* Was ist der Unterschied zwischen `print` und `return`?
* Warum sind Variablen in einer Funktion „lokal“?
* Wie fängt man einen Fehler ab, ohne ihn zu verstecken?
* Wie prüft man, ob eine Funktion richtig rechnet?

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=7" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

> Die Beispiele mit echten Dateien laufen auf einem Server, genau wie Python auf Ihrem Rechner. Der erste Klick auf „Ausführen“ kann einige Sekunden dauern.

--{{0}}--
In Vorlesung 06 haben wir gezeigt, dass es auf dem Fichtelberg heute rund 28 Frosttage weniger gibt als vor 100 Jahren. Der Fichtelberg liegt aber auf 1.213 Metern Höhe. Ob dort oben dasselbe passiert wie im Tal, wo die meisten Menschen leben, wissen wir noch nicht. Die Station Chemnitz liegt heute auf 416 Metern, und ihre Datei hat dasselbe Format. Frosttage sind übrigens nicht nur eine Wetterfrage: Der Wechsel von Frost und Tauwetter sprengt Gestein, lockert Böden und setzt Hänge in Bewegung. Wir brauchen also dieselbe Auswertung ein zweites Mal. Heute lernen Sie, wie man sie dafür nicht kopiert.

--------------------------------------------------------------------------------

## Rückblick

Ihre Vorbereitungsaufgaben: `frosttage.py` auf dem eigenen Rechner ausführen und im langen Skript aus Vorlesung 06 die **Messtage** ergänzen, sodass Jahre mit weniger als 300 Messtagen keinen Frostwert bekommen.

> **An wie vielen Stellen mussten Sie ändern?** In beiden Blöcken an denselben Stellen: Dictionary `messtage` anlegen, Fach anlegen, mitzählen, beim Schreiben prüfen. Bei einer dritten Station wäre jede Änderung dreimal nötig.

Heute geben wir wiederkehrenden Schritten einen **Namen** und schreiben sie nur noch **einmal**. Dann beantworten wir die Leitfrage für Chemnitz.

--{{0}}--
Jede Kopie ist eine Stelle, an der man eine Korrektur vergessen kann. Das ist kein theoretisches Risiko: Wer im Freiberger Block die Messtage vergisst, bekommt für 1948 wieder null Frosttage, und das Programm läuft trotzdem ohne Fehlermeldung. Ihre dritte Vorbereitungsaufgabe hat gezeigt, wie viel in den beiden Blöcken gleich ist: alles außer den Dateinamen für Ein- und Ausgabe. Falls Sie nicht dazu kamen: Legen Sie die beiden Blöcke im Beispiel `examples/06_DateienLesen/auswertung.py` nebeneinander.

## Eine Funktion definieren

```` @BlocklyId(frostfunktion, runner=frostfunktion hideRunner height=420)
def ist_frosttag(minimum):
    return minimum != -999 and minimum < 0

print(ist_frosttag(-3.5))
print(ist_frosttag(2.1))
print(ist_frosttag(-999))
````

```python
# runner: frostfunktion
```
@Pyodide.eval

<!-- data-type="none" -->
| Teil                  | Bedeutung                                                      |
| :-------------------- | :------------------------------------------------------------- |
| `def`                 | Hier beginnt eine Funktionsdefinition.                         |
| `ist_frosttag`        | Der Name: Er sagt, **was** die Funktion tut.                    |
| `(minimum)`           | Der **Parameter**: ein Platzhalter für den Wert beim Aufruf.    |
| `return ...`          | Das **Ergebnis**, das die Funktion an den Aufrufer zurückgibt.  |
| `ist_frosttag(-3.5)`  | Der **Aufruf**: `minimum` bekommt den Wert `-3.5`.              |

--{{0}}--
Die Bedingung aus Vorlesung 03 steht jetzt an einer einzigen Stelle. Ändert sich die Definition eines Frosttags oder die Kodierung der Fehlwerte, ändern wir genau eine Zeile. Die Funktion wird dreimal aufgerufen, jedes Mal mit einem anderen Wert für `minimum`. Der Name einer Funktion sollte sagen, was sie liefert. `ist_frosttag` liefert `True` oder `False`, man liest den Aufruf deshalb wie eine Frage: Ist das ein Frosttag?

                                     {{1}}
*******************************************************************************

Ein Aufruf schickt einen Wert in die Funktion und bekommt das Ergebnis zurück:

<!-- style="max-width: 580px; display: block; margin: auto" -->
```ascii
 +----------------------------+          +-------------------------+
 | Hauptprogramm              |   −3.5   | Funktion ist_frosttag   |
 |                            +--------->|                         |
 | ist_frosttag(−3.5)         |          | minimum bekommt −3.5    |
 |                            |   True   | rechnet die Bedingung   |
 | Ergebnis True              |<---------+ return True             |
 +----------------------------+          +-------------------------+
```

*******************************************************************************

### Typische Fehlvorstellung: `def` führt die Funktion aus

> **Typische Fehlvorstellung:** _„Sobald Python die Zeile mit `def` erreicht, läuft die Funktion.“_

```python
def begruessung():
    print("Hallo Fichtelberg!")

print("Programmstart")
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[( )] `Hallo Fichtelberg!` und dann `Programmstart`
[(X)] nur `Programmstart`
[( )] eine Fehlermeldung, weil `begruessung` nie aufgerufen wird
***
`def` **definiert** die Funktion nur, wie ein Rezept, das man ins Kochbuch schreibt. Gekocht wird erst beim Aufruf `begruessung()`. Ohne Aufruf passiert nichts, und das ist auch kein Fehler.
***

--{{0}}--
Daraus folgt auch: Eine Funktion muss definiert sein, bevor sie aufgerufen wird. Python liest das Programm von oben nach unten. Steht der Aufruf über dem `def`, kennt Python den Namen noch nicht und meldet `NameError`. Deshalb stehen Funktionen üblicherweise oben in der Datei, das Hauptprogramm unten.

## Parameter und Rückgabewert

Eine Funktion kann mehrere Parameter haben und mit **beliebigen** Werten aufgerufen werden:

```python
def zaehle_unter(werte, grenze):
    anzahl = 0
    for wert in werte:
        if wert != -999 and wert < grenze:
            anzahl = anzahl + 1
    return anzahl

januar = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]
print("Frosttage:", zaehle_unter(januar, 0))
print("Strenger Frost:", zaehle_unter(januar, -10))
```
@Pyodide.eval

> Das ist das Zählmuster aus Vorlesung 03, jetzt mit einem Namen und mit einstellbarer Grenze. Eine Funktion ist ein **Muster, das man wiederverwenden kann**.

--{{0}}--
Die Werte beim Aufruf heißen auch Argumente: `januar` und `0` im ersten Aufruf, `januar` und `-10` im zweiten. Sie werden der Reihe nach den Parametern zugeordnet, der erste Wert dem ersten Parameter. `return` beendet die Funktion sofort und gibt den Wert dahinter zurück. Was danach in der Funktion steht, wird nicht mehr ausgeführt.

### Typische Fehlvorstellung: `print` gibt etwas zurück

> **Typische Fehlvorstellung:** _„Was eine Funktion ausgibt, kann ich weiterverwenden.“_

```python
def mittelwert(werte):
    print(sum(werte) / len(werte))

m = mittelwert([2.5, -1.5, 0.5])
print("Ergebnis:", m)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt die letzte Zeile aus?

[( )] `Ergebnis: 0.5`
[(X)] `Ergebnis: None`
[( )] eine Fehlermeldung, weil `mittelwert` nichts zurückgibt
***
`print` zeigt den Wert nur auf dem Bildschirm an, für Sie, nicht für das Programm. Zurückgegeben wird nur, was hinter `return` steht. Fehlt `return`, gibt die Funktion den besonderen Wert **`None`** zurück: „nichts“.

Die Zahl `0.5` erscheint trotzdem auf dem Bildschirm, aus dem `print` **in** der Funktion. Das macht den Fehler so tückisch. Spätestens bei `m + 1` gibt es einen `TypeError`.

Richtig: `return sum(werte) / len(werte)`.
***

--{{0}}--
`None` ist ein eigener Datentyp mit genau einem Wert. Er bedeutet „hier ist nichts“. Im Live Hacking nutzen wir ihn absichtlich: Eine Funktion, die für einen Zeitraum keinen Mittelwert bilden kann, gibt `None` zurück statt einer erfundenen Zahl.

### Typische Fehlvorstellung: Namen müssen passen

> **Typische Fehlvorstellung:** _„Der Wert, den ich übergebe, muss genauso heißen wie der Parameter.“_

Die Funktion `zaehle_unter(werte, grenze)` von oben. Legen Sie sich fest, **bevor** Sie weiterlesen: Welche Aufrufe funktionieren?

[[X]] `zaehle_unter(januar, 0)`
[[X]] `zaehle_unter([-3.0, 1.0], -1)`
[[X]] `zaehle_unter(werte=januar, grenze=0)`
[[ ]] Nur Aufrufe, bei denen die übergebene Liste `werte` heißt.
***
Beim Aufruf wird der **Wert** übergeben, nicht der Name. In der Funktion heißt er dann `werte`, egal, wie er außerhalb hieß oder ob er überhaupt einen Namen hatte. Die dritte Variante nennt die Parameter ausdrücklich; das macht lange Aufrufe lesbarer.
***

## Lokale Variablen

Variablen, die **in** einer Funktion entstehen, existieren nur während des Aufrufs:

```python
def zaehle_frost(werte):
    anzahl = 0
    for wert in werte:
        if wert != -999 and wert < 0:
            anzahl = anzahl + 1
    return anzahl

ergebnis = zaehle_frost([-1.9, 0.1, -4.2])
print(ergebnis)
print(anzahl)
```
@Pyodide.eval

Die letzte Zeile scheitert mit `NameError`: `anzahl` ist eine **lokale** Variable der Funktion. Nach dem Aufruf ist sie verschwunden, nur der Rückgabewert kommt heraus.

--{{0}}--
Das ist kein Mangel, sondern der eigentliche Nutzen: Eine Funktion kann intern beliebige Namen verwenden, ohne Variablen im restlichen Programm zu überschreiben. Wer das Hauptprogramm liest, muss nicht wissen, wie die Funktion innen aussieht. Auch der Parameter `werte` und die Schleifenvariable `wert` sind lokal. Die Grenze gilt nur in eine Richtung: Findet Python einen Namen nicht in der Funktion, sucht es draußen weiter. Lesen geht also, und ein Dictionary von draußen kann die Funktion auch verändern. Im Live Hacking sehen Sie, wozu das führt.

                                     {{1}}
*******************************************************************************

<!-- style="max-width: 640px; display: block; margin: auto" -->
```ascii
  während des Aufrufs                       nach dem Aufruf
 +-----------------------------------+     +-------------------------+
 | Hauptprogramm                     |     | Hauptprogramm           |
 |                                   |     |                         |
 |   +---------------------------+   |     |   ergebnis = 2          |
 |   | Funktion zaehle_frost     |   |     |                         |
 |   |   werte = [−1.9, 0.1, …]  |   |     |   anzahl: gibt es nicht |
 |   |   anzahl = 2              |   |     |                         |
 |   |   wert = −4.2             |   |     +-------------------------+
 |   +-------------+-------------+   |
 |                 | return 2        |
 |                 v                 |
 |   ergebnis = 2                    |
 +-----------------------------------+
```

*******************************************************************************

## Fehler abfangen: try und except

Mit `try` und `except` fängt man einen **erwarteten** Fehler ab, statt abzubrechen, aber nur den, den man nennt:

```python
texte = ["-6.2", " TNK", "-3.8", "-999"]
for text in texte:
    try:
        wert = float(text)
        print("Zahl:", wert)
    except ValueError:
        print("Keine Zahl:", text)
```
@Pyodide.eval

* Python führt den `try`-Block aus. Tritt dort ein `ValueError` auf, springt es in den `except`-Block, und das Programm läuft weiter.
* `" TNK"` stammt aus der Kopfzeile der DWD-Datei (Vorlesung 06). Ohne `try` bricht `float` dort ab.
* `-999` ist für Python eine gültige Zahl. Fehlwerte erkennen Sie weiter mit `!= -999`.

<!-- data-type="none" -->
| Fehler hinter `except`  | tritt auf, wenn …             |
| :---------------------- | :---------------------------- |
| `ValueError`            | ein Text keine Zahl ist        |
| `KeyError`              | ein Schlüssel fehlt            |
| `FileNotFoundError`     | eine Datei nicht da ist        |
| `ZeroDivisionError`     | durch null geteilt wird        |

--{{0}}--
Der Name des Fehlers steht in der letzten Zeile jeder Fehlermeldung. Genau diesen Namen schreiben Sie hinter `except`. Ein typischer Einsatz ist eine Schleife über mehrere Dateien: Fehlt eine, meldet das Programm das und wertet die übrigen trotzdem aus. Das ist eine Ihrer Vorbereitungsaufgaben.

### Typische Fehlvorstellung: `except` macht das Programm richtig

> **Typische Fehlvorstellung:** _„Mit `try` und `except` gibt es keine Fehler mehr.“_

```python
summe = 0
anzahl = 0
for text in ["-3.5", "2,1", "-999", "0.4"]:
    try:
        summe = summe + float(text)
        anzahl = anzahl + 1
    except:
        pass
print("Mittelwert:", round(summe / anzahl, 2))
```
@Pyodide.eval

`except:` ohne Namen fängt **jeden** Fehler ab, `pass` heißt „tue nichts“. Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[( )] eine Fehlermeldung, weil `"2,1"` keine Zahl ist
[( )] `Mittelwert: -0.33`, aus -3.5, 2.1 und 0.4
[( )] `Mittelwert: -1.55`, aus -3.5 und 0.4
[(X)] `Mittelwert: -334.03`
***
Zwei Fehler, keine Meldung:

* `"2,1"` hat ein Komma. `float` scheitert, `except` verschluckt den Fehler, und ein echter Messwert fehlt **still**.
* `-999` ist eine gültige Zahl. Es gibt keinen Fehler, den `except` abfangen könnte, und der Fehlwert geht in den Mittelwert ein: (-3.5 - 999 + 0.4) / 3.

`except` fängt Abbrüche ab, keine falschen Werte. Deshalb: den Fehler beim Namen nennen (`except ValueError:`) und melden, was übersprungen wurde.
***

> **KI und Fehlermeldungen:** Bitten Sie eine KI, eine Fehlermeldung „wegzumachen“, schlägt sie oft `try` und `except` vor, manchmal mit `except: pass`. Dann ist die Meldung weg, der Fehler nicht. Fragen Sie: Welcher Fehler wird abgefangen, und was passiert mit dem Wert?

--{{0}}--
Eine Fehlermeldung ist eine Information: Sie sagt, dass das Programm auf etwas gestoßen ist, das es nicht erwartet hat. Wer sie unterdrückt, verliert diese Information. Ein Programm, das abbricht, ist ärgerlich. Ein Programm, das still ein falsches Ergebnis liefert, ist gefährlich, weil es niemand bemerkt. Das ist derselbe Faden wie bei Freiberg 1948 in Vorlesung 06.

## Live Hacking: Das lange Skript zerlegen

> [!NOTE] ❓ Aufgabe
>
> _Ist der Rückgang der Frosttage auf dem Fichtelberg eine Ausnahme, oder zeigt Chemnitz dasselbe?_
>
> Machen Sie aus der Frostzählung des langen Skripts Funktionen und vergleichen Sie die Mittelwerte 1961–1990 und 1995–2024 für den Fichtelberg und Chemnitz.

> **Live Hacking (≈ 20 min).** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam. Die Schritte unten zeigen die typischen Irrwege.

--{{0}}--
Wir nehmen uns den Frost-Teil des langen Skripts vor, mit den Messtagen aus Ihrer Vorbereitungsaufgabe. Höchstwerte und Ergebnisdatei lassen wir heute weg, das Prinzip ist dasselbe. Die vollständig zerlegte Fassung mit allen Teilen finden Sie in `examples/07_Funktionen/auswertung.py`. Den Zeitraum 1891 bis 1920 aus Vorlesung 06 vergleichen wir heute nicht: In der Chemnitzer Datei fehlen die Jahre 1902 bis 1934 ganz, für diesen Zeitraum blieben nur zehn Jahre.

### Pseudocode - Was wiederholt sich?

> **Wie würden Sie vorgehen?**
>
> * Welche Zeilen unterscheiden sich in den beiden Blöcken des langen Skripts? Das war Ihre dritte Vorbereitungsaufgabe.
> * Was muss eine Funktion also bekommen, und was muss sie zurückgeben?
> * Was rechnen wir danach mit den Ergebnissen aus?

                                     {{1}}
*******************************************************************************

Nur die **Dateinamen** unterscheiden sich. Die Ergebnisdatei lassen wir heute weg, der Name der Messdatei wird zum Parameter:

```text
auswerten(dateiname)                  liefert frost und messtage
mittel_frost(frost, messtage, start)  liefert den Mittelwert über 30 Jahre

Hauptprogramm:
    Für jede Station:
        auswerten
        Für die Startjahre 1961 und 1995: mittel_frost ausgeben
```

*******************************************************************************

### Schritt 1 - Die Auswertung wird eine Funktion

Der Frost-Teil des langen Skripts, eingerückt unter `def`:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateiname = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
os.makedirs(os.path.dirname(dateiname), exist_ok=True)
urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
FICHTELBERG = ("data/fichtelberg/"
               "produkt_klima_tag_18900801_20251231_01358.txt")

def auswerten(dateiname):
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

auswerten(FICHTELBERG)
print("Fichtelberg 2024:", frost["2024"])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Die letzten beiden Zeilen rufen `auswerten(FICHTELBERG)` auf und geben danach `frost["2024"]` aus. Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert?

[( )] `Fichtelberg 2024: 127`
[( )] `Fichtelberg 2024: None`
[(X)] `NameError: name 'frost' is not defined`
***
`frost` ist eine **lokale** Variable von `auswerten`. Die Funktion hat alles richtig gezählt, aber nach dem Aufruf ist das Dictionary verschwunden. Nichts davon kommt heraus, weil die Funktion nichts zurückgibt.
***

--{{0}}--
Der Name `FICHTELBERG` in Großbuchstaben ist eine Vereinbarung unter Programmierenden: Großbuchstaben bedeuten „dieser Wert ändert sich im Programm nicht“. Python selbst behandelt ihn wie jede andere Variable. Die Klammern um die beiden Textteile erlauben es, einen langen Dateinamen auf zwei Zeilen zu verteilen. Python setzt die Teile wieder zusammen.

### Schritt 2 - Die Dictionaries nach draußen

Naheliegende Abhilfe: `frost` und `messtage` **vor** der Funktion anlegen, dann gibt es sie auch danach. Und gleich noch Chemnitz dazu:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python main.py
FICHTELBERG = ("data/fichtelberg/"
               "produkt_klima_tag_18900801_20251231_01358.txt")
CHEMNITZ = ("data/chemnitz/"
            "produkt_klima_tag_18820101_20251231_00853.txt")
frost = {}
messtage = {}

def auswerten(dateiname):
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

auswerten(FICHTELBERG)
print("Fichtelberg 2024:", frost["2024"])
auswerten(CHEMNITZ)
print("Chemnitz 2024:", frost["2024"])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

Die letzten Zeilen werten erst den Fichtelberg, dann Chemnitz aus und geben jeweils `frost["2024"]` aus. Für den Fichtelberg kennen wir 127. Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was meldet es für Chemnitz?

[( )] weniger als 127, Chemnitz liegt rund 800 Meter tiefer
[(X)] mehr als 127
[( )] eine Fehlermeldung, weil `frost` außerhalb der Funktion steht
***
`Chemnitz 2024: 178`, ohne Fehlermeldung. Im wärmeren Tal mehr Frosttage als auf dem Berg? Das kann nicht stimmen.

Lesen geht nach draußen: Findet Python `frost` nicht in der Funktion, nimmt es das Dictionary von draußen, und `frost[jahr] = …` verändert genau dieses.
***

                                     {{1}}
*******************************************************************************

Beide Aufrufe zählen in **dasselbe** Dictionary. Chemnitz hatte 2024 nur 51 Frosttage, die Funktion hat sie zu den 127 vom Fichtelberg addiert:

<!-- style="max-width: 600px; display: block; margin: auto" -->
```ascii
 auswerten(FICHTELBERG) --- 127 dazu ---+
                                        |
                                        v
                      +-----------------------------------+
                      | frost (außerhalb der Funktion)    |
                      |   2024: 178, also 127 und 51      |
                      +-----------------------------------+
                                        ^
                                        |
 auswerten(CHEMNITZ) ------ 51 dazu ----+
```

> **Regel:** Was eine Funktion braucht, bekommt sie als Parameter oder legt sie selbst an. Was sie liefert, gibt sie mit `return` zurück. Ausnahme: Konstanten wie `MINDESTTAGE`, die oben im Programm stehen und sich nie ändern.

*******************************************************************************

--{{0}}--
Für eine einzige Station hätte diese Abhilfe funktioniert, und genau das macht sie gefährlich: Der Fehler zeigt sich erst beim zweiten Aufruf, und auch dann ohne Fehlermeldung. Bemerkt haben wir ihn nur, weil wir wissen, dass es im Tal weniger Frost gibt als auf dem Berg. Eine Plausibilitätsprüfung mit Vorwissen ist oft die schnellste Kontrolle.

### Schritt 3 - Ergebnisse mit return

`frost` und `messtage` zurück in die Funktion, am Ende `return frost, messtage`. Die Stationen stehen jetzt in einem Dictionary: Name → Datei.

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python -auswerten.py
def auswerten(dateiname):
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

```
```python main.py
STATIONEN = {
    "Fichtelberg": ("data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "Chemnitz": ("data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
}

for name in STATIONEN:
    frost, messtage = auswerten(STATIONEN[name])
    print(name, "2024:", frost["2024"], "Frosttage an",
          messtage["2024"], "Messtagen")
```
@LIA.eval(`["hole_daten.py", "auswerten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && cat auswerten.py main.py > programm.py && python3 programm.py"`)

* `return frost, messtage` gibt **zwei** Werte zurück. `frost, messtage = auswerten(...)` verteilt sie der Reihe nach auf zwei Namen. Die Reihenfolge muss stimmen, Python prüft sie nicht.
* Jeder Aufruf legt **neue**, leere Dictionaries an. Fichtelberg 127, Chemnitz 51.
* `auswerten` ist eingeklappt, damit das Hauptprogramm auf die Folie passt. Bei Ihnen steht alles in **einer** `.py`-Datei, die Funktionen oben.

--{{0}}--
Dass die Namen draußen wieder `frost` und `messtage` heißen, ist Zufall und Bequemlichkeit. Sie könnten auch `frost_tage` heißen, es kommt nur auf die Reihenfolge an. Zum Einklappen: Der Server hängt `auswerten.py` und `main.py` vor dem Start zu einer Datei `programm.py` zusammen, deshalb nennt eine Fehlermeldung diesen Namen. Auf Ihrem Rechner steht alles in einer Datei. Wie man Funktionen sauber auf mehrere Dateien verteilt, lernen Sie in Vorlesung 09.

### Schritt 4 - Mittelwerte als zweite Funktion

Das Mittelwertmuster aus Vorlesung 06 wird zur Funktion `mittel_frost`. Es zählen nur Jahre mit mindestens 300 Messtagen. `STATIONEN` ist jetzt mit `auswerten` eingeklappt:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python -auswerten.py
STATIONEN = {
    "Fichtelberg": ("data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "Chemnitz": ("data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
}

def auswerten(dateiname):
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

```
```python main.py
MINDESTTAGE = 300

def mittel_frost(frost, messtage, start):
    summe = 0
    anzahl = 0
    for jahr in range(start, start + 30):
        schluessel = str(jahr)        # Schlüssel sind Text: "1961"
        if schluessel in frost and messtage[schluessel] >= MINDESTTAGE:
            summe = summe + frost[schluessel]
            anzahl = anzahl + 1
    return round(summe / anzahl, 1)

for name in STATIONEN:
    frost, messtage = auswerten(STATIONEN[name])
    for start in [1961, 1995]:
        print(name, start, "bis", start + 29, "→",
              mittel_frost(frost, messtage, start), "Frosttage")
```
@LIA.eval(`["hole_daten.py", "auswerten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && cat auswerten.py main.py > programm.py && python3 programm.py"`)

                                     {{1}}
*******************************************************************************

<!-- data-type="none" -->
| Station     | 1961–1990 | 1995–2024 | Rückgang                  |
| :---------- | --------: | --------: | :------------------------ |
| Fichtelberg |     171,2 |     154,7 | 16,5 Tage, knapp 10 %     |
| Chemnitz    |      94,6 |      79,6 | 15,0 Tage, knapp 16 %     |

**Antwort auf die Leitfrage:** Der Fichtelberg ist keine Ausnahme. Auch in Chemnitz fehlen heute rund 15 Frosttage, gemessen am Ausgangswert sogar mehr. Das sind zwei Stationen, noch kein Beweis für ganz Sachsen.

Die 28 Tage aus Vorlesung 06 bezogen sich auf 1891–1920. Für Chemnitz fehlen die Jahre 1902–1934, deshalb vergleichen wir heute ab 1961.

*******************************************************************************

--{{0}}--
`MINDESTTAGE` steht als Konstante oben, damit man die Grenze an einer Stelle ändern kann. Sie gilt für alle Stationen gleich, deshalb ist sie kein Parameter. Die Prozentangaben: 16,5 von 171,2 sind 9,6 Prozent, 15,0 von 94,6 sind 15,9 Prozent. In absoluten Tagen ist der Rückgang an beiden Orten fast gleich, Chemnitz hatte aber von vornherein weniger Frosttage zu verlieren. Eine Einschränkung verrät erst die Metadatendatei: Die Station Chemnitz ist 1976 umgezogen, von 357 auf 416 Meter Höhe. Der Zeitraum 1961 bis 1990 mischt also zwei Standorte. Solche Stationswechsel können eine Messreihe verfälschen; in Vorlesung 14 kommen wir darauf zurück.

### Schritt 5 - Eine dritte Station

Freiberg ist **ein Eintrag** im Dictionary. Beide Funktionen sind jetzt eingeklappt:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt",
           "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python -funktionen.py
MINDESTTAGE = 300

def auswerten(dateiname):
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
    summe = 0
    anzahl = 0
    for jahr in range(start, start + 30):
        schluessel = str(jahr)        # Schlüssel sind Text: "1961"
        if schluessel in frost and messtage[schluessel] >= MINDESTTAGE:
            summe = summe + frost[schluessel]
            anzahl = anzahl + 1
    return round(summe / anzahl, 1)

```
```python main.py
STATIONEN = {
    "Fichtelberg": ("data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "Chemnitz": ("data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
    "Freiberg": ("data/freiberg/"
                 "produkt_klima_tag_19450701_19930430_01441.txt"),
}

for name in STATIONEN:
    frost, messtage = auswerten(STATIONEN[name])
    for start in [1961, 1995]:
        print(name, start, "bis", start + 29, "→",
              mittel_frost(frost, messtage, start), "Frosttage")
```
@LIA.eval(`["hole_daten.py", "funktionen.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && cat funktionen.py main.py > programm.py && python3 programm.py"`)

Die Freiberger Temperaturreihe in unserer Datei endet im April 1993. Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert beim Zeitraum 1995 bis 2024?

[( )] Freiberg bekommt 0 Frosttage.
[( )] Python überspringt den Zeitraum.
[(X)] Das Programm bricht mit einer Fehlermeldung ab.
***
`ZeroDivisionError: division by zero`: Kein einziges Jahr erfüllt die Bedingung, `anzahl` bleibt 0. Abhilfe in `mittel_frost`, vor der Division:

```python
    if anzahl == 0:
        return None
```

Warum nicht `return 0`? Null Frosttage wäre eine Aussage über das Wetter. `None` sagt ehrlich: Für diesen Zeitraum gibt es keinen Wert. Das ist dieselbe Unterscheidung wie bei Freiberg 1948 in Vorlesung 06.
***

--{{0}}--
Hier wäre auch `try` und `except ZeroDivisionError` möglich gewesen. Die Prüfung `if anzahl == 0` ist aber klarer: Sie sagt genau, welchen Fall wir erwarten, und behandelt ihn dort, wo er entsteht. `try` und `except` lohnen sich vor allem für Fehler, die man nicht vorher prüfen kann, etwa ob eine Datei lesbar ist.

### Ergebnis

Mit der Abhilfe aus Schritt 5:

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
dateien = ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
           "data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt",
           "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"]
for dateiname in dateien:
    os.makedirs(os.path.dirname(dateiname), exist_ok=True)
    urllib.request.urlretrieve(basis + dateiname, dateiname)
```
```python -funktionen.py
MINDESTTAGE = 300          # weniger Messtage: Jahr zählt nicht


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
        schluessel = str(jahr)        # Schlüssel sind Text: "1961"
        if schluessel in frost and messtage[schluessel] >= MINDESTTAGE:
            summe = summe + frost[schluessel]
            anzahl = anzahl + 1
    if anzahl == 0:
        return None
    return round(summe / anzahl, 1)

```
```python main.py
STATIONEN = {
    "Fichtelberg": ("data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "Chemnitz": ("data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
    "Freiberg": ("data/freiberg/"
                 "produkt_klima_tag_19450701_19930430_01441.txt"),
}

for name in STATIONEN:
    frost, messtage = auswerten(STATIONEN[name])
    for start in [1961, 1995]:
        print(name, start, "bis", start + 29, "→",
              mittel_frost(frost, messtage, start), "Frosttage")
```
@LIA.eval(`["hole_daten.py", "funktionen.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && cat funktionen.py main.py > programm.py && python3 programm.py"`)

<!-- data-type="none" -->
| Vorher (Vorlesung 06)                    | Nachher                                              |
| :--------------------------------------- | :--------------------------------------------------- |
| zwei kopierte Blöcke                     | eine Funktion `auswerten`, für jede Station aufgerufen |
| Messtage an zwei Stellen nachtragen      | eine Konstante `MINDESTTAGE`, eine Bedingung          |
| dritte Station: einen Block kopieren     | dritte Station: ein Eintrag in `STATIONEN`            |
| um das Programm zu verstehen, alles lesen | Hauptprogramm lesen, Funktionen nur bei Bedarf       |

> Die Texte in dreifachen Anführungszeichen direkt unter `def` heißen **Docstrings**. Sie beschreiben, was die Funktion tut, und erscheinen, wenn man `help(auswerten)` aufruft.

--{{0}}--
Freiberg 1961 bis 1990 hat 91,5 Frosttage im Mittel, ähnlich wie Chemnitz. Für 1995 bis 2024 steht dort `None`. Schöner wäre die Ausgabe „keine Daten“; das ist eine kleine Übung für zu Hause. Die vollständige Fassung mit Höchstwerten und Ergebnisdateien liegt in `examples/07_Funktionen/auswertung.py`.

## Funktionen prüfen

Eine Funktion mit klarem Ein- und Ausgang lässt sich einzeln prüfen. `assert` bricht mit einer Fehlermeldung ab, wenn eine Bedingung **nicht** erfüllt ist:

```python
def ist_frosttag(minimum):
    return minimum != -999 and minimum < 0

assert ist_frosttag(-0.1) == True
assert ist_frosttag(0.0) == False
assert ist_frosttag(-999) == False
print("Alle Prüfungen bestanden.")
```
@Pyodide.eval

Ändern Sie die Funktion zu `return minimum < 0` und führen Sie die Prüfungen erneut aus. Welche schlägt fehl?

> Gute Prüffälle liegen **an den Grenzen**: genau 0,0 °C, knapp darunter, und der Fehlwert. Genau dort stecken die Fehler, die man beim Draufschauen übersieht.

--{{0}}--
Für `mittel_frost` lägen die Grenzen bei einem Jahr mit genau 300 Messtagen, das zählt, einem mit 299, das nicht zählt, und einem Zeitraum ganz ohne Daten wie Freiberg 1995 bis 2024. Solche Prüfungen mit kleinen, von Hand gebauten Dictionaries finden Sie in `examples/07_Funktionen/pruefen.py`. Der Fehler aus Schritt 5 wäre damit aufgefallen, bevor wir Freiberg ausgewertet haben, vorausgesetzt, man schreibt den Fall „keine Daten“ als Prüffall auf.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
def verdopple(x):
    x = x * 2
    return x

x = 5
y = verdopple(x)
print(x, y)
```

[( )] `10 10`
[(X)] `5 10`
[( )] `5 5`
[( )] eine Fehlermeldung, weil `x` zweimal vorkommt
***
Das `x` in der Funktion ist ein **anderes** `x` als das im Hauptprogramm: ein lokaler Parameter, der beim Aufruf den Wert 5 bekommt. Die Funktion ändert nur ihr eigenes `x`. Das `x` draußen bleibt 5. Anders in Schritt 2 des Live Hackings: Dort hat die Funktion kein eigenes `frost` angelegt, sondern mit `frost[jahr] = …` das Dictionary von draußen verändert.
***

**Welche Aussagen stimmen?**

[[X]] Eine Funktion ohne `return` gibt `None` zurück.
[[ ]] `print` in einer Funktion gibt den Wert an den Aufrufer zurück.
[[X]] Nach `return` wird der Rest der Funktion nicht mehr ausgeführt.
[[X]] Eine Funktion muss definiert sein, bevor sie aufgerufen wird.
[[ ]] Lokale Variablen einer Funktion sind nach dem Aufruf im Hauptprogramm verfügbar.
***
`print` zeigt nur an, zurückgegeben wird mit `return`. Lokale Variablen verschwinden nach dem Aufruf, das war der `NameError` aus Schritt 1 im Live Hacking.
***

**Welche Werte landen in der Liste `zahlen`?**

```python
zahlen = []
for text in ["1.5", "n/a", "-999", "2,0"]:
    try:
        zahlen.append(float(text))
    except ValueError:
        print("übersprungen:", text)
```

[[X]] `1.5`
[[ ]] `n/a`
[[X]] `-999.0`
[[ ]] `2.0`
***
`"n/a"` und `"2,0"` lösen einen `ValueError` aus und werden mit Meldung übersprungen. `-999` ist eine gültige Zahl und landet in der Liste. Den Fehlwert muss man weiterhin selbst mit `!= -999` aussortieren.
***

**Ergänzen Sie die Funktion.**

Die Funktion soll den Mittelwert aller gültigen Werte zurückgeben, oder `None`, wenn es keinen gültigen Wert gibt.

```python
def mittel_ohne_fehlwerte(werte):
    summe = 0
    anzahl = 0
    for wert in werte:
        if wert != -999:
            summe = summe + wert
            anzahl = anzahl + 1
    # ... Ihre Ergänzung
```

<details>
<summary>**Lösung**</summary>

```python
    if anzahl == 0:
        return None
    return summe / anzahl
```

Ohne die Prüfung gäbe es bei einem Jahr ohne Messwerte eine Division durch null, genau der Fall Freiberg 1948.

</details>

## Nächste Woche

Nächste Woche ist **Demonstration**: Ein Mikrocontroller misst, MicroPython steuert ihn. Bis hierher kamen alle Daten fertig aus einer Datei. Dann sehen Sie, wie sie entstehen.

Im Januar geht es mit Vorlesung 09 weiter: Die Funktionen von heute wandern in eine eigene Datei, ein **Modul**.

**Zur Vorbereitung**

- [ ] Öffnen Sie in Visual Studio Code den Ordner `examples/07_Funktionen/` und führen Sie `frosttage_stationen.py` aus. Ändern Sie die Ausgabe so, dass statt `None` der Text „keine Daten“ erscheint.
- [ ] Schreiben Sie in `frosttage_stationen.py` einen Dateinamen absichtlich falsch. Fangen Sie den `FileNotFoundError` ab, sodass das Programm diese Station mit einem Hinweis überspringt und die übrigen auswertet.
- [ ] Schreiben Sie eine Funktion `laengste_frostperiode(minima)` mit dem Muster aus Vorlesung 04 und prüfen Sie sie mit `assert`, auch mit einer leeren Liste.

**Zur Übung**

Blatt 7 steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 14.12.

**Zum Wiederholen:** Die Begriffe dieser Vorlesung finden Sie in der [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=7).
