<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Prüfen und Wiederholen: Bedingungen mit if/elif/else, logische Verknüpfungen und die for-Schleife — am Beispiel der Frosttage auf dem Fichtelberg.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

@style
.flex-container {
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    gap: 20px;
}

.flex-child {
    flex: 1;
    min-width: 260px;
}
@end

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/03_PruefenUndWiederholen.md)

# Prüfen und Wiederholen

| Parameter                | Kursinformationen                                                                                                                                                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                      |
| **Semester**             | @config.semester                                                                                                                                                     |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                    |
| **Inhalte:**             | `if, elif, else, Einrückung, and/or/not, for-Schleife, Zählmuster`                                                                                                   |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/03_PruefenUndWiederholen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/03_PruefenUndWiederholen.md) |
| **Autoren**              | @author                                                                                                                                                              |

--------------------------------------------------------------------------------

**Leitfrage:** _An wie vielen Tagen gab es 2024 auf dem Fichtelberg Frost?_

**Fragen an die heutige Veranstaltung ...**

* Wie trifft ein Programm Entscheidungen?
* Warum ist Einrückung in Python keine Formsache?
* Wie verknüpft man mehrere Bedingungen?
* Wie wiederholt man dieselbe Anweisung für jeden Wert einer Messreihe?

--------------------------------------------------------------------------------

## Rückblick

Aus der letzten Vorlesung wissen Sie: Ein Vergleich liefert einen Wahrheitswert.

```python
minimum = -3.5
print(minimum < 0)
```
@Pyodide.eval

Die Frage aus Vorlesung 01 war aber nicht "Ist dieser Wert kleiner als 0?", sondern:

> _Wie viele von 366 Werten sind kleiner als 0?_

Dafür brauchen wir zwei neue Werkzeuge: eines, das abhängig von einem Wahrheitswert **etwas tut oder lässt**, und eines, das dieselbe Prüfung **für jeden Wert wiederholt**.

## Python auf Ihrem Rechner

Ab heute arbeiten wir zusätzlich mit Python-Dateien auf Ihrem Rechner. Die Browserbeispiele bleiben — für die Übungen schreiben Sie aber `.py`-Dateien.

<div class="flex-container">
<div class="flex-child">

**1. Datei anlegen**

In Visual Studio Code: _Datei → Neue Datei_, speichern als `frost.py`.

```python frost.py
minimum = -3.5
print("Minimum:", minimum)
```

</div>
<div class="flex-child">

**2. Ausführen**

Entweder über den ▷-Knopf oben rechts, oder im Terminal:

```bash
python frost.py
```

Unter Windows heißt der Befehl gegebenenfalls `py frost.py`.

</div>
</div>

> Warum der Umweg über Dateien? Ein Programm in einer Datei können Sie **speichern, wieder ausführen, weitergeben und verbessern**. Genau das unterscheidet es von einer Formel, die man einmal in eine Zelle tippt.

## Entscheidungen: `if`

```` @BlocklyId(ifeinfach, runner=ifeinfach hideRunner height=260)
minimum = -3.5

if minimum < 0:
    print("Frosttag!")

print("Prüfung beendet.")
````

```python
# runner: ifeinfach
```
@Pyodide.eval

Ändern Sie `minimum` auf `2.1`. Welche Zeile wird dann nicht mehr ausgegeben?

### Einrückung ist Syntax

                                     {{0-1}}
*******************************************************************************

Woher weiß Python, welche Anweisungen zum `if` gehören? **An der Einrückung.**

``` ascii
if minimum < 0:                 ← Doppelpunkt: jetzt kommt ein Block
    print("Frosttag!")          ← eingerückt: gehört zum if
    zaehler = zaehler + 1       ← eingerückt: gehört zum if
print("Prüfung beendet.")       ← nicht eingerückt: läuft immer
```

Übliche Einrückung sind **vier Leerzeichen**. Visual Studio Code setzt sie automatisch, wenn Sie nach dem Doppelpunkt Enter drücken.

*******************************************************************************

                                     {{1}}
*******************************************************************************

Zwei Programme, die sich nur in der Einrückung der letzten Zeile unterscheiden:

<div class="flex-container">
<div class="flex-child">

```python
minimum = 2.1
if minimum < 0:
    print("Frosttag!")
print("Minimum geprüft.")
```
@Pyodide.eval

