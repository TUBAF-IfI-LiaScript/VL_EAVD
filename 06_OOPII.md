<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.7
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md#10
        https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

link:   style.css

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/06_OOPII.md)

# Objektorientierte Programmierung mit C++

| Parameter                 | Kursinformationen                                                                                                                                     |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | @config.lecture                                                                                                                                       |
| **Semester**              | @config.semester                                                                                                                                      |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                     |
| **Inhalte:**              | `Operatorenüberladung / Vererbung`                                                                                                                    |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/06_OOPII.md) |
| **Autoren**               | @author                                                                                                                                               |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Was sind Operatoren?
* Warum werden eigene Operatoren für individuelle Klassen benötigt?
* Wann spricht man von Vererbung und warum wird sie angewendet?
* Welche Zugriffsattribute kennen Sie im Zusammenhang mit der Vererbung?

---------------------------------------------------------------------

## Reflexion Ihrer Fragen / Rückmeldungen

                          {{0-1}}
********************************************************************

> Zur Erinnerung ... Wettstreit zur partizipativen Materialentwicklung mit den Informatikern ...

<section class="flex-container">

<!-- class="flex-child" style="min-width: 250px;" -->
![Weihnachtsmänner](./images/00_Einfuehrung/Weihnachtsmaenner.jpeg "Preis für das aktivste Auditorium")

<div class="flex-child" style="min-width: 250px;">

<!-- data-type="none" -->
| Format                   | Informatik Studierende  | Nicht-Informatik Studierende |
|--------------------------|-------------------------|------------------------------|
| Verbesserungsvorschlag   | 3                       | 2                            |
| Fragen                   | 2                       | 8                            |
| generelle Hinweise       | 0                       | 1                            |

</div>

</section>

********************************************************************

                  {{1-2}}
********************************************************************

_Die Zustimmung (in Prozent) für die Verwendung der künstlichen Intelligenz im Pflegebereich unter der Bevölkerung von Mauritius und Réunion soll vergleichend betrachtet werden. Die Ergebnisse der Umfragen für die Jahre 2010 bis 2020 (je ein Wert pro Jahr) sollen in zwei Arrays erfasst werden (je ein Array pro Insel) und in einem Programm ausgewertet werden._

+ _Für beide Inseln soll aus den in Arrays erfassten Werten je ein Mittelwert berechnet werden. Schreiben Sie dazu eine Funktion, die ein Array übergeben bekommt und einen Mittelwert als ein Ergebnis an die main-Funktion zurück liefert. Rufen Sie die Funktion in der main-Funktion für jedes beider Arrays auf und geben Sie die Mittelwerte in der main-Funktion aus._
+ _Schreiben Sie eine weitere Funktion, die die korrespondierenden Werte beider Arrays miteinander vergleicht. Geben Sie für jedes Jahr aus, auf welcher Insel die Zustimmung größer war, bei den gleichen Werte ist eine entsprechende Meldung auszugeben. Rufen Sie die Funktion in der main-Funktion auf._
+ _In der main()-Funktion sind die Werte von der Console einzulesen und in die Arrays zu speichern._

Lösung Beispielaufgabe aus der Klausur

