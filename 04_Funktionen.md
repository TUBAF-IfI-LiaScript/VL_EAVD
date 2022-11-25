<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner


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

## Motivation

**Einführungsbeispiel**

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
Rückgabedatentyp Funktionsname([Parameterliste]) {
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
  Variablen.

* Parameterliste - Parameter sind Variablen (oder Pointer bzw. Referenzen darauf) die durch
  einen Datentyp und einen Namen spezifiziert werden. Mehrere Parameter
  werden durch Kommas getrennt.

  Parameterliste ist optional, die Klammern jedoch nicht.  Alternative zur
  fehlenden Parameterliste ist die Liste aus einen Parameter vom Datentyp `void` ohne Angabe des Namen.

* Anweisungsblock - Der Anweisungsblock umfasst die im Rahmen der
  Funktion auszuführenden Anweisungen und Deklarationen. Er wird
  durch geschweifte Klammern gekapselt.

Die Funktionsdefinition wird für jede Funktion genau einmal benötigt.

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

Der Funktionsaufruf einer Funktionen mit dem Rückgabewert ist meistens Teil
einer Anweisung, z.B. einer Zuweisung oder einer Ausgabeanweisung.

```cpp                              callAFunction.cpp
#include <iostream>
#include <cmath>
using namespace std;

void Info(){
    cout<<"Dieses Programm rundet Zahlenwerte.\n";
    cout<<"-----------------------------------\n";
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
}

int main(void){
    Info();
    float input = 8.4535;
    cout<<"Eingabewert "<<input<<" - Ausgabewert "<<runden(input)<<"\n";
    cout<<"Eingabewert "<<input<<" - Ausgabewert "<<rundenf(input,2)<<"\n";
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out -lm`, `./a.out`)


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


### asdfas

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
die Funktion erst nach dem Aufruf definiert. Hier erfolgt eine automatische
(implizite) Deklaration. Der Complier zeigt dies aber durch ein *Warning* an.

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

Bisher wurden Funktionen betrachtet, die skalare Werte als Parameter erhilten
und ebenfalls einen skalaren Wert als einen Rückgabewert lieferten. Allerdings
ist diese Möglichkeit sehr einschränkend.

Es wird in vielen Programmiersprachen, darunter in C/C++, zwei Arten der
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
Unabhängig von der Notation entspricht die Größe des übergebenen Arrays der Difinition in der
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
`argv` ist ein Array von Befehlszeilenargumenten, wobei argv[0] das Programm selbst und argv[argc] immer NULL ist.

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

### `inline`-Funktionen

Der `inline`-Funktion wird das Schlüsselwort `inline` vorangestellt, z.B.:

```cpp
inline void ausgabeBruch(int z, int n) {
   std::cout<<z<<" / "<<n<<"\n";
}
```

`inline`-Funktion wird vom Compiler direkt an der Stelle eingefügt, wo der Aufruf
stattfinden soll. Gegebenenfalls ist die Ausführung der `inline`-Funktion schneller,
da die mit dem Aufruf verbundenen Sicherung der Rücksprungadresse, der Sprung zur
Funktion und der Rücksprung nach Ausführung entfallen. Das Schlüsselwort `inline`
ist für den Compiler allerdings nur ein Hinweis und kein Befehl.


## Beispiel des Tages

Eine Funktion, die sich selbst aufruft, wird als rekursive Funktion bezeichnet. Den Aufruf selbst nennt man Rekursion. Als Beispiel dient die  Fakultäts-Funktion `n!`, die sich rekursiv als $n(n-1)!$ definieren lässt (wobei $0! = 1$).

```cpp                fakultaet.cpp
#include <iostream>
using namespace std;

int fakultaet (int a){
  if (a == 0)
    return 1;
  else
    return (a * fakultaet(a-1));
}

int main(){
  int eingabe;
  cout<<"Ganze Zahl eingeben: ";
  cin>>eingabe;
  cout<<"Fakultaet der Zahl: "<<fakultaet(eingabe)<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

<!--START_SKIP_IN_PDF-->
