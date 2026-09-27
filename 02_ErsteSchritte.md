<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Erste Schritte in Python: Ausgabe, Rechnen, Variablen, Datentypen und das Lesen von Fehlermeldungen — am Beispiel der Fichtelberg-Messreihe.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md)

# Erste Schritte in Python

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `Interpreter, Ausgabe, Rechnen, Variablen, Datentypen, Typumwandlung, Fehlermeldungen`                                                             |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie sage ich dem Rechner, was er tun soll?_

**Fragen an die heutige Veranstaltung ...**

* Wie wird aus einem Programmtext etwas, das der Rechner ausführt?
* Wie speichert ein Programm Werte, und wie rechnet es damit?
* Warum ist `"6,26"` etwas anderes als `6.26`?
* Was sagt mir eine Fehlermeldung — und wie gehe ich damit um?

> Alle Beispiele laufen heute direkt im Browser. Sie müssen nichts installieren.

--------------------------------------------------------------------------------

## Rückblick

    --{{0}}--
Letzte Woche haben Sie gesehen, wo die Tabellenkalkulation an ihre Grenzen kommt. Als Vorbereitung sollten Sie beschreiben, wie man den wärmsten Tag findet.

Ihre Hausaufgabe: _Den wärmsten Tag in `fichtelberg_2024.csv` finden, ohne `MAX` zu benutzen._ Eine mögliche Lösung:

``` text
Merke dir den ersten Tag als "bisher wärmster".
Für jeden weiteren Tag:
    Wenn sein Maximum höher ist als das des bisher wärmsten:
        Merke dir diesen Tag als "bisher wärmster".
Gib den bisher wärmsten Tag aus.
```

> Darin stecken schon fast alle Zutaten eines Programms: Man muss sich etwas **merken** (heute), etwas **vergleichen** und etwas **wiederholen** (nächste Woche). Heute kümmern wir uns um das Merken und Rechnen.

## Vom Text zur Ausführung

    --{{0}}--
Ein Prozessor versteht nur sehr einfache Befehle in Form von Nullen und Einsen. Irgendjemand muss unseren Programmtext also übersetzen.

Ein Prozessor versteht nur **Maschinenbefehle** — sehr einfache Anweisungen wie "lade Wert", "addiere", "springe", codiert als Bitmuster. Zwischen Ihrem Programmtext und dem Prozessor steht deshalb ein Übersetzer. Bei Python ist das der **Interpreter**:

``` ascii
  +-----------------+        +------------------+        +--------------+
  | Programmtext    |        | Python-          |        |              |
  | frost.py        |------->| Interpreter      |------->|  Prozessor   |
  |                 |        | liest Zeile für  |        |              |
  | minimum = -3.5  |        | Zeile, prüft,    |        |              |
  | print(minimum)  |        | führt aus        |        |              |
  +-----------------+        +------------------+        +--------------+
                                      |
                                      v
                             Ausgabe oder Fehlermeldung
```

Zwei Dinge sollten Sie sich merken:

1. Der Interpreter arbeitet **von oben nach unten**, eine Anweisung nach der anderen.
2. Stößt er auf etwas, das er nicht versteht, **bricht er ab** und sagt Ihnen, wo und warum.

### Warum Python?

<!-- data-type="none" -->
| Grund                                 | Was das für Sie bedeutet                                          |
| :------------------------------------ | :---------------------------------------------------------------- |
| gut lesbar                            | Programme sehen fast aus wie der Pseudocode von letzter Woche      |
| in der Wissenschaft verbreitet        | Für fast jede Fachfrage gibt es eine fertige Bibliothek            |
| eine Sprache für die ganze Kette      | Vom Mikrocontroller (Vorlesung 08) bis zur Auswertung im Notebook  |
| frei verfügbar                        | Keine Lizenzkosten, läuft auf jedem Rechner                        |

> Python ist nicht die schnellste Sprache und nicht die einzige. Für unsere Zwecke — Daten einlesen, aufbereiten, auswerten, darstellen — ist sie aber die naheliegendste.

