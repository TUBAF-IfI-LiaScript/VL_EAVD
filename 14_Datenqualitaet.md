<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Datenqualität: Freiberg zieht um — gleiche Datei, andere Messung. Metadaten, Referenzstation, Reproduzierbarkeit, Ausblick und Prüfungsvorbereitung.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/a9680241e4/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md)

# Datenqualität, Ausblick, Prüfungsvorbereitung

| Parameter                | Kursinformationen                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                              |
| **Inhalte:**             | `Stationswechsel, Metadaten, Referenzstation, Datenqualität prüfen, Reproduzierbarkeit, Ausblick, Musteraufgaben`                              |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md) |
| **Autoren**              | @author                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Kann ich meinem Ergebnis trauen — und wie geht es weiter?_

**Fragen an die heutige Veranstaltung ...**

* Was verraten Metadaten, was die Daten selbst verschweigen?
* Wie prüft man einen Bruch in einer Messreihe mit einer Referenzstation?
* Woran erkennt man ein belastbares — und ein reproduzierbares — Ergebnis?
* Welche Aufgabentypen kommen in der Klausur?

> Beim ersten Ausführen lädt der Browser pandas nach. Das dauert einige Sekunden.

--------------------------------------------------------------------------------

## Rückblick

Im Lauf des Semesters sind wir immer wieder über dieselbe Frage gestolpert: **Stimmt, was das Programm ausrechnet?**

<!-- data-type="none" -->
| Vorlesung | Was schiefging                                  | ohne Fehlermeldung? |
| :-------- | :---------------------------------------------- | :-----------------: |
| 03        | `-999` als Frosttag gezählt                      | ja                  |
| 06        | Freiberg 1948: „0 Frosttage“, weil nicht gemessen | ja                  |
| 08        | Personenzähler: zwei Personen, eine Zählung      | ja                  |
| 10        | 10 Fehlwerte verschieben ein 30-Jahres-Mittel um 1 °C | ja             |
| 12        | 1890 als „mildes Jahr“, weil Monate fehlen       | ja                  |
| 13        | eine Linie über fünf Jahre ohne Daten            | ja                  |

Programme rechnen richtig — mit dem, was man ihnen gibt. Heute der schwierigste Fall: ein Fehler, der in den Daten selbst gar nicht zu sehen ist.

## Freiberg zieht um

Die DWD-Station Freiberg misst den Niederschlag seit 1945. 1993 wurde sie geschlossen, 2015 wieder eröffnet. Dieselbe Stationsnummer 01441, dieselbe Datei, dasselbe Format:

```text produkt_nieder_tag_19450701_20251231_01441.txt
STATIONS_ID;MESS_DATUM;QN_6;  RS; RSF;SH_TAG;NSH_TAG;eor
       1441;19920601;    9;   0.6;   6;   0;   0;eor
       1441;20240601;    9;  14.1;   4;-999;-999;eor
```

`RS` ist die Niederschlagshöhe des Tages in mm.

> **Live Hacking.** Hat sich der Niederschlag in Freiberg verändert? In der Vorlesung entwickeln wir die Auswertung gemeinsam.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/freiberg/produkt_nieder_tag_19450701_20251231_01441.txt")
fb = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
fb["Jahr"] = fb["MESS_DATUM"] // 10000

summe = fb.groupby("Jahr")["RS"].sum()
print("bis 1993:", round(summe[summe.index < 1994].mean()), "mm pro Jahr")
print("ab 2015: ", round(summe[summe.index > 2014].mean()), "mm pro Jahr")
```
@Pyodide.eval

Rund 11 % weniger Niederschlag. **Was haben wir vergessen?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Unvollständige Jahre (Vorlesung 12): 1945 beginnt im Juli, 1993 endet im April, 2015 beginnt im April. Ihre Summen sind viel zu klein und ziehen beide Mittel nach unten.

*******************************************************************************

### Versuch 2

                                     {{0-1}}
*******************************************************************************

```python
import pandas as pd
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
       "data/freiberg/produkt_nieder_tag_19450701_20251231_01441.txt")
fb = pd.read_csv(open_url(url), sep=";", skipinitialspace=True, na_values=-999)
fb["Jahr"] = fb["MESS_DATUM"] // 10000

