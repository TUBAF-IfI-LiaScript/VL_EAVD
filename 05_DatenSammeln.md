<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.2.1
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
| **Inhalte:**             | `Listen anlegen und füllen, append, Index und Slices, range, parallele Listen, Dictionary (Ausblick)`                                              |
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

## Rückblick

Bisher haben wir Listen nur **benutzt**: als fertige Werte im Programm oder als Ergebnis von `text.split()`. Und wir haben uns in einer Schleife immer nur **einen** Wert gemerkt — einen Zähler, eine Summe, den bisher kältesten Tag.

Die Leitfrage verlangt mehr: **ein Ergebnis pro Jahr**. Dafür müssen wir Ergebnisse **sammeln**, das Ergebnis ist dann selbst eine Liste.

![Drei Felder mit Klötzchen. Links unter „Bisher (VL 03, 04)“: sieben Tiefsttemperaturen ergeben einen Wert, 6 Frosttage. Rechts unter der gemeinsamen Überschrift „Heute (VL 05): Listen als Ergebnis“ zwei Felder: „Werte entnehmen“, aus denselben sieben Werten werden die sechs Frostwerte als neue Liste ausgewählt, und „Ein Ergebnis pro Jahr“, Werte der Jahre 2015, 2016 und 2017 ergeben, je Jahr farbig gruppiert, die Liste der Jahreshöchstwerte 28,1, 24,8 und 26,8 °C.](images/05_DatenSammeln/eingabe_ausgabe.svg)<!-- style="max-height: 40vh;" -->

--{{0}}--
`text.split()` aus Vorlesung 03 hat uns schon eine Liste geliefert, wir haben sie nur nicht so genannt. Neu ist heute, dass wir Listen selbst füllen.

## Listen anlegen und füllen

Eine Liste beginnt oft leer und wächst mit `append`:

```` @BlocklyId(sammeln, runner=sammeln hideRunner height=600)
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]

frostwerte = []

for minimum in minima:
    if minimum < 0:
        frostwerte.append(minimum)

print("Frostwerte:", frostwerte)
print("Anzahl:", len(frostwerte))
````

```python
# runner: sammeln
```
@Pyodide.eval

Das ist das **Sammelmuster** — dieselbe Struktur wie das Zählmuster aus Vorlesung 03:

<!-- data-type="none" -->
| Muster     | vor der Schleife     | in der Schleife                  |
| :--------- | :------------------- | :------------------------------- |
| Zählen     | `frosttage = 0`      | `frosttage = frosttage + 1`      |
| Sammeln    | `frostwerte = []`    | `frostwerte.append(minimum)`     |

> `len(frostwerte)` liefert die Anzahl — das Zählmuster ist im Sammelmuster also schon enthalten.

--{{0}}--
`append` heißt „anhängen“: Der neue Wert kommt ans Ende der Liste. Die leere Liste `[]` vor der Schleife ist der Startwert, so wie die 0 beim Zählen. Und `len` zählt am Ende, was hineingekommen ist.

## Zugriff über den Index

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

### Typische Fehlvorstellung: `range` ist eine Liste

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

### Typische Fehlvorstellung: Index oder Wert?

> **Typische Fehlvorstellung:** _„`bester` enthält die höchste Temperatur.“_

Legen Sie sich fest, **bevor** Sie nachsehen: Was gibt `print(bester)` nach der Schleife im Beispiel oben aus?

[( )] `26.9`
[(X)] `2`
[( )] `"2024-08-13"`
***
`bester` ist ein **Index**, keine Temperatur: die Position des wärmsten Tages in beiden Listen. Die Temperatur steht in `maxima[bester]`, das Datum in `datumswerte[bester]`. Wer Index und Inhalt verwechselt, vergleicht Positionen mit Temperaturen — und Python meldet keinen Fehler, weil beides Zahlen sind.
***

--{{0}}--
Der Name `bester` ist hier mit Absicht knapp, er lässt offen, ob ein Index oder eine Temperatur drinsteht. In Ihren eigenen Programmen ist ein Name besser, dem man den Inhalt ansieht, etwa `index_waermster`. Dann passiert diese Verwechslung seltener.

## Üben: Fehler finden bei Listen

**⏱ 7 Minuten, zu zweit.** Alle sechs Programme sollen `Frostwerte: [-1.9, -2.4, -1.7]` ausgeben. Vier melden einen Fehler, zwei laufen ohne Meldung falsch. Lesen Sie bei den Meldungen genau, welche Zeile und welches Wort Python nennt.

> Beginnen Sie mit 1, 2 und 5. Solche Fehlersuchen kommen auch in der Klausur vor.

<div class="flex-container">
<div class="flex-child">

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

</div>
<div class="flex-child">

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

</div>
</div>

<details>
<summary>**Lösung**</summary>

