<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Visualisierung: Diagrammformen, ein Diagramm mit matplotlib bauen, Trends berechnen — und erkennen, wann eine korrekte Grafik in die Irre führt.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/a9680241e4/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/13_Visualisierung.md)

# Visualisierung

| Parameter                | Kursinformationen                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                              |
| **Inhalte:**             | `Diagrammformen, matplotlib, Achsen und Beschriftung, Trendlinie mit polyfit, gleitendes Mittel, irreführende Darstellungen`                   |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/13_Visualisierung.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/13_Visualisierung.md) |
| **Autoren**              | @author                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie zeige ich, was ich gefunden habe?_

**Fragen an die heutige Veranstaltung ...**

* Welche Diagrammform passt zu welcher Frage?
* Was gehört an jedes Diagramm?
* Wie berechnet man einen Trend — und für welchen Zeitraum?
* Wie kann eine korrekte Grafik trotzdem täuschen?

> Beim ersten Ausführen lädt der Browser pandas und matplotlib nach. Das dauert einige Sekunden. Beim ersten Diagramm meldet matplotlib in roter Schrift „Matplotlib is building the font cache“ — das ist keine Fehlermeldung, sondern ein Hinweis.

--------------------------------------------------------------------------------

## Rückblick

Letzte Woche sind Tabellen entstanden: Frosttage für 132 Jahre, Mittelwerte für 14 Jahrzehnte. Zahlenkolonnen, in denen man ein Muster nur mit Mühe erkennt.

Im Datenkreislauf aus Vorlesung 00 ist **Visualisieren** der Schritt, in dem ein Ergebnis für andere verständlich wird — und der Schritt, in dem man selbst oft zum ersten Mal sieht, was in den Daten steckt.

## Die richtige Form

<!-- data-type="none" -->
| Frage                                   | Diagrammform      | matplotlib           |
| :-------------------------------------- | :---------------- | :------------------- |
| Wie entwickelt sich ein Wert über die Zeit? | Liniendiagramm | `plt.plot(x, y)`     |
| Wie unterscheiden sich Gruppen?         | Balkendiagramm    | `plt.bar(x, y)`      |
| Wie sind Werte verteilt?                | Histogramm        | `plt.hist(werte)`    |
| Hängen zwei Größen zusammen?            | Streudiagramm     | `plt.scatter(x, y)`  |

Welche Form passt zu: _„Wie viele Frosttage gab es im Mittel pro Jahr in jedem Jahrzehnt?“_ (Vorlesung 12)

[( )] Liniendiagramm
[(X)] Balkendiagramm
[( )] Histogramm
[( )] Streudiagramm
***
14 Jahrzehnte sind 14 Gruppen, die man vergleicht — ein Balkendiagramm, wie in Vorlesung 01. Ein Liniendiagramm würde einen kontinuierlichen Verlauf zwischen den Jahrzehnten suggerieren; für die Frosttage **pro Jahr** wäre es dagegen passend.
***

## Ein Diagramm bauen

Das Jahresmittel auf dem Fichtelberg, nur vollständige Jahre (Vorlesung 12):

```python
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000
jahre = df.groupby("Jahr").agg(mittel=("TMK", "mean"), tage=("TMK", "count"))
voll = jahre[jahre["tage"] >= 360]

plt.plot(voll.index, voll["mittel"])
plt.xlabel("Jahr")
plt.ylabel("Jahresmittel der Lufttemperatur in °C")
plt.title("Fichtelberg (1213 m), vollständige Jahre")
plt.show()
```
@Pyodide.eval

**Was an jedes Diagramm gehört**

* Achsenbeschriftung **mit Einheit**
* ein Titel oder eine Bildunterschrift, die sagt, was zu sehen ist — und **woher die Daten stammen**
* bei mehreren Linien eine Legende
* der Hinweis, was weggelassen wurde (hier: unvollständige Jahre)

> Ein Diagramm muss ohne den Text, in dem es steht, verständlich sein. Fehlt die Einheit, weiß niemand, ob es um °C, °F oder Frosttage geht.

## Trend

Wie stark ist es wärmer geworden? Eine **Trendgerade** legt eine Gerade so durch die Punkte, dass sie im Mittel möglichst nah an allen liegt. `np.polyfit(x, y, 1)` liefert ihre Steigung und ihren Achsenabschnitt:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000
jahre = df.groupby("Jahr").agg(mittel=("TMK", "mean"), tage=("TMK", "count"))
ab1975 = jahre[(jahre["tage"] >= 360) & (jahre.index >= 1975)]