## Die erste Anweisung

    --{{0}}--
Beginnen wir mit der einfachsten Anweisung überhaupt: etwas auf den Bildschirm schreiben.

Die Anweisung `print` gibt etwas aus. Was ausgegeben werden soll, steht in runden Klammern. Text steht in Anführungszeichen.

> Nutzen Sie die Schaltflächen über dem Editor, um zwischen **Blöcken** und **Text** zu wechseln. Beide zeigen dasselbe Programm.

```` @BlocklyId(hallo, runner=hallo hideRunner height=240)
print("Hallo Fichtelberg!")
print("Höhe der Station in Metern:")
print(1213)
````

```python
# runner: hallo
```
@Pyodide.eval

**Ausprobieren**

* Ergänzen Sie eine Zeile, die das Jahr des Messbeginns (1890) ausgibt.
* Was passiert, wenn Sie bei `"Hallo Fichtelberg!"` ein Anführungszeichen weglassen?
* `print` kann mehrere Dinge auf einmal ausgeben, getrennt durch Kommas: `print("Höhe:", 1213, "m")`

## Rechnen

    --{{0}}--
Python ist auch ein ziemlich guter Taschenrechner. Die Rechenzeichen sind die, die Sie erwarten, mit ein paar Ergänzungen.

<!-- data-type="none" -->
| Operator | Bedeutung             | Beispiel   | Ergebnis |
| :------: | :-------------------- | :--------- | :------- |
| `+`      | Addition              | `3 + 4`    | `7`      |
| `-`      | Subtraktion           | `3 - 4`    | `-1`     |
| `*`      | Multiplikation        | `3 * 4`    | `12`     |
| `/`      | Division              | `7 / 2`    | `3.5`    |
| `//`     | ganzzahlige Division  | `7 // 2`   | `3`      |
| `%`      | Rest der Division     | `7 % 2`    | `1`      |
| `**`     | Potenz                | `2 ** 10`  | `1024`   |

Es gilt Punkt- vor Strichrechnung, Klammern gehen vor.

```python
print(3 + 4 * 2)
print((3 + 4) * 2)
print(7 / 2)
print(7 // 2)
print(18900801 // 10000)
```
@Pyodide.eval

> Die letzte Zeile ist kein Zufall: Das DWD-Datum `18900801` ganzzahlig durch `10000` geteilt ergibt das Jahr. Genau diesen Trick nutzt die Vier-Zeilen-Lösung aus der letzten Vorlesung.

                                     {{1}}
*******************************************************************************

> [!WARNING]
> **Dezimalpunkt, nicht Dezimalkomma!** Python ist eine englischsprachige Sprache. `6.26` ist eine Zahl. `6,26` ist etwas völlig anderes:

```python
print(6.26 + 1)
print(6,26 + 1)
```
@Pyodide.eval

Die zweite Zeile gibt `6 27` aus. Python hat zwei Werte gesehen — `6` und `26 + 1` — und beide ausgegeben. **Keine Fehlermeldung, aber ein falsches Ergebnis.** Das ist die gefährlichste Art von Fehler.

*******************************************************************************

## Variablen

    --{{0}}--
Um sich etwas zu merken, braucht ein Programm Variablen. Eine Variable ist ein Name für einen Wert.

Eine **Variable** ist ein Name, unter dem sich ein Programm einen Wert merkt.

```` @BlocklyId(variablen, runner=variablen hideRunner height=300)
tagesmittel = 6.26
minimum = -14.1
maximum = 26.9

spanne = maximum - minimum
print("Temperaturspanne 2024:", spanne)
````

```python
# runner: variablen
```
@Pyodide.eval

### Das Gleichheitszeichen ist keine Gleichung

                                     {{0-1}}
*******************************************************************************

In der Mathematik ist `x = x + 1` ein Widerspruch. In Python ist es eine ganz normale Anweisung:

```python
zaehler = 0
zaehler = zaehler + 1
zaehler = zaehler + 1
print(zaehler)
```
@Pyodide.eval

> **Lesen Sie `=` als "wird zu".** Rechts wird zuerst ausgerechnet, dann wird das Ergebnis unter dem Namen links abgelegt. Der alte Wert ist danach weg.

*******************************************************************************

                                     {{1}}
*******************************************************************************

**Programme im Kopf ausführen**

Die wichtigste Fähigkeit dieses Kurses — und eine typische Klausuraufgabe — ist, ein Programm Zeile für Zeile im Kopf nachzuvollziehen. Dazu legt man eine Tabelle an, eine Spalte pro Variable:

```python
a = 5
b = a * 2
a = a + b
b = b - 1
print(a, b)
```

<!-- data-type="none" -->
| nach Zeile | `a`  | `b`  |
| :--------- | :--- | :--- |
| 1          | 5    | –    |
| 2          | 5    | 10   |
| 3          | 15   | 10   |
| 4          | 15   | 9    |

Die Ausgabe lautet also `15 9`.

*******************************************************************************

### Namen wählen

Ein Variablenname

* besteht aus Buchstaben, Ziffern und dem Unterstrich `_`,
* beginnt **nicht** mit einer Ziffer,
* unterscheidet Groß- und Kleinschreibung: `Minimum` und `minimum` sind zwei verschiedene Variablen,
* darf kein reserviertes Wort wie `if`, `for`, `print` oder `True` sein.

<!-- data-type="none" -->
| Name            | erlaubt? | gut?                                                     |
| :-------------- | :------: | :------------------------------------------------------- |
| `tagesmittel`   | ja       | ja — sagt, was drin ist                                  |
| `t`             | ja       | nur für ganz kurze Rechnungen                            |
| `max_temp_2024` | ja       | ja — Wörter trennt man mit `_`                           |
| `2024_max`      | **nein** | beginnt mit einer Ziffer                                 |
| `höhe`          | ja       | besser `hoehe` — Umlaute machen früher oder später Ärger |

> Ein guter Name spart einen Kommentar. `x = 1213` erklärt nichts, `stationshoehe_m = 1213` alles.

## Datentypen

    --{{0}}--
Jeder Wert in Python hat einen Typ. Der Typ bestimmt, was man mit dem Wert tun kann.

Jeder Wert hat einen **Datentyp**. Der Typ entscheidet, was man mit dem Wert tun kann.

<!-- data-type="none" -->
| Typ     | Bedeutung                    | Beispiel aus unserem Datensatz |
| :------ | :--------------------------- | :----------------------------- |
| `int`   | ganze Zahl                   | `1358` (Stations-ID)           |
| `float` | Kommazahl                    | `-14.1` (Minimum in °C)        |
| `str`   | Text (Zeichenkette)          | `"Fichtelberg"`                |
| `bool`  | Wahrheitswert                | `True` (war es ein Frosttag?)  |

Mit `type(...)` können Sie jeden Wert nach seinem Typ fragen:

```python
print(type(1358))
print(type(-14.1))
print(type("Fichtelberg"))
print(type(-14.1 < 0))
print(type("18900801"))
```
@Pyodide.eval

### Text ist nicht Zahl

                                     {{0-1}}
*******************************************************************************

Wenn Sie eine Datei einlesen (Vorlesung 06), bekommen Sie immer **Text**. Auch wenn er aussieht wie eine Zahl:

```python
minimum_aus_datei = "-14.1"
print(minimum_aus_datei + 1)
```
@Pyodide.eval

Python weigert sich — zu Recht. Was soll `"-14.1" + 1` sein?

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Lösung ist eine **Typumwandlung**:

<!-- data-type="none" -->
| Umwandlung    | Beispiel           | Ergebnis     |
| :------------ | :----------------- | :----------- |
| `float(...)`  | `float("-14.1")`   | `-14.1`      |
| `int(...)`    | `int("1890")`      | `1890`       |
| `str(...)`    | `str(1213)`        | `"1213"`     |
| `int(...)`    | `int(6.9)`         | `6` — schneidet ab, rundet nicht! |

```python
minimum_aus_datei = "-14.1"
minimum = float(minimum_aus_datei)
print(minimum + 1)

wert_aus_tabelle = "6,26"
print(float(wert_aus_tabelle))
```
@Pyodide.eval

Die letzte Zeile scheitert. Ändern Sie sie so, dass sie funktioniert.

> **Tipp:** Texte haben eine Methode `replace`: `"a,b".replace(",", ".")` ergibt `"a.b"`.

<details>
<summary>**Lösung**</summary>

```python
print(float(wert_aus_tabelle.replace(",", ".")))
```

Solche Reparaturen gehören zum Alltag der Datenaufbereitung. Sie werden uns noch oft begegnen.

</details>

*******************************************************************************

### Mit Text arbeiten

Texte kann man zusammensetzen, nach ihrer Länge fragen und Teile herausschneiden:

```python
station = "Fichtelberg"
print("Station " + station)
print(len(station))

datum = "18900801"
jahr = datum[0:4]
monat = datum[4:6]
print(jahr, monat)
```
@Pyodide.eval

> `datum[0:4]` bedeutet: die Zeichen ab Position 0 bis **vor** Position 4. Python beginnt beim Zählen immer bei **0**.

### Vergleiche

Vergleiche liefern einen Wahrheitswert — `True` oder `False`:

<!-- data-type="none" -->
| Operator | Bedeutung            | Beispiel       | Ergebnis |
| :------: | :------------------- | :------------- | :------- |
| `<`      | kleiner              | `-14.1 < 0`    | `True`   |
| `>`      | größer               | `-14.1 > 0`    | `False`  |
| `<=`     | kleiner oder gleich  | `0 <= 0`       | `True`   |
| `==`     | gleich               | `-999 == -999` | `True`   |
| `!=`     | ungleich             | `5.2 != -999`  | `True`   |

```python
minimum = -3.5
frosttag = minimum < 0
print("Frosttag?", frosttag)
```
@Pyodide.eval

> Achtung: `=` weist zu, `==` vergleicht. Die Verwechslung ist einer der häufigsten Anfängerfehler.
>
> Mit diesen Wahrheitswerten trifft ein Programm **Entscheidungen** — darum geht es in der nächsten Vorlesung.

## Kommentare

Alles hinter einem `#` ignoriert der Interpreter. Kommentare sind für Menschen:

```python
fehlwert = -999      # So kennzeichnet der DWD "nicht gemessen"
minimum = -999

# Ein Fehlwert ist kein Frost, auch wenn -999 < 0 ist!
print(minimum < 0)
```
@Pyodide.eval

> Gute Kommentare erklären, **warum** etwas so ist — nicht **was** dasteht. `zaehler = zaehler + 1  # erhöhe zaehler um 1` hilft niemandem.

## Fehlermeldungen lesen

    --{{0}}--
Fehlermeldungen sind kein Zeichen von Versagen. Sie sind die Art, wie der Interpreter mit Ihnen spricht. Wer sie lesen kann, hilft sich selbst.

Fehler sind normal — auch nach Jahren der Programmiererfahrung. Entscheidend ist, die Meldung zu **lesen**, statt sie wegzuklicken.

```python
stationshoehe = 1213
print("Die Station liegt auf", stationshoe, "m Höhe")
```
@Pyodide.eval

Eine Python-Fehlermeldung lesen Sie **von unten nach oben**:

``` text
Traceback (most recent call last):
  File "<exec>", line 2, in <module>          ← wo: Zeile 2
NameError: name 'stationshoe' is not defined  ← was: diesen Namen gibt es nicht
```

Die häufigsten Fehler am Anfang:

