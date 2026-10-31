<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.3.0
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
    min-width: 400px;
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

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=3" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

--{{0}}--
Heute lernt Ihr Programm zwei Dinge, die bisher gefehlt haben: entscheiden und wiederholen. Am Ende beantworten wir damit die Frage aus Vorlesung 01, diesmal mit 366 echten Werten. Der größte Stolperstein ist die Einrückung. Sie wird Ihnen heute einige Fehlermeldungen einbringen, das ist normal und gehört zum Lernen.

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

--{{0}}--
`minimum < 0` liefert `True` oder `False`. Bisher konnte ein Programm diesen Wert nur ausgeben. Von heute an steuert er, was als Nächstes passiert. Aus Vorlesung 01 kennen Sie die drei Bausteine Folge, Verzweigung und Wiederholung. Die Folge haben Sie letzte Woche benutzt, die beiden anderen kommen heute dazu.

## Dieselben Beispiele auf Ihrem Rechner

Alle Codebeispiele laufen hier direkt im Browser. Sie sind aber **gewöhnliches Python**: In einer Datei auf Ihrem Rechner ist das Ergebnis dasselbe.

<div class="flex-container">
<div class="flex-child">

**Im Browser**

```python
minimum = -3.5
print("Minimum:", minimum)
print("Frost?", minimum < 0)
```
@Pyodide.eval

</div>
<div class="flex-child">

**Auf Ihrem Rechner**, als Datei `frost.py`:

```bash
$ python frost.py
Minimum: -3.5
Frost? True
```

</div>
</div>

> Nutzen Sie das: Jedes Beispiel dieser Vorlesung ist ein Ausgangspunkt für eigene Versuche in Visual Studio Code.

Es gibt eine einzige Ausnahme: Zeilen mit `open_url`, mit denen wir Daten aus unserem Repository, dem Ablageort der Kursdateien auf GitHub, in den Browser holen. Sie sind im Text jeweils markiert.

--{{0}}--
Das Dollarzeichen steht für die Eingabeaufforderung im Terminal und wird nicht mitgetippt. Unter macOS und Linux heißt der Befehl oft `python3`. Eine Datei können Sie speichern, verändern, erneut ausführen und weitergeben. Genau das unterscheidet ein Programm von einer Formel, die man einmal in eine Zelle tippt.

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

Ändern Sie `minimum` im Textbereich auf `2.1`. Welche Zeile wird dann nicht mehr ausgegeben?

--{{0}}--
Lesen Sie die Zeile wie einen Satz: Wenn das Minimum kleiner als null ist, dann gib Frosttag aus. Hinter dem `if` steht immer etwas, das wahr oder falsch ist, hier der Vergleich aus der letzten Vorlesung. Ist es falsch, überspringt Python den eingerückten Teil und macht danach ganz normal weiter.

### Einrückung ist Syntax

                                     {{0-1}}
*******************************************************************************

Woher weiß Python, welche Anweisungen zum `if` gehören? **An der Einrückung.** Sie gehört zur **Syntax**, also zu den Schreibregeln der Sprache. Die eingerückten Zeilen, die zusammengehören, heißen **Block**.