steigung, achse = np.polyfit(ab1975.index, ab1975["mittel"], 1)
print("Trend:", round(steigung * 10, 2), "°C pro Jahrzehnt")
plt.plot(ab1975.index, ab1975["mittel"], "o", label="Jahresmittel")
plt.plot(ab1975.index, steigung * ab1975.index + achse, label="Trend")
plt.ylabel("°C"); plt.legend(); plt.show()
```
@Pyodide.eval

Das ist die Herkunft der **0,05 °C pro Jahr** aus Vorlesung 04 — dort stand sie als feste Zahl im Text, jetzt können Sie sie selbst berechnen.

### Typische Fehlvorstellung: Ein Trend ist ein Trend

> **Typische Fehlvorstellung:** _„Die Daten haben einen Trend — man muss ihn nur ausrechnen.“_

Dieselbe Messreihe, drei Zeiträume:

<!-- data-type="none" -->
| Zeitraum      | Jahre | Trend pro Jahrzehnt |
| :------------ | ----: | ------------------: |
| 1891–2025     |   127 | 0,15 °C             |
| 1975–2025     |    51 | 0,50 °C             |
| 2010–2025     |    16 | 1,18 °C             |

Welcher Trend ist der richtige?

[( )] 0,15 °C — der längste Zeitraum ist immer der richtige.
[( )] 1,18 °C — die neuesten Daten sind die aussagekräftigsten.
[(X)] Alle drei sind korrekt berechnet; welcher passt, hängt von der Frage ab — und der Zeitraum muss immer dabei stehen.
***
Die Erwärmung hat sich beschleunigt; deshalb liefert ein früherer Startpunkt einen flacheren Trend. Über 16 Jahre ist eine Gerade aber stark vom Zufall einzelner warmer oder kalter Jahre geprägt. Wer einen Trend nennt, ohne den Zeitraum zu nennen — oder den Zeitraum so wählt, dass die gewünschte Zahl herauskommt —, führt in die Irre, auch wenn jede Rechnung stimmt. Das nennt man **Rosinenpicken**.
***

## Irreführende Darstellungen

Dieselben Zahlen, zwei Diagramme: die mittleren Frosttage pro Jahr in den 1900ern und den 2020ern (Vorlesung 12).

```python
import matplotlib.pyplot as plt

jahrzehnt = ["1900er", "2020er"]
frosttage = [189.8, 140.0]

fig, (links, rechts) = plt.subplots(1, 2, figsize=(8, 3))
links.bar(jahrzehnt, frosttage)
links.set_ylim(130, 195)
links.set_title("Achse ab 130")
rechts.bar(jahrzehnt, frosttage)
rechts.set_ylim(0, 200)
rechts.set_title("Achse ab 0")
plt.show()
```
@Pyodide.eval

Um wie viel Prozent ist die Zahl der Frosttage gesunken?

[( )] um rund 80 % — so sieht es links aus
[(X)] um rund 26 %
[( )] um rund 50 %
***
(189,8 − 140,0) / 189,8 ≈ 26 %. Im linken Diagramm ist der rechte Balken nur noch ein Fünftel so hoch wie der linke — weil die Achse bei 130 beginnt und die Balkenlänge damit nicht mehr proportional zum Wert ist. Bei **Balken** muss die Achse bei null beginnen. Bei **Linien** ist ein Ausschnitt erlaubt, wenn die Achse deutlich beschriftet ist.
***

Weitere häufige Fallen:

* **Zeitraum auswählen** — siehe Trend oben.
* **Lücken überbrücken** — eine Linie verbindet Punkte auch über Jahre ohne Daten hinweg (siehe Live Hacking).
* **Fehlende Einheit oder Quelle** — der Leser kann nicht prüfen, was er sieht.
* **Zwei y-Achsen** mit frei gewählten Skalen — damit lässt sich fast jeder Zusammenhang „zeigen“.

## Live Hacking: Frosttage pro Jahr

Ein Diagramm der Frosttage pro Jahr seit 1891 — für einen Bericht.

> **Live Hacking.** In der Vorlesung bauen wir das Diagramm Schritt für Schritt. Die Versuche zeigen, was dabei schiefgeht.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

frost = (df["TNK"] < 0).groupby(df["Jahr"]).sum()
plt.plot(frost.index, frost)
plt.show()
```
@Pyodide.eval

**Was stimmt an diesem Diagramm nicht?** Sehen Sie genau hin — um 1890 und um 1910.

*******************************************************************************

                                     {{1}}
*******************************************************************************

Drei Probleme, keine Fehlermeldung:

1. **Unvollständige Jahre:** 1890 (58), 1891, 1910 und 1915 erscheinen als scheinbar milde Jahre — es fehlen einfach Tage (Vorlesung 12).
2. **Die Lücke wird überbrückt:** Zwischen 1910 und 1915 zieht die Linie einen glatten Strich, als gäbe es Daten.
3. **Keine Beschriftung:** Keine Einheit, kein Titel, keine Quelle.

