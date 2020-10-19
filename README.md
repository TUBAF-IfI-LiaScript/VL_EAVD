<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.1
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner

-->

# Vorlesung Prozedurale Programmierung

Der vorliegende C-Kurs wird seit dem Wintersemester 2018/19 an der TU Bergakademie
Freiberg für die Veranstaltung "Prozedurale Programmierung" genutzt und auf der Basis von LiaScript realisiert. Die
Veranstaltung richtet sich an Nicht-Informatiker aus verschiedenen
ingenieurwissenschaftlichen Disziplinen mit keinen oder geringen
Programmierkenntnissen. Kern der Lösung ist die Möglichkeit Code direkt in der
Webseite auszuführen und auch Änderungen vorzunehmen, die dann in einem
"Versionssystem light" verfügbar sind.

Die interaktive Version dieses Kurses ist unter [LiaScript](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/README.md) einz

## Zielstellung

Welche Fähigkeiten sollen in diesem Kurs vermittelt werden? Wir möchten Sie in die Lage versetzen einfache Messaufgaben mit einem Mikrocontroller zu realisieren. Der Schwerpunkt liegt dabei auf der Einführung allgemeiner Programmierkonzepte unter C und C++ und weniger auf der hardwarenahen Programmierung. Dabei bauen wir auf der Hardware und der Tool-Chain des Arduino Projektes auf.

Dabei lernen Sie die Grundlagen

+ imperativer prozeduraler Programmierung anhand von C,
+ objektorientierte Programmierung anhand von C++ sowie
+ die Anwendung dieser beiden Ansätze für eigene kleine Messaufgaben

kennen.

**Beispiele 1 - Blinkende LED**

Mit einiger Erfahrung in C (und C++) lassen sich einfache Mess- und Regelungstechnikaufgaben
sehr einfach automatisieren. Ein Startpunkt dafür ist das Arduino Projekt, dass sowohl eine
entsprechende Hardware, wie auch eine Programmierumgebung bereitstellt.

```cpp        ArduinoHelloWorld.ino
void setup() {      // Konfiguration
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {       // Ausführung
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```


**Beispiel 2 - Ein bisschen realistischer bitte!**

... gut, dass ist noch nicht sonderlich beeindruckend. Vielleicht lässt folgende
Anwendung das Potential etwas deutlicher werden. Lassen Sie uns annehmen, wir
wollen die Lichtsituation an einem bestimmten Punkt vermessen. Dazu verwenden
wir einen Sensor, der mit einem Controller verbunden ist und senden die
gesammelten Daten an den Rechner des Entwicklers.

```cpp        ArduinoReadLightSensor.ino
void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

void loop() {
  // reads the input on analog pin A0 (value between 0 and 1023)
  int analogValue = analogRead(A0);
  Serial.print(analogValue);   // the raw analog reading
  delay(500);
}
```

Wenn wir noch einen Schritt weitergehen können wir die Daten auch an einen Server übergeben. Dieser übernimmt die Aufbereitung und Visualisierung.

<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/856893/charts/7?bgcolor=%23ffffff&color=%23d62020&days=3&dynamic=true&type=line"></iframe>

Hier lassen sich dann die eigentlichen "Untersuchungen" realisieren und zum Beispiel die Frage beantworten, ob die Sonne am Wochenende häufiger scheint.

![Diagramme](./images/00_Readme/AlleWetter.png)<!-- width="70%" -->

Die roten Punkte stellen die Verteilung der Wochenendmessungen der vergangenen Woche dar, während die blauen Kreuze die Wochentage illustrieren. Dunkelheit wird durch einen Wert nahe 1023 ausgedrückt, während helle Messituationen durch kleine Werte dargestellt werden.

> Lust auf mehr?

> Interaktive Session: Wer von Ihnen hat bereits Programmiererfahrung?

## Strukurierung der Veranstaltung

| Nr. | Datum      | Inhalt                            | Link |
|:--- | ---------- | --------------------------------- | ---- |
| 0   | 20.10.2020 | Einführung                        |      |
| 1   |            | Eingabe/Ausgabe, Datentypen       |      |
| 2   |            | Operatoren                        |      |
| 3   |            | Kontrollstrukturen                |      |
| 4   |            | Funktionen & Zeiger               |      |
| 5   |            | Komplexe Datentypen               |      |
| 6   |            | Objektorientierter Programmierung |      |
| 7   |            | Klassen                           |      |
| 8   |            | Vererbung                         |      |


## Organisatorisches

**Dozenten**

| Name            | Email                                                  |
|:--------------- |:------------------------------------------------------ |
| Sebastian Zug   | sebastian.zug@informatik.tu-freiberg.de                |
| Galina Rudolf   | galina.rudolf@informatik.tu-freiberg.de                |
| Nico Sonack     | nico.sonack@student.tu-freiberg.de                     |
| Baldur Paulwitz | baldur-heinrich-eckart.paulwitz@student.tu-freiberg.de |

