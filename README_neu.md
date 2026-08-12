<!-- 

author:   Sebastian Zug & Bernhard Jung

email:    sebastian.zug@informatik.tu-freiberg.de

version:  2.0.0

language: de

narrator: Deutsch Female

comment: Erhebung, Analyse und Visualisierung digitaler Daten - Einführung in die Programmierung mit Python für Nicht-Informatiker

logo: ./images/Readme/Wetterstation.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/liaScript/mermaid_template/master/README.md
        https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
        https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

@style
.flex-container {
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    gap: 20px;
}

.flex-child {
    flex: 1;
    margin-right: 20px;
}

@media (max-width: 600px) {
    .flex-child {
        flex: 100%;
        margin-right: 0;
    }
}

.eavd-person {
    border-left: 3px solid #999;
    padding: 0.2rem 0 0.2rem 0.9rem;
}

.eavd-note {
    border-left: 3px solid #999;
    padding: 0.2rem 0 0.2rem 0.9rem;
    font-size: 0.94rem;
    margin: 1.2rem 0;
}
@end

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/README_neu.md)

# Herzlich willkommen!

-------------------------------------------------------------------------------

<h3>
Vorlesung _Prozedurale Programmierung / Einführung in die Informatik_
</h3>

-------------------------------------------------------------------------------

<div class="flex-container">
<div class="flex-child eavd-person">

**Prof. Dr. Sebastian Zug**

Professur für Softwareentwicklung
und Robotik

sebastian.zug@informatik.tu-freiberg.de

</div>
<div class="flex-child eavd-person">

**Prof. Dr. Bernhard Jung**

Professur für Virtuelle Realität
und Multimedia

bernhard.jung@informatik.tu-freiberg.de

</div>
</div>

-------------------------------------------------------------------------------

> TU Bergakademie Freiberg, Wintersemester 2026/27


> [!CAUTION]
> Dieses Dokument beschreibt die Neukonzeption der Veranstaltung und dient der internen Abstimmung. Es ersetzt die bisherige <code>README.md</code> erst nach Freigabe.


# Die Grundidee

Die Veranstaltung richtet sich an Studierende aus Nicht-Informatikstudiengängen. Sie
werden in Ihrer fachlichen Praxis Messreihen auswerten, Analysendaten sortieren
und Ergebnisse darstellen müssen. Genau darauf zielt dieser Kurs.

Wissenschaftliche Daten durchlaufen dabei ein bestimmtes Muster:

``` ascii
      ┌──────────────────────── neue Frage ──────────────────────────────┐
      │                                                                  │
      ▼                                                                  │
  ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐   ┌───────┐  │
  │ FRAGE │──▶│ ERHE- │──▶│ AUFBE-│──▶│ ANALY-│──▶│ VISUA-│──▶│ DOKU- │──┘
  │       │   │ BUNG  │   │ REITEN│   │  SE   │   │ LISIE-│   │ MENTA-│
  └───────┘   └───────┘   └───────┘   └───────┘   │ RUNG  │   │ TION  │
                                                  └───────┘   └───────┘
  Hypothese   Messen      Fehlwerte   Rechnen     Diagramm    Nachvoll-
  Messgröße   Sammeln     Einheiten   Vergleichen Karte       ziehbar
  Methodik    Speichern   Ausreißer   Zusammen-   Tabelle     machen
                                      fassen
```
<!-- style="font-size: 0.75em; line-height: 1.2;" -->

> **Der Pfeil zurück ist der wichtigste.** Fast nie führt der erste Durchlauf
> zum Ziel: Die Daten reichen nicht, die Frage war zu unscharf, oder das
> Ergebnis wirft eine neue Frage auf. Auswerten heißt, diese Schleife mehrfach
> zu drehen.

Der Name der Veranstaltung nennt drei dieser Schritte — **Erhebung**, **Analyse**
und **Visualisierung**. Die übrigen kommen nicht zu kurz: Ohne klare Frage weiß
niemand, was zu messen ist, und ohne Dokumentation ist ein Ergebnis nicht
überprüfbar.

