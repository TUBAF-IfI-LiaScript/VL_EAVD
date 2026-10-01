<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
language: de
narrator: Deutsch Female

comment:  Datenqualität: Freiberg zieht um — gleiche Datei, andere Messung. Dazu Ausblick und Prüfungsvorbereitung.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md)

# Datenqualität, Ausblick, Prüfungsvorbereitung

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `Metadaten, Stationswechsel, Referenzstation, Homogenität, Ausblick, Musteraufgaben`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/14_Datenqualitaet.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Kann ich meinem Ergebnis trauen — und wie geht es weiter?_

**Fragen an die heutige Veranstaltung ...**

* Was verraten Metadaten, was die Daten verschweigen?
* Wie prüft man einen Messreihenbruch mit einer Referenzstation?
* Welche Aufgabentypen kommen in der Klausur?

**Einordnung:** Vorlesung 14, Woche 15 · Werkzeug: Vorlesung im Browser (Pyodide); Übung in Visual Studio Code mit Zellen (`# %%`)

--------------------------------------------------------------------------------

## Freiberg zieht um

> **Geplant:** Niederschlag Freiberg 1945–1993 und ab 2015: 758 mm vs. 668 mm. Klima oder Messung? Material und Zahlen: `data/README.md`.

## Die Metadaten

> **Geplant:** Gerät (Hellmann → PLUVIO → rain[e]H3), Messtag (07 Uhr MOZ → 06 UTC), Betreiber, `QN_6`.

## Die Referenzstation

> **Geplant:** Verhältnis Freiberg/Chemnitz: 1,13 (1976–1987, beide Hellmann) vs. 0,96 (2016–2025). Auch Chemnitz hat Brüche (Umzug 1976).

## Reproduzierbarkeit

> **Geplant:** Kann ich meine eigene Rechnung wiederholen? Skript statt Handarbeit, Rückbezug auf die Notebook-Fehlvorstellung aus VL 10.

## Ausblick

> **Geplant:** Was nach dem Kurs kommt: Bibliotheken, APIs, eigene Projekte.

## Prüfungsvorbereitung

> **Geplant:** Musteraufgaben zu allen Aufgabentypen aus VL 00, Abschnitt _Prüfung_.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `12_Anwendungen.md`: Abschnitte _Klausurvorbereitung_, _Finale Worte_, Teil 2 (Open-Meteo-API) als möglicher Ausblick

**Offene Punkte**

- [ ] `RSF`-Codes (Niederschlagsform) in der DWD-Dokumentation nachschlagen, bevor sie gedeutet werden.