</div>
<div class="flex-child">

```python
minimum = 2.1
if minimum < 0:
    print("Frosttag!")
    print("Minimum geprüft.")
```
@Pyodide.eval

</div>
</div>

> In vielen anderen Sprachen markieren Klammern `{ }` die Blöcke, die Einrückung ist nur Kosmetik. In Python **ist** die Einrückung die Struktur. Falsch eingerückter Code ist falscher Code.

*******************************************************************************

### Entweder – oder: `else`

Soll auch im anderen Fall etwas passieren, folgt ein `else`:

```python
minimum = 2.1

if minimum < 0:
    print("Frosttag")
else:
    print("frostfrei")
```
@Pyodide.eval

Genau **einer** der beiden Blöcke wird ausgeführt — nie beide, nie keiner.

### Mehrere Fälle: `elif`

Der Deutsche Wetterdienst kennt feste Begriffe für besondere Tage, alle definiert über das **Tagesmaximum**:

<!-- data-type="none" -->
| Begriff        | Bedingung                 | Fichtelberg 2024 |
| :------------- | :------------------------ | ---------------: |
| Eistag         | Maximum < 0 °C            | 44               |
| Sommertag      | Maximum ≥ 25 °C           | 6                |
| Heißer Tag     | Maximum ≥ 30 °C           | 0                |

Mit `elif` ("else if") prüft man mehrere Fälle nacheinander:

```python
maximum = 26.9

if maximum >= 30:
    print("Heißer Tag")
elif maximum >= 25:
    print("Sommertag")
elif maximum < 0:
    print("Eistag")
else:
    print("gewöhnlicher Tag")
```
@Pyodide.eval

> Python prüft von oben nach unten und nimmt **den ersten Fall, der zutrifft**. Alle weiteren werden übersprungen.

**Die Reihenfolge zählt.** Was gibt dieses Programm für `maximum = 31.0` aus?

```python
maximum = 31.0

if maximum >= 25:
    print("Sommertag")
elif maximum >= 30:
    print("Heißer Tag")
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen:

[( )] `Heißer Tag`
[(X)] `Sommertag`
[( )] `Sommertag` und `Heißer Tag`
***
31 ist größer als 25, also trifft schon der erste Fall zu. Der zweite wird **nie** erreicht — für keinen einzigen Wert. Jeder heiße Tag ist auch ein Sommertag; der speziellere Fall muss deshalb zuerst geprüft werden.
***

### Bedingungen verknüpfen

Manchmal hängt eine Entscheidung von mehreren Bedingungen ab:

<!-- data-type="none" -->
| Operator | Bedeutung                         | Beispiel                              |
| :------- | :-------------------------------- | :------------------------------------ |
| `and`    | beide müssen zutreffen            | `minimum < 0 and maximum > 0`         |
| `or`     | mindestens eine muss zutreffen    | `maximum >= 25 or minimum < -10`      |
| `not`    | kehrt den Wahrheitswert um        | `not minimum < 0`                     |

```python
minimum = -4.2
maximum = 2.6

if minimum < 0 and maximum > 0:
    print("Frost-Tau-Wechsel: nachts Frost, tagsüber Tauwetter")
```
@Pyodide.eval

> Frost-Tau-Wechsel sind für Geologen und Bauingenieure interessant: Gefrierendes Wasser sprengt Gestein und Beton.

                                     {{1}}
*******************************************************************************

**Der Fehlwert schlägt zurück**

Erinnern Sie sich an `-999`? Der DWD kennzeichnet so Tage, an denen nicht gemessen wurde.

```python
minimum = -999

if minimum < 0:
    print("Frosttag")
```
@Pyodide.eval

Ein Tag ohne Messung als Frosttag gezählt — ohne jede Fehlermeldung. Korrigieren Sie die Bedingung.

<details>
<summary>**Lösung**</summary>

```python
if minimum != -999 and minimum < 0:
    print("Frosttag")
```

Kein Programm erkennt einen Fehlwert von selbst. Sie müssen wissen, wie er im Datensatz kodiert ist — dafür steht es in der Datensatzbeschreibung.

</details>

*******************************************************************************

## Wiederholen: `for`

Eine Prüfung für einen Wert können wir jetzt. Für 366 Werte brauchen wir eine **Schleife**.

In Python schreibt man mehrere Werte als **Liste** in eckige Klammern. Die `for`-Schleife nimmt sich dann **jeden Wert der Reihe nach** vor:

```python
minima = [-14.1, -12.1, -11.1, -10.2, -8.3, -7.5, -6.5]

