<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.3.0
language: de
narrator: Deutsch Female

comment:  Daten sammeln: Listen anlegen, füllen, indizieren und durchlaufen — bis zum wärmsten Tag jedes Jahres.

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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md)

# Daten sammeln

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `Listen anlegen und füllen, append, len/min/max/sorted, Funktion und Methode, Index und Slices, range, parallele Listen, verschachtelte Schleife, Text vs. Zahl, Dictionary (Ausblick)` |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Welches war auf dem Fichtelberg der wärmste Tag jedes Jahres?_

**Fragen an die heutige Veranstaltung ...**

* Wie legt man eine Liste an und füllt sie Schritt für Schritt?
* Wie greift man auf einzelne Werte und ganze Bereiche zu?
* Wie hält man zusammengehörige Werte — Datum und Temperatur — beisammen?
* Wie sammelt man ein Ergebnis pro Jahr?

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=5" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

--{{0}}--
Bisher hat sich ein Programm immer genau einen Wert gemerkt. Heute lernt es, beliebig viele Werte aufzubewahren: in einer Liste. Damit beantworten wir am Ende eine Frage mit zehn Antworten, eine pro Jahr. Der wärmste Tag 2024 ist übrigens ein alter Bekannter: Es ist der 13. August aus Ihrer Hausaufgabe zu Vorlesung 02.

--------------------------------------------------------------------------------

## Rückblick und Ziel

Bisher haben wir Listen nur **benutzt**: als fertige Werte im Programm oder als Ergebnis von `text.split()`. Und wir haben uns in einer Schleife immer nur **einen** Wert gemerkt — einen Zähler, eine Summe, den bisher kältesten Tag.

Die Leitfrage verlangt mehr: **ein Ergebnis pro Jahr**. Dafür müssen wir Ergebnisse **sammeln**, das Ergebnis ist dann selbst eine Liste.

![Drei Felder mit Klötzchen. Links unter „Bisher (VL 03, 04)“: sieben Tiefsttemperaturen ergeben einen Wert, 6 Frosttage. Rechts unter der gemeinsamen Überschrift „Heute (VL 05): Listen als Ergebnis“ zwei Felder: „Werte entnehmen“, aus denselben sieben Werten werden die sechs Frostwerte als neue Liste ausgewählt, und „Ein Ergebnis pro Jahr“, Werte der Jahre 2015, 2016 und 2017 ergeben, je Jahr farbig gruppiert, die Liste der Jahreshöchstwerte 28,1, 24,8 und 26,8 °C.](images/05_DatenSammeln/eingabe_ausgabe.svg)<!-- style="max-height: 30vh;" -->

<!-- data-type="none" -->
| Muster     | vor der Schleife     | in der Schleife                  |
| :--------- | :------------------- | :------------------------------- |
| Zählen     | `frosttage = 0`      | `frosttage = frosttage + 1`      |
| Sammeln    | `frostwerte = []`    | `frostwerte.append(minimum)`     |

```python
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]

frostwerte = []
for minimum in minima:
    if minimum < 0:
        frostwerte.append(minimum)

print("Frostwerte:", frostwerte)
print("Anzahl:", len(frostwerte))
```
@Pyodide.eval

--{{0}}--
`text.split()` aus Vorlesung 03 hat uns schon eine Liste geliefert, wir haben sie nur nicht so genannt.

> [!TIP]
> Neu heute: Listen selbst **anlegen** (`frostwerte = []`) und **füllen** (`frostwerte.append(minimum)`).

> `len(frostwerte)` liefert die Anzahl — das Zählmuster ist im Sammelmuster also schon enthalten.

--{{0}}--
`append` heißt „anhängen“: Der neue Wert kommt ans Ende der Liste. Die leere Liste `[]` vor der Schleife ist der Startwert, so wie die 0 beim Zählen. Und `len` zählt am Ende, was hineingekommen ist.

## Grundlegende Operationen

> [!TIP]
> Mit Listen macht man immer wieder dasselbe. Python hat dafür fertige Werkzeuge:
>
> + **Zusammenfassen:** Wie viele Werte, welcher ist der kleinste? → `len`, `min`, `max`, `sum`
> + **Sortieren:** → `sorted`, `sort`
> + **Prüfen, ob ein Wert enthalten ist:** → `in`
> + **Einen Wert an einer Stelle holen:** → Index, etwa `minima[0]`

--{{0}}--
Vieles davon haben Sie in Vorlesung 04 mit Schleifen selbst programmiert, etwa den kältesten Tag mit dem Extremwertmuster. `min(minima)` erledigt das in einer Zeile. Die Muster bleiben trotzdem wichtig: Sobald eine Bedingung dazukommt, etwa „der kälteste Tag im Januar“, hilft kein fertiges Werkzeug mehr.


### Funktionen und Methoden für Listen

Es gibt zwei Schreibweisen: Eine **Funktion** bekommt die Liste in Klammern und liefert ein Ergebnis, die Liste bleibt, wie sie ist. Eine **Methode** steht mit Punkt hinter der Liste. `append` und `sort` verändern die Liste selbst und liefern **nichts** zurück: `None`, Pythons Wert für „nichts“.

