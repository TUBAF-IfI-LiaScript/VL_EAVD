<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  pandas I: Die DWD-Rohdatei mit read_csv einlesen, Spalten auswählen, filtern.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md)

# pandas I — Einlesen

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `DataFrame, read_csv, Spalten, Zeilen, Filter, Fehlwerte mit na_values, Datumsangaben`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/11_PandasEinlesen.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _48.000 Zeilen in einer Anweisung?_

**Fragen an die heutige Veranstaltung ...**

* Was nimmt `read_csv` uns alles ab, was wir in VL 06 von Hand gemacht haben?
* Wie wählt man Spalten und Zeilen aus?
* Wie filtert man nach Bedingungen?

**Einordnung:** Vorlesung 11, Woche 12 · Werkzeug: Vorlesung im Browser (Pyodide); Übung in Visual Studio Code mit Zellen (`# %%`)

--------------------------------------------------------------------------------

## Von der Mühsal zum Werkzeug

> **Geplant:** Die rund 50 Zeilen aus VL 06 neben `pd.read_csv(url, sep=";", skipinitialspace=True, na_values=-999)` stellen.

## Der DataFrame

> **Geplant:** `head`, `shape`, `dtypes`, `describe`.

## Fehlende Werte: `NaN`

> **Geplant:** `na_values=-999` macht aus `-999` den Wert `NaN` ("not a number"). `isna()`, `count()` vs. `len()`, `dropna()`.
>
> * **Typische Fehlvorstellung: „`NaN` ist null“** — Rückbezug auf Freiberg 1948 (VL 06): `mean()` und `sum()` überspringen `NaN` stillschweigend; `(df["TNK"] < 0).sum()` zählt für 1948 wieder 0 Frosttage. Abhilfe: gemessene Tage mitzählen (`count()`).

## Auswählen und Filtern

> **Geplant:** `df["TNK"]`, `df[df["TNK"] < 0]`.

## Datum

> **Geplant:** `MESS_DATUM` in ein Datum umwandeln (`pd.to_datetime`).

## Kontrollfragen

> **Geplant:** Klausurnahe Aufgaben im Stil von VL 02–04.

## Nächste Woche

> **Geplant:** Aggregieren: Jahrzehnte zusammenfassen.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `10_DatenAnalyse.md`: Abschnitte _Pandas Grundlagen_, _Noch immer von Excel überzeugt?_

**Offene Punkte**

- [ ] Laden im Browser mit Pyodide: `pd.read_csv` mit URL testen (ggf. über `open_url` + `io.StringIO`).
