<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md

-->

# Operatoren und Vererbung

Die interaktive Version des Kurses ist unter diesem [Link](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/10_Vererbung.md#1) zu finden.

**Wie weit waren wir gekommen?**

```text @plantUML.png
@startuml
ditaa

+-------------------------------------+  +-------------------------------------+
| API Implementierung des Herstellers |  | Eigene Klassenimplementierungen     |
| * Led-Klasse                        |  | * Filter-Klasse                     |
| * Drucksensor-Klasse                |  | * System-Monitor-Klasse             |
| * Serial-Klasse                     |  | * ....                              |
| * ....                        cCCB  |  | * ....                      cBFB    |
+-------------------------------------+  +-------------------------------------+
               |                                            |
               |                                            |
               +-----------------------+--------------------+
                                       |
                                       v
                   +-------------------------------------+
                   | // Mein Programm                    |
                   | void setup{                         |
                   |   RGB_LED rgbLed(red, green, blue); |
                   | }                                   |
                   |                                     |
                   | void setup{                         |
                   |   rgbLed.setColor(255, 0, 0);       |
                   | }                      {d}cBFB      |
                   +-------------------------------------+                      
```

Für die Implementierung einer Ausgabe auf dem Display des MXCHIP Boards nutzen wir die Klassenimplementierung der API.

[Link](https://microsoft.github.io/azure-iot-developer-kit/docs/apis/display/)


**Inhalt der heutigen Veranstaltung**

* Vertiefung der Anwendung objektorientierter Konzepte
* Definition klassenspezifischer Operatoren
* Einführung der Vererbung

**Fragen an die heutige Veranstaltung ...**

*

## Operatorüberladung
Motivation
-------------------

Folgendes Beispiel illustriert den erreichten Status unserer C++ Implementierungen. Unsere Klasse `Student` besteht aus:

+ 3 Membervariablen (Zeile 5-7)
+ 3 Konstruktoren (Zeile 9-11)
+ 1 Memeberfunktion (Zeile 13)

Alle sind als `public` markiert.

```cpp                     Comparison.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(const Student&);
    Student(std::string n);
    Student(std::string n, int a, std::string o);

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode
};

Student::Student(std::string n): name{n}, alter{18}, ort{"Freiberg"}{}

Student::Student(std::string n, int a, std::string o): name{n}, alter{a}, ort{o} {}

Student::Student(const Student& other){
  this->name = other.name;
  this->alter = other.alter;
  this->ort = other.ort;
}

void Student::ausgabeMethode(std::ostream& os){
    os << name << " " << ort << " " << alter << "\n";
}

int main()
{
  //Student gustav {"Zeuner", 27, "Chemnitz"};
  Student gustav = Student("Zeuner", 27, "Chemnitz");
  //Student gustav("Zeuner", 27, "Chemnitz");
  gustav.ausgabeMethode(std::cout);

  Student bernhard {"Cotta", 18, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student NochMalBernhard = Student(gustav);
  bernhard.ausgabeMethode(std::cout);
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

> **Aufgabe:** Schreiben Sie
>
>   + eine Funktion `int vergleich(Student, Student)` und
>
>   + eine Methode `int Student::vergleich(Student, Student)`,
> die zwei Studenten miteinander vergleicht!


{{1}}
> Was ist der Nachteil unserer Lösung?

### Konzept

Das Überladen von Operatoren erlaubt die flexible klassenspezifische Nutzung von
Arithmetischen- und Vergleichs-Symbolen wie  \+, \-, \*, \/, =. Damit kann deren Bedeutung für
selbstdefinierter Klassen (fast) mit einer neuen Bedeutung versehen werden. Ausnahmen bilden   spezieller Operatoren, die nicht überladen werden dürfen (  ?: ,  :: ,  . ,  .* , typeid , sizeof und die Cast-Operatoren).

```
Matrix a, b;
Matrix c = a + b;    \\ hier wird mit dem Plus eine Matrixoperation ausgeführt

String a, b;
String c = a + b;    \\ hier werden mit dem Plus zwei Strings konkateniert
```

Operatorüberladung ist Funktionsüberladung, wobei die Funktionen durch eine spezielle Namensgebung gekennzeichnet sind. Diese beginnen mit dem Schlüsselwort `operator`, das von dem Token für den jeweiligen Operator gefolgt wird.

```cpp
class Matrix{
  public:
    Matrix operator+(Matrix zweiterOperand){ ... }
    Matrix operator/(Matrix zweiterOperand){ ... }
    Matrix operator*(Matrix zweiterOperand){ ... }
}

class String{
  public:
    String operator+(String zweiterString){ ... }
}
```

Operatoren können entweder als Methoden der Klasse oder als globale Funktionen zu überladen werden. Die Methodenbeispiele sind zuvor dargestellt, analoge Funktionen ergeben sich zu:

```cpp
class Matrix{
  public:
    ...
}

Matrix operator+(Matrix ersterOperand, Matrix zweiterOperand){ ... }
Matrix operator/(Matrix ersterOperand, Matrix zweiterOperand){ ... }
Matrix operator*(Matrix ersterOperand, Matrix zweiterOperand){ ... }
```

> **Merke:** Funktion oder Methode - welche Version sollte wann zum Einsatz kommen? Einstellige Operatoren `++` sollten Sie als Methode, zweistellige Operatoren ohne Manipulation der Operanden als Funktion implementieren. Für zweistellige Operatoren, die einen der Operanden verändern (`+=`), sollte als Methode realsiert werden.

Als Bespiel betrachten wir eine Klasse Rechteck und implementieren zwei Operatorüberladungen:

+ eine Vergleichsoperation
+ eine Additionsoperation die `A = A + B` oder abgekürzt `A+=B`

implementiert.

```cpp                     Comparison.cpp
#include <iostream>

class Rectangle {
  private:
    float width, height;
  public:
    Rectangle(int w, int h): width{w}, height{h} {}
    float area() {return width*height;}
    Rectangle operator+=(Rectangle offset) {
       float ratio = (offset.area() + this->area()) / this->area();
       this->width = ratio *  this->width;
       return *this;
    }
};

bool operator>(Rectangle a, Rectangle b){
    if (a.area() > b.area()) return 1;
    else return 0;
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
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

> **Merke:** Üblicherweise werden die Operanden bei der Operatorüberladung als Referenzen übergeben. Damit wird eine Kopie vermieden. In Kombination mit dem Schlüsselwort `const` kann dem Compiler angezeigt werden. dass keine Veränderung an den Daten vorgenommen wird. Sie müssen also nicht gespeichert werden.

```
bool operator>(const Rectangle& a, const Rectangle& b){
    if (a.area() > b.area()) return 1;
    else return 0;
}
```

Stellen wir die Abläufe nochmals grafisch dar:

+ Aufruf über Call-by-Value [Pythontutor](http://pythontutor.com/visualize.html#code=%23include%20%3Ciostream%3E%0A%0Aclass%20Rectangle%20%7B%0A%20%20private%3A%0A%20%20%20%20float%20width,%20height%3B%0A%20%20public%3A%0A%20%20%20%20Rectangle%28int%20w,%20int%20h%29%3A%20width%7Bw%7D,%20height%7Bh%7D%20%7B%7D%0A%20%20%20%20float%20area%28%29%20%7Breturn%20width*height%3B%7D%0A%20%20%20%20Rectangle%20operator%2B%3D%28Rectangle%20offset%29%20%7B%0A%20%20%20%20%20%20%20float%20ratio%20%3D%20%28offset.area%28%29%20%2B%20this-%3Earea%28%29%29%20/%20this-%3Earea%28%29%3B%0A%20%20%20%20%20%20%20this-%3Ewidth%20%3D%20ratio%20*%20%20this-%3Ewidth%3B%0A%20%20%20%20%20%20%20return%20*this%3B%0A%20%20%20%20%7D%0A%7D%3B%0A%0Abool%20operator%3E%28Rectangle%20a,%20Rectangle%20b%29%7B%0A%20%20%20%20if%20%28a.area%28%29%20%3E%20b.area%28%29%29%20return%201%3B%0A%20%20%20%20else%20return%200%3B%0A%7D%0A%0Aint%20main%20%28%29%20%7B%0A%20%20Rectangle%20rect_a%283,4%29%3B%0A%20%20Rectangle%20rect_b%285,7%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Vergleich%3A%20%22%20%3C%3C%20%28rect_a%20%3E%20rect_b%29%20%3C%3C%20%22%5Cn%22%3B%0A%0A%20%20std%3A%3Acout%20%3C%3C%20%22Fl%C3%A4che%20a%20%3A%20%22%20%3C%3C%20rect_a.area%28%29%20%3C%3C%20%22%5Cn%22%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Fl%C3%A4che%20b%20%3A%20%22%20%3C%3C%20rect_b.area%28%29%20%3C%3C%20%22%5Cn%22%3B%0A%20%20rect_a%20%2B%3D%20rect_b%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Summe%20%20%20%20%3A%20%22%20%3C%3C%20rect_a.area%28%29%3B%0A%0A%20%20return%200%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D&textReferences=false)
+ Aufruf über Referenz [Pythontutor](http://pythontutor.com/visualize.html#code=%23include%20%3Ciostream%3E%0A%0Aclass%20Rectangle%20%7B%0A%20%20private%3A%0A%20%20%20%20float%20width,%20height%3B%0A%20%20public%3A%0A%20%20%20%20Rectangle%28int%20w,%20int%20h%29%3A%20width%7Bw%7D,%20height%7Bh%7D%20%7B%7D%0A%20%20%20%20float%20area%28%29%20%7Breturn%20width*height%3B%7D%0A%7D%3B%0A%0Abool%20operator%3E%28Rectangle%26%20a,%20Rectangle%26%20b%29%7B%0A%20%20%20%20if%20%28a.area%28%29%20%3E%20b.area%28%29%29%20return%201%3B%0A%20%20%20%20else%20return%200%3B%0A%7D%0A%0Aint%20main%20%28%29%20%7B%0A%20%20Rectangle%20rect_a%283,4%29%3B%0A%20%20Rectangle%20rect_b%285,7%29%3B%0A%20%20std%3A%3Acout%20%3C%3C%20%22Vergleich%3A%20%22%20%3C%3C%20%28rect_a%20%3E%20rect_b%29%20%3C%3C%20%22%5Cn%22%3B%0A%0A%20%20return%200%3B%0A%7D&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=cpp&rawInputLstJSON=%5B%5D&textReferences=false)

### Anwendung

Im folgenden Beispiel wird der Vergleichsoperator `==` überladen. Dabei sehen
wir den Abgleich des Namens und des Alters als ausreichend an.

```cpp                     Comparison.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(const Student&);
    Student(std::string n);
    Student(std::string n, int a, std::string o);

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode

    bool operator==(const Student&);
};

Student::Student(const Student& other){
  this->name = other.name;
  this->alter = other.alter;
  this->ort = other.ort;
}

Student::Student(std::string n): name{n}, alter{18}, ort{"Freiberg"}{}

Student::Student(std::string n, int a, std::string o): name{n}, alter{a}, ort{o} {}

void Student::ausgabeMethode(std::ostream& os){
    os << name << " " << ort << " " << alter << "\n";
}

bool Student::operator==(const Student& other){
  if ((this->name == other.name) && (this->alter == other.alter)){
    return true;
  }else{
    return false;
  }
}

int main()
{
  //Student gustav {"Zeuner", 27, "Chemnitz"};
  Student gustav = Student("Zeuner", 27, "Chemnitz");
  //Student gustav("Zeuner", 27, "Chemnitz");
  gustav.ausgabeMethode(std::cout);

  Student bernhard {"Cotta", 18, "Zillbach"};
  bernhard.ausgabeMethode(std::cout);

  Student NochMalBernhard = Student(bernhard);
  NochMalBernhard.ausgabeMethode(std::cout);

  if (bernhard == NochMalBernhard){
    std::cout << "Identische Studenten \n";
  }else{
    std::cout << "Ungleiche Identitäten \n";
  }
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Eine besondere Form der Operatorüberladung ist der `<<`, mit dem die Ausgabe auf ein Streamobjekt realsiert werden kann.

```cpp                     Comparison.cpp
#include <iostream>

class Student{
  public:
    std::string name;
    int alter;
    std::string ort;

    Student(const Student&);
    Student(std::string n);
    Student(std::string n, int a, std::string o);

    void ausgabeMethode(std::ostream& os); // Deklaration der Methode

    bool operator==(const Student&);
};

Student::Student(std::string n, int a, std::string o): name{n}, alter{a}, ort{o} {}

std::ostream& operator<<(std::ostream& os, const Student& student)
{
    os << student.name << '/' << student.alter << '/' << student.ort;
    return os;
}

int main()
{
  Student gustav = Student("Zeuner", 27, "Chemnitz");
  std::cout << gustav;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Eine umfangreiche Diskussion zur Operatorüberladung finden Sie unter https://www.c-plusplus.net/forum/topic/232010/%C3%BCberladung-von-operatoren-in-c-teil-1/2

## Vererbung