<!-- data-type="none" -->
| Art       | Schreibweise                    | Beispiel             | liefert                    | `minima` danach  |
| :-------- | :------------------------------ | :------------------- | :------------------------- | :--------------- |
| Funktion  | `len(liste)`                    | `len(minima)`        | `7`                        | unverändert      |
| Funktion  | `min(liste)`, `max`, `sum`      | `min(minima)`        | `-11.9`                    | unverändert      |
| Funktion  | `sorted(liste)`                 | `sorted(minima)`     | eine neue, sortierte Liste | unverändert      |
| Operator  | `wert in liste`                 | `-4.2 in minima`     | `True`                     | unverändert      |
| Methode   | `liste.append(wert)`            | `minima.append(3.5)` | `None`                     | ein Wert mehr    |
| Methode   | `liste.sort()`                  | `minima.sort()`      | `None`                     | sortiert         |

```python
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]

print(len(minima), min(minima), max(minima), sum(minima))
print(sorted(minima))
print(minima)
print(-4.2 in minima)
```
@Pyodide.eval

--{{0}}--
Methoden kennen Sie schon von Texten: `"a,b".replace(",", ".")` aus Vorlesung 02. Textmethoden liefern allerdings einen **neuen** Text, denn ein Text lässt sich nicht verändern. Eine Liste lässt sich verändern, deshalb bauen `append` und `sort` sie selbst um und liefern `None`. Nicht jede Listenmethode liefert `None`: `minima.pop()` entfernt den letzten Wert **und** gibt ihn zurück. `in` ist weder Funktion noch Methode, sondern ein Operator wie `<` oder `+`. `min` und `max` liefern übrigens den Wert, nicht seine Position in der Liste. Wann man die Position braucht, zeigt der Abschnitt „Zusammengehörige Werte“.

### Zugriff über den Index

Jeder Wert einer Liste hat eine Position, den **Index**. Gezählt wird ab 0, `minima[0]` kennen Sie schon aus Vorlesung 04:

``` text
minima  =  [ -1.9,  -2.4,   0.1,  -1.7,  -1.7,  -4.2, -11.9 ]
Index         0      1      2      3      4      5      6
von hinten   -7     -6     -5     -4     -3     -2     -1
```

```python
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]

print(minima[0])      # erster Wert
print(minima[-1])     # letzter Wert
print(minima[2:5])    # Index 2, 3 und 4
print(minima[:3])     # die ersten drei
```
@Pyodide.eval

> Das kennen Sie schon: `datum[0:4]` aus Vorlesung 02 funktioniert bei Texten genauso. Auch dort ist der Endindex **nicht** enthalten.

                                     {{1}}
*******************************************************************************

**Einzelne Werte ändern**

Über den Index kann man einen Wert auch ersetzen — etwa einen Fehlwert:

```python
minima = [-1.9, -999, 0.1, -1.7]
minima[1] = -2.4
print(minima)
print(minima[4])
```
@Pyodide.eval

Die letzte Zeile scheitert mit `IndexError`: Eine Liste mit vier Werten hat die Indizes 0 bis 3. Das ist der häufigste Fehler im Umgang mit Listen.

*******************************************************************************

--{{0}}--
Negative Indizes zählen von hinten, `minima[-1]` ist immer der letzte Wert, egal wie lang die Liste ist. In vielen anderen Programmiersprachen und in der Bibliothek NumPy heißt eine solche Folge von Werten ein Array. Arrays sehen aus wie Listen, verhalten sich beim Rechnen aber anders, mehr dazu in Vorlesung 10.

--{{1}}--
Ersetzen sollte man einen Fehlwert nur, wenn man den richtigen Wert aus einer anderen Quelle kennt, etwa aus einem Protokoll. Hier ist `-2.4` der echte Wert vom 2. Januar, den wir aus der Liste oben kennen. Sonst lässt man ihn aus, wie beim Mittelwert in Vorlesung 04.

## Zahlenfolgen mit `range`

`range` erzeugt eine Folge ganzer Zahlen:

<!-- data-type="none" -->
| Aufruf              | erzeugt                       |
| :------------------ | :---------------------------- |
| `range(5)`          | 0, 1, 2, 3, 4                 |
| `range(2015, 2025)` | 2015, 2016, ..., 2024         |
| `range(0, 366, 7)`  | 0, 7, 14, ..., 364            |

Auch hier ist der Endwert **nicht** enthalten. Das passt genau zum Index: `range(len(minima))` liefert alle Indizes einer Liste von vorn gezählt, 0 bis `len(minima) - 1`.

```python
minima = [-1.9, -2.4, 0.1, -1.7]

for i in range(len(minima)):
    print("Index", i, "Wert", minima[i])
```
@Pyodide.eval

> Wozu der Umweg über den Index, wenn `for minimum in minima` einfacher ist? Weil man manchmal **zwei Listen gleichzeitig** durchlaufen muss.

--{{0}}--
`range(len(minima))` ist die übliche Art, über die Positionen einer Liste zu laufen. Mit dem Index `i` kommt man an den Wert `minima[i]` und an jeden anderen Wert derselben Position, auch in einer zweiten Liste.

