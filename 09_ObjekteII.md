<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.3
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_ObjekteII.md)

# Memberfunktionen und Konstruktoren

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Vorlesung Prozedurale Programmierung`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2021/22`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | ` Elemente der Objektorientierten Programmierung`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_ObjekteII.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_ObjekteII.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Welche Aufgabe erfüllt ein Konstruktor?
* Was geschieht, wenn kein expliziter Konstruktor durch den Entwickler vorgesehen wurde?
* Wann ist ein Dekonstruktor erforderlich?
* Was bedeutet das "Überladen" von Funktionen?
* Nach welchen Kriterien werden überladene Funktionen differenziert?

---------------------------------------------------------------------

**Wie weit waren wir gekommen?**

```cpp   Rectangle
#include <iostream>

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
  std::cout << "area: " << rect.area();
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out `, `./a.out`)

## Parallelität von Klassen und Strukturen in C++

```cpp                     class.cpp
#include <iostream>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabe(){  // Achtung keine besonders gute Lösung
                     // siehe den Abschnitt "bessere Ausgabe"
        std::cout << name << " " << ort << " " << alter  << std::endl;
    }
};

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabe();
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

```cpp                     struct.cpp
#include <iostream>

struct Student{
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabe(){
        std::cout << name << " " << ort << " " << alter  << std::endl;
    }
};

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabe();
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

> **Merke: ** Während `struct` in C nur eine Datenstruktur beschreibt, kann in C++ damit ein Objekt spezifiziert werden!

> **Merke: ** Klassen und Strukturen unterscheiden sich unter C++ durch die Default-Zugriffsrechte und die Möglichkeit der Vererbung.

> Im Folgenden fokussieren die Ausführungen Klassen, eine analoge Anwendung mit Strukturen ist aber zumeist möglich.

## Memberfunktionen

Mit der Integration einer Funktion in eine Klasse wird diese zur _Methode_ oder _Memberfunktion_. Der Mechanismus bleibt zwar der gleiche, es erfolgt der Aufruf, ggf mit Parametern, die Abarbeitung realisiert Berechnungen, Ausgaben usw. und ein optionaler Rückgabewert bzw. geänderte Parameter (bei Call-by-Referenz Aufrufen) werden zurückgegeben.

Worin liegt der technische Unterschied?

```cpp                     ApplicationOfStructs.cpp
#include <iostream>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabeMethode(){
        std::cout << name << " " << ort << " " << alter  << std::endl;
    }
};

void ausgabeFunktion(Student studentA){
    std::cout << studentA.name << " " << studentA.ort << " " << studentA.alter  << std::endl;
}

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode();

  ausgabeFunktion(bernhard);

  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Methoden können, wie wir es bereits im Beispiel der vergangenen Woche gesehen werden auch von der Klassendefinition getrennt werden.

```cpp                     ApplicationOfStructs.cpp
#include <iostream>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabeMethode();    // Deklaration der Methode
};

// Implementierung der Methode
void Student::ausgabeMethode(){
    std::cout << name << " " << ort << " " << alter  << std::endl;
}

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode();
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Diesen Ansatz kann man weiter treiben und die Aufteilung auf einzelne Dateien realisieren. Der Code einer inline-Funktion wird vom Compiler direkt an der Stelle eingefügt, wo der Aufruf stattfindet. Die inline-Funktionen sollten aber möglichst klein gehalten werden. In der Klasse definierte Funktionen sind alle inline, d.h. umfangreiche Funktionen sollen sinnvollerweise außerhalb der Klasse definiert werden und in der Klasse nur deklariert. Es bietet sich weiterhin die Verteilung auf .h und .cpp-Dateien.

```cpp     -Student.h
#ifndef STUDENT_H_INCLUDED
#define STUDENT_H_INCLUDED

#include <iostream>
#include <string>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabeMethode();    // Deklaration der Methode
};

#endif
```
```cpp     -Student.cpp
#include "Student.h"

void Student::ausgabeMethode(){
    std::cout << name << " " << ort << " " << alter  << std::endl;
}

```
```cpp     +main.cpp
#include <iostream>
#include "Student.h"

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode();
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["Student.h", "Student.cpp", "main.cpp"]`, `g++ -Wall main.cpp Student.cpp -o a.out`, `./a.out`)

Was gab es noch mal an unserer `ausgabeMethode()` zu meckern? In der aktuellen Version geben wir das Gerät, auf das die Ausgabe umgesetzt wird explizt im Code an. Was aber, wenn jemand die Implementierung nutzen möchte und das Resultat eben nicht in der Konsole sondern auf dem Drucker, einem Speicher usw. ausgegeben wissen möchte?

Das "Zieldevice" wird als Referenz übergeben (vgl. Vorlesung 08). Damit erzeugen wir keine Kopie sondern können auf der ursprünglichen Instanz den Zustand verändern (Ausgabedaten übergeben).

