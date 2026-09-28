<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
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

--------------------------------------------------------------------------------

## Rückblick

Bisher haben wir Listen nur **benutzt**: als fertige Werte im Programm oder als Ergebnis von `text.split()`. Und wir haben uns in einer Schleife immer nur **einen** Wert gemerkt — einen Zähler, eine Summe, den bisher kältesten Tag.

Die Leitfrage verlangt mehr: **ein Ergebnis pro Jahr**. Dafür müssen wir Ergebnisse **sammeln**.

## Listen anlegen und füllen

Eine Liste beginnt oft leer und wächst mit `append`:

```` @BlocklyId(sammeln, runner=sammeln hideRunner height=340)
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

## Zugriff über den Index

Jeder Wert einer Liste hat eine Position, den **Index**. Gezählt wird ab 0:

``` ascii
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

## Zahlenfolgen mit `range`

`range` erzeugt eine Folge ganzer Zahlen:

<!-- data-type="none" -->
| Aufruf              | erzeugt                       |
| :------------------ | :---------------------------- |
| `range(5)`          | 0, 1, 2, 3, 4                 |
| `range(2015, 2025)` | 2015, 2016, ..., 2024         |
| `range(0, 366, 7)`  | 0, 7, 14, ..., 364            |

Auch hier ist der Endwert **nicht** enthalten. Das passt genau zum Index: `range(len(minima))` liefert alle gültigen Indizes einer Liste.

```python
minima = [-1.9, -2.4, 0.1, -1.7]

for i in range(len(minima)):
    print("Index", i, "Wert", minima[i])
```
@Pyodide.eval

> Wozu der Umweg über den Index, wenn `for minimum in minima` einfacher ist? Weil man manchmal **zwei Listen gleichzeitig** durchlaufen muss.

## Zusammengehörige Werte

Für die Leitfrage brauchen wir zu jeder Temperatur das **Datum**. Wir halten beides in zwei Listen gleicher Länge — Index `i` gehört in beiden Listen zum selben Tag:

``` ascii
daten   =  [ "2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14" ]
maxima  =  [   22.5,         25.0,         26.9,         23.9       ]
               i = 0         i = 1         i = 2         i = 3
```

```python
daten  = ["2024-08-11", "2024-08-12", "2024-08-13", "2024-08-14"]
maxima = [22.5, 25.0, 26.9, 23.9]

bester = 0
for i in range(len(maxima)):
    if maxima[i] > maxima[bester]:
        bester = i

print("Wärmster Tag:", daten[bester], "mit", maxima[bester], "°C")
```
@Pyodide.eval

> Statt Wert **und** Datum merken wir uns nur den **Index** des bisher wärmsten Tages. Über ihn kommen wir an beides.

### Typische Fehlvorstellung: Index oder Wert?

> **Typische Fehlvorstellung:** _„`bester` enthält die höchste Temperatur.“_

Was gibt `print(bester)` nach der Schleife im Beispiel oben aus?

[( )] `26.9`
[(X)] `2`
[( )] `"2024-08-13"`
***
`bester` ist ein **Index**, keine Temperatur: die Position des wärmsten Tages in beiden Listen. Die Temperatur steht in `maxima[bester]`, das Datum in `daten[bester]`. Wer Index und Inhalt verwechselt, vergleicht Positionen mit Temperaturen — und Python meldet keinen Fehler, weil beides Zahlen sind.
***

## Ein Ergebnis pro Jahr

Für die Jahre 2015 bis 2024 liegen Datum und Tagesmaximum als zwei Dateien im Repository — 3.653 Tage, ein Wert pro Zeile, wie in Vorlesung 03.

> **Live Hacking.** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam. Die Versuche unten zeigen die typischen Irrwege.

> [!NOTE]
> Wie in Vorlesung 03: `open_url` funktioniert nur hier im Browser. Auf Ihrem Rechner lesen Sie Dateien ab Vorlesung 06 mit `open()`.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

Idee: Für jedes Jahr alle Tage durchgehen und nur die Tage dieses Jahres berücksichtigen.

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
daten = open_url(basis + "datum.txt").read().split()
maxima = open_url(basis + "maximum.txt").read().split()

for jahr in range(2015, 2025):
    hoechst = -100.0
    for i in range(len(daten)):
        if daten[i][0:4] == jahr and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
    print(jahr, hoechst)
```
@Pyodide.eval

Jedes Jahr: -100,0 °C. **Was ist passiert?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`daten[i][0:4]` ist der **Text** `"2015"`, `jahr` die **Zahl** `2015`. Text und Zahl sind nie gleich — die Bedingung ist nie erfüllt, und es gibt keine Fehlermeldung.

Die Lösung: `daten[i][0:4] == str(jahr)`. Genau der Unterschied zwischen `"-14.1"` und `-14.1` aus Vorlesung 02.

*******************************************************************************

### Typische Fehlvorstellung: Zahlen als Text vergleichen