> **Typische Fehlvorstellung:** _„`range(2015, 2025)` erzeugt die Liste aller Jahre von 2015 bis 2025.“_

```python
jahre = range(2015, 2025)
print(jahre)
print(list(jahre))
print(len(jahre), 2025 in jahre)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt `print(jahre)` aus?

[(X)] `range(2015, 2025)`
[( )] `[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]`
[( )] `[2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]`
***
Zwei Fehlvorstellungen auf einmal:

* `range` ist **keine Liste**, sondern ein eigener Datentyp. Er erzeugt die Zahlen erst, wenn man sie braucht — deshalb gibt `print(jahre)` nur `range(2015, 2025)` aus. Eine echte Liste entsteht mit `list(...)`.
* Der Endwert **2025 ist nicht enthalten**. Wer die Jahre 2015 bis 2025 will, schreibt `range(2015, 2026)`.
***

--{{0}}--
`2025 in jahre` fragt, ob ein Wert enthalten ist, und liefert `True` oder `False`. Dasselbe `in` kennen Sie aus der `for`-Schleife, dort bedeutet es „für jeden Wert in“.

## Typische Fehlvorstellung: Index oder Wert?

> **Typische Fehlvorstellung:** _„In der Schleife ist `minimum` die Position des Werts, also schreibe ich `minima[minimum]`.“_

```python
minima = [-1.9, -2.4, 0.1, -1.7]

for minimum in minima:
    print(minima[minimum])
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert?

[( )] Es gibt die vier Werte aus: `-1.9`, `-2.4`, `0.1`, `-1.7`.
[( )] Es gibt die Positionen aus: `0`, `1`, `2`, `3`.
[(X)] Es bricht mit einer Fehlermeldung ab.
***
`TypeError: list indices must be integers or slices, not float`. Die Schleife `for minimum in minima` liefert die **Werte**, nicht ihre Positionen. Im ersten Durchlauf heißt die Zeile also `minima[-1.9]`, und eine Kommazahl ist kein Index.

Den Wert haben Sie schon: `print(minimum)` genügt. Die Positionen brauchen Sie nur, wenn Sie über denselben Index an eine zweite Liste wollen. Dafür gibt es `for i in range(len(minima)):` aus dem Abschnitt davor, dann ist `i` die Position und `minima[i]` der Wert.
***

                                     {{1}}
*******************************************************************************

<!-- style="max-width: 760px; display: block; margin: auto" -->
```ascii
              +--------+--------+--------+--------+
   Wert       |  −1.9  |  −2.4  |   0.1  |  −1.7  |  <--- for minimum in minima
              +--------+--------+--------+--------+
   Position       0        1        2        3       <--- for i in range(len(minima))
```

*******************************************************************************

--{{0}}--
Hier hilft die Fehlermeldung, weil die Temperaturen Kommazahlen sind. Gefährlicher wird es bei ganzen Zahlen, etwa Frosttagen pro Monat: Bei `werte = [2, 0, 1]` gibt `print(werte[wert])` ohne Fehler `1`, `2`, `0` aus, also Werte von den falschen Positionen. Fragen Sie sich deshalb bei jeder eckigen Klammer: Steht darin eine Position oder ein Messwert?

## Typische Fehlvorstellung: Nur Zahlen in einer Liste?

> **Typische Fehlvorstellung:** _„In eine Liste gehören nur Zahlen.“_

```python
tag = ["2024-08-13", 26.9]
print(tag[0], tag[1] + 1)
print(max(tag))
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert?

[( )] Schon die erste Zeile scheitert: Text und Zahl passen nicht in eine Liste.
[(X)] Die zweite Zeile gibt `2024-08-13 27.9` aus, die dritte bricht mit einer Fehlermeldung ab.
[( )] Alle Zeilen laufen, `max` liefert `26.9`.
***
Eine Liste nimmt **jeden** Wert auf: Zahlen, Texte, auch gemischt. Jeder Wert behält dabei seinen Typ, `tag[1] + 1` rechnet also ganz normal. Erst `max` scheitert: `TypeError: '>' not supported between instances of 'float' and 'str'`. Einen Text und eine Zahl kann Python nicht der Größe nach vergleichen. Dasselbe gilt für `sorted`, und `sum` scheitert schon am Addieren von Zahl und Text.
***

--{{0}}--
Aus der Tabellenkalkulation kennen Sie Spalten, in denen nur ein Typ steht. Python-Listen sind da großzügiger, Sie haben es schon bei `text.split()` gesehen: Dort entsteht eine Liste aus Texten. Erst die Bibliothek NumPy in Vorlesung 10 legt alle Werte auf einen Typ fest. Man könnte Datum und Temperatur eines Tages also in eine Liste packen. Für die Leitfrage nehmen wir trotzdem zwei Listen, eine pro Spalte: Dann bleiben `max` und `sorted` auf den Temperaturen möglich.

## Zusammengehörige Werte

Für die Leitfrage brauchen wir zu jeder Temperatur das **Datum**. Wir halten beides in zwei Listen gleicher Länge — Index `i` gehört in beiden Listen zum selben Tag:

``` text
datumswerte = [ "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14" ]
maxima      = [   22.5,         25.0,         26.9,         23.9       ]
                  i = 0         i = 1         i = 2         i = 3
