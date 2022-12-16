<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md#10


-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/04_Funktionen.md)

# Grundlagen der Sprache C++

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2022/23`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Funktionen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/04_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/04_Funktionen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Welche Komponenten beschreiben Definition einer Funktion?
* Wozu werden in der Funktion die Parameter gebraucht?
* Wann ist es sinnvoll Referenzen-Parameter zu verwenden?
* Warum ist es sinnvoll Funktionen in Look-Up-Tables abzubilden, letztendlich
  kostet das Ganze doch Speicherplatz?

---------------------------------------------------------------------

## Einschub - Klausurhinweise

> + Während der Klausur können Sie "alle Hilfsmittel aus Papier" verwenden!

> + Im OPAL finden sich Klausurbeispiele.

__Beispielhafte Klausuraufgabe aus dem vergangenen Jahr__

_Die Zustimmung (in Prozent) für die Verwendung der künstlichen Intelligenz im Pflegebereich unter der Bevölkerung von Mauritius und Réunion soll vergleichend betrachtet werden. Die Ergebnisse der Umfragen für die Jahre 2010 bis 2020 (je ein Wert pro Jahr) in zwei Arrays erfasst werden (je ein Array pro Insel) und in einem Programm ausgewertet werden._

+ _Für beide Inseln soll aus den in Arrays erfassten Werten je ein Mittelwert berechnet werden. Schreiben Sie dazu eine Funktion, die ein Array übergeben bekommt und einen Mittelwert als ein Ergebnis an die main-Funktion zurück liefert. Rufen Sie die Funktion in der main-Funktion für jedes beider Arrays auf und geben Sie die Mittelwerte in der main-Funktion aus._
+ _Schreiben Sie eine weitere Funktion, die die korrespondierenden Werte beider Arrays miteinander vergleicht. Geben Sie für jedes Jahr aus, auf welcher Insel die Zustimmung größer war, bei den gleichen Werte ist eine entsprechende Meldung auszugeben. Rufen Sie die Funktion in der main-Funktion auf._
+ _In der main()-Funktion sind die Werte von der Console einzulesen und in die Arrays zu speichern._


## Motivation

Erklären Sie die Idee hinter folgendem Code.

```cpp                          onBlock.cpp
#include <iostream>
#include <cmath>

using namespace std;
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
  cout<<"Die Summe betraegt "<<summe<<", der Mittelwert "<<mittelwert<<"\n";
  // Ausgabe Standardabweichung
  float stdabw = sqrt(abweichung / VALUECOUNT);
  cout<<"Die Standardabweichung der Grundgesamtheit betraegt "<<stdabw<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)

Ihre Aufgabe besteht nun darin ein neues Programm zu schreiben, das Ihre
Implementierung der Mittelwertbestimmung integriert. Wie gehen Sie vor? Was sind
die Herausforderungen dabei?

> Stellen Sie das Programm so um, dass es aus einzelnen Bereichen besteht und überlegen Sie, welche Variablen wo gebraucht werden.

### Prozedurale Programmierung Ideen und Konzepte

*Bessere Lesbarkeit*

Der Quellcode eines Programms kann schnell mehrere tausend Zeilen umfassen. Beim
Linux Kernel sind es sogar über 15 Millionen Zeilen und Windows, das ebenfalls
zum Großteil in C geschrieben wurde, umfasst schätzungsweise auch mehrere
Millionen Zeilen. Um dennoch die Lesbarkeit des Programms zu gewährleisten, ist
die Modularisierung unerlässlich.

*Wiederverwendbarkeit*

In fast jedem Programm tauchen die gleichen Problemstellungen mehrmals auf. Oft
gilt dies auch für unterschiedliche Applikationen. Da nur Parameter und
Rückgabetyp für die Benutzung einer Funktion bekannt sein müssen, erleichtert
dies die Wiederverwendbarkeit. Um die Implementierungsdetails muss sich der
Entwickler dann nicht mehr kümmern.

*Wartbarkeit*

Fehler lassen sich durch die Modularisierung leichter finden und beheben.
Darüber hinaus ist es leichter, weitere Funktionalitäten hinzuzufügen oder zu
ändern.

In allen 3 Aspekten ist der Vorteil in der Kapselung der Funktionalität zu
suchen.

### Anwendung

Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine,
möglicherweise wiederverwendbare Codeelemente zerlegen.


