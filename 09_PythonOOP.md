<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de & jung@informatik.tu-freiberg.de
version:  1.0.9
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_PythonOOP.md)

# Objektorientierung in Python

| Parameter                | Kursinformationen                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                              |
| **Inhalte:**             | `Objektorientierung in Python`                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_PythonOOP.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_PythonOOP.md) |
| **Autoren**              | @author                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Wie lassen sich die Konzepte der OOP in Python ausdrücken?
* Welche spezifischen Einschränkungen gibt es dabei?

--------------------------------------------------------------------

## Objektorientierung in Python

> Klassen werden verwendet, um benutzerdefinierte Datenstrukturen zu erstellen und definieren Funktionen, sogenannte Methoden, die das Verhalten und die Aktionen identifizieren, die ein aus der Klasse erstelltes Objekt mit seinen Daten ausführen kann.

Eine kurze Auffrischung Ihrer Erinnerungen zur objektorientierter Programmierung in C++ ...

```cpp                     Comparison.cpp
#include <iostream>
#include <cmath>

class Rectangle {
  private:
    float width, height;
  public:
    Rectangle(float w, float h){
        this->width = abs(w);  // ensure non-negative width
        this->height = abs(h);
    }
    float area() {return width*height;}
    Rectangle operator+=(Rectangle offset) {
       float ratio = (offset.area() + this->area()) / this->area();
       this->width = ratio *  this->width;
       return *this;
    }
};

int main () {
  Rectangle rect_a(3,4);
  Rectangle rect_b(1,3);
  std::cout << "Fläche a : " << rect_a.area() << "\n";
  std::cout << "Fläche b : " << rect_b.area() << "\n";
  rect_a += rect_b;
  std::cout << "Summe    : " << rect_a.area();

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

| Zeile | Bedeutung                                                                     |
| ----: | ----------------------------------------------------------------------------- |
|  4-18 | Definition der Klasse `Rectangle` (Schablone für Daten, Methoden, Operatoren) |
|     6 | Gekapselte Daten der Klasse, diese sind "von Außen" nicht sichtbar            |
|     8 | Konstruktor mit Evaluation der übergebenen Parameter                          |
|    12 | Methode über den Daten der Klasse                                             |
|    13 | Individueller Operator `+` mit einer spezifischen Bedeutung                   |
| 21-26 | Generierung von Objekten mittels Konstruktoraufruf und Parameterübergabe, Methoden- und Operatoraufrufe      |

Objektorientierte Programmierung (OOP) ist ein Paradigma, das über die Ideen der Prozeduralen Programmierung hinaus geht. Es definiert Objekte und deren Verhalten. Dabei baut es auf 3 zentralen Grundprinzipien auf:

1. __Kapselung__ Objekte kapseln ihre Daten, Operatoren, Methoden usw. sofern diese nicht als "öffentlich" deklariert sind. 

> _Was intern passiert bleibt intern!_

2. __Vererbung__ Objekte können "Fähigkeiten" an andere, speziellere Objekte weitergeben. 

> _Von wem hat er das denn wohl?_

3. __Polymorphismus__ Objekte werden durch Kapselung und Vererbung  austauschbar! 

> _Was bist denn Du für einer?_

Vorteile der objektorientierten Programmierung

- höhere Wartbarkeit durch Abstraktion 
- Wiederverwendbarkeit von Code (bessere Wiederverwendbarkeit je kleiner und allgemeiner die Objekte gehalten sind)
- schlanker und übersichtlicher Code durch Vererbung

Warum also nicht immer objektorientiert entwickeln?

OOP verführt ggf. dazu, das eigentliche Problem durch einen aufwändigen Entwurf unnötig zu verkomplizieren. Dabei ist die Entwicklung der Gesamtstruktur eines komplexen Softwareprojektes aus n Objekten eine Kunst und braucht viel Übung! Erst, wenn man entsprechende Regeln kennt und sinnvoll anwendet, zeigen sich die Vorteile des Paradigmas.

### ... und in Python?

> **In Python ist alles ein Objekt!**

... z.B. auch Integer und Floats, die in C++ und vielen anderen Programmiersprachen keine Objekte sind

```python
import inspect