```

```python
datumswerte = ["2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14"]
maxima      = [22.5, 25.0, 26.9, 23.9]

bester = 0
for i in range(len(maxima)):
    if maxima[i] > maxima[bester]:
        bester = i

print("Wärmster Tag:", datumswerte[bester], "mit", maxima[bester], "°C")
```
@Pyodide.eval

> Statt Wert **und** Datum merken wir uns nur den **Index** des bisher wärmsten Tages. Über ihn kommen wir an beides.

**Zur Vorbereitungsaufgabe aus Vorlesung 04:** Frost-Tau-Wechsel sprengen Gestein und Beton (Vorlesung 03). Um sie zu zählen, brauchen Sie Minimum **und** Maximum desselben Tages, also `minima[i]` und `maxima[i]` mit demselben `i`. Zur Kontrolle: 2024 waren es 79.

> **Schon Erfahrung?** Eine KI schlägt hier gern `max(zip(datumswerte, maxima))` vor. Probieren Sie es aus: Das Ergebnis ist `('2024-08-14', 23.9)`. Warum? Und wie bekommen Sie mit `enumerate(maxima)` Index und Wert gleichzeitig?

--{{0}}--
Die vier Werte sind echt: das Tagesmaximum vom 11. bis 14. August 2024. Der 13. August ist der wärmste Tag des Jahres, den Sie in Vorlesung 02 gesucht haben. Zur Frage für Erfahrene: `zip` bildet Paare aus Datum und Temperatur, und `max` vergleicht Paare zuerst nach dem ersten Wert, also nach dem Datum. Es liefert den spätesten Tag, ohne Fehlermeldung.

## Üben: Fehler finden bei Listen

**⏱ 7 Minuten, zu zweit.** Alle sechs Programme sollen `Frostwerte: [-1.9, -2.4, -1.7]` ausgeben. Vier melden einen Fehler, zwei laufen ohne Meldung falsch. Lesen Sie bei den Meldungen genau, welche Zeile und welches Wort Python nennt.

> Beginnen Sie mit 1, 2 und 5. Solche Fehlersuchen kommen auch in der Klausur vor.

**1.**

```python
minima = [-1.9, -2.4, 0.1, -1.7]
for minimum in minima:
    frostwerte = []
    if minimum < 0:
        frostwerte.append(minimum)
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

**2.**

```python
minima = [-1.9, -2.4 0.1, -1.7]
frostwerte = []
for minimum in minima:
    if minimum < 0:
        frostwerte.append(minimum)
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

**3.**

```python
minima = [-1.9, -2.4, 0.1, -1.7]
frostwerte = []
for minimum in minima:
    if minimum < 0:
        frostwerte.append(minima)
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

**4.**

```python
minima = [-1.9, -2.4, 0.1, -1.7]
frostwerte = []
for minimum in minima:
    if minimum < 0:
        frostwerte = frostwerte.append(minimum)
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

**5.**

```python
minima = [-1.9, -2.4, 0.1, -1.7]
frostwerte = []
for i in range(len(minima) + 1):
    if minima[i] < 0:
        frostwerte.append(minima[i])
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

**6.**

```python
minima = [-1.9, -2.4, 0.1, -1.7]
frostwerte = []
for minimum in minima:
    if minimum < 0:
        frostwerte.append[minimum]
print("Frostwerte:", frostwerte)
```
@Pyodide.eval

<details>
<summary>**Lösung**</summary>

1. Ausgabe `Frostwerte: [-1.7]`: `frostwerte = []` steht **in** der Schleife und leert die Liste bei jedem Durchlauf. Übrig bleibt der letzte Frostwert. Startwerte gehören vor die Schleife.
2. `SyntaxError: invalid syntax. Perhaps you forgot a comma?`: Zwischen `-2.4` und `0.1` fehlt das Komma. Python rät hier sogar richtig.
3. Ausgabe mit dreimal der ganzen Liste: `append(minima)` hängt die ganze Liste an, nicht den einzelnen Wert `minimum`. Derselbe Namensfehler wie in Vorlesung 03.
4. `AttributeError: 'NoneType' object has no attribute 'append'`: `append` verändert die Liste und gibt **nichts** zurück (`None`). Wer das Ergebnis zuweist, hat danach keine Liste mehr. Richtig ist nur `frostwerte.append(minimum)`.
5. `IndexError: list index out of range`: `range(len(minima) + 1)` läuft bis Index 4, die Liste hat nur die Indizes 0 bis 3.
6. `TypeError: 'builtin_function_or_method' object is not subscriptable`: Eckige statt runder Klammern. `append` ist eine Methode und wird wie jede Funktion mit `(...)` aufgerufen, `[...]` ist der Zugriff über den Index.

</details>

--{{0}}--
Die Programme 1 und 3 sind die gefährlichen: Sie laufen durch und liefern eine Liste, die nur auf den zweiten Blick falsch ist. Programm 4 ist ein Klassiker, auch in Code von einer KI: `append` sieht aus wie eine Rechnung, die ein Ergebnis liefert, verändert aber die Liste selbst. Die Meldung erscheint erst beim zweiten Frostwert, weil `frostwerte` nach dem ersten Durchlauf `None` ist.

