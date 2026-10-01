<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Bibliotheken: NumPy als erste Bibliothek — Arrays, elementweises Rechnen, Masken und Fehlwerte; Zellen in VS Code; Jupyter Notebooks lesen können.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/a9680241e4/README.md

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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md)

# Bibliotheken: NumPy

| Parameter                | Kursinformationen                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                              |
| **Inhalte:**             | `NumPy-Arrays, elementweises Rechnen, Masken, Fehlwerte, loadtxt, Zellen mit # %% in VS Code, Jupyter Notebooks lesen`                         |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md) |
| **Autoren**              | @author                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Warum muss ich das Rad nicht neu erfinden?_

**Fragen an die heutige Veranstaltung ...**

* Was leistet NumPy gegenüber Listen?
* Wie zählt, filtert und mittelt man ohne Schleife?
* Wie arbeitet man Schritt für Schritt mit Daten, ohne das Werkzeug zu wechseln?
* Was ist ein Jupyter Notebook — und worauf muss man beim Lesen achten?

> Beim ersten Ausführen lädt der Browser die Bibliothek NumPy nach. Das dauert einige Sekunden.

--------------------------------------------------------------------------------

## Rückblick

Im Herbst haben Sie Muster von Hand gebaut — Zählen, Aufsummieren, Extremwert suchen. Zum Beispiel die Frosttage 2024:

```python
frosttage = 0
for minimum in minima_2024:
    if minimum < 0:
        frosttage = frosttage + 1
```

Diese Muster brauchen fast alle, die mit Messdaten arbeiten. Deshalb hat sie längst jemand gebaut — schneller, geprüft und frei verfügbar. In Vorlesung 09 haben Sie gesehen, wie man fremde Module mit `import` nutzt. Heute die wichtigste Bibliothek für Zahlen: **NumPy**.

## NumPy-Arrays

Ein **Array** ist eine Folge von Werten desselben Typs — ähnlich einer Liste, aber mit einer entscheidenden Eigenschaft: Rechnungen wirken auf **jedes Element**.

```python
import numpy as np

minima = np.array([-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9])

print(minima * 1.8 + 32)      # alle Werte in °F
print(minima.mean())          # Mittelwert
print(minima.min(), minima.argmin())   # Minimum und seine Position
```
@Pyodide.eval

* `import numpy as np` ist die übliche Abkürzung — Sie werden sie in fast jedem Programm sehen.
* `minima * 1.8 + 32` rechnet die Formel für alle sieben Werte auf einmal. Keine Schleife.
* `argmin()` liefert den **Index** des kleinsten Werts — das Muster „Extremwert mit Position“ aus Vorlesung 04 in einem Wort.

### Typische Fehlvorstellung: Ein Array ist eine Liste

> **Typische Fehlvorstellung:** _„Array und Liste sehen gleich aus — also verhalten sie sich auch gleich.“_

```python
import numpy as np

liste = [2.4, -1.8, -3.5]
array = np.array([2.4, -1.8, -3.5])

print(liste * 2)
print(array * 2)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt `print(liste * 2)` aus?

[( )] `[4.8, -3.6, -7.0]`
[(X)] `[2.4, -1.8, -3.5, 2.4, -1.8, -3.5]`
[( )] eine Fehlermeldung
***
Für Listen bedeutet `* 2` „zweimal hintereinander“ — die Liste wird wiederholt. Für Arrays bedeutet es „jeden Wert mal zwei“. Ebenso hängt `liste + liste` zwei Listen aneinander, während `array + array` elementweise addiert.

Merkregel: Listen sind **Behälter**, Arrays sind **Messreihen**.
***

## Zählen und Filtern mit Masken

Ein Vergleich mit einem Array liefert ein Array aus Wahrheitswerten — eine **Maske**:

```python
import numpy as np

minima = np.array([-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9])