> Das Schema fasst zwei etablierte Prozessmodelle zusammen:
>
> + **CRISP-DM** _(Cross-Industry Standard Process for Data Mining, 1999)_ —
>   sechs Phasen, ausdrücklich als Kreislauf angelegt, bis heute das
>   meistgenutzte Modell der Datenanalyse
> + **Forschungsdatenlebenszyklus** — Planen, Erheben, Aufbereiten, Analysieren,
>   Publizieren, Archivieren, Nachnutzen
>
> Wir nutzen eine vereinfachte Fassung: ohne Archivierung und ohne
> wirtschaftliche Begriffe, dafür mit den Vorlesungen an den passenden Stellen.

# Lernziele

                                     {{0-1}}
*******************************************************************************

Am Ende des Semesters können Sie eine wissenschaftliche Fragestellung auf eine
Datenverarbeitung abbilden — von der Rohdatei bis zur belegten Aussage.

Im Einzelnen:

| Sie können ...            | Konkret heißt das                                                                                          |
| :------------------------ | :--------------------------------------------------------------------------------------------------------- |
| **entwickeln**            | eine vollständige Auswertung selbst schreiben — einlesen, bereinigen, auswerten, darstellen                  |
| **beurteilen**            | einschätzen, ob ein Ergebnis belastbar ist, und erkennen, wann eine Darstellung in die Irre führt            |
| **analysieren**           | fremden Code lesen und nachvollziehen, was er tut — auch wenn Sie ihn nicht selbst geschrieben haben         |
| **anwenden**              | die Werkzeuge der Datenanalyse auf eigene Messreihen und Analysendaten übertragen                            |
| **verstehen**             | erklären, was hinter den Bausteinen steckt: Schleife, Bedingung, Funktion, Modul, Objekt                    |
| **erinnern**              | die Grundbegriffe benennen: Algorithmus, Datentyp, Bibliothek, Fehlwert                                     |


*******************************************************************************

                                     {{1-2}}
*******************************************************************************

> [!NOTE]
> **Drei Fähigkeiten, die über den Kurs hinaus tragen**
>
> 1. **Sie erkennen, wann sich Programmieren lohnt** — und wann eine
>    Tabellenkalkulation genügt. Beides zu wissen ist mehr wert, als eine
>    Sprache zu kennen.
> 2. **Sie können Ergebnisse hinterfragen** — die eigenen und die anderer. Woher
>    kommen die Daten, was fehlt darin, was trägt die Aussage wirklich?
> 3. **Sie können sich selbst weiterhelfen** — Fehlermeldungen lesen,
>    Dokumentation nutzen, Beispiele übertragen. Kein Kurs deckt ab, was Sie
>    später brauchen werden.


> **Was ausdrücklich nicht das Ziel ist:** Sie werden keine Software-Entwickler.
> Sie werden Fachleute, die programmieren können, wenn es ihre Arbeit
> voranbringt.

*******************************************************************************

# Methodik innerhalb der Vorlesung

![](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHoweDZpaXN5ODhxaGJ4NHRxYnhuYnIyNnc0dXE4ZDE4YjRtZ2QxZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/wcgn5fVDjvR7pdvz4C/giphy.gif)

## 1. Die fachliche Frage kommt zuerst

Klassische Programmierkurse arbeiten die Sprache ab: Datentypen, Schleifen,
Funktionen, Objekte — und ganz am Ende, wenn noch Zeit ist, die Anwendung. Wir
drehen das um.

Jede Vorlesung beginnt mit einer Frage an einen echten Datensatz. Die
Sprachkonzepte kommen dann, wenn man sie zur Beantwortung braucht.

``` text
statt:    "Heute beschäftigen wir uns mit Schleifen."
sondern:  "Wir müssen 27.000 Zeilen eines Datensatzes durchgehen. Wie machen wir das?"
                              ↓
                     Dafür gibt es Schleifen.
```

> Der Unterschied ist nicht kosmetisch. Wer weiß, *wozu* ein Konzept dient,
> behält es. Wer es als Vokabel lernt, vergisst es nach der Klausur.

## 2. Ein Datensatz durch das ganze Semester

Als roter Faden dient eine **Klimamessreihe des Deutschen Wetterdienstes** aus
dem Erzgebirge — Tageswerte über mehrere Jahrzehnte, frei verfügbar, mit allen
Widrigkeiten realer Daten.

Derselbe Datensatz, wachsende Werkzeuge:

| Woche | Was wir damit tun                                       | Womit          |
| ----- | :------------------------------------------------------ | :------------- |
| 3     | Eine Zeile lesen und prüfen: War es ein Frosttag?        | `if`           |
| 4     | Ein Jahr durchlaufen und mitteln                         | `for`          |
| 6     | Die Rohdatei einlesen — mit Fehlwerten und Umlauten      | Dateizugriff   |
| 11    | Alle Jahre gruppieren und vergleichen                    | `pandas`       |
| 13    | Einen Klimatrend belegen — und seine Grenzen benennen    | Statistik      |

                                     {{1-2}}
*******************************************************************************

> [!TIP]
> Dass dieser Datensatz "schmutzig" ist, ist kein Nachteil, sondern der Punkt. An sauberen Datensätzen lernt man nichts über Datenanalyse.

**Warum ein echter, schmutziger Datensatz?**

```text produkt_wetter_tag.txt
STATIONS_ID;MESS_DATUM;QN_4;NEBEL;GEWITTER;STURM_6; TAU;eor
       1684;18800101;-999;-999;-999;-999;-999;-999;eor
       1684;20181230;  10;   0;   0;   0;   1;   0;eor
```

Fehlwerte als `-999`. Semikolon als Trenner, aufgefüllt mit Leerzeichen. Eine
`eor`-Spalte am Zeilenende. Datumsangaben ohne Trennzeichen.

*******************************************************************************

## 3. Fachbeispiele aus Ihren Disziplinen

Der Wetterdatensatz trägt die Methodik. Die fachliche Verankerung leisten
Datensätze aus den beteiligten Disziplinen — Analysendaten aus der Mineralogie,
Bohrprofile und Korngrößenverteilungen aus der Geologie, Messreihen zur
Wasser- und Luftqualität aus dem Umweltingenieurwesen.

> **Der entscheidende Punkt:** Zeitreihe, Probentabelle, Verteilung — alle diese
> Formen werden mit denselben Werkzeugen bearbeitet. Sie lernen ein Werkzeug und
> sehen es in vier fachlichen Gestalten.


## 4. Grafisches Verständnis

                                     {{0-1}}
*******************************************************************************

In jeder Vorlesungsgruppe sitzen Studierende, die noch nie eine Zeile Code
gesehen haben, neben solchen mit Vorerfahrung. Deshalb stehen die Beispiele der Einstiegsphase in **zwei Ansichten zur Wahl** —
als Blöcke zum Zusammenschieben oder als Text zum Tippen.

> **Entscheidend:** Das sind nicht zwei Sprachen, sondern zwei Ansichten auf
> dasselbe Programm. Wer Blöcke verschiebt, sieht daneben den Python-Code
> mitwachsen. Wer Python tippt, sieht die Blöcke mitwandern.

*******************************************************************************

                                     {{1-3}}
*******************************************************************************

Hier die Aufgabe aus Vorlesung 03: Eine Woche mit Tagestemperaturen, gezählt
werden sollen die **Frosttage**.

> Nutzen Sie die Schaltflächen über dem Editor, um zwischen **Blöcken** und
> **Text** zu wechseln. Beide zeigen dasselbe Programm. Ändern Sie etwas in einer
> Ansicht und sehen Sie zu, wie die andere nachzieht.

```` @BlocklyId(frosttage, runner=frosttage hideRunner height=380)
# Gemessene Tagestemperaturen einer Januarwoche
temperaturen = [2.4, -1.8, -3.5, 0.7, -0.2, 1.9, -4.1]

frosttage = 0

for temperatur in temperaturen:
    if temperatur < 0:
        frosttage = frosttage + 1

print("Frosttage in dieser Woche:", frosttage)
````

```python
# runner: frosttage
```
@Pyodide.eval

> **Ausprobieren:** Ändern Sie die Bedingung von `< 0` auf `< 2`. Wie viele Tage
> werden jetzt gezählt? Und warum ist das keine sinnvolle Definition mehr?

*******************************************************************************

                                     {{2-3}}
*******************************************************************************

**Was in diesem kleinen Beispiel schon alles steckt**

| Element                     | Vorlesung |
| :-------------------------- | :-------- |
| Liste von Messwerten        | VL 05     |
| Schleife über alle Werte    | VL 04     |
| Bedingung mit Vergleich     | VL 03     |
| Zähler hochzählen           | VL 04     |
| Ausgabe des Ergebnisses     | VL 02     |