## Ein Ergebnis pro Jahr

> [!NOTE] ❓ Aufgabe
>
> _Welches war auf dem Fichtelberg der wärmste Tag jedes Jahres von 2015 bis 2024?_
>
> Gesucht ist für jedes Jahr das Datum und die Temperatur, also zehn Ergebnisse.

Für die Jahre 2015 bis 2024 liegen Datum und Tagesmaximum als zwei Dateien im Repository — 3.653 Tage, ein Wert pro Zeile, wie in Vorlesung 03. Quelle: Deutscher Wetterdienst, Station 01358, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Zur Erinnerung: So liefert der DWD die Daten (Vorlesung 01). Wir brauchen daraus nur zwei Spalten, `MESS_DATUM` und `TXK`, das Tagesmaximum (`…` = Spalten ausgelassen):

```text produkt_klima_tag_18900801_20251231_01358.txt
STATIONS_ID;MESS_DATUM; … ;    TMK;     UPM;    TXK;    TNK;    TGK;eor
...
       1358;  20150101; … ;   -0.9;  100.00;    0.0;   -2.0;   -2.1;eor
       1358;  20150102; … ;   -2.1;  100.00;   -0.1;   -4.1;   -4.2;eor
       1358;  20150103; … ;   -4.6;   99.00;   -4.1;   -5.6;   -5.9;eor
...
```

Daraus sind für heute zwei Dateien mit je einem Wert pro Zeile entstanden:

<div class="flex-container">
<div class="flex-child">

```text 2015_2024_datum.txt
2015-01-01
2015-01-02
2015-01-03
...
```

</div>
<div class="flex-child">

```text 2015_2024_maximum.txt
0.0
-0.1
-4.1
...
```

</div>
</div>

--{{0}}--
Das Datum haben wir beim Vorbereiten lesbarer gemacht: aus `20150101` wurde `2015-01-01`. Zeile 1 der einen Datei gehört zu Zeile 1 der anderen, genau wie bei den zwei Listen im Abschnitt „Zusammengehörige Werte“. Wie man die Rohdatei selbst zerlegt, mit Semikolons, Leerzeichen und Fehlwerten, ist Thema der nächsten Vorlesung.

> **Live Hacking (≈ 20 min).** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam. Die Schritte unten zeigen die typischen Irrwege.

> [!NOTE] Nur im Browser
> Wie in Vorlesung 03: `open_url` funktioniert nur hier im Browser. Auf Ihrem Rechner lesen Sie Dateien ab Vorlesung 06 mit `open()`.

### Pseudocode

> **Wie würden Sie vorgehen?** Beschreiben Sie den Ablauf in eigenen Worten, noch ohne Python.
>
> * Was muss für jedes Jahr von vorn beginnen?
> * Was merkt sich das Programm, während es die Tage durchgeht?
> * Woran erkennt es, dass ein Tag zum gesuchten Jahr gehört?

                                     {{1}}
*******************************************************************************

```text
Für jedes Jahr von 2015 bis 2024:
    Setze hoechst auf -100 und tag auf "" (noch kein Tag gefunden).
    Für jeden Tag in der Liste:
        Wenn der Tag zu diesem Jahr gehört
        und sein Maximum größer als hoechst ist:
            Merke das Maximum als hoechst und das Datum als tag.
    Gib Jahr, tag und hoechst aus.
```

*******************************************************************************

### Schritt 1 - Tagesmaximum pro Jahr

Idee: Für jedes Jahr alle Tage durchgehen und nur die Tage dieses Jahres berücksichtigen. Zwei Bausteine dafür:

* `datumswerte[i]` ist das Datum des Tages `i`, etwa `"2015-08-07"`, und `datumswerte[i][0:4]` davon die ersten vier Zeichen, `"2015"`.
* `hoechst = -100.0` ist ein Startwert, den jede echte Temperatur übertrifft.
* Eine **verschachtelte Schleife**: Die äußere läuft über die Jahre, die innere für jedes Jahr über alle Tage.
* `split()` liefert Texte, deshalb macht `float(maxima[i])` aus jedem Maximum vor dem Vergleich eine Zahl.

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
datumswerte = open_url(basis + "datum.txt").read().split()
maxima      = open_url(basis + "maximum.txt").read().split()

for jahr in range(2015, 2025):
    hoechst = -100.0
    for i in range(len(datumswerte)):
        if datumswerte[i][0:4] == jahr and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
    print(jahr, hoechst)