frost = minima < 0
print(frost)
print("Frosttage:", frost.sum())
print("Nur Frostwerte:", minima[frost])
```
@Pyodide.eval

* `frost.sum()` zählt die `True`-Werte, denn `True` zählt als 1 und `False` als 0. Das ist das Zählmuster aus Vorlesung 03 in einer Zeile.
* `minima[frost]` behält nur die Werte, an deren Position die Maske `True` ist. Das ist das Sammelmuster aus Vorlesung 05.

Und das ganze Jahr 2024 — zum Vergleich mit Vorlesung 03:

```python
import numpy as np
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
       "VL_EAVD/master/data/fichtelberg/2024_minimum.txt")
minima = np.array(open_url(url).read().split(), dtype=float)

print("Frosttage 2024:", (minima < 0).sum())
```
@Pyodide.eval

> `dtype=float` wandelt beim Anlegen alle Texte in Zahlen um — die Schleife mit `float(wert)` aus Vorlesung 03 entfällt. (`open_url` gibt es wie bisher nur im Browser.)

## Von der Mühsal zum Werkzeug

<!-- data-type="none" -->
| Frage                         | von Hand (Herbst)                    | mit NumPy                     |
| :---------------------------- | :----------------------------------- | :---------------------------- |
| Wie viele Frosttage?          | Zählmuster, VL 03 — 4 Zeilen         | `(minima < 0).sum()`          |
| Mittelwert?                   | Aufsummieren, VL 04 — 5 Zeilen       | `werte.mean()`                |
| Wann war es am kältesten?     | Extremwert mit Position, VL 04       | `minima.argmin()`             |
| Nur die Frostwerte?           | Sammelmuster, VL 05                  | `minima[minima < 0]`          |
| Längste Frostperiode?         | Zustand verfolgen, VL 04             | **keine fertige Funktion**    |

> Die letzte Zeile ist wichtig: Nicht jede Frage hat eine fertige Funktion. Die längste Frostperiode bleibt eine Schleife — und wer die Muster aus dem Herbst kann, schreibt sie. Bibliotheken ersetzen das Denken nicht, sie nehmen Routinearbeit ab.

## Live Hacking: Wie viel wärmer ist es geworden?

Der DWD vergleicht das Klima über **30-jährige Zeiträume**. Wie unterscheidet sich das Tagesmittel auf dem Fichtelberg 1901–1930 von 1991–2020?

NumPy kann die Rohdatei direkt lesen: `np.loadtxt` mit Trennzeichen, übersprungener Kopfzeile und den gewünschten Spalten (`MESS_DATUM` = 1, `TMK` = 13).

> **Live Hacking.** In der Vorlesung entwickeln wir die Auswertung gemeinsam. Die Versuche zeigen die typischen Irrwege.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

```python
import numpy as np
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
zeilen = open_url(url).read().splitlines()
daten = np.loadtxt(zeilen, delimiter=";", skiprows=1, usecols=(1, 13))
jahr, mittel = daten[:, 0] // 10000, daten[:, 1]

alt = jahr >= 1901 and jahr <= 1930
print(mittel[alt].mean())
```
@Pyodide.eval

`ValueError: The truth value of an array … is ambiguous`. **Was ist passiert?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`and` erwartet **einen** Wahrheitswert links und rechts. Ein Array hat aber über 47.000 davon — Python weiß nicht, ob „alle“ oder „irgendeiner“ gemeint ist. Für Masken verknüpft man elementweise mit `&` (und) und `|` (oder), **mit Klammern**:

```python
alt = (jahr >= 1901) & (jahr <= 1930)
```

Die Klammern sind nötig, weil `&` stärker bindet als `>=`.

*******************************************************************************

### Versuch 2

                                     {{0-1}}
*******************************************************************************

```python
import numpy as np
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
zeilen = open_url(url).read().splitlines()
daten = np.loadtxt(zeilen, delimiter=";", skiprows=1, usecols=(1, 13))
jahr, mittel = daten[:, 0] // 10000, daten[:, 1]

