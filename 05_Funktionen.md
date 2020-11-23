<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md

-->

# Funktionen

Die interaktive Version des Kurses ist unter diesem [Link](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/05_Funktionen.md#1) zu finden.

**Wie weit waren wir gekommen?**

<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=%23include%20%3Cstdio.h%3E%0A%23include%20%3Cmath.h%3E%0A%0A%23define%20VALUECOUNT%2017%0A%0Aint%20main%28void%29%20%7B%0A%20%20int%20a%20%5B%5D%20%3D%20%7B1,2,3,3,4,2,3,4,5,6,7,8,9,1,2,3,4%7D%3B%0A%0A%20%20int%20summe_I%20%3D%200%3B%0A%20%20for%20%28int%20i%3D0%3B%20i%3CVALUECOUNT%3B%20i%2B%2B%29%7B%0A%20%20%20%20summe_I%20%2B%3D%20a%5Bi%5D%3B%0A%20%20%7D%0A%20%20%0A%20%20int%20summe_II%20%3D%200%3B%0A%20%20//int*%20prt_b%20%3D%20NULL%3B%0A%20%20int%20*ptr_ende%20%3D%20%28int%20*%29%28%26a%20%2B%201%29%20-%201%3B%0A%20%20for%20%28int*%20prt_b%20%3D%20a%3B%20prt_b%3C%3Dptr_ende%3B%20prt_b%2B%2B%29%7B%0A%20%20%20%20summe_II%20%2B%3D%20*prt_b%3B%0A%20%20%7D%0A%20%20%0A%20%20printf%28%22Die%20Summe%20betraegt%20%25d%20%25d%5Cn%22,%20summe_I,%20summe_II%29%3B%0A%0A%20%20return%200%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=76&heapPrimitives=nevernest&origin=opt-frontend.js&py=c&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


>  Zur Erinnerung ... an die Schritte zur Realisierung einer Variablen
> * Deklaration ist nur die Vergabe eines Namens und eines Typs für die Variable.
> * Definition ist die Reservierung des Speicherplatzes.
> * Initialisierung ist die Zuweisung eines ersten Wertes.

**Inhalt der heutigen Veranstaltung**

* Strukturierung von Code anhand von Funktionen und Prozeduren
* Konfiguration von Parametern und Rückgabewerten
* Verwendung von Funktionen beim Entwurf von Software

**Fragen an die heutige Veranstaltung ...**

* Nennen Sie Vorteile prozeduraler Programmierung!
* Welche Komponenten beschreiben Definition einer Funktion?
* Welche unterschiedlichen Bedeutungen kann das Schlüsselwort `static`
  ausfüllen?
* Beschreiben Sie Gefahren bei der impliziten Typkonvertierung.
* Erläutern Sie die Begriffe Sichtbarkeit und Lebensdauer von Variablen.
* Welche kritischen Punkte sind bei der Verwendung globaler Variablen zu
  beachten.
* Warum ist es sinnvoll Funktionen in Look-Up-Tables abzubilden, letztendlich
  kostet das Ganze doch Speicherplatz?


## Motivation

**Einführungsbeispiel**

```cpp                          onBlock.c
#include <stdio.h>
#include <math.h>

#define VALUECOUNT 17

int main(void) {
  int a [] = {1,2,3,3,4,2,3,4,5,6,7,8,9,1,2,3,4};
  int hist[10] = {0,0,0,0,0,0,0,0,0,0};
  for (int i=0; i<VALUECOUNT; i++){
    hist[a[i]]++;
  }
  for (int i=0; i<10; i++){
     printf("%d - %d\n", i, hist[i]);
  }
  int summe = 0;
  for (int i=0; i<VALUECOUNT; i++){
    summe += a[i];
  }
  float mittelwert = summe / (float)VALUECOUNT;
  printf("Die Summe betraegt %d, der Mittelwert %3.1f\n", summe, mittelwert);
  float abweichung = 0;
  for (int i=0; i<VALUECOUNT; i++){
    //abweichung += pow((a[i]-mittelwert),2.);
    abweichung += (a[i]-mittelwert)*(a[i]-mittelwert);
  }
  float std = sqrt(abweichung / VALUECOUNT);
  printf("Die Standardabweichung der Grundgesamtheit betraegt %5.2f\n", std);
  return 0;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)

Ihre Aufgabe besteht nun darin ein neues Programm zu schreiben, das Ihre
Implementierung der Mittelwertbestimmung integriert. Wie gehen Sie vor? Was sind
die Herausforderungen dabei?

{{1}}
**Prozedurale Programmierung Ideen und Konzepte**

{{1}}
*Bessere Lesbarkeit*

{{1}}
Der Quellcode eines Programms kann schnell mehrere tausend Zeilen umfassen. Beim
Linux Kernel sind es sogar über 15 Millionen Zeilen und Windows, das ebenfalls
zum Großteil in C geschrieben wurde, umfasst schätzungsweise auch mehrere
Millionen Zeilen. Um dennoch die Lesbarkeit des Programms zu gewährleisten, ist
die Modularisierung unerlässlich.

{{1}}
*Wiederverwendbarkeit*

{{1}}
In fast jedem Programm tauchen die gleichen Problemstellungen mehrmals auf. Oft
gilt dies auch für unterschiedliche Applikationen. Da nur Parameter und
Rückgabetyp für die Benutzung einer Funktion bekannt sein müssen, erleichtert
dies die Wiederverwendbarkeit. Um die Implementierungsdetails muss sich der
Entwickler dann nicht mehr kümmern.

{{1}}
*Wartbarkeit*

{{1}}
Fehler lassen sich durch die Modularisierung leichter finden und beheben.
Darüber hinaus ist es leichter, weitere Funktionalitäten hinzuzufügen oder zu
ändern.

{{1}}
In allen 3 Aspekten ist der Vorteil in der Kapselung der Funktionalität zu
suchen.

{{2}}
**Wie würden wir das vorhergehende Beispiel umstellen?**

{{2}}
Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine,
möglicherweise wiederverwendbare Codeelemente zerlegen.

{{2}}
```cpp                          standardabweichung.c
#include <stdio.h>

// Funktion für den Mittelwert
// Mittelwert = f_Mittelwert(daten)

// Funktion für die Standardabweichung
// Standardabweichung =  f_Standardabweichung(daten)

// Funktion für die Histogrammgenerierung
// Histogramm = f_Histogramm(daten)

// Funktion für die Ausgabe
// f_Ausgabe(daten, {Mittelwert, Standardabweichung, Histogramm})

{{2}}
int main(void) {
  int a[] = {3,4,5,6,2,3,2,5,6,7,8,10};
  // b = f_Mittelwert(a) ...
  // c = f_Standardabweichung(a) ...
  // d = f_Standardabweichung(a) ...
  // f_Ausgabe(a, b, c, d) ...
  return 0;
}
```

{{3}}
**Wie findet sich diese Idee in großen Projekten wieder?**

{{3}}
> **Write Short Functions**
>
>*Prefer small and focused functions.*
>
> *We recognize that long functions are sometimes appropriate, so no hard limit*
> *is placed on functions length. If a function exceeds about 40 lines, think*
> *about whether it can be broken up without harming the structure of the*
> *program.*
>
> *Even if your long function works perfectly now, someone modifying it in a*
> *few months may add new behavior. This could result in bugs that are hard*
> *to find. Keeping your functions short and simple makes it easier for other*
> *people to read and modify your code.*
>
> *You could find long and complicated functions when working with some code.*
> *Do not be intimidated by modifying existing code: if working with such a*
> *function proves to be difficult, you find that errors are hard to debug, or*
> *you want to use a piece of it in several different contexts, consider*
> *breaking up the function into smaller and more manageable pieces.*
>
>[Google Style Guide für C++ Projekte](https://google.github.io/styleguide/cppguide.html#Write_Short_Functions)

### Funktionsdefinition

```
[Spezifizierer] Rückgabedatentyp Funktionsname([Parameterliste]) {
   /* Anweisungsblock mit Anweisungen */
   [return Rückgabewert]
}
```

* Rückgabedatentyp - Welchen Datentyp hat der Rückgabewert?

  Eine Funktion ohne Rückgabewert wird vom Programmierer als `void`
  deklariert. Sollten Sie keinen Rückgabetyp angeben, so wird
  automatisch eine Funktion mit Rückgabewert vom Datentyp `int` erzeugt.

* Funktionsname - Dieser Bestandteil der Funktionsdefinition ist
  eine eindeutige Bezeichnung, die für den Aufruf der Funktion
  verwendet wird.

  Es gelten die gleichen Regeln für die Namensvergabe wie für
  Variablen. Logischerweise sollten keine Funktionsnamen der
  Laufzeitbibliothek verwenden, wie z. B. `printf()`.

* Parameterliste - Parameter sind Variablen (oder Pointer darauf) die durch
  einen Datentyp und einen Namen spezifiziert werden. Mehrere Parameter
  werden durch Kommas getrennt.

  Parameterliste ist optional, die Klammern jedoch nicht.  Alternative zur
  fehlenden Parameterliste ist die Liste aus einen Parameter vom Datentyp `void` ohne Angabe des Namen.

* Anweisungsblock - Der Anweisungsblock umfasst die im Rahmen der
  Funktion auszuführenden Anweisungen und Deklarationen. Er wird
  durch geschweifte Klammern gekapselt.

* Spezifizierer - Hier wird die Konfiguration bestimmter
  Speicherklassen eröffnet. Erlaubt sind Speicherklassen `extern` und `static`,
  wobei `static` bei Funktionen (und globalen Variablen) bewirkt, dass auf die
  Funktion (Variable) nur innerhalb einer Datei zugegriffen werden kann.

Die Funktionsdefinition wird für jede Funktion genau einmal benötigt.

### Beispiele für Funktionsdefinitionen

``` c
int main (void) {
  /* Anweisungsblock mit Anweisungen */
}
```

``` c
int printf(const char * restrict format, ...){
   /* Anweisungsblock mit Anweisungen */
}

//int a = printf("Hello World\n %d", 1);
```

``` c
void printDatenSatz(struct student datensatz){
   /* Anweisungsblock mit Anweisungen */
}
```

``` c
int mittelwert(int * array){
   /* Anweisungsblock mit Anweisungen */
}
```

### Aufruf der Funktion
> **Merke:** Die Funktion (mit der Ausnahme der `main`-Funktion) wird erst
> ausgeführt, wenn sie aufgerufen wird. Vor dem Aufruf muss die Funktion
> definiert oder deklariert werden.

Der Funktionsaufruf einer Funktionen mit dem Rückgabewert ist meistens Teil
einer Anweisung, z.B. einer Zuweisung oder einer Ausgabeanweisung.

```cpp                              callAFunction.c
#include <stdio.h>
#include <math.h>

void Info(){
    printf("Dieses Programm rundet Zahlenwerte.\n");
    printf("-----------------------------------\n");
}

int runden(float a){
    if ((a - (int)a)<0.5)
       return ((int) a);
    else
       return (((int) a) + 1);
}

float rundenf(float a, int nachkomma){
    float shifted= a* pow(10, nachkomma);
    if ((shifted - (int)shifted)<0.5)
       return ((float)(int)shifted * pow(10, -nachkomma));
    else
       return ((float)((int)shifted + 1) * pow(10, -nachkomma));
    printf("%f", shifted);
}

int main(void){
    Info();
    float input = 8.4535;
    printf("Eingabewert %f - Ausgabewert %d\n", input, runden(input));
    printf("Eingabewert %f - Ausgabewert %f\n", input, rundenf(input,2));

    return 0;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)


### Fehler

**Rückgabewert ohne Rückgabedefintion**

```cpp
void foo()
{
	/* Code */
	return 5; /* Fehler */
}

int main(void)
{
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
**Erwartung eines Rückgabewertes**

{{1}}
```cpp
#include <stdio.h>

void foo(){
   printf("Ausgabe");
}

int main(void) {
  int i = foo();
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{2}}
**Implizite Convertierungen**

{{2}}
```cpp
#include <stdio.h>

float foo(){
   return 3.123f;
}

int main(void) {
  int i = foo();
  printf("%d\n",i);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{2}}
``` bash @output
▶ gcc -Wconversion experiments.c
experiments.c: In function ‘main’:
experiments.c:9:11: warning: conversion to ‘int’ from ‘float’ may alter its value [-Wfloat-conversion]
   int i = foo();
           ^
```

{{3}}
**Parameterübergabe ohne entsprechende Spezifikation**

{{3}}
```cpp
#include <stdio.h>

int foo(void){       // <- Die Funktion erwartet explizit keine Parameter
   return 3;
}

int main(void) {
  int i = foo(5);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{4}}
**Anweisungen nach dem return-Schlüsselwort**

{{4}}
```cpp
int foo()
{
	return 5;
  /* Code */   // Wird nie erreicht!
}
```

{{5}}
**Falsche Reihenfolgen der Parameter**

{{5}}
```cpp
#include <stdio.h>

void foo(int index, float wert){
  printf("Index   -  Wert\n");
  printf("%5d   - %5.1f\n\n", index, wert);
}

int main(void) {
  foo(4, 6.5);
  foo(6.5, 4);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### Funktionsdeklaration

```cpp  experiments.c
#include <stdio.h>

int main(void) {
  int i = foo();   // <- Aufruf der Funktion
  return 0;
}

int foo(void){         // <- Defintion der Funktion
   return 3;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


Damit der Compiler überhaupt von einer Funktion Kenntnis nimmt, muss diese vor
ihrem Aufruf bekannt gegeben werden. Im vorangegangenen Beispiel wird die
die Funktion erst nach dem Aufruf definiert. Hier erfolgt eine automatische
(implizite) Deklaration. Der Complier zeigt dies aber durch ein *Warning* an.

{{1}}
Eine explizite Deklaration zeigt folgendes Beispiel:

{{1}}
```cpp
#include <stdio.h>

// Deklarationsteil
float berechneFlaeche(float breite, float hoehe); // <- Semikolon am Ende!!!

int main() {
   printf("Ergebnis %4.1f[m^2]\n", berechneFlaeche(23.2, 4.0));
   return 0;
}

// Definitionsteil
float berechneFlaeche(float breite, float hoehe){
   return breite * hoehe;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{2}}
Das Ganze wird dann relevant, wenn Funktionen aus anderen Quellcodedateien
eingefügt werden sollen. Die Deklaration macht den Compiler mit dem Aussehen der
Funktion bekannt. Diese werden mit `extern` als Spezifizierer markiert.

{{2}}
```cpp
extern float berechneFlaeche(float breite, float hoehe);
```

### Parameterübergabe und Rückgabewerte

Bisher wurden Funktionen betrachtet, die skalere Werte als Parameter erhilten
und ebenfalls einen skalaren Wert als einen Rückgabewert lieferten. Allerdings
ist diese Möglichkeit sehr einschränkend.

Es wird in vielen Programmiersprachen, darunter in C, zwei Arten der
Parameterübergabe realisiert.

**call-by-value**

In allen Beispielen bis jetzt wurden Parameter an die Funktionen *call-by-value*,
übergeben. Das bedeutet, dass innerhalb der aufgerufenen Funktion mit einer
Kopie der Variable gearbeitet wird und die Änderungen sich nicht auf den
ursprünglichen Wert auswirken.

```cpp          Student.c
#include <stdio.h>

// Definitionsteil
void doSomething(int a){
  printf("%d a in der Schleife\n", ++a);
}

int main(void) {
   int a = 5;
   printf("%d a in main\n", a);
   doSomething(a);
   printf("%d a in main\n", a);
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


**call-by-reference**

Bei einer Übergabe als Referenz wirken sich Änderungen an den Parametern auf die
ursprünglichen Werte aus. *Call-by-reference* wird unbedigt notwendig, wenn eine
Funktion mehrere Rückgabewerte hat.

Die *call-by-reference*-Parameterübergabe wird in der nächsten Vorlesung
eingehend diskutiert.

### Herausforderung komplexer Parametersätze und Rückgabewerte

Eine weitere Möglichkeit mehrere Werte zu übergeben bieten die zusammengesetzen
Datentypen `struct`s und arrays.

```cpp          Student.c
#include <stdio.h>
#include <string.h>

struct datensatz{
  char name[20];
  int alter;
  int note;
};

// Definitionsteil
struct datensatz initDatensatz(char name[], int alter, int note){
   struct datensatz student;
   strcpy(student.name, name);
   student.alter = alter;
   student.note = note;
   return student;
}

int main(void) {
   struct datensatz eintrag = initDatensatz("Micky Maus", 50, 1);
   printf("Name %s \nAlter %d \nNote %d\n", eintrag.name, eintrag.alter, eintrag.note);
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{1}}
An die Funktion übergebene Arrays werden nicht wie bei *call-by-value* kopiert, sondern als Zeiger übergeben (*call-by-reference*) und können
demzufolge in der Funktion verändert werden. Übergeben wird an die Funktion
die Anfangsadresse des Arrays.

{{1}}
```cpp       ByReference.c
#include <stdio.h>

void pluseins(int feld[])
{
	int i;
	for (i=0;i<10;i++) {
    feld[i]++;
    printf("%d ", feld[i]);
  }
}

int main(void)
{
    int feld[10];
  	int i;
	  for (i=0;i<10;i++) feld[i]=i;

    pluseins(feld);
    //oder pluseins(&feld[0]);
    return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### `main`-Funktion

In jedem Programm muss und darf nur ein `main`-Funktion geben. Diese Funktion
wird beim Programmstart automatisch ausgeführt.

Definition der `main`-Funktion entsprechend dem C99-Standard:

```c
int main(void) {
  /*Anweisungen*/
}
```

```c
int main(int argc, char *argv[]) {
  /*Anweisungen*/
}
```

Mehr zu den Parameter `argc` und `argv` in einer der folgenden Vorlesungen.

### `inline`-Funktionen

Der `inline`-Funktion wird das Schlüsselwort `inline` vorangestellt, z.B.:

```c
static inline void ausgabeBruch(int z, int n) {
   printf("%d / %d\n", z, n);
}
```

`inline`-Funktion wird vom Compiler direkt an der Stelle eingefügt, wo der Aufruf
stattfinden soll. Gegebenfalls ist die Ausführung der `inline`-Funktion schneller,
da die mit dem Aufruf verbundenen Sicherung der Rücksprungadresse, der Sprung zur
Funktion und der Rücksprung nach Ausführung entfallen. Das Schlüsselwort `inline`
ist für den Compiler allerdings nur ein Hinweis und kein Befehl.

## Lebensdauer und Sichtbarkeit von Variablen

Im Zusammenhang mit Funktionen stellt sich die Frage nach der Sichtbarkeit und
der Lebensdauer einer Variablen um so mehr.

Zur Erinnerung: **globale**-Variable werden außerhalb jeder Funktionen definiert
und gelten in allen Funktionen, **lokale**-Variablen gelten nur in der Funktion,
in der sie definiert sind.

```cpp                 variables.c
#include <stdio.h>

const float pi = 3.14;

float berechneUmfang(float durchmesser){
  return durchmesser * pi;
}

float berechneFlaeche(float durchmesser){
  float radius = durchmesser / 2;
  return radius * radius * pi;
}

int main() {
   char gueltig = 0;
   float durchmesser = 23.2;
   if (durchmesser > 0) gueltig = 1;
   if (gueltig){
     int linecount = 0;
     printf("Umfang    %4.1f\n", berechneUmfang(23.2));
     linecount++;
     printf("Flaeche  %4.1f\n", berechneFlaeche(23.2));
     linecount++;
     printf("Pi kenne ich hier auch %f\n", pi);
     linecount++;
     printf("%d Zeilen ausgegeben\n", linecount);
   }
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

| Variable     | Spezifik         | Bedeutung                       |
|:-------------|:-----------------|:--------------------------------|
| `pi`         | global, const    | im gesammten Programm           |
| `radius`     | lokal            | nur in `berechneFlaeche`        |
| `gueltig`    | lokal            | nur in `main`                   |
| `linecount`  | lokal            | nur im Anweisungsblock von  `if`|

{{1}}
** Static-Variablen**

{{1}}
`static`-Variablen, definiert in einer Funktion, behalten ihren Wert auch nach
dem Verlassen des Funktionsblocks.

{{1}}
```cpp                static.c
#include <stdio.h>

int zaehler(){
  static int count = 0; //wird nur beim ersten Aufruf ausgeführt
  return ++count;       //wird nur beim jedem Aufruf ausgeführt
}

int main() {
   printf("%d \n", zaehler());
   printf("%d \n", zaehler());
   printf("%d \n", zaehler());
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

## Beispiel des Tages

Todo
