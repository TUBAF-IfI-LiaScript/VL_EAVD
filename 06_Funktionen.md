<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP.__eval
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s }}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);

    try {
        var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
        var info = log[1] + " " + log[4];

        if (info.length > 80)
          info = info.substring(0,76) + "..."

        error.add_detail(0, info, "error", log[2]-1, log[3]);
    } catch(e) {}

    throw error;
    }
</script>
@end


@JSCPP.eval: @JSCPP.__eval(@input, )

@JSCPP.eval_input: @JSCPP.__eval(@input,`@input(1)`)

@output: <pre class="lia-code-stdout">@0</pre>

-->


# Vorlesung VI - Funktionen

**Fragen an die heutige Veranstaltung ...**

* Nennen Sie Vorteile prozeduraler Programmierung!
* Welche Komponenten beschreiben den Definition einer Funktion?
* Welche unterschiedlichen Bedeutungen kann das Schlüsselwort `static`
  ausfüllen?
* Beschreiben Sie Gefahren bei der impliziten Typkonvertierung.
* Erläutern Sie die Begriffe Sichtbarkeit und Lebensdauer von Variablen.
* Welche kritischen Punkte sind bei der Verwendung globaler Variablen zu
  beachten.

---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/06_Funktionen.md

---------------------------------------------------------------------


**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | auto           | `double` | `int`      | `struct` | `break`    |
|             | `else`         | `long`   | `switch`   | `case`   | `enum`     |
|             | register       | typedef  | `char`     | extern   | return     |
|             | union          | const    | `float`    | `short`  | `unsigned` |
|             | `continue`     | `for`    | `signed`   | `void`   | `default`  |
|             | `goto`         | `sizeof` | volatile   | `do`     | `if`       |
|             | static         | `while`  |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | inline   | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

---

Standardbibliotheken

| Name         | Bestandteil | Funktionen                           |
|:-------------|:------------|:-------------------------------------|
| `<stdio.h>`  |             | Input/output (`printf`)              |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite |
| `<float.h>`  |             | Parameter der Floatwerte             |
| `<limits.h>` |             | Größe der Basistypen                 |
| `<fenv.h>`   |             | Verhalten bei Typumwandlungen        |
| `<string.h>` |             | Stringfunktionen                     |

https://en.cppreference.com/w/c/header


## 0. Wiederholung

### Initialisierung von n-dimensionalen Arrays

![Matrix](img/2DArray.jpg)<!-- width="90%" -->

```cpp                          nDimArray.c
#include <stdio.h>

int main() {
  // Initiallisierung
  int brett[8][8] = {0};
  // Zuweisung
  brett[2][1] = 1;
  brett[4][2] = 2;
  brett[3][5] = 3;
  brett[6][7] = 4;
  // Ausgabe
  int i, j;
  // Schleife fuer Zeilen, Y-Achse
  for(i=0; i<8; i++) {
  	// Schleife fuer Spalten, X-Achse
  	for(j=0; j<8; j++) {
  		printf("%d ", brett[i][j]);
  	}
  	printf("\n");
  }
  return 0;
}
```

``` bash @output
▶ ./a.out
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 1 0 0 0 0 0 0
0 0 0 0 0 3 0 0
0 0 2 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 4
0 0 0 0 0 0 0 0
```