> **Typische Fehlvorstellung:** _„Was wie eine Zahl aussieht, wird wie eine Zahl verglichen.“_

Nach `split()` sind alle Werte **Text**. Was passiert, wenn man `float()` vergisst?

```python
maxima = "28.1 24.8 9.5".split()
print(maxima)
print("9.5" > "28.1")
print(max(maxima))
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Welchen Wert liefert `max(maxima)`?

[( )] `"28.1"`
[(X)] `"9.5"`
[( )] eine Fehlermeldung, weil man Texte nicht vergleichen kann
***
Texte werden **Zeichen für Zeichen** verglichen, wie Wörter im Wörterbuch. Das erste Zeichen von `"9.5"` ist `9`, das von `"28.1"` ist `2` — und `9` kommt nach `2`. Also gilt `"9.5" > "28.1"`.

Das Programm läuft ohne Fehlermeldung und liefert ein plausibel aussehendes, aber falsches Ergebnis. In Versuch 1 wäre dieser Fehler aufgefallen, weil `float(maxima[i])` die Umwandlung erzwingt.
***

### Versuch 2

                                     {{0-1}}
*******************************************************************************

Mit `str(jahr)` stimmen die Werte. Jetzt sammeln wir sie — und merken uns auch den Tag:

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
daten = open_url(basis + "datum.txt").read().split()
maxima = open_url(basis + "maximum.txt").read().split()

hoechst = -100.0
for jahr in range(2015, 2025):
    for i in range(len(daten)):
        if daten[i][0:4] == str(jahr) and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
            tag = daten[i]
    print(jahr, tag, hoechst)
```
@Pyodide.eval

Ab 2016 stimmt etwas nicht. **Was?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`hoechst = -100.0` steht jetzt **vor** der äußeren Schleife. Der Höchstwert von 2015 (28,1 °C) gilt deshalb weiter; 2016 muss ihn übertreffen, um überhaupt gezählt zu werden. Der Startwert gehört **in** die Jahresschleife: Jedes Jahr beginnt die Suche von vorn.

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

```python
from pyodide.http import open_url
basis = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
         "VL_EAVD/master/data/fichtelberg/2015_2024_")
daten = open_url(basis + "datum.txt").read().split()
maxima = open_url(basis + "maximum.txt").read().split()

jahreshoechst = []
for jahr in range(2015, 2025):
    hoechst = -100.0
    for i in range(len(daten)):
        if daten[i][0:4] == str(jahr) and float(maxima[i]) > hoechst:
            hoechst = float(maxima[i])
            tag = daten[i]
    jahreshoechst.append(hoechst)
    print(jahr, tag, hoechst)
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

Drei Muster stecken ineinander:

<!-- data-type="none" -->
| Ebene             | Muster              | Variable          |
| :---------------- | :------------------ | :---------------- |
| äußere Schleife   | Sammeln             | `jahreshoechst`   |
| innere Schleife   | Extremwert suchen   | `hoechst`, `tag`  |
| Bedingung         | Filtern             | `== str(jahr)`    |

> Die Startwerte zeigen, wohin eine Variable gehört: `jahreshoechst = []` **vor** alle Schleifen (gilt für alle Jahre), `hoechst = -100.0` **in** die Jahresschleife (gilt für ein Jahr).

*******************************************************************************

### Mit dem Ergebnis weiterarbeiten

Jetzt liegen die zehn Jahreshöchstwerte in einer Liste — und lassen sich weiterverarbeiten. Ergänzen Sie Versuch 3 um folgende Zeilen:

```python
print("Mittel der Jahreshöchstwerte:", sum(jahreshoechst) / len(jahreshoechst))
print("Jahre über 28 °C:", len([h for h in jahreshoechst if h > 28]))
```

Die zweite Zeile verwendet eine Kurzschreibweise, die Sie noch nicht kennen. Schreiben Sie sie als Schleife mit dem Zählmuster.

Der wärmste Tag im ganzen Zeitraum war der 30. Juni [[2019]] mit 29,5 °C.

## Ausblick: Dictionary

Die Lösung oben geht für jedes Jahr **alle** 3.653 Tage durch — 36.530 Durchläufe für zehn Jahre. Für 135 Jahre wären es sechs Millionen.

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

> Mit einem Dictionary genügt **ein** Durchlauf durch alle Tage: Für jeden Tag schaut man nach, ob sein Jahr schon einen Eintrag hat und ob der neue Wert größer ist. Genau so arbeitet `groupby` in pandas (Vorlesung 12).

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

- [ ] Schreiben Sie die Kurzschreibweise `len([h for h in jahreshoechst if h > 28])` als Schleife.
- [ ] Erweitern Sie Versuch 3 um eine zweite Liste `jahrestage`, in der Sie die Daten der wärmsten Tage sammeln.
- [ ] Öffnen Sie die Rohdatei `data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt` in einem Texteditor. Welche Schritte sind nötig, um aus einer Zeile das Datum und das Tagesmaximum `TXK` zu gewinnen?
