<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Copilot & Anna
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.7
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md#10
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

link:     style.css


-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/03_ArrayZeigerReferenzen.md)

# Grundlagen der Sprache C++

| Parameter                 | Kursinformationen                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | @config.lecture                                                                                                                                                                  |
| **Semester**              | @config.semester                                                                                                                                                                 |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                |
| **Inhalte:**              | `Array, Zeiger und Referenzen`                                                                                                                                                   |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/03_ArrayZeigerReferenzen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/03_ArrayZeigerReferenzen.md) |
| **Autoren**               | @author                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Was ist ein Array?
* Wie können zwei Arrays verglichen werden?
* Erklären Sie die Idee des Zeigers in der Programmiersprache C/C++.
* Welche Gefahr besteht bei der Initialisierung von Zeigern?
* Was ist ein `NULL`-Zeiger und wozu wird er verwendet?

---------------------------------------------------------------------

## Reflexion Ihrer Fragen / Rückmeldungen

> Zur Erinnerung ... Wettstreit zur partizipativen Materialentwicklung mit den Informatikern ...

<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Weihnachtsmänner](./images/00_Einfuehrung/Weihnachtsmaenner.jpeg "Preis für das aktivste Auditorium")

<div class="flex-child" style="min-width: 250px;">

<!-- data-type="none" -->
| Format                   | Informatik Studierende  | Nicht-Informatik Studierende |
|--------------------------|-------------------------|------------------------------|
| Verbesserungsvorschlag   | 2                       | 2                            |
| Fragen                   | 2                       | 3                            |
| generelle Hinweise       | 0                       | 1                            |

</div>

</section>

## Wie weit waren wir gekommen?

> Aufgabe: Die LED blinkt im Beispiel 10 mal. Integrieren Sie eine Abbruchbedingung für diese Schleife, wenn der grüne Button gedrückt wird. Welches Problem sehen Sie?

<div>
  <wokwi-pushbutton color="green" pin="2"  port="D" label="2"></wokwi-pushbutton>
  <wokwi-led color="red"   pin="13" port="B" label="13"></wokwi-led>
</div>
```cpp       ButtonLogic.cpp
void setup() {
  pinMode(2, INPUT);      // Button grün
  pinMode(13, OUTPUT);

  while (digitalRead(2) == LOW) {     // Kopfgesteuerte Schleife für das 
     delay(10);                       // warten auf den Buttondruck
  }

  for (int i = 0; i<10; i++) {        // 10 mal LED blinken - Wiederholungs
    digitalWrite(13, HIGH);           // -schleife
    delay(500);
    digitalWrite(13, LOW);
    delay(500);
  }
}

void loop() {
}
```
@AVR8js.sketch

## Arrays

Bisher umfassten unsere Variablen einzelne Skalare. Arrays erweitern das
Spektrum um Folgen von Werten, die in n-Dimensionen aufgestellt werden können.
Ein Array ist eine geordnete Folge von Werten des gleichen Datentyps.
Die Deklaration erfolgt in folgender Anweisung:

```text
Datentyp Variablenname[Anzahl_der_Elemente];
```

```cpp
int a[6];
```


<!-- data-type="none" style="table-layout: fixed; max-width:600px;"-->
| `a[0]` | `a[1]` | `a[2]` | `a[3]` | `a[4]` | `a[5]` |


```text
Datentyp Variablenname[Anzahl_der_Elemente_Dim0][Anzahl_der_Elemente_Dim1];
```

```cpp
int a[3][5];
```
<!-- data-type="none" style="table-layout: fixed; max-width:800px;"-->
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