alt = (jahr >= 1901) & (jahr <= 1930)
neu = (jahr >= 1991) & (jahr <= 2020)
print("1901–1930:", round(mittel[alt].mean(), 2))
print("1991–2020:", round(mittel[neu].mean(), 2))
```
@Pyodide.eval

Rund 2,3 °C Erwärmung. **Kann das stimmen?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Fehlwerte. In den 9.203 Tagen von 1901 bis 1930 stehen nur **10** Mal `-999` — aber jeder davon zieht das Mittel um rund 0,1 °C nach unten. Zusammen macht das ein ganzes Grad. NumPy rechnet ohne Rückfrage mit `-999` wie mit jeder anderen Zahl.

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

```python
import numpy as np
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt")
zeilen = open_url(url).read().splitlines()
daten = np.loadtxt(zeilen, delimiter=";", skiprows=1, usecols=(1, 13))
jahr, mittel = daten[:, 0] // 10000, daten[:, 1]

gueltig = mittel != -999
alt = (jahr >= 1901) & (jahr <= 1930) & gueltig
neu = (jahr >= 1991) & (jahr <= 2020) & gueltig
print("1901–1930:", round(mittel[alt].mean(), 2), "°C aus", alt.sum(), "Tagen")
print("1991–2020:", round(mittel[neu].mean(), 2), "°C aus", neu.sum(), "Tagen")
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

Rund **1,4 °C** wärmer im Mittel. Und noch etwas steht in der Ausgabe: 1901–1930 stützt sich auf **9.193 Tage**, 1991–2020 auf 10.958. Die Lücke 1911–1914 aus Vorlesung 09 fehlt im älteren Zeitraum — der Vergleich ist trotzdem sinnvoll, aber man sollte es dazuschreiben.

> Drei Zeilen Masken ersetzen drei verschachtelte Schleifen. Aber die beiden entscheidenden Gedanken — Fehlwerte ausschließen, Datenbasis prüfen — nimmt einem keine Bibliothek ab.

*******************************************************************************

## Zellen in Visual Studio Code

Bei der Datenanalyse probiert man Schritt für Schritt: Daten laden, ansehen, filtern, wieder ansehen. Dafür muss man nicht das Werkzeug wechseln. In Visual Studio Code teilt `# %%` eine gewöhnliche `.py`-Datei in **Zellen**:

```python auswertung.py
# %% Daten laden
import numpy as np
daten = np.loadtxt("data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
                   delimiter=";", skiprows=1, usecols=(1, 13))
jahr, mittel = daten[:, 0] // 10000, daten[:, 1]

# %% Erst einmal ansehen
print(daten.shape, jahr.min(), jahr.max())

# %% Klimavergleich
gueltig = mittel != -999
print(mittel[(jahr >= 1991) & (jahr <= 2020) & gueltig].mean())
```

* Über jeder Zelle erscheint „Run Cell“: Sie führt nur diesen Abschnitt aus, das Ergebnis erscheint im interaktiven Fenster.
* Die Datei bleibt ein **normales Skript**: `python auswertung.py` führt alles von oben nach unten aus — genau wie bisher.

> Das ist die Arbeitsweise für die Übungen ab heute. Die Beispiele aus der Vorlesung lassen sich weiterhin eins zu eins übertragen; nur `open_url` ersetzen Sie durch den Dateinamen.

## Exkurs: Jupyter Notebooks lesen

In Projekten und Abschlussarbeiten begegnen Ihnen **Jupyter Notebooks** (`.ipynb`): Code, Ergebnisse, Diagramme und Text in Zellen, oft im Browser. Ein Beispiel liegt im Repository: [`notebooks/numpy_01_intro.ipynb`](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/notebooks/numpy_01_intro.ipynb).

