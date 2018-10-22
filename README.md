<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

comment:  This is a very simple comment.
          Multiline is also okay.

translation: English   translation/english.md

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s.replace(/\n/g, "<br>");}}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);
    var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
    var info = log[1] + " " + log[4];

    if (info.length > 80)
      info = info.substring(0,76) + "..."

    error.add_detail(0, info, "error", log[2]-1, log[3]);

    throw error;
  }
</script>
@end


-->

# C-Kurs

![C logo](img/logo.png)

See the interactive version at
[https://LiaScript.github.io](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/README.md)

Der vorliegende C-Kurs wurde für das Semester 2018/19 an der TU Bergakademie Freiberg vorbereitet und auf der Basis von LiaScript realisiert. Die Veranstaltung richtet sich an Nicht-Informatiker aus verschiedenen ingenieurwissenschaftlichen Disziplinen mit keinen oder geringen Programmierkenntnissen. Kern der Lösung ist die Möglichkeit Code direkt in der Webseite auszuführen und auch Änderungen vorzunehmen, die dann in einem
"Versionssystem light" verfügbar sind.

Ausführbarer C Code sieht wie folgt aus, der Titel kann weggelassen werden.

```cpp                     HelloWorld.c
#include<stdio.h>

int main() {
	printf("Hello World\\n");
	return 0;
}
```
@JSCPP(@input, )

Das folgende Beispiel illustriert die Übergabe von Argumenten über die "Commandozeile".

```cpp                     GetChar.c
#include<stdio.h>

int main(){
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
@JSCPP(@input,`@input(1)`)

Fehlerausgaben werden entsprechend der Compilerimplementierung wie folgt generiert:

```cpp                     ErroneousHelloWorld.c
#include<stdio.h>

int main() {
	printf("Hello World\n");
	return 0;
}
```
@JSCPP(@input, )

# Prozedurale Programmierung (WS 2018/19)

**Dozenten**

| Name                | Email                                     |
|:--------------------|:------------------------------------------|
|Sebastian Zug        | sebastian.zug@informatik.tu-freiberg.de   |
|Georg Jäger          | georg.jaeger@informatik.tu-freiberg.de    |
|Galina Rudolf        | galina.rudolf@informatik.tu-freiberg.de   |
|Jonas Treumer        | jonas.treumer@informatik.tu-freiberg.de   |
|Ben Lorenz           | ben.lorenz@informatik.tu-freiberg.de      |
|Martin Reinhardt     | martin.reinhardt@informatik.tu-freiberg.de|
|Tobias Bräuer        | tobias.braeuer@student.tu-freiberg.de  |

**Zielstellung der Veranstaltung**

+ Grundlegendes Verständnis von (hardwarenaher) Programmierung
+ Elementare Fähigkeiten in der Programmiersprache C
+ Anwendung von Programmiertools im Entwicklungsprozess
+ Systematischer Entwurf von Algorithmen

**Zeitaufwand und Engagement**

"Der Zeitaufwand beträgt 180h und setzt sich zusammen aus 60h
Präsenzzeit und 120h Selbststudium. Letzteres umfasst die Vor- und
Nachbereitung der Lehrveranstaltungen, die eigenständige Lösung von
Übungsaufgaben sowie die Prüfungsvorbereitung."

# Literaturempfehlungen

**Online Kurse**

+ [The GNU C Reference Manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html)
+ Wolf, J., "C von A bis Z", Rheinwerk Verlag [Link](http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/000_c_vorwort_001.htm#mj764cb3fd439d3b95d1843e7c7d17f235)
+ C Kurs Universität Chemnitz, [Link](https://www.tu-chemnitz.de/urz/archiv/kursunterlagen/C/index.htm)

**Videotutorials**

+ Vorlesung Prof. Dr. Justus Piater, Universität Insbruck 2014 [Link](https://www.youtube.com/watch?v=7P7dSOKAonM)
+ Reihe von Tutorials zu verschiedenen Veranstaltungen der Goethe Universität Frankfurt [Link](https://www.youtube.com/watch?v=CeEfTlRFEA0&t=210s)

**Bücher**

+ Kernighan B.W., Ritchie D.M., "Programmieren in C", Hanser Verlag
+ Prinz P., Crawford T., "C in a Nutshell", O'Reilly


# Vorlesungsinhalte

| Datum      | Inhalt                                |
|:-----------|---------------------------------------|
| 23.10.2018 | [1.  Einführung](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/Einfuehrung.md)    |
| 30.10.2018 | Grundkonzepte der Sprache, Variablen und Datentypen, Ein- und Ausgabe  |
| 06.11.2018 |              |
| 13.11.2018 |              |
| 30.11.2018 |              |
| 27.11.2018 |              |
| 04.12.2018 |              |
| 11.12.2018 |              |
| 18.12.2018 |              |
# ... und wozu brauche ich das?

**Antwort A:** Das Studium vermittelt ein Weltbild und keine eng zugeschnitte Sicht.

**Antwort B:** Die Fähigkeit in Algorithmen zu denken ist eine Grundlage
wissenschaftlichen Arbeitens.

**Antwort C:** Am Ende steht Ihnen das Rüstzeug zur Verfügung kleine
eingebettete C-Projekte selbst anzugehen.

![instruction-set](./img/Example_I_DistanceMeasurements.jpeg)<!-- width="50%" --> US- Distanzsensor

# "C ist schwierig zu erlernen"

*"Viele haben bei uns wegen dem Info Grundlagen Modul gewechselt. Allerdings hängt das auch von dir und deinem Talent ab. Das Tempo ist rasant. Jede Art von Vorerfahrung hilft dir eigentlich sehr. Also wenn du noch Zeit hast vorm Studienbeginn, schnapp dir ein gutes Buch zur gelehrten Sprache, und fange schonmal bissl an kleine Sachen zu programmieren."* [Foreneintrag]

*"Ich habe es grade irgendwie selbst gelöst, aber keine Ahnung warum es funktioniert hat."* [Foreneintrag]

Herausforderungen

+ Abstrakte Denkweise
+ Penible Beachtung der Syntax
+ Ungewohnte Arbeitsmittel

# Wie können Sie zum Gelingen der Veranstaltung beitragen?

+ Stellen Sie Fragen, seinen Sie kommunikativ!
+ Organisieren Sie sich in Arbeitsgruppen!
+ Experimentieren Sie mit verschiedenen Entwicklungsumgebung um "Ihren Editor" zu finden
+ Machen Sie Verbesserungsvorschläge für die Vorlesungsfolien!

![instruction-set](./img/screenShotAtom.png)<!-- width="100%" -->

Link auf den GitHub: https://github.com/liaScript/CCourse

# Und wenn Sie dann immer noch programmieren wollen ...

![instruction-set](./img/BAF_bots.png)<!-- width="80%" -->

# Autorenliste

Sebastian Zug, Georg Jäger, André Dietrich
