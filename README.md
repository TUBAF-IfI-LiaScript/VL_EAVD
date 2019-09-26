<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/LiaTemplates/Rextester/master/README.md

-->

# C-Kurs

![C logo](img/logo.png)

See the interactive version at
[https://LiaScript.github.io](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/README.md)

Der vorliegende C-Kurs wird seid dem Wintersemester 2018/19 an der TU Bergakademie
Freiberg für die Veranstalutng "Prozedurale Programmierung" genutzt und auf der Basis von LiaScript realisiert. Die
Veranstaltung richtet sich an Nicht-Informatiker aus verschiedenen
ingenieurwissenschaftlichen Disziplinen mit keinen oder geringen
Programmierkenntnissen. Kern der Lösung ist die Möglichkeit Code direkt in der
Webseite auszuführen und auch Änderungen vorzunehmen, die dann in einem
"Versionssystem light" verfügbar sind.

Basis für die Ausführungsumgebung ist die API von Rextester https://rextester.com/. Vielen Dank für diesen Service!

Ausführbarer C Code sieht wie folgt aus, der Titel kann weggelassen werden.

```cpp                     HelloWorld.c
#include <stdio.h>

int main(void) {
	printf("Hello World\n");
	return 0;
}
```
@Rextester.C

Der obligatorische Markdown-Quellcodeblock wird durch um den Makroaufruf `@Rextester.C` am
Ende ergänzt. Dabei können unterschiedliche Compiler (gcc, clang, Microsoft C Compiler) und Parametersets genutzt werden.

```
@Rextester.C
@Rextester.C_clang
@Rextester.C_vc
@Rextester.C(true,`@input(1)`)
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c`)
```

Der zweite Parameter gibt an, ob die Rückgaben der Rextester-Ausführungsumgebung
auf dem Bildschirm angezeigt werden sollen. Der Aufruf des vorhergehenden Code-Samples
mit `@Rextester.C(true, )` generiert eine knappe Statistik der Kompilierung
und der Ausführungsparameter.

```cpp                     HelloWorld.c
#include <stdio.h>

int main(void) {
	printf("Hello World\n");
	return 0;
}
```
@Rextester.C(true, )

Das folgende Beispiel `@Rextester.C(false,`@input(1)`)` illustriert die Übergabe von Argumenten über die "Commandozeile".

```cpp                     GetChar.c
#include <stdio.h>

int main(void){
	char c;
	printf("Mit welchem Buchstaben beginnt ihr Vorname? ");
	c = getchar();
	printf("\nIch weiss jetzt, dass Ihr Vorname mit '%c' beginnt.\n", c);
	return 0;
}
```
``` text                  stdin
T
```
@Rextester.C(false,`@input(1)`)

Fehlerausgaben werden entsprechend der Compilerimplementierung wie folgt generiert:

```cpp                     ErroneousHelloWorld.c
#include <stdio.h>