i=5

for name, data in inspect.getmembers(i):
    if name == '__builtins__':
        continue
    print(f'{name} - {repr(data)}')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Klassen in Python

Alle Klassendefinitionen beginnen mit dem Schlüsselwort `class`, gefolgt vom Namen der Klasse und einem Doppelpunkt. Jeder Code, der unterhalb der Klassendefinition eingerückt ist, wird als Teil des Klassenhauptteils betrachtet.

Analog zu C++ nutzt Python für die Interaktion mit den Klassenelementen eine _dot notation_.

```python    OOPclass.py
import inspect

class Dog:    # Schlüsselwort "class"
    family = "Canidae"
    name = "Bello"
    age = 5

d = Dog()
print(d.family)
d.name = "Russel"
print(d.name)

for name, data in inspect.getmembers(d):
    if name == '__builtins__':
        continue
    print(f'{name} - {repr(data)}')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


> Aufgabe: Erläutern Sie die Ausgabe folgenden Codes. Wie müssen wir das Ergebnis interpretieren?

```python    OOPclass.py
import inspect

class Dog:  
    family = "Canidae"
    name = "Bello"
    age = 5

d1 = Dog()
print("dog 1:", d1.name, d1.age)
print(d1)
d2 = Dog()
print("dog 2:", d2.name, d2.age)
print(d2)

print(d1 == d2)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

    {{1}}
****************************************************************************
Antworten:

+ d1 und d2 sind Objekte vom Typ "Hund" mit gleichen Attributen (Name, Alter, Familie), aber es handelt sich trotzdem um verschiedene Objekte (deren Daten an verschiedenen Stellen im Speicher liegen)

+ Gleichheit von zwei Objekten der Klasse Hund wird offenbar nicht als
  Gleichheit aller Attribute berechnet. 
  
  + Man könnte Gleichheit von Hunden auch anders definieren (durch Definition
    einer speziellen Methode `__eq__`) 

Zudem fällt auf:
Name und Alter sind für individuelle Hunde üblicherweise verschieden,
die Familie "Canidae" bezieht sich aber auf alle Hunde.
Um dies besser zu modellieren, sollte zwischem Instanzvariablen und Klassenvariablen unterschieden werden ...

****************************************************************************



### OOP Grundelemente in Python


> Frage: Für welche Aufgaben ist der Konstruktor in einer Klasse verantwortlich?

```python    OOPclass.py
class Dog:
    family = "Canidae"     # Klassenvariable 
    def __init__(self, name, age):
        self.name = name   # Instanzvariable
        self.age = age

i = Dog("Rex", 5)
print(i.name, i.family, i.age)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Instanzmethoden sind Funktionen, die innerhalb einer Klasse definiert sind und nur von einer Instanz dieser Klasse aufgerufen werden können. Genau wie bei `__init__()` ist der erste Parameter einer Instanzmethode immer self.

```python    OOPclass.py
class Dog:
    family = "Canidae"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def makeSound(self):     # : nicht vergessen!
        print(f"{self.name} says Wuff")

i = Dog("Rex", 5)
i.makeSound()
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Aufgabe: Schreiben Sie eine Methode, so dass eine Instanz von Dog in Abhängigkeit von ihrem Alter schläft. Recherchieren Sie dazu unter `python delay` die notwendigen Methoden der `time` Klasse.

Wie Sie bereits bei der Inspektion der  `list`, `int` aber auch der `Dog` Klasse gesehen haben, existiert eine Zahl von vordefinierten Funktionen - die sogenannten _dunder Methods_. Das Wort _dunder_ leitet sich von _double underscore_ ab.