```cpp                     example.cpp
#include <iostream>

const int YEARS = 11; // von 2010 bis 2020 inkl.

double berechneMittelwert(const double arr[], int size) {
    double summe = 0.0;
    for (int i = 0; i < size; ++i) {
        summe += arr[i];
    }
    return summe / size;
}

void vergleicheZustimmung(const double arrMauritius[], const double arrReunion[], int size) {
    std::cout << "\nVergleich der Zustimmung pro Jahr:\n";
    for (int i = 0; i < size; ++i) {
        int jahr = 2010 + i;
        std::cout << "Jahr " << jahr << ": ";
        if (arrMauritius[i] > arrReunion[i]) {
            std::cout << "Mauritius hat höhere Zustimmung (" << arrMauritius[i] << "% vs " << arrReunion[i] << "%)\n";
        } else if (arrMauritius[i] < arrReunion[i]) {
            std::cout << "Réunion hat höhere Zustimmung (" << arrReunion[i] << "% vs " << arrMauritius[i] << "%)\n";
        } else {
            std::cout << "Beide Inseln haben gleiche Zustimmung (" << arrMauritius[i] << "%)\n";
        }
    }
}

int main() {
    //Das wäre die korrekte Lösung - um die Eingaben zu vermeiden habe ich feste Werte eingetragen
    //
    // double zustimmungMauritius[YEARS];
    // double zustimmungReunion[YEARS];
    //
    //std::cout << "Geben Sie die Zustimmung in Prozent für Mauritius für die Jahre 2010 bis 2020 ein:\n";
    //for (int i = 0; i < YEARS; ++i) {
    //    std::cout << "Jahr " << 2010 + i << ": ";
    //    std::cin >> zustimmungMauritius[i];
    //}
    //
    //std::cout << "\nGeben Sie die Zustimmung in Prozent für Réunion für die Jahre 2010 bis 2020 ein:\n";
    //for (int i = 0; i < YEARS; ++i) {
    //    std::cout << "Jahr " << 2010 + i << ": ";
    //    std::cin >> zustimmungReunion[i];
    //}

    // Feste Werte für Mauritius
    double zustimmungMauritius[YEARS] = {65.5, 67.2, 70.1, 72.3, 74.0, 75.5, 77.8, 80.0, 82.1, 84.3, 85.0}; 
    // Feste Werte für Réunion       
    double zustimmungReunion[YEARS] = {60.0, 62.5, 65.0, 68.0, 70.5, 73.0, 75.0, 78.0, 80.0, 83.0, 85.0}; 

    double mittelwertMauritius = berechneMittelwert(zustimmungMauritius, YEARS);
    double mittelwertReunion = berechneMittelwert(zustimmungReunion, YEARS);

    std::cout << "\nMittelwert der Zustimmung (2010-2020):\n";
    std::cout << "Mauritius: " << mittelwertMauritius << "%\n";
    std::cout << "Réunion:   " << mittelwertReunion << "%\n";

    vergleicheZustimmung(zustimmungMauritius, zustimmungReunion, YEARS);

    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

********************************************************************

## Rückblick

> Unter einer Klasse (auch Objekttyp genannt) versteht man in der objektorientierten Programmierung ein abstraktes Modell bzw. einen Bauplan für eine Reihe von ähnlichen Objekten.

![Prinzipdarstellung](images/06_OOPII/KlasseObjektBeispiel.png "Von Binz - Own Creation, CC BY-SA 4.0, https://commons.wikimedia.org/w/index.php?curid=62707688 ")

## Operatorenüberladung

Motivation
-------------------

Folgendes Beispiel illustriert den erreichten Status unserer C++ Implementierungen. Unsere Klasse `Student` besteht aus:

+ 3 Membervariablen (Zeile 5-7)
+ 2 Konstruktoren (Zeile 9-10)
+ 1 Memberfunktion (Zeile 12)

Alle sind als `public` markiert.

```cpp                     example.cpp
#include <iostream>

class Student {
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(std::string n);
    Student(std::string n, int a, std::string o);

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode
};

Student::Student(std::string n):
  name(n), alter(8), ort("Freiberg")
{}

Student::Student(std::string n, int a, std::string o):
  name(n), alter(a), ort(o)
{}

void Student::ausgabeMethode(std::ostream& os) {
  os << name << " " << ort << " " << alter << "\n";
}

