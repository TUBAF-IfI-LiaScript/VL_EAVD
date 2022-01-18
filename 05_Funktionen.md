<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.1.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/05_Funktionen.md)

# Funktionen

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Vorlesung Prozedurale Programmierung`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2021/22`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Motivation, Definition und Verwendung von Funktionen in C-Programmen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/05_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/05_Funktionen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

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

## Feedback von Ihrer Seite

---------------------------------------------------------------------

Die Geschwindigkeit der Lehrveranstaltung ist

[(A)] Zu langsam
[(B)] Genau richtig
[(C)] Zu schnell

---------------------------------------------------------------------

Ich ...

[(A)] ... bin ich hier, weil ich hier sein muss.
[(B)] ... sehe durchaus die Anwendbarkeit des vermittelten Inhalts, Begeisterung kommt aber keine auf
[(C)] ... habe Spaß am Programmieren.

---------------------------------------------------------------------

## Motivation

**Einführungsbeispiel**

```cpp                          onBlock.c
#include <stdio.h>
#include <math.h>

#define VALUECOUNT 17

int main(void) {
  int a [] = {1,2,3,3,4,2,3,4,5,6,7,8,9,1,2,3,4};

  // Ergebnis Histogramm
  int hist[10] = {0,0,0,0,0,0,0,0,0,0};
  // Ergebnis Mittelwert
  int summe = 0;
  // Ergebnis Standardabweichung
  float abweichung = 0;
  for (int i=0; i<VALUECOUNT; i++){
    hist[a[i]]++;
    summe += a[i];
  }
  float mittelwert = summe / (float)VALUECOUNT;
  for (int i=0; i<VALUECOUNT; i++){
    abweichung += pow((a[i]-mittelwert),2.);
  }
  // Ausgabe
  for (int i=0; i<10; i++){
     printf("%d - %d\n", i, hist[i]);
  }
  // Ausgabe Mittelwert
  printf("Die Summe betraegt %d, der Mittelwert %3.1f\n", summe, mittelwert);
  // Ausgabe Standardabweichung
  float std = sqrt(abweichung / VALUECOUNT);
  printf("Die Standardabweichung der Grundgesamtheit betraegt %5.2f\n", std);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out -lm`, `./a.out`)

Ihre Aufgabe besteht nun darin ein neues Programm zu schreiben, das Ihre
Implementierung der Mittelwertbestimmung integriert. Wie gehen Sie vor? Was sind
die Herausforderungen dabei?

> Stellen Sie das Programm so um, dass es aus einzelnen Bereichen besteht und überlegen Sie, welche Variablen wo gebraucht werden.

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
  // d = f_Histogramm(a) ...
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
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out -lm`, `./a.out`)


### Fehler

**Rückgabewert ohne Rückgabedefintion**

```cpp   return.c
void foo()
{
	/* Code */
	return 5; /* Fehler */
}

