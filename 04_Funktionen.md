<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.4
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/04_Funktionen.md)

# Grundlagen der Sprache C++

| Parameter                 | Kursinformationen                                                                                                                                          |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | @config.lecture                                                                                                                                            |
| **Semester**              | @config.semester                                                                                                                                           |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                          |
| **Inhalte:**              | `Funktionen`                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_Funktionen.md) |
| **Autoren**               | @author                                                                                                                                                    |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Welche Komponenten beschreiben Definition einer Funktion?
* Wozu werden in der Funktion die Parameter gebraucht?
* Wann ist es sinnvoll Referenzen-Parameter zu verwenden?
* Warum ist es sinnvoll Funktionen in Look-Up-Tables abzubilden, letztendlich
  kostet das Ganze doch Speicherplatz?

---------------------------------------------------------------------

## Motivation

Erklären Sie die Idee hinter folgendem Code.

```cpp                          onBlock.cpp
#include <iostream>
#include <cmath>
#include <iomanip>

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
  for (int i=0; i<12; i++){
     std::cout << std::setw(2) <<  i << " ";
  }
  std::cout << std::endl;
  for (int i=0; i<12; i++){
     std::cout << std::setw(2) << a[i] << " ";
  }
  std::cout << std::endl;
  // Ausgabe Mittelwert
  cout<<"Die Summe betraegt "<<summe<<", der Mittelwert "<<mittelwert<<"\n";
  // Ausgabe Standardabweichung
  float stdabw = sqrt(abweichung / VALUECOUNT);
  cout<<"Die Standardabweichung der Grundgesamtheit betraegt "<<stdabw<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)

Sie wollen den Code in einem neuen Projekt wiederverwenden. Was sind
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

> Finden Sie Fehler im zuvor gezeigten Code?

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
>[Google Sthttps://stackoverflow.com/questions/2485963/c-alignmtionen 

![](https://media.giphy.com/media/xT9IgzoKnwFNmISR8I/giphy.gif)

## Funktionen in C++

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

                        {{0-1}}
*******************************************************

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

int main(void){
    info();
    float input = -8.4565;
    cout<<"Eingabewert "<<input<<" - Ausgabewert "<<runden(input)<<"\n";
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

*******************************************************

                        {{1-2}}
*******************************************************

> __Hinweis:__ C++ unterstützt gleiche Codenahmen bei unterschiedlichen Parametern. Der Compiler "sucht sich" die passende Funktion aus. Der Mechanismus wird als _Funktionsüberladung_ bezeichnet. 

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


> Welche Verbesserungsmöglichkeit sehen Sie bei dem Programm? Tipp: Wie können wir den redundanten Code eliminieren?

*******************************************************

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

// int foo(void); // Explizite Einführung der Funktion foo()

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
Das Ganze wird dann relevant, wenn Funktionen aus anderen Quellcodedateien
eingefügt werden sollen. Die Deklaration macht den Compiler mit dem Aussehen der
Funktion bekannt. Diese werden mit dem Schlüsselwort `extern`  markiert.

{{1}}
```cpp
extern float berechneFlaeche(float breite, float hoehe);
```

## Parameterübergabe und Rückgabewerte

Bisher wurden Funktionen betrachtet, die skalare Werte als Parameter erhielten
und ebenfalls einen skalaren Wert als einen Rückgabewert lieferten. Allerdings
ist diese Möglichkeit sehr einschränkend.

```cpp          Student.cpp
#include <iostream>
using namespace std;

#include <iostream>
using namespace std;

//           Rückgabe der Ergebnisse
//  +------------------------------------+
//  |                                    |
   int add(int a, int b){ // <--+        |
      return a+b;         //    | Aufruf |   
   }                      //    | mit    |   
                          //    | Para-  |   
   int main(void) {       //    | metern |  
     int i = add(5, 6);   //----+        |  
//    ^                                  |  
//    +----------------------------------+
     cout<<"i="<<i<<"\n";
     return 0;
   }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Es wird in vielen Programmiersprachen, darunter in C/C++, zwei generelle Konzepte der
Parameterübergabe realisiert.

### Call-by-Value

In allen Beispielen bis jetzt wurden Parameter an die Funktionen *call-by-value*,
übergeben. Das bedeutet, dass innerhalb der aufgerufenen Funktion mit einer
Kopie der Variable gearbeitet wird und die Änderungen sich nicht auf den
ursprünglichen Wert auswirken.