1. Ausgabe `Frostwerte: [-1.7]`: `frostwerte = []` steht **in** der Schleife und leert die Liste bei jedem Durchlauf. Übrig bleibt der letzte Frostwert. Startwerte gehören vor die Schleife.
2. `SyntaxError: invalid syntax. Perhaps you forgot a comma?`: Zwischen `-2.4` und `0.1` fehlt das Komma. Python rät hier sogar richtig.
3. Ausgabe mit dreimal der ganzen Liste: `append(minima)` hängt die ganze Liste an, nicht den einzelnen Wert `minimum`. Derselbe Namensfehler wie in Vorlesung 03.
4. `AttributeError: 'NoneType' object has no attribute 'append'`: `append` verändert die Liste und gibt **nichts** zurück (`None`). Wer das Ergebnis zuweist, hat danach keine Liste mehr. Richtig ist nur `frostwerte.append(minimum)`.
5. `IndexError: list index out of range`: `range(len(minima) + 1)` läuft bis Index 4, die Liste hat nur die Indizes 0 bis 3.
6. `TypeError: 'builtin_function_or_method' object is not subscriptable`: Eckige statt runder Klammern. `append` ist eine Funktion und wird mit `(...)` aufgerufen, `[...]` ist der Zugriff über den Index.

</details>

--{{0}}--
Die Programme 1 und 3 sind die gefährlichen: Sie laufen durch und liefern eine Liste, die nur auf den zweiten Blick falsch ist. Programm 4 ist ein Klassiker, auch in Code von einer KI: `append` sieht aus wie eine Rechnung, die ein Ergebnis liefert, verändert aber die Liste selbst. Die Meldung erscheint erst beim zweiten Frostwert, weil `frostwerte` nach dem ersten Durchlauf `None` ist.

## Ein Ergebnis pro Jahr

Für die Jahre 2015 bis 2024 liegen Datum und Tagesmaximum als zwei Dateien im Repository — 3.653 Tage, ein Wert pro Zeile, wie in Vorlesung 03. Quelle: Deutscher Wetterdienst, Station 01358, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

> **Live Hacking.** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam. Die Versuche unten zeigen die typischen Irrwege.

> [!NOTE] Nur im Browser
> Wie in Vorlesung 03: `open_url` funktioniert nur hier im Browser. Auf Ihrem Rechner lesen Sie Dateien ab Vorlesung 06 mit `open()`.

### Erst im Kleinen: Schleife in der Schleife

Für jedes Jahr alle Tage durchgehen heißt: eine Schleife **in** einer Schleife.

```python
for jahr in [2015, 2016]:
    for monat in ["Juni", "Juli", "August"]:
        print(jahr, monat)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt es aus?

[( )] 2 Zeilen, eine pro Jahr
[( )] 5 Zeilen, erst die Jahre, dann die Monate
[(X)] 6 Zeilen, erst alle Monate von 2015, dann alle von 2016
[( )] 6 Zeilen, abwechselnd 2015 und 2016
***
Die innere Schleife läuft für **jedes** Jahr einmal ganz durch: 2 · 3 = 6 Zeilen. Erst wenn sie fertig ist, kommt das nächste Jahr. Im Live Hacking sind es 10 Jahre · 3.653 Tage = 36.530 Durchläufe.
***

### Versuch 1

Idee: Für jedes Jahr alle Tage durchgehen und nur die Tage dieses Jahres berücksichtigen. Zwei Bausteine dafür:

* `datumswerte[i]` ist das Datum des Tages `i`, etwa `"2015-08-07"`, und `datumswerte[i][0:4]` davon die ersten vier Zeichen, `"2015"`.
* `hoechst = -100.0` ist ein Startwert, den jede echte Temperatur übertrifft.

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

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Welcher Höchstwert erscheint für 2015?

                                     {{1}}
*******************************************************************************

Ergebnis: jedes Jahr -100,0 °C. **Was ist passiert?** `datumswerte[i][0:4]` ist der **Text** `"2015"`, `jahr` die **Zahl** `2015`. Text und Zahl sind nie gleich — die Bedingung ist nie erfüllt, und es gibt keine Fehlermeldung.

Die Lösung: `datumswerte[i][0:4] == str(jahr)`. Genau der Unterschied zwischen `"-14.1"` und `-14.1` aus Vorlesung 02.

*******************************************************************************

--{{0}}--
Hier steht eine Schleife in einer Schleife, eine **verschachtelte Schleife**. Die äußere läuft über die zehn Jahre, die innere für jedes Jahr über alle 3.653 Tage, zusammen 36.530 Durchläufe. Den ersten Wert des Jahres wie in Vorlesung 04 haben wir hier nicht zur Hand, weil die Tage eines Jahres irgendwo in der langen Liste liegen.

--{{1}}--
Python wandelt hier nichts von selbst um. Ob ein Wert Text oder Zahl ist, entscheidet, wo er herkommt: aus `split()` kommt immer Text, aus `range` immer eine Zahl.

### Typische Fehlvorstellung: Zahlen als Text vergleichen

> **Typische Fehlvorstellung:** _„Was wie eine Zahl aussieht, wird wie eine Zahl verglichen.“_

Nach `split()` sind alle Werte **Text**. Was passiert, wenn man `float()` vergisst?

```python
maxima = "28.1 24.8 9.5".split()
print(maxima)
print("9.5" > "28.1")
print(max(maxima), type(max(maxima)))
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Welchen Wert liefert `max(maxima)`?