```cpp                     ostream.cpp
#include <iostream>
#include <fstream>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode
};

// Implementierung der Methode
void Student::ausgabeMethode(std::ostream& os){
    os << name << " " << ort << " " << alter;
}

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  std::ofstream datei;
  datei.open ("StudentenListe.txt", std::ios::out);
  bernhard.ausgabeMethode(datei);
  datei.close();

  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

### Überladung von Methoden

C verbietet Funktionen die einen gleichen Namen haben. Damit ist die variable Verwendung von Funktionen in Abhängigkeit von der Signatur der Funktion nicht möglich.

```c                     overwrite.c
#include <stdio.h>

int Divide(int dividend, int divisor){
  return dividend / divisor;
}

double Divide(double dividend, double divisor){
  return dividend / divisor;
}

int main()
{
  int a = 5;
  int b = 10;
  int c = Divide(a, b);

  float x = 5.23;
  float y = 15.34;
  float z = Divide(x, y);

  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Beachten Sie einen zweiten Effekt im oben genannten Beispiel! Wenn Sie die Zeilen 7 bis 9 auskommentieren, kommt eine implizierter Cast-Operation also eine Typumwandlung zur Wirkung. Der Compiler bildet unsere Gleitkommazahlen auf Ganzzahldarstellungen ab und wendet die Funktion an. Das entspricht aber nicht unserer Intention in diesem Abschnitt - wir wollten ja zwei Funktionen für unterschiedliche Datentypen entwerfen.

C++ eröffnet mit dem Überladen von Funktionen neue Möglichkeiten. Dieser Mechanismus lässt sich auf Funktionen und Methoden anwenden.

```c                     overwrite.cpp
#include <stdio.h>

int Divide(int dividend, int divisor){
  return dividend / divisor;
}

double Divide(double dividend, double divisor){
  return dividend / divisor;
}

int main()
{
  int a = 5;
  int b = 10;
  int c = Divide(a, b);

  float x = 5.23;
  float y = 15.34;
  float z = Divide(x, y);

  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

```cpp                     ostream.cpp
#include <iostream>
#include <fstream>

class Seminar{
  public:
    std::string name;
    bool passed;
};

class Lecture{
  public:
    std::string name;
    float mark;
};

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void printCertificate(std::ostream& os, Seminar sem);
    void printCertificate(std::ostream& os, Lecture sem);
};

void Student::printCertificate(std::ostream& os, Seminar sem){
  std::string comment = " nicht bestanden";
  if (sem.passed)
    comment = " bestanden!";
  os << "\n" << name << " hat das Seminar " << sem.name <<  comment;
}

void Student::printCertificate(std::ostream& os, Lecture lect){
  os << "\n" << name << " hat in der Vorlesung " << lect.name << " die Note " << lect.mark << " erreicht";
}

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  Seminar roboticSeminar {"Robotik-Seminar", false};
  Lecture ProzProg {"Prozedurale Programmierung", 1.3};

  bernhard.printCertificate(std::cout, roboticSeminar);
  bernhard.printCertificate(std::cout, ProzProg);

  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

> **Merke: ** Der Rückgabedatentyp trägt nicht zur Unterscheidung der Methoden bei. Unterscheidet sich die Signatur nur in diesem Punkt, "meckert" der Compiler.

## Initalisierung/Zerstören eines Objektes

Die Klasse spezifiziert unter anderem (!) welche Daten in den Instanzen/Objekten zusammenfasst werden. Wie aber erfolgt die Initialisierung? Bisher haben wir die Daten bei der Erzeugung der Instanz übergeben.

```cpp                     Konstruktoren.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort;

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode
};

// Implementierung der Methode
void Student::ausgabeMethode(std::ostream& os){
    os << name << " " << ort << " " << alter << "\n";
}

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student alexander { .name = "Humboldt" , .ort = "Berlin"  };
  alexander.ausgabeMethode(std::cout);

  Student unbekannt;
  unbekannt.ausgabeMethode(std::cout);

  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Es entstehen 3 Instanzen der Klasse `Student`, die sich im Variablennamen `bernhard`, `alexander` und `unbekannt` und den Daten unterscheiden.

Im Grunde können wir unsere drei Datenfelder im Beispiel in vier
Kombinationen  initialisieren:

```
{name, alter, ort}
{name, alter}
{name}
{}
```

**Elementinitialisierung beim Aufruf:**

| Umsetzung                                                                             | Beispiel                                      |
|:------------------------------------------------------------------------------------- |:--------------------------------------------- |
| vollständige Liste in absteigender Folge (uniforme Initialisierung)                   | `Student Bernhard {"Cotta", 25, "Zillbach"};` |
| unvollständige Liste (die fehlenden Werte werden durch Standard Defaultwerte ersetzt) | `Student Bernhard {"Cotta", 25};`             |
| vollständig leere Liste, die zum Setzen von Defaultwerten führt                                                                                      | `Student Bernhard {};`                        |
| Aggregierende Initialisierung (C++20)                                                                                      |   `Student alexander = { .ort = "unknown"}; `                                             |

Wie können wir aber:

+ erzwingen, dass eine bestimmte Membervariable in jedem Fall gesetzt wird (weil die Klasse sonst keinen Sinn macht)
+ prüfen, ob die Werte einem bestimmten Muster entsprechen ("Die PLZ kann keine negativen Werte umfassen")
+ automatische weitere Einträge setzen (einen Zeitstempel, der die Initialisierung festhält)
+ ... ?

### Konstruktoren

Konstruktoren dienen der Koordination der Initialisierung der Instanz einer Klasse. Sie werden entweder implizit über den Compiler erzeugt oder explizit durch den Programmierer angelegt.

```cpp
class class_name {
  access_specifier_1:
    typ member1;
  access_specifier_2:
    typ member2;
    memberfunktionA(...)

