<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Daten sammeln: Listen anlegen, füllen, indizieren und durchlaufen — bis zum wärmsten Tag jedes Jahres.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md)

# Daten sammeln

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `Listen, append, Index und Slices, len, range, parallele Listen, Dictionary (Ausblick)`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/05_DatenSammeln.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Welches war auf dem Fichtelberg der wärmste Tag jedes Jahres?_

**Fragen an die heutige Veranstaltung ...**

* Wie legt man eine Liste an und füllt sie Schritt für Schritt?
* Wie greift man auf einzelne Werte und Bereiche zu?
* Wie hält man zusammengehörige Werte (Datum und Temperatur) beisammen?
* Wie sammelt man ein Ergebnis pro Jahr?

**Einordnung:** Vorlesung 05, Woche 6 · Werkzeug: Python nativ, Beispiele wahlweise als Blöcke oder Text

--------------------------------------------------------------------------------

## Rückblick

> **Geplant:** Bisher: Listen nur als fertige Werte (`[-1.9, -2.4, ...]`) oder aus `text.split()`. Heute bauen wir sie selbst auf.

## Listen anlegen und füllen

> **Geplant:** `[]`, `append`, `len`. Beispiel: nur die Frosttage einer Woche in eine neue Liste übernehmen (Filtern).

## Zugriff über den Index

> **Geplant:** `liste[0]`, `liste[-1]`, Slices `liste[0:7]` (erste Woche). Anknüpfen an `datum[0:4]` aus VL 02. Typischer Fehler: `IndexError`.

## Zahlenfolgen mit `range`

> **Geplant:** Aus VL 04 hierher verschoben: `range(n)`, `range(a, b)`, Endwert nicht enthalten. `for i in range(len(liste))` als Brücke zwischen Index und Wert.

## Zusammengehörige Werte

> **Geplant:** Parallele Listen `daten` und `maxima` aus zwei Dateien in `data/fichtelberg/` (Format wie `2024_minimum.txt`). Wärmster Tag 2024 = 26,9 °C am 13. August. Ausblick: Dictionary `{jahr: maximum}`.

## Ein Ergebnis pro Jahr

> **Geplant:** Leitfrage: wärmster Tag jedes Jahres. Benötigt Jahresdateien — **offen:** entweder einspaltige Dateien je Jahr vorbereiten oder die Leitfrage auf wenige Jahre beschränken. Vollständig lösbar erst nach VL 06.

## Kontrollfragen

> **Geplant:** Index-Rechnungen im Kopf (`liste[-2]`, `liste[2:5]`), `append` in der Schleife vs. davor, `IndexError` finden.

## Nächste Woche

> **Geplant:** Die Rohdatei selbst einlesen.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `03_ArrayZeigerReferenzen.md` (C++-Arrays; nur Konzept Index)
* `07_PythonGrundlagen.md`: Abschnitte _Alles ist ein Objekt_, _Negative Indices und Slices_, _Schleifen oder List Comprehension_

**Offene Punkte**

- [ ] Datenbasis für „jedes Jahr“ vor VL 06 klären (siehe Abschnitt _Ein Ergebnis pro Jahr_).
- [ ] Dictionary hier nur anreißen oder vollständig einführen?