| Methode      | Typ                  | implementiert                              |
| ------------ | -------------------- | ------------------------------------------ |
| `__init__()` | Konstruktor          |                                            |
| `__str__()`  | Methode              | Generiert einen String aus den Objektdaten |
| ...          |                      |                                            |
| `__add__()`  | Operator Obj `+` Obj   | Arithmetische Operation                    |
| ...          |                      |                                            |
| `__eq__()`   | Operator  Obj `==` Obj | Logische Operation                         |
| `__lt__()`   | Operator  Obj `<=` Obj |                                            |
| ...          |                      |                                            |

Eine gute Einführung und detailierte Erklärung liefert [Link](https://mathspp.com/blog/pydonts/dunder-methods)

### Kapselung 

Python nutzt zwei führende Unterstriche, um Methoden und Variablen als _private_ zu markieren.

```python    private.py
class A:
	def method_public(self):
		print("This is a public method")

	def __method_private(self):
		print("This is a private method")

obj = A()
obj.method_public()
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Auf private Methoden einer Klasse kann weder außerhalb der Klasse noch von irgendeiner Basisklasse aus zugegriffen werden kann. 

> Wie können wir die private Methode überhaupt aufrufen?

### Vererbung

> Was stört Sie an folgendem Codebeispiel?

```python    RedundantCode.py
class Student:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("Student -", self.firstname, self.lastname)


class StaffMember:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print("Staff -", self.firstname, self.lastname)

humboldt = Student("Alexander", "von Humboldt")
cotta = StaffMember("Bernhard", "von Cotta")

humboldt.printname()
cotta.printname()
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Vererbung überträgt das Verhalten einer Basisklasse auf eine abgeleitete Klasse. Dadurch wird redundanter Code gespart.

```python    Inheritance.py
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  
  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
   pass

class StaffMember(Person):
   pass

humboldt = Student("Alexander", "von Humboldt")
cotta = StaffMember("Bernhard", "von Cotta")

humboldt.printname()
cotta.printname()
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Unterklassen erweitern ihre Oberklasse typischerweise um zusätzliche Attribute und Methoden. Methoden der Unterklasse können Methoden der Oberklasse überschreiben (*Method Overriding*). Im folgenden Beispiel wird dies anhand von zwei *dunder Methoden* gezeigt:

* in der `__init__`-Methode (Konstruktor zur Erzeugung von Instanzen) ist der
  Unterklassen wird jeweils ein weiteres Attribut angelegt. Die Konstruktoren
  der Unterklassen müssen auch den Konstruktor der Oberklasse aufrufen.

* die `__str()__`-Methode liefert eine String-Repräsention des Objekts, die
  inbesonder auch von `print` genutzt wird. Die Implementierung in den Unterklassen rufen hier auch die `__str__`-Methode der Oberklasse auf.  

```python    Inheritance2.py
"Unterklassen mit zusätzlichen Attributen"

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
  
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):
    def __init__(self, fname, lname, id=10000):
        super().__init__(fname, lname)
        self.student_id = id

    def __str__(self):
        return "Student: " + super().__str__() + f", ID: {self.student_id}"

class StaffMember(Person):
    def __init__(self, fname, lname, id=2000):
        super().__init__(fname, lname)
        self.staff_id = id

    def __str__(self):
        return "Staff Member: " + super().__str__() + f", ID: {self.staff_id}"

humboldt = Student("Alexander", "Humboldt")
cotta = StaffMember("Bernhard", "von-Cotta", id=2001)

print(humboldt)
print(cotta)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Instanzvariablen und Klassenvariablen

Die Unterscheidung zwischen Instanzvariablen und Klassenvariablen wurde schon
oben bei der Klasse Dog angesprochen. 

Instanzvariablen (oder *Member Variables*) sind typischerweise für jedes Objekt
unterschiedliche belegt. Beispiele sind etwa der Name von Personen oder Tieren (Alexander, Mary, Fido, ...) oder die Matrikelnummer von Studierenden.

*Klassenvariablen* beziehen dagegen sich auf die Klasse selbst.

+  Der Zugriff auf Klassenvariablen sollte nach dem Schema 
   **Klassenname.Klassenvariable** erfolgen! 