for minimum in minima:
    print("Nächster Wert:", minimum)

print("Fertig.")
```
@Pyodide.eval

Lesen Sie die Schleife als: _"Für jedes `minimum` in `minima`: führe den eingerückten Block aus."_ Der Name `minimum` bekommt bei jedem Durchlauf den nächsten Wert der Liste.

> Listen lernen Sie in Vorlesung 05 genauer kennen. Heute reicht: Eine Liste enthält mehrere Werte, und `for` geht sie der Reihe nach durch.

### Das Zählmuster

Jetzt setzen wir alles zusammen — Schleife, Bedingung und eine Variable, die mitzählt:

```` @BlocklyId(frostwoche, runner=frostwoche hideRunner height=380)
# Tiefsttemperaturen vom 1. bis 7. Januar 2024
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]

frosttage = 0

for minimum in minima:
    if minimum < 0:
        frosttage = frosttage + 1

print("Frosttage:", frosttage)
````

```python
# runner: frostwoche
```
@Pyodide.eval

Dieses **Zählmuster** hat immer drei Teile:

<!-- data-type="none" -->
| Teil             | Code                          | Wo?                           |
| :--------------- | :---------------------------- | :---------------------------- |
| Zähler anlegen   | `frosttage = 0`               | **vor** der Schleife          |
| Bedingt erhöhen  | `frosttage = frosttage + 1`   | **in** der Schleife, im `if`  |
| Ergebnis nutzen  | `print(...)`                  | **nach** der Schleife         |

### Schleifen im Kopf ausführen

                                     {{0-1}}
*******************************************************************************

Wie in der letzten Vorlesung legen wir eine Tabelle an — diesmal eine Zeile pro Schleifendurchlauf:

<!-- data-type="none" -->
| Durchlauf | `minimum` | `minimum < 0` | `frosttage` danach |
| :-------: | --------: | :-----------: | :----------------: |
| –         | –         | –             | 0                  |
| 1         | -1.9      | True          | 1                  |
| 2         | -2.4      | True          | 2                  |
| 3         | 0.1       | False         | 2                  |
| 4         | -1.7      | True          | 3                  |
| 5         | -1.7      | True          | 4                  |
| 6         | -4.2      | True          | 5                  |
| 7         | -11.9     | True          | 6                  |

*******************************************************************************

                                     {{1}}
*******************************************************************************

**Drei typische Fehler.** Was geben diese Varianten aus — und warum?

<div class="flex-container">
<div class="flex-child">

```python
minima = [-1.9, -2.4, 0.1]
for minimum in minima:
    frosttage = 0
    if minimum < 0:
        frosttage = frosttage + 1
print(frosttage)
```
@Pyodide.eval

</div>
<div class="flex-child">

```python
minima = [-1.9, -2.4, 0.1]
frosttage = 0
for minimum in minima:
    if minimum < 0:
        frosttage = frosttage + 1
    print(frosttage)
```
@Pyodide.eval

</div>
<div class="flex-child">

```python
minima = [-1.9, -2.4, 0.1]
frosttage = 0
for minimum in minima:
    if minimum < 0:
    frosttage = frosttage + 1
print(frosttage)
```
@Pyodide.eval

</div>
</div>

<details>
<summary>**Lösung**</summary>

1. Der Zähler wird in **jedem Durchlauf** auf 0 zurückgesetzt. Übrig bleibt nur das Ergebnis des letzten Tages: `0`.
2. `print` ist eine Ebene zu tief eingerückt und steht in der Schleife — es gibt einen Zwischenstand pro Tag aus: `1 2 2`.
3. Nach dem Doppelpunkt fehlt die Einrückung: `IndentationError`.

</details>

*******************************************************************************

## Die Antwort auf die Leitfrage

Die 366 Tiefsttemperaturen des Jahres 2024 liegen in unserem Repository, ein Wert pro Zeile. Statt sie abzutippen, holen wir sie direkt von dort:

```python
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
       "VL_EAVD/master/data/fichtelberg/2024_minimum.txt")
