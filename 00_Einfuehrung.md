<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.1
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/Pyodide

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/00_Einfuehrung.md)


# Einführung

| Parameter                 | Kursinformationen                                                                                                                                                                                      |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Veranstaltung:**        | `Vorlesung Prozedurale Programmierung`                                                                                                                                                                 |
| **Semester**              | `Wintersemester 2021/22`                                                                                                                                                                               |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                      |
| **Inhalte:**              | `Vorstellung des Arbeitsprozesses`                                                                                                                                            |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/00_Einfuehrung.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/00_Einfuehrung.md) |
| **Autoren**               | @author                                                                                                                                                                                                |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Welche Aufgabe erfüllt eine Programmiersprache?
* Erklären Sie die Begriffe Compiler, Editor, Programm, Hochsprache!

---------------------------------------------------------------------

##  Wie arbeitet ein Rechner eigentlich?

{{0-1}}
Programme sind Anweisungslisten, die vom Menschen erdacht, auf einem Rechner zur
Ausführung kommen. Eine zentrale Hürde ist dabei die Kluft zwischen menschlicher
Vorstellungskraft und Logik, die **implizite Annahmen und Erfahrungen**
einschließt und der **"stupiden" Abarbeitung von Befehlsfolgen** in einem
Rechner.

{{0-1}}
Programmiersprachen bemühen sich diese Lücke zu schließen und werden dabei von
einer Vielzahl von Tools begleitet, diesen **Transformationsprozess**
unterstützen sollen.

{{0-1}}
Um das Verständnis für diesen Vorgang zu entwickeln werden zunächst die Vorgänge
in einem Rechner bei der Abarbeitung von Programmen beleuchtet, um dann die
Realisierung eines Programmes mit C zu adressieren.

{{0-1}}
![instruction-set](./images/00_Einfuehrung/Programmiersprache_Umfeld.png "Erzeugung von Programmcode [^Programmerstellung]")<!-- width="80%" -->