```cpp                          standardabweichung.cpp
#include <iostream>

using namespace std;
// Funktion für den Mittelwert
// Mittelwert = f_Mittelwert(daten)

// Funktion für die Standardabweichung
// Standardabweichung =  f_Standardabweichung(daten)

// Funktion für die Histogrammgenerierung
// Histogramm = f_Histogramm(daten)

// Funktion für die Ausgabe
// f_Ausgabe(daten, {Mittelwert, Standardabweichung, Histogramm})

int main(void) {
  int a[] = {3,4,5,6,2,3,2,5,6,7,8,10};
  // b = f_Mittelwert(a) ...
  // c = f_Standardabweichung(a) ...
  // d = f_Histogramm(a) ...
  // f_Ausgabe(a, b, c, d) ...
  return 0;
}
```

**Wie findet sich diese Idee in großen Projekten wieder?**

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


## C++ Funktionen 

![](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

### Funktionsdefinition

```
Rückgabedatentyp Funktionsname([Parameterliste]) {
   /* Anweisungsblock mit Anweisungen */
   [return Rückgabewert]
}
```

* __Rückgabedatentyp__ - Welchen Datentyp hat der Rückgabewert?

  Eine Funktion ohne Rückgabewert wird vom Programmierer als `void`
  deklariert. Sollten Sie keinen Rückgabetyp angeben, so wird
  automatisch eine Funktion mit Rückgabewert vom Datentyp `int` erzeugt.

* __Funktionsname__ - Dieser Bestandteil der Funktionsdefinition ist
  eine eindeutige Bezeichnung, die für den Aufruf der Funktion
  verwendet wird.

  Es gelten die gleichen Regeln für die Namensvergabe wie für
  Variablen.

* __Parameterliste__ - Parameter sind Variablen (oder Pointer bzw. Referenzen darauf) die durch
  einen Datentyp und einen Namen spezifiziert werden. Mehrere Parameter
  werden durch Kommas getrennt.

  Parameterliste ist optional, die Klammern jedoch nicht.  Alternative zur
  fehlenden Parameterliste ist die Liste aus einen Parameter vom Datentyp `void` ohne Angabe des Namen.

* __Anweisungsblock__ - Der Anweisungsblock umfasst die im Rahmen der
  Funktion auszuführenden Anweisungen und Deklarationen. Er wird
  durch geschweifte Klammern gekapselt.

Für die Funktionen gelten die gleichen Gültigkeits- und Sichtbarkeitsregeln wie für die Variablen.

### Beispiele für Funktionsdefinitionen

``` cpp
int main (void) {
  /* Anweisungsblock mit Anweisungen */
}
```

``` cpp
double pow (double base, double exponent){
   /* Anweisungsblock mit Anweisungen */
}

//int y = pow(25.0,0.5));
```

``` cpp
void tauschen(int &var1,int &var2){
   /* Anweisungsblock mit Anweisungen */
}
```

``` cpp
int mittelwert(int * array){
   /* Anweisungsblock mit Anweisungen */
}
```

### Aufruf der Funktion
> **Merke:** Die Funktion (mit der Ausnahme der `main`-Funktion) wird erst
> ausgeführt, wenn sie aufgerufen wird. Vor dem Aufruf muss die Funktion
> definiert oder deklariert werden.

Der Funktionsaufruf einer Funktionen mit dem Rückgabewert kann Teil
einer Anweisung, z.B. einer Zuweisung oder einer Ausgabeanweisung.

```cpp                              callAFunction.cpp
#include <iostream>
#include <cmath>
using namespace std;

void info(){
    cout<<"Dieses Programm rundet Zahlenwerte.\n";
    cout<<"-----------------------------------\n";
}

int runden(float a){
    if (a < 0)
       return (int)(a - 0.5);
    else
       return (int)(a + 0.5);
}

float rundenf(float a, int nachkomma){
    float shifted= a* pow(10, nachkomma);
    int result=0;
    if (shifted < 0)
    	  result = int(shifted -0.5);
    else
    		result = int(shifted +0.5);
    return (float)result * pow(10, -nachkomma);
}

int main(void){
    info();
    float input = -8.4565;
    cout<<"Eingabewert "<<input<<" - Ausgabewert "<<runden(input)<<"\n";
    cout<<"Eingabewert "<<input<<" - Ausgabewert "<<rundenf(input,1)<<"\n";
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)

Die Funktion `runden` nutzt die Funktionalität des Cast-Operators `int` aus.

+ Wenn N eine positive Zahl ist, wird 0.5 addiert 

  + $15.2 + 0.5 = 15.7$ `int(15.7) = 15` 
  + $15.7 + 0.5 = 16.2$ `int(16.2) = 16` 

+ Wenn N eine negative Zahl ist, wird 0.5 subtrahiert 

  + $-15.2 - 0.5 = -15.7$ `int(-15.7) = -15` 
  + $-15.7 - 0.5 = -16.2$ `int(-16.2) = -16` 

> Welche Verbesserungsmöglichkeit sehen Sie bei dem Programm? Tipp: Wie können wir den redundanten Code eleminieren?

> __Hinweis:__ C++ unterstützt gleiche Codenahmen bei unterschiedlichen Parametern. Der Compiler "sucht sich" die passende Funktion aus. Der Mechanismus wird als _Funktionsüberladung_ bezeichnet. 

### Fehler

**Rückgabewert ohne Rückgabedefintion**

```cpp   return.cpp
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
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
**Erwartung eines Rückgabewertes**

{{1}}
```cpp   returnII.cpp
#include <iostream>
using namespace std;

void foo(){
   cout<<"Ausgabe";
}

int main(void) {
  int i = foo();
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
**Falscher Rückgabetyp**

{{2}}
```cpp     conversion.cpp
#include <iostream>
using namespace std;

float foo(){
   return 3.123f;
}

int main(void) {
  int i = foo();
  cout<<i<<"\n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall -Wconversion main.cpp -o a.out`, `./a.out`)

{{3}}
**Parameterübergabe ohne entsprechende Spezifikation**

{{3}}
```cpp    paramters.cpp
#include <iostream>

int foo(void){       // <- Die Funktion erwartet explizit keine Parameter
   return 3;
}

int main(void) {
  int i = foo(5);
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall -Wconversion main.cpp -o a.out`, `./a.out`)


{{4}}
**Anweisungen nach dem return-Schlüsselwort**

{{4}}
```cpp    codeOrder.cpp
int foo()
{
	return 5;
  /* Code */   // Wird nie erreicht!
}
```

{{5}}
**Falsche Reihenfolgen der Parameter**

{{5}}
```cpp     conversion.cpp
#include <iostream>
using namespace std;

void foo(int index, float wert){
  cout<<"Index   -  Wert\n";
  cout<<index<<"   - "<<wert<<"\n\n";
}

int main(void) {
  foo(4, 6.5);
  foo(6.5, 4);
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall -Wconversion main.cpp -o a.out`, `./a.out`)