Im folgenden Beispiel wird in der Klasse Student eine Klassenvariable *next\_available\_id* zur automatischen Generierung eindeutiger Martikelnummern
für neue Studierende genutzt.

```python    ClassVariable.py
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
  
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Student(Person):

    next_available_id = 10000

    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.student_id = Student.next_available_id
        Student.next_available_id += 1

    def __str__(self):
        return "Student: " + super().__str__() + f", ID: {self.student_id}"


humboldt = Student("Alexander", "Humboldt")
hegeler = Student("Mary", "Hegeler")

print(humboldt)
print(hegeler)
print("Next available student ID:", Student.next_available_id)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Python und C++ mit Blick auf OOP Konzepte

* Das Konzept der (Methoden-)Überladung wird in Python nicht nativ unterstützt!

  * in C++ kann es in einer Klasse mehrere Methoden gleichen Namens geben,
    sofern sich die Typen der Parameter unterscheiden

  * in Python kann es dagegen nur eine Methode mit demselben Namen geben

  * als Konsequenz werden in Python oft Funktionen mit relativ vielen Parametern
    definiert

    * viele oder oft auch alle Parameter haben Default-Werte, oft `None`

    * zusätzliche Typannotationen der Parameter verbessern die Lesbarkeit

    * der Aufruf der Methoden erfolgt dann flexibel über Schlüsselwort-Argumente
      (d.h. durch explizite Angabe des Parameternames)

```python    Dog.py
class Dog:
    def __init__(self, 
                 name:str | None = None, 
                 age:int | None = None, 
                 breed:str | None = None):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"Dog(Name: {self.name}, Age: {self.age}, Breed: {self.breed})"

# Creating Dog instances with different combinations of arguments
d1 = Dog(name = "Buddy", age=3, breed = "Golden Retriever")
d2 = Dog(age = 5, name = "Max")
d3 = Dog(name = "Bella", breed = "Beagle")
d4 = Dog()

print(d1, d2, d3, d4, sep="\n")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

* Private ist in Python nicht wirklich private

  * direkter Aufruf privater Methoden über ihren eigentlichen Methodennamen resultiert in einem Fehler

  * private Methoden _können_ jedoch mittels "Name Mangling" aufgerufen werden

  * private Methoden _sollte_ man trotzdem nicht von außerhalb der Klasse aufrufen (schlechter Stil)

```python    NameMangling.py
class A:
	def fun(self):
		print("This is a public method.", 
			    "It may call a private method but this is none of your business.")

	def __fun(self):
		print("This is a private method.")

obj = A()
obj.fun()
# obj.__fun()   # <- AttributeError
obj._A__fun()   # <- Name Mangling  "_classname__function"
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### OOP Beispiele

Nehmen wir an, dass wir eine Liste von Vornamen erzeugen wollen. Dabei soll sichergestellt werden, dass diese unabhängig von den Eingaben der Bediener vergleichbar sind. Zudem sollen fehlerhafte Eingaben, die zum Beispiel Zahlen enthalten erkannt und gefiltert werden.

```python    NameList.py
class NameList(list):
  def __init__(self):
    super().__init__()

  def append(self, item):
    if isinstance(item, str) and item.isalpha():
      super().append(item.lower())
    else:
      print(f"Cannot add {item} to name list!",   
            "Expected a string with alphabetic characters only.")

  def uniques(self):
    # return set(self)  # no duplicates, but unordered
    return sorted(set(self))  # no duplicates, ordered

friends = NameList()
friends.append("Jannes")
friends.append("linda")
friends.append("Moritz")
friends.append("MORITZ")
friends.append("Linda2")  # name with digit is not allowed
friends.append(42)   # wrong data type for name lists

print(friends)
print(friends.uniques())
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Dafür schreiben wir eine abgeleitet Listenklasse mit einer eigenen Implementierung von `append()`.

> __Aufgabe__ Erweitern Sie die Implementierung auf die `extend()` Methode der Listen.