[^Programmerstellung]: Programmiervorgang und Begriffe(Autor VÖRBY, https://commons.wikimedia.org/wiki/File:Programmiersprache_Umfeld.png

{{1-2}}
Beispiel: Intel 4004-Architektur (1971)

{{1-2}}
![intel](./images/00_Einfuehrung/4004_arch.svg.png"Intel 4004 Architekturdarstellung [^Intel4004]")<!-- style="width: 80%; display: block; margin-left: auto; margin-right: auto;"-->

[^Intel4004]: Autor Appaloosa, Intel 4004, https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1190px-4004_arch.svg.png

{{2}}
Jeder Rechner hat einen spezifischen Satz von Befehlen, die durch "0" und "1"
ausgedrückt werden, die er überhaupt abarbeiten kann.

{{2}}
Speicherauszug den Intel 4004:

{{2}}
<!-- data-type="none" -->
| Adresse | Speicherinhalt | OpCode     | Mnemonik  |
|:--------|:---------------|:-----------|:----------|
| 0010    | 1101 0101      | 1101 DDDD  | LD $5     |
| 0012    | 1111 0010      | 1111 0010  | IAC       |

{{3}}
Unterstützung für die Interpretation aus dem Nutzerhandbuch, dass das _Instruction Set_ beschreibt:

{{3}}
![instruction-set](./images/00_Einfuehrung/4004_Instruction_set.png)<!-- width="100%" -->

{{3}}
Quelle: [Intel 4004 Assembler](http://e4004.szyc.org/asm.html)

### Programmierung

Möchte man so Programme schreiben?

**Vorteil:** ggf. sehr effizienter Code (Größe, Ausführungsdauer), der gut auf die
Hardware abgestimmt ist

**Nachteile:**

* systemspezifische Realisierung
* geringer Abstraktionsgrad, bereits einfache Konstrukte benötigen viele Codezeilen
* weitgehende semantische Analysen möglich

**Beispiel**

```asm @output
 Assembler Code    |  Fortran
                   |
 .START ST         |  A:=2;
 ST: MOV R1, #2    |  FOR I:=1 TO 20 LOOP
     MOV R2, #1    |      A:=A*I;
 M1: CMP R2, #20   |  END LOOP;
     BGT M2        |  PRINT(A);
     MUL R1, R2    |
     INI R2        |
     JMP M1        |
 M2: JSR PRINT     |
 .END              |
```

{{1}}
> Eine höhere Programmiersprache ist eine Programmiersprache zur Abfassung eines
> Computerprogramms, die in **Abstraktion und Komplexität** von der Ebene der
> Maschinensprachen deutlich entfernt ist. Die Befehle müssen durch
> **Interpreter oder Compiler** in Maschinensprache übersetzt werden.

{{2}}
> Ein **Compiler** (auch Kompiler; von englisch für zusammentragen bzw.
> lateinisch compilare ‚aufhäufen‘) ist ein Computerprogramm, das Quellcodes
> einer bestimmten Programmiersprache in eine Form übersetzt, die von einem
> Computer (direkter) ausgeführt werden kann.

{{2}}
Stufen des Compile-Vorganges:

{{2}}
![instruction-set](./images/00_Einfuehrung/compilerElements.png "Stufen der Compilierung [^Compiliation]")<!-- width="80%" -->

[^Compiliation]: Jimmy Thong, Oct 13, 2016, What happens when you type GCC main.c, https://medium.com/@vietkieutie/what-happens-when-you-type-gcc-main-c-2a136896ade3


### Einordnung von C und C++

* Adressiert Hochsprachenaspekte und Hardwarenähe -> Hohe Geschwindigkeit bei
  geringer Programmgröße
* Imperative Programmiersprache

                                 {{1}}
  > **imperative (befehlsorientierte) Programmiersprachen**: Ein Programm
  > besteht aus einer Folge von Befehlen an den Computer. Das Programm
  > beschreibt den Lösungsweg für ein Problem (C, Python, Java, LabView,
  > Matlab, ...).
  >
  > **deklarative Programiersprachen**: Ein Programm beschreibt die
  > allgemeinen Eigenschaften von Objekten und ihre Beziehungen
  > untereinander. Das Programm beschreibt zunächst nur das Wissen zur Lösung
  > des Problems (Prolog, Haskal, SQL, ...).


* Wenige Schlüsselwörter als Sprachumfang

                                  {{2}}
  > **Schlüsselwort** Reserviertes Wort, das der Compiler verwendet, um ein
  > Programm zu parsen (z.B. if, def oder while). Schlüsselwörter dürfen nicht
  > als Name für eine Variable gewählt werden

* Große Mächtigkeit

                                  {{3}}
  > Je "höher" und komfortabler die Sprache, desto mehr ist der Programmierer
  > daran gebunden, die in ihr vorgesehenen Wege zu beschreiten.

## Erstes C Programm

![instruction-set](./images/00_Einfuehrung/helloWorldFromRitchie.png)<!-- width="90%" -->

Quelle: [Brian_Kernighan, Programming in C: A Tutorial  1974](http://www.lysator.liu.se/c/bwk-tutor.html#simple-c)

### "Hello World"


```cpp                     HelloWorld.c
// That's my first C program
// Karl Klammer, Oct. 2018

#include<stdio.h>

int main(void) {     // alternativ "int main()"
	printf("Hello World");
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

| Zeile | Bedeutung                                                                                   |
|:----- |:------------------------------------------------------------------------------------------- |
| 1 - 2 | Kommentar (wird vom Präprozessor entfernt)                                                  |
| 4     | Voraussetzung für das Einbinden von Befehlen der Standardbibliothek hier `printf()`         |
| 6     | Einsprungstelle für den Beginn des Programmes                                               |
| 6 - 9 | Ausführungsblock der `main`-Funktion                                                        |
| 7     | Anwendung einer Funktion ... `name(Parameterliste)` ... hier zur Ausgabe auf dem Bildschirm |
| 8     | Definition eines Rückgabewertes für das Betriebssystem                                      |


### Ein Wort zu den Formalien

```cpp                     HelloWorld.c
// Karl Klammer
// Print Hello World drei mal

#include <stdio.h>

int main() {
  int zahl;
  for (zahl=0; zahl<3;  zahl++){
	    printf("Hello World! ");
  }
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


```cpp                     BadHelloWorld.c
#include <stdio.h>
int main() {int zahl; for (zahl=0; zahl<3;  zahl++){ printf("Hello World! ");} return 0;}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

                                  {{1}}
* Das *systematische Einrücken* verbessert die Lesbarkeit und senkt damit die
  Fehleranfälligkeit Ihres Codes!
* Wählen sie *selbsterklärende Variablen- und Funktionsnamen*!
* Nutzen Sie ein *Versionsmanagmentsystem*, wenn Sie ihren Code entwickeln!
* Kommentieren Sie Ihr Vorgehen trotz "Good code is self-documenting"

### Gute Kommentare

*1. Kommentare als Pseudocode*

```cpp
/* loop backwards through all elements returned by the server
(they should be processed chronologically)*/
for (i = (numElementsReturned - 1); i >= 0; i--){
    /* process each element's data */
    updatePattern(i, returnedElements[i]);
}
```

*2. Kommentare zur Datei*

```cpp
// This is the mars rover control application
//
// Karl Klammer, Oct. 2018
// Version 109.1.12

int main(){...}
```

*3. Beschreibung eines Algorithmus*

```cpp
/* Function:  approx_pi
 * --------------------
 * computes an approximation of pi using:
 *    pi/6 = 1/2 + (1/2 x 3/4) 1/5 (1/2)^3  + (1/2 x 3/4 x 5/6) 1/7 (1/2)^5 +
 *
 *  n: number of terms in the series to sum
 *
 *  returns: the approximate value of pi obtained by suming the first n terms
 *           in the above series
 *           returns zero on error (if n is non-positive)
 */

 double approx_pi(int n);
```

In realen Projekten werden Sie für diese Aufgaben Dokumentationstools verwenden,
die die Generierung von Webseite, Handbüchern auf der Basis eigener
Schlüsselworte in den Kommentaren unterstützen ->
[doxygen](http://fnch.users.sourceforge.net/doxygen_c.html).

*4. Debugging*

```cpp
int main(){
  ...
  preProcessedData = filter1(rawData);
  // printf('Filter1 finished ... \n');
  // printf('Output %d \n', preProcessedData);
  result=complexCalculation(preProcessedData);
  ...
}
```

### Schlechte Kommentare

*1. Überkommentierung von Code*

```cpp
x = x + 1;  /* increment the value of x */
printf("Hello World\n"); // displays Hello world
```

"... over-commenting your code can be as bad as under-commenting it"

Quelle: [C Code Style Guidelines](https://www.cs.swarthmore.edu/~newhall/unixhelp/c_codestyle.html)

*2. "Merkwürdige Kommentare"*

``` JavaScript
//When I wrote this, only God and I understood what I was doing
//Now, God only knows

// sometimes I believe compiler ignores all my comments

// Magic. Do not touch.

// I am not responsible of this code.

try {

} catch(e) {

} finally { // should never happen }

```

[Sammlung von Kommentaren](https://fuzzzyblog.blogspot.com/2014/09/40-most-funny-code-comments.html)

### Was tun, wenn es schief geht?

```cpp                     ErroneousHelloWorld.c
#include<stdio.h>

int main() {
  for (zahl=0; zahl<3;  zahl++){
	    printf("Hello World ! ")
  }
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Methodisches Vorgehen:

* ** RUHE BEWAHREN **
* Lesen der Fehlermeldung
* Verstehen der Fehlermeldung / Aufstellen von Hypothesen
* Systematische Evaluation der Thesen
* Seien Sie im Austausch mit anderen (Kommilitonen, Forenbesucher, usw.) konkret

### Compilermessages

**Beispiel 1**

```cpp                     Error.c
#include <stdio.h>

int mani() {
    printf("Hello World");
    return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

**Beispiel 2**

```cpp                     Error.c
#include <stdio.h>

int main()
    printf("Hello World");
    return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

> Manchmal muss man sehr genau hinschauen, um zu verstehen, warum ein Programm nicht funktioniert. Versuchen Sie es!

```cpp                     ErroneousHelloWorld.c
#include <stdio.h>

imt main() {
	printf("Hello World\n'');
	printf("Wo liegt der Fehler?")
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


### Und wenn das Kompilieren gut geht?

... dann bedeutet es noch immer nicht, dass Ihr Programm wie erwartet
funktioniert.

```cpp                     ErroneousHelloWorld.c
#include <stdio.h>

int main() {
  char zahl;
  for (zahl=250; zahl<256; zahl++){
	    printf("Hello World !");
  }
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


## Warum dann C?

Zwei Varianten der Umsetzung ... C vs. Python

```cpp                     HelloWorld.c
#include <stdio.h>

int main() {
  char zahl;
  for (int zahl=0; zahl<3; zahl++){
	    printf("%d Hello World\n", zahl);
  }
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

```py                      HelloWorld.py
import sys

for i in range(3):
	print(i, "Hello World")

#sys.exit()
```
@Pyodide.eval

## Und wo kommt der Begriff des Algorithmus vor?

... Nehmen wir mal an ...