```
@Pyodide.eval

                                     {{1}}
*******************************************************************************

Ergebnis: jedes Jahr -100,0 °C. **Was ist passiert?** `datumswerte[i][0:4]` ist der **Text** `"2015"`, `jahr` die **Zahl** `2015`. Text und Zahl sind nie gleich — die Bedingung ist nie erfüllt, und es gibt keine Fehlermeldung.

Die Lösung: `datumswerte[i][0:4] == str(jahr)`. Genau der Unterschied zwischen `"-14.1"` und `-14.1` aus Vorlesung 02.

*******************************************************************************

--{{0}}--
Die äußere Schleife läuft zehnmal, die innere jedes Mal über alle 3.653 Tage, zusammen 36.530 Durchläufe. Den ersten Wert des Jahres wie in Vorlesung 04 haben wir hier nicht zur Hand, weil die Tage eines Jahres irgendwo in der langen Liste liegen.

--{{1}}--
Python wandelt hier nichts von selbst um. Ob ein Wert Text oder Zahl ist, entscheidet, wo er herkommt: aus `split()` kommt immer Text, aus `range` immer eine Zahl.

### Typische Fehlvorstellung: Zahlen als Text vergleichen

> **Typische Fehlvorstellung:** _„Was wie eine Zahl aussieht, wird wie eine Zahl verglichen.“_

```python
# Zwei Zahlen
print(9.5 > 28.1)
print(1.5 > 28.1)
# Zwei Texte
print("9.5" > "28.1")
print("1.5" > "28.1")
# Zahl und Text
print(9.5 == "28.1")
print(9.5 > "28.1")
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Welche Zeile gibt `True` aus?

[( )] `print(9.5 > 28.1)`
[(X)] `print("9.5" > "28.1")`
[( )] `print("1.5" > "28.1")`
[( )] keine, 9,5 und 1,5 sind beide kleiner als 28,1
***
Texte werden **Zeichen für Zeichen** verglichen, wie Wörter im Wörterbuch. Die erste Stelle, an der sie sich unterscheiden, entscheidet, nicht die Anzahl der Stellen:

``` text
"9.5"  >  "28.1"     "9" kommt nach "2"  →  True
"1.5"  >  "28.1"     "1" kommt vor  "2"  →  False
```

Bei `"1.5"` stimmt das Ergebnis also zufällig, bei `"9.5"` nicht. Das ist das Tückische: Bei positiven Werten mit gleich vielen Stellen vor dem Punkt, etwa `"21.3"` und `"28.1"`, geht der Textvergleich gut, und der Fehler fällt beim Testen nicht auf. Deshalb steht in Schritt 1 `float(maxima[i])`.

Zahl und Text: `==` liefert still `False`, `>` bricht mit `TypeError` ab. Gleichheit lässt sich für alle Werte prüfen, eine Reihenfolge nicht.
***

--{{0}}--
Die Reihenfolge der Zeichen ist festgelegt: Minus vor Punkt vor den Ziffern 0 bis 9, dann Groß- vor Kleinbuchstaben. Deshalb steht „Zebra“ vor „aal“. Auch negative Werte gehen schief: `"-5.0" > "-4.0"` ist `True`, weil die 5 nach der 4 kommt. Dass `==` zwischen Text und Zahl keine Meldung bringt, hat einen Grund: Fragen wie `"2015" in [2015, 2016]` müssen für beliebige Werte eine Antwort haben, und die lautet hier „nein“. Genau deshalb blieb Schritt 1 still.

### Schritt 2 - Tagesdatum extrahieren und merken

Mit `str(jahr)` stimmen die Werte. Jetzt merken wir uns auch den Tag. Weil das Jahr in der Ausgabe ohnehin vorn steht, genügen Monat und Tag: `datumswerte[i][5:10]` macht aus `"2019-06-30"` den Text `"06-30"`.

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
datumswerte = open_url(basis + "datum.txt").read().split()
maxima      = open_url(basis + "maximum.txt").read().split()

hoechst = -100.0
for jahr in range(2015, 2025):
    for i in range(len(datumswerte)):
        if datumswerte[i][0:4] == str(jahr) and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
            tag = datumswerte[i][5:10]
    print(jahr, tag, hoechst)
```
@Pyodide.eval

Ab 2016 stimmt etwas nicht. **Was?** Vergleichen Sie mit dem Pseudocode: Wo steht dort „Setze hoechst auf -100“?

                                     {{1}}
*******************************************************************************

`hoechst = -100.0` steht jetzt **vor** der äußeren Schleife. Der Höchstwert von 2015 (28,1 °C) gilt deshalb weiter; 2016 muss ihn übertreffen, um überhaupt gezählt zu werden. Der Startwert gehört **in** die Jahresschleife: Jedes Jahr beginnt die Suche von vorn.

<!-- style="max-width: 640px; display: block; margin: auto" -->
```ascii
    hoechst = −100                       ✗ Schritt 2: gilt für alle Jahre
  +-------------------------------------------------------+
  | für jedes Jahr                                        |
  |                                                       |
  |   hoechst = −100, tag leer       ✓ gilt für ein Jahr  |
  |                                                       |
  |   +-----------------------------------------------+   |
  |   | für jeden Tag                                 |   |
  |   |   Tag aus diesem Jahr und wärmer als hoechst? |   |
  |   |   → Maximum als hoechst, Datum als tag merken |   |
  |   +-----------------------------------------------+   |
  |                                                       |
  |   Jahr, tag und hoechst ausgeben                      |
  +-------------------------------------------------------+
