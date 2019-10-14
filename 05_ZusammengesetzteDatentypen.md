<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md
-->

# Vorlesung V - Strukturierte Datentypen

**Fragen an die heutige Veranstaltung ...**

* Was sind *Arrays*, `struct`s und `enum`s?
* Was sind Gemeinsamkeiten und was sind Unterschiede von *Strings* und *Arrays*?
* Welche Gefahren lauern bei der Arbeit mit *Arrays*?
* Welche Indexnummer hat das erste Element eines *Arrays*?
* Erklären Sie den Unterschied zwischen Initalisierung und Zuweisung.
* Wie vergleichen Sie zwei `structs`?

---------------------------------------------------------------------
Aktuelle Vorlesung im Versionsmanagementsystem GitHub:

[https://github.com/SebastianZug/CCourse/blob/master/05_ZusammengesetzteDatentypen.md](https://github.com/SebastianZug/CCourse/blob/master/05_ZusammengesetzteDatentypen.md)

----------------------------------------------------------------------

{{1}}
**Wie weit sind wir schon gekommen?**

{{1}}
ANSI C (C89)/ Schlüsselwörter:

{{1}}
| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | `auto`         | `double` | `int`      | struct   | `break`    |
|             | `else`         | `long`   | `switch`   | `case`   | enum       |
|             | `register`     | typedef  | `char`     | `extern` | return     |
|             | union          | `const`  | `float`    | `short`  | `unsigned` |
|             | `continue`     | `for`    | `signed`   | `void`   | `default`  |
|             | `goto`         | `sizeof` | `volatile` | `do`     | `if`       |
|             | `static`       | `while`  |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | inline   | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

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

## 1. Aufzählungen

Enumerationen, kurz `enum`, dienen der Definition bestimmter Sets von Elementen,
die eine Variable überhaupt annehmen kann. Wenn wir zum Beispiel die Farben
einer Ampel in einem Programm handhaben wollen, sind dies lediglich "Rot", "Gelb"
und "Grün". Im Schachspiel sind nur die Figuren "Bauer", "Pferd", "Springer",
"Turm", "Dame" und "König" definiert.

Die Definition eines Aufzählungsdatentyps `enum` hat die Form wie im folgenden
Beispiel:

```cpp
#include <stdio.h>

int main(void) {
  enum { karo, herz, pik, kreuz};                // Beispiel der Farben beim Skat
  // const int kreuz=0, pik=1, karo=2, herz=3;   // Analoge Anweisung
  int karte = karo;
  printf("Wert der Karte: %d\n", karte);
  return 0;
}
```
@Rextester.C


{{1}}
Möglicherweise sollen den Karten aber auch konkrete Werte zugeordnet werden,
die bestimmte Wertigkeiten reflektieren.

{{1}}
```cpp
#include <stdio.h>

int main(void) {
       // Beispiel der Farben beim Skat
  enum { karo=9, herz=10, pik=11, kreuz=12};
  int karte = karo;
  printf("Wert der Karte: %d\n", karte);
  return 0;
}
```
@Rextester.C

{{1}}
An dieser Stelle sind Sie aber frei, was die eigentlichen Werte angeht. Es sind
zum Beispiel Konfigurationen möglich wie

{{1}}
```cpp
enum { karo=9, herz=10, pik=11, kreuz=12};
enum { karo=9, herz, pik, kreuz};            // Gleiches Resultat
enum { karo=9, herz, pik=123, kreuz};        // implizit kreuz = 124
```

## 2. Arrays

Bisher umfassten unsere Variablen einzelne Skalare. Arrays erweitern das
Spektrum um Folgen von Werten, die in n-Dimensionen aufgestellt werden können.
Array ist eine geordnete Folge von Werten des gleichen Datyps.
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

| `a[0][0]` | `a[0][1]` | `a[0][2]` | `a[0][3]` | `a[0][4]` |
| `a[1][0]` | `a[1][1]` | `a[1][2]` | `a[1][3]` | `a[1][4]` |
| `a[2][0]` | `a[2][1]` | `a[2][2]` | `a[2][3]` | `a[2][4]` |


> **Achtung 1:** Im hier beschriebenen Format muss zum Zeitpunkt der Übersetzung
> die Größe des Arrays (Anzahl\_der\_Elemente) bekannt sein.

> **Achtung 2:** Der Variablenname steht nunmehr nicht für einen Wert sondern
> für die Speicheradresse des ersten Feldes!

### Deklaration, Definition, Initialisierung, Zugriff

Initialisierung und genereller Zugriff auf die einzelnen Elemente des Arrays
sind über einen Index möglich.

```cpp                     ArrayExample.c
#include <stdio.h>

int main(void) {
  int a[3];       // Array aus 3 int Werten
  a[0] = -2;
  a[1] = 5;
  a[2] = 99;
  for (int i=0; i<3; i++)
    printf("%d ", a[i]);
  printf("\nNur zur Info %ld", sizeof(a));
  printf("\nZahl der Elemente %ld", sizeof(a) / sizeof(int));
  printf("\nAnwendung des Adressoperators auf das Array %d", *a);
  return 0;
  }
```
@Rextester.C

{{1}}
Wie können Arrays noch initialisiert werden?

{{1}}
```cpp                     ArrayExample.c
#include <stdio.h>

int main(void) {
  int a[] = {5, 2, 2, 5, 6};   // Alternative Form der Initialisierung
  float b[5] = {1.0};
  for (int i=0; i<5; i++){
    printf("%d  %f\n", a[i], b[i]);
  }
  return 0;
}
```
@Rextester.C

{{2}}
Und wie bestimme ich den erforderlichen Speicherbedarf bzw. die Größe des
Arrays?

{{2}}
```cpp                     ArrayExample.c
#include <stdio.h>

int main(void) {
  int a[3];
  printf("\nNur zur Speicherplatz [Byte] %ld", sizeof(a));
  printf("\nZahl der Elemente %ld\n", sizeof(a)/sizeof(int));
  return 0;
}
```
@Rextester.C

### Fehlerquelle Nummer 1 - out of range

```cpp                     ArrayExample.c
#include <stdio.h>

int main(void) {
  int a[3];
  a[0] = -2; a[1] = 5; a[2] = 99;
  for (int i=0; i<=3; i++)
    printf("%d ", a[i]);
  return 0;
  }
```
@Rextester.C


### Anwendung eines eindimesionalen Arrays

Schreiben Sie ein Programm, das zwei Vektoren miteinander vergleicht. Warum ist
die intuitive Lösung `a == b` nicht korrekt, wenn `a` und `b` arrays sind?

```cpp                     ArrayExample.c
#include <stdio.h>

int main(void) {
  int a[] = {0, 1, 2, 4, 3, 5, 6, 7, 8, 9};
  int b[10];
  for (int i=0; i<10; i++)
    b[i]=i;
  for (int i=0; i<10; i++)
    if (a[i]!=b[i])
      printf("An Stelle %d unterscheiden sich die Vektoren \n", i);
  return 0;
  }
```
@Rextester.C

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
![Matrix](img/2DArray.jpg)<!--
style=" width: 90%;
        max-width: 800px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

{{2}}
```cpp                          nDimArray.c
#include <stdio.h>

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
  		printf("%d ", brett[i][j]);
  	}
  	printf("\n");
  }
  return 0;
}
```
@Rextester.C

{{2}}
Quelle: [C-Kurs](http://www.c-howto.de/tutorial/arrays-felder/zweidimensionale-felder/)



### Anwendung eines zweidimesionalen Arrays

Addition zweier Matrizen

```cpp
#include <stdio.h>

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
			printf("%d\t",C[i][j]);
		printf("\n");
	}
    return 0;
}
```
@Rextester.C

[Multiplikation zweier Matrizen](https://www.codewithc.com/c-program-for-gauss-elimination-method/)


### Strings/Zeichenketten

Folgen von Zeichen, die sogenannten *Strings* werden in C durch Arrays mit
Elementen vom Datentyp `char` repräsentiert. Die Zeichenfolgen werden mit
`\0` abgeschlossen.

```cpp                                         stringarray.c
#include <stdio.h>

int main(void) {
  printf("Diese Form eines Strings haben wir bereits mehrfach benutzt!\n");
  // Alternativ
  char a[50];
  a[49] = '\0';
  printf("->%s<-\n", a);
  const char b[] = { 'H', 'a', 'l', 'l', 'o', ' ',
                     'F', 'r', 'e', 'i', 'b', 'e', 'r', 'g', '\0' };
  printf("->%s<-\n", b);
  const char c[] = "Noch eine \0Moeglichkeit";
  printf("->%s<-\n", c);
  char d[] = { 80, 114, 111, 122, 80, 114, 111, 103, 32, 50, 48, 49, 57, 0  };
  printf("->%s<-\n", d);
  return 0;
}
```
@Rextester.C

{{1}}
Beispiel einer fehlerhaften Verwendung eines `const char` Arrays

{{1}}
```cpp                     arrayInitVsAssignment.c
#include <stdio.h>
#include <string.h>       // notwendig für strcpy

int main(void) {
  const char a[] = "Das ist der Originaltext";
  strcpy(a, "Das ist ein neuer Text");
  printf("%s\n",a);
  return 0;
}
```
@Rextester.C



### Anwendung von Zeichenketten

Schreiben Sie ein Programm, dass in einem Text groß geschriebene Buchstaben
durch klein geschriebene ersetzt und umgekehrt.

Da Variablen des Datentyps `char` genau ein Byte benötigen, liefert `sizeof`-Operator im folgenden Beispiel die Anzahl der Elemente des Arrays.

```cpp                     ArrayExample.c
#include <stdio.h>

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
  printf("%s\n", a);
  printf("%s\n", b);
  return 0;
}
```
@Rextester.C

{{1}}
Des Weiteren verwendet das Programm die ASCII-Codierung der Zeichen.

{{1}}
![ASCII](img/ASCII_Zeichensatz.jpeg)<!--
style="width: 100%;
       max-width: 600px;
       display: block;
       margin-left: auto;
       margin-right: auto;" -->

### Fehlerquellen

Bitte unterscheiden Sie die Initialisierungsphase von normalen Zuweisungen,
bei denen Sie nur auf einzelne Elemente zugreifen können.

```cpp                     arrayInitVsAssignment.c
#include <stdio.h>
#include <string.h>       // notwendig für strcpy

int main(void) {
  char a[] = "Das ist der Originaltext";
  a = "Das ist ein neuer Text";  // Compiler Error
  //strcpy(a, "Das ist ein neuer Text");
  a[0]='X';
  printf("%s\n",a);
  return 0;
}
```
@Rextester.C


Auf die umfangreiche Funktionssammlung der `string.h` zur Manipulation von
Strings wird in einer folgenden Vorlesung eingegangen.

## 3. `struct`

Mit `struct` werden zusammengehörige Variablen unterschiedlicher Datentypen und
Bedeutung in einem Konstrukt zusammengefasst. Damit wird für den Entwickler der
Zusammenhang deutlich. Die Variablen der Struktur werden als Komponenten (engl.
members) bezeichnet.

Beispiele:

```cpp
struct datum
{
  int tag;
  char monat[10];
  int jahr;
};


struct Student
{
  int Matrikel;
  char name[20];
  char vorname[25];
};  // <- Hier steht ein Semikolon!
```

### Deklaration, Definition, Initialisierung und Zugriff

Und wie erzeuge ich Variablen dieses erweiterten Types, wie werden diese
initialisiert und wie kann ich auf die einzelnen Komponenten zugreifen?

Der Bespiel zeigt, dass die Definition der Variable unmittelbar nach der
`struct`-Definition oder mit einer gesonderten Anweisung mit einer vollständigen,
partiellen Initialisierung bzw. ohne Initialisierung erfolgen kann.

Die nachträgliche Veränderung einzelner Komponenten ist über Zugriff mit Hilfe
des Punkt-Operators möglich.

```cpp                           structExample.c
#include <stdio.h>
#include <string.h>

int main() {
  struct datum
  {
      int tag;
      char monat[10];
      int jahr;
  } geburtstag_1 = {18, "April", 1986};              // <- Initialisierung
                                                     //    Variable geburtstag_1
  struct datum geburtstag_2 = {13, "Januar", 2013};  // <- Initialisierung
                                                     //    Variable geburtstag_2
  geburtstag_2.tag = 13;                             // Zuweisungen
  geburtstag_2.jahr =1803;
  strcpy(geburtstag_2.monat, "April");

  // Unvollstaendige Initialisierung
  struct datum geburtstag_3 ={.monat = "September"}; // <- partielle Initialisierung

  printf("Person A wurde am %2d. %-10s %4d geboren.\n", geburtstag_1.tag, geburtstag_1.monat, geburtstag_1.jahr);
  printf("Person B wurde am %2d. %-10s %4d geboren.\n", geburtstag_2.tag, geburtstag_2.monat, geburtstag_2.jahr);
  printf("Person C wurde am %2d. %-10s %4d geboren.\n", geburtstag_3.tag, geburtstag_3.monat, geburtstag_3.jahr);
  return 0;
}
```
@Rextester.C

### Vergleich von `struct`-Variablen

Der C-Standard kennt keine Methodik um `struct`s in einem Rutsch auf Gleichheit
zu prüfen. Entsprechend ist es an jedem Entwickler eine eigene Funktion dafür zu
schreiben. Diese kann unterschiedliche Aspekte des `struct`s adressieren.

Im nachfolgenden Beispiel werden zur Überprüfung der Gleichheit die `tag`und
`monat` vergliehen. Der Vergleich wird dadurch vereinfacht, dass
wir für die Repräsentation des Monats ein `enum` verwenden. Damit entfällt
aufwändigerer Vergleich der Strings.

```cpp                           structExample.c
#include <stdio.h>

enum MONAT {Januar, Februar, Maerz, April, Mai};

struct datum
{
    int tag;
    enum MONAT monat;
    int jahr;
};

int main() {
  struct datum person_1 = {10, Januar, 2013};
  struct datum person_2 = {10, Maerz, 1956};
  person_2.monat = Januar;

  if ((person_1.tag == person_2.tag) && (person_1.monat == person_2.monat))
      printf("Oha, der gleiche Geburtstag im Jahr!\n");
  else
      printf("Ungleiche Geburtstage!\n");
}
```
@Rextester.C

### Arrays von Strukturen

Natürlich lassen sich die beiden erweiterten Datenformate auf der Basis von
`struct` und Arrays miteinander kombinieren.

-> Live (arrayOfStructs.c)

### Typdefinition mit `typedef`

Mit Hilfe des Schlüsselworts `typedef` kann für einen Datentyp, einschließlich
eines `struct`-Datentyps, ein neuer Bezeichner definiert werden:

```c
typedef Typendefinition Bezeichner;
```
Zum Beispiel kann der Datentyp `Datum` definiert und zur einfacheren
Variablendeklaration verwendet werden:

```cpp
struct datum
{
  int tag;
  char monat[10];
  int jahr;
};

typedef struct datum Datum;

Datum geburtsdatum;
```

Alternative Möglichkeit der Definition des Datentyp zeigt folgender Beispiel:

```cpp
typedef struct datum
{
  int tag;
  char monat[10];
  int jahr;
} Datum;

Datum geburtsdatum;
```

## Beispiel des Tages

Berechnen Sie einen gleitenden Mittelwert und das Maximum aus folgender
Zahlenreihe. Geben Sie das Resultat in einem Graphen wieder.

```cpp                     magicSquare.c
#include <stdio.h>
#define VALUECOUNT  20
#define MAXVALUE 10

int main(){
  int values[]={0,4,3,2,3,4,5,5,2,4,5,6,7,4,2,4,5,5,5,5};
  // Initialization of the matrix
  int matrix[MAXVALUE+1][VALUECOUNT];
  for (int i=0; i <=MAXVALUE; i++){
       for (int j=0; j<VALUECOUNT; j++){
          matrix[i][j]=0xff;
       }
  }
  // Realisierung der Werte des Vektors
  for (int i=0; i<VALUECOUNT; i++){
    matrix[values[i]][i] = values[i];
  }
  // Ausgabe
  printf("Values\n     ^\n");
  for (int i=MAXVALUE; i>=0; i--){
       printf("%3d  |", i);
       for (int j=0; j<VALUECOUNT; j++){
          if (matrix[i][j]!=0xff) printf("*");
          else printf(" ");
       }
       printf("\n");
  }
  printf("     ---------------------------->\n              index \n");
  return 0;
}
```
@Rextester.C