text = open_url(url).read()

frosttage = 0
for wert in text.split():
    if float(wert) < 0:
        frosttage = frosttage + 1

print("Frosttage 2024:", frosttage)
```
@Pyodide.eval

Zwei Zeilen sind neu:

* `open_url(url).read()` holt die Datei als einen einzigen langen **Text**. Wie man Dateien liest, behandeln wir ausführlich in Vorlesung 06.
* `text.split()` zerlegt diesen Text an Zeilenumbrüchen und Leerzeichen in eine Liste einzelner Texte: `"-1.9\n-2.4\n0.1"` wird zu `["-1.9", "-2.4", "0.1"]`. Aus jedem macht `float(wert)` eine Zahl — genau wie in Vorlesung 02.

> Dieselben fünf Zeilen zählen 7 oder 366 oder 47.595 Werte. Das Programm wird nicht länger, wenn die Daten mehr werden. Genau das war in der Tabellenkalkulation das Problem.

**Erweitern Sie das Programm**

1. Zählen Sie zusätzlich die Tage mit **strengem Frost** (Minimum unter -10 °C).
2. Wie viele Tage waren **frostfrei**? Lösen Sie das auf zwei Wegen: mit einem zweiten Zähler und ohne.
3. Zählen Sie die Tage, an denen das Minimum **genau** 0,0 °C war. Welcher Vergleichsoperator ist dafür nötig?

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
werte = [3, -1, 4, -1, -5]
a = 0
b = 0
for w in werte:
    if w < 0:
        a = a + 1
    else:
        b = b + w
print(a, b)
```

[[3 7]]
[[?]] `a` zählt die negativen Werte, `b` addiert die übrigen.
***
Negative Werte: -1, -1, -5 → `a = 3`. Übrige Werte: 3 + 4 → `b = 7`.
***

**Am 5. Januar 2024 lag das Maximum auf dem Fichtelberg bei genau 0,0 °C. Welche Aussagen stimmen?**

[[X]] Mit der Bedingung `maximum < 0` ist der 5. Januar **kein** Eistag.
[[ ]] Mit der Bedingung `maximum <= 0` ist der 5. Januar **kein** Eistag.
[[X]] Die Wahl zwischen `<` und `<=` ändert das Ergebnis, wenn Werte genau auf der Grenze liegen.
[[ ]] Bei Kommazahlen spielt der Unterschied zwischen `<` und `<=` keine Rolle.
***
Der DWD definiert den Eistag mit "Maximum **unter** 0 °C", also `<`. Solche Grenzfälle sind in Messdaten häufiger als man denkt, weil Werte auf eine Nachkommastelle gerundet werden.
***

**Welche Bedingung erkennt einen Frosttag, ohne dass Fehlwerte (`-999`) mitgezählt werden?**

[( )] `minimum < 0 or minimum != -999`
[(X)] `minimum < 0 and minimum != -999`
[( )] `minimum < 0 and minimum == -999`
[( )] `not minimum == -999`
***
Beide Bedingungen müssen gelten: unter 0 **und** kein Fehlwert. Mit `or` wäre jeder gemessene Wert ein Frosttag.
***

**Ordnen Sie zu: Was steht vor, in oder nach der Schleife?**

[ [vor] [in] [nach] ]
[ (X)  ( )  ( )  ] `frosttage = 0`
[ ( )  (X)  ( )  ] `if minimum < 0:`
[ ( )  (X)  ( )  ] `frosttage = frosttage + 1`
[ ( )  ( )  (X)  ] `print("Frosttage:", frosttage)`

## Nächste Woche

Das Zählmuster merkt sich eine Zahl über alle Durchläufe hinweg. In der nächsten Vorlesung merken wir uns mehr — und beantworten eine Frage, an der die Tabellenkalkulation verzweifelt:

> _Wie lang war die längste ununterbrochene Frostperiode?_

**Zur Vorbereitung**

- [ ] Schreiben Sie `frost.py` auf Ihrem Rechner mit den sieben Januarwerten und bringen Sie es zum Laufen.
- [ ] Überlegen Sie in Pseudocode: Was muss man sich merken, um die längste Frostperiode zu finden?
- [ ] Wie würden Sie den **Mittelwert** der sieben Werte mit einer Schleife berechnen?