*******************************************************************************

### Versuch 2

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000
jahre = df.groupby("Jahr").agg(frost=("TNK", lambda t: (t < 0).sum()),
                                tage=("TNK", "count"))
voll = jahre[jahre["tage"] >= 360].reindex(range(1891, 2026))

plt.plot(voll.index, voll["frost"], marker=".")
plt.ylabel("Frosttage pro Jahr")
plt.show()
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

`reindex(range(1891, 2026))` legt für **jedes** Jahr eine Zeile an — fehlende Jahre bekommen `NaN`. Und an `NaN` **unterbricht** matplotlib die Linie. Jetzt sieht man die Lücke 1911–1915, statt sie zu übermalen. Die Punkte (`marker=".")`) zeigen zusätzlich, wo tatsächlich Werte liegen.

Aber: Von Jahr zu Jahr schwankt die Zahl stark. Ist da überhaupt ein Trend?

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
import matplotlib.pyplot as plt
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000
jahre = df.groupby("Jahr").agg(frost=("TNK", lambda t: (t < 0).sum()),
                                tage=("TNK", "count"))
voll = jahre[jahre["tage"] >= 360].reindex(range(1891, 2026))
glatt = voll["frost"].rolling(10, center=True, min_periods=7).mean()

plt.plot(voll.index, voll["frost"], ".", color="lightgray", label="einzelne Jahre")
plt.plot(voll.index, glatt, label="gleitendes Mittel über 10 Jahre")
plt.ylabel("Frosttage pro Jahr (Minimum < 0 °C)")
plt.title("Fichtelberg, vollständige Jahre — Daten: DWD")
plt.legend(); plt.show()
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

Ein **gleitendes Mittel** ersetzt jeden Wert durch das Mittel der umliegenden zehn Jahre. Zufällige Ausreißer — ein strenger Winter, ein milder — mitteln sich heraus, der langfristige Verlauf bleibt.

Jetzt erzählt das Diagramm, was die Zahlen sagen: lange Zeit um 175–190 Frosttage, seit den 1990ern ein deutlicher Rückgang auf unter 150. Und es verschweigt nicht, wo Daten fehlen.

> Drei Versionen, dieselben Daten. Die erste war nicht falsch berechnet — sie war falsch **gezeigt**.

*******************************************************************************

## Kontrollfragen

**Warum ist diese Darstellung irreführend?** (Klausurformat)

> Ein Balkendiagramm zeigt die Jahresniederschläge in Freiberg: 754 mm (1946–1992) und 664 mm (2016–2025). Die y-Achse beginnt bei 650 mm, der zweite Balken ist kaum zu sehen.

<details>
<summary>**Lösung**</summary>

Zwei Gründe:

* Die **Achse beginnt nicht bei null**: Der Rückgang um rund 12 % erscheint wie ein Einbruch auf fast nichts.
* **Inhaltlich** stammen die Werte von zwei verschiedenen Standorten mit verschiedenen Messgeräten — der Rückgang ist zu einem großen Teil ein Messartefakt, kein Klimasignal. Das ist das Thema der nächsten Vorlesung.

</details>

**Was gibt `np.polyfit(jahre, werte, 1)` zurück?**

[( )] den Mittelwert und die Standardabweichung
[(X)] die Steigung und den Achsenabschnitt der Trendgeraden
[( )] die Werte der Trendgeraden für jedes Jahr

**Welche Aussagen über Diagramme stimmen?**

[[X]] Bei Balkendiagrammen muss die y-Achse bei null beginnen.
[[ ]] Ein Liniendiagramm sollte fehlende Jahre durch eine durchgehende Linie verbinden.
[[X]] Zu einem Trend gehört die Angabe des Zeitraums.
[[X]] Ein gleitendes Mittel macht langfristige Entwicklungen sichtbar und dämpft Ausreißer.

## Nächste Woche

In der letzten Vorlesung fragen wir: **Kann ich meinem Ergebnis trauen?** Freiberg zieht um — und die Daten sehen danach genauso aus wie vorher. Dazu: Ausblick und Prüfungsvorbereitung.

**Zur Vorbereitung**

- [ ] Erstellen Sie in VS Code (mit Zellen `# %%`) ein Diagramm der **Sommertage** pro Jahr mit gleitendem Mittel. Speichern Sie es mit `plt.savefig("sommertage.png")`.
- [ ] Zeichnen Sie das Jahresmittel von Fichtelberg und Chemnitz in ein gemeinsames Diagramm. Wo fehlen Chemnitzer Daten?
- [ ] Suchen Sie in einer Zeitung oder einem Bericht ein Diagramm, das Sie für irreführend halten. Woran liegt es?
