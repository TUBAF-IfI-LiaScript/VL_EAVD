<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  pandas II: Gruppieren und Zusammenfassen — Frosttage pro Jahr und pro Jahrzehnt.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md)

# pandas II — Aggregieren

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `groupby, Aggregationsfunktionen, neue Spalten, Zusammenführen zweier Stationen`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_PandasAggregieren.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Wie fasse ich Jahrzehnte zusammen?_

**Fragen an die heutige Veranstaltung ...**

* Wie berechnet man eine Kennzahl pro Gruppe?
* Wie legt man abgeleitete Spalten an?
* Wie verbindet man zwei Datensätze?

**Einordnung:** Vorlesung 12, Woche 13 · Werkzeug: Vorlesung im Browser (Pyodide); Übung in Visual Studio Code mit Zellen (`# %%`)

--------------------------------------------------------------------------------

## Aufgabe 3 aus Vorlesung 01

> **Geplant:** Frosttage pro Jahr in vier Anweisungen — die Aufgabe, die in der Tabellenkalkulation aussichtslos war.

## groupby

> **Geplant:** Pro Jahr, pro Jahrzehnt; `mean`, `sum`, `count`.

## Vollständige Jahre

> **Geplant:** Jahre mit Lücken (1890, 1910–1915) erkennen und ausschließen.

## Zwei Stationen

> **Geplant:** Fichtelberg und Chemnitz über das Datum zusammenführen (`merge`) — Vorbereitung auf VL 14.

## Kontrollfragen

> **Geplant:** Ergebnis eines `groupby` skizzieren (Klausurformat aus VL 00, Abschnitt _Prüfung_).

## Nächste Woche

> **Geplant:** Visualisierung.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `10_DatenAnalyse.md`