Wir nutzen Notebooks in diesem Kurs nicht als Werkzeug — aber Sie sollten sie lesen können. Und dabei eine Falle kennen.

### Typische Fehlvorstellung: Ein Notebook zeigt, was gerechnet wurde

> **Typische Fehlvorstellung:** _„Was im Notebook von oben nach unten steht, ist das, was gerechnet wurde.“_

Ein Notebook zeigt vor jeder Zelle, als wievielte sie ausgeführt wurde:

``` text
In [1]:  temperatur = 20

In [3]:  temperatur = temperatur + 5

In [2]:  print(temperatur)
         20
```

Welchen Wert hat `temperatur` jetzt im Notebook?

[( )] `20` — so steht es in der Ausgabe
[(X)] `25`
[( )] `30`
***
Die Zellen wurden in der Reihenfolge 1, **2, 3** ausgeführt, nicht von oben nach unten: erst die Zuweisung, dann die Ausgabe (20), zuletzt die Erhöhung. Die Ausgabe `20` ist also veraltet — der aktuelle Wert ist 25. Wer das Notebook von oben nach unten liest, zieht den falschen Schluss.

In einem Notebook bleiben Variablen außerdem erhalten, auch wenn man die Zelle, die sie erzeugt hat, ändert oder löscht. Deshalb gilt: Ein Notebook ist erst dann glaubwürdig, wenn es nach „Restart & Run All“ von oben nach unten dasselbe Ergebnis liefert. In Vorlesung 14 kommen wir darauf zurück.
***

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
import numpy as np
werte = np.array([3, -1, 4, -2])
print((werte > 0).sum(), werte[werte > 0])
```

[( )] `True [3 4]`
[(X)] `2 [3 4]`
[( )] `7 [3 4]`
[( )] `2 [True False True False]`
***
`werte > 0` ist die Maske `[True, False, True, False]`; ihre Summe zählt die `True`-Werte (2). `werte[maske]` behält die Werte an den `True`-Positionen.
***

**Welche Ausdrücke liefern für ein Array `t` die Werte zwischen 0 und 10?**

[[ ]] `t[t > 0 and t < 10]`
[[X]] `t[(t > 0) & (t < 10)]`
[[ ]] `t[t > 0 & t < 10]`
[[ ]] `t[0:10]`
***
Nur die zweite Form ist richtig. `and` funktioniert nicht mit Arrays, ohne Klammern bindet `&` zu stark, und `t[0:10]` liefert die ersten zehn **Positionen**, nicht die Werte zwischen 0 und 10 — Index und Inhalt verwechselt (Vorlesung 05).
***

**Warum ist `mittel.mean()` über die Fichtelberg-Daten falsch?**

<details>
<summary>**Lösung**</summary>

Die Spalte enthält Fehlwerte `-999`, die NumPy wie normale Zahlen mitrechnet. Richtig: `mittel[mittel != -999].mean()`.

</details>

## Nächste Woche

NumPy kennt nur Zahlen ohne Namen: Spalte 13 ist `TMK` — aber das steht nirgends. Nächste Woche lernen Sie **pandas**: Tabellen mit beschrifteten Spalten, in denen `-999` gleich beim Einlesen zu „kein Wert“ wird.

**Zur Vorbereitung**

- [ ] Legen Sie die Datei `auswertung.py` aus dem Abschnitt _Zellen in Visual Studio Code_ im Repository-Ordner an und führen Sie die Zellen einzeln aus.
- [ ] Ergänzen Sie eine Zelle, die den Vergleich für das Tagesminimum `TNK` (Spalte 16) wiederholt. Ist die Erwärmung bei den Minima größer oder kleiner?
- [ ] Wie viele Frosttage hatte der Fichtelberg im Durchschnitt pro Jahr 1901–1930 und 1991–2020? Hinweis: Frosttage zählen, durch die Zahl der Jahre teilen — und an die Lücke denken.