  class_name (...) {           // <- Konstruktor
    // Initalisierungscode
  }
};

class_name instance_name (...);
```

> **Merke: ** Ein Konstruktor hat keinen Rückgabetyp!

Beim Aufruf `Student bernhard {"Cotta", 25, "Zillbach"};` erzeugt der Compiler eine Methode `Student::Student(std::string, int, std::string)`, die die Initialisierungsparameter entgegennimmt und diese der Reihenfolge nach an die Membervariablen übergibt. Sobald wir nur einen explizten Konstruktor integrieren, weist der Compiler diese Verantwortung von sich.

Entfernen Sie den Kommentar in Zeile 11 und der Compiler macht Sie darauf aufmerksam.

```cpp                     defaultConstructor.cpp
#include <iostream>

class Student{
  public:
    std::string name;  // "-"
    int alter;
    std::string ort;

    void ausgabeMethode(std::ostream& os){
        os << name << " " << ort << " " << alter;
    }

    //Student();
};

// Implementierung der Methode


int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Dabei sind innerhalb des Konstruktors zwei Schreibweisen möglich:

```cpp
//Initalisierung
Student(std::string name, int alter, std::string ort): name(name), alter(alter), ort(ort)
{
}

// Zuweisung innerhalb des Konstruktors
Student(std::string name, int alter, std::string ort):
    this->name = name;
    this->alter = alter;
    this->ort = ort;
}
```

Die zuvor beschriebene Methodenüberladung kann auch auf die Konstruktoren angewandt werden. Entsprechend stehen dann eigene Aufrufmethoden für verschiedene Datenkonfigurationen zur Verfügung. In diesem Fall können wir auf drei verschiedenen Wegen Default-Werte setzen:

+ ohne spezfische Vorgabe wird der Standardinitialisierungswert verwendt (Ganzzahlen 0, Gleitkomma 0.0, Strings "")
+ die Vorgabe eines indivduellen Default-Wertes (vgl. Zeile 5)

```cpp                     constructor.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort; // = "Freiberg"

    void ausgabeMethode(std::ostream& os){
        os << name << " " << ort << " " << alter << "\ņ";
    }

    Student(std::string name, int alter, std::string ort): name(name), alter(alter), ort(ort)
    {
    }

    Student(std::string name): name(name)
    {
    }
};

int main()
{
  Student bernhard {"Cotta", 25, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student alexander = Student("Humboldt");
  alexander.ausgabeMethode(std::cout);

  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Delegierende Konstruktoren rufen einen weiteren Konstruktor für die teilweise
Initialisierung auf. Damit lassen sich Codeduplikationen, die sich aus der
Kombination aller Parameter ergeben, minimieren.

```cpp
Student(std::string n, int a, std::string o): name{n}, alter{a}, ort{o} { }
Student(std::string n) : Student (n, 18, "Freiberg") {};
Student(int a, std::string o): Student ("unknown", a, o) {};
```

### Destruktoren

```cpp                     Destructor.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(std::string n, int a, std::string o);
    ~Student();
};

Student::Student(std::string n, int a, std::string o): name{n}, alter{a}, ort{o} {}

Student::~Student(){
  std::cout << "Destructing object of type 'Student' with name = '" << this->name << "'\n";
}

int main()
{
  Student max {"Maier", 19, "Dresden"};
  std::cout << "End...\n";
  return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Destruktoren werden aufgerufen, wenn eines der folgenden Ereignisse eintritt:

* Das Programm verlässt den Gültigkeitsbereich (*Scope*, d.h. einen Bereich der mit `{...}` umschlossen ist) eines lokalen Objektes.
* Ein Objekt, das `new`-erzeugt wurde, wird mithilfe von `delete` explizit aufgehoben (Speicherung auf dem Heap)
* Ein Programm endet und es sind globale oder statische Objekte vorhanden.
* Der Destruktor wird unter Verwendung des vollqualifizierten Namens der Funktion explizit aufgerufen.

Einen Destruktor explizit aufzurufen, ist selten notwendig (oder gar eine gute Idee!).

## Anwendung

1. Ansteuern einer mehrfarbigen LED

    Die Auflistung der Memberfunktionen der entsprechenden Klasse finden Sie unter [Link](https://microsoft.github.io/azure-iot-developer-kit/docs/apis/led/)

2. Abfragen eines Sensors

    Die Auflistung der Memberfunktionen der entsprechenden Klassen finden Sie unter [Link](https://microsoft.github.io/azure-iot-developer-kit/docs/apis/)

Der Beispielcode für die Anwendungen ist in den `examples` Ordnern des Projektes enthalten.
