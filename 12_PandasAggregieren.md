<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  pandas II: Gruppieren und Zusammenfassen mit groupby — Frosttage pro Jahr und pro Jahrzehnt, vollständige Jahre, zwei Stationen verbinden.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/a9680241e4/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md)

# pandas II — Aggregieren

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `groupby, Aggregationsfunktionen, agg, vollständige Jahre, Jahrzehnte, merge`                                                                      |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie fasse ich Jahrzehnte zusammen?_

**Fragen an die heutige Veranstaltung ...**

* Wie berechnet man eine Kennzahl für jede Gruppe — jedes Jahr, jedes Jahrzehnt?
* Woran erkennt man, ob Gruppen vergleichbar sind?
* Wie verbindet man zwei Datensätze?

> Beim ersten Ausführen lädt der Browser pandas nach. Das dauert einige Sekunden.

--------------------------------------------------------------------------------

## Aufgabe 3 aus Vorlesung 01

Erinnern Sie sich an die dritte Aufgabe mit der Tabellenkalkulation? _„Wie hat sich die Zahl der Frosttage pro Jahr seit 1890 entwickelt?“_ — 135 Jahre, für jedes eine eigene Formel. Praktisch aussichtslos.

In Vorlesung 06 haben wir es mit einem Dictionary und rund 15 Zeilen geschafft. Heute:

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

frosttage = (df["TNK"] < 0).groupby(df["Jahr"]).sum()
print(frosttage)
```
@Pyodide.eval

Eine Zeile Auswertung. Die Arbeit steckt — wie letzte Woche — im richtigen Einlesen.

## groupby: Teilen, Anwenden, Zusammenfügen

`groupby` arbeitet in drei Schritten:

``` ascii
     Jahr  TNK                Jahr 2023          Jahr 2024
    ┌─────┬──────┐          ┌─────┬──────┐     ┌─────┬──────┐
    │2023 │ -2.1 │          │2023 │ -2.1 │     │2024 │ -1.9 │       Jahr  Frosttage
    │2023 │  0.4 │  teilen  │2023 │  0.4 │     │2024 │ -2.4 │  zusammen-  ┌─────┬────┐
    │2024 │ -1.9 │ ───────▶ │2023 │ -0.7 │     │2024 │  0.1 │  fügen      │2023 │ 2  │
    │2024 │ -2.4 │          └─────┴──────┘     └─────┴──────┘ ─────────▶ │2024 │ 2  │
    │2023 │ -0.7 │           anwenden: Frost zählen                       └─────┴────┘
    │2024 │  0.1 │
    └─────┴──────┘
```

1. **Teilen:** Die Zeilen werden nach dem Wert einer Spalte in Gruppen sortiert.
2. **Anwenden:** Auf jede Gruppe wird dieselbe Funktion angewendet — `sum`, `mean`, `max`, `count`, ...
3. **Zusammenfügen:** Die Ergebnisse bilden eine neue, kurze Tabelle: eine Zeile pro Gruppe.

Am kleinen Beispiel zum Nachrechnen:

```python
import pandas as pd

df = pd.DataFrame({"Jahr": [2023, 2023, 2024, 2024, 2023, 2024],
                   "TNK":  [-2.1, 0.4, -1.9, -2.4, -0.7, 0.1]})

print(df.groupby("Jahr")["TNK"].mean())
print(df.groupby("Jahr")["TNK"].agg(["min", "max", "count"]))
```
@Pyodide.eval

> Das ist das Dictionary-Prinzip aus Vorlesung 06: ein Eintrag pro Jahr, in einem Durchlauf gefüllt. `groupby` erledigt das für jede Spalte und jede Funktion.

## Live Hacking: Frosttage pro Jahrzehnt

In Vorlesung 01 haben Sie ein Diagramm gesehen: die mittlere Zahl der Frosttage pro Jahr, für jedes Jahrzehnt seit 1890. Heute berechnen wir es selbst.

> **Live Hacking.** In der Vorlesung entwickeln wir die Auswertung gemeinsam. Die Versuche zeigen die typischen Irrwege.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

frost = df[df["TNK"] < 0]
print(frost.groupby("Jahr")["TNK"].count().head())
print(df.groupby("Jahr")["TNK"].count().head())
```
@Pyodide.eval