int main(void) {
  int a[3];       // Array aus 3 int Werten
  a[0] = -2;
  a[1] = 5;
  a[2] = 99;
  for (int i=0; i<3; i++){
    std::cout << a[i] << " ";
  }
  std::cout << "\nNur zur Info " << sizeof(a) << "\n";
  std::cout << "Zahl der Elemente " << sizeof(a) / sizeof(int) << "\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> Schauen wir uns das Ganze noch in einer Animation an: [PythonTutor](https://pythontutor.com/iframe-embed.html#code=%23include%20%3Ciostream%3E%0Ausing%20namespace%20std%3B%0A%0Aint%20main%28%29%20%7B%0A%20%20int%20a%5B3%5D%3B%20%20%20%20%20%20%20//%20Array%20aus%203%20int%20Werten%0A%20%20a%5B0%5D%20%3D%20-2%3B%0A%20%20a%5B1%5D%20%3D%205%3B%0A%20%20a%5B2%5D%20%3D%2099%3B%0A%20%20for%20%28int%20i%3D0%3B%20i%3C3%3B%20i%2B%2B%29%7B%0A%20%20%20%20printf%28%22%25d%20%22,%20a%5Bi%5D%29%3B%0A%20%20%7D%0A%20%20cout%3C%3C%22%5CnGr%C3%B6%C3%9Fe%20des%20Arrays%20%22%3C%3Csizeof%28a%29%3C%3Cendl%3B%0A%20%20cout%3C%3C%22Zahl%20der%20Elemente%20%22%20%3C%3C%20sizeof%28a%29%20/%20sizeof%28int%29%20%3C%3Cendl%3B%0A%20%20cout%3C%3C%22Adresse%20des%20Arrays%20%22%20%3C%3C%20a%3B%0A%20%20return%200%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=14&heapPrimitives=nevernest&origin=opt-frontend.js&py=cpp_g%2B%2B9.3.0&rawInputLstJSON=%5B%5D&textReferences=false)


{{1}}
Wie können Arrays noch initialisiert werden:

{{1}}
+ vollständig (alle Elemente werden mit einem spezifischen Wert belegt)
+ anteilig (einzelne Elemente werden mit spezifischen Werten gefüllt, der rest mit 0)

{{1}}
```cpp                     ArrayExample.cpp
#include <iostream>
#include <iomanip>

int main(void) {
  int a[] = {5, 2, 2, 5, 6};
  float b[5] = {1.01};
  for (int i=0; i<5; i++) {
    std::cout << i << "  "  << a[i] << " / " << std::fixed << b[i] << "\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Und wie bestimme ich den erforderlichen Speicherbedarf bzw. die Größe des
Arrays?

{{2}}
```cpp                     ArrayExample.cpp
#include <iostream>

int main(void) {
  int a[3];
  std::cout << "Speicherplatz [Byte] " << sizeof(a) << "\n";
  std::cout << "Zahl der Elemente " << sizeof(a)/sizeof(int) << "\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Fehlerquelle Nummer 1 - out of range

```cpp                     ArrayExample.cpp
#include <iostream>

int main(void) {
  int a[] = {-2, 5, 99};
  for (int i=0; i<=3; i++)
    std::cout << a[i] << " ";
  std::cout << "\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


### Anwendung eines eindimesionalen Arrays

Schreiben Sie ein Programm, das zwei Vektoren miteinander vergleicht. Warum ist
die intuitive Lösung `a == b` nicht korrekt, wenn `a` und `b` arrays sind?

```cpp                     ArrayExample.cpp
#include <iostream>

int main(void) {
  int a[] = {0, 1, 2, 4, 3, 5, 6, 7, 8, 9};
  int b[10];
  for (int i=0; i<10; i++)  // "Befüllen" des Arrays b
    b[i] = i;

  // Wir haben jetzt zwei Arrays a und b vorzuliegen und wolle diese 
  // parweise vergleichen
  for (int i=0; i<10; i++)
    if (a[i] != b[i])
      std::cout << "An Stelle " << i << " unterscheiden sich die Arrays!\n";
  return 0;
  }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Welche Verbesserungsmöglichkeiten sehen Sie bei dem Programm?

### Mehrdimensionale Arrays

                     {{0-1}}
********************************************

Deklaration:

```cpp
int Matrix[4][5];    /* Zweidimensional - 4 Zeilen x 5 Spalten */
```

Deklaration mit einer sofortigen Initialisierung aller bzw. einiger Elemente:

```cpp
int Matrix[4][5] = {{1,  2,  3,  4,  5},
                    {6,  7,  8,  9,  10},
                    {11, 12, 13, 14, 15},
                    {16, 17, 18, 19, 20}};

int Matrix[4][4] = {{1,},
                    {1, 1},
                    {1, 1, 1},
                    {1, 1, 1, 1}};

int Matrix[4][4] = {1,2,3,4,5,6,7,8};
```
******************************************

{{1}}
Initialisierung eines n-dimensionalen Arrays:

{{1}}
![Matrix](./images/04_ZeigerUndArrays/2DArray.jpg "Darstellung der Matrixinhalte für das nachfolgende Codebeispiel - Aufgabe aus [C-Kurs](http://www.c-howto.de/tutorial/arrays-felder/zweidimensionale-felder/")<!--
style=" width: 60%;
        max-width: 800px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

{{1}}
> **Praxisbezug:**
> Solche zweidimensionalen Arrays werden oft genutzt, um Karten oder Spielfelder zu modellieren – zum Beispiel für ein Labyrinth, ein Brettspiel oder eine Landkarte. Die Zahlen im Array stehen dann für verschiedene Objekte oder Besonderheiten:
> - 0 = freies Feld
> - 1 = Startpunkt
> - 2 = Hindernis
> - 3 = Schatz
> - 4 = Ziel
> So kann man das Feld auswerten, anzeigen oder für eine Spiellogik weiterverarbeiten.


{{2}}
```cpp                          nDimArray.cpp
#include <iostream>

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
  for (i=0; i<8; i++) {
    // Schleife fuer Spalten, X-Achse
    for (j=0; j<8; j++) {
      std::cout << brett[i][j] << " ";
    }
    std::cout << "\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)



### Anwendung eines zweidimesionalen Arrays

Elementwese Addition zweier Matrizen

```cpp       Addition.cpp
#include <iostream>

int main(void)
{
  int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int B[2][3] = {{10, 20, 30}, {40, 50, 60}};
  int C[2][3];
  int i, j;
  for (i=0; i<2; i++)
    for (j=0; j<3; j++)
      C[i][j] = A[i][j] + B[i][j];
  for (i=0; i<2; i++)
  {
    for (j=0; j<3; j++)
      std::cout << C[i][j] << "\t";
    std::cout << "\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> Weiteres Beispiel: Lösung eines Gleichungssystem mit dem Gausschen Elimnationsverfahren [Link](https://www.codewithc.com/c-program-for-gauss-elimination-method/)

> **Merke:** Größere Daten in Arrays abzulegen ist in der Regel effizienter als einzelne Variablen zu verwenden. Die Verwendung von Arrays ist aber nicht immer die beste Lösung. Prüfen Sie höherabstraktere Formate wie Listen oder Vektoren!

## Sonderfall Zeichenketten / Strings

Folgen von Zeichen werden in C/C++ durch Arrays mit
Elementen vom Datentyp `char` repräsentiert. Die Zeichenfolgen werden mit
`\0` abgeschlossen.

```cpp                                         stringarray.cpp
#include <iostream>

int main(void) {
  std::cout << "Diese Form eines Strings haben wir bereits mehrfach benutzt!\n";
  //////////////////////////////////////////////////////////////////////////////

  char a[] = "Ich bin ein char Array!";  // Der Compiler fügt das \0 automatisch ein!
  if (a[23] == '\0') {
    std::cout << "char Array Abschluss in a gefunden!\n";
  }

  std::cout << "->" << a << "<-\n";
  char b[] = { 'H', 'a', 'l', 'l', 'o', ' ',
               'F', 'r', 'e', 'i', 'b', 'e', 'r', 'g', '\0' };
  std::cout << "->" << b << "<-\n";
  char c[] = "Noch eine \0Moeglichkeit";
  std::cout << "->" << c << "<-\n";
  char d[] = { 69, 65, 86, 68, 32, 50, 48, 50, 52, 0 };
  std::cout << "->" << d << "<-\n";

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

C++ implementiert einen separaten string-Datentyp (Klasse), die ein deutliche komfortableren Umgang mit Texten erlaubt. Beim Anlegen eines solchen muss nicht angegeben werden, wie viele Zeichen reserviert werden sollen. Zudem könenn Strings einfach zuweisen und vergleichen werden, wie es für andere Datentypen üblich ist. Die C const char * Mechanismen funktionieren aber auch hier.

```cpp                                         stringarray.cpp
#include <iostream>
#include <string>      // Header für string Klasse

int main(void) {
  std::string hanna = "Hanna";
  std::string anna = "Anna";
  std::string alleBeide = anna + " + " + hanna;
  std::cout << "Hallo: " << alleBeide << "\n";

  int res = anna.compare(hanna);
  if (res == 0)
    std::cout << "Both input strings are equal.\n";
  else if (res < 0)
    std::cout << "String 1 is smaller as compared to String 2\n.";
  else
    std::cout << "String 1 is greater as compared to String 2\n.";

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

> An dieser Stelle sei bereits erwähnt, dass die Übergabe der "call-by-reference"-Parameter via Reference ist ebenfalls möglich und einfacher in der Handhabung.

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

> **Merke:** Zeiger sollten vor der Verwendung initialisiert werden.

Der Zeiger kann initialisiert werden durch die Zuweisung:

* der Adresse einer Variable, wobei die Adresse mit Hilfe des Adressoperators `&` ermittelt wird,
* eines Arrays,
* eines weiteren Zeigers oder
* des Wertes von `NULL`.

<!--- TODO: Sollten wir im C++ Kontext nicht mind. auf `nullptr` verweisen? --->

```cpp                      PointerExamples.cpp
#include <iostream>

int main(void) {
  int a = 0;
  int * ptr_a = &a;       /* mit Adressoperator */

  int feld[10];
  int * ptr_feld = feld;  /* mit Array */

  int * ptr_b = ptr_a;    /* mit weiterem Zeiger */

  int * ptr_Null = NULL;  /* mit NULL */

  std::cout << "Pointer ptr_a    " << ptr_a << "\n";
  std::cout << "Pointer ptr_feld " << ptr_feld << "\n";
  std::cout << "Pointer ptr_b    " << ptr_b << "\n";
  std::cout << "Pointer ptr_Null " << ptr_Null << "\n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


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

int main(void) {
  int a = 15;
  int * ptr_a = &a;
  std::cout << "Wert von a                     " << a << "\n";
  std::cout << "Pointer ptr_a                  " << ptr_a << "\n";
  std::cout << "Wert hinter dem Pointer ptr_a  " << *ptr_a << "\n";
  *ptr_a = 10;
  std::cout << "Wert von a                     " << a << "\n";
  std::cout << "Wert hinter dem Pointer ptr_a  " << *ptr_a << "\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
> Schauen wir wiederum auf eine grafische Darstellung [PythonTutor](http://pythontutor.com/iframe-embed.html#code=%23include%20%3Cstdio.h%3E%0A%23include%20%3Cstdlib.h%3E%0A%0Aint%20main%28void%29%0A%7B%0A%20%20int%20a%20%3D%2015%3B%0A%20%20int%20*%20ptr_a%20%3D%20%26a%3B%0A%20%20printf%28%22Wert%20von%20a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25d%5Cn%22,%20a%29%3B%0A%20%20printf%28%22Pointer%20ptr_a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25p%5Cn%22,%20ptr_a%29%3B%0A%20%20printf%28%22Wert%20hinter%20dem%20Pointer%20ptr_a%20%20%25d%5Cn%22,%20*ptr_a%29%3B%0A%20%20*ptr_a%20%3D%2010%3B%0A%20%20printf%28%22Wert%20von%20a%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%25d%5Cn%22,%20a%29%3B%0A%20%20printf%28%22Wert%20hinter%20dem%20Pointer%20ptr_a%20%20%25d%5Cn%22,%20*ptr_a%29%3B%0A%20%20return%20EXIT_SUCCESS%3B%0A%7D&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=c&rawInputLstJSON=%5B%5D&textReferences)

### Fehlerquellen

Fehlender Adressoperator bei der Zuweisung

```cpp               PointerFailuresI.cpp
#include <iostream>

int main(void) {
  int a = 5;
  int * ptr_a;
  ptr_a = a;
  std::cout << "Pointer ptr_a                  " << ptr_a << "\n";
  std::cout << "Wert hinter dem Pointer ptr_a  " << *ptr_a << "\n";
  std::cout << "Aus Maus!\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
Fehlender Dereferenzierungsoperator beim Zugriff

{{1}}
```cpp          PointerFailuresII.cpp
#include <iostream>

int main(void)
{
  int a = 5;
  int * ptr_a = &a;
  std::cout << "Pointer ptr_a                  " << ptr_a << "\n";
  std::cout << "Wert hinter dem Pointer ptr_a  " << ptr_a << "\n";
  std::cout << "Aus Maus!\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out 2&>1`)

{{2}}
Uninitialierte Pointer zeigen "irgendwo ins nirgendwo"!

{{2}}
```cpp                  PointerFailuresIII.cpp
#include <iostream>

int main(void) {
  int * ptr_a;
  // korrekte Initalisierung
  // int * ptr_a = NULL;

  // ... hier passiert irgendwas 

  *ptr_a = 10;
  // Prüfung auf gültige Adresse
  // if (ptr_a != NULL) *ptr_a = 10;
  std::cout << "Pointer ptr_a                  " << ptr_a << "\n";
  std::cout << "Wert hinter dem Pointer ptr_a  " << *ptr_a << "\n";
  std::cout << "Aus Maus!\n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


## Referenz

Eine Referenz ist wie ein zweiter Name für eine Variable. Sie zeigt immer auf ein existierendes Objekt und kann nicht „ins Leere“ zeigen. 

> Referenzen existieren nur in C++. In C gibt es nur Zeiger.

Im Gegensatz zu Zeigern (Pointer) ist die Handhabung für Einsteiger viel einfacher:

|                | Zeiger (Pointer)         | Referenz                |
|----------------|-------------------------|-------------------------|
| Kann NULL sein | Ja                      | Nein                    |
| Muss initialisiert werden | Nein         | Ja                      |
| Dereferenzierung nötig?   | Ja (`*p`)    | Nein                    |
| Nachträglich umsetzbar?   | Ja (kann auf andere Variable zeigen) | Nein (bleibt immer auf das gleiche Objekt) |
| Speicherfreigabe nötig?   | Ja (bei `new`) | Nein                  |

**Beispiel:**

```cpp // referenzen.cpp
#include <iostream>

int main(void) {
  int  a = 1;      // Variable
  int &r = a;      // Referenz auf a
  int *p = &a;     // Zeiger auf a

  std::cout << "a: " << a << " r: " << r << " *p: " << *p << std::endl;
  r = 5;           // Ändert auch a
  std::cout << "a: " << a << " r: " << r << std::endl;
  *p = 10;         // Ändert auch a
  std::cout << "a: " << a << " r: " << r << std::endl;
}
```
@LIA.eval(["main.cpp"], `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Merke:**
> - Referenzen sind ideal für Funktionsparameter, wenn man Werte verändern möchte, ohne Kopien zu erzeugen.
> - Zeiger braucht man, wenn man „ins Leere“ zeigen oder dynamisch Speicher verwalten will.

**Typische Anwendungen für Referenzen:**
- Übergabe an Funktionen („call by reference“)
- Vermeidung von Kopien großer Objekte
- Spezielle Memberfunktionen (z. B. Copy-Konstruktor)

> **Achtung:** Referenzen sind nicht geeignet, um dynamisch Speicher zu verwalten oder auf „nichts“ zu zeigen.


## Beispiel der Woche

Gegeben ist ein Array, das eine sortierte Reihung von Ganzzahlen umfasst.
Geben Sie alle Paare von Einträgen zurück, die in der Summe 18 ergeben.

Die intuitive Lösung entwirft einen kreuzweisen Vergleich aller sinnvollen Kombinationen
der $n$ Einträge im Array. Dafür müssen wir $(n-1)^2 /2$ Kombinationen bilden.

<!-- data-type="none" style="table-layout: fixed; max-width:1050px;"-->
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
#define ZIELWERT 18

int main(void) {
  int a[] = {1, 2, 5, 7, 9, 10, 12, 13, 16, 17, 18, 21, 25};
  int i_left = 0;
  int i_right = 12;

  std::cout << "Value left " << a[i_left] << " right " << a[i_right] << "\n-----------------------\n";
  do {
    std::cout << "Value left " << a[i_left] << " right " << a[i_right];
    if (a[i_right] + a[i_left] == ZIELWERT)
      std::cout << " -> TREFFER";
    std::cout << "\n";

    if (a[i_right] + a[i_left] >= ZIELWERT)
      i_right--;
    else
      i_left++;
  } while (i_right != i_left);

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


# Quiz

## Arrays

> Erstellen Sie ein eindimensionales Array namens `arr`, das 7 Elemente vom Typ `int` enthält.
[[int arr[7];]]

> Erstellen Sie ein zweidimensionales Array namens `arr`, das 3*4 Elemente vom Typ `int` enthält.
[[int arr[3][4];]]

Zugriff
====================

> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

int main(void) {
  float b[5] = {1.0, 4.8, 1.2, 42.0, 99.0};
  std::cout << b[2] << "\n";
  return 0;
}
```
[[1.2]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

int main() {
  int a[5] = {5, 8};
  std::cout << a[2] << "\n";
  return 0;
}
```
[[0]]
************************************************************************

Mehrdimensionale Arrays
====================

> Es existiert ein Array `int A[2][5];`. Setzen Sie `[_____]` gleich 1.
|            | Spalten   |           |           |           |           |
| ---------- | --------- | --------- | --------- | --------- | --------- |
| **Zeilen** | `a[0][0]` | `a[0][1]` | ...       |           |           |
|            |           |           | `[_____]`   |           |           |
[[A[1][2] = 1;]]
<script>
let input = "@input".trim()

input == "A[1][2] = 1;" || input == "A[1][2]= 1;" || input == "A[1][2] =1;" || input == "A[1][2]=1;"
</script>

{{1}}
************************************************************************
> Durch was muss `[_____]` ersetzt werden damit die Zahl `19` aus `m[4][5]` ausgegeben wird?
```cpp
#include <iostream>

int main() {
  int m[4][5] = {{1, 2, 3, 4, 5},
                {6, 7, 8, 9, 10},
                {11,12,13,14,15},
                {16,17,18,19,20}};
  std::cout << [_____] << "\n";
  return 0;
}
```
[[m[3][3]]]
************************************************************************

{{2}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

int main() {
  int A[2][3] = {{1, 2, 3}, {4, 5, 6}};
  int B[2][3] = {{10, 20, 30}, {40, 50, 60}};

  std::cout << A[1][0] + B[0][1] << "\n";
  return 0;
}
```
[[24]]
************************************************************************

## Zeichenketten

> Durch welche Sequenz werden Zeichenketten abgeschlossen?
[[\0]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

int main() {
  char c[] = "Peter wohnt irgendwo\0 in Freiberg.";
  std::cout << c << "\n";
}
```
[[Peter wohnt irgendwo]]
************************************************************************

## Zeiger

> Worauf zeigen Zeiger?
[( )] `chars`
[( )] Referenzen
[(X)] Speicheraddressen

Definition
====================

> Welche der folgenden Definitionen sind möglich?
[[X]] int* z1;
[[X]] float * z2;
[[X]] char *z3;
[[X]] int \*z4, \*z5;
[[ ]] int z6*;
[[X]] int *z7, i;

Initialisierung
====================

> Durch welches Zeichen werden Addressen ermittelt?
[[&]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

int main() {
  int a = 15;
  int *ptr_a = &a;
  std::cout << *ptr_a << "\n";

  return 0;
}
```
[( )] Die Addresse von `a`
[(X)] 15
[( )] `NULL`
************************************************************************

Dynamische Datenobjekte
====================

> Wie häufig kann `delete` auf ein Objekt angewendet werden?
[( )] 0
[(X)] 1
[( )] 42
[( )] Beliebig oft

{{1}}
************************************************************************
> Wie lautet die Aussage dieses Programms?
```cpp
#include <iostream>

int main() {
  int a = 10;
  int *ptr_a = &a;
  std::cout << ptr_a  << "\n";
  delete ptr_a;
  return 0;
}
```
[( )] 10
[( )] Die Addresse von `a`
[( )] Die Addresse des Zeigers `*ptr_a`
[(X)] Es gibt einen Error
************************************************************************

## Referenz

> Welche der im Beispiel benutzten Variablen ist eine Referenz?
```cpp
#include <iostream>

int main() {
  int a = 10;
  int &b = a;
  int *c = b;
  std::cout << c << "\n";
  return 0;
}
```
[( )] a
[(X)] b
[( )] c

{{1}}
************************************************************************
> Hier ist ein Programm mit Ausgabe vorgegeben. Was müsste statt `[_____]` ausgegeben werden?
```cpp
#include <iostream>

int main(void) {
  int  a = 1;
  int &r = a;

  std::cout << "a: " << &a << " r: " << &r << endl;
}
```
```
a: [_____] r: 0x7ffdddd212fc
```
[[0x7ffdddd212fc]]
************************************************************************

{{2}}
************************************************************************
> Hier ist ein Programm mit Ausgabe vorgegeben. Was müsste statt `[_____]` ausgegeben werden?
```cpp
#include <iostream>

int main(void) {
  int  a = 1;
  int &r = a;

  std::cout << "a: " << a << " r: " << r << "\n";
}
```
```
a: 1 r: [_____]
```
[[1]]
************************************************************************
