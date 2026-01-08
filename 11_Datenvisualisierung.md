<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de & jung@informatik.tu-freiberg.de
version:  1.0.8
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_Datenvisualisierung.md)

# Objektorientierung / Visualisierung mit Python

| Parameter                | Kursinformationen                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                              |
| **Inhalte:**             | `Visualisierung mit Python`                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_Datenvisualisierung.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_Datenvisualisierung.md) |
| **Autoren**              | @author                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Wie lassen sich die Konzepte der OOP in Python ausdrücken?
* Welche spezifischen Einschränkungen gibt es dabei?
* Welche Grundkonzepte stehen hinter der Programmierung von Grafiken?
* Wie geht man bei der Erschließung von unbekannten Methoden sinnvoll vor?

---------------------------------------------------------------------

Organisatorisches
========================

+ Wer von Ihnen ist Hörerin oder Hörer der Vorlesung _Einführung in die Informatik_?

+ Bitte bringen Sie sofern möglich Ihre Notebooks zu den Übungen mit. Installieren Sie darauf bereits Python mittels [Anaconda](https://www.anaconda.com/products/distribution).

+ In der letzten Übung wird eine Zusammenfassung der behandelten Inhalte angeboten. Dabei wird insbesondere auf die Objektorientierung unter C++ eingegangen.

## Objektorientierung in Python

> Klassen werden verwendet, um benutzerdefinierte Datenstrukturen zu erstellen und definieren Funktionen, sogenannte Methoden, die das Verhalten und die Aktionen identifizieren, die ein aus der Klasse erstelltes Objekt mit seinen Daten ausführen kann.

Eine kurze Auffrischung Ihrer Erinnerungen zur objektorientierter Programmierung in C++ ...

```cpp                     Comparison.cpp
#include <iostream>

class Rectangle {
  private:
    float width, height;
  public:
    Rectangle(int w, int h){
        if ((w > 0) & (h > 0)) {
                this->width = w;
                this->height = h;
        }else{
                this->width = w;
                this->height = h;
        }
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
|  3-22 | Definition der Klasse `Rectangle` (Schablone für Daten, Methoden, Operatoren) |
|     5 | Gekapselte Daten der Klasse, diese sind "von Außen" nicht sichtbar            |
|     7 | Konstruktor mit Evaluation der übergebenen Parameter                          |
|    16 | Methode über den Daten der Klasse                                             |
|    17 | Individueller Operator `+` mit einer spezifischen Bedeutung                   |
| 25-28 | Generierung von Objekten mittels Konstruktoraufruf und Parameterübergabe      |

Objektorientierte Programmierung (OOP) ist ein Paradigma, das über die Ideen der Prozeduralen Programmierung hinaus geht. Es definiert Objekte und deren Verhalten. Dabei baut es auf 3 zentralen Grundprinzipien auf:

1. __Kapselung__ Objekte kapseln ihre Daten, Operatoren, Methoden usw. sofern diese nicht als "öffentlich" deklariert sind. 

> _Was intern passiert bleibt intern!_

2. __Vererbung__ Objekte können "Fähigkeiten" an andere, speziellere Objekte weitergeben. 

> _Von wem hat er das denn wohl?_

3. __Polymorphismus__ Objekte werden durch Kapselung und Vererbung  austauschbar! 

> _Was bist denn Du für einer?_

Vorteile der objektorientierten Programmierung

- höhere Wartbarkeit durch Abstraktion 
- Wiederverwendbarkeit von Code (je mehr desto kleiner und allgemeiner die Objekte gehalten sind)
- schlanker und übersichtlicher Code durch Vererbung

Warum also nicht immer objektorientiert entwickeln?

OOP verführt ggf. dazu, das eigentliche Problem durch eine aufwändigen Entwurf unnötig zu verkomplizieren. Dabei ist die Entwicklung der Gesamtstruktur eines komplexen Softwareprojektes aus n Objekten eine Kunst und braucht viel Übung! Erst, wenn man entsprechende Regeln kennt und sinnvoll anwendet, zeigen sich die Vorteile des Paradigmas.

### ... und in Python?

> **In Python ist alles ein Objekt!**

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

i = Dog()
print(i.family)
i.name = "Russel"
print(i.name)

for name, data in inspect.getmembers(i):
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

i = Dog()
print(i)
j = Dog()
print(j)

print(i == j)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### OOP Grundelemente in Python

> Frage: Für welche Aufgaben ist der Konstruktor in einer Klasse verantwortlich?

```python    OOPclass.py
class Dog:
    family = "Canidae"
    def __init__(self, name, age):
        self.name = name
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

Wie Sie bereits bei der Inspektion der  `list`, `int` aber auch der `Dog` Klassen gesehen haben, existiert eine Zahl von vordefinierten Funktionen - die sogenannten _dunder Methods_. Das Wort _dunder_ leitet sich von _double underscore_ ab.

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

### Python und C++ mit Blick auf OOP Konzepte

* Das Konzept der (Methoden-)Überladung wird in Python nicht nativ unterstützt!

  * in C++ kann es in einer Klasse mehrere Methoden gleichen Namens geben,
    sofern sich die Typen der Parameter unterscheiden

  * in Python kann es dagegen nur eine Methode mit demselben Namen geben

  * als Konsequenz müssen in Python oft Typ-Überprüfungen der Argumente
    durchgeführt werden, z.B. mit der builtin-Funktion `isinstance`

```python    OOPclass.py
class Dog:  
  family = "Canidae"
  def __init__(self, *args):
    if len(args)>0:
      if isinstance(args[0], str):
        self.name = args[0]
      else:
        print("Der Datentyp passt nicht für die Variable Name!")
    else:
      self.name = "-"

i = Dog()
print(i.name, i.family)
j = Dog("Fido")
print(j.name, j.family)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

* Private ist in Python nicht wirklich private

  * direkter Aufruf privater Methoden über ihren eigentlichen Methodennamen resultiert in einem Fehler

  * private Methoden _können_ jedoch mittels "Name Mangling" aufgerufen werden

  * private Methoden _sollte_ man trotzdem nicht direkt aufrufen (schlechter Stil)

```python    NameMangling.py
class A:
	def fun(self):
		print("This is a public method")

	def __fun(self):
		print("This is a private method")

obj = A()
obj.fun()
# obj.__fun()   # <- AttributeError
obj._A__fun()   # <- Name Mangling  "_classname__function"
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### OOP Beispiel

Nehmen wir an, dass wir eine Liste von Vornamen erzeugen wollen. Dabei soll sichergestellt werden, dass diese unabhängig von den Eingaben der Bediener vergleichbar sind. Zudem sollen fehlerhafte Eingaben, die zum Beispiel Zahlen enthalten erkannt und gefiltert werden.

```python    newListClass.py
class NameList(list):
  def __init__(self):
    super().__init__()

  def append(self, item):
    if isinstance(item, str):
      super().append(item.lower())
    else:
      print(f"Cannot add {item} to name list! Expected a string.")

  def uniques(self):
    # return set(self)  # no duplicates, but unordered
    return sorted(set(self))  # no duplicates, ordered

friends = NameList()
friends.append("Jannes")
friends.append("linda")
friends.append("Moritz")
friends.append("MORITZ")
friends.append("Linda2")  
friends.append(42)   # wrong data type for name lists

print(friends)
print(friends.uniques())
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Dafür schreiben wir eine abgeleitet Listenklasse mit einer eigenen Implementierung von `append()`.

> __Aufgabe__ Erweitern Sie die Implementierung auf die `extend()` Methode der Listen.

## Datenvisualisierung

In der vergangenen Woche haben wir Ihre Zugehörigkeit zu verschiedenen Studiengängen eingelesen und analysiert [Link L09](https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/master/09_PythonVertiefung.md#6).

Auf die Frage hin, welche Häufigkeiten dabei auftraten, beantwortete unser Skript mit einem Dictonary:

```bash
{'S-UWE': 1, 'S-WIW': 18, 'S-GÖ': 9, 'S-VT': 2, 'S-BAF': 3, 'S-WWT': 8, 'S-NT': 4, 
 'S-ET': 3, 'S-MB': 1, 'S-FWK': 3, 'F1-INF': 2, 'S-BWL': 2, 'S-MAG': 4, 'F2-ANCH': 3, 
 'S-ACW': 4, 'S-GTB': 4, 'S-GBG': 5, 'S-GM': 2, 'S-ERW': 1, 'S-INA': 1, 'S-MORE': 1,
  'S-CH': 1}
```

<!--
data-title="Teilnehmende Studierende pro Studiengang"
data-show
-->
| Studiengang | Anzahl |
| ----------- | ------ |
| 'S-UWE'     | 1      |
| 'S-WIW'     | 18     |
| 'S-GÖ'      | 9      |
| 'S-VT'      | 2      |
| 'S-BAF'     | 3      |
| 'S-WWT'     | 8      |
| 'S-NT'      | 4      |
| 'S-ET'      | 3      |
| 'S-MB'      | 1      |
| 'S-FWK'     | 3      |
| 'F1-INF'    | 2      |
| 'S-BWL'     | 2      |
| 'S-MAG'     | 4      |
| 'F2-ANCH'   | 3      |
| 'S-ACW'     | 4      |
| 'S-GTB'     | 4      |
| 'S-GBG'     | 5      |
| 'S-GM'      | 2      |
| 'S-ERW'     | 1      |
| 'S-INA'     | 1      |
| 'S-MORE'    | 1      |
| 'S-CH'      | 1      |


Die textbasierte Ausgabe ist nur gering geeignet, um einen raschen Überblick zu erlangen. Entsprechend suchen wir nach einer grafischen Ausgabemöglichkeit für unsere Python Skripte.

### Python Visualisierungstools

Python stellt eine Vielzahl von Paketen für die Visualisierung von Dateninhalten bereit. Diese zielen auf unterschiedliche Visionen oder Features:

+ einfache Verwendbarkeit
+ große Bandbreite von Diagrammarten und Adaptionsmöglichkeiten
+ interaktive Diagramme 
+ Vielzahl von Exportschnittstellen

| Package    | Link                                | Besonderheiten                                             |
| ---------- | ----------------------------------- | ---------------------------------------------------------- |
| plotly     | [Link](https://plotly.com/)         | Fokus auf interaktive Diagramme eingebettetet in Webseiten |
| seaborn    | [Link](https://seaborn.pydata.org/) | Leistungsfähige Darstellung von statistischen Daten         |
| matplotlib | [Link](https://matplotlib.org/)     |                                                            |
| ...        |                                     |                                                            |

### Matplotlib Grundlagen

```python      Beispiel.py
import matplotlib.pyplot as plt

a = [5,6,7,9,12]
b =[x**2 for x in a]   # List Comprehension
plt.plot(a, b)

#plt.show()  
plt.savefig('foo.png') # notwendig für die Ausgabe in LiaScript
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

| Anpassung                      | API                                                                                      |                                                   |
| ------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Linientyp der Datendarstellung | [pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)     | `plt.plot(a, b, 'ro:')`                           |
| Achsenlabel hinzufügen         | [pyplot.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) | `plt.xlabel('my data', fontsize=14, color='red')` |
| Titel einfügen                 |  [pyplot.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)                                                                                       | `plt.title(r'$\sigma_i=15$')`                     |
| Gitter einfügen                |  [pyplot.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)                                                                                        | `plt.grid()`                                      |
| Legende                        |  [pyplot.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)                                                                                        | `plt.plot(a, b, 'ro:', label="Data")`             |
|                                |                                                                                          | `plt.legend()`                                    |
| Speichern                      |  [pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)                                                                                        | `plt.savefig('foo.png') `                         |

![Matplot](images/10_Datenvisualisierung/UbersichtGrafiken.png "Tutorial von Rizky Maulana Nurhidayat auf [medium](https://towardsdatascience.com/visualizations-with-matplotlib-part-1-c9651008b6b8) ")

Weiter Tutorials sind zum Beispiel unter 

!?[MatplotlibTutorial](https://www.youtube.com/watch?v=UO98lJQ3QGI)


### Matplotlib Beispiele

```python      MultipleDiagrams.py
import numpy as np
import matplotlib.pyplot as plt

N = 21
x = np.linspace(0, 10, 11)
y = [3.9, 4.4, 10.8, 10.3, 11.2, 13.1, 14.1,  9.9, 13.9, 15.1, 12.5]

# fit a linear curve an estimate its y-values and their error.
a, b = np.polyfit(x, y, deg=1)
y_est = a * x + b
y_err = x.std() * np.sqrt(1/len(x) +
                          (x - x.mean())**2 / np.sum((x - x.mean())**2))

fig, ax = plt.subplots()
ax.plot(x, y_est, '-')
ax.fill_between(x, y_est - y_err, y_est + y_err, alpha=0.2)
ax.plot(x, y, 'o', color='tab:brown')

#plt.show()  
plt.savefig('foo.png') # notwendig für die Ausgabe in LiaScript
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


```python      MultipleDiagrams.py
import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure()
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
#plt.show()  
plt.savefig('foo.png') # notwendig für die Ausgabe in LiaScript
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


## Beispiel der Woche

```python      Beispiel.py
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq

# Number of sample points
N = 600
# sample spacing
T = 1.0 / 800.0
x = np.linspace(0.0, N*T, N, endpoint=False)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = fftfreq(N, T)[:N//2]

fig, axs = plt.subplots(2, 1)
axs[0].plot(x, y)
axs[1].plot(xf, 2.0/N * np.abs(yf[0:N//2]))
plt.grid()

#plt.show()
plt.savefig('foo.png')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

# Quiz
## Objektorientierung in Python

> Für welche der genannten Grundprinzipien der objektorientierten Programmierung treffen folgende Aussagen zu:

[[Kapselung]  [Vererbung] [Polymorphie] ]
[( )          ( )         (X)           ] Welche konkrete Implementierung der Methode aufgerufen wird, hängt davon ab mit welchem konkreten Objekt sie aufrufen wird.
[(X)          ( )         ( )           ] Objekte schützen ihre Daten und Methoden sofern diese nicht als "öffentlich" deklariert sind.
[( )          (X)         ( )           ] Objekte können ihre Daten und Methoden an andere, spezielle Objekte weitergeben.

### Klassen in Python
> Mit welchem Schlüsselwort beginnen Klassendefinitionen in Python?
[[class]]

{{1}}
********************************************************************
> Wodurch muss `[_____]` ersetzt werden, um den Nachnamen von Student `neuer` auszugeben?
```python
class Student:
    lastName = "Neuer"
    firstName = "Markus"
    age = 20

neuer = Student()
print([_____])
```
[[neuer.lastName]]
********************************************************************

### OOP Grundelemente in Python
> Wie lauten die Ausgaben foldender Programme?
```python
class Player:
    health = 100
    exp = 10

    def __init__(self, name, level):
        self.name = name
        self.level = level


p1 = Player("Peter", 2)
p2 = Player("Frank", 6)
print(p2.level, p2.exp)
```
[[6 10]]

{{1}}
********************************************************************
```python
class Player:
    health = 100
    exp = 10

    def __init__(self, name, level):
        self.name = name
        self.level = level

    def level_up(self):
        self.level += 1
        self.exp = 0


p1 = Player("Peter", 2)
p2 = Player("Frank", 6)
p2.level_up()
print(p2.level, p2.exp)
```
[[7 0]]
********************************************************************

{{2}}
********************************************************************
> Welche dieser Methoden ist eine *dunder Method*?

[(X)] `__sum__`
[( )] `sum`
[( )] `_sum`
[( )] `_sum_`
********************************************************************

### Kapselung
> Welche der im folgenden Code aufgeführten Methoden und Variablen sind öffentlich und welche privat?
```python
class Dog:
  def bark(self):
      print("woof")

  def __bark_loud(self):
    print("WOOF!")

Fifi = Dog()
Fifi.bark_loud()
```
[[`bark()`] [`__bark_loud()`] ]
[(X)      ( )             ] öffentlich
[( )      (X)             ] privat

{{1}}
********************************************************************
> Was ist die Ausgabe des oben gezeigten Codes?
[( )] woof
[( )] WOOF!
[(X)] Das Programm wird mit einem Error abgebrochen
********************************************************************

{{2}}
********************************************************************
> Ist es in Python grundsätzlich möglich auch private Methoden auszuführen?
[(X)] Ja
[( )] Nein

> Wordurch muss `[_____]` ersetzt werden, um die Methode `__bark_loud()` auszuführen?
```python
class Dog:
  def bark(self):
      print("woof")

  def __bark_loud(self):
    print("WOOF!")

Fifi = Dog()
Fifi.[_____]
```
[[_Dog__bark_loud()]]
********************************************************************

### Vererbung
> Wodurch muss `[_____]` ersetzt werden, um eine neue Klasse `Auto` zu erstellen, die das Verhalten der Klasse `Fahrzeug` erbt?
```python
class Fahrzeug:
  def __init__(self, ps):
    self.ps = ps

class [_____]:
   pass

a1 = Auto(70)
```
[[Auto(Fahrzeug)]]

## Datenvisualisierung
### Matplotlib Grundlagen
> Wodurch muss `[_____]` ersetzt werden, um einen plot mit dem Jahr auf der X-Achse und der Anzahl der Tassen Tee auf der Y-Achse zu erstellen?
```python
import matplotlib.pyplot as plt

year = [2000, 2001, 2002, 2003, 2004]
ttg =[232, 533, 433, 410, 450] # Tassen Tee getrunken
plt.[_____]

plt.show()
```
[[plot(year, ttg)]]
<script>
let input = "@input".trim().toLowerCase()

input == "plot(year, ttg)" || input == "plot(year,ttg)"
</script>
