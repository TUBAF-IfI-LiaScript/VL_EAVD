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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/03_ArrayZeigerReferenzen.md)

# Grundlagen der Sprache C++

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2022/23`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Array, Zeiger und Referenzen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/03_ArrayZeigerReferenzen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/03_ArrayZeigerReferenzen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Was ist ein Array?
* Wie können zwei Arrays verglichen werden?
* Erklären Sie die Idee des Zeigers in der Programmiersprache C/C++.
* Welche Gefahr besteht bei der Initialisierung von Zeigern?
* Was ist ein `NULL`-Zeiger und wozu wird er verwendet?

---------------------------------------------------------------------

## Wie weit waren wir gekommen?

> Aufgabe: Die LED blinkt im Beispiel 10 mal. Integrieren Sie eine Abbruchbedingung für diese Schleife, wenn der rote Button gedrückt wird. Welches Problem sehen Sie?

<div>
  <wokwi-pushbutton color="green" pin="2"  port="D"></wokwi-pushbutton>
  <wokwi-pushbutton color="red" pin="3"  port="D"></wokwi-pushbutton>
  <wokwi-led color="red"   pin="13" port="B" label="13"></wokwi-led>
</div>

```cpp       ButtonLogic.cpp
void setup() {
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  pinMode(13, OUTPUT);
}

void loop() {
  bool a = digitalRead(2);
  if (a){
    for (int i = 0; i<10; i++){
      digitalWrite(13, HIGH);
      delay(250);
      digitalWrite(13, LOW);
      delay(250);
    }
  }
}
```
@AVR8js.sketch

## Arrays

Bisher umfassten unsere Variablen einzelne Skalare. Arrays erweitern das
Spektrum um Folgen von Werten, die in n-Dimensionen aufgestellt werden können.
Array ist eine geordnete Folge von Werten des gleichen Datentyps.
Die Deklaration erfolgt in folgender Anweisung:

```text
Datentyp Variablenname[Anzahl_der_Elemente];
```

```cpp
int a[6];
```

| `a[0]` | `a[1]` | `a[2]` | `a[3]` | `a[4]` | `a[5]` |


```text
Datentyp Variablenname[Anzahl_der_Elemente_Dim0][Anzahl_der_Elemente_Dim1];
```

```cpp
int a[3][5];
```

|            | Spalten   |           |           |           |           |
| ---------- | --------- | --------- | --------- | --------- | --------- |
| **Zeilen** | `a[0][0]` | `a[0][1]` | `a[0][2]` | `a[0][3]` | `a[0][4]` |
|            | `a[1][0]` | `a[1][1]` | `a[1][2]` | `a[1][3]` | `a[1][4]` |
|            | `a[2][0]` | `a[2][1]` | `a[2][2]` | `a[2][3]` | `a[2][4]` |

> **Achtung 1:** Im hier beschriebenen Format muss zum Zeitpunkt der Übersetzung
> die Größe des Arrays (Anzahl\_der\_Elemente) bekannt sein.

> **Achtung 2:** Der Variablenname steht nunmehr nicht für einen Wert sondern
> für die Speicheradresse (Pointer) des ersten Elementes!

### Deklaration, Definition, Initialisierung, Zugriff

Initialisierung und genereller Zugriff auf die einzelnen Elemente des Arrays
sind über einen Index möglich.

```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main(void) {
  int a[3];       // Array aus 3 int Werten
  a[0] = -2;
  a[1] = 5;
  a[2] = 99;
  for (int i=0; i<3; i++)
    cout<<a[i]<<" ";
  cout<<"\nNur zur Info "<< sizeof(a);
  cout<<"\nZahl der Elemente "<< sizeof(a) / sizeof(int);
  return 0;
  }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=%23include%20%3Cstdio.h%3E%0A%0Aint%20main%28void%29%20%7B%0A%20%20int%20a%5B3%5D%3B%20%20%20%20%20%20%20//%20Array%20aus%203%20int%20Werten%0A%20%20a%5B0%5D%20%3D%20-2%3B%0A%20%20a%5B1%5D%20%3D%205%3B%0A%20%20a%5B2%5D%20%3D%2099%3B%0A%20%20for%20%28int%20i%3D0%3B%20i%3C3%3B%20i%2B%2B%29%0A%20%20%20%20printf%28%22%25d%20%22,%20a%5Bi%5D%29%3B%0A%20%20printf%28%22%5CnNur%20zur%20Info%20%25ld%22,%20sizeof%28a%29%29%3B%0A%20%20printf%28%22%5CnZahl%20der%20Elemente%20%25ld%22,%20sizeof%28a%29%20/%20sizeof%28int%29%29%3B%0A%20%20printf%28%22%5CnAnwendung%20des%20Adressoperators%20auf%20das%20Array%20%25d%22,%20*a%29%3B%0A%20%20return%200%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=c&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>