Die erste Zeile zählt Frosttage, die zweite... **was eigentlich?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`df.groupby("Jahr")["TNK"].count()` zählt **alle gemessenen Tage** pro Jahr, nicht die Frosttage. Wer `count()` mit „zählen, was mich interessiert“ verwechselt, bekommt rund 365 „Frosttage“ pro Jahr.

Aber gerade diese zweite Zeile ist wertvoll: 1890 hat nur **132** gemessene Tage, 1891 nur 275. Die Messreihe beginnt am 1. August 1890 — und 1890/91 fehlt ein Winter (Vorlesung 09).

*******************************************************************************

### Typische Fehlvorstellung: Jedes Jahr zählt gleich

> **Typische Fehlvorstellung:** _„Jede Zeile der Ergebnistabelle steht für ein Jahr — also kann ich die Jahre direkt vergleichen.“_

Die Messreihe beginnt im August 1890. Das Jahr 1890 hat 58 Frosttage, 2024 hatte 127.

[( )] 1890 war ein ungewöhnlich milder Winter.
[(X)] 1890 ist mit 2024 nicht vergleichbar.
[( )] Die Daten von 1890 sind falsch.
***
1890 umfasst nur August bis Dezember — 132 Tage, der kalte Jahresanfang fehlt völlig. Eine Gruppe ist nur dann mit anderen vergleichbar, wenn sie auf einer vergleichbaren Datenbasis beruht. Deshalb gehört zu jeder Aggregation die Frage: Aus wie vielen Werten stammt dieser Wert? (`count()` — Vorlesung 11.)
***

### Versuch 2

                                     {{0-1}}
*******************************************************************************

Also: nur vollständige Jahre, und dann pro Jahrzehnt zusammenfassen.

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

jahre = df.groupby("Jahr").agg(frost=("TNK", lambda t: (t < 0).sum()),
                                tage=("TNK", "count"))
