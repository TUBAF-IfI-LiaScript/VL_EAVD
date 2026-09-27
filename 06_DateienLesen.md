<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Dateien lesen: Die DWD-Rohdatei mit Bordmitteln einlesen — Zeilen zerlegen, Fehlwerte behandeln, Typen umwandeln.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md)

# Dateien lesen

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `open, with, Zeilen lesen, split, strip, Typumwandlung, Fehlwerte, Kopfzeile, Dateien schreiben`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_DateienLesen.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Wie kommen 48.000 Zeilen in mein Programm?_

**Fragen an die heutige Veranstaltung ...**

* Wie öffnet und liest man eine Textdatei?
* Wie zerlegt man eine Zeile in ihre Spalten?
* Was tut man mit Kopfzeile, Leerzeichen und `-999`?
* Wie schreibt man ein Ergebnis in eine neue Datei?

**Einordnung:** Vorlesung 06, Woche 7 · Werkzeug: Python nativ; im Browser weiter mit `open_url`

--------------------------------------------------------------------------------

## Rückblick

> **Geplant:** In VL 03–05 kamen die Werte fertig zerlegt aus einspaltigen Dateien. Heute die echte Datei `produkt_klima_tag_18900801_20251231_01358.txt`.

## Eine Datei öffnen

> **Geplant:** `with open(...) as f:`, zeilenweise lesen, `\n` am Zeilenende. Lokal (Repository-Klon) und im Browser (`open_url`) gegenüberstellen.

## Eine Zeile zerlegen

> **Geplant:** `zeile.split(";")`, `strip()`, Spalten per Index (`TMK` = 13, `TNK` = 16). Kopfzeile überspringen.

## Fehlwerte und Lücken

> **Geplant:** `-999` herausfiltern; die Lücke 1910–1915 bemerken (Datum der Folgezeile prüfen).

## Live Hacking: Das lange Skript

> **Geplant:** Frosttage pro Jahr für alle 135 Jahre — bewusst als ein langes Skript (60–80 Zeilen), das in VL 07 zerlegt wird. **Vorher prüfen:** Umfang für die Folien, Kernausschnitte statt Gesamtcode zeigen.

## Ergebnisse schreiben

> **Geplant:** `open(..., "w")`, eine Ergebniszeile pro Jahr — Grundlage für VL 07.

## Kontrollfragen

> **Geplant:** Welche Spalte liefert `split` für …? Warum fehlt die erste Zeile? Was passiert ohne `strip()`?

## Nächste Woche

> **Geplant:** Das Skript ist lang und unübersichtlich — Funktionen schaffen Ordnung.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `07_PythonGrundlagen.md`: Abschnitt _Ausgabe in Dateien, Lesen aus Dateien_

**Offene Punkte**

- [ ] Freiberg-Datei als Übungsaufgabe („dasselbe für Freiberg“) einplanen.
