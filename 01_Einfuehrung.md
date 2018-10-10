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

# Vorlesung I - Einführung

## Fragen an die heutige Veranstaltung ...

* Wie wird ein textuelles Programm in einen ausführbaren Code transformiert?
* Was bedeutet der Begriff Hochsprache, was verbirgt ist ein Assembler?
* Woraus ergibt sich die Aktualität der Sprache C?
* Welche Eigenschaften grenzt C von anderen Programmiersprachen ab?
* Welche Aufgabe hat ein Compiler?
* Wordurch definieren sich verschiedene "Geschmacksrichtungen" im Entwicklungsprozess

## 1. Grundlegendes

### Wie arbeitet ein Rechner eigentlich?

Beispiel: Intel 4004 Architektur (1971) [^1]

![intel](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1190px-4004_arch.svg.png)<!--style="width: 100%"-->

[^1]: Wikipedia Eintrag Intel 4004 (Autor Appaloosa)

### Was heißt das "Maschinensprache"?

Jeder Rechner hat einen spezifischen Satz von Befehlen, die durch "0" und "1"
ausgedrückt werden, die er überhaupt abarbeiten kann.

Speicherauszug den Intel 4004:

    {{0-1}}
| Adresse | Speicherinhalt |
|:--------|:---------------|
| 0000    | 1101 0101      |
| 0002    | 1111 0010      |

    {{1}}
| Adresse | Speicherinhalt | OpCode     | Mneomonik |
|:--------|:---------------|:-----------|:----------|
| 0000    | 1101 0101      | 1101 DDDD  | LD $5     |
| 0002    | 1111 0010      | 1111 0010  | IAC       |


Unterstützung für die Interpretation aus dem Nutzerhandbuch, das das Instruction set beschreibt[^1]:

![instruction-set](./img/4004_Instruction_set.png)<!-- width="100%" -->

[^1]: Intel 4004 Assembler (Quelle: http://e4004.szyc.org/asm.html)

### Aber möchte man so umfangreiche Programme schreiben?

Vorteil - ggf. sehr effizienter Code (Größe, Ausführungsdauer), der gut auf die Hardware abgestimmt ist

Nachteile

* systemspezifische Realisierung
* geringer Abstraktionsgrad, bereits einfache Konstrukte benötigen viele Codezeilen
* weitgehende semantische Analysen möglich

```
Assembler Code                            Fortran

.START ST                                 A:=2;
ST: MOV R1, #2                            FOR I:=1 TO 20 LOOP
    MOV R2, #1                                  A:=A*I;
M1: CMP R2, #20                           END LOOP;
    BGT M2                                PRINT(A);
    MUL R1, R2
    INI R2
    JMP M1
M2: JSR PRINT
.END
```

> Eine höhere Programmiersprache ist eine Programmiersprache zur Abfassung eines
> Computerprogramms, die in **Abstraktion und Komplexität** von der Ebene der
> Maschinensprachen deutlich entfernt ist. ... Die Befehle müssen durch
> **Interpreter oder Compiler** in Maschinensprache übersetzt werden.

https://de.wikipedia.org/wiki/Liste_von_Programmiersprachen

### Compiliervorgang

> Ein **Compiler** (auch Kompiler; von englisch für zusammentragen bzw. lateinisch
> compilare ‚aufhäufen‘) ist ein Computerprogramm, das Quellcodes einer bestimmten
> Programmiersprache in eine Form übersetzt, die von einem Computer (direkter)
> ausgeführt werden kann.

Stufen des Compile-Vorganges[^1]:

![instruction-set](./img/compilerElements.png)<!-- width="100%" -->

[^1]: Abbildung Stufen der Compilierung (Quelle: https://medium.com/@vietkieutie/what-happens-when-you-type-gcc-main-c-2a136896ade3)

## 2. Warum also C?

### Historische Einordnung

Zielrichtung ... Entwicklung eines Betriebssystems

### Eigenschaften von C

* Adressiert Hochsprachenaspekte und Hardwarenähe -> Hohe Geschwindigkeit bei geringer Programmgröße

* Imperative Programmiersprache
{{1}}
> ALTERNATIVE PARAFDIGMEN

* Wenige Schlüsselwörter als Sprachumfang
{{2}}
> Schlüsselwort: Reserviertes Wort, das der Compiler verwendet, um ein Programm zu parsen (z.B. if, def oder while). Schlüsselwörter dürfen nicht als Name für eine Variable gewählt werden

* Große Mächtigkeit
{{3}}
> WAS BEDEUTET MÄCHTIGKEIT

### Heutige Anwendung

Hardwarenahe Programmierung:

* Eingebettete Systeme -> Siehe Beispiel
* Betriebssysteme

Relevanz in der Anwendung[^1]

![instruction-set](../img/TIOBE.png)<!-- width="100%" -->

[^1]: TIOBE Index (Quelle: https://www.informatik-aktuell.de/aktuelle-meldungen/2018/juli/ranking-der-programmiersprachen-java-wieder-ganz-vorne.html)

### "C ist schwierig zu erlernen"


## 3. Erstes C Programm


### "Hello World"

```cpp                     HelloWorld.c
/* That's my first c program
   Karl Klammer, Oct. 2018 */

#include<stdio.h>

int main() {
	printf("Hello World\\n");
	return 0;
}
```
@JSCPP(@input, )

| Zeile | Bedeutung |
|:------|:---------------|
| 1 - 2 | Kommentar, wird vom Präprozessor entfernt |
| 4     | Voraussetzung für das Einbinden von Befehlen der Standardbibliothek hier printf() |


### Ein Wort zu den Formalien

```cpp                     HelloWorld.c
#include<stdio.h>

int main() {
  /* hier steht ein Kommentar */
  int zahl;
  for (zahl=0; zahl<3;  zahl++){
	    printf("Hello World\\n");
  }
	return 0;
}
```
@JSCPP(@input, )

```cpp                     BadHelloWorld.c
#include<stdio.h> int main() /* hier steht ein Kommentar */ {int i;
for (zahl=0; zahl<3;  zahl++){printf("Hello World\n");}
return 0;}
```
@JSCPP(@input, )

* Das *systematische Einrücken* verbessert die Lesbarkeit und senkt damit die Fehleranfälligkeit Ihres Codes!
* Wählen sie *selbsterklärende Variablen- und Funktionsnamen*!
* Nutzen Sie ein *Versionsmanagmentsystem*, wenn Sie ihren Code entwickeln!
* Kommentieren Sie Ihr Vorgehen!

### Gute Kommentare, schlechte Kommentare


### Was tuen, wenn es schief geht?

```cpp                     ErroneousHelloWorld.c
#include<stdio.h>

int main() {
  for (zahl=0; zahl<3;  zahl++){
	    printf("Hello World\\n")
  }
	return 0;
}
```
@JSCPP(@input, )

Methodisches Vorgehen:
* ** RUHE BEWAHREN **
* Lesen der Fehlermeldung
* Verstehen der Fehlermeldung / Aufstellen von Hypothesen
* Systematische Evaluation der Thesen

## 4. Werkzeuge

### Arbeitsumgebung

* Arbeiten mit der LiaScript-Umgebung
* Online-Compiler und Ausführungsumgebungen für C

https://www.onlinegdb.com/online_c_compiler

* Lokale Tool-Chain auf dem eigenen Rechner (Pelles C)