int main()
{
  Student gustav = Student("Zeuner", 27, "Chemnitz");
  //Student gustav {"Zeuner", 27, "Chemnitz"};
  //Student gustav("Zeuner", 27, "Chemnitz");
  gustav.ausgabeMethode(std::cout);

  Student bernhard {"Cotta", 18, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student nochmalBernhard {"Cotta", 18, "Zillbach"};
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Aufgabe:** Schreiben Sie
>
> + eine Funktion `int vergleich(Student, Student)` und
>
> + eine Methode `int Student::vergleich(Student)`,
>
> die zwei Studenten miteinander vergleicht!
>
> Was ist der konzeptionelle Unterschied zwischen beiden Implementierungen?


{{1}}
> __Frage:__ Was ist der Nachteil unserer Lösung?

### Konzept

Das Überladen von Operatoren erlaubt die flexible klassenspezifische Nutzung von Arithmetischen- und Vergleichs-Symbolen wie  `+`, `-`, `*`, `==`. Damit kann deren Bedeutung für selbstdefinierte Klassen mit einer neuen Bedeutung versehen werden. Ausnahmen bilden spezielle Operatoren, die nicht überladen werden dürfen (  ?: ,  :: ,  . ,  .* , typeid , sizeof und die Cast-Operatoren).

```
Matrix a, b;
Matrix c = a + b;    \\ hier wird mit dem Plus eine Matrixoperation ausgeführt

String a, b;
String c = a + b;    \\ hier werden mit dem Plus zwei Strings konkateniert
```

Operatorüberladung ist Funktionsüberladung, wobei die Funktionen durch eine spezielle Namensgebung gekennzeichnet sind. Diese beginnen mit dem Schlüsselwort `operator`, das vom Symbol für den jeweiligen Operator gefolgt wird.

```cpp
class Matrix {
  public:
    Matrix operator+(Matrix zweiterOperand) { ... }
    Matrix operator/(Matrix zweiterOperand) { ... }
    Matrix operator*(Matrix zweiterOperand) { ... }
}

class String {
  public:
    String operator+(String zweiterString) { ... }
}
```

Operatoren können entweder als Methoden der Klasse oder als globale Funktionen überladen werden. Die Methodenbeispiele sind zuvor dargestellt, analoge Funktionen ergeben sich zu:

```cpp
class Matrix {
  public:
    ...
}

Matrix operator+(Matrix ersterOperand, Matrix zweiterOperand) { ... }
Matrix operator/(Matrix ersterOperand, Matrix zweiterOperand) { ... }
Matrix operator*(Matrix ersterOperand, Matrix zweiterOperand) { ... }
```

> **Merke:** Funktion oder Methode - welche Version sollte wann zum Einsatz kommen? Einstellige Operatoren `++` sollten Sie als Methode, zweistellige Operatoren ohne Manipulation der Operanden als Funktion implementieren. Für zweistellige Operatoren, die einen der Operanden verändern (`+=`), sollte als Methode realisiert werden.

Als Beispiel betrachten wir eine Klasse Rechteck und implementieren zwei Operatorüberladungen:

+ eine Vergleichsoperation
+ eine Additionsoperation die `A = A + B` oder abgekürzt `A+=B`

implementiert.

```cpp                     Comparison.cpp
#include <iostream>

class Rectangle {
  private:
    float width, height;
  public:
    Rectangle(int w, int h):
      width{w}, height{h}
    {}
    float area() {
      return width * height;
    }
    Rectangle operator+=(Rectangle offset) {
      float ratio = (offset.area() + this->area()) / this->area();
      this->width = ratio *  this->width;
      return *this;
    }
};

bool operator>(Rectangle a, Rectangle b) {
  if (a.area() > b.area())
    return 1;
  else
    return 0;
}

int main () {
  Rectangle rect_a(3,4);
  Rectangle rect_b(5,7);
  std::cout << "Vergleich: " << (rect_a > rect_b) << "\n";

  std::cout << "Fläche a : " << rect_a.area() << "\n";
  std::cout << "Fläche b : " << rect_b.area() << "\n";
  rect_a += rect_b;
  std::cout << "Summe    : " << rect_a.area();

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Merke:** Üblicherweise werden die Operanden, welche lediglich betrachtet werden, bei der Operatorüberladung als Referenzen übergeben. Damit wird eine Kopie vermieden.
> In Kombination mit dem Schlüsselwort `const` kann dem Compiler angezeigt werden. dass keine Veränderung an den Daten vorgenommen wird. Sie müssen also nicht gespeichert werden.

<!--- TODO: Aufgabe: Überlegen Sie sich, in welchen Situationen ein pass by reference eventuell doch sinnvoll wäre. --->

```
bool operator>(const Rectangle& a, const Rectangle& b) {
  if (a.area() > b.area())
    return 1;
  else
    return 0;
}
```

Stellen wir die Abläufe nochmals grafisch dar [Pythontutor](http://pythontutor.com/visualize.html#code=%23include%20%3Ciostream%3E%0A%0Aclass%20Rectangle%20%7B%0A%20%20private%3A%0A%20%20%20%20float%20width,%20height%3B%0A%20%20public%3A%0A%20%20%20%20Rectangle%28int%20w,%20int%20h%29%3A%20width%7Bw%7D,%20height%7Bh%7D%20%7B%7D%0A%20%20%20%20float%20area%28%29%20%7Breturn%20width*height%3B%7D%0A%7D%3B%0A%0Abool%20operator%3E%28Rectangle%26%20a,%20Rectangle%26%20b%29%7B%0A%20%20%20%20if%20%28a.area%28%29%20%3E%20b.area%28%29%29%20return%201%3B%0A%20%20%20%20else%20return%200%3B%0A%7D%0A%0Aint%20main%20%28%29%20%7B%0A%20%20Rectangle%20rect_a%283,4%29%3B%0A%20%20Rectangle%20rect_b%285,7%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Vergleich%3A%20%22%20%3C%3C%20%28rect_a%20%3E%20rect_b%29%20%3C%3C%20%22%5Cn%22%3B%0A%0A%20%20return%200%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D&textReferences=false)

### Anwendung

Im folgenden Beispiel wird der Vergleichsoperator `==` überladen. Dabei sehen
wir den Abgleich des Namens und des Alters als ausreichend an.

```cpp                     Comparison.cpp
#include <iostream>

class Student {
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(std::string n);
    Student(std::string n, int a, std::string o);

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode
    bool operator==(const Student&);
};

Student::Student(std::string n):
  name(n), alter(8), ort("Freiberg")
{}

Student::Student(std::string n, int a, std::string o):
  name(n), alter(a), ort(o)
{}

void Student::ausgabeMethode(std::ostream& os) {
  os << name << " " << ort << " " << alter << "\n";
}

bool Student::operator==(const Student& other) {
  if ((this->name == other.name) && (this->alter == other.alter))
    return true;
  else
    return false;
}

int main()
{
  Student gustav = Student("Zeuner", 27, "Chemnitz");
  gustav.ausgabeMethode(std::cout);

  Student bernhard {"Cotta", 18, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student NochMalBernhard {"Cotta", 18, "Zillbach"};
  NochMalBernhard.ausgabeMethode(std::cout);

  if (bernhard == NochMalBernhard)
    std::cout << "Identische Studenten\n";
  else
    std::cout << "Ungleiche Identitäten\n";
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


Eine besondere Form der Operatorüberladung ist der `<<`, mit dem die Ausgabe auf ein Streamobjekt realsiert werden kann.

Eine umfangreiche Diskussion zur Operatorüberladung finden Sie unter https://www.c-plusplus.net/forum/topic/232010/%C3%BCberladung-von-operatoren-in-c-teil-1/2

Ebenso eine ausführliche Auskunft über Operatoren und ihre Eigenheiten: https://en.cppreference.com/w/cpp/language/operators.html

## Vererbung

```cpp                     MultipleTypesOfPeople.cpp
#include <iostream>

class Student {
  public:
    std::string name;
    std::string ort;
    std::string studiengang;

    Student(std::string n, std::string o, std::string sg):
      name{n}, ort{o}, studiengang{sg}
    {}
    void printCertificate(std::ostream& os) {
      os << "Studentendatensatz: " << name << " " << ort << " " << studiengang << "\n";
    }
};

int main() {
  Student gustav = Student("Zeuner", "Chemnitz", "Mathematik");
  gustav.printCertificate(std::cout);

  // Professor winkler = Professor("Winkler", "Freiberg");
  // winkler.printCertificate(std::cout);
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Aufgabe:** Implementieren Sie eine neue Klasse `Professor`, die aber auf die Membervariable `Studiengang` verzichtet, aber eine neue Variable `Fakultät` einführt.

### Motivation

> **Merke:** Eine unserer Hauptmotivationen bei der "ordentlichen" Entwicklung von Code ist die Vermeidung von Code-Duplikationen!

In unserem Code entstehen Dopplungen, weil bestimmte Variablen oder Memberfunktionen usw. mehrfach für individuelle Klassen implementiert werden. Dies wäre für viele Szenarien analog der Fall:

| Basisklasse | abgeleitete Klassen                 | Gemeinsamkeiten                                                  |
| ----------- | ----------------------------------- | ---------------------------------------------------------------- |
| Fahrzeug    | Flugzeug, Boot, Automobil           | Position, Geschwindigkeit, Zulassungsnummer, Führerscheinpflicht |
| Datei       | Foto, Textdokument, Datenbankauszug | Dateiname, Dateigröße, Speicherort                               |
| Nachricht   | Email, SMS, Chatmessage             | Adressat, Inhalt, Datum der Versendung                           |

> **Merke:**  Die _Vererbung_ ermöglicht die Erstellung neuer Klassen, die ein in existierenden Klassen definiertes Verhalten wieder verwenden, erweitern und ändern. Die Klasse, deren Member vererbt werden, wird Basisklasse genannt, die erbende Klasse als abgeleitete Klasse bezeichnet.

### Implementierung in C++

In C++ werden Vererbungsmechanismen folgendermaßen abgebildet:

```cpp
class Fahrzeug {
  public:
    int aktuellePosition[2];    // lat, long Position auf der Erde
    std::string zulassungsnummer;
    bool fuehrerscheinpflichtig
    ...
};

class Flugzeug: public Fahrzeug {
  public:
    int flughoehe;
    void fliegen();
    ...
};

class Boot: public Fahrzeug {
  public:
    void schwimmen();
    ...
};
```

Die allgemeinere Klasse `Fahrzeug` liefert einen Bauplan für die spezielleren Klassen, die diese Vorgaben weiter ergänzen. Folglich müssen wir uns die Frage stellen, welche Daten oder Funktionalität übergreifend abgebildet werden soll und welche individuell realisiert werden sollen.

Dabei können ganze Ketten von Vererbungen entstehen, wenn aus einem sehr allgemeinen Objekt über mehrere Stufen eine spezifischere Zusammenstellung von Membern umgesetzt wird.

```cpp
class Fahrzeug {
  public:
    int aktuellePosition[2];    // lat, long Position auf der Erde
    std::string zulassungsnummer;
    bool fuehrerscheinpflichtig
    ...
};

class Automobil: public Fahrzeug {
  public:
    void fahren();
    int zahlderRaeder;
    int sitze;
    ...
};

class Hybrid: public Automobil {
  public:
    void fahreElektrisch();
    ...
};
```

Was bedeutet das für unsere Implementierung von Studenten und Professoren?

```cpp                     Inheritance.cpp
#include <iostream>

class Student {
  public:
    std::string name;
    std::string ort;
    std::string studiengang;

    Student(std::string n, std::string o, std::string sg):
      name{n}, ort{o}, studiengang{sg}
    {};
    void printCertificate(std::ostream& os) {
      os << "Studentendatensatz: " << name << " " << ort << " " << studiengang << "\n";
    }
};

int main()
{
  Student gustav = Student("Zeuner", "Chemnitz", "Mathematik");
  gustav.printCertificate(std::cout);

  //Professor winkler = Professor("Winkler", "Freiberg");
  //winkler.printCertificate(std::cout);
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


Ein weiteres Beispiel greift den Klassiker der Einführung objektorientierter Programmierung auf, den Kanon der Haustiere :-)
Das Beispiel zeigt die Initialisierung der Membervariablen :

+ der Basisklasse beim Aufruf des Konstruktors der erbenden Klasse
+ der Member der erbenden Klasse wie gewohnt

```cpp                     Animals.cpp
#include <iostream>

// Vererbende Klasse Animal
class Animal {
  public:
    Animal():
      name{"Animal"}, weight{0.0}
    {}
    Animal(std::string _name, double _weight):
      name{_name}, weight{_weight}
    {};
    void sleep () {
      std::cout << name << " is sleeping!\n";
    }

    std::string name;
    double weight;
};

// Erbende Klasse Dog - Dog übernimmt die Methoden und Attribute von Animal
class Dog: public Animal {
public:
    Dog(std::string name, double weight, int id):
      Animal(name, weight), id{id}
    {};

    // Dog-spezifische Methoden: bark() und top_speed()
    void bark() {
      std::cout << "woof woof\n";
    }
    double top_speed() {
      if (weight < 40) return 15.5;
      else if (weight < 90) return 17.0;
      else return 16.2;
    }

    int id;
};

int main() {
    Dog dog = Dog("Rufus", 50.0, 2342);
    dog.sleep();
    dog.bark();
    std::cout << dog.top_speed() << "\n";
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Überschreiben von Methoden der Basisklasse (Polymorphie)

Die grundsätzliche Idee bezieht sich auf die Implementierung "eigener" Methoden gleicher Signatur in den abgeleiteten Klassen. Diese implementieren dann das spezifische Verhalten der jeweiligen Objekte.

```cpp                     Inheritance.cpp
#include <iostream>

class Person {
  public:
    std::string name;
    std::string ort;

    Person(std::string n, std::string o):
      name{n}, ort{o}
    {}
    void printData(std::ostream& os) {
      os << "Datensatz: "  << name << " " << ort << "\n";
    }
};

class Student: public Person {
  public:
    std::string studiengang;

    Student(std::string n, std::string o, std::string sg):
      Person(n, o), studiengang{sg}
    {}
    void printData(std::ostream& os) {
      os << "Student Datensatz: "  << name << " " << ort << "\n";
    }
};

class Professor: public Person {
  public:
    int id;

    Professor(std::string n, std::string o, int id):
      Person(n, o), id{id}
    {}
    void printData(std::ostream& os) {
      os << "Prof. Datensatz: "  << name << " " << ort << "\n";
    }
};

int main()
{
  Student *gustav = new Student("Zeuner", "Chemnitz", "Mathematik");
  gustav->printData(std::cout);
  delete gustav;

  Professor *winkler = new Professor("Winkler", "Freiberg", 234234);
  winkler->printData(std::cout);
  delete winkler;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

## Anwendungsbeispiele

Entwerfen Sie eine Klasse, die das Verhalten einer Ampel mit den notwendigen
Zuständen modelliert. Welche Methoden sollten zusätzlich in die Klasse aufgenommen werden?

<div>
  <wokwi-led color="red" pin="13" port="B" label="13"></wokwi-led>
  <wokwi-led color="yellow" pin="12" port="B" label="12"></wokwi-led>
  <wokwi-led color="green" pin="11" port="B" label="11"></wokwi-led>
  <span id="simulation-time"></span>
</div>

```cpp       TrafficLight.cpp
class Ampel {
private:
    int redPin, yellowPin, greenPin;
    int state = 0;

public:
    Ampel(int red, int yellow, int green):
      redPin{red}, yellowPin{yellow}, greenPin{green}
    {
      pinMode(red, OUTPUT);
      pinMode(yellow, OUTPUT);
      pinMode(green, OUTPUT);
    };
    void activateRed() {
      digitalWrite(redPin, HIGH);
    }
    void startOnePeriod(int waitms) {
      digitalWrite(redPin, HIGH);
      delay(waitms);
      digitalWrite(yellowPin, HIGH);
      delay(waitms);
      digitalWrite(redPin, LOW);
      digitalWrite(yellowPin, LOW);
      digitalWrite(greenPin, HIGH);
    }
};

void setup() {
  Ampel trafficLight = Ampel(13, 12, 11);
  trafficLight.activateRed();
  trafficLight.startOnePeriod(1000);
}

void loop() {
  delay(100);
}
```
@AVR8js.sketch

## Allgemeine C++ Anwendungsbeispiele

Nachfolgend sollen einige Anwendungsbeispiele die Möglichkeiten von C++ in Bezug auf Ihre Fachdisziplinen aufzeigen.

+ Messung der Ausbreitung von Schwingungen in Festkörpern
+ Bildanalyse mit OpenCV am Beispiel von Dünnschliffen

> Beide Beispiele finden Sie im Repository unter [Link]()

# Quiz
## Operatorenüberladung

Konzept
---------


> Welches Schlüsselwort wird bei der Operatorüberladung verwendet?
[[operator]]

{{1}}
**************************************************************************
> Für welche Operatoren sollten die Methoden einer Klasse und für welche die globalen Funktionen bevorzugt zum Einsatz kommen?
[[Methode]  [Funktion]]
[(X)        ( )       ] `++`
[( )        (X)       ] `+`
[( )        (X)       ] `*`
[( )        (X)       ] `%`
[(X)        ( )       ] `--`
[(X)        ( )       ] `+=`
**************************************************************************

{{2}}
**************************************************************************
> Wie lautet die Ausgabe dieses Programms? (Hinweise können über das Feld mit der Glühbirne angezeigt werden.)
```cpp
#include<iostream>

class Vektor {
  public:
    int x = 0, y = 0;

    Vektor(int x, int y);

    Vektor operator+(const Vektor& vek_tmp);

    void printVektor() {
      std::cout << x << ", " << y << "\n";
    }
};

Vektor::Vektor(int x, int y):
  x(x), y(y)
{}

Vektor Vektor::operator+(const Vektor& vek_tmp) {
  Vektor vek_loe(0, 0);
  vek_loe.x = this->x + vek_tmp.x;
  vek_loe.y = this->y + vek_tmp.y;
  return vek_loe;
}

int main() {
  Vektor v1(4, 7), v2(10, 9);
  Vektor v3 = v1 + v2;
  v3.printVektor();
}
```
[[14, 16]]
[[?]] In diesem Beispiel sollen zwei Vektoren addiert werden. Im nächsten Tipp steht eine genauere Erklärung der Operatorüberladung anhand dieses Beispiels.
[[?]] `this->x` und `this->y` sind die Datenfelder des Objektes vor dem Operator (in der `main`-Funktion des Vektors `v1`). Der Vektor `v2`, der hinter dem Operator in der `main`-Funktion steht, wird an die Methode übergeben. `vek_tmp.x` und `vek_tmp.x` sind hier die Datenfelder des Vektors `v2`. Der neue Vektor `vek_loe` entsteht infolge der Addition und wird zurückgegeben.
**************************************************************************

Anwendung
---------

> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

class Ort {
  public:
    std::string name;
    std::string bundesland;
    int einwohner;

    Ort(const Ort&);
    Ort(std::string n);
    Ort(std::string n, std::string b, int e);
};

Ort::Ort(std::string n, std::string b, int e):
  name{n}, bundesland{b}, einwohner{e}
{}

std::ostream& operator<<(std::ostream& os, const Ort& ort)
{
  os << ort.name << ", " << ort.bundesland << ", " << ort.einwohner;
  return os;
}

int main()
{
  Ort Freiberg = Ort("Freiberg", "Sachsen" , 41823);
  std::cout << Freiberg << "\n";
}
```
[[Freiberg, Sachsen, 41823]]

## Vererbung

> Erbt die erbende Klasse immer alle Attribute und Methoden der Basisklasse?
[(X)] Ja
[( )] Nein

Implementierung in C++
-----------------

> Wodurch muss `[_____]` ersetzt werden um eine Klasse `Flugzeug` zu definieren, die von der Klasse `Fahrzeug` erbt?
```cpp
#include <iostream>

class Fahrzeug {
  public:
    int aktuellePosition[2];
    std::string Zulassungsnummer;
    bool Fuehrerscheinpflichtig;
};

[_____]{
  public:
    int Flughoehe;
    void fliegen();
};
```
[[class Flugzeug: public Fahrzeug]]
<script>
let input = "@input".trim()

input == "class Flugzeug: public Fahrzeug" || input == "class Flugzeug:public Fahrzeug"
</script>

{{1}}
**************************************************************************
> Kann eine abgeleitete Klasse als Basis-Klasse für eine weitere Klasse verwendet werden?
[(X)] Ja
[( )] Nein
**************************************************************************

{{2}}
**************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```cpp
#include <iostream>

class Fahrzeug {
  public:
    Fahrzeug():
      name{"Fahrzeug"}
    {}
    Fahrzeug(std::string _name):
      name{_name}
    {}
    void defekt() {
      std::cout << name << " muss in die Werkstatt.\n";
    }

    std::string name;
};

class Auto: public Fahrzeug {
  public:
    Auto(std::string name, int ps):
      Fahrzeug(name), ps{ps}
    {};

    int ps = 0;
};

int main() {
  Auto auto1 = Auto("Peters Auto", 100);
  auto1.defekt();
  return 0;
}
```
[[Peters Auto muss in die Werkstatt.]]
**************************************************************************

Vererbungsattribute
-----------------------

> Welche Zugriffspezifizierer sind für die Mitglieder einer Basisklasse zu verwenden damit die folgenden Aussagen zutreffen?
[[`private`]  [`protected`] [`public`]]
[( )          ( )           (X)       ] Zugriff ist aus einer beliebigen Klasse möglich.
[(X)          ( )           ( )       ] Zugriff ist nur innerhalb der Basisklasse möglich.
[( )          (X)           ( )       ] Zugriff ist in der Basisklasse und in erbenden Klassen möglich.

Polymorphie
-----------------------

> Was ist Polymorphie?
[( )] Eine Technik, die es verhindert, bestehende Methoden in den ableiteten Klassen aufzurufen
[(X)] Eine Technik, die es ermöglicht, bestehende Methoden zu überschreiben
[( )] Eine Technik, die es ermöglicht, Datenfelder einer Klasse in den abgeleiteten Klassen zu überschreiben

{{1}}
**************************************************************************
> Welche Aussagen treffen im Bezug auf Polymorphie zu?
[( )] Polymorphie soll beim Erstellen einer abgeleiteten Klasse immer durch Vergabe eines anderen Namens umgangen werden.
[(X)] Polymorphie ermöglicht die Methoden der Basisklase in der abgeleiteten Klasse mit einer anderen Funktionalität zu versehen.
[( )] Polymorphie wird verwendet um die Methoden der Basisklasse zu löschen.
**************************************************************************

{{2}}
**************************************************************************
> Wie lautet die Ausgabe dieses Programms?

```cpp
#include <iostream>

class Basisklasse {
  public:
    void ausgabe() {
      std::cout << "Ausgabe1\n";
    }
};

class Ableitungsklasse : public Basisklasse {
  public:
    void ausgabe() {
      std::cout << "Ausgabe2\n";
    }
};

int main() {
  Basisklasse b = Basisklasse();
  b.ausgabe();

  Ableitungsklasse a = Ableitungsklasse();
  a.ausgabe();
  return 0;
}
```
[[Ausgabe1Ausgabe2]]
**************************************************************************