[( )] `"28.1"`
[(X)] `"9.5"`
[( )] eine Fehlermeldung, weil man Texte nicht vergleichen kann
***
Texte werden **Zeichen für Zeichen** verglichen, wie Wörter im Wörterbuch. Das erste Zeichen von `"9.5"` ist `9`, das von `"28.1"` ist `2` — und `9` kommt nach `2`. Also gilt `"9.5" > "28.1"`. Die Ausgabe `9.5 <class 'str'>` zeigt es: `print` lässt bei Text die Anführungszeichen weg, `type` verrät, dass es Text ist.

Das Programm läuft ohne Fehlermeldung und liefert ein plausibel aussehendes, aber falsches Ergebnis. In Versuch 1 kann dieser Fehler nicht passieren, weil `float(maxima[i])` jeden Wert vor dem Vergleich umwandelt.
***

--{{0}}--
Vergleicht man Text und Zahl mit `>`, bricht Python mit einem `TypeError` ab. Nur `==` und `!=` liefern stillschweigend ein Ergebnis: Text und Zahl sind nie gleich. Beim Vergleich zweier Texte gibt es dagegen nie eine Meldung, deshalb ist dieser Fehler so tückisch.

### Versuch 2

Mit `str(jahr)` stimmen die Werte. Jetzt sammeln wir sie — und merken uns auch den Tag:

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
            tag = datumswerte[i]
    print(jahr, tag, hoechst)
```
@Pyodide.eval

Ab 2016 stimmt etwas nicht. **Was?**

                                     {{1}}
*******************************************************************************

`hoechst = -100.0` steht jetzt **vor** der äußeren Schleife. Der Höchstwert von 2015 (28,1 °C) gilt deshalb weiter; 2016 muss ihn übertreffen, um überhaupt gezählt zu werden. Der Startwert gehört **in** die Jahresschleife: Jedes Jahr beginnt die Suche von vorn.

*******************************************************************************

--{{1}}--
Achten Sie auf die Spalte mit dem Datum: 2016 bis 2018 steht dort der 7. August 2015, ab 2020 der 30. Juni 2019. Nur 2015 und 2019 stimmen, weil nur sie den mitgeschleppten Wert übertreffen. Alle anderen Jahre erben Wert und Tag eines früheren Jahres.

### Versuch 3

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
            tag = datumswerte[i]
    jahreshoechst.append(hoechst)
    print(jahr, tag, hoechst)
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

Jetzt liegen die zehn Jahreshöchstwerte in einer Liste — das Ergebnis von Versuch 3 — und lassen sich weiterverarbeiten:

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

Mittel und Zählmuster kennen Sie aus Vorlesung 04. Neu ist `sorted`: Es liefert eine **neue**, sortierte Liste, `reverse=True` absteigend, `[:3]` nimmt die ersten drei.

--{{0}}--
Ohne `round` stünde dort `27.169999999999998`, die Ungenauigkeit der Kommazahlen aus Vorlesung 04. Nach dem Sortieren weiß die Liste allerdings nicht mehr, welcher Wert zu welchem Jahr gehört: 29,1 und 28,4 °C stammen aus 2022 und 2023, aber das steht nirgends mehr. Dafür braucht man beides zusammen, etwa im Dictionary oder später in pandas. Vorsicht bei `jahreshoechst.sort()`: Es sortiert die Liste selbst um und gibt wie `append` nichts zurück.

## Ausblick: Dictionary

Die Lösung oben geht für jedes Jahr **alle** 3.653 Tage durch — 36.530 Durchläufe für zehn Jahre. Für 135 Jahre wären es über sechs Millionen.

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

## Nächste Woche

Heute kamen die Daten vorbereitet aus zwei einspaltigen Dateien. Nächste Woche lesen wir die **Rohdatei** des DWD selbst — mit Semikolons, Leerzeichen, Kopfzeile und `-999` — und beantworten die Leitfrage für alle 135 Jahre.

**Zur Vorbereitung**

- [ ] Erweitern Sie Versuch 3 um eine zweite Liste `jahrestage`, in der Sie die Daten der wärmsten Tage sammeln.
- [ ] Speichern Sie die [Rohdatei des DWD](https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt) (6,5 MB; Rechtsklick → „Ziel speichern unter“) und öffnen Sie sie in VS Code. Welche Schritte sind nötig, um aus einer Zeile das Datum und das Tagesmaximum `TXK` zu gewinnen?

**Zur Übung**

Blatt 5 (Warum wurde Schokolade so teuer?) steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 30.11.

**Zum Wiederholen:** Die Begriffe dieser Vorlesung finden Sie in der [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=5).