### Funktionsdeklaration

```cpp  experiments.cpp
#include <iostream>
using namespace std;

int main(void) {
  int i = foo();       // <- Aufruf der Funktion
  cout<<"i="<<i<<"\n";
  return 0;
}

int foo(void){         // <- Definition der Funktion
   return 3;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


Damit der Compiler überhaupt von einer Funktion Kenntnis nimmt, muss diese vor
ihrem Aufruf bekannt gegeben werden. Im vorangegangenen Beispiel wird die
die Funktion erst nach dem Aufruf definiert. Der Complier zeigt dies an.

{{1}}
Eine explizite Deklaration zeigt folgendes Beispiel:

{{1}}
```cpp     explicite.cpp
#include <iostream>
using namespace std;

int foo(void); // Explizite Einführung der Funktion foo()

int main(void) {
  int i = foo(); // <- Aufruf der Funktion
  cout << "i=" << i << "\n";
  return 0;
}

int foo(void) { // <- Definition der Funktion foo()
  return 3;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Das Ganze wird dann relevant, wenn Funktionen aus anderen Quellcodedateien
eingefügt werden sollen. Die Deklaration macht den Compiler mit dem Aussehen der
Funktion bekannt. Diese werden mit dem Schlüsselwort `extern`  markiert.

{{2}}
```cpp
extern float berechneFlaeche(float breite, float hoehe);
```

### Parameterübergabe und Rückgabewerte

Bisher wurden Funktionen betrachtet, die skalare Werte als Parameter erhielten
und ebenfalls einen skalaren Wert als einen Rückgabewert lieferten. Allerdings
ist diese Möglichkeit sehr einschränkend.

Es wird in vielen Programmiersprachen, darunter in C/C++, zwei Konzepte der
Parameterübergabe realisiert.

**call-by-value**

In allen Beispielen bis jetzt wurden Parameter an die Funktionen *call-by-value*,
übergeben. Das bedeutet, dass innerhalb der aufgerufenen Funktion mit einer
Kopie der Variable gearbeitet wird und die Änderungen sich nicht auf den
ursprünglichen Wert auswirken.

```cpp          Student.cpp
#include <iostream>
using namespace std;

// Definitionsteil
void doSomething(int a) { cout << ++a << " a in der Schleife\n"; }

int main(void) {
  int a = 5;
  cout << a << " a in main\n";
  doSomething(a);
  cout << a << " a in main\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


**call-by-reference**

Bei einer Übergabe als Referenz wirken sich Änderungen an den Parametern auf die
ursprünglichen Werte aus, es werden keine Kopien von Parametern angelegt.
*Call-by-reference* wird unbedigt notwendig, wenn eine
Funktion mehrere Rückgabewerte hat.

In C++ wird die "call-by-reference"- Parameterübergabe mit Hilfe der Referenzen
realisiert. In der Liste der formalen Parameter wird eine Referenz eines
passenden Typs definiert. Beim Funktionsaufruf wird als Argument eine
Variable des gleichen Datentyps übergeben.

```cpp                    ParameterI.cpp
#include <iostream>
using namespace std;

void inkrementieren(int &variable){
  variable++;
}

int main(void) {
  int a=0;
  inkrementieren(a);
  cout<<"a = "<<a<<"\n";
  inkrementieren(a);
  cout<<"a = "<<a<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Der Vorteil der Verwendung der Referenzen als Parameter besteht darin, dass
in der Funktion mehrere Variablen auf eine elegante Weise verändert
werden können. Die Funktion hat somit quasi mehrere Ergebnisse.

```cpp     ParameterIII.cpp
#include <iostream>
#include <cmath>
using namespace std;

void tauschen(char &anna, char &hanna){
  char aux=anna;
  anna=hanna;
  hanna=aux;
}

int main(void) {
  char anna='A',hanna='H';
  cout<<anna<<" und "<<hanna<<"\n";
  tauschen(anna,hanna);
  cout<<anna<<" und "<<hanna<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Es besteht ebenfalls die Möglichkeit, die bereits in C zur Verfügung stand, "call-by-reference"- Parameterübergabe mit Hilfe der Zeiger (Pointer)
zu realisieren. Im allgemeinen ist die Verwendung von Referenzen vorzuziehen,
bei Übergabe der Array-Parameter wird jedoch der Zeiger verwendet.

```cpp                   ParameterII.cpp
#include <iostream>
#include <cmath>
using namespace std;

double sinussatz(double *lookup_sin, int angle, double opositeSide){
  return opositeSide*lookup_sin[angle];
}
/*
double sinussatz(double lookup_sin[], int angle, double opositeSide){
  return opositeSide*lookup_sin[angle];
}
*/

int main(void) {
  double sin_values[360] = {0};
  for(int i=0; i<360; i++) {
    sin_values[i] = sin(i*M_PI/180);
  }
  cout<<"Größe des Arrays "<<sizeof(sin_values)<<"\n";
  cout<<"Result =  "<<sinussatz(sin_values, 30, 20)<<" \n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)

Statt Zeiger kann die Notation als Array undefinierter (definierter) Größe verwendet werden.
Unabhängig von der Notation entspricht die Größe des übergebenen Arrays der Definition in der
aufrufenden Funktion (hier main-Funktion).

Auch bei der Verwendung von Zeigern und Referenzen werden keine Kopien von Paramern angelegt, sondern die
Parameter selbst direkt verändert. Falls keine Veränderung angestrebt wird, aber das Anlegen von Kopien
vermieden werden soll, können konstante Zeiger bzw. Referenzen verwendet werden.

```cpp                   ParameterIV.cpp
#include <iostream>
#include <cmath>
using namespace std;

double sinussatz(const double *lookup_sin, int angle, double opositeSide){
  return opositeSide*lookup_sin[angle];
}

int main(void) {
  double sin_values[360] = {0};
  for(int i=0; i<360; i++) {
    sin_values[i] = sin(i*M_PI/180);
  }
  cout<<"Größe des Arrays "<<sizeof(sin_values)<<"\n";
  cout<<"Result =  "<<sinussatz(sin_values, 30, 20)<<" \n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)


### Zeiger und Referenzen als Rückgabewerte

Analog zur Bereitstellung von Parametern entsprechend dem "call-by-reference"
Konzept können auch Rückgabewerte als Pointer oder Referenz vorgesehen sein. Allerdings
sollen Sie dabei aufpassen ...

```cpp                         returnReferenz.cpp
#include <iostream>
using namespace std;

int& doCalc(int &wert) {
  int a = wert + 5;
  return a;
}

int main(void) {
  int b = 5;
  cout<<"Irgendwas stimmt nicht "<<doCalc(b);
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Mit dem Beenden der Funktion werden deren lokale Variablen vom Stack gelöscht.
Um diese Situation zu handhaben können Sie zwei Lösungsansätze realisieren.

**Variante 1**  Sie übergeben den Rückgabewert in der Parameterliste.

```cpp          ReferenzAsParameter.cpp
#include <iostream>
#include <cmath>
using namespace std;

void kreisflaeche(double durchmesser, double &flaeche) {
  flaeche = M_PI * pow(durchmesser / 2, 2);
  // Hier steht kein return !
}

int main(void) {
  double wert = 5.0;
  double flaeche = 0;
  kreisflaeche(wert, flaeche);
  cout<<"Die Kreisfläche beträgt für d="<<wert<<"[m] "<<flaeche<<"[m²] \n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)


{{1}}
**Variante 2** Für den Rückgabezeiger wird der Speicherplatz mit `new` dynamisch angelegt, aber Achtung: zu jedem new gehört ein `delete`.

{{1}}
```cpp                        PointerInsteadOfReturnII.cpp
#include <iostream>
#include <cmath>
using namespace std;

double* kreisflaeche(double durchmesser) {
  double *flaeche=new double;
  *flaeche = M_PI * pow(durchmesser / 2, 2);
  return flaeche;
}

int main(void) {
  double wert = 5.0;
  double *flaeche;
  flaeche=kreisflaeche(wert);
  cout<<"Die Kreisfläche beträgt für d="<<wert<<"[m] "<<*flaeche<<"[m²] \n";
  delete flaeche;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)

### Besonderheit Arrays

```cpp     conversion.c
#include <iostream>
#include <cstdlib>
using namespace std;

void printSizeOf(int intArray[])
{
    cout<<"sizeof of parameter: "<<sizeof(intArray)<<"\n";
}

void printLength(int intArray[])
{
    cout<<"Length of parameter: "<<sizeof(intArray) / sizeof(intArray[0])<<"\n";
}

int main()
{
    int array[] = { 0, 1, 2, 3, 4, 5, 6 };

    cout<<"sizeof of array: "<<sizeof(array)<<"\n";
    printSizeOf(array);

    cout<<"Length of array: "<< sizeof(array) / sizeof(array[0])<<"\n";
    printLength(array);
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall -Wconversion main.cpp -o a.out`, `./a.out`)




### `main`-Funktion

In jedem Programm muss und darf nur eine `main`-Funktion geben. Diese Funktion
wird beim Programmstart automatisch ausgeführt.

Definition der `main`-Funktion:

```cpp
int main(void) {
  /*Anweisungen*/
}
```

```cpp
int main(int argc, char *argv[]) {
  /*Anweisungen*/
}
```

Die Bezeichner `argc` und `argv` sind traditionell, können aber beliebig gewählt werden.
`argc` ist die Anzahl der Argumente, die von den Benutzern des Programms in der Kommandozeile angegeben werden. Der argc-Parameter ist immer größer als oder gleich 1.
`argv` ist ein Array von Befehlszeilenargumenten, wobei `argv[0]` das Programm selbst und `argv[argc]` immer NULL ist.

Im Beispiel wird die kompilierte Version von mainArgumente.cpp intern mit `./a.out 1 2 3 aus die Maus` aufgerufen.

```cpp                        mainArgumente.cpp
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  for (int i=0;i<argc;i++)
    cout<<argv[i]<<" ";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out 1 2 3 aus die Maus`)

## Beispiel des Tages

Wie werden Funktionen im realen Programmierbetrieb angewendet? Werfen Sie einen Blick auf die Dokumentation unseres Mikrocontrollers. 

https://microsoft.github.io/azure-iot-developer-kit/docs/apis/display/

Dort finden Sie einzelne Funktionen, die der Display Klasse (wird in der nächsten Woche behandelt) zugordnet sind.+

+
+
+


```cpp                ArduinoDisplay.cpp
#include <OledDisplay.h>

                                  // Aus Platzgründen entfernt
unsigned char BMP[] = {0,0,0,0,0,0,0,0,0,0,0, ..... 0,0,0,0,0,0,0,0};

void setup(){
    Screen.init();
}
void loop(){
    // print a string to the screen with wrapped = false
    Screen.print("This is OLEDDisplay Testing", false);
    delay(1000);
    // print a string to the screen with wrapped = true
    Screen.print("This is a very small display including only 4 lines", true);
    delay(1000);
    for(int i =0; i<=3; i++)
    {
        char buf[100];
        sprintf(buf, "This is row %d", i);
        Screen.print(i, buf);
    }
    delay(1000);
    // draw a bitmap to the screen
    Screen.draw(0, 0, 128, 8, BMP);
    delay(1000);
    // clean screen ready for next loop
    Screen.clean();
}
```

> Aufgabe: Wie könnten wir den Code abwandeln, um eine Laufschrift umzusetzen?

{{1}}
```cpp BuggyCode.cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
	String text = "Das ist ein Test";
	Serial.println(text);
	String output = "";
	int signs_per_line = 5;
	for (int i=0; i<text.length(); i++){
		 if (i <= text.length()-signs_per_line)
				output = text.substring(i, i+signs_per_line);
		 else
        output = text.substring(i, text.length()) +
                 text.substring(0, signs_per_line-(text.length()-i));
		 Serial.println(output);
	}
}

void loop() {
}
```
@AVR8js.sketch

# Quiz
## Funktionen
### Funktionsdefinition
> Wechen Rückgabewert liefert eine als `void` deklatierte Funktion?
[( )] Es können alle Arten von Rückgabewerten zurückgegeben werden.
[(X)] Es wird kein Wert zurückgegeben.

{{1}}
************************************************************************
> Welcher Datentyp wird automatisch als Rückgabewert ausgewählt, wenn Sie keinen Rückgabetyp angeben?
[( )] `void`
[(X)] `int`
[( )] `float`
[( )] `double`
[( )] `char`
[( )] `boolean`
************************************************************************

{{2}}
************************************************************************
> Muss die Parameterliste einer Funktionen wenigstens einen Parameter enthalten?
[( )] Ja
[(X)] Nein
************************************************************************

### Aufruf von Fuktionen
> Wodurch muss `[_____]` ersetzt werden damit die Funktion `divi` ermittelt ob `a` ein Teiler von `b` ist? Die Lösung ist ohne Leerzeichen einzugeben.
```cpp
#include <iostream>
using namespace std;

bool divi(int x, int y){
  if(x%y == 0)
    return true;
  else
    return false;
}

int main() {
  int a = 11;
  int b = 1001;
  bool bdiv = [_____]
  if(bdiv == 1)
    cout <<  a << " ist ein Teiler von " << b << "." << endl;
  else
    cout <<  a << " ist kein Teiler von " << b << "." << endl;
}
```
[[divi(b,a);]]

### Fehler
> ist dieses Programm fehlerfrei?
```cpp
#include <iostream>
using namespace std;

int foo(){
   return 42;
}

int main(void) {
  int i = foo();
  return 0;
}
```
[(X)] Ja
[( )] Nein

{{1}}
************************************************************************
> Ist dieses Programm fehlerfrei?
```cpp
#include <iostream>
using namespace std;

void foo(){
   return 42;
}

int main(void) {
  foo();
  return 0;
}
```
[( )] Ja
[(X)] Nein
************************************************************************

{{2}}
************************************************************************
> Welche Fehler liegen bei diesem Programm vor?
```cpp
#include <iostream>
using namespace std;

void foo(int index, float wert){
  cout<<"Index   -  Wert\n";
  cout<<index<<"   - "<<wert<<"\n\n";
  return index;
}

int main(void) {
  float f = foo(6.5, 4);
  return 0;
}
```
[[X]] Datentypen der Parameter beim Aufruf und der Defintion stimmen nicht überein
[[X]] Rückgabewert ohne Definition des Rückgabetyps
[[ ]] Anweisung nach dem `return` Schlüsselwort
************************************************************************

### Funktionsdeklaration
> Ersetzen Sie `[_____]` durch eine explizite Deklaration der Funktion `hw`.
```cpp
#include <iostream>
using namespace std;

[_____]

int main(void) {
  hw();
  return 0;
}

void hw(void) {
  cout << "Hello World!" << endl;
  return;
}
```
[[void hw();]]

{{1}}
************************************************************************
> Mit welcher dieser Anweisungen kann eine Funktion aus einer anderen Quellcodedatei einzufügt werden?
[(X)] `extern int x(int y, bool z);`
[( )] `import int x(int y, bool z);`
[( )] `using int x(int y, bool z);`
************************************************************************

### Parameterübergabe und Rückgabewerte
> Ordnen Sie die Eigenschaften den entsprechenden Arten der Parameterübergabe zu.
- [[*call-by-value*] [*call-by-reference*]]
- [    ( )           (X)      ]  Ermöglicht mehrere Rückgabewerte
- [    (X)           ( )      ]  Arbeitet mit einer Kopie der Variablen
- [    (X)           ( )      ]  Beeinflusst nicht den tatsächlichen Wert von Variablen in der `main`
- [    ( )           (X)      ]  Beeinflusst den tatsächlichen Wert von Variablen in der `main`


{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>
using namespace std;

void f_a(int &variable){
  variable++;
}

void f_b(int variable){
  variable--;
}

void f_c(int &variable){
  variable = 18;
}

int main(void) {
  int a = 0;
  f_a(a);
  f_c(a);
  f_b(a);
  f_b(a);
  f_a(a);
  cout << a;
  return 0;
}
```
[[19]]
************************************************************************

{{2}}
************************************************************************
> Womit werden Array-Parameter übergeben?
[( )] Referenz
[(X)] Zeiger
************************************************************************

### Zeiger und Referenzen als Rückgabewerte
> Wo liegt der Fehler im folgenden Programm?
```cpp
#include <iostream>
using namespace std;

int& doCalc(int &wert) {
  int a = wert++;
  return a;
}

int main(void) {
  int b = 0;
  cout << doCalc(b);
  return 0;
}
```
[(X)] Die mit `return` übergebene Referenz zeigt außerhalb der Funktion `doCalc` auf einen nicht existierenden Speicherplatz
[( )] Referenzen dürfen nicht für die Rückgabe mit `return` verwendet werden

{{1}}
************************************************************************
> Für die Variable `volumen` soll der Speicherplatz dynamisch zur Verfügung gestellt werden. Ersetzen Sie `[_____]` um die notwendige Ergängung der Anweisung.
```cpp
#include <iostream>
#include <cmath>
using namespace std;

double* kugelvolumen(double durchmesser) {
  double *volumen = [_____]
  *volumen = (4.0/3.0) * M_PI * pow(durchmesser / 2, 3);
  return volumen;
}

int main(void) {
  double wert = 5.0;
  double *volumen;
  volumen = kugelvolumen(wert);
  cout << "Das Kugelvolumen beträgt für d=" << wert << "[m] " << *volumen << "[m³] \n";
  delete volumen;
  return 0;
}
```
[[new double;]]
************************************************************************

### `main`-Funktion
> Beurteilen Sie ob folgende Aussagen wahr oder falsch sind.
- [[Wahr]        [Falsch]]
- [(X)           ( )     ]  In jedem Programm darf es nur eine (1) `main`-Fuktion geben.
- [( )           (X)     ]  Solange alle Funktionen `void` zurückgeben darf es auch mehrere `main`-Funktionen geben.
- [( )           (X)     ]  `argc` wird als erstes Argument in der Befehlszeile übergeben und kann alle ganzzahligen positiven Werte grösser 0 annehmen.
- [( )           (X)     ]  `argc` ist ein Array von Befehlszeilenargumenten.
- [(X)           ( )     ]  `argv` ist ein Array von Befehlszeilenargumenten.
- [(X)           ( )     ]  `argv[0]` ist das Programm selbst.

{{1}}
************************************************************************
> Was ist `argv[argc]`?
[(X)] NULL-Zeiger
[( )] Das letzte Argument im der Befehlszeile
************************************************************************

{{2}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms wenn die kompilierte Version des Programms intern mit `./a.out 3 2 1 Maus im Haus` aufgerufen wird?
```cpp
#include <iostream>
using namespace std;

int main(int argc, char *argv[]) {
  cout << argv[4];
  return 0;
}
```
[[Maus]]
************************************************************************