jahre = fb.groupby("Jahr").agg(mm=("RS", "sum"), tage=("RS", "count"))
voll = jahre[jahre["tage"] >= 360]
print(voll[voll.index < 1994]["mm"].agg(["mean", "count"]).round())
print(voll[voll.index > 2014]["mm"].agg(["mean", "count"]).round())
```
@Pyodide.eval

Immer noch rund 90 mm weniger — 12 %. **Ein Klimasignal?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Rechnung ist jetzt sauber. Aber die Daten allein können die Frage nicht beantworten: Vor und nach der Lücke steht **dieselbe Stationsnummer** — ob dahinter auch dieselbe Messung steht, verrät die Datei nicht. Das verraten die **Metadaten**.

*******************************************************************************

## Die Metadaten

Zu jeder DWD-Station gehören Metadaten-Dateien: Lage, Geräte, Betreiber, Messverfahren. Für Freiberg (im Repository unter `data/freiberg/`):

<!-- data-type="none" -->
| Merkmal          | bis 1993                                         | ab 2015                                            |
| :--------------- | :----------------------------------------------- | :------------------------------------------------- |
| Standort         | 380 m, 13,34° O                                  | 416 m, 13,27° O — rund 5 km weiter westlich         |
| Messgerät        | Hellmann, manuell abgelesen                      | PLUVIO, ab 2020/22 rain[e]H3 (Wägung, elektronisch) |
| Messtag          | 07:00 bis 07:00 Uhr Folgetag (Ortszeit)          | aus der Meldung von 06 UTC                          |
| Betreiber        | Wetterdienst, Meteorologischer Dienst der DDR, DWD | DWD                                               |
| Schneehöhe       | nahezu immer gemessen                            | an 43 % der Tage `-999`                             |

Anderer Ort, anderes Gerät, andere Definition des Messtags. Jedes davon kann die Jahressumme verändern — ohne dass sich am Klima etwas geändert hat.

### Typische Fehlvorstellung: Gleiche Station, gleiche Messung

> **Typische Fehlvorstellung:** _„Dieselbe Stationsnummer und dasselbe Dateiformat bedeuten dieselbe Messung.“_

Was folgt aus den Metadaten für den Rückgang um 12 %?

[( )] Der Niederschlag in Freiberg ist um 12 % gesunken.
[( )] Die Daten nach 2015 sind falsch und sollten verworfen werden.
[(X)] Ohne weiteren Vergleich lässt sich nicht trennen, was Klima und was Messänderung ist.
***
Beide Messreihen sind für sich korrekt — aber sie messen nicht dasselbe. Ein Bruch in einer Messreihe heißt **Inhomogenität**. Ob der Rückgang ein Klimasignal ist, lässt sich mit Freiberg allein nicht entscheiden: Vorher und nachher überschneiden sich nicht. Man braucht eine **Referenz**.
***

## Die Referenzstation

Chemnitz liegt rund 30 km entfernt in ähnlicher Höhe und misst seit 1976 am selben Ort. Wenn sich das **Klima** geändert hat, sollte Chemnitz denselben Rückgang zeigen. Wenn sich nur die **Messung** in Freiberg geändert hat, ändert sich das **Verhältnis** Freiberg zu Chemnitz.

### Versuch 3

```python
import pandas as pd
from pyodide.http import open_url

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/data/"
def jahressummen(pfad, spalte):
    d = pd.read_csv(open_url(basis + pfad), sep=";",
                    skipinitialspace=True, na_values=-999)
    j = d.groupby(d["MESS_DATUM"] // 10000)[spalte].agg(["sum", "count"])
    return j[j["count"] >= 360]["sum"]

fb = jahressummen("freiberg/produkt_nieder_tag_19450701_20251231_01441.txt", "RS")
ch = jahressummen("chemnitz/produkt_klima_tag_18820101_20251231_00853.txt", "RSK")
beide = pd.DataFrame({"freiberg": fb, "chemnitz": ch}).dropna()
beide["verhaeltnis"] = beide["freiberg"] / beide["chemnitz"]

for von, bis in [(1976, 1987), (2016, 2025)]:
    z = beide[(beide.index >= von) & (beide.index <= bis)]
    print(von, "–", bis, z.mean().round(2).to_dict())
```
@Pyodide.eval

Lesen Sie das Ergebnis ab und vergleichen Sie die Zeiträume:

* **Chemnitz** misst in beiden Zeiträumen praktisch gleich viel (712 und 703 mm). Das Klima hat sich beim Niederschlag also kaum verändert.
* **Freiberg** lag von 1976 bis 1987 rund **13 % über** Chemnitz, seit 2016 rund **5 % darunter**.
* Der Rückgang in Freiberg ist deshalb zum großen Teil eine Folge des **Stationswechsels**, nicht des Klimas.

> Warum gerade 1976–1987? In diesem Zeitraum stand die Chemnitzer Station schon am heutigen Ort, und **beide** Stationen maßen mit Hellmann-Geräten. Auch die Referenz muss man prüfen: Chemnitz ist 1976 selbst umgezogen und hat seitdem dreimal das Gerät gewechselt (`data/README.md`).

Genau so arbeitet der DWD bei der **Homogenisierung** von Messreihen: Brüche werden mit Nachbarstationen erkannt und — wo möglich — korrigiert. Wer Rohdaten verwendet, muss das selbst bedenken.

## Kann ich meinem Ergebnis trauen?

Sechs Fragen, die Sie jeder eigenen Auswertung stellen sollten — alle sind uns im Semester begegnet:

<!-- data-type="none" -->
| Frage                                                    | Werkzeug                                 | VL     |
| :------------------------------------------------------- | :--------------------------------------- | :----- |
| Wie sind fehlende Werte kodiert — und habe ich sie ausgeschlossen? | `na_values`, `isna()`              | 03, 11 |
| Fehlen Zeilen ganz?                                      | Datum der Folgezeile, `finde_luecken`    | 06, 09 |
| Aus wie vielen Werten stammt jede Zahl?                  | `count()` neben jedem Mittel             | 11, 12 |
| Sind meine Gruppen vergleichbar?                         | nur vollständige Jahre, Mittel statt Summe | 12   |
| Hat sich die Messung geändert?                           | Metadaten, Referenzstation               | 14     |
| Zeigt meine Grafik, was die Zahlen sagen?                | Achse ab null, Zeitraum nennen, Lücken zeigen | 13 |

## Reproduzierbarkeit

Ein Ergebnis ist **reproduzierbar**, wenn jemand anderes — oder Sie selbst in einem Jahr — mit denselben Daten zum selben Ergebnis kommt.

* **Ein Skript von der Rohdatei bis zum Ergebnis.** Keine Zwischenschritte von Hand in der Tabellenkalkulation, die nirgends dokumentiert sind (Vorlesung 01).
* **Rohdaten nicht verändern.** Bereinigen im Programm, nicht in der Datei.
* **Datenstand festhalten.** Der DWD ergänzt und korrigiert Daten laufend — notieren Sie, wann Sie die Datei abgerufen haben.
* **Von oben nach unten ausführbar.** Ein Skript läuft immer vollständig. Ein Notebook nur dann, wenn man es nach „Restart & Run All“ prüft (Vorlesung 10).

Welche Auswertung ist reproduzierbar?

[( )] Frosttage in der Tabellenkalkulation gezählt, Fehlwerte vorher von Hand gelöscht.
[(X)] Ein Skript liest die Rohdatei, schließt `-999` aus und gibt die Frosttage aus; Datenquelle und Abrufdatum stehen im Kommentar.
[( )] Ein Notebook, dessen Zellen in der Reihenfolge 1, 4, 2, 3 ausgeführt wurden.
***
Nur das Skript lässt sich von jemand anderem genau so wiederholen. In der Tabellenkalkulation ist nicht mehr nachvollziehbar, welche Zeilen gelöscht wurden; im Notebook hängt das Ergebnis von einer Ausführungsreihenfolge ab, die man im fertigen Dokument nicht sieht.
***

## Ausblick

Sie haben in diesem Semester den ganzen Datenkreislauf aus Vorlesung 00 durchlaufen — von der Frage über die Erhebung (Vorlesung 08) bis zur belegten, geprüften Aussage. Was als Nächstes kommen kann:

* **Ihre eigenen Daten:** Analysendaten, Bohrprofile, Pegelstände — dieselben Werkzeuge, andere Spalten.
* **Daten aus dem Netz:** Viele Datenquellen bieten Schnittstellen (APIs), die man direkt aus Python abfragt, etwa aktuelle Wetterdaten.
* **Weitere Bibliotheken:** `scipy` für Statistik und Signalverarbeitung, `seaborn` für Diagramme, `geopandas` für Karten.
* **Ein Überblick über das Semester:** Die [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) zeigt alle Begriffe und wie sie zusammenhängen — gut geeignet, um vor der Prüfung die Fäden noch einmal abzufahren.

> Was Sie mitnehmen sollten, sind weniger die Befehle als die Fragen: Wie sind die Daten entstanden? Was fehlt? Lohnt sich ein Programm? Und kann ich dem Ergebnis trauen?

## Prüfungsvorbereitung

Die Klausur prüft, ob Sie Code **lesen, verstehen, korrigieren und skizzieren** können (Vorlesung 00). Hier zu jedem Aufgabentyp ein Beispiel — bearbeiten Sie es zuerst **auf Papier**.

**1. Welchen Wert gibt das Programm aus?**

```python
werte = [3, -2, 5, -999, -1]
n = 0
s = 0
for w in werte:
    if w != -999 and w < 0:
        n = n + 1
        s = s + w
print(n, s)
```

<details>
<summary>**Lösung**</summary>

`2 -3` — gezählt werden die negativen Werte ohne Fehlwert: −2 und −1.

</details>

**2. Finden Sie alle Fehler.**

```python
def mittelwert(werte)
    summe = 0
    for w in werte:
        summe = summe + w
    print(summe / len(werte))

m = mittelwert([2.5, 3.5])
print("Mittel: " + m)
```

<details>
<summary>**Lösung**</summary>

* Zeile 1: Doppelpunkt fehlt nach `def mittelwert(werte)` (`SyntaxError`).
* Zeile 5: `print` statt `return` — die Funktion gibt `None` zurück (Vorlesung 07).
* Zeile 8: Text und Zahl lassen sich nicht mit `+` verbinden; richtig: `print("Mittel:", m)`.

</details>

**3. Schreiben Sie eine Funktion** `frosttage(minima)`, die die Zahl der Werte unter 0 zurückgibt und Fehlwerte `-999` nicht mitzählt.

<details>
<summary>**Lösung**</summary>

```python
def frosttage(minima):
    anzahl = 0
    for m in minima:
        if m != -999 and m < 0:
            anzahl = anzahl + 1
    return anzahl
```

</details>

**4. Skizzieren Sie das Ergebnis.**

```python
df = pd.DataFrame({"Jahr": [2023, 2024, 2023, 2024],
                   "TNK": [-1.0, 2.0, -3.0, -1.0]})
print(df.groupby("Jahr")["TNK"].agg(["min", "count"]))
```

<details>
<summary>**Lösung**</summary>

``` text
      min  count
Jahr
2023 -3.0      2
2024 -1.0      2
```

</details>

**5. Warum ist diese Darstellung irreführend?** Ein Balkendiagramm vergleicht die Frosttage zweier Jahrzehnte; die y-Achse beginnt bei 130.

<details>
<summary>**Lösung**</summary>

Bei Balken muss die Achse bei null beginnen; sonst ist die Balkenlänge nicht proportional zum Wert, und ein Rückgang um 26 % sieht aus wie einer um 80 % (Vorlesung 13).

</details>

**6. Warum ist `-999` in diesem Datensatz ein Problem?**

<details>
<summary>**Lösung**</summary>

`-999` ist eine Zahl, die „nicht gemessen“ bedeutet. Programme rechnen damit wie mit einem Messwert: Es zählt als Frosttag (`-999 < 0`), verschiebt Mittelwerte stark und erscheint als Minimum. Man muss es ausschließen oder beim Einlesen in `NaN` umwandeln — und dann prüfen, wie viele Werte übrig bleiben.

</details>

> Mehr Übungsmaterial: die Abschnitte _Kontrollfragen_ und _Typische Fehlvorstellung_ jeder Vorlesung — sie sind genau im Klausurformat gestellt.