> Ersetzen Sie die sieben Werte durch 27.000 Zeilen aus einer echten Datei, und
> Sie stehen bei Vorlesung 06. Genau das ist der Weg durch dieses Semester.

*******************************************************************************

## 5. Live Hacking

Ab der vierten Vorlesung entsteht in jeder Sitzung ein Programm vor Ihren Augen —
inklusive Irrwegen, Fehlermeldungen und Korrekturen.

> Programmieren ist ein Prozess, kein Ergebnis. Fertiger Code auf einer Folie
> verschweigt genau den Teil, den Sie lernen müssen.

Ein Beispiel wächst dabei über drei Vorlesungen mit:

``` text
VL 06:  ein langes, unübersichtliches Skript
            ↓  wird live zerlegt
VL 07:  vier benannte Funktionen
            ↓  wandern live in eine eigene Datei
VL 08:  ein wiederverwendbares Modul
```

Codequalität wird so nicht als Vorschrift behauptet, sondern als Verbesserung
erlebt.

## 6. Werkzeuge mit klarer Rollenteilung

| Zeitraum        | Werkzeug                        | Wofür es steht                         |
| :-------------- | :------------------------------ | :------------------------------------- |
| Woche 1 – 9     | Python nativ (Editor, Terminal) | Automatisierung, wiederholbare Abläufe |
| Woche 10 – 15   | Jupyter Notebooks               | Exploration, Analyse, Bericht          |

--{{1}}--
Der Wechsel erfolgt bewusst nach der Weihnachtspause und wird begründet.
Notebooks sind das reale Werkzeug der Datenauswertung, Skripte das der
Automatisierung. Wer beides kennt, kann wählen.

## 7. Von der Mühsal zum Werkzeug

Das didaktische Rückgrat des Kurses ist eine bewusste Reihenfolge: **erst
mühsam selbst, dann elegant mit Werkzeug.**

In Woche 6 lesen Sie die Rohdatei mit Bordmitteln ein. Das kostet 60 bis 80
Zeilen und ist unangenehm. In Woche 11 tut dasselbe eine einzige Zeile:

```python
df = pd.read_csv(datei, sep=";", na_values=-999, parse_dates=["MESS_DATUM"])
```

> Wer den mühsamen Weg gegangen ist, versteht, *was* diese Zeile abnimmt.
> Wer ihn übersprungen hat, hält sie für Magie — und steht hilflos da, sobald
> sie einmal nicht funktioniert.

Dasselbe Prinzip trägt den Einstieg: In der **ersten Vorlesung** lösen Sie
Aufgaben mit einer Tabellenkalkulation. Die erste ist leicht, die zweite mühsam,
die dritte praktisch aussichtslos. In **Woche 12** erledigen wir genau diese
dritte Aufgabe in vier Zeilen Code.

# Ablauf des Semesters

Vorlesungszeit: **19.10.2026 – 18.12.2026** und **04.01.2027 – 12.02.2027**

### Phase 0 — Motivation

| Nr. | Woche | Inhalt                     | Leitfrage                              |
| :-- | :---- | :------------------------- | :------------------------------------- |
| 01  | 1     | Warum programmieren?       | Wo hört die Tabellenkalkulation auf?   |
| 02  | 2     | Erste Schritte in Python   | Wie sage ich dem Rechner, was er tun soll? |

### Phase 1 — Grundlagen am Datensatz

> Werkzeug: Python nativ — Editor, Terminal, `.py`-Dateien

<!-- data-type="none" -->
| Nr. | Woche | Inhalt                   | Leitfrage an die Daten                      |
| :-- | :---- | :----------------------- | :------------------------------------------ |
| 03  | 3     | Entscheidungen           | An wie vielen Tagen gab es Frost?           |
| 04  | 4     | Wiederholungen           | Wie warm war es im Mittel 2020?             |
| 05  | 5     | Daten sammeln            | Welches war der wärmste Tag jedes Jahres?   |
| 06  | 6     | Dateien lesen            | Wie kommen 27.000 Zeilen in mein Programm?  |
| 07  | 7     | Funktionen               | Wie vermeide ich, alles dreimal zu schreiben? |
| 08  | 8     | Programme strukturieren  | Wie organisiere ich Code, der wächst?       |

> Ab Vorlesung 04 gehört in jede Sitzung ein Live Hacking von etwa 20 Minuten.

### Zäsur — Wo Daten herkommen

