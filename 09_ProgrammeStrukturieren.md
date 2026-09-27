<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Programme strukturieren: Eigene Module, import und die Brücke zu fremden Bibliotheken.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md)

# Programme strukturieren

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `Module, import, Namensräume, Projektstruktur, Bibliotheken aus der Standardbibliothek`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_ProgrammeStrukturieren.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Wie organisiere ich Code, der wächst?_

**Fragen an die heutige Veranstaltung ...**

* Wie verteilt man Funktionen auf mehrere Dateien?
* Was passiert bei `import`?
* Was ist die Standardbibliothek, und was sind externe Pakete?

**Einordnung:** Vorlesung 09, Woche 10 · Werkzeug: Python nativ; Vorbereitung auf den Wechsel zu Notebooks

--------------------------------------------------------------------------------

## Rückblick

> **Geplant:** Die vier Funktionen aus VL 07 — und die Weihnachtspause dazwischen.

## Live Hacking: Ein eigenes Modul

> **Geplant:** Die Funktionen wandern in `dwd.py`; `import dwd` im Auswerteskript.

## Standardbibliothek

> **Geplant:** `math`, `statistics`, `datetime` (DWD-Datum `18900801` umwandeln).

## Externe Pakete

> **Geplant:** `pip install`, Ausblick: `import pandas` ist dasselbe Prinzip.

## Kontrollfragen

> **Geplant:** Welche Datei wird bei `import dwd` gesucht? Namenskonflikte.

## Nächste Woche

> **Geplant:** Wechsel zu Jupyter Notebooks.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `07_PythonGrundlagen.md`: Abschnitt _Zusätzliche Module einbinden_

**Offene Punkte**

- [ ] Kandidat für Kürzung, falls Zeit fehlt (Module an VL 07 oder VL 10 anhängen).
