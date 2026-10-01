<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  pandas I: Die DWD-Rohdatei mit read_csv in einer Anweisung einlesen, Spalten auswählen, fehlende Werte als NaN behandeln, filtern und mit Datumsangaben arbeiten.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/a9680241e4/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md)

# pandas I — Einlesen

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `DataFrame, read_csv, Spalten, describe, NaN, count, Filtern, neue Spalten, Datum`                                                                 |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _48.000 Zeilen in einer Anweisung?_

**Fragen an die heutige Veranstaltung ...**

* Was nimmt `read_csv` uns ab, was wir in Vorlesung 06 von Hand gemacht haben?
* Wie wählt man Spalten und Zeilen aus?
* Was ist `NaN` — und warum ist es nicht dasselbe wie null?
* Wie rechnet man mit Datumsangaben?

> Beim ersten Ausführen lädt der Browser pandas nach. Das dauert einige Sekunden.

--------------------------------------------------------------------------------

## Rückblick

Zweimal haben wir die Rohdatei schon gelesen:

<!-- data-type="none" -->
| Vorlesung | Werkzeug       | Aufwand                         | Was fehlte                         |
| :-------- | :------------- | :------------------------------ | :--------------------------------- |
| 06        | `open`, `split` | rund 50 Zeilen                 | alles von Hand                     |
| 10        | `np.loadtxt`   | eine Anweisung                  | Spaltennamen, Fehlwerte            |

In Vorlesung 10 musste man wissen, dass `TMK` die Spalte 13 ist, und `-999` selbst herausfiltern. Heute: **pandas**, die Bibliothek für Tabellen.

## Von der Mühsal zum Werkzeug

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)

print(df.shape)
print(df[["MESS_DATUM", "TNK", "TMK", "TXK"]].head())
```
@Pyodide.eval

Jedes Argument erledigt einen Schritt, den Sie in Vorlesung 06 selbst programmiert haben:

<!-- data-type="none" -->
| Argument                  | erledigt                                         | VL 06                      |
| :------------------------ | :----------------------------------------------- | :------------------------- |
| `sep=";"`                 | Zeilen an den Semikolons zerlegen                | `zeile.split(";")`         |
| (automatisch)             | erste Zeile als Spaltennamen nutzen              | `f.readline()`             |
| `skipinitialspace=True`   | Leerzeichen nach dem Trennzeichen entfernen      | `strip()`                  |
| (automatisch)             | Zahlen als Zahlen erkennen                       | `float(...)`               |
| `na_values=-999`          | Fehlwerte als „kein Wert“ markieren              | `if wert != -999`          |

> Auf Ihrem Rechner schreiben Sie statt `open_url(url)` einfach den Dateinamen: `pd.read_csv("data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt", ...)`.

## Der DataFrame

Das Ergebnis ist ein **DataFrame**: eine Tabelle mit benannten Spalten. Jede Spalte ist eine **Series** — ein NumPy-Array mit Beschriftung.

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)

print(df["TMK"].mean())
print(df["TNK"].min(), df["TXK"].max())
print(df["TMK"].describe())
```
@Pyodide.eval

* `df["TMK"]` wählt eine Spalte **über ihren Namen** — keine Spaltennummer mehr wie in Vorlesung 10.
* `df[["MESS_DATUM", "TNK"]]` (doppelte Klammern) wählt mehrere Spalten und liefert wieder einen DataFrame.
* `describe()` fasst eine Spalte zusammen: Anzahl, Mittel, Streuung, Minimum, Quartile, Maximum.

> Beachten Sie: `df["TMK"].mean()` liefert hier **3,24 °C** — ohne dass wir Fehlwerte herausgefiltert haben. Warum, zeigt der nächste Abschnitt.

## Fehlende Werte: NaN

`na_values=-999` ersetzt beim Einlesen jedes `-999` durch **NaN** („not a number“) — pandas' Zeichen für „kein Wert“. Rechenfunktionen wie `mean()`, `min()` oder `sum()` **überspringen** NaN.

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)