Beispiel und Grafik aus dem C-Kurs [http://www.c-howto.de/](http://www.c-howto.de/tutorial/arrays-felder/zweidimensionale-felder/)


### Arrays und Pointer auf Arrays


### `const char` Arrays

```cpp                     arrayInitVsAssignment.c
#include <stdio.h>
#include <string.h>       // notwendig für strcpy

int main() {
  const char a[] = "Das ist der Originaltext";
  strcpy(a, "Das ist ein neuer Text");
  printf("%s\n",a);
  return 0;
}
```

``` bash @output
▶ gcc arrayInitVsAssignment.c
experiments.c: In function ‘main’:
experiments.c:6:10: warning: passing argument 1 of ‘strcpy’ discards ‘const’ qualifier from pointer target type [-Wdiscarded-qualifiers]
   strcpy(a, "Das ist ein neuer Text");
          ^
In file included from experiments.c:2:0:
/usr/include/string.h:125:14: note: expected ‘char * restrict’ but argument is of type ‘const char *’
 extern char *strcpy (char *__restrict __dest, const char *__restrict __src)
              ^
```

### Definition vs. Deklaration

Zur Erinnerung ... an die Schritte zur Realisierung einer Variablen

* Deklaration ist nur die Vergabe eines Namens und eines Typs für die Variable.
* Definition ist die Reservierung des Speicherplatzes.
* Initialisierung ist die Zuweisung eines ersten Wertes.

## 1. Definition von Funktionen

**Einführungsbeispiel**

```cpp                          onBlock.c
#include <stdio.h>
#include <math.h>

#define VALUECOUNT 17

int main() {
  int a [] = {1,2,3,3,4,2,3,4,5,6,7,8,9,1,2,3,4};
  // Histogramm berechnen
  int hist[10];
  for (int i=0; i<VALUECOUNT; i++){
    hist[a[i]]++;
  }
  // Histgramm ausgeben
  for (int i=0; i<10; i++){
     printf("%d - %d\n", i, hist[i]);
  }
  // Berechnen der Gesamtsumme / Mittelwert
  int summe = 0;
  for (int i=0; i<VALUECOUNT; i++){
    summe += a[i];
  }
  float mittelwert = summe / (float)VALUECOUNT;
  printf("Die Summe betraegt %d, der Mittelwert %3.1f\n", summe, mittelwert);
  // Berechne die Varianz
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
@JSCPP.eval

Ihre Aufgabe besteht nun darin ein neues Programm zu schreiben, das Ihre
Implementierung der Mittelwertbestimmung integriert. Wie gehen Sie vor? Was sind
die Herausforderungen dabei?

**Prozedurale Programmierung Ideen und Konzepte**

_Bessere Lesbarkeit_

Der Quellcode eines Programms kann schnell mehrere tausend Zeilen umfassen. Beim
Linux Kernel sind es sogar über 15 Millionen Zeilen und Windows, das ebenfalls
zum Großteil in C geschrieben wurde, umfasst schätzungsweise auch mehrere
Millionen Zeilen. Um dennoch die Lesbarkeit des Programms zu gewährleisten, ist
die Modularisierung unerlässlich.

_Wiederverwendbarkeit_

In fast jedem Programm tauchen die gleichen Problemstellungen mehrmals auf. Oft
gilt dies auch für unterschiedliche Applikationen. Da nur Parameter und
Rückgabetyp für die Benutzung einer Funktion bekannt sein müssen, erleichtert
dies die Wiederverwendbarkeit. Um die Implementierungsdetails muss sich der
Entwickler dann nicht mehr kümmern.

_Wartbarkeit_

Fehler lassen sich durch die Modularisierung leichter finden und beheben.
Darüber hinaus ist es leichter, weitere Funktionalitäten hinzuzufügen oder zu
ändern.

In allen 3 Aspekten ist der Vorteil in der Kapselung der Funktionalität zu
suchen.


**Wie würden wir das vorhergehende Beispiel umstellen?**

Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine,
möglicherweise wiederverwendbare Codeelemente zerlegen.


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


int main() {
  int a[] = {3,4,5,6,2,3,2,5,6,7,8,10};
  // b = f_Mittelwert(a) ...
  // c = f_Standardabweichung(a) ...
  // d = f_Standardabweichung(a) ...
  // f_Ausgabe(a, b, c, d) ...
  return 0;
}
```

**Wie findet sich diese Idee in großen Projekten wieder?**

Google Style Guide für C++ Projekte
https://google.github.io/styleguide/cppguide.html#Write_Short_Functions

> **Write Short Functions**
>
> Prefer small and focused functions.
>
> We recognize that long functions are sometimes appropriate, so no hard limit
> is placed on functions length. If a function exceeds about 40 lines, think
> about whether it can be broken up without harming the structure of the
> program.
>
> Even if your long function works perfectly now, someone modifying it in a few
> months may add new behavior. This could result in bugs that are hard to find.
> Keeping your functions short and simple makes it easier for other people to
> read and modify your code.
>
> You could find long and complicated functions when working with some code. Do
> not be intimidated by modifying existing code: if working with such a function
> proves to be difficult, you find that errors are hard to debug, or you want to
> use a piece of it in several different contexts, consider breaking up the
> function into smaller and more manageable pieces.

### Funktionsdefinition

```
[Spezifizierer] Rückgabedatentyp Funktionsname([Parameter]) {
   /* Anweisungsblock mit Anweisungen */
   [return Rückgabewert]
}
```

* Rückgabedatentyp - Welchen Datentyp hat der Rückgabewert?

  Eine Funktion ohne Rückgabewert wird vom Programmierer als `void`
  deklariert. Sollten Sie keinen Rückgabetyp angeben, so wird
  automatisch eine Funktion mit Rückgabewert vom Datentyp int erzeugt.

* Funktionsname - Dieser Bestandteil der Funktionsdefinition ist
  eine eindeutige Bezeichnung, die für den Aufruf der Funktion
  verwendet wird.

  Es gelten die gleichen Regeln für die Namensvergabe wie für
  Variablen. Logischerweise sollten keine Funktionsnamen der
  Laufzeitbibliothek verwenden, wie z. B. `printf()`.

* Parameter - Die Parameter sind beim Funktionsaufruf optional,
  die umgebenden Klammern nicht!

  Parameter sind Variablen (oder Pointer darauf) die durch einen
  Datentyp und einen Namen spezifiziert werden. Mehrer Parameter
  werden durch Kommas getrennt.

+ Anweisungsblock - Der Anweisungsblock umfasst die im Rahmen der
  Funktion auszuführenden Anweisungen und Deklarationen. Er wird
  durch geschweifte Klammern gekapselt.

+ Spezifizierer - Hier wird die Konfiguration bestimmter
  Speicherklassen eröffnet.

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

int main(){
    Info();
    float input = 8.4535;
    printf("Eingabewert %f - Ausgabewert %d\n", input, runden(input));
    printf("Eingabewert %f - Ausgabewert %f\n", input, rundenf(input,2));

    return 0;
}
```

### Fehler

**Rückgabewert ohne Rückgabedefintion**

```cpp
void foo()
{
	/* Code */
	return 5; /* Fehler */
}
```

``` bash @output
▶ gcc experiments.c
experiments.c: In function ‘foo’:
experiments.c:5:10: warning: ‘return’ with a value, in function returning void
   return 1;
          ^
```

**Erwartung eines Rückgabewertes**

```cpp
#include <stdio.h>

void foo(){
   printf("Ausgabe");
}

int main() {
  int i = foo();
  return 0;
}
```

``` bash @output
▶ gcc experiments.c
experiments.c: In function ‘main’:
experiments.c:9:11: error: void value not ignored as it ought to be
   int i = foo();
           ^
```

**Implizite Convertierungen**

```cpp
#include <stdio.h>

float foo(){
   return 3.123f;
}

int main() {
  int i = foo();
  return 0;
}
```

``` bash @output
▶ gcc -Wconversion experiments.c
experiments.c: In function ‘main’:
experiments.c:9:11: warning: conversion to ‘int’ from ‘float’ may alter its value [-Wfloat-conversion]
   int i = foo();
           ^
```

**Parameterübergabe ohne entsprechende Spezifikation**

```cpp
#include <stdio.h>

int foo(void){       // <- Die Funktion erwartet explizit keine Parameter
   return 3;
}

int main() {
  int i = foo(5);
  return 0;
}
```

``` bash @output
▶ gcc experiments.c
experiments.c: In function ‘main’:
experiments.c:8:11: error: too many arguments to function ‘foo’
   int i = foo(5);
           ^
experiments.c:3:5: note: declared here
 int foo(void){
     ^
```

**Anweisungen nach dem return-Schlüsselwort**

```cpp
int foo()
{
	return 5;
  /* Code */   // Wird nie erreicht!
}
```

**Falsche Reihenfolgen der Parameter**

```cpp
#include <stdio.h>

void foo(int index, float wert){
  printf("Index   -  Wert\n");
  printf("%5d   - %5.1f\n\n", index, wert);
}

int main() {
  foo(4, 6.5);
  foo(6.5, 4);
  return 0;
}
```
@JSCPP.eval

### Funktionsdeklaration

```cpp  experiments.c
#include <stdio.h>

int main() {
  int i = foo();   // <- Aufruf der Funktion
  return 0;
}

int foo(void){         // <- Defintion der Funktion
   return 3;
}
```

``` bash @output
experiments.c: In function ‘main’:
experiments.c:4:11: warning: implicit declaration of function ‘foo’ [-Wimplicit-function-declaration]
   int i = foo(5);
           ^
```

Damit der Compiler überhaupt von einer Funktion Kenntnis nimmt, muss diese vor
ihrem Aufruf deklariert werden. Im vorangegangenen Beispiel ist das automatisch
(implizit) geschehen. Der Complier hat dies aber durch ein *Warning* angezeigt.

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
@JSCPP.eval

Das Ganze wird dann relevant, wenn Funktionen aus anderen Quellcodedateien
eingefügt werden sollen. Die Deklaration macht den Compiler mit dem Aussehen der
Funktion bekannt. Diese werden mit `extern` als Spezifizierer markiert.

```cpp
extern float berechneFlaeche(float breite, float hoehe);
```

### Herausforderung komplexer Parametersätze und Rückgabewerte

Bisher wurden Beispiele besprochen, die einen skaleren Rückgabewert
realisierten. Allerdings wäre diese Möglichkeit sehr einschränkend. Eine Lösung
darüberhinaus stellen `struct`s und arrays dar.

```cpp
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

int main() {
   struct datensatz eintrag = initDatensatz("Micky Maus", 50, 1);
   printf("Name %s \nAlter %d \nNote %d\n", eintrag.name, eintrag.alter, eintrag.note);
   return 0;
}
```

``` bash @output
▶ ./a.out
Name Micky Maus
Alter 50
Note 1
```

## 2.  Lebensdauer und Sichtbarkeit von Variablen

Im Zusammenhang mit Funktionen stellt sich die Frage nach der Sichtbarkeit und
der Lebensdauer einer Variablen um so mehr.

```cpp
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
@JSCPP.eval

| Variable     | Spezifik         | Bedeutung                       |
|:-------------|:-----------------|:--------------------------------|
| `pi`         | global, const    | im gesammten Programm           |
| `radius`     | lokal            | nur in `berechneFlaeche`        |
| `gueltig`    | lokal            | nur in `main`                   |
| `linecount`  | lokal            | nur im Anweisungsblock von  `if`|


** Static Variablen**

```cpp
#include <stdio.h>

int zaehler(){
  static int count = 0;
  return ++count;
}

int main() {
   printf("%d \n", zaehler());
   printf("%d \n", zaehler());
   printf("%d \n", zaehler());
   return 0;
}
```

``` bash @output
▶ ./a.out
1
2
3
```


## Beispiel des Tages

Generieren Sie mit einem C Programm Dateien im Excelformat, um diese dann weiter
verarbeiten zu können. Dazu nutzen wir die Bibliothek libxlsxwriter, deren
Dokumentation und Quellcode Sie unter

https://libxlsxwriter.github.io/index.html

finden. Die Dokumentation für die im Beispiel verwendeten Funktionen findet sich
dann für lxw_workbook auf der Seite

https://libxlsxwriter.github.io/workbook_8h.html#a1cf96608a23ee4eb0e8467c15240d00b


```cpp
#include "xlsxwriter.h"
/* Some data we want to write to the worksheet. */
struct expense {
    char item[32];
    int  cost;
};
struct expense expenses[] = {
    {"Rent", 1000},
    {"Gas",   100},
    {"Food",  300},
    {"Gym",    50},
};
int main() {
    /* Create a workbook and add a worksheet. */
    lxw_workbook  *workbook  = workbook_new("tutorial01.xlsx");
    lxw_worksheet *worksheet = workbook_add_worksheet(workbook, NULL);
    /* Start from the first cell. Rows and columns are zero indexed. */
    int row = 0;
    int col = 0;
    /* Iterate over the data and write it out element by element. */
    for (row = 0; row < 4; row++) {
        worksheet_write_string(worksheet, row, col,     expenses[row].item, NULL);
        worksheet_write_number(worksheet, row, col + 1, expenses[row].cost, NULL);
    }
    /* Write a total using a formula. */
    worksheet_write_string (worksheet, row, col,     "Total",       NULL);
    worksheet_write_formula(worksheet, row, col + 1, "=SUM(B1:B4)", NULL);
    /* Save the workbook and free any allocated memory. */
    return workbook_close(workbook);
}
```

![Resultat](/img/excelLib.png)