``` text
if minimum < 0:                 ← Doppelpunkt: jetzt kommt ein Block
    print("Frosttag!")          ← eingerückt: gehört zum if
    print("Unter null Grad.")   ← eingerückt: gehört zum if
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

> In Python **ist** die Einrückung die Struktur. Falsch eingerückter Code ist falscher Code.

*******************************************************************************

--{{0}}--
Die vier Leerzeichen sind eine Vereinbarung. Python verlangt nur, dass alle Zeilen eines Blocks gleich weit eingerückt sind.

--{{1}}--
In vielen anderen Sprachen markieren Klammern die Blöcke, die Einrückung ist dort nur Kosmetik. Python hat sich anders entschieden: Was für Menschen zusammengehörig aussieht, gehört auch für den Rechner zusammen. Beide Programme laufen übrigens fehlerfrei. Sie tun nur etwas anderes, und das meldet Python nicht.

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

--{{0}}--
`else` hat keine eigene Bedingung, es steht für alle übrigen Fälle. Es gehört immer zu einem `if` und steht auf derselben Einrückungstiefe. Ein `if` ohne `else` ist erlaubt, ein `else` ohne `if` nicht.

### Mehrere Fälle: `elif`

Der Deutsche Wetterdienst kennt feste Begriffe für besondere Tage. Anders als der Frosttag (Minimum unter 0 °C) sind diese über das **Tagesmaximum** definiert:

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

--{{0}}--
Am Frosttag fällt die Temperatur irgendwann unter null, am Eistag bleibt sie den ganzen Tag darunter. Jeder Eistag ist also auch ein Frosttag. `elif`-Zweige darf es beliebig viele geben, das `else` am Ende ist freiwillig. Ein Zweig muss auch nicht direkt etwas ausgeben. Oft merkt man sich das Ergebnis in einer Variablen, etwa `art = "Sommertag"`, und gibt es am Ende mit `print(art)` aus.

### Bedingungen verknüpfen

Manchmal hängt eine Entscheidung von mehreren Bedingungen ab:

<!-- data-type="none" -->
| Operator | Bedeutung                         | Beispiel                              |
| :------- | :-------------------------------- | :------------------------------------ |
| `and`    | beide müssen zutreffen            | `minimum < 0 and maximum > 0`         |
| `or`     | mindestens eine muss zutreffen    | `maximum >= 25 or minimum < -10`      |
| `not`    | kehrt den Wahrheitswert um        | `not minimum < 0`                     |

```python
minimum = -2.4    # 2. Januar 2024
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
minimum = -999

if minimum != -999 and minimum < 0:
    print("Frosttag")
```

Kein Programm erkennt einen Fehlwert von selbst. Sie müssen wissen, wie er im Datensatz kodiert ist — dafür steht es in der Datensatzbeschreibung.

</details>

*******************************************************************************

--{{0}}--
2024 gab es auf dem Fichtelberg 79 solcher Frost-Tau-Wechsel-Tage. `not minimum < 0` bedeutet dasselbe wie `minimum >= 0`. Python wertet zuerst `not` aus, dann `and`, zuletzt `or`. Wer unsicher ist, setzt runde Klammern.

--{{1}}--
Für Python ist `-999` eine ganz gewöhnliche Zahl, nur Sie wissen, dass sie „nicht gemessen“ bedeutet. Erinnern Sie sich an die -250,9 °C aus Vorlesung 00: Auch dort gab es keine Fehlermeldung.

## Wiederholen: `for`

Eine Prüfung für einen Wert können wir jetzt. Für 366 Werte brauchen wir eine **Schleife**.

In Python schreibt man mehrere Werte als **Liste** in eckige Klammern. Die `for`-Schleife nimmt sich dann **jeden Wert der Reihe nach** vor:

```python
# Tiefsttemperaturen vom 8. bis 14. Januar 2024
minima = [-14.1, -12.1, -11.1, -10.2, -8.3, -7.5, -6.5]

for minimum in minima:
    print("Nächster Wert:", minimum)