print("Zeilen:", len(df))
print("gemessene Minima:", df["TNK"].count())
print("fehlende Minima:", df["TNK"].isna().sum())
```
@Pyodide.eval

* `len(df)` zählt **Zeilen**, `count()` zählt **Werte** — der Unterschied sind die fehlenden.
* `isna()` liefert eine Maske: `True`, wo ein Wert fehlt.

### Typische Fehlvorstellung: NaN ist null

> **Typische Fehlvorstellung:** _„Wo kein Wert steht, zählt pandas eben null — das ist doch richtig.“_

Erinnern Sie sich an Freiberg 1948 (Vorlesung 06)? Dasselbe mit pandas:

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

jahr1948 = df[df["Jahr"] == 1948]
print("Frosttage:", (jahr1948["TNK"] < 0).sum())
print("Tage mit Messung:", jahr1948["TNK"].count(), "von", len(jahr1948))
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Welche Aussage über Freiberg 1948 ist richtig?

[( )] Es gab keinen Frosttag.
[(X)] Über Frost in Freiberg 1948 lässt sich nichts sagen.
[( )] pandas zeigt einen Fehler an, weil alle Werte fehlen.
***
`NaN < 0` ist `False` — also zählt `(jahr1948["TNK"] < 0).sum()` null Frosttage, ohne Warnung. Erst `count()` zeigt: 0 von 366 Tagen wurden gemessen. pandas macht das Überspringen bequem — aber es ersetzt nicht die Frage, wie viele Werte einem Ergebnis zugrunde liegen.

Faustregel: Zu jeder Zahl gehört die Angabe, aus wie vielen Werten sie stammt.
***

## Auswählen und Filtern

Masken funktionieren wie bei NumPy — und neue Spalten entstehen durch Zuweisung:

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Jahr"] = df["MESS_DATUM"] // 10000

frost2024 = df[(df["Jahr"] == 2024) & (df["TNK"] < 0)]
print("Frosttage 2024:", len(frost2024))
print(df[df["TXK"] >= 30][["MESS_DATUM", "TXK"]])
```
@Pyodide.eval

* `df["Jahr"] = ...` legt eine **neue Spalte** an — für alle 47.595 Zeilen auf einmal.
* `df[maske]` behält die Zeilen, für die die Maske `True` ist.
* 127 Frosttage 2024 — dieselbe Antwort wie in Vorlesung 03 und 10, zum dritten Mal mit einem anderen Werkzeug.
* Nur an **drei** Tagen seit 1890 erreichte das Maximum auf dem Fichtelberg 30 °C.

## Datum

`MESS_DATUM` ist eine Zahl wie `19830727` — und mit Zahlen kann man nicht wie mit Daten rechnen (Vorlesung 09). pandas wandelt die ganze Spalte auf einmal um:

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
df["Datum"] = pd.to_datetime(df["MESS_DATUM"], format="%Y%m%d")

januar = df[df["Datum"].dt.month == 1]
print("Mittel aller Januartage:", round(januar["TMK"].mean(), 2), "°C")
print("aus", januar["TMK"].count(), "Tagen")
```
@Pyodide.eval

`.dt` öffnet die Datumsbestandteile einer Spalte: `.dt.year`, `.dt.month`, `.dt.day`, `.dt.dayofweek`.

## Live Hacking: Die Extremwerte der Messreihe

**Wann war es auf dem Fichtelberg am kältesten — und wann am wärmsten?** Eine einfache Frage. Aber die Rohdatei hat ihre Tücken, und `read_csv` erkennt sie nicht alle von selbst.

> **Live Hacking.** In der Vorlesung lesen wir die Datei schrittweise ein. Die Versuche zeigen, was dabei passiert.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url))
print(df.shape)
```
@Pyodide.eval

47.595 Zeilen — aber nur **eine** Spalte. **Warum?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`read_csv` heißt „comma-separated values“ und erwartet standardmäßig **Kommas**. Die DWD-Datei trennt mit Semikolons. Ohne `sep=";"` landet jede Zeile vollständig in einer einzigen Zelle — wie beim Import in die Tabellenkalkulation ohne Angabe des Trennzeichens (Vorlesung 01).

*******************************************************************************

### Versuch 2

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";")
print(df["TNK"].min())
```
@Pyodide.eval

`KeyError: 'TNK'` — dabei steht `TNK` doch in der Kopfzeile. **Was ist los?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Kopfzeile lautet `…; TMK; UPM; TXK; TNK;…` — mit **Leerzeichen** vor den Namen. Die Spalte heißt also `" TNK"`, nicht `"TNK"`. Ein Blick mit `print(list(df.columns))` hätte es gezeigt. `skipinitialspace=True` entfernt die Leerzeichen nach jedem Trennzeichen.

> **Typische Fehlvorstellung:** _„Eine Spalte heißt so, wie ich sie lese.“_ Für den Rechner zählt jedes Zeichen — auch die unsichtbaren.

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True)
print("kältester Tag:", df["TNK"].min(), "°C")
```
@Pyodide.eval

