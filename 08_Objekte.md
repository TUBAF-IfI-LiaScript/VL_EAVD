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
        https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md

-->

# Grundzüge objektorientierter Programmierung

Die interaktive Version des Kurses ist unter diesem [Link](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/08_Objekte.md#1) zu finden.

**Wie weit waren wir gekommen?**

Das folgende Beispiel wiederholt die Verwendung von `typedef` und `stuct` innerhalb eines Arrays für eine Ampelsteuerung.

<!--
style="width: 80%; max-width: 460px; display: block; margin-left: auto; margin-right: auto;"
-->
```ascii
                  .-- 5s --. .-- 2s --. .-- 5s --.
                  |        | |        | |        |
                  |        v |        v |        v
                 .-.       .-.        .-.       .-.
 Ampelzustände  ( 0 )     ( 1 )      ( 2 )     ( 3 )
                 '-'       '-'        '-'       '-'
                  ^                              |
                  |                              |
                  .------------- 2s -------------.

                 RED  RED/YELLOW     GREEN     YELLOW
````

<div>
  <wokwi-led color="red"    pin="13" port="B" label="13"></wokwi-led>
  <wokwi-led color="yellow" pin="12" port="B" label="13"></wokwi-led>
  <wokwi-led color="green"  pin="11" port="B" label="13"></wokwi-led>
</div>

```cpp       TrafficLights.cpp
typedef struct {
    int state;
    int next;
    int A_red;
    int A_yellow;
    int A_green;
    int timer;
} ampel_state_t;

ampel_state_t state_table[4] = {

// state     A_red             timer
//  |   next  |  A_yellow       |
//  |    |    |   |    A_green  |
//----------------------------------------------
{   0,   1,   1,  0,    0,      5},
{   1,   2,   1,  1,    0,      1 },
{   2,   3,   0,  0,    1,      5},
{   3,   0,   0,  1,    0,      1,}
};

const int greenPin = 13;
const int yellowPin = 12;
const int redPin = 11;
int state = 0;

void setup() {
  pinMode(greenPin, OUTPUT);
  pinMode(yellowPin, OUTPUT);
  pinMode(redPin, OUTPUT);
}

void loop() {
  if (state_table[state].A_red == 1) digitalWrite(redPin, HIGH);
  else digitalWrite(redPin, LOW);
  if (state_table[state].A_yellow == 1) digitalWrite(yellowPin, HIGH);
  else digitalWrite(yellowPin, LOW);
  if (state_table[state].A_green == 1) digitalWrite(greenPin, HIGH);
  else digitalWrite(greenPin, LOW);
  delay(state_table[state].timer*1000);
  state =  state_table[state].next;
}
```
@AVR8js.sketch

**Inhalt der heutigen Veranstaltung**

* Motivation der Objektorientierten Programmierung

**Fragen an die heutige Veranstaltung ...**

* Was sind Objekte?

## Motivation

```cpp                 ZusammengesetzteDatenstrukturen.c
#include <stdio.h>

#define ARRAYSIZE 5

struct Datum
{
    int tag;
    int monat;
    int jahr;
};

//int berechneZeitDiff(struct Datum TagA, struct Datum TagB){
//
//}

//int bestimmeWochentag(struct Datum Tag){
//
//}

typedef struct Datum geburtstag;

struct Person
{
    char name[25];
    geburtstag meinGeburtstag;
    int telefonnummer;
};

typedef struct Person freund;

void printFreund(freund freundA){
  printf("%s - %d.%d.%d\n",freundA.name,
                           freundA.meinGeburtstag.tag,
                           freundA.meinGeburtstag.monat,
                           freundA.meinGeburtstag.jahr);
}

//int zumGeburtstagAnrufen(freund Freund){
//
//}

typedef freund FreundeskreisListe[ARRAYSIZE];

void printFreundeskreis(FreundeskreisListe liste, int size){
  printf("Meinen Freunde: \n");
  for (int i = 0; i < size; i++){
    printFreund(liste[i]);
  }
}

int main() {
  freund A = {"Peter", 1,1,2010, 1234};
  freund B = {.name = "Paul",
              .meinGeburtstag = {10, 1, 2013},
              .telefonnummer = 56756 };
  printFreund(A);

  FreundeskreisListe meineFreunde = {0};
  meineFreunde[0] = A;
  meineFreunde[1] = B;
  printFreundeskreis(meineFreunde, 2);
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

> **Aufgabe: ** Erweitern Sie die Implementierung so, dass anhand der Tage und Monatswerte der Geburtstage abgeprüft werden kann, ob eine gemeinsame Feier in Frage kommt.

Das prozedurale Programmierparadigma zielt darauf imperative Programme in überschaubare Teile aufzugliedern. Diese Teile werden als Prozeduren (Unterprogramme, Routinen oder Funktionen) bezeichnet. Insgesamt soll damit sichergestellt werden, das der Programmcode übersichtlicher wird und unnötige Code-Wiederholungen vermieden werden. Durch die Abstraktion der Algorithmen stellt das prozedurale Software-Paradigma einen entscheidenden Schritt von einfachen Assemblersprachen hin zu komplexeren Hochsprachen dar.

Versuchen wir die Idee mal auf unser Beispiel anzuwenden. Welche Daten und Methoden könnte man zusammenfassen, um sie ggf. wieder zu verwenden?

| Daten                | Methoden                                                      |
| -------------------- | ------------------------------------------------------------- |
| `struct Datum`       | `int berechneZeitDiff(struct Datum TagA, struct Datum TagB)`  |
|                      | `int bestimmeWochentag(struct Datum Tag)`                     |
|                      | ...                                                           |
| `struct Person`      | `int zusammenFeiern(freund FreundA, freund FreundA)`          |
|                      | `int anrufen(freund Freund)`                                  |
|                      | ...                                                           |
| `FreundeskreisListe` | `void printFreundeskreis(FreundeskreisListe liste, int size)` |

## Tests

```c     -Datum.c
struct Datum
{
    int tag;
    int monat;
    int jahr;
};

//int berechneZeitDiff(struct Datum TagA, struct Datum TagB){
//
//}

//int bestimmeWochentag(struct Datum Tag){
//
//}
```
```c     -Person.c
struct Person
{
    char name[25];
    geburtstag meinGeburtstag;
    int telefonnummer;
};

typedef struct Person freund;

void printFreund(freund freundA){
  printf("%s - %d.%d.%d\n",freundA.name,
                           freundA.meinGeburtstag.tag,
                           freundA.meinGeburtstag.monat,
                           freundA.meinGeburtstag.jahr);
}

//int zumGeburtstagAnrufen(freund Freund){
//
//}
```
```c     -FreundeskreisListe.c
typedef freund FreundeskreisListe[ARRAYSIZE];

void printFreundeskreis(FreundeskreisListe liste, int size){
  printf("Meinen Freunde: \n");
  for (int i = 0; i < size; i++){
    printFreund(liste[i]);
  }
}
```
```c     +main.c
int main() {
  freund A = {"Peter", 1,1,2010, 1234};
  freund B = {.name = "Paul",
              .meinGeburtstag = {10, 1, 2013},
              .telefonnummer = 56756 };
  printFreund(A);

  FreundeskreisListe meineFreunde = {0};
  meineFreunde[0] = A;
  meineFreunde[1] = B;
  printFreundeskreis(meineFreunde, 2);
}
```
<script>
   LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)
</script>

> **Merke: ** Gliedern Sie Ihre Codebeispiele entsprechend einem logischen Zusammenhang. Damit eröffnet sich die Möglichkeit die Methoden und Datentypen in einer Implementierung wiederzuverwenden?


> **Aufgabe: ** Welche Erweiterungen und Änderungen müssten Sie vornehmen, um eine Liste der Studierenden der Universität mit einer Notendarstellung daraus zu entwickeln?

## Objektorientierung

Die objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das auf dem Konzept der "Objekte" basiert, die **Daten und Code enthalten** können: Daten in Form von Feldern (oft als Attribute oder Eigenschaften bekannt) und Code in Form von Prozeduren (oft als Methoden bekannt).

Ein Merkmal von Objekten ist, dass die eigenen Prozeduren eines Objekts auf die Datenfelder seiner selbst zugreifen und diese oft verändern können - Objekte haben somit eine Vorstellung davon oder von sich selbst :-).

Ein OOP-Computerprogramm kombiniert Objekt und lässt sie interagieren. Viele der am weitesten verbreiteten Programmiersprachen (wie C++, Java, Python usw.) sind Multi-Paradigma-Sprachen und unterstützen mehr oder weniger objektorientierte Programmierung, typischerweise in Kombination mit imperativer, prozeduraler Programmierung.

> **Merke: ** Unter einer Klasse versteht man in der objektorientierten Programmierung ein abstraktes Modell bzw. einen Bauplan für eine Reihe von ähnlichen Objekten.

<!--
style="width: 90%; max-width: 860px; display: block; margin-left: auto; margin-right: auto;"
-->
```ascii
main                        Farm                           Animals
+-----------------------+  +--------------------------+   +--------------------+
| Farm JohnsFarm;       |->| Animal myAnimals[];      |-> | string name;       |
| Farm PetersFarm;      |  | checkAnimalsPosition();  |   | ...                |
| ...                   |  | feedAnimals();           |
                           | getAnimalStatistics();   |    Buildings
                           | ...                      |   +--------------------+
                           | Farmbuilding buildings[];|-> | int purpose        |
                                                          | startScanning()    |
                                                          | ...                |
```

Die Datenstruktur eines Objekts wird durch die Attribute (Eigenschaften) seiner Klassendefinition festgelegt. Aber mit einer Klasse werden nicht nur Eigenschaften der Objekte festgelegt, sondern auch ihr Verhalten.

## C vs. C++

C++ kombiniert die Effizienz von C mit den Abstraktionsmöglichkeiten der objektorientierten Programmierung. C++ Compiler können C Code überwiegend kompilieren, umgekehrt funktioniert das nicht.