```

*******************************************************************************

--{{1}}--
Achten Sie auf die Wiederholungen: 2015 bis 2018 steht viermal `08-07 28.1`, ab 2019 sechsmal `06-30 29.5`. Nur 2015 und 2019 stimmen, weil nur sie den mitgeschleppten Wert übertreffen. Alle anderen Jahre erben Wert und Tag eines früheren Jahres. Mit dem vollen Datum wäre es noch deutlicher: Unter 2016 stünde `2015-08-07`, ein Tag aus dem falschen Jahr.

### Ergebnis

Gegenüber Schritt 2 ändert sich dreierlei:

* `hoechst = -100.0` steht wieder **in** der Jahresschleife, dazu `tag = ""`: Jedes Jahr beginnt ohne Höchstwert und ohne Tag.
* `jahreshoechst = []` steht **vor** allen Schleifen, die Liste sammelt über alle Jahre.
* `jahreshoechst.append(hoechst)` hängt am Ende jedes Jahres dessen Höchstwert an.

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
datumswerte = open_url(basis + "datum.txt").read().split()
maxima      = open_url(basis + "maximum.txt").read().split()

jahreshoechst = []
for jahr in range(2015, 2025):
    hoechst = -100.0
    tag = ""
    for i in range(len(datumswerte)):
        if datumswerte[i][0:4] == str(jahr) and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
            tag = datumswerte[i][5:10]
    jahreshoechst.append(hoechst)
    print(jahr, tag, hoechst)
print(jahreshoechst)
```
@Pyodide.eval

                                     {{1}}
*******************************************************************************

Drei Muster stecken ineinander:

<!-- data-type="none" -->
| Ebene             | Muster              | Variable          |
| :---------------- | :------------------ | :---------------- |
| äußere Schleife   | Sammeln             | `jahreshoechst`   |
| innere Schleife   | Extremwerte         | `hoechst`, `tag`  |
| Bedingung         | Spalte mit Bedingung | `== str(jahr)`   |

> Die Startwerte zeigen, wohin eine Variable gehört: `jahreshoechst = []` **vor** alle Schleifen (gilt für alle Jahre), `hoechst = -100.0` und `tag = ""` **in** die Jahresschleife (gelten für ein Jahr).

*******************************************************************************

--{{1}}--
Die Tabelle ist der Bauplan aus Vorlesung 04, nur dreifach ineinander. Die Bedingung ist das Muster „Spalte mit Bedingung“: Sie wählt aus allen Tagen die eines Jahres aus. Fragen Sie bei jeder Variablen: Gilt sie für alle Jahre oder für eines? Daraus ergibt sich, wo ihr Startwert steht. Ohne `tag = ""` fiele es hier nicht auf, weil jedes Jahr Werte hat. Fehlt aber ein Jahr in den Daten, erbte es still das Datum des Vorjahres.

Lesen Sie das Ergebnis ab und tragen Sie es ein:

Der wärmste Tag im ganzen Zeitraum war der 30. Juni [[2019]] mit 29,5 °C.
***
Die Jahreshöchstwerte liegen zwischen 24,5 °C (19. Juni 2021) und 29,5 °C (30. Juni 2019). 2024 war es der 13. August mit 26,9 °C, der Tag aus Ihrer Hausaufgabe zu Vorlesung 02.
***

--{{0}}--
Die Antwort auf die Leitfrage sind zehn Zeilen, eine pro Jahr. Das kühlste der zehn Jahre war 2021: Selbst sein wärmster Tag erreichte nur 24,5 °C.

### Mit dem Ergebnis weiterarbeiten

Jetzt liegen die zehn Jahreshöchstwerte in einer Liste — das Ergebnis des Programms oben — und lassen sich weiterverarbeiten:

```python
jahreshoechst = [28.1, 24.8, 26.8, 26.7, 29.5, 26.9, 24.5, 29.1, 28.4, 26.9]

mittel = sum(jahreshoechst) / len(jahreshoechst)
print("Mittel der Jahreshöchstwerte:", round(mittel, 1))

ueber_28 = 0
for h in jahreshoechst:
    if h > 28:
        ueber_28 = ueber_28 + 1
print("Jahre über 28 °C:", ueber_28)

print("Die drei höchsten:", sorted(jahreshoechst, reverse=True)[:3])
```
@Pyodide.eval

Mittel und Zählmuster kennen Sie aus Vorlesung 04. `sorted` liefert eine **neue**, sortierte Liste, `reverse=True` sortiert absteigend, `[:3]` nimmt die ersten drei.

--{{0}}--
Ohne `round` stünde dort `27.169999999999998`, die Ungenauigkeit der Kommazahlen aus Vorlesung 04. Nach dem Sortieren weiß die Liste allerdings nicht mehr, welcher Wert zu welchem Jahr gehört: 29,1 und 28,4 °C stammen aus 2022 und 2023, aber das steht nirgends mehr. Dafür braucht man beides zusammen, etwa im Dictionary oder später in pandas. Deshalb hier `sorted` und nicht `jahreshoechst.sort()`: Die Liste in der Reihenfolge der Jahre bleibt so erhalten.

## Ausblick: Dictionary