int main(void) {
	printf("Hello World\n")
	return 0;
}
```
@Rextester.C_clang(true, )

# Prozedurale Programmierung (WS 2019/20)

**Dozenten**

| Name             | Email                                      |
|:-----------------|:-------------------------------------------|
| Sebastian Zug    | sebastian.zug@informatik.tu-freiberg.de    |
| Galina Rudolf    | galina.rudolf@informatik.tu-freiberg.de    |
| Jonas Treumer    | jonas.treumer@informatik.tu-freiberg.de    |
| Alexander Buhl   | alexander.buhl@student.tu-freiberg.de      |

**Zielstellung der Veranstaltung**

* Grundlegendes Verständnis von (hardwarenaher) Programmierung
* Elementare Fähigkeiten in der Programmiersprache C
* Anwendung von Programmiertools im Entwicklungsprozess
* Systematischer Entwurf von Algorithmen

**Zeitaufwand und Engagement**

Der Zeitaufwand beträgt 180h und setzt sich zusammen aus 60h Präsenzzeit und
120h Selbststudium. Letzteres umfasst die Vor- und Nachbereitung der
Lehrveranstaltungen, die eigenständige Lösung von Übungsaufgaben sowie die
Prüfungsvorbereitung.

# Literaturempfehlungen

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

# Vorlesungsinhalte

| Datum      | Inhalt                                                                                                                                                                   |
|:---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 14.10.2018 | [1.  Einführung](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/01_Einfuehrung.md)                                       |

[//]: #  | 30.10.2018 | [2. Variablen und Datentypen, Ein- und Ausgabe](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/02_Grundlagen.md#1)       |
| 06.11.2018 | [3. Operatoren](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/03_Operatoren.md#1)                                       |
| 13.11.2018 | [4. Kontrollstrukturen](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/04_Kontrollstrukturen.md#1)                       |
| 20.11.2018 | [5. Komplexe Datentypen](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/05_ZusammengesetzteDatentypen.md#1)              |
| 27.11.2018 | [6. Funktionen](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/06_Funktionen.md#1)                                       |
| 04.12.2018 | [7. Zeiger](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/07_Zeiger.md#1)                                               |
| 11.12.2018 | [8. Input/Output](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/08_InputOutput.md#1)                                    |
| 18.12.2018 | Ausfall                                                                                                                                                                  |
| 08.01.2019 | [9. Dynamische Speicherverwaltung](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/09_DynamischeSpeicherverwaltung.md#1)  |
| 15.01.2019 | [10. Parameterübergabe und Makros](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/10_MakrosKommandozeilenparameter.md#1) |
| 22.01.2019 | [11. Standardbibliothek](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/11_Standardbibliothek.md#1)                      |
| 29.01.2019 | [12. Algorithmen](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/12_Algorithmen.md#1)                                    |
| 05.02.2019 | [13. Ausblick](https://liascript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/13_Ausblick.md#1)                                          |

# ... und wozu brauche ich das?

**Antwort A:**
Das Studium vermittelt ein Weltbild und keine eng zugeschnitte Sicht.

**Antwort B:**
Die Fähigkeit in Algorithmen zu denken ist eine Grundlage wissenschaftlichen
Arbeitens.

**Antwort C:**
Am Ende steht Ihnen das Rüstzeug zur Verfügung kleine eingebettete C-Projekte
selbst anzugehen.

![US- Distanzsensor](./img/Example_I_DistanceMeasurements.jpeg)<!--
style="width: 50%; display: block; margin-left: auto; margin-right: auto;" -->

Beispielanwendung: Monitoring der Helligkeit und des Noisepegels im Hörsaal

HAVE TO BE ACTIVATED

<iframe width="450" height="260" style="border: 1px solid #cccccc;" src="https://thingspeak.com/channels/596617/charts/1?bgcolor=%23ffffff&color=%23d62020&dynamic=true&results=60&type=line&update=15"></iframe>

# "C ist schwierig zu erlernen"

> Viele haben bei uns wegen dem Info-Grundlagenmodul gewechselt. Allerdings
> hängt das auch von dir und deinem Talent ab. Das Tempo ist rasant. Jede Art
> von Vorerfahrung hilft dir eigentlich sehr. Also wenn du noch Zeit hast vorm
> Studienbeginn, schnapp dir ein gutes Buch zur gelehrten Sprache, und fange
> schonmal bissl an kleine Sachen zu programmieren." _(Foreneintrag)_
>
> Ich habe es grade irgendwie selbst gelöst, aber keine Ahnung warum es
> funktioniert hat. _(Foreneintrag)_

Herausforderungen:

* Abstrakte Denkweise
* Penible Beachtung der Syntax
* Ungewohnte Arbeitsmittel

# Wie können Sie zum Gelingen der Veranstaltung beitragen?

* Stellen Sie Fragen, seinen Sie kommunikativ!
* Organisieren Sie sich in Arbeitsgruppen!
* Experimentieren Sie mit verschiedenen Entwicklungsumgebung um "Ihren Editor"
  zu finden
* Machen Sie Verbesserungsvorschläge für die Vorlesungsfolien!

![Atom IDE Screenshot](./img/screenShotAtom.png)<!-- width="100%" -->

Link auf den GitHub: https://github.com/liaScript/CCourse

# Und wenn Sie dann immer noch programmieren wollen ...

![WALL-E](./img/BAF_bots.png)<!--
style="width: 80%; display: block; margin-left: auto; margin-right: auto;" -->

# Autorenliste

Sebastian Zug, Galina Rudolf, Georg Jäger, André Dietrich, Tobias Bräuer