voll = jahre[jahre["tage"] >= 360]
print(voll.groupby(voll.index // 10 * 10)["frost"].sum())
```
@Pyodide.eval

Die meisten Jahrzehnte liegen um 1.700 Frosttage — die 2020er nur bei 840, die 1910er sogar bei 746. **Zwei besonders milde Jahrzehnte?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die 2020er haben erst **sechs** Jahre (2020–2025), die 1910er wegen der Lücke nur **vier** vollständige, die 1890er acht. Eine **Summe** hängt davon ab, wie viele Jahre eine Gruppe enthält. Vergleichbar ist das **Mittel** pro Jahr.

`lambda t: (t < 0).sum()` ist übrigens eine kleine Funktion ohne Namen — „nimm die Werte `t` einer Gruppe und zähle die negativen“. Sie dürfen dafür ebenso gut eine Funktion mit `def` schreiben (Vorlesung 07).

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

jahre = df.groupby("Jahr").agg(frost=("TNK", lambda t: (t < 0).sum()),
                                tage=("TNK", "count"))
voll = jahre[jahre["tage"] >= 360]
print(voll.groupby(voll.index // 10 * 10)["frost"].agg(["mean", "count"]).round(1))
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

Das ist das Diagramm aus Vorlesung 01: von rund 190 Frosttagen pro Jahr in den 1900ern auf 140 in den 2020ern. Die Spalte `count` sagt, auf wie vielen vollständigen Jahren jeder Wert beruht — die 1910er auf vier, die 2020er auf sechs.

> Drei Entscheidungen stecken in diesem Ergebnis, und keine davon trifft pandas für Sie: was als Frosttag zählt, welches Jahr vollständig ist, und ob Summe oder Mittel vergleichbar ist.

*******************************************************************************

## Zwei Stationen verbinden

Wie viel kälter ist es auf dem Fichtelberg (1213 m) als in Chemnitz (416 m)? Dazu müssen die Messungen **desselben Tages** nebeneinanderstehen. `merge` verbindet zwei Tabellen über eine gemeinsame Spalte:

```python
import pandas as pd
from pyodide.http import open_url

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/data/"
def lies(pfad):
    return pd.read_csv(open_url(basis + pfad), sep=";",
                       skipinitialspace=True, na_values=-999)

fichtel = lies("fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
chemnitz = lies("chemnitz/produkt_klima_tag_18820101_20251231_00853.txt")
beide = pd.merge(fichtel[["MESS_DATUM", "TMK"]], chemnitz[["MESS_DATUM", "TMK"]],
                 on="MESS_DATUM", suffixes=("_fichtel", "_chemnitz"))

diff = beide["TMK_chemnitz"] - beide["TMK_fichtel"]
print("gemeinsame Tage:", len(beide))
print("Chemnitz im Mittel wärmer um:", round(diff.mean(), 2), "°C")
print("größte Umkehr:", beide.loc[diff.idxmin(), "MESS_DATUM"], diff.min(), "°C")
```
@Pyodide.eval

* `merge(..., on="MESS_DATUM")` behält nur Tage, die in **beiden** Tabellen stehen — Lücken der einen Station fallen automatisch heraus.
* `suffixes` unterscheidet die gleichnamigen Spalten.
* Im Mittel ist Chemnitz knapp **5 °C wärmer** — rund 0,6 °C pro 100 Höhenmeter.
* Am 12. Januar 1964 war es auf dem Gipfel dagegen **11,9 °C wärmer** als in Chemnitz: eine Inversionswetterlage, bei der kalte Luft im Tal liegt. Ein Mittelwert verdeckt solche Tage — der Blick auf die Extreme zeigt sie.

> Dieselbe Technik brauchen wir in Vorlesung 14: Mit Chemnitz als Referenz prüfen wir, ob ein Bruch in der Freiberger Messreihe am Klima liegt oder an der Messung.

## Kontrollfragen

**Skizzieren Sie das Ergebnis.** (Klausurformat)

```python
df = pd.DataFrame({"Station": ["A", "B", "A", "B", "A"],
                   "TMK":     [2.0, 5.0, 4.0, 7.0, 3.0]})
print(df.groupby("Station")["TMK"].agg(["mean", "count"]))
```

<details>
<summary>**Lösung**</summary>

``` text
         mean  count
Station
A         3.0      3
B         6.0      2
```

Eine Zeile pro Gruppe, eine Spalte pro Funktion. A: (2 + 4 + 3) / 3 = 3,0 aus drei Werten; B: (5 + 7) / 2 = 6,0 aus zwei Werten.

</details>

**Was liefert `df.groupby("Jahr")["TNK"].count()`?**

[( )] die Zahl der Frosttage pro Jahr
[(X)] die Zahl der gemessenen Minima pro Jahr
[( )] die Zahl der Jahre
[( )] die Summe der Minima pro Jahr

**Warum ist die Summe der Frosttage pro Jahrzehnt kein guter Vergleich?**

[[X]] Jahrzehnte können unterschiedlich viele (vollständige) Jahre enthalten.
[[ ]] `sum()` überspringt die Frosttage.
[[X]] Das laufende Jahrzehnt ist noch nicht abgeschlossen.
[[ ]] Summen sind bei Temperaturen grundsätzlich verboten.

## Nächste Woche

Heute sind Zahlenkolonnen entstanden — 14 Jahrzehnte, 132 Jahre. Nächste Woche machen wir sie sichtbar: mit **Diagrammen**, die zeigen, was in den Zahlen steckt — und lernen, wann ein Diagramm in die Irre führt.

**Zur Vorbereitung**

- [ ] Berechnen Sie auf Ihrem Rechner die mittlere Zahl der **Sommertage** (Maximum ab 25 °C) pro Jahrzehnt. Welches Jahrzehnt hatte die meisten?
- [ ] Wiederholen Sie die Frosttage pro Jahrzehnt für Chemnitz. Welche Jahrzehnte fehlen — und warum (Vorlesung 09)?
- [ ] Wie viele Tage im Jahr ist es auf dem Fichtelberg im Mittel kälter als 0 °C (Tagesmittel), wie viele in Chemnitz?