Die Lösung oben geht für jedes Jahr **alle** 3.653 Tage durch — 36.530 Durchläufe für zehn Jahre. Für alle Jahre seit 1890 wären es über sechs Millionen.

Python kennt eine Datenstruktur, die ein Ergebnis direkt unter einem **Schlüssel** ablegt, dem **Dictionary**:

```python
hoechst = {}
hoechst["2015"] = 28.1
hoechst["2016"] = 24.8
print(hoechst)
print(hoechst["2015"])
print("2017" in hoechst)
```
@Pyodide.eval

> Mit einem Dictionary genügt **ein** Durchlauf durch alle Tage: Für jeden Tag schaut man nach, ob sein Jahr schon einen Eintrag hat und ob der neue Wert größer ist. Ähnlich arbeitet `groupby` in pandas (Vorlesung 12).

--{{0}}--
Weil die Datei nach dem Datum sortiert ist, ginge es auch ohne Dictionary in einem Durchlauf, mit dem Muster „Blöcke und Zustände“ aus Vorlesung 04: Wechselt das Jahr, ist ein Block zu Ende. Das Dictionary ist heute nur ein Ausblick, Sie müssen es noch nicht können. In Vorlesung 06 lernen Sie es genauer kennen.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
werte = [5, 3, 8, 1, 9, 2]
print(werte[1], werte[-2], werte[2:4])
```

[( )] `5 2 [8, 1, 9]`
[(X)] `3 9 [8, 1]`
[( )] `3 2 [3, 8]`
[( )] `5 9 [8, 1]`
***
`werte[1]` ist der **zweite** Wert (3), `werte[-2]` der vorletzte (9), `werte[2:4]` die Indizes 2 und 3.
***

**Welche Zahlen erzeugt `range(3, 7)`?**

[( )] 3, 4, 5, 6, 7
[(X)] 3, 4, 5, 6
[( )] 4, 5, 6, 7
[( )] 0, 1, 2, 3, 4, 5, 6
***
Der Startwert 3 ist enthalten, der Endwert 7 nicht.
***

**Wo muss `hoechst = -100.0` stehen, damit jedes Jahr seinen eigenen Höchstwert bekommt?**

```python
for jahr in range(2015, 2025):
    for i in range(len(datumswerte)):
        if datumswerte[i][0:4] == str(jahr) and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
    print(jahr, hoechst)
```

[( )] vor `for jahr …`
[(X)] zwischen `for jahr …` und `for i …`
[( )] direkt unter `for i …`
***
Der Startwert gilt für ein Jahr, also gehört er in die Jahresschleife, vor die Tagesschleife. Vor `for jahr` schleppt jedes Jahr den Höchstwert der Vorjahre mit (Schritt 2). In der Tagesschleife würde er bei jedem Tag zurückgesetzt, am Ende stünde der Wert vom 31. Dezember.
***

**Wo muss die Zeile stehen, damit am Ende alle Frostwerte in der Liste sind?**

```python
for minimum in minima:
    if minimum < 0:
        frostwerte.append(minimum)
```

[ [vor der Schleife] [in der Schleife] ]
[        (X)             ( )        ] `frostwerte = []`
[        ( )             (X)        ] `frostwerte.append(minimum)`
***
Stünde `frostwerte = []` in der Schleife, würde die Liste bei jedem Durchlauf geleert. Am Ende enthielte sie höchstens den letzten Frostwert.
***

**Eine Liste hat 366 Einträge. Welche Zugriffe erzeugen einen `IndexError`?**

[[ ]] `liste[0]`
[[ ]] `liste[365]`
[[X]] `liste[366]`
[[ ]] `liste[-366]`
[[X]] `liste[-367]`

**Nach welchen Zeilen ist die Liste `werte` verändert?**

[[ ]] `n = len(werte)`
[[X]] `werte.append(4)`
[[ ]] `neu = sorted(werte)`
[[X]] `werte.sort()`
[[ ]] `print(max(werte))`
***
Nur die Methoden `append` und `sort` verändern die Liste selbst. Die Funktionen `len`, `sorted` und `max` liefern ein Ergebnis und lassen `werte`, wie es ist.
***

## Nächste Woche

Heute kamen die Daten vorbereitet aus zwei einspaltigen Dateien. Nächste Woche lesen wir die **Rohdatei** des DWD selbst — mit Semikolons, Leerzeichen, Kopfzeile und `-999` — und beantworten die Leitfrage für alle Jahre seit 1890.

**Zur Vorbereitung**

- [ ] Erweitern Sie das Programm aus „Ergebnis“ um eine zweite Liste `jahrestage`, in der Sie die Daten der wärmsten Tage sammeln.
- [ ] Speichern Sie die [Rohdatei des DWD](https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt) (6,5 MB; Rechtsklick → „Ziel speichern unter“) und öffnen Sie sie in VS Code. Welche Schritte sind nötig, um aus einer Zeile das Datum und das Tagesmaximum `TXK` zu gewinnen?

**Zur Übung**

Blatt 5 (Warum wurde Schokolade so teuer?) steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 30.11.

**Zum Wiederholen:** Die Begriffe dieser Vorlesung finden Sie in der [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=5).