print("Fertig.")
```
@Pyodide.eval

Lesen Sie die Schleife als: _"Für jedes `minimum` in `minima`: führe den eingerückten Block aus."_

> Listen lernen Sie in Vorlesung 05 genauer kennen. Heute reicht: Eine Liste enthält mehrere Werte, und `for` geht sie der Reihe nach durch.

--{{0}}--
Der Name `minimum` bekommt bei jedem Durchlauf den nächsten Wert der Liste. Sie wählen ihn selbst, `for m in minima:` täte dasselbe. Wenn Sie in der Tabellenkalkulation eine Formel nach unten ziehen, wiederholen Sie auch dieselbe Anweisung für jede Zeile. Die Schleife schreibt diese Wiederholung einmal auf, statt sie in jede Zeile zu kopieren.

### Das Zählmuster

Jetzt setzen wir alles zusammen — Schleife, Bedingung und eine Variable, die mitzählt:

```` @BlocklyId(frostwoche, runner=frostwoche hideRunner height=540)
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

--{{0}}--
In der Tabellenkalkulation übernimmt `ZÄHLENWENN` das Zählen, hier machen Sie es selbst. Die Variable `frosttage` ist das Gedächtnis des Programms: Sie ist die Antwort auf die Frage aus Vorlesung 02, was man sich merken muss. In Vorlesung 04 kommen weitere solche Muster dazu.

### Der Algorithmus aus Vorlesung 01

In Vorlesung 01 haben wir das Zählen als Pseudocode aufgeschrieben. Hier steht er Zeile für Zeile in Python, wie versprochen in **fünf Zeilen**:

<!-- data-type="none" -->
| Pseudocode                       | Python                          |
| :------------------------------- | :------------------------------ |
| Setze frosttage auf 0.           | `frosttage = 0`                 |
| Für jedes Minimum in der Liste:  | `for minimum in minima:`        |
| Wenn Minimum < 0:                | `if minimum < 0:`               |
| Erhöhe frosttage um 1.           | `frosttage = frosttage + 1`     |
| Gib frosttage aus.               | `print("Frosttage:", frosttage)` |

> Wer den Pseudocode aufgeschrieben hat, hat die eigentliche Arbeit schon getan. Python verlangt nur noch die genaue Schreibweise.

--{{0}}--
Die Liste selbst kommt als sechste Zeile dazu, sie gehört aber zu den Daten, nicht zum Algorithmus. Ändert sich die Liste, bleiben die fünf Zeilen gleich. Genau deshalb lohnt sich das Aufschreiben: Der Algorithmus zählt ebenso sieben wie 366 Tage.

### Schleifen im Kopf ausführen

                                     {{0-1}}
*******************************************************************************

Wie in den letzten Vorlesungen legen wir ein **Ablaufprotokoll** an — diesmal eine Zeile pro Schleifendurchlauf:

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

1. Der Zähler wird in **jedem Durchlauf** auf 0 zurückgesetzt, die verrutschte Zeile aus Vorlesung 01, jetzt in Python. Übrig bleibt nur das Ergebnis des letzten Tages: `0`.
2. `print` ist eine Ebene zu tief eingerückt und steht in der Schleife — es gibt einen Zwischenstand pro Tag aus: `1`, `2`, `2`, je in einer eigenen Zeile.
3. Nach dem Doppelpunkt fehlt die Einrückung: `IndentationError`.

</details>

*******************************************************************************

--{{0}}--
Jede Zeile der Tabelle ist ein Durchlauf. Achten Sie auf Durchlauf 3: Die Bedingung ist falsch, der Zähler bleibt stehen, die Schleife läuft trotzdem weiter. Die erste Zeile ohne Durchlauf ist `frosttage = 0`. Sie wird genau einmal ausgeführt, vor der Schleife.

--{{1}}--
Die drei Varianten sehen fast gleich aus, jeweils steht nur eine Zeile an einer anderen Stelle. Führen Sie sie im Kopf aus, bevor Sie sie starten. Dass ein Programm durchläuft, heißt auch hier nicht, dass es die gesuchte Zahl liefert.

### Typische Fehlvorstellung: Die Schleifenvariable

> **Typische Fehlvorstellung:** _„Nach der Schleife ist die Schleifenvariable weg — oder sie steht wieder am Anfang.“_

```python
minima = [-1.9, -2.4, 0.1, -1.7]

for minimum in minima:
    print("in der Schleife:", minimum)

print("nach der Schleife:", minimum)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt die letzte Zeile aus?

[( )] eine Fehlermeldung, weil `minimum` nur in der Schleife existiert
[( )] `nach der Schleife: -1.9`
[(X)] `nach der Schleife: -1.7`
***
`minimum` ist eine ganz gewöhnliche Variable. Die Schleife weist ihr nacheinander jeden Wert der Liste zu — nach dem letzten Durchlauf bleibt der **letzte** Wert stehen. Wer nach der Schleife mit `minimum` weiterrechnet, rechnet also nur mit dem letzten Tag.
***

--{{0}}--
In einigen anderen Sprachen, etwa Java oder C, ist eine Zählvariable, die im Schleifenkopf angelegt wird, nach der Schleife tatsächlich nicht mehr bekannt. Wollen Sie einen Wert über die Schleife hinaus behalten, legen Sie dafür am besten vor der Schleife eine eigene Variable an.

### Fehlermeldungen bei `if` und `for`

