<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  0.1.0
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

* Wie misst ein Ultraschallsensor eine Entfernung?
* Wie wird aus einer Entfernung eine gezählte Person?
* Welche Annahmen stecken im Messprogramm — und wann gehen sie schief?

**Einordnung:** Vorlesung 08, Woche 9 · Werkzeug: Demonstration (nicht prüfungsrelevant)

--------------------------------------------------------------------------------

## Bis hierher kamen alle Daten fertig aus einer Datei

> **Geplant:** Anknüpfung an VL 00/01: der Personenzähler.

## Der Aufbau

> **Geplant:** ESP32 + HC-SR04, Code `examples/00_Einfuehrungsbeispiele/Personenzaehler/personenzaehler.py`. **Vorher:** auf Hardware testen (laut Commit-Nachricht noch ungetestet).

## Live: Wir zählen

> **Geplant:** Messung im Hörsaal, serielle Ausgabe mitschreiben.

## Was schiefgeht

> **Geplant:** Die Tabelle aus der README (Messbereich, Entprellzeit, fehlender Richtungssinn) live nachstellen.

## Die Daten kommen wieder

> **Geplant:** Die heute aufgezeichnete Datei wird im Januar ausgewertet.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `Optional_MikrocontrollerEinfuehrung.md` (Arduino/C++)
* `examples/00_Einfuehrungsbeispiele/Personenzaehler/`

**Offene Punkte**

- [ ] Welche Hardware steht im Hörsaal zur Verfügung?