| Nr. | Woche | Inhalt                                        |
| :-- | :---- | :-------------------------------------------- |
| —   | 9     | **Demonstration: Datenerhebung mit MicroPython** |


Der Veranstaltungstitel beginnt mit *Erhebung*. Diese Sitzung zeigt, was das
bedeutet: Ein Mikrocontroller misst, MicroPython steuert ihn — dieselbe Sprache,
andere Hardware.

Die dabei aufgezeichneten Daten kommen im Januar als Analysebeispiel zurück.

> Die Sitzung ist **nicht prüfungsrelevant**. Sie ist bewusst vor die
> Weihnachtspause gelegt.

### Phase 2 — Datenanalyse

> Werkzeug: Jupyter Notebooks

<!-- data-type="none" -->
| Nr. | Woche | Inhalt                     | Leitfrage an die Daten                     |
| :-- | :---- | :------------------------- | :----------------------------------------- |
| 09  | 10    | Notebooks & Bibliotheken   | Warum muss ich das Rad nicht neu erfinden?  |
| 10  | 11    | pandas I — Einlesen        | 27.000 Zeilen in einer Zeile?               |
| 11  | 12    | pandas II — Aggregieren    | Wie fasse ich Jahrzehnte zusammen?          |
| 12  | 13    | Visualisierung             | Wie zeige ich, was ich gefunden habe?       |
| 13  | 14    | Datenqualität & Auswertung | Kann ich meinem Ergebnis trauen?            |
| 14  | 15    | Die ganze Pipeline         | Was habe ich gelernt — und was kommt danach? |

# Prüfung

Die Veranstaltung schließt mit einer **schriftlichen Prüfung** ab.

Das hat eine Konsequenz, die wir offenlegen: Eine Klausur prüft nicht, ob Sie eine Analyse *bauen* können, sondern ob Sie Code **lesen, verstehen, korrigieren und skizzieren** können. Darauf bereiten wir gezielt vor.

| Kompetenz                        | Wie sie geübt wird                                    |
| :------------------------------- | :---------------------------------------------------- |
| Code lesen und Ergebnis vorhersagen | Kurzes "Was tut dieser Code?" in jeder Vorlesung ab 04 |
| Fehler finden                    | Live Hacking mit echten Irrwegen                       |
| Code auf Papier schreiben        | Übungsaufgaben ohne Rechner, Schwerpunkt Phase 1       |
| Konzepte erklären                | Skizzenaufgaben, Schwerpunkt Phase 2                   |

**Was in der Klausur vorkommt**

+ _Welchen Wert gibt das folgende Programm in Zeile x aus?_
+ _Finden Sie alle syntaktischen und logischen Fehler im nachfolgenden Code._
+ _Schreiben Sie eine Funktion, die ..._
+ _Was macht `groupby` mit dieser Tabelle? Skizzieren Sie das Ergebnis._
+ _Warum ist diese Darstellung irreführend?_
+ _Warum ist `-999` in diesem Datensatz ein Problem?_

**Was nicht vorkommt**

+ Auswendig gelernte Bibliothekssyntax
+ Inhalte der Mikrocontroller-Demonstration

Die letzte Vorlesungswoche enthält eine explizite Prüfungsvorbereitung mit Musteraufgaben.

# Was sich geändert hat

Die Veranstaltung wurde zum Wintersemester 2026/27 grundlegend überarbeitet.

| Bisher                             | Neu                                           |
| :--------------------------------- | :-------------------------------------------- |
| C++ (Phase 1) und Python (Phase 2) | Python durchgängig                            |
| Datenanalyse ab der 13. Vorlesung  | Echte Daten ab der ersten Vorlesung           |
| Sprachkonzepte als Lehrplan        | Fachliche Fragen als Lehrplan                 |
| Konstruierte Übungsbeispiele       | Ein realer Datensatz durch das ganze Semester |
| Mikrocontroller als eigener Strang | Eine Demonstration zur Datenerhebung          |

> Der Verzicht auf C++ ist die weitreichendste Änderung. Ursprünglich zielte die Veranstaltung darauf ab den Bogen von der Datenerhebung mit Mikrocontrollern bis hin zu Analyse dieser Informationen zu spannen. Das Ziel bleibt zwar erhalten, gleichwohl fokussieren wir uns auf eine Sprache - Python.