int main(void)
{
  foo()
  return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
**Erwartung eines Rückgabewertes**

{{1}}
```cpp   returnII.c
#include <stdio.h>

void foo(){
   printf("Ausgabe");
}

int main(void) {
  int i = foo();
  return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{2}}
**Implizite Convertierungen**

{{2}}
```cpp     conversion.c
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
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall -Wconversion main.c -o a.out`, `./a.out`)


{{3}}
**Parameterübergabe ohne entsprechende Spezifikation**

{{3}}
```cpp    paramters.c
#include <stdio.h>

int foo(void){       // <- Die Funktion erwartet explizit keine Parameter
   return 3;
}

int main(void) {
  int i = foo(5);
  return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall -Wconversion main.c -o a.out`, `./a.out`)


{{4}}
**Anweisungen nach dem return-Schlüsselwort**

{{4}}
```cpp    codeOrder.c
int foo()
{
	return 5;
  /* Code */   // Wird nie erreicht!
}
```

{{5}}
**Falsche Reihenfolgen der Parameter**

{{5}}
```cpp     conversion.c
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
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall -Wconversion main.c -o a.out`, `./a.out`)


### asdfas

```cpp     conversion.c
#include <stdio.h>
#include <stdlib.h>

void printSizeOf(int intArray[]);
void printLength(int intArray[]);

int main(int argc, char* argv[])
{
    int array[] = { 0, 1, 2, 3, 4, 5, 6 };

    printf("sizeof of array: %d\n", (int) sizeof(array));
    printSizeOf(array);

    printf("Length of array: %d\n", (int)( sizeof(array) / sizeof(array[0]) ));
    printLength(array);
}

void printSizeOf(int intArray[])
{
    printf("sizeof of parameter: %d\n", (int) sizeof(intArray));
}

void printLength(int intArray[])
{
    printf("Length of parameter: %d\n", (int)( sizeof(intArray) / sizeof(intArray[0]) ));
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall -Wconversion main.c -o a.out`, `./a.out`)


### Funktionsdeklaration

```cpp  experiments.c
#include <stdio.h>

int main(void) {
  int i = foo();       // <- Aufruf der Funktion
  printf("i=%d\n", i);
  return 0;
}

int foo(void){         // <- Definition der Funktion
   return 3;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


Damit der Compiler überhaupt von einer Funktion Kenntnis nimmt, muss diese vor
ihrem Aufruf bekannt gegeben werden. Im vorangegangenen Beispiel wird die
die Funktion erst nach dem Aufruf definiert. Hier erfolgt eine automatische
(implizite) Deklaration. Der Complier zeigt dies aber durch ein *Warning* an.

{{1}}
Eine explizite Deklaration zeigt folgendes Beispiel:

{{1}}
```cpp     explicite.c
#include <stdio.h>

int foo(void);         // Explizite Einführung der Funktion foo()

int main(void) {
  int i = foo();       // <- Aufruf der Funktion
  printf("i=%d\n", i);
  return 0;
}

int foo(void){         // <- Definition der Funktion foo()
   return 3;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

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

Mit Hilfe des Zeigers wird in C die "call-by-reference"- Parameterübergabe
realisiert. In der Liste der formalen Parameter wird ein Zeiger eines
passenden Typs definiert. Beim Funktionsaufruf wird als Argument statt
Variable eine Adresse übergeben. Beachten Sie, dass für den Zugriff auf den Inhalt des Zeigers (einer Adresse) der Inhaltsoperator `*` benötigt wird.

```c                    ParameterI.c
#include <stdio.h>
#include <stdlib.h>

void inkrementieren(int *variable){
  (*variable)++;
}

int main(void) {
  int a=0;
  inkrementieren(&a);
  printf("a = %d\n", a);
  inkrementieren(&a);
  printf("a = %d\n", a);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


Die Adresse einer Variable wird mit dem Adressenoperator `&`
ermittelt. Weiterhin kann an den Zeiger-Parameter eine Array-Variable
übergeben werden.

```c                   ParameterII.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double sinussatz(double *lookup_sin, int angle, double opositeSide){
  return opositeSide*lookup_sin[angle];
}

int main(void) {
  double sin_values[360] = {0};
  for(int i=0; i<360; i++) {
    sin_values[i] = sin(i*M_PI/180);
  }
  printf("Größe des Arrays %ld\n", sizeof(sin_values));
  printf("Result =  %lf \n", sinussatz(sin_values, 30, 20));
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out -lm`, `./a.out`)

Der Vorteil der Verwendung der Zeiger als Parameter besteht darin, dass
in der Funktion mehrere Variablen auf eine elegante Weise verändert
werden können. Die Funktion hat somit quasi mehrere Ergebnisse.

```c     ParameterIII.c
#include <stdio.h>
#include <stdlib.h>

void tauschen(char *anna, char *hanna){
  char aux=*anna;
  *anna=*hanna;
  *hanna=aux;
}

int main(void) {
  char anna='A',hanna='H';
  printf("%c und %c\n", anna,hanna);
  tauschen(&anna,&hanna);
  printf("%c und %c\n", anna,hanna);;
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### Zeiger als Rückgabewerte

Analog zur Bereitstellung von Parametern entsprechend dem "call-by-reference"
Konzept können auch Rückgabewerte als Pointer vorgesehen sein. Allerdings
sollen Sie dabei aufpassen ...

```c                         returnPointer.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int * doCalc(int *wert) {
  int a = *wert + 5;
  return &a;
}

int main(void) {
  int b = 5;
  printf("Irgendwas stimmt nicht %d", * doCalc(&b) );
  return EXIT_SUCCESS;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Mit dem Beenden der Funktion werden deren lokale Variablen vom Stack gelöscht.
Um diese Situation zu handhaben können Sie zwei Lösungsansätze realisieren.

**Variante 1**  Sie übergeben den Rückgabewert in der Parameterliste.

```c          PointerAsParameter.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void kreisflaeche(double durchmesser, double *flaeche) {
  *flaeche = M_PI * pow(durchmesser / 2, 2);
  // Hier steht kein return !
}

int main(void) {
  double wert = 5.0;
  double flaeche = 0;
  kreisflaeche(wert, &flaeche);
  printf("Die Kreisfläche beträgt für d=%3.1lf[m] %3.1lf[m²] \n", wert, flaeche);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out -lm`, `./a.out`)

{{1}}
**Variante 2** Rückgabezeiger adressiert mit `static` bezeichnete Variable. Aber Achtung, diese Lösung funktioniert nicht bei rekursiven Aufrufen.

{{1}}
```c                             PointerInsteadOfReturnI.c
#include <stdio.h>
#include <stdlib.h>

int* cumsum(int wert) {
  static int sum = 0;
  sum += wert;
  return &sum;
}

int main(void) {
  int wert = 2;
  int *sum;
  sum=cumsum(wert);
  sum=cumsum(wert);
  printf("Die Summe ist : %d\n", *sum);
  sum=cumsum(wert);
  printf("Die Summe ist : %d\n", *sum);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{2}}
**Variante 3** Für den Rückgabezeiger wird der Speicherplatz mit `malloc` dynamisch angelegt (dazu später mehr).

{{2}}
```c                        PointerInsteadOfReturnII.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double* kreisflaeche(double durchmesser) {
  double *flaeche=(double*)malloc(sizeof(double));
  *flaeche = M_PI * pow(durchmesser / 2, 2);
  return flaeche;
}

int main(void) {
  double wert = 5.0;
  double *flaeche;
  flaeche=kreisflaeche(wert);
  printf("Die Kreisfläche beträgt für d=%3.1lf[m] %3.1lf[m²] \n", wert, *flaeche);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out -lm`, `./a.out`)


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
stattfinden soll. Gegebenenfalls ist die Ausführung der `inline`-Funktion schneller,
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

Eine Funktion, die sich selbst aufruft, wird als rekursive Funktion bezeichnet. Den Aufruf selbst nennt man Rekursion. Als Beispiel dient die  Fakultäts-Funktion `n!`, die sich rekursiv als $n(n-1)!$ definieren lässt (wobei $0! = 1$).

```cpp                fakultaet.c
#include <stdio.h>

int fakultaet (int a){
  if (a == 0)
    return 1;
  else
    return (a * fakultaet(a-1));
}

int main(){
  int eingabe;
  printf("Ganze Zahl eingeben: ");
  scanf("%d",&eingabe);
  printf("Fakultaet der Zahl: %d\n",fakultaet(eingabe));
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

<!--START_SKIP_IN_PDF-->
## Quizze

#1 Einfache Funktion
====================

```c
void berechneSumme(int a, double b) {
  return a + b;
}

int main() {
  double Summe;
  Summe = berechneSumme(30, 15.6);

  return 0;
}
```

Was steht am Ende in Summe?

- [( )] `45.6`
- [(X)] Der Kompiliervorgang wird mit einem Fehler abgebrochen.
- [( )] Das Programm wird erfolgreich kompiliert, aber die Variable `Summe` erhält den Wert `0`.

#2 Rückgabe mehrerer Werte mit einem Array
==============================

```c
void berechnungen(int a, double b, double* arr) {
  arr[0] = a + b;
  arr[1] = a - b;
}

int main() {
  double Ergebnisse[] = {0, 0};
  berechnungen(30, 15.6, Ergebnisse);

  return 0;
}
```

Was steht am Ende in Ergebnisse?

- [(X)] `{45.6, 14.4}`
- [( )] Der Kompiliervorgang wird mit einem Fehler abgebrochen.
- [( )] Das Programm wird erfolgreich kompiliert, aber die Variable `Ergebnisse` erhält die Werte `{0, 0}`.
<!--END_SKIP_IN_PDF-->
