<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Notebooks und Bibliotheken: Jupyter als Werkzeug der Exploration, NumPy als erste Bibliothek.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_NotebooksBibliotheken.md)

# Notebooks & Bibliotheken

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `Jupyter Notebook, Zellen, Markdown, NumPy-Arrays, vektorisiertes Rechnen`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_NotebooksBibliotheken.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_NotebooksBibliotheken.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Warum muss ich das Rad nicht neu erfinden?_

**Fragen an die heutige Veranstaltung ...**

* Was unterscheidet ein Notebook von einem Skript?
* Wann ist welches Werkzeug das richtige?
* Was leistet NumPy gegenüber Listen?

**Einordnung:** Vorlesung 10, Woche 11 · Werkzeug: Jupyter Notebooks

--------------------------------------------------------------------------------

## Skript oder Notebook?

> **Geplant:** Begründeter Werkzeugwechsel (VL 00, Abschnitt _Werkzeuge_; README, Prinzip _Klare Werkzeugwahl_).

## Arbeiten mit Zellen

> **Geplant:** Ausführungsreihenfolge, typische Fallen (Zelle nicht neu ausgeführt).

## NumPy

> **Geplant:** Arrays als Kern der Vorlesung (Hinweis darauf steht in VL 05).
>
> * **Typische Fehlvorstellung: „Ein Array ist dasselbe wie eine Liste“** — Vorhersage-Quiz mit `werte * 2` (Liste: wiederholt, Array: verdoppelt), `werte + werte` (aneinanderhängen vs. elementweise addieren), `werte < 0` (Liste: `TypeError`, Array: `[False, True]`), gemischte Typen.
> * Von der Mühsal zum Werkzeug: Zählmuster (VL 03) und Mittelwert (VL 04) gegenüber `(minima < 0).sum()` und `minima.mean()`.
> * Überleitung: Eine pandas-Spalte ist ein Array mit Beschriftung.

## Kontrollfragen

> **Geplant:** Klausurnahe Aufgaben im Stil von VL 02–04.

## Nächste Woche

> **Geplant:** pandas: die ganze Datei in einer Zeile.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `10_DatenAnalyse.md`: Abschnitt _NumPy_
* `notebooks/`