**Übungen**

Die Übungen vertiefen das erlernte anhand praktischer Programmieraufgaben. Dabei werden zunächst die Grundlagen aus C und C++ vermittelt und dann im Januar kleinere Experimente mit einem Mikrocontroller realisiert.

> Ist jemand noch nicht für die Übungen eingeschrieben?

**Zeitaufwand und Engagement**

Der Zeitaufwand beträgt 180h und setzt sich zusammen aus 60h Präsenzzeit und
120h Selbststudium. Letzteres umfasst die Vor- und Nachbereitung der
Lehrveranstaltungen, die eigenständige Lösung von Übungsaufgaben sowie die
Prüfungsvorbereitung.

Sie müssen, insbesondere wenn Sie noch keine Programmiererfahrung haben, ggf. deutlich mehr Zeit in den Kurs investieren. Dies macht gemeinsam mehr Spaß als allein!

### Vorlesungsmaterialien

Die Vorlesungsunterlagen selbst sind unter

https://github.com/SebastianZug/VL_ProzeduraleProgrammierung

verfügbar. Diese können entweder in der Markdown-Syntax oder als interaktives Dokument betrachtet werden.

> Achtung! Es handelt sich um "lebende" Materialien.

+ der Inhalt wird sich ggf. anhand Ihrer Verbesserungsvorschläge verändern
+ die Dokumente enthalten eine Vielzahl von ausführbarem Code.

### Literatur

**Online Kurse**

* [The GNU C Reference Manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html)
* Wolf, J., _"C von A bis Z"_, Rheinwerk Verlag
  [Link](http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/000_c_vorwort_001.htm#mj764cb3fd439d3b95d1843e7c7d17f235)
* C Kurs Universität Chemnitz,
  [Link](https://www.tu-chemnitz.de/urz/archiv/kursunterlagen/C/index.htm)

**Videotutorials**

* Vorlesung Prof. Dr. Justus Piater, Universität Insbruck 2014
  [YouTube](https://www.youtube.com/watch?v=7P7dSOKAonM)
* Reihe von Tutorials zu verschiedenen Veranstaltungen der Goethe Universität
  Frankfurt [YouTube](https://www.youtube.com/watch?v=CeEfTlRFEA0&t=210s)

**Bücher**

* Kernighan B.W., Ritchie D.M., _"Programmieren in C"_, Hanser Verlag
* Prinz P., Crawford T., _"C in a Nutshell"_, O'Reilly
* Wolf J., _"Grundkurs C"_, Rheinwerk Computing
* Theis T., _"C++ für Einsteiger und Umsteiger"_, Rheinwerk Computing


## ... und wozu brauche ich das überhaupt?

                                 {{0-1}}
*******************************************************************************

**Antwort A:**
Das Studium vermittelt ein Weltbild und keine eng zugeschnittene Sicht.

**Antwort B:**
Die Fähigkeit in Algorithmen zu denken, ist eine Grundlage wissenschaftlichen
Arbeitens.

**Antwort C:**
Am Ende steht Ihnen das Rüstzeug zur Verfügung kleine eingebettete C-Projekte
selbst anzugehen.

*******************************************************************************

## "C und C++ sind schwierig zu erlernen"

> _Viele haben bei uns wegen dem Info-Grundlagenmodul gewechselt. Allerdings_
> _hängt das auch von dir und deinem Talent ab. Das Tempo ist rasant. Jede Art_
> _von Vorerfahrung hilft dir eigentlich sehr. Also wenn du noch Zeit hast vorm_
> _Studienbeginn, schnapp dir ein gutes Buch zur gelehrten Sprache, und fange_
> _schonmal bissl an kleine Sachen zu programmieren._ (Foreneintrag)
>
> _Ich habe es grade irgendwie selbst gelöst, aber keine Ahnung warum es_
> _funktioniert hat. _(Foreneintrag)_

Herausforderungen:

* Abstrakte Denkweise
* Penible Beachtung der Syntax
* Ungewohnte Arbeitsmittel

## Wie können Sie zum Gelingen der Veranstaltung beitragen?

* Stellen Sie Fragen, seinen Sie kommunikativ!

> Hinweis auf OPAL Forum!

* Organisieren Sie sich in Arbeitsgruppen!

> Hinweis auf Repl.it

* Machen Sie Verbesserungsvorschläge für die Vorlesungsfolien!

Link auf den GitHub: https://github.com/SebastianZug/VL_ProzeduraleProgrammierung/

## Und wenn Sie dann immer noch programmieren wollen ...

Dann wartet das TUFbots-Team auf Sie ...

![WALL-E](./images/00_Readme/RoboCup.jpeg)<!--
style="width: 80%; display: block; margin-left: auto; margin-right: auto;" -->

Quelle: _Meisterschaft der Maschinen: RoboCup@Work_, Heise Verlag
