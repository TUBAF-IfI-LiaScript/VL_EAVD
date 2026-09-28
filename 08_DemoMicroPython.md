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

* Wie wird aus einer physikalischen Größe eine Zahl in einer Datei?
* Welche Annahmen stecken in einem Messprogramm — und wann gehen sie schief?
* Warum hat jede Zahl im Datensatz eine Genauigkeit, einen Messort und ein Ausfallrisiko?

**Einordnung:** Vorlesung 08, Woche 9, letzter Termin vor der Weihnachtspause · Werkzeug: Demonstration mit MicroPython · nicht prüfungsrelevant

--------------------------------------------------------------------------------

## Bis hierher kamen alle Daten fertig aus einer Datei

> **Geplant:** Rückblick auf sieben Vorlesungen: Die Fichtelberg-Datei war einfach da. Aber jemand hat das Thermometer aufgestellt, abgelesen, später automatisiert — und in VL 06 haben wir gesehen, dass Lücken, Fehlwerte und Stationswechsel ihre Spuren hinterlassen. Heute stehen wir auf der anderen Seite: Wir erzeugen selbst Messdaten.

## Der Aufbau

> **Geplant:** Mikrocontroller, Sensor, Verbindung zum Rechner. MicroPython als "dieselbe Sprache, andere Hardware": `while True`, Variablen, `if` — alles bekannt.

**Offen: Welche Hardware?**

<!-- data-type="none" -->
| Kriterium                   | ESP32 + Ultraschallsensor HC-SR04                            | Calliope mini                                                  |
| :-------------------------- | :----------------------------------------------------------- | :------------------------------------------------------------- |
| Szenario                    | Personenzähler an der Hörsaaltür (README, VL 00/01)          | z. B. Temperatur, Licht oder Bewegung im Hörsaal               |
| Aufbau                      | Verkabelung nötig                                            | Sensoren auf der Platine, sofort einsatzbereit                 |
| Code                        | liegt vor: `examples/00_Einfuehrungsbeispiele/Personenzaehler/personenzaehler.py`, auf Hardware noch **ungetestet** | neu zu schreiben; MicroPython-Unterstützung für das eingesetzte Modell prüfen |
| Bezug zum Datensatz         | Zählen, Entprellen, Zeitstempel                              | Temperatur — direkter Bezug zur Fichtelberg-Reihe              |
| Messfehler zum Vorführen    | Messbereich, Entprellzeit, fehlender Richtungssinn           | z. B. Sensor misst Chip- statt Raumtemperatur, Eigenerwärmung — **am Gerät prüfen** |
| Wiederverwendung            | Studierende haben die Hardware in der Regel nicht            | Calliope ist an vielen Schulen verbreitet, ggf. ausleihbar     |

## Live: Wir messen

> **Geplant:** Messung während der Vorlesung, Ausgabe über die serielle Schnittstelle als CSV-Zeilen mitschreiben. Die Datei wird anschließend ins Repository gelegt (`data/demo/`).

## Was schiefgeht

> **Geplant:** Die Annahmen im Messprogramm live verletzen und im Datenstrom sichtbar machen. Für den Personenzähler steht die Tabelle in der README (Messbereich, Entprellzeit, Richtungssinn).
>
> * **Typische Fehlvorstellung: „Ein Sensor misst, was draufsteht.“** — Beispiele je nach Hardware (Chiptemperatur statt Raumtemperatur; zwei Personen nebeneinander = eine Zählung).
> * **Typische Fehlvorstellung: „Ein Zeitstempel ist die Zeit des Ereignisses.“** — Zeitstempel entsteht beim Empfang am Rechner bzw. beim Schreiben; Verzögerung, Uhr des Controllers ohne Echtzeituhr.

## Die Daten kommen wieder

> **Geplant:** Die heute aufgezeichnete Datei wird im Januar ausgewertet (VL 10/11) — einschließlich der Messfehler, die wir heute erzeugt haben. Rückbezug auf VL 14: Auch der DWD hat Standorte und Geräte gewechselt.

## Material

**Wiederverwendbar aus dem bisherigen Kurs** (Stand vor der Neukonzeption, Commit `21d3061`):

* `Optional_MikrocontrollerEinfuehrung.md` (Arduino/C++): Konzept Mikrocontroller als Datensammler, serielle Schnittstelle
* `examples/00_Einfuehrungsbeispiele/Personenzaehler/` (Arduino- und MicroPython-Fassung)

**Offene Punkte**

- [ ] Hardware festlegen: ESP32 + HC-SR04 oder Calliope mini (oder Ähnliches).
- [ ] Messprogramm auf der gewählten Hardware testen.
- [ ] Übertragung in den Hörsaal klären: Wie kommen die Messwerte live auf den Beamer (serielle Konsole, Thonny, Web-Editor)?
- [ ] Messfehler, die vorgeführt werden sollen, vorher am Gerät reproduzieren.
- [ ] Format der aufgezeichneten Datei festlegen, damit sie in VL 10/11 ohne Umwege ausgewertet werden kann.