−999 °C auf dem Fichtelberg. **Was fehlt?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`na_values=-999`. Ohne diese Angabe ist `-999` für pandas eine ganz normale Zahl — und die kleinste der Datei. Derselbe Fehler wie beim Mittelwert in Vorlesung 04 und beim Klimavergleich in Vorlesung 10: Werkzeuge kennen Ihre Daten nicht.

*******************************************************************************

### Versuch 4

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
df = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)

kalt = df["TNK"].idxmin()
warm = df["TXK"].idxmax()
print("kältester Tag:", df.loc[kalt, "MESS_DATUM"], df.loc[kalt, "TNK"], "°C")
print("wärmster Tag: ", df.loc[warm, "MESS_DATUM"], df.loc[warm, "TXK"], "°C")
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

* `idxmin()` liefert die **Zeilennummer** des kleinsten Werts — wie `argmin()` in NumPy und das Muster „Extremwert mit Position“ aus Vorlesung 04.
* `df.loc[zeile, "Spalte"]` holt einen einzelnen Wert über Zeile und Spaltenname.

Am 9. Februar 1956 fiel das Minimum auf −30,4 °C, am 27. Juli 1983 stieg das Maximum auf 30,8 °C.

> Die eigentliche Arbeit in diesem Live Hacking war nicht die Auswertung — die ist eine Zeile. Es war das **richtige Einlesen**. Das ist bei echten Daten fast immer so.

*******************************************************************************

## Kontrollfragen

**Ein DataFrame hat 366 Zeilen, in der Spalte `TNK` fehlen 6 Werte. Was liefern die Ausdrücke?**

[ [366] [360] [6] ]
[ (X)   ( )   ( ) ] `len(df)`
[ ( )   (X)   ( ) ] `df["TNK"].count()`
[ ( )   ( )   (X) ] `df["TNK"].isna().sum()`

**Welche Ausdrücke liefern alle Zeilen mit einem Minimum unter −10 °C im Jahr 1956?**

[[X]] `df[(df["Jahr"] == 1956) & (df["TNK"] < -10)]`
[[ ]] `df[df["Jahr"] == 1956 and df["TNK"] < -10]`
[[ ]] `df["TNK"] < -10`
[[X]] `df[df["Jahr"] == 1956][df[df["Jahr"] == 1956]["TNK"] < -10]`
***
Die erste Form ist die übliche. Die zweite scheitert an `and` (Vorlesung 10). Die dritte liefert nur die Maske, nicht die Zeilen. Die vierte funktioniert, filtert aber umständlich in zwei Schritten.
***

**Welches Argument von `read_csv` fehlt, wenn `df["TMK"].mean()` für die Fichtelberg-Daten etwa 3,0 °C statt 3,24 °C ergibt?**

[( )] `sep=";"`
[( )] `skipinitialspace=True`
[(X)] `na_values=-999`
***
Ohne `na_values` gehen die zehn `-999` als Zahlen in das Mittel ein und ziehen es nach unten. Ohne `sep` oder `skipinitialspace` gäbe es die Spalte `TMK` gar nicht — das Programm würde mit einem Fehler abbrechen statt ein falsches Ergebnis zu liefern.
***

## Nächste Woche

Heute haben wir Zeilen ausgewählt — für **ein** Jahr, **einen** Monat. Nächste Woche fassen wir **alle** Jahre auf einmal zusammen: Aufgabe 3 aus Vorlesung 01, die in der Tabellenkalkulation praktisch aussichtslos war.

**Zur Vorbereitung**

- [ ] Lesen Sie auf Ihrem Rechner die Freiberger Datei mit `pd.read_csv` ein (in einer Zelle mit `# %%`). Wie viele Minima fehlen insgesamt?
- [ ] Bestimmen Sie den kältesten und den wärmsten Tag in Freiberg. Liegen sie am selben Datum wie auf dem Fichtelberg?
- [ ] Wie oft lag das Tagesmittel auf dem Fichtelberg im Juli unter 5 °C?