Mit `if` und `for` kommen drei typische Meldungen dazu. Sie zeigen meist direkt auf die richtige Stelle, anders als der Tippfehler aus Vorlesung 02, und oft schlägt Python die Korrektur gleich mit vor.

<!-- data-type="none" -->
| Im Code                     | Meldung (letzte Zeile)                                                 | Korrektur                    |
| :-------------------------- | :--------------------------------------------------------------------- | :--------------------------- |
| `if minimum < 0`            | `SyntaxError: expected ':'`                                            | Doppelpunkt ans Zeilenende   |
| `if minimum = 0:`           | `SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?` | vergleichen mit `==`         |
| Block nicht eingerückt      | `IndentationError: expected an indented block after 'if' statement on line 4` | vier Leerzeichen einrücken   |

`:=` aus der zweiten Meldung brauchen Sie nicht, diesen Vorschlag können Sie ignorieren.

--{{0}}--
Bei einem Syntaxfehler läuft gar nichts, auch nicht die Zeilen davor: Python prüft zuerst das ganze Programm. Das ergänzt das „Zeile für Zeile“ aus Vorlesung 02. Ein `NameError` oder `TypeError` taucht dagegen erst auf, wenn die Zeile an der Reihe ist. Die Zeilen davor sind dann schon gelaufen.

### Ein Fehler nach dem anderen

> **Python meldet immer nur den ersten Fehler.** Nach jeder Korrektur erneut ausführen, bis das Programm durchläuft.

Das Programm soll die Frosttage zählen. Führen Sie es aus, korrigieren Sie die gemeldete Stelle, führen Sie es erneut aus — bis `Frosttage: 2` erscheint. Wie viele Fehler waren es?

```python
minima = [-1.9, -2.4, 0.1]
frosttage = 0
for minimum in minima
    if minimum < 0:
    frosttage = frosttage + 1
print("Frosttage:", frosttage)
```
@Pyodide.eval

<details>
<summary>**Lösung**</summary>

Zwei Fehler, gemeldet nacheinander:

1. Zeile 3: `SyntaxError: expected ':'`. Nach `for minimum in minima` fehlt der Doppelpunkt.
2. Erst nach dieser Korrektur meldet Python Zeile 5: `IndentationError: expected an indented block after 'if' statement on line 4`. `frosttage = frosttage + 1` muss eine Ebene tiefer eingerückt werden, unter das `if`.

</details>

                                    --{{0}}--
Dass nach der ersten Korrektur ein neuer Fehler erscheint, wirkt am Anfang entmutigend. Es ist aber ein Fortschritt: Python ist eine Zeile weiter gekommen. Bei längeren Programmen hilft es, nach jeder kleinen Änderung auszuführen, statt zwanzig Zeilen zu schreiben und dann alle Fehler auf einmal zu suchen.

## Die Antwort auf die Leitfrage

Die 366 Tiefsttemperaturen des Jahres 2024 liegen in unserem Repository, ein Wert pro Zeile. Statt sie abzutippen, holen wir sie direkt von dort. Quelle: Deutscher Wetterdienst, Station 01358, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

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

**127 Frosttage**, dieselbe Zahl wie mit `ZÄHLENWENN` in Vorlesung 01. Zwei unabhängige Wege, ein Ergebnis: So prüft man ein Programm.

Das Zählmuster kennen Sie. Neu sind nur die Zeilen, die die Daten holen und zerlegen. **Sie müssen sie heute nicht im Detail verstehen:** `open_url(url).read()` holt die Datei als einen langen Text, `text.split()` zerlegt ihn in einzelne Werte.

--{{0}}--
`from pyodide.http import open_url` stellt die Funktion `open_url` bereit. Die Adresse steht in runden Klammern, damit sie auf zwei Zeilen passt. `text.split()` zerlegt den Text an Zeilenumbrüchen und Leerzeichen: Aus `"-1.9\n-2.4\n0.1"` wird die Liste `["-1.9", "-2.4", "0.1"]`, dabei steht `\n` für einen Zeilenumbruch. Das sind immer noch Texte. Erst `float(wert)` macht daraus Zahlen, genau wie in Vorlesung 02. Wie man Dateien liest, behandeln wir ausführlich in Vorlesung 06.