<!-- data-type="none" -->
| Fehler         | Bedeutung                                        | typische Ursache                          |
| :------------- | :----------------------------------------------- | :---------------------------------------- |
| `SyntaxError`  | Der Text ist kein gültiges Python                | Klammer oder Anführungszeichen vergessen  |
| `NameError`    | Diesen Namen kennt Python nicht                  | Tippfehler, Variable noch nicht angelegt  |
| `TypeError`    | Diese Operation passt nicht zu diesem Typ        | `"-14.1" + 1`                             |
| `ValueError`   | Der Typ stimmt, der Wert aber nicht              | `float("6,26")`                           |

> **Und dann?** Lesen, Zeile anschauen, Hypothese bilden, ändern, erneut ausführen. Hilft das nicht: die letzte Zeile der Meldung in eine Suchmaschine kopieren. Sie sind garantiert nicht die erste Person mit diesem Fehler.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
x = 4
y = x + 3
x = y * 2
y = x - y
print(x, y)
```

[[14 7]]
[[?]] Legen Sie eine Tabelle mit einer Spalte für `x` und einer für `y` an.
***
| nach Zeile | `x` | `y` |
| :--------- | :-- | :-- |
| 1          | 4   | –   |
| 2          | 4   | 7   |
| 3          | 14  | 7   |
| 4          | 14  | 7   |

In Zeile 4 wird `y` zu `14 - 7 = 7` — der Wert bleibt also zufällig gleich.
***

**Welchen Typ haben die folgenden Werte?**

[ [int] [float] [str] [bool] ]
[ (X)   ( )     ( )   ( )    ] `1890`
[ ( )   (X)     ( )   ( )    ] `-0.5`
[ ( )   ( )     (X)   ( )    ] `"-0.5"`
[ ( )   ( )     ( )   (X)    ] `-0.5 < 0`
[ ( )   (X)     ( )   ( )    ] `7 / 7`
[ (X)   ( )     ( )   ( )    ] `18900801 // 10000`

**Welche Fehlermeldung erzeugt `print("Frosttage: " + 127)`?**

[( )] `SyntaxError`
[( )] `NameError`
[(X)] `TypeError`
[( )] `ValueError`
***
Text und Zahl lassen sich nicht mit `+` verbinden. Richtig wäre `print("Frosttage: " + str(127))` oder einfacher `print("Frosttage:", 127)`.
***

**Finden Sie alle Fehler.**

```python
Tagesmittel = 6.26
spanne = 26,9 - -14.1
print("Mittel:" tagesmittel)
```

[[X]] Zeile 2: `26,9` muss `26.9` heißen
[[X]] Zeile 3: Zwischen `"Mittel:"` und dem Namen fehlt ein Komma
[[X]] Zeile 3: `tagesmittel` ist klein geschrieben, angelegt wurde `Tagesmittel`
[[ ]] Zeile 2: `- -14.1` ist nicht erlaubt
***
`- -14.1` ist korrekt und bedeutet "minus minus 14,1", also plus 14,1. Der Fehler in Zeile 2 erzeugt übrigens **keine** Fehlermeldung — `spanne` wird einfach ein Paar aus zwei Werten.
***

## Nächste Woche

Ab der nächsten Vorlesung arbeiten wir zusätzlich mit Python auf Ihrem eigenen Rechner.

**Zur Vorbereitung**

- [ ] Installieren Sie Python (mindestens Version 3.12) von [python.org](https://www.python.org/downloads/).
- [ ] Installieren Sie den Editor [Visual Studio Code](https://code.visualstudio.com/) mit der Erweiterung _Python_.
- [ ] Schreiben Sie eine Datei `hallo.py` mit einer `print`-Anweisung und führen Sie sie aus.
- [ ] Probieren Sie: Wie rechnet man in Python eine Temperatur von °C in °F um? ($F = C \cdot 1{,}8 + 32$)

> Wenn die Installation nicht klappt: Bringen Sie Ihren Laptop in die Übung mit. Dort helfen wir.