---

Zum Vergleich mit dem einführenden C++-Beispiel hier noch eine Python-Implementierung der [Rectangle-Klasse in C++](#2). Der `+=`-Operator wird hier mittels der dunder-Methode `__iadd__()` (in-place addition) implementiert.

```python    Rectangle.py
class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = abs(width)  # ensure non-negative width
        self.height = abs(height)

    def area(self):
        return self.width * self.height

    def __iadd__(self, offset):
        ratio = (offset.area() + self.area()) / self.area()
        self.width = ratio * self.width
        return self

if __name__ == "__main__":
    rect_a = Rectangle(3, 4)
    rect_b = Rectangle(1, 3)
    print(f"Fläche a : {rect_a.area()}")
    print(f"Fläche b : {rect_b.area()}")
    rect_a += rect_b
    print(f"Summe    : {rect_a.area()}")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Dataclasses

Dataclasses, die es seit Python 3.7 gibt, ermöglichen eine einfache und komfortable Definition von Klassen, die hauptsächlich der Datenhaltung dienen, aber deren Verhalten (durch Definition von Methoden) weniger wichtig ist.
Sie sind in etwa vergleichbar zu `struct`s in C++.

Für Dataclasses wird viel "Boilerplate-Code" automatisch generiert, z.B. die Methoden `__init__()`, `__eq__()` und  `__repr__()`. 

Die automatische Code-Generierung erfolgt durch einen *Dekorator* `@dataclass`.

*Felder* von Datenklassen werden über Typannotationen sowie optionalen Default-Werten definiert (man verwendet den Begriff *Feld* auch, weil die Felder
syntaktisch eher wie Klassenvariablen aussehen, durch den Dekorator aber zu Instanzvariablen gemacht werden; durch den anderen Begriff wird es weniger verwirrend).

```python    dataclass_example.py
from dataclasses import dataclass

@dataclass
class Dog:
    name: str | None = None  # field 'name' with default value None
    age: int | None = None 
    breed: str | None = None

d1 = Dog(name = "Buddy", age=3, breed = "Golden Retriever")
d2 = Dog(age = 5, name = "Max")
d3 = Dog(name = "Bella", breed = "Beagle")
d4 = Dog(breed = "Beagle", name = "Bella")
d5 = Dog()

print(d1, d2, d3, d4, d5, sep="\n")
print("Is d3 equal to d4?", d3 == d4)  # True, as the field values are the same
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Hinter den Kulissen erzeugt der Dekorator u.a. automatisch einen Konstruktor:

```
"Automatically generated __init__ method by @dataclass:"
    def __init__(self, 
                 name: str | None = None, 
                 age: int | None = None, 
                 breed: str | None = None):
        self.name = name
        self.age = age
        self.breed = breed
```

Interessant an Dataclasses ist zudem, dass Instanzen entweder als veränderliche (Default) oder unveränderliche Objekte definiert werden können.

+ Erweitert man den Dekorator um den Parameter `frozen=True`, dann sind die
  Instanzen unveränderlich

+ Ein Vorteil von unveränderlichen Objekten ist, dass sie Elemente von Sets
  oder Schlüssel von Dictionaries sein können.


```python    frozen_dataclass.py
from dataclasses import dataclass

@dataclass(frozen=True)  # default: frozen=False
class Dog:
    name: str | None = None  # field 'name' with default value None
    age: int | None = None 
    breed: str | None = None
    
d1 = Dog(name = "Buddy", age=3, breed = "Golden Retriever")
d2 = Dog(name = "Bella", breed = "Beagle")
d3 = Dog(breed = "Beagle", name = "Bella")

dogs = {d1, d2, d3}  # d2 and d3 are considered equal
print(dogs)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> __Aufgabe__ Definieren Sie ein Dictionary, in welchem Instanzen der Dataclass Dog als Schlüssel verwendet werden. Experimentieren Sie dabei mit den beiden möglichen Werten den Parameter `frozen` des Dekorators (False bzw. True).