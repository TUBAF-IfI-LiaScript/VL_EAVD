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

| Standard    |                 |                 |            |          |            |
|:----------- |:--------------- |:--------------- |:---------- |:-------- |:---------- |
| **C89/C90** | auto            | `double`        | `int`      | `struct` | `break`    |
|             | `else`          | `long`          | `switch`   | `case`   | `enum`     |
|             | register        | `typedef`       | `char`     | `extern` | `return`   |
|             | union           | `const`         | `float`    | `short`  | `unsigned` |
|             | `continue`      | `for`           | `signed`   | `void`   | default    |
|             | `goto`          | `sizeof`        | volatile   | `do`     | `if`       |
|             | static          | `while`         |            |          |            |
| **C99**     | `_Bool`         | _Complex        | _Imaginary | `inline` | restrict   |
| **C11**     | _Alignas        | _Alignof        | _Atomic    | _Generic | _Noreturn  |
|             | _Static\_assert | \_Thread\_local |            |          |            |

**Inhalt der heutigen Veranstaltung**

* Wie strukturieren wir unseren Code?
* Motivation der Objektorientierten Programmierung
* Entwicklung von C++ aus dem bekannten Set von C Schlüsselworten

**Fragen an die heutige Veranstaltung ...**

* Was sind Objekte?

## Motivation

Nehmen wir an, dass Sie einen Code entwickeln, der unterschiedliche Implementierungen vereint. Wir kombinieren dazu verschiedene Datentypen und Funktionen. Wie aber sieht es um die Übersichtlichkeit und Wiederverwendbarkeit aus?

```cpp                 ZusammengesetzteDatenstrukturen.c
#include <stdio.h>

struct Datum
{
    int tag;
    int monat;
    int jahr;
};

int berechneZeitDiff(struct Datum TagA, struct Datum TagB){
  //
  return 1;
}

int bestimmeWochentag(struct Datum Tag){
  //
  return 1;
}

struct Person
{
    char name[25];
    struct Datum geburtstag;
    int telefonnummer;
};

typedef struct Person Freund;

void printFreund(Freund freundA){
  printf("%s - %d.%d.%d\n",freundA.name,
                           freundA.geburtstag.tag,
                           freundA.geburtstag.monat,
                           freundA.geburtstag.jahr);
}

int zumGeburtstagAnrufen(Freund freund, struct Datum heute){
  //
  return 1;
}

void printFreundeskreis(Freund liste[], int size){
  printf("Meinen Freunde: \n");
  for (int i = 0; i < size; i++){
    printFreund(liste[i]);
  }
}

int main() {
  Freund A = {"Peter", 1,1,2010, 1234};
  Freund B = {.name = "Paul",
              .geburtstag = {10, 1, 2013},
              .telefonnummer = 56756 };
  printFreund(A);

  Freund meineFreunde[] = {0};
  meineFreunde[0] = A;
  meineFreunde[1] = B;
  printFreundeskreis(meineFreunde, 2);
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

> **Aufgabe: ** Erweitern Sie die Implementierung so, dass in der Methode `zumGeburtstagAnrufen()` anhand der Tage und Monatswerte der Geburtstage abgeprüft wird, ob der angerufene denn wirklich Geburtstag hat. Die Funktion soll eine "1" zurückgeben, wenn das der Fall ist.

Das prozedurale Programmierparadigma zielt darauf imperative Programme in überschaubare Teile aufzugliedern. Diese Teile werden als Prozeduren (Unterprogramme, Routinen oder Funktionen) bezeichnet. Insgesamt soll damit sichergestellt werden, das der Programmcode übersichtlicher wird und unnötige Code-Wiederholungen vermieden werden. Durch die Abstraktion der Algorithmen stellt das prozedurale Software-Paradigma einen entscheidenden Schritt von einfachen Assemblersprachen hin zu komplexeren Hochsprachen dar.

> "Teile und Herrsche" ist ein häufig bemühter Ausdruck in der Informatik. Wir haben ihn bereits in Bezug auf Algorithmen kennen gelernt, er kann aber gleichermaßen auch auf die Codezerlegung angewandt werden.

## Header-Files

Wir zerlegen unser Projekt in einzelne Dateien! Diese können wir einfach in anderen Projekten einbinden, ohne die gesamte Implementierungen aus der vorangegangenen Anwendung zu integrieren.

| Daten                | Methoden                                                      |
| -------------------- | ------------------------------------------------------------- |
| `struct Datum`       | `int berechneZeitDiff(struct Datum TagA, struct Datum TagB)`  |
|                      | `int bestimmeWochentag(struct Datum Tag)`                     |
|                      | ...                                                           |
| `struct Person`      | `int printFreund(freund FreundA)`          |
|                      | `int zumGeburtstagAnrufen(freund Freund)`                     |
|                      | ...                                                           |
| `FreundeskreisListe` | `void printFreundeskreis(FreundeskreisListe liste, int size)` |

C und C++ unterscheiden zu diesem Zweck zwei Dateitypen - die eigentliche Implementierung `.c` und den "Bauplan", die Headerdateien `.h`.  Eine Headerdatei sollte ausschließlich enthalten:

+ Funktionsdeklarationen (Prototypen)
+ Variablen-Deklarationen (extern)
+ globale Konstanten (#define, const)
+ eigene Typ-Definitionen (typedef struct, union, enum)

> **Merke: ** Die Header-Files enthalten die Basisinformationen für die Nutzung die in den Code-Dateien enthaltene Implementierung.

```c     -Datum.h
#ifndef DATUM_H_INCLUDED
#define DATUM_H_INCLUDED
/* ^^ these are the include guards */

struct Datum
{
    int tag;
    int monat;
    int jahr;
};

#endif
```
```c     -Person.h
#include <stdio.h>
#include "Datum.h"

#ifndef PERSON_H_INCLUDED
#define PERSON_H_INCLUDED

struct Person
{
    char name[25];
    struct Datum Geburtstag;
    int telefonnummer;
};

void printPerson(struct Person freundA);

#endif
```
```c     -Person.c
#include "Person.h"

void printPerson(struct Person freundA){
  printf("%s - %d.%d.%d\n",freundA.name,
                           freundA.Geburtstag.tag,
                           freundA.Geburtstag.monat,
                           freundA.Geburtstag.jahr);
}

```
```c     +main.c
#include "Person.h"

void printFreundeskreis(struct Person liste [], int size){
  printf("Meinen Freunde: \n");
  for (int i = 0; i < size; i++){
    printPerson(liste[i]);
  }
}

int main() {
  struct Person A = {"Peter", {1, 1, 2010}, 1234};
  struct Person B = {.name = "Paul",
              .Geburtstag = {10, 1, 2013},
              .telefonnummer = 56756 };
  printPerson(A);

  struct Person meineFreunde[2] = {0};
  meineFreunde[0] = A;
  meineFreunde[1] = B;
  printFreundeskreis(meineFreunde, 2);
}
```
@LIA.eval(`["Datum.h", "Person.h", "Person.c", "main.c"]`, `gcc -Wall main.c Person.c Datum.h -o a.out`, `./a.out`)

Wie erfolgt die Kompilierung in diesem Fall?

**Schritt 1 - Kompilieren**

```
gcc main.c -o main.o -c
gcc Person.c -o Person.o -c
```

**Schritt 2 - Linken**

```
gcc -o myprog main.o Person.o
```

Üblicherweise werden sogenannte Makesysteme wie das Programm Make, qmake oder Scons für die automatisierte Ausführung von Kompilation und Linken genutzt.

## Objektorientierte Programmierung

Wir kapseln zusammengehörigen Code in Dateien - Ziel erreicht? In den Dateien stehen unsere Datenformate und die eigentlichen Funktionen aber konzeptionell immer noch immer nebeneinander.

```c
struct Person
{
    char name[25];
    struct Datum geburtstag;
    int telefonnummer;
};

typedef struct Person Freund;

void printFreund(Freund freundA){
  printf("%s - %d.%d.%d\n",freundA.name,
                           freundA.geburtstag.tag,
                           freundA.geburtstag.monat,
                           freundA.geburtstag.jahr);
}

int zumGeburtstagAnrufen(Freund freundm, struct Datum heute){
  //
  return 1;
}
```

Was wollen wir mit der Zusammenfassung in einer Datei eigentlich ausdrücken? Auf eine `Person` (für die wir den Alias-Typ `Freund`) benutzen, können die Funktionen `void printFreund(Freund freundA)` und `int zumGeburtstagAnrufen(Freund freund)` angewandt werden. Eine echte Zuordnung ist nicht gegeben!

Die objektorientierte Programmierung (OOP) ist ein Programmierparadigma, das auf dem Konzept der "Objekte" basiert, die Daten und Code enthalten können: Daten in Form von Feldern (oft als Attribute oder Eigenschaften bekannt) und Code in Form von Prozeduren (oft als Methoden bekannt).

```ascii
                 Person
                   |
  +----------------+-----------------+
  |                                  |
  +- char name[25];                  +- print()
  +- struct Datum geburtstag;        +- zumGeburtstagAnrufen()
  +- int telefonnummer;              +- ...

     Daten                              Methoden/Funktionen                    .
```

Ein Merkmal von Objekten ist, dass die eigenen Prozeduren eines Objekts auf die Datenfelder seiner selbst zugreifen und diese oft verändern können - Objekte haben somit eine Vorstellung davon oder von sich selbst :-).

Ein OOP-Computerprogramm kombiniert Objekt und lässt sie interagieren. Viele der am weitesten verbreiteten Programmiersprachen (wie C++, Java, Python usw.) sind Multi-Paradigma-Sprachen und unterstützen mehr oder weniger objektorientierte Programmierung, typischerweise in Kombination mit imperativer, prozeduraler Programmierung.

<!--
style="width: 90%; max-width: 860px; display: block; margin-left: auto; margin-right: auto;"
-->
```ascii
main                        Farm                           Animal
+-----------------------+  +--------------------------+   +--------------------+
| Farm JohnsFarm;       |->| Animal myAnimals[];      |-> | string name;       |
| Farm PetersFarm;      |  | checkAnimalsPosition();  |   | ...                |
| ...                   |  | feedAnimals();           |
                           | getAnimalStatistics();   |    Building
                           | ...                      |   +--------------------+
                           | Farmbuilding buildings[];|-> | int purpose        |
                                                          | startScanning()    |
                                                          | ...                |
```

Wir erzeugen ausgehend von unserem Bauplan verschiedene Instanzen / Objekte vom Typ `Animals`. Jede hat den gleichen Funktionsumfang, aber unterschiedliche Daten.

> **Merke: ** Unter einer Klasse versteht man in der objektorientierten Programmierung ein abstraktes Modell bzw. einen Bauplan für eine Reihe von ähnlichen Objekten.

## C vs. C++

Analog zu C ist C++ eine von der ISO genormte Programmiersprache. Sie wurde ab 1979 von Bjarne Stroustrup  bei AT&T als Erweiterung der Programmiersprache C entwickelt. Bezeichnenderweise trug C++ zunächst den Namen "C with classes".
C++ erweitert die Abstraktionsmöglichkeiten erlaubt aber trotzdem eine
maschinennahe Programmierung. Der Standard definiert auch eine Standardbibliothek, zu der wiederum verschiedene Implementierungen existieren.

| Jahr | Entwicklung                                                                                                                                  |
|:---- |:-------------------------------------------------------------------------------------------------------------------------------------------- |
| 197? | Anfang der 70er Jahre entsteht die Programmiersprache C                                                                                      |
| ...        |                                                                                                                                         |
| 1979 | „C with Classes“ -  Klassenkonzept mit Datenkapselung, abgeleitete Klassen, ein strenges Typsystem, Inline-Funktionen und Standard-Argumente |
| 1983 | "C++" - Überladen von Funktionsnamen und Operatoren, virtuelle Funktionen, Referenzen, Konstanten, eine änderbare Freispeicherverwaltung     |
| 1985 | Referenzversion                                                                                                                              |
| 1989 | Version 2.0 - Mehrfachvererbung, abstrakte Klassen, statische Elementfunktionen, konstante Elementfunktionen                                 |
| 1998 | ISO/IEC 14882:1998 oder C++98                                                                                                                |
| ...  | Kontinuierliche Erweiterungen C++11, C++20, ...                                                                                              |

### Konzeptionelle Unterschiede

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

### Was ändert sich?

C++ adaptiert einige der C Konzepte oder erweitert diese. Dabei werden bestimmte Symbole einer alternativen Bedeutung unterworfen.

**Ein- und Ausgabe**

Wir kennen die Ausgabe mittels `printf` aus dem C-Kontext. Dieser kann auch unter C++ verwendet werden. C++  stellt das Konzept der Streams bereit, dass im Unterschied zu den elementaren Datentypen von `printf` auf die neu definierten Datentypen (Klassen) erweitert werden kann.

Als Standard werden verwendet:

+ `std::cin` für die Standardeingabe (Tastatur),
+ `std::cout` für die Standardausgabe (Console) und
+ `std::cerr` für die Standardfehlerausgabe (Console)

> **Achtung:** Das `std::` ist ein zusätzlicher Indikator für eine bestimmte Implementierung, ein sogenannter Namespace. Um sicherzustellen, dass eine spezifische Funktion, Datentyp etc. genutzt wird stellt man diese Bezeichnung dem verwendenten Element zuvor. Mit `using namespace std;` kann man die permanente Nennung umgehen.

Stream-Objekte  werden durch
`#include <iostream>`
bekannt gegeben. Definiert werden sie als Komponente der Standard Template Library (STL) im Namensraum `std`.

Mit Namensräumen können Deklarationen und Definitionen unter einem Namen zusammengefasst und gegen andere Namen abgegrenzt werden.

```cpp   iostream.cpp
#include <iostream>

int main(void) {
  char hanna[]="Hanna";
  char anna[]="Anna";
  std::cout << "C++ stream: " << "Hallo "<< hanna << ", " << anna <<std::endl;
  printf("C funktioniert auch hier %s", hanna);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

Die Streams lassen sich nicht nur für die Standard Ein- und Ausgabe verwenden, sondern auch mit Dateien oder Zeichenketten.

Mehr zu `iostream` unter
[https://www.c-plusplus.net/forum/topic/152915/ein-und-ausgabe-in-c-io-streams](https://www.c-plusplus.net/forum/topic/152915/ein-und-ausgabe-in-c-io-streams)

**Echter string Typ**

C++ implementiert einen separaten `string`-Datentyp (Klasse), die ein deutliche komfortableren Umgang mit Texten erlaubt. Beim Anlegen eines muss nicht angegeben werden, wie viele Zeichen reserviert werden sollen. Zudem könenn Strings einfach zuweisen und vergleichen werden, wie es für andere Datentypen üblich ist. Die C `const char *` Mechanismen funktionieren aber auch hier.

```cpp   string.cpp
#include <iostream>
#include <string>

int main(void) {
  std::string hanna = "Hanna";
  std::string anna = "Anna";
  std::string alleBeide = anna + " + " + hanna;
  std::cout<<"Hallo: "<<alleBeide<<std::endl;
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

**Referenzen und Zeiger**

Neben bereits bekannten Zeigern gibt es in C++ Referenzen.
Referenzen ähnlich wie Zeiger sind Verweise auf Variablen (Objekte) und müssen auf eine Variable (Objekt) initialisiert werden.

```cpp
int v=0;
int &rv = v;
rv++; //unterscheidet sich in Gebrauch nicht von einer Variable
```

**Referenz-Parameter einer Funktion**

Zeiger (Wiederholung)

```cpp   pointer.cpp
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
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

Referenzen

```cpp references.cpp
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
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

Konstante Referenzen können innerhalb der Funktion nicht verändern werden.

```cpp
void tauschen(const char &anna, const char &hanna){
  char aux=anna;
  anna=hanna;//geht nicht
  hanna=aux; //geht nicht
}
```

Der Vorteil der Referenz-Parameter gegenüber den call-by-value-Parameter: es werden keine Kopien von Objekten (Variablen) angelegt.

Können in C++ immer Referenzen statt Zeiger verwenden? Nein, um den Speicherplazt dynamisch zur Verfügung zu stellen brauchen wir weiterhin Zeiger.

## Objektorientierung mit C++

Eine Klasse wird in C++ mit dem Schlüsselwort `class` definiert und enthält Daten  (member variables, Attribute) und Funktionen (member functions, Methoden).

Klassen erweitern das Konzept der `structs` und verschmelzen Daten und Methoden
in einem "Objekt" und deklarieren den individuellen Zugriff. Die wichtigste Eigenschaft einer Klasse ist, dass es sich um einen Typ handelt!

```cpp
class class_name {
  access_specifier_1:
    member1;
  access_specifier_2:
    member2;
  ...
};   // <- Das Semikolon wird gern vergessen

class_name instance_name;
```
Wenn `class_name`  ein gültiger Bezeichner für die Klasse ist, ist `instance_name` eine optionale Liste von Namen für Objekte dieser Klasse. Der Hauptteil der Deklaration kann _member_ enthalten, die entweder Daten- oder Funktionsdeklarationen sein können und jeweils einem Zugriffsbezeichner `access_spefier`.

Ein Zugriffsbezeichner ist eines der folgenden drei Schlüsselwörter: `private`, `public` oder `protected`. Diese Bezeichner ändern die Zugriffsrechte für die *member*, die ihnen nachfolgen:

+ `private` *member* einer Klasse sind nur von anderen *members* derselben Klasse (oder von ihren "Freunden") aus zugänglich.
+ `protected`  *member*  sind von anderen  *member*  derselben Klasse (oder von ihren "Freunden") aus zugänglich, aber auch von Mitgliedern ihrer abgeleiteten Klassen.
+ `public` *member*  sind öffentliche  *member*  von überall her zugänglich, wo das Objekt sichtbar ist.

Standardmäßig sind alle Members in der Klasse `private`!

```cpp      FirstClassExample.cpp
#include <iostream>

class Datum
{
  public:
    int tag;
    int monat;
    int jahr;

    void print(){
        std::cout << tag << "." << monat <<"." << jahr <<std::endl;
    }
};

int main()
{
  // 1. Instanz der Klasse, Objekt myDatumA
  Datum myDatumA;
  myDatumA.tag = 12;
  myDatumA.monat = 12;
  myDatumA.jahr = 2000;
  myDatumA.print();

  // 2. Instanz der Klasse, Objekt myDatumB
  // alternative Initialisierung
  Datum myDatumB = {.tag = 12, .monat = 3, .jahr = 1920};
  myDatumB.print();
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

Und wie können wir weitere Methoden zu unserer Klasse hinzufügen?

```cpp      AdditionalMethod.cpp
#include <iostream>
#include <ctime>

class Datum{
  public:
    int tag;
    int monat;
    int jahr;

    const int monthDays[12] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    void print(){
        std::cout << tag << "." << monat <<"." << jahr <<std::endl;
    }

    int istSchaltJahr(){
      if (((jahr % 4 == 0) && (jahr % 100 != 0)) || (jahr % 400 == 0)) return 1;
      else return 0;
    }

    int nterTagimJahr(){
      int n = tag;
      for (int i=0; i<monat - 1; i++){
          n += monthDays[i];
      }
      if (monat > 2) n += istSchaltJahr();
      return n;
    }
};

int main()
{
  Datum myDatumA;
  myDatumA.tag = 31;
  myDatumA.monat = 12;
  myDatumA.jahr = 2000;
  myDatumA.print();
  std::cout << myDatumA.nterTagimJahr() << "ter Tag im Jahr " << myDatumA.jahr << std::endl;
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

### Objekte in Objekten

Natürlich lassen sich Klassen beliebig miteinander kombinieren. Das folgende Beispiel reimplementiert unsere Freundesliste aus der C-Welt.

```cpp      ClassOfFriends.cpp
#include <iostream>
#include <ctime>
#include <string>

class Datum{
  public:
    int tag;
    int monat;
    int jahr;

    void print(){
        std::cout << tag << "." << monat <<"." << jahr <<std::endl;
    }
};

class Person{
  public:
    Datum geburtstag;
    std::string name;

    void print(){
        std::cout << name << ": ";
        geburtstag.print();
        std::cout <<std::endl;
    }

    int zumGeburtstagAnrufen() {
       time_t t = time(NULL);
       tm* tPtr = localtime(&t);
       if ((geburtstag.tag == tPtr->tm_mday) &&
           (geburtstag.monat == (tPtr->tm_mon + 1))) {
          std::cout << "\"Weil heute Dein ... \"" <<std::endl;
          return 1;
       }
       else return -1;
    }
};

int main()
{
  Person freundA = {.geburtstag = {1, 2, 2020}, .name = "Peter"};
  freundA.print();
  if (freundA.zumGeburtstagAnrufen() == 1){
      std::cout << "Zum Geburtstag gratuliert!" <<std::endl;
  }
  else{
      std::cout << freundA.name << " hat heute nicht Geburtstag" <<std::endl;
  }
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

> **Welche Unterschiede sehen Sie den Unterschied im Vergleich zu unserer C-Implementierung?**

### Datenkapselung

Als Datenkapselung bezeichnet man das Verbergen von Implementierungsdetails einer Klasse. Auf die interne Daten kann nicht direkt zugegriffen werden, sondern nur über definierte Schnittstelle, die durch  `public`-Methoden repräsentiert wird.

+ get- und set-Methoden
+ andere Methoden

```cpp getSetMethods.cpp
#include <iostream>
using namespace std;
class Datum
{
    private:
      int tag;
      int monat;
      int jahr;
    public:
      void setTag(int _tag){
        tag=_tag;
      }
      void setMonat(int _monat){
        monat=_monat;
      }
      void setJahr(int _jahr){
        jahr=_jahr;
      }
      int getTag(){
        return tag;
      }
      //analog monat und jahr
      void ausgabe()
      {
          cout<<tag<<"."<<monat<<"."<<jahr<<endl;
      }
 };

 int main()
 {
   Datum datum;
   datum.setTag(31);datum.setMonat(12);datum.setJahr(1999);
   datum.ausgabe();//jetzt geht es
 }
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)


### Aufteilung in Dateien

Natürlich können wir die Konzepte der Modularisierung auch unter C++ umsetzen. Unser kleines Beispiel umfasst dann 2 Klassen, die von einer `main.cpp` aufgerufen werden.

```c     -Datum.h
#include <iostream>

#ifndef DATUM_H_INCLUDED
#define DATUM_H_INCLUDED
/* ^^ these are the include guards */

class Datum
{
  public:
    int tag;
    int monat;
    int jahr;

    void print(){
        std::cout << tag << "." << monat <<"." << jahr <<std::endl;
    }
};

#endif
```
```cpp     -Person.h
#ifndef PERSON_H_INCLUDED
#define PERSON_H_INCLUDED

#include <iostream>
#include <string>
#include "Datum.h"

class Person{
  public:
    Datum geburtstag;
    std::string name;

    void print();
    int zumGeburtstagAnrufen();
};

#endif
```
```cpp     -Person.cpp
#include "Person.h"

void Person::print(){
    std::cout << name << ": ";
    geburtstag.print();
    std::cout <<std::endl;
}

int Person::zumGeburtstagAnrufen() {
   time_t t = time(NULL);
   tm* tPtr = localtime(&t);
   if ((geburtstag.tag == tPtr->tm_mday) &&
       (geburtstag.monat == (tPtr->tm_mon + 1))) {
      std::cout << "\"Weil heute Dein ... \"" <<std::endl;
      return 1;
   }
   else return -1;
}

```
```cpp     +main.cpp
#include <iostream>
#include <string>
#include "Person.h"

void GeburtstagsCheck(Person liste [], int size){
  printf("Meinen Freunde: \n");
  for (int i = 0; i < size; i++){
    if (liste[i].zumGeburtstagAnrufen() == 1){
        std::cout << "Zum Geburtstag gratuliert!" <<std::endl;
    }
    else{
        std::cout << liste[i].name << " hat heute nicht Geburtstag" <<std::endl;
    }
  }
}

int main() {
  Person freundA = {.geburtstag = {.tag = 1, .monat = 2, .jahr = 2020}, .name = "Peter"};
  Person freundB = {.geburtstag = {10, 1, 2013}, .name = "Paul"};

  Person meineFreunde[2];
  meineFreunde[0] = freundA;
  meineFreunde[1] = freundB;
  GeburtstagsCheck(meineFreunde, 2);
}
```
@LIA.eval(`["Datum.h", "Person.h", "Person.cpp", "main.cpp"]`, `g++ -Wall main.cpp Person.cpp Datum.h -o a.out`, `./a.out`)

## Beispiel des Tages

> **Aufgabe: ** Erweitern Sie das Beispiel um zusätzliche Funktionen, wie die Berechnung des Umfanges. Überwachen Sie die Eingaben der Höhe und der Breite. Sofern diese negativ sind, sollte die Eingabe zurückgewiesen werden.

```cpp   Rectangle
#include <iostream>
using namespace std;

class Rectangle {
  private:
    int width, height;
  public:
    void set_values (int,int);          // Deklaration
    int area() {return width*height;}   // Deklaration und Defintion
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}

int main () {
  Rectangle rect;
  rect.set_values (3,4);
  cout << "area: " << rect.area();
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)