> [!NOTE] Nur im Browser
> `pyodide.http.open_url` gibt es nur in der Python-Umgebung dieser Webseite. In Visual Studio Code auf Ihrem Rechner führt die Zeile zu einem `ModuleNotFoundError`. Dort lesen Sie die Datei direkt — wie das geht, zeigt Vorlesung 06.

> Das Zählmuster wird nicht länger, wenn die Daten mehr werden: Dieselben Zeilen zählen 7 oder 366 Werte. **Aber Vorsicht:** 2024 enthält keinen einzigen Fehlwert, deshalb stimmt die 127. Auf alle 47.595 Tage seit 1890 angewandt, käme dieselbe Bedingung auf 22.330 statt 22.320 Frosttage, denn zehn Tage stehen auf `-999`. Eine Meldung gäbe es nicht.

**Erweitern Sie das Programm**

1. Zählen Sie zusätzlich die Tage mit **strengem Frost** (Minimum unter -10 °C).
2. Wie viele Tage waren **frostfrei**? Lösen Sie das auf zwei Wegen: mit einem zweiten Zähler und ohne.
3. Zählen Sie die Tage, an denen das Minimum **genau** 0,0 °C war. Welcher Vergleichsoperator ist dafür nötig?

<details>
<summary>**Zur Kontrolle**</summary>

1. 7 Tage mit strengem Frost.
2. 239 frostfreie Tage: mit einem zweiten Zähler oder als `366 - 127`.
3. 1 Tag, geprüft mit `==`.

</details>

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
Der DWD definiert den Eistag mit "Maximum **unter** 0 °C", also `<`. 2024 lag das Maximum an 4 Tagen bei genau 0,0 °C: Mit `<` sind es 44 Eistage, mit `<=` wären es 48. Weil Werte auf eine Nachkommastelle gerundet werden, liegen sie öfter genau auf der Grenze.
***

**Welche Bedingung erkennt einen Frosttag, ohne dass Fehlwerte (`-999`) mitgezählt werden?**

[( )] `minimum < 0 or minimum != -999`
[(X)] `minimum < 0 and minimum != -999`
[( )] `minimum < 0 and minimum == -999`
[( )] `not minimum == -999`
***
Beide Bedingungen müssen gelten: unter 0 **und** kein Fehlwert. Mit `or` wäre die Bedingung für jeden Wert wahr, auch für `-999`.
***

**Ordnen Sie zu: Was steht vor, in oder nach der Schleife?**

[ [vor] [in] [nach] ]
[ (X)  ( )  ( )  ] `frosttage = 0`
[ ( )  (X)  ( )  ] `if minimum < 0:`
[ ( )  (X)  ( )  ] `frosttage = frosttage + 1`
[ ( )  ( )  (X)  ] `print("Frosttage:", frosttage)`

## Ihre Begriffe für die Kurslandkarte

Die [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) wächst mit dem Semester. Wir schlagen die Begriffe vor, Sie ergänzen, was fehlt: Aus Ihren Datenwünschen in Vorlesung 00 sind so schon die ersten Anwendungen geworden. Nehmen Sie sich dafür jetzt fünf Minuten.

**Welches Wort von heute müssten Sie jemandem aus Ihrem Semester erklären können?**

[[___ ___ ___]]

**Welche Daten aus Ihrem Fach würden Sie gern so auswerten?**

[[___ ___ ___]]

## Nächste Woche

Das Zählmuster merkt sich eine Zahl über alle Durchläufe hinweg. In der nächsten Vorlesung merken wir uns mehr — und beantworten eine Frage, an der die Tabellenkalkulation verzweifelt:

> _Wie lang war die längste ununterbrochene Frostperiode?_

**Zur Vorbereitung**

- [ ] Schreiben Sie `frost.py` auf Ihrem Rechner mit den sieben Januarwerten und bringen Sie es zum Laufen.
- [ ] Überlegen Sie in Pseudocode: Was muss man sich merken, um die längste Frostperiode zu finden?
- [ ] Wie würden Sie den **Mittelwert** der sieben Werte mit einer Schleife berechnen?

**Zur Übung**

Blatt 3 (Erdbeben einordnen) steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 16.11.
