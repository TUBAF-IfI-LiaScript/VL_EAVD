<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Bibliotheken: NumPy als erste Bibliothek, Zellen in VS Code für die Datenanalyse, Jupyter Notebooks lesen können.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md)

# Bibliotheken: NumPy

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `NumPy-Arrays, vektorisiertes Rechnen, Zellen mit # %% in VS Code, Jupyter Notebooks lesen`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_Bibliotheken.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Warum muss ich das Rad nicht neu erfinden?_

**Fragen an die heutige Veranstaltung ...**

* Was leistet NumPy gegenüber Listen?
* Wie arbeitet man Schritt für Schritt mit Daten, ohne das Werkzeug zu wechseln?
* Was ist ein Jupyter Notebook — und worauf muss man beim Lesen achten?

**Einordnung:** Vorlesung 10, Woche 11 · Werkzeug: Vorlesung im Browser (Pyodide); Übung weiter in Visual Studio Code mit `.py`-Dateien

--------------------------------------------------------------------------------

## NumPy

> **Geplant:** Arrays als Kern der Vorlesung (Hinweis darauf steht in VL 05).
>
> * **Typische Fehlvorstellung: „Ein Array ist dasselbe wie eine Liste“** — Vorhersage-Quiz mit `werte * 2` (Liste: wiederholt, Array: verdoppelt), `werte + werte` (aneinanderhängen vs. elementweise addieren), `werte < 0` (Liste: `TypeError`, Array: `[False, True]`), gemischte Typen.
> * Von der Mühsal zum Werkzeug: Zählmuster (VL 03) und Mittelwert (VL 04) gegenüber `(minima < 0).sum()` und `minima.mean()`.
> * Überleitung: Eine pandas-Spalte ist ein Array mit Beschriftung.

## Zellen in Visual Studio Code

> **Geplant:** Für die Datenanalyse ab jetzt Zellen mit `# %%` in einer gewöhnlichen `.py`-Datei: VS Code führt sie einzeln aus und zeigt Diagramme im interaktiven Fenster. Kein Werkzeugwechsel — die Datei bleibt ein Skript, das von oben nach unten läuft (bewusste Entscheidung gegen einen Wechsel zu Notebooks, siehe README, Prinzip _Klare Werkzeugwahl_).

## Exkurs: Jupyter Notebooks lesen

> **Geplant:** Kurz zeigen, was ein Notebook ist, damit Studierende es lesen können, wenn es ihnen in Projekten begegnet — z. B. mit `notebooks/numpy_01_intro.ipynb`.
>
> * **Typische Fehlvorstellung: „Was im Notebook steht, ist das, was gerechnet wurde.“** — Zellen lassen sich in beliebiger Reihenfolge ausführen, Variablen überdauern gelöschte oder geänderte Zellen. Vorhersage-Quiz mit einer Zellfolge, die in anderer Reihenfolge ausgeführt wurde. Rückbezug in VL 14 (Reproduzierbarkeit).

## Kontrollfragen

> **Geplant:** Klausurnahe Aufgaben im Stil von VL 02–04.

## Nächste Woche

> **Geplant:** pandas: die ganze Datei in einer Zeile.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `10_DatenAnalyse.md`: Abschnitt _NumPy_
* `notebooks/numpy_01_intro.ipynb`, `notebooks/numpy_02_image_processing.ipynb` (Bernhard Jung, Januar 2026) — Beispiel für den Exkurs oder Zusatzmaterial