```cpp          Student.cpp
#include <iostream>
using namespace std;

void doSomething(int a) {
   // eine KOPIE von a wird um 1 erhöht
   cout << ++a << " a in der Schleife\n";
}

int main(void) {
  int a = 5;
  cout << a << " a in main\n";
  doSomething(a);
  cout << a << " a in main\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Merke:** Die _Call-by-value-_Funktionen können den Wert der Variablen nicht verändern.

### Call-by-Reference

Bei einer Übergabe als Referenz wirken sich Änderungen an den Parametern auf die
ursprünglichen Werte aus, es werden keine Kopien von Parametern angelegt.
*Call-by-reference* wird unbedingt notwendig, wenn eine
Funktion mehrere Rückgabewerte hat.

> In C++ kann die "call-by-reference"- Parameterübergabe mit Hilfe der Referenzen oder Pointern
realisiert werden. 


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

Es besteht ebenfalls die Möglichkeit, "call-by-reference"- Parameterübergabe mit Hilfe der Zeiger (Pointer)
zu realisieren. 

```cpp                   ParameterII.cpp
#include <iostream>
#include <cmath>
using namespace std;

double hypothenuse(double *lookup_sin, int winkel, double gegenkathete){
  return gegenkathete/lookup_sin[angle];
}
/*
double hypothenuse(double lookup_sin[], int winkel, double gegenkathete){
  return gegenkathete/lookup_sin[angle];
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
    cout<<"sizeof of array as parameter: "<<sizeof(intArray)<<"\n";
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
    
    cout<<"Size of int pointer: "<< sizeof(int*) <<"\n";
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

```c++                        Functions.cpp
#include <iostream>
#include <cmath>
#include <iomanip>

using namespace std;

double Mittelwert(int *values, int entries);
int Summe(int *values, int entries);
void Ausgabe(int *values, int entries);

double Mittelwert(int *values, int entries){
  double summe = Summe(values, entries);
  return summe / entries;
}

int Summe(int *values, int entries){
  int summe = 0;
  for (int i=0; i<entries; i++){
    summe += values[i];
  }
  return summe;
}

void Ausgabe(int *values, int entries){
  for (int i=0; i<entries; i++){
     std::cout << std::setw(2) <<  i << " ";
  }
  std::cout << std::endl;
  for (int i=0; i<entries; i++){
     std::cout << std::setw(2) << values[i] << " ";
  }
  std::cout << std::endl;
}

int main(void) {
  int a [] = {1,2,3,3,4,2,3,4,5,6,7,8,9,1,2,3,3};
  const int entries = sizeof(a)/sizeof(a[0]);
  Ausgabe(a, entries);

  int summe = Summe(a, entries);
  double mittelwert = Mittelwert(a, entries);
  cout<<"Die Summe betraegt "<<summe<<", der Mittelwert "<<mittelwert<<"\n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall -Wconversion main.cpp -o a.out`, `./a.out`)


# Quiz
## Funktionen

Funktionsdefinitionen
===================

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

Aufruf von Fuktionen
===================

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

Fehler
===================

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

Funktionsdeklaration
===================

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


> Mit welcher dieser Anweisungen kann eine Funktion aus einer anderen Quellcodedatei einzufügt werden?
[(X)] `extern int x(int y, bool z);`
[( )] `import int x(int y, bool z);`
[( )] `using int x(int y, bool z);`


Parameterübergabe und Rückgabewerte
===================

> Ordnen Sie die Eigenschaften den entsprechenden Arten der Parameterübergabe zu.
- [[*call-by-value*] [*call-by-reference*]]
- [    ( )           (X)      ]  Ermöglicht mehrere Rückgabewerte
- [    (X)           ( )      ]  Arbeitet mit einer Kopie der Variablen
- [    (X)           ( )      ]  Beeinflusst nicht den tatsächlichen Wert von Variablen in der `main`
- [    ( )           (X)      ]  Beeinflusst den tatsächlichen Wert von Variablen in der `main`



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

> Womit werden Array-Parameter übergeben?
[( )] Referenz
[(X)] Zeiger


Zeiger und Referenzen als Rückgabewerte
===================

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

`main`-Funktion
===================

> Beurteilen Sie ob folgende Aussagen wahr oder falsch sind.
- [[Wahr]        [Falsch]]
- [(X)           ( )     ]  In jedem Programm darf es nur eine (1) `main`-Fuktion geben.
- [( )           (X)     ]  Solange alle Funktionen `void` zurückgeben darf es auch mehrere `main`-Funktionen geben.
- [( )           (X)     ]  `argc` wird als erstes Argument in der Befehlszeile übergeben und kann alle ganzzahligen positiven Werte grösser 0 annehmen.
- [( )           (X)     ]  `argc` ist ein Array von Befehlszeilenargumenten.
- [(X)           ( )     ]  `argv` ist ein Array von Befehlszeilenargumenten.
- [(X)           ( )     ]  `argv[0]` ist das Programm selbst.


> Was ist `argv[argc]`?
[(X)] NULL-Zeiger
[( )] Das letzte Argument in der Befehlszeile

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
