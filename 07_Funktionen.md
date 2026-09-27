<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Funktionen: Wiederkehrende Schritte benennen, Parameter und Rückgabewerte — das lange Skript aus Vorlesung 06 wird zerlegt.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md)

# Funktionen

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `def, Parameter, return, lokale Variablen, Docstrings, Funktionen testen`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Wie vermeide ich, alles dreimal zu schreiben?_

**Fragen an die heutige Veranstaltung ...**

* Wie definiert und ruft man eine Funktion?
* Was ist der Unterschied zwischen `print` und `return`?
* Warum sind Variablen in einer Funktion "lokal"?
* Wie prüft man, ob eine Funktion richtig rechnet?

**Einordnung:** Vorlesung 07, Woche 8 · Werkzeug: Python nativ

--------------------------------------------------------------------------------

## Rückblick

> **Geplant:** Das lange Skript aus VL 06: dieselben Schritte für Fichtelberg und Freiberg zweimal kopiert.

## Eine Funktion definieren

> **Geplant:** `def ist_frosttag(minimum):` — Muster aus VL 03 als Funktion.

## Parameter und Rückgabewert

> **Geplant:** `return` vs. `print`; mehrere Parameter (`zaehle_unter(werte, grenze)`).

## Lokale Variablen

> **Geplant:** Warum `frosttage` innerhalb der Funktion außen nicht existiert.

## Live Hacking: Zerlegen

> **Geplant:** Das Skript aus VL 06 wird in vier benannte Funktionen zerlegt: `lese_datei`, `zerlege_zeile`, `ist_fehlwert`, `frosttage_pro_jahr`.

## Funktionen prüfen

> **Geplant:** Kleine Testaufrufe mit bekannten Ergebnissen (`assert`).

## Kontrollfragen

> **Geplant:** Ausgabe vorhersagen mit `return` vs. `print`; fehlendes `return` finden.

## Nächste Woche

> **Geplant:** Demonstration: Wie entstehen Messdaten? (VL 08)

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `04_Funktionen.md` (C++; Konzepte Parameter/Rückgabe)
* `08_PythonVertiefung.md`: Abschnitte _Eigene Funktionen_, _Typ-Hinweise für Variablen_

**Offene Punkte**

- [ ] Typ-Hinweise aufnehmen oder weglassen?
