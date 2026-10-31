<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.2
language: de
narrator: Deutsch Female

comment:  Demonstration: Ein Mikrocontroller misst, MicroPython steuert ihn — wie Messdaten entstehen und wo sie ihre Fehler herbekommen.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/08_DemoMicroPython.md)

# Demonstration: Datenerhebung mit MicroPython

| Parameter                | Kursinformationen                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                |
| **Semester**             | @config.semester                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                              |
| **Inhalte:**             | `Mikrocontroller, Sensoren, MicroPython, serielle Ausgabe, Messfehler`                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/08_DemoMicroPython.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/08_DemoMicroPython.md) |
| **Autoren**              | @author                                                                                                        |

--------------------------------------------------------------------------------

> [!WARNING]
> **Diese Vorlesung ist in Vorbereitung.** Das Dokument enthält bisher nur die geplante Gliederung.

**Leitfrage:** _Wo kommen die Daten eigentlich her?_

**Fragen an die heutige Veranstaltung ...**

* Wie wird aus einer physikalischen Größe eine Zahl in einer Datei?
* Welche Annahmen stecken in einem Messprogramm — und wann gehen sie schief?
* Warum hat jede Zahl im Datensatz eine Genauigkeit, einen Messort und ein Ausfallrisiko?

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=8" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

**Einordnung:** Vorlesung 08, Woche 9, letzter Termin vor der Weihnachtspause · Werkzeug: Demonstration mit MicroPython · nicht prüfungsrelevant

--------------------------------------------------------------------------------

## Bis hierher kamen alle Daten fertig aus einer Datei

> **Geplant:** Rückblick auf sieben Vorlesungen: Die Fichtelberg-Datei war einfach da. Aber jemand hat das Thermometer aufgestellt, abgelesen, später automatisiert — und in VL 06 haben wir gesehen, dass Lücken, Fehlwerte und Stationswechsel ihre Spuren hinterlassen. Heute stehen wir auf der anderen Seite: Wir erzeugen selbst Messdaten.

## Der Aufbau

> **Geplant:** Mikrocontroller, Sensor, Verbindung zum Rechner. MicroPython als "dieselbe Sprache, andere Hardware": `while True`, Variablen, `if` — alles bekannt.

**Hardware: Arduino Alvik** (entschieden 15.10.2026). Derselbe Roboter zählt in VL 00 an der Hörsaaltür; in VL 08 öffnen wir ihn und sehen, was darin passiert.

<!-- data-type="none" -->
| Was                  | Alvik                                                                                           |
| :------------------- | :---------------------------------------------------------------------------------------------- |
| Rechner              | Arduino Nano ESP32 mit MicroPython; Motoren und Sensoren hängen an einem zweiten Controller        |
| Sensor für die Demo  | Abstandssensor nach vorn (Lichtlaufzeit, 4×4 Felder, davon fünf Frontzonen und oben/unten)        |
| Code                 | liegt vor und ist getestet: `examples/00_Einfuehrungsbeispiele/Alvik/` (`alvik_messung.py`, `alvik_ampel.py`, `zaehler.py`) |
| Verbindung           | USB-Kabel; `mpremote` startet das Programm, die Zeilen kommen als Text am Laptop an               |
| Bezug zum Kurs       | Personenzähler aus VL 00/01: Zählen, Zeitstempel, Richtung                                        |
| Messfehler, belegt   | Zone ohne Ziel behält ihren letzten Wert; Zeilen kommen gepuffert an; zu häufiges Abfragen senkt die Messrate von ~13 auf ~2 pro Sekunde (siehe `Alvik/README.md`) |

## Live: Wir messen

> **Geplant:** Messung während der Vorlesung, Ausgabe über die serielle Schnittstelle als CSV-Zeilen mitschreiben. Die Datei wird anschließend ins Repository gelegt (`data/demo/`).

## Was schiefgeht

> **Geplant:** Die Annahmen im Messprogramm live verletzen und im Datenstrom sichtbar machen. Für den Personenzähler steht die Tabelle in VL 00, Abschnitt _Zurück zum Personenzähler_ (`ANTEIL`, `NACHLAUF_MS`, `MAX_DAUER_MS`, Richtung).
>
> * **Typische Fehlvorstellung: „Ein Sensor misst, was draufsteht.“** — Beim Alvik: Eine Zone ohne Ziel meldet weiter ihren letzten Wert; zwei Personen dicht hintereinander sind eine Zählung.
> * **Typische Fehlvorstellung: „Ein Zeitstempel ist die Zeit des Ereignisses.“** — Beim Alvik kommen die Zeilen gepuffert am Laptop an; die Empfangszeit ist nicht die Messzeit, die Uhr des Roboters zählt nur Millisekunden seit dem Start.

## Die Daten kommen wieder

> **Geplant:** Die heute aufgezeichnete Datei wird im Januar ausgewertet (VL 10/11) — einschließlich der Messfehler, die wir heute erzeugt haben. Rückbezug auf VL 14: Auch der DWD hat Standorte und Geräte gewechselt.

## Ihre Begriffe für die Kurslandkarte

Die [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) wächst mit dem Semester, und Sie bestimmen mit, was hineinkommt. Ihre Antworten sammeln wir im Hörsaal gemeinsam; die Begriffe dieser Woche sind seit Beginn der Vorlesung in der Karte freigeschaltet, und Ihre Vorschläge ergänzen sie.

**Welche Begriffe aus der heutigen Vorlesung gehören für Sie in die Kurslandkarte?**

[[___ ___ ___]]

**Wo könnten Sie das, was heute dran war, in Ihrem Fach anwenden?**

[[___ ___ ___]]

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `Optional_MikrocontrollerEinfuehrung.md` (Arduino/C++): Konzept Mikrocontroller als Datensammler, serielle Schnittstelle
* `examples/00_Einfuehrungsbeispiele/Alvik/` (Messprogramm, Aufstellhilfe, Zähler mit Live-Anzeige, Testbefunde)

**Offene Punkte**

- [x] Hardware festlegen: Arduino Alvik.
- [x] Messprogramm auf dem Alvik testen (15.10.2026, 6 von 6 Durchgängen mit richtiger Richtung).
- [ ] Wie viele Alviks stehen zur Verfügung — reicht es für Gruppen im Hörsaal oder bleibt es bei einer Demo?
- [x] Übertragung in den Hörsaal: USB und `mpremote`, Live-Anzeige mit `zaehler.py --live`.
- [ ] Messfehler, die vorgeführt werden sollen, vorher am Gerät reproduzieren.
- [x] Format der aufgezeichneten Datei: `rohdaten_JJJJ-MM-TT.csv` und `zaehlungen_JJJJ-MM-TT.csv`, Semikolon getrennt.