| Kriterium             | C                              | C++                                                           |
|:----------------------|:-------------------------------|:--------------------------------------------------------------|
| Programmierparadigma  | Prozedural                     | Prozedural, objektorientiert, funktional                      |
| Kapselung             | keine                          | Integration von Daten und Funktionen in `structs` und Klassen |
| Überladen             | nein                           | Funktions- und Operator-Überladung                            |
| Programmierung        | Präprozessor, C, Assemblercode | Präprozessor, C, C++, Assemblercode, Templates                |
| Konzept von Zeigern   | Pointer                        | (Smart-) Pointer, Referenzen                                  |
| Integrationsfähigkeit | gering                         | hoch (namespaces)                                             |

**Warum sollten wir uns nun mit C++ beschäftigen? Welche Möglichkeiten eröffnen sich daraus?**

C++ ermöglicht sowohl die effiziente und maschinennahe Programmierung als auch eine Programmierung auf hohem Abstraktionsniveau. Der Standard definiert auch eine Standardbibliothek, zu der verschiedene Implementierungen existieren. Entsprechend findet C++ sowohl auf der Systemprogrammierungsebene, wie auch der Anwendungsentwicklung Anwendung.

> Zunächst die gute Nachricht, C++ versteht auch C!

### Ein- und Ausgabe mit `iostreams`

Für die Ein- und Ausgabe der Daten in C++ werden Streams verwendet.
Während in C die Ein-, Ausgabe nur von elementaren Datentypen möglich ist, kann Stream-Konzept auf die neu definierten Datentypen erweitert werden.

Als Standard werden verwendet:

+ `std::cin` für die Standardeingabe (Tastatur),
+ `std::cout` für die Standardausgabe (Console) und
+ `std::cerr` für die Standardfehlerausgabe (Console)

Stream-Objekte  werden durch
`#include <iostream>`
bekannt gegeben. Definiert werden sie als Komponente der Standard Template Library (STL) im Namensraum `std`.

Mit Namensräumen können Deklarationen und Definitionen unter einem Namen zusammengefasst und gegen andere Namen abgegrenzt werden.

```
#include <iostream>

int main(void) {
  char hanna[]="Hanna";
  char anna[]="Anna";
  std::cout<<"Hallo "<<hanna<<std::endl;
  std::cout<<"Hallo "<<anna<<std::endl;
  return EXIT_SUCCESS;
}
```

Die Streams lassen sich nicht nur für die Standard Ein- und Ausgabe verwenden, sondern auch mit Dateien oder Zeichenketten.

Mehr zu `iostream` unter
[https://www.c-plusplus.net/forum/topic/152915/ein-und-ausgabe-in-c-io-streams](https://www.c-plusplus.net/forum/topic/152915/ein-und-ausgabe-in-c-io-streams)

### Referenzen und Zeiger

Neben bereits bekannten Zeigern gibt es in C++ Referenzen.
Referenzen ähnlich wie Zeiger sind Verweise auf Variablen (Objekte) und müssen auf eine Variable (Objekt) initialisiert werden.

```
int v=0;
int &rv = v;
rv++; //unterscheidet sich in Gebrauch nicht von einer Variable
```

** Referenz-Parameter einer Funktion**

Zeiger (Wiederholung)

```
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

Referenzen

```
#include <iostream>

void tauschen(char &anna, char &hanna){
  char aux=anna;
  anna=hanna;
  hanna=aux;
}

int main(void) {
  char anna='A',hanna='H';
  std::cout<<anna<<" "<<hanna<<std::endl;
  tauschen(anna,hanna);
  std::cout<<anna<<" "<<hanna<<std::endl;
  return EXIT_SUCCESS;
}
```

Konstante Referenzen können innerhalb der Funktion nicht verändern werden.

```
void tauschen(const char &anna, const char &hanna){
  char aux=anna;
  anna=hanna;//geht nicht
  hanna=aux; //geht nicht
}
```

Der Vorteil der Referenz-Parameter gegenüber den call-by-value-Parameter: es werden keine Kopien von Objekten (Variablen) angelegt.

Können in C++ immer Referenzen statt Zeiger verwenden? Nein, um den Speicherplazt dynamisch zur Verfügung zu stellen brauchen wir weiterhin Zeiger.



## Objektorientierung mit C++

Eine Klasse wird in C++ mit dem Schlüsselwort `class` definiert und enthält Daten  (member variables, Attribute) und Funktionen (member functions, Methoden). Der Zugriff auf alle Members wird durch die Schlüsselworte  `private`, `protected` oder `public` geregelt. Standardmäßig sind alle Members in der Klasse `private`.

```
#include <iostream>
class Datum
{
  //private:
    int tag;
    int monat;
    int jahr;
  //public:
    void ausgabe()//hier wird kein Parameter benoetigt, warum?
    {
        std::cout<<tag<<"."<<monat<<"."<<jahr<<std::endl;
    }
};

int main()
{
  Datum datum;
  datum.ausgabe();//was ist denn hier falsch?
  return 0;
}

```




## Beispiel des Tages
