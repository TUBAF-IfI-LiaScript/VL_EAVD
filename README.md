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

# Zielstellung der Veranstaltung

+ Grundlegendes Verständnis von (hardwarenaher) Programmierung
+ Elementare Fähigkeiten in der Programmiersprache C
+ Anwendung von Programmiertools im Entwicklungsprozess
+ Systematischer Entwurf von Algorithmen

# Literaturempfehlungen

** Online Kurse**

+ [The GNU C Reference Manual](https://www.gnu.org/software/gnu-c-manual/gnu-c-manual.html)
+ Wolf, J., "C von A bis Z", Rheinwerk Verlag [Link](http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/000_c_vorwort_001.htm#mj764cb3fd439d3b95d1843e7c7d17f235)
+ C Kurs Universität Chemnitz, [Link](https://www.tu-chemnitz.de/urz/archiv/kursunterlagen/C/index.htm)

** Videotutorials **

+ Vorlesung Prof. Dr. Justus Piater, Universität Insbruck 2014 [Link]()
+ Vorlesung ...

** Bücher **

+ Kernighan B.W., Ritchie D.M., "Programmieren in C", Hanser Verlag
+ Prinz P., Crawford T., "C in a Nutshell", O'Reilly


# Vorlesungsinhalte

| Datum      | Inhalt                                |
|:-----------|---------------------------------------|
| 23.10.2018 | [1.  Einführung](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/Einfuehrung.md)    |
| 30.10.2018 | Grundkonzepte der Sprache             |
|            | Variablen und Datentypen              |

# "C ist schwierig zu erlernen"

*"Viele haben bei uns wegen dem Info Grundlagen Modul gewechselt. Allerdings hängt das auch von dir und deinem Talent ab. Das Tempo ist rasant. Jede Art von Vorerfahrung hilft dir eigentlich sehr. Also wenn du noch Zeit hast vorm Studienbeginn, schnapp dir ein gutes Buch zur gelehrten Sprache, und fange schonmal bissl an kleine Sachen zu programmieren."* [Foreneintrag]

*"Wenn Du nicht bereit bist, bei Themen, die Dir nicht liegen, Zeit und Energie zu opfern, um sie zu verstehen - bleib ganz von einem Studium weg."*  [Foreneintrag]