{{1}}
Wie können Arrays noch initialisiert werden:

{{1}}
+ vollständig (alle Elemente werden mit einem spezifischen Wert belegt)
+ anteilig (einzelne Elemente werden mit spezfischen Werten gefüllt, der rest mit 0)

{{1}}
```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main(void) {
  int a[] = {5, 2, 2, 5, 6};
  float b[5] = {1.0};
  for (int i=0; i<5; i++){
      cout<<a[i]<<" "<< b[i]<<"\n";
    }
  return 0;
}
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Und wie bestimme ich den erforderlichen Speicherbedarf bzw. die Größe des
Arrays?

{{2}}
```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main(void) {
  int a[3];
  cout<<"\nNur zur Speicherplatz [Byte] "<<sizeof(a);
  cout<<"\nZahl der Elemente "<<sizeof(a)/sizeof(int)<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Fehlerquelle Nummer 1 - out of range

```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main(void) {
  int a[] = {-2, 5, 99};
  for (int i=0; i<=3; i++)
    cout<<a[i]<<" ";
  return 0;
  }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


### Anwendung eines eindimesionalen Arrays

Schreiben Sie ein Programm, das zwei Vektoren miteinander vergleicht. Warum ist
die intuitive Lösung `a == b` nicht korrekt, wenn `a` und `b` arrays sind?

```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main(void) {
  int a[] = {0, 1, 2, 4, 3, 5, 6, 7, 8, 9};
  int b[10];
  for (int i=0; i<10; i++)
    b[i]=i;
  for (int i=0; i<10; i++)
    if (a[i]!=b[i])
      cout<<"An Stelle "<<i<<" unterscheiden sich die Vektoren \n";
  return 0;
  }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Welche Verbesserungsmöglichkeiten sehen Sie bei dem Programm?

### Mehrdimensionale Arrays

Deklaration:

```cpp
int Matrix[4][5];    /* Zweidimensional - 4 Zeilen x 5 Spalten */
```

Deklaration mit einer sofortigen Initialisierung aller bzw. einiger Elemente:

```cpp
int Matrix[4][5] = { {1,2,3,4,5},
                     {6,7,8,9,10},
                     {11,12,13,14,15},
                     {16,17,18,19,20}};

int Matrix[4][4] = { {1,},
                     {1,1},
                     {1,1,1},
                     {1,1,1,1}};

int Matrix[4][4] = {1,2,3,4,5,6,7,8};
```

{{1}}
Initialisierung eines n-dimensionalen Arrays:

{{1}}
![Matrix](./images/04_ZeigerUndArrays/2DArray.jpg)<!--
style=" width: 60%;
        max-width: 800px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

{{2}}
```cpp                          nDimArray.cpp
#include <iostream>
using namespace std;

int main(void) {
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
  		cout<<brett[i][j]<<" ";
  	}
  	cout<<"\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Quelle: [C-Kurs](http://www.c-howto.de/tutorial/arrays-felder/zweidimensionale-felder/)

### Anwendung eines zweidimesionalen Arrays

Elementwese Addition zweier Matrizen

```cpp       Addition.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int A[2][3]={{1,2,3},{4,5,6}};
  int B[2][3]={{10,20,30},{40,50,60}};
	int C[2][3];
	int i,j;
	for (i=0;i<2;i++)
		for (j=0;j<3;j++)
			C[i][j]=A[i][j]+B[i][j];
	for (i=0;i<2;i++)
	{
		for (j=0;j<3;j++)
			cout<<C[i][j]<<"\t";
		cout<<"\n";
	}
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

[Multiplikation zweier Matrizen](https://www.codewithc.com/c-program-for-gauss-elimination-method/)


### Strings/Zeichenketten

Folgen von Zeichen, die sogenannten *Strings* werden in C/C++ durch Arrays mit
Elementen vom Datentyp `char` repräsentiert. Die Zeichenfolgen werden mit
`\0` abgeschlossen.

> **Merke:** C++ stellt mit dem Header `<string>` ebenfalls einen Standartdatentyp `string` mit zahlreichen Funktionen zur Verfügung.

```cpp                                         stringarray.cpp
#include <iostream>
using namespace std;

int main(void) {
  cout<<"Diese Form eines Strings haben wir bereits mehrfach benutzt!\n";
  //////////////////////////////////////////////////////////////////////////////

  char a[] = "Ich bin ein char Array!";  // Der Compiler fügt das \0 automatisch ein!
  if (a[23] == '\0'){
    cout<<"char Array Abschluss in a gefunden!";
  }

  cout<<"->"<<a<<"<-\n";
  char b[] = { 'H', 'a', 'l', 'l', 'o', ' ',
               'F', 'r', 'e', 'i', 'b', 'e', 'r', 'g', '\0' };
  cout<<"->"<<b<<"<-\n";
  char c[] = "Noch eine \0Moeglichkeit";
  cout<<"->"<<c<<"<-\n";
  char d[] = { 80, 114, 111, 122, 80, 114, 111, 103, 32, 50, 48,  50, 50,  0  };
  cout<<"->"<<d<<"<-\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
Wie kopiere ich die Inhalte in einem Array?

{{1}}
```cpp                     arrayStrCopy1.cpp
#include <iostream>
using namespace std;

#include <string.h>       // notwendig für strcpy

int main(void) {
  char a[] = "012345678901234567890123456789";
  strcpy(a, "Das ist ein neuer Text");
  cout<<a<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
```cpp                     arrayStrCopy2.cpp
#include <iostream>
#include <string>
using namespace std;

int main(void) {
  char a[]="012345678901234567890123456789";
  string b="Das ist ein neuer Text";
  size_t length = b.copy(a,b.size(),0);
  a[length]='\0';
  cout<<a<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Anwendung von Zeichenketten

Schreiben Sie ein Programm, dass in einem Text groß geschriebene Buchstaben
durch klein geschriebene ersetzt und umgekehrt.

![Matrix](./images/01_EinAusgabeDatentypen/ASCII_Zeichensatz.jpeg)<!--
style=" width: 60%;
        max-width: 800px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

Da Variablen des Datentyps `char` genau ein Byte benötigen, liefert `sizeof`-Operator im folgenden Beispiel die Anzahl der Elemente des Arrays.


```cpp                     ArrayExample.cpp
#include <iostream>
using namespace std;

int main() {
  char a[] = "Das ist ein beispielhafter Text.";
  char b[sizeof a];
  for (int i=0; i< sizeof a; i++){
    b[i] = a[i];
    if ((a[i]>=65) && (a[i]<=90))
        b[i] = a[i] + 32;
    if ((a[i]>=97) && (a[i]<=122))
        b[i] = a[i] - 32;
  }
  cout<<a<<"\n";
  cout<<b<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


### Fehlerquellen

Bitte unterscheiden Sie die Initialisierungsphase von normalen Zuweisungen,
bei denen Sie nur auf einzelne Elemente zugreifen können.

```cpp                     arrayInitVsAssignment.cpp
#include <iostream>
using namespace std;

#include <string.h>       // notwendig für strcpy

int main(void) {
  char a[] = "Das ist der Originaltext";
  a = "Das ist ein neuer Text";  // Compiler Error
  //strcpy(a, "Das ist ein neuer Text");
  a[0]='X';
  cout<<a<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


## Grundkonzept Zeiger

Bisher umfassten unserer Variablen als Datencontainer Zahlen oder Buchstaben.
Das Konzept des Zeigers (englisch Pointer) erweitert das Spektrum der Inhalte
auf Adressen.

An dieser Adresse können entweder Daten, wie Variablen oder Objekte, aber auch
Programmcodes (Anweisungen) stehen. Durch Dereferenzierung des Zeigers ist es
möglich, auf die Daten oder den Code zuzugreifen.

<!--
style=" width: 70%;
        max-width: 400x;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->
```ascii
  Variablen-     Speicher-      Inhalt
  name           addresse
                                +----------+
                 0000           |          |
                                +----------+
                 0001           |          |
                                +----------+
  a   ------>    0002       +---| 00001007 | Adresse
                          z |   +----------+
                 0003     e |   |          |
                          i |   +----------+
                 ....     g |   |          |
                          t |   +----------+
                 1005       |   |          |
                          a |   +----------+
                 1006     u |   |          |
                          f |   +----------+
  b   ------>    1007    <--+   | 00001101 |  Wert = 13
                                +----------+
                 1008           |          |
                                +----------+
                 ....           |          |                                   .
```


Welche Vorteile ergeben sich aus der Nutzung von Zeigern, bzw. welche
Programmiertechniken lassen sich realisieren:

* dynamische Verwaltung von Speicherbereichen,
* Übergabe von Datenobjekten an Funktionen via "call-by-reference",
* Übergabe von Funktionen als Argumente an andere Funktionen,
* Umsetzung rekursiver Datenstrukturen wie Listen und Bäume.

> An dieser Stelle sei erwähnt, dass die Übergabe der "call-by-reference"-Parameter via Reference ist ebenfalls möglich und einfacher in der Handhabung.

### Definition von Zeigern

Die Definition eines Zeigers besteht aus dem Datentyp des Zeigers und dem
gewünschten Zeigernamen. Der Datentyp eines Zeigers besteht wiederum aus dem
Datentyp des Werts auf den gezeigt wird sowie aus einem Asterisk. Ein Datentyp
eines Zeigers wäre also z. B. `double*`.

```cpp
/* kann eine Adresse aufnehmen, die auf einen Wert vom Typ Integer zeigt */
int* zeiger1;
/* das Leerzeichen kann sich vor oder nach dem Stern befinden */
float *zeiger2;
/* ebenfalls möglich */
char * zeiger3;
/* Definition von zwei Zeigern */
int *zeiger4, *zeiger5;
/* Definition eines Zeigers und einer Variablen vom Typ Integer */
int *zeiger6, ganzzahl;
```


### Initialisierung

> **Merke:** Zeiger müssen vor der Verwendung initialisiert werden.

Der Zeiger kann initialisiert werden durch die Zuweisung:
* der Adresse einer Variable, wobei die Adresse mit Hilfe des Adressoperators
  `&` ermittelt wird,
* eines Arrays,
* eines weiteren Zeigers oder
* des Wertes von `NULL`.

```cpp                      PointerExamples.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int a = 0;
  int * ptr_a = &a;       /* mit Adressoperator */

  int feld[10];
  int * ptr_feld = feld;  /* mit Array */

  int * ptr_b = ptr_a;    /* mit weiterem Zeiger */

  int * ptr_Null = NULL;  /* mit NULL */

  cout<<"Pointer ptr_a    "<<ptr_a<<"\n";
  cout<<"Pointer ptr_feld "<<ptr_feld<<"\n";
  cout<<"Pointer ptr_b    "<<ptr_b<<"\n";
  cout<<"Pointer ptr_Null "<<ptr_Null<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{1}}
Die konkrete Zuordnung einer Variablen im Speicher wird durch den Compiler und
das Betriebssystem bestimmt. Entsprechend kann die Adresse einer Variablen nicht
durch den Programmierer festgelegt werden. Ohne Manipulationen ist die Adresse
einer Variablen über die gesamte Laufzeit des Programms unveränderlich, ist aber
bei mehrmaligen Programmstarts unterschiedlich.

{{1}}
In den Ausgaben von Pointer wird dann eine
hexadezimale Adresse ausgegeben.

{{1}}
Zeiger können mit dem "Wert" `NULL` als ungültig markiert werden. Eine
Dereferenzierung führt dann meistens zu einem Laufzeitfehler nebst
Programmabbruch. NULL ist ein Macro und wird in mehreren Header-Dateien
definiert (mindestens in `<cstddef>` (`stddef.h`)). Die Definition ist vom Standard
implementierungsabhängig vorgegeben und vom Compilerhersteller passend
implementiert, z. B.

{{1}}
```cpp
#define NULL 0
#define NULL 0L
#define NULL (void *) 0
```

{{2}}
Und umgekehrt, wie erhalten wir den Wert, auf den der Pointer zeigt? Hierfür
benötigen wir den *Inhaltsoperator* `*`.

{{2}}
```cpp                   DereferencingPointers.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int a = 15;
  int * ptr_a = &a;
  cout<<"Wert von a                     "<<a<<"\n";
  cout<<"Pointer ptr_a                  "<<ptr_a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<*ptr_a<<"\n";
  *ptr_a = 10;
  cout<<"Wert von a                     "<<a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<*ptr_a<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
<iframe width="800" height="500" frameborder="0" src="http://pythontutor.com/iframe-embed.html#code=%23include%20%3Cstdio.h%3E%0A%23include%20%3Cstdlib.h%3E%0A%0Aint%20main%28void%29%0A%7B%0A%20%20int%20a%20%3D%2015%3B%0A%20%20int%20*%20ptr_a%20%3D%20%26a%3B%0A%20%20printf%28%22Wert%20von%20a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25d%5Cn%22,%20a%29%3B%0A%20%20printf%28%22Pointer%20ptr_a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25p%5Cn%22,%20ptr_a%29%3B%0A%20%20printf%28%22Wert%20hinter%20dem%20Pointer%20ptr_a%20%20%25d%5Cn%22,%20*ptr_a%29%3B%0A%20%20*ptr_a%20%3D%2010%3B%0A%20%20printf%28%22Wert%20von%20a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25d%5Cn%22,%20a%29%3B%0A%20%20printf%28%22Wert%20hinter%20dem%20Pointer%20ptr_a%20%20%25d%5Cn%22,%20*ptr_a%29%3B%0A%20%20return%20EXIT_SUCCESS%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=c&rawInputLstJSON=%5B%5D&textReferences=false"> </iframe>

### Fehlerquellen

Fehlender Adressoperator bei der Zuweisung

```cpp               PointerFailuresI.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int a = 5;
  int * ptr_a;
  ptr_a = a;
  cout<<"Pointer ptr_a                  "<<ptr_a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<*ptr_a<<"\n";
  cout<<"Aus Maus!\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
Fehlender Dereferenzierungsoperator beim Zugriff

{{1}}
```cpp          PointerFailuresII.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int a = 5;
  int * ptr_a = &a;
  cout<<"Pointer ptr_a                  "<<(void*)ptr_a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<ptr_a<<"\n";
  cout<<"Aus Maus!\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Uninitialierte Pointer zeigen "irgendwo ins nirgendwo"!

{{2}}
```cpp                  PointerFailuresIII.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int * ptr_a;
  *ptr_a = 10;
  // korrekte Initalisierung
  // int * ptr_a = NULL;
  // Prüfung auf gültige Adresse
  // if (ptr_a != NULL) *ptr_a = 10;
  cout<<"Pointer ptr_a                  "<<ptr_a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<*ptr_a<<"\n";
  cout<<"Aus Maus!\n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Dynamische Datenobjekte

C++ bietet die Möglichkeit den Speicherplatz für eine Variable zur Laufzeit zur Verfügung zu stellen.
Mit `new`-Operator wird der Speichrerplatz bereit gestellt und mit `delete`-Operator (`delete[]`) wieder freigegeben.

`new` erkennt die benötigte Speichermenge am angegebenen Datentyp und reserviert für die Variable auf dem Heap die entsperechde Byte-Menge.

```cpp                   new.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int * ptr_a;
  ptr_a=new int;
  *ptr_a = 10;
  cout<<"Pointer ptr_a                  "<<ptr_a<<"\n";
  cout<<"Wert hinter dem Pointer ptr_a  "<<*ptr_a<<"\n";
  cout<<"Aus Maus!\n";
  delete ptr_a;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

```cpp                   newArray.cpp
#include <iostream>
using namespace std;

int main(void)
{
  int * ptr_a;
  ptr_a=new int[3];
  ptr_a[0] = ptr_a[1] = ptr_a[2] = 42;
  cout<<"Werte hinter dem Pointer ptr_a:  ";
  for (int i=0;i<3;i++) cout<<ptr_a[i]<<" ";
  cout<<"\n";
  cout<<"Aus Maus!\n";
  delete[] ptr_a;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

+ `delete` daft nur einmal auf ein Objekt angewendet werden
+ `delete` daft ausschließlich auf mit new angelegte Objekte oder NULL-Pointer angewandt werden
+ Nach der Verwendung von `delete` ist das Objekt *undefiniert* (nicht gleich NULL)

> **Merke:** Die Verwendung von Zeigern kann zur unerwünschten Speicherfragmentierung und die Programmierfehler zu den Programmabstürzen und Speicherlecks führen. *Intelligente* Zeiger stellen sicher, dass Programme frei von Arbeitsspeicher- und Ressourcenverlusten sind.


## Referenz

Eine Referenz ist eine Datentyp, der Verweis (Aliasnamen) auf ein Objekt liefert und ist genau wie eine Variable zu benutzen ist.
Der Vorteil der Referenzen gegenüber den Zeigern besteht in der einfachen Nutzung:

+ Dereferenzierung ist nicht notwendig, der Compiler löst die Referenz selbst auf
+ Freigabe ist ebenfalls nicht notwendig

> **Merke:** Auch Referenzen müssen vor der Verwendung initialisiert werden. Eine Referenz bezieht sich immer auf ein existierendes Objekt, sie kann nie NULL sein

```cpp referenzen.cpp
#include <iostream>
using namespace std;

int main(void)
{
int  a = 1;  // Variable
int &r = a;  // Referenz auf die Variable a

std::cout << "a: " << a << " r: " << r << std::endl;
std::cout << "a: " << &a << " r: " << &r << std::endl;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Die Referenzen werden verwendet:

+ zur "call bei reference"-Parameterübergabe
+ zur Optimierung des Programms, um Kopien von Objekten zu vermeiden
+ in speziellen Memberfunktionen, wie Copy-Konstruktor und Zuweisungsoperator
+ als sogenannte universelle Referenz (engl.: universal reference), die bei Templates einen beliebigen Parametertyp repräsentiert.

> **Achtung:** Zur dynamischen Verwaltung von Speicherbereichen sind Referenzen nicht geeignet.


## Beispiel der Woche

Gegeben ist ein Array, das eine sortierte Reihung von Ganzzahlen umfasst.
Geben Sie alle Paare von Einträgen zurück, die in der Summe 18 ergeben.

Die intuitive Lösung entwirft einen kreuzweisen Vergleich aller sinnvollen Kombinationen
der $n$ Einträge im Array. Dafür müssen wir $(n-1)^2 /2$ Kombinationen bilden.

<!-- data-type="none" style="table-layout: fixed; max-width:950px;"-->
|     | 1   | 2   | 5   | 7   | 9   | 10  | 12  | 13  | 16  | 17  | 18  | 21  | 25  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1   | x   |     |     |     |     |     |     |     |     | 18  |     |     |     |
| 2   | x   | x   |     |     |     |     |     |     | 18  |     |     |     |     |
| 5   | x   | x   | x   |     |     |     |     | 18  |     |     |     |     |     |
| 7   | x   | x   | x   | x   |     |     |     |     |     |     |     |     |     |
| 9   | x   | x   | x   | x   | x   |     |     |     |     |     |     |     |     |
| 10  | x   | x   | x   | x   | x   | x   |     |     |     |     |     |     |     |
| 12  | x   | x   | x   | x   | x   | x   | x   |     |     |     |     |     |     |
| 13  | x   | x   | x   | x   | x   | x   | x   | x   |     |     |     |     |     |
| 16  | x   | x   | x   | x   | x   | x   | x   | x   | x   |     |     |     |     |
| 17  | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   |     |     |     |
| 18  | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   |     |     |
| 21  | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   |     |
| 25  | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   | x   |

Haben Sie eine bessere Idee?

```cpp                             Pairing.cpp
#include <iostream>
using namespace std;
#define ZIELWERT 18

int main(void)
{
  int a[] = {1, 2, 5, 7, 9, 10, 12, 13, 16, 17, 18, 21, 25};
  int i_left=0;
  int i_right=12;
  cout<<"Value left "<<a[i_left]<<" right "<<a[i_right]<<"\n-----------------------\n";
  do{
    cout<<"Value left "<<a[i_left]<<" right "<<a[i_right];
    if (a[i_right] + a[i_left] == ZIELWERT){
       cout<<" -> TREFFER";
    }
    cout<<"\n";
    if (a[i_right] + a[i_left] >= ZIELWERT) i_right--;
    else i_left++;
  }while (i_right != i_left);
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

<!--START_SKIP_IN_PDF-->
