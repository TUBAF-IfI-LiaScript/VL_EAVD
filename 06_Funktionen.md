<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md
-->


# Vorlesung VI - Funktionen

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

---------------------------------------------------------------------
Aktuelle Vorlesung im Versionsmanagementsystem GitHub:

[https://github.com/SebastianZug/CCourse/blob/master/06_Funktionen.md](https://github.com/SebastianZug/CCourse/blob/master/06_Funktionen.md)

---------------------------------------------------------------------


**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | `auto`         | `double` | `int`      | `struct` | `break`    |
|             | `else`         | `long`   | `switch`   | `case`   | `enum`     |
|             | `register`     | `typedef`| `char`     | `extern` | return     |
|             | union          | `const`  | `float`    | `short`  | `unsigned` |
|             | `continue`     | `for`    | `signed`   | `void`   | `default`  |
|             | `goto`         | `sizeof` | `volatile` | `do`     | `if`       |
|             | static         | `while`  |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | inline   | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

---

{{1}}
Standardbibliotheken

{{1}}
| Name         | Bestandteil | Funktionen                           |
|:-------------|:------------|:-------------------------------------|
| `<stdio.h>`  |             | Input/output                         |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite |
| `<float.h>`  |             | Parameter der Floatwerte             |
| `<limits.h>` |             | Größe der Basistypen                 |
| `<fenv.h>`   |             | Verhalten bei Typumwandlungen        |

{{1}}
[C standard library header files](https://en.cppreference.com/w/c/header)

## 0. Definition vs. Deklaration von Variablen

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

int main(void) {
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
@Rextester.C

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
@Rextester.C


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
@Rextester.C

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
@Rextester.C


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
@Rextester.C

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
@Rextester.C


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
@Rextester.C

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

**call-by-reference**

Bei einer Übergabe als Referenz wirken sich Änderungen an den Parametern auf die
ursprünglichen Werte aus. *Call-by-reference* wird unbedigt notwendig, wenn eine
Funktion mehrere Rückgabewerte hat.

Die *call-by-reference*-Parameterübergabe wird in der nächsten Vorlesung
eingehend diskutiert.

### Herausforderung komplexer Parametersätze und Rückgabewerte

Eine weitere Möglichkeit mehrere Werte zu übergeben bieten die zusammengesetzen
Datentypen `struct`s und arrays.

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

int main(void) {
   struct datensatz eintrag = initDatensatz("Micky Maus", 50, 1);
   printf("Name %s \nAlter %d \nNote %d\n", eintrag.name, eintrag.alter, eintrag.note);
   return 0;
}
```
@Rextester.C


{{1}}
An die Funktion übergebene Arrays werden nicht wie bei *call-by-value* kopiert, sondern als Zeiger übergeben (*call-by-reference*) und können
demzufolge in der Funktion verändert werden. Übergeben wird an die Funktion
die Anfangsadresse des Arrays.

{{1}}
```cpp
#include <stdio.h>

void pluseins(int feld[])
{
	int i;
	for (i=0;i<10;i++) feld[i]++;
}
int main(void)
{
    int feld[10];
  	int i;
	  for (i=0;i<10;i++) feld[i]=0;

    pluseins(feld);
    //oder pluseins(&feld[0]);
    return 0;
}
```

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

## 2.  Lebensdauer und Sichtbarkeit von Variablen

Im Zusammenhang mit Funktionen stellt sich die Frage nach der Sichtbarkeit und
der Lebensdauer einer Variablen um so mehr.

Zur Erinnerung: **globale**-Variable werden außerhalb jeder Funktionen definiert
und gelten in allen Funktionen, **lokale**-Variablen gelten nur in der Funktion,
in der sie definiert sind.

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
@Rextester.C

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
```cpp
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
@Rextester.C

## Beispiel des Tages

Generieren Sie mit einem C-Programm Dateien im Excelformat, um diese dann weiter
verarbeiten zu können. Dazu nutzen wir die Bibliothek `libxlsxwriter`, deren
Dokumentation und Quellcode Sie unter

[https://libxlsxwriter.github.io/index.html](https://libxlsxwriter.github.io/index.html)

finden. Die Dokumentation für die im Beispiel verwendeten Funktionen findet sich
dann für `lxw_workbook` auf der Seite

[https://libxlsxwriter.github.io/workbook_8h.html](https://libxlsxwriter.github.io/workbook_8h.html#a1cf96608a23ee4eb0e8467c15240d00b)


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
