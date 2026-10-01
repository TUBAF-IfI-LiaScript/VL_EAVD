<!--

author:   Sebastian Zug & Bernhard Jung

email:    sebastian.zug@informatik.tu-freiberg.de

version:  2.0.0

language: de

narrator: Deutsch Female

comment: Erhebung, Analyse und Visualisierung digitaler Daten - Einführung in die Programmierung mit Python für Nicht-Informatiker

logo: ./images/Readme/Wetterstation.png

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/README.md)

# Erhebung, Analyse und Visualisierung digitaler Daten

> **Dieser Kurs wird gerade überarbeitet.** Zum Wintersemester 2026/27 bauen wir die Veranstaltung grundlegend um — Inhalte, Reihenfolge und Beispiele können sich noch ändern.
>
> **Stand 01.10.2026:** Vorlesungen 00–07 und 09–14 sind ausgearbeitet, Vorlesung 08 (Demonstration Datenerhebung) liegt als Rumpf vor. Die Materialien des bisherigen Kurses (C++/Python) sind in der Git-Historie erreichbar (Commit `21d3061`).
>
> Hinweise und Fehler gern als [Issue](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/issues).

> Prof. Dr. Sebastian Zug · Prof. Dr. Bernhard Jung
>
> TU Bergakademie Freiberg, Wintersemester 2026/27

Die Veranstaltung führt Studierende aus Nicht-Informatikstudiengängen in die Programmierung mit Python ein — mit einem klaren Ziel: eigene Messreihen und Analysendaten auswerten, von der Rohdatei bis zur belegten Aussage.

**Für Studierende:** Der Einstieg ist die erste Vorlesung, [00 Motivation](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/00_Motivation.md). Dort finden Sie Lernziele, Arbeitsweise, Prüfung und Organisatorisches.

**Kurslandkarte (Entwurf zur Diskussion):** [tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) — Begriffe, Zusammenhänge und didaktische Fäden über das Semester. Quelle und Anleitung: [`kurslandkarte/`](kurslandkarte/README.md).

## Intention

Wissenschaftliche Daten durchlaufen einen Kreislauf aus Frage, Erhebung, Aufbereitung, Analyse, Visualisierung und Dokumentation — und meist mehrere Runden davon. Der Kurs folgt diesem Kreislauf; das Schema fasst CRISP-DM und den Forschungsdatenlebenszyklus in vereinfachter Form zusammen.

Sechs Prinzipien tragen die Konzeption:

<!-- data-type="none" -->
| Prinzip                          | Umsetzung                                                                                          |
| :------------------------------- | :------------------------------------------------------------------------------------------------- |
| **Die Frage kommt zuerst**       | Jede Vorlesung beginnt mit einer Leitfrage an echte Daten; Sprachkonzepte folgen, wenn sie gebraucht werden. |
| **Ein Datensatz, das ganze Semester** | DWD-Klimareihe Fichtelberg (seit 1890, ca. 48.000 Zeilen) — mit Fehlwerten, Lücken, Rohformat. |
| **Erst mühsam, dann mit Werkzeug** | Tabellenkalkulation (VL 01) → eigene Schleifen (VL 03–07) → pandas (VL 11–12) für dieselben Fragen. |
| **Live Hacking**                 | Ab VL 04 entsteht in jeder Sitzung ein Programm live, inklusive Irrwegen. Ein Skript wächst über VL 06 (lang), VL 07 (Funktionen) und VL 09 (Modul). |
| **Typische Fehlvorstellungen**   | Eigene Abschnitte mit Vorhersage-Quiz, angelehnt an [PD4CS](https://www.pd4cs.org/mc-index/) und ergänzt um datenspezifische Fehlvorstellungen. |
| **Klare Werkzeugwahl**           | Blöcke oder Text für Einführungsbeispiele (VL 02–07), Python im Browser (Pyodide) und auf dem Server (CodeRunner) — eins zu eins übertragbar auf den eigenen Rechner. Zum Arbeiten durchgehend Visual Studio Code mit `.py`-Dateien, ab VL 10 mit Zellen (`# %%`). Jupyter Notebooks werden bewusst nicht als Werkzeug eingeführt (zusätzliches Denkmodell, versteckter Zustand), sondern nur zum Lesen vorgestellt. |

Die Prüfung ist schriftlich. Geübt wird deshalb vor allem das Lesen, Vorhersagen und Korrigieren von Code.

## Zeitplan

Vorlesung montags; Vorlesungszeit 19.10.–18.12.2026 und 04.01.–12.02.2027.

<!-- data-type="none" -->
| Termin | VL | Thema                                         | Phase                        |
| :----- | :- | :-------------------------------------------- | :--------------------------- |
| 19.10. | [00](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/00_Motivation.md) | Motivation, Organisation                      | Einstieg                     |
| 26.10. | [01](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/01_VomProblemZumProgramm.md) | Vom Problem zum Programm                      | Einstieg                     |
| 02.11. | [02](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/02_ErsteSchritte.md) | Erste Schritte in Python                      | Einstieg                     |
| 09.11. | [03](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/03_PruefenUndWiederholen.md) | Prüfen und Wiederholen                        | Grundlagen am Datensatz      |
| 16.11. | [04](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/04_MusterInMessreihen.md) | Muster in Messreihen                          | Grundlagen am Datensatz      |
| 23.11. | [05](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/05_DatenSammeln.md) | Daten sammeln                                 | Grundlagen am Datensatz      |
| 30.11. | [06](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/06_DateienLesen.md) | Dateien lesen                                 | Grundlagen am Datensatz      |
| 07.12. | [07](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/07_Funktionen.md) | Funktionen                                    | Grundlagen am Datensatz      |
| 14.12. | [08](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/08_DemoMicroPython.md) | Demonstration: Datenerhebung mit MicroPython  | Zäsur: Wo Daten herkommen    |
| 04.01. | [09](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/09_ProgrammeStrukturieren.md) | Programme strukturieren                       | Grundlagen am Datensatz      |
| 11.01. | [10](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/10_Bibliotheken.md) | Bibliotheken: NumPy                           | Datenanalyse                 |
| 18.01. | [11](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/11_PandasEinlesen.md) | pandas I — Einlesen                           | Datenanalyse                 |
| 25.01. | [12](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/12_PandasAggregieren.md) | pandas II — Aggregieren                       | Datenanalyse                 |
| 01.02. | [13](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/13_Visualisierung.md) | Visualisierung                                | Datenanalyse                 |
| 08.02. | [14](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/14_Datenqualitaet.md) | Datenqualität, Ausblick, Prüfungsvorbereitung | Datenanalyse                 |

> Die Demonstration (VL 08) ist bewusst der letzte Termin vor Weihnachten: Nach sieben Vorlesungen mit fertigen Dateien sehen die Studierenden, wie Messdaten entstehen. Die dabei aufgezeichneten Daten kommen im Januar als Analysebeispiel zurück. VL 09 schließt die Grundlagen ab und bereitet mit eigenen Modulen den Schritt zu fremden Bibliotheken vor.

## Datensätze

Alle Messreihen liegen unter [`data/`](data/README.md), mit Quellen, Lizenz (DWD, CC BY 4.0) und bekannten Lücken:

* **Fichtelberg** (Station 01358) — roter Faden, Tageswerte 1890–2025
* **Freiberg** (01441) — lokales Beispiel; Klimawerte 1945–1993, Niederschlag bis heute
* **Chemnitz** (00853) — Referenzstation

> **Beispiel für Vorlesung 14: Freiberg zieht um.** Die DWD-Station Freiberg misst Niederschlag bis 1993 und wieder ab 2015 — unter derselben Nummer, im selben Dateiformat, aber an einem anderen Ort, mit anderem Gerät und anderer Definition des Messtags. Die mittlere Jahressumme (vollständige Jahre) fällt von 754 mm auf 664 mm. Hat sich das Klima geändert? Die Nachbarstation Chemnitz sagt: nein. Ihre Jahressumme bleibt praktisch gleich, nur das Verhältnis Freiberg/Chemnitz springt von 1,13 (1976–1987) auf 0,95 (2016–2025).

## Was sich geändert hat

Die Veranstaltung wurde zum Wintersemester 2026/27 grundlegend überarbeitet.

<!-- data-type="none" -->
| Bisher                             | Neu                                           |
| :--------------------------------- | :-------------------------------------------- |
| C++ (Phase 1) und Python (Phase 2) | Python durchgängig                            |
| Datenanalyse ab der 13. Vorlesung  | Echte Daten ab der ersten Vorlesung           |
| Sprachkonzepte als Lehrplan        | Fachliche Fragen als Lehrplan                 |
| Konstruierte Übungsbeispiele       | Ein realer Datensatz durch das ganze Semester |
| Mikrocontroller als eigener Strang | Eine Demonstration zur Datenerhebung          |

> Der Verzicht auf C++ ist die weitreichendste Änderung. Ursprünglich zielte die Veranstaltung darauf ab, den Bogen von der Datenerhebung mit Mikrocontrollern bis hin zur Analyse dieser Informationen zu spannen. Das Ziel bleibt erhalten, wir konzentrieren uns dafür aber auf eine Sprache — Python.

Die Materialien des bisherigen Kurses sind in der Git-Historie erreichbar (Stand vor der Neukonzeption: Commit `21d3061`).
