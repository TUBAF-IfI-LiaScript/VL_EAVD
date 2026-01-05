<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de & junginformatik.tu-freiberg.de 
version:  1.0.5
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/08_PythonVertiefung.md)

# Vertiefung der Python Konzepte

| Parameter                | Kursinformationen                                                                                                                                                      |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                        |
| **Semester**             | @config.semester                                                                                                                                                       |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                      |
| **Inhalte:**             | `Erweiterte Konzepte der Programmiersprache Python`                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/09_PythonVertiefung.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/08_PythonVertiefung.md) |
| **Autoren**              | @author                                                                                                                                                                |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------


**Fragen an die heutige Veranstaltung ...**

+ Welche Standarddatentypen exisiteren in Python über die Liste hinaus?
+ In welchen Anwendungsfällen kommen diese zum Einsatz?
+ Wie lassen sich Funktionen mit Python realsieren und welche Unterschiede existieren im Vergleich zu C++?

---------------------------------------------------------------------

## Weitere Datentypen 

Sie haben bereits Listen (`list`), `range` Objekte und Text (`string`) als Datenstruktur kennengelernt - im Weiteren existieren daneben vier weitere Sequenzdatentypen: byte sequences (`bytes` objects), byte arrays (`bytearray` objects) und `tuples`.
Dazu kommen `dictionaries` und `sets` als Containertypen. 

| Datentyp    | Besonderheit                                    | Syntax                  |
|-------------|-------------------------------------------------|-------------------------|
| `list`      | *veränderbare* Sequenz von (beliebigen) Daten | `l = ["grün", 1, True]` |
|             |                                                 | `l[0] = 4` `l.append(1)`      |
| `strings`   | Darstellung von Zeichenketten, unveränderbar    | `s = "Universität"`       |
| `bytes`     | Unveränderbare Folge von ASCII-Zeichen              | `b = b"Universitaet"`        |
| `bytearray` | Unveränderbare Folge von Bytes (Integer 0...255)              | `b_array = bytearray([0, 1, 255])`        |
| `tupel`     | Unveränderbare Folge von Elementen              | `t1 = (1, 2, 3)`        |
| `range`     | iterierbare, unveränderbare Folge von Elementen | `r = range(3, 20, 2)`   |

### Tupel oder Liste?

+ Listen sind veränderbar, d.h. Elemente können hinzugefügt, gelöscht oder modifiziert werden.

+ Tupel sind dagegen unveränderbar.


Warum ein Tupel anstelle einer Liste verwenden?

+ Die Programmausführung ist beim Iterieren eines Tupels etwas schneller als bei der entsprechenden Liste - Dies wird wahrscheinlich nicht auffallen, wenn die Liste oder das Tupel klein ist.

+ Der Speicherbedarf eines Tupels fällt etwas in der Regel geringer aus, als bei einer Listendarstellung ein und des selben Inhaltes

  + weil die zusätzlichen Möglichkeiten zur Veränderung von Listen etwas zusätzlichen Speicherbedarf zur Verwealtung erfordern.

+ Manchmal sollen Daten unveränderlich gehalten werden - Tupel schützen die Informationen vor versehentlichen Änderungen.

```python  size.py
import sys

a_list = []
a_tuple = ()
a_list = ["Hello", "TU", "Freiberg"]
a_tuple = ("Hello", "TU", "Freiberg")
print("List data size : " + str(sys.getsizeof(a_list)))
print("Tupel data size: " + str(sys.getsizeof(a_tuple)))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

```python  duration.py
import time

l=list(range(1_000_000))
t=tuple(range(1_000_000))

start = time.perf_counter()
for item in l:
    a = item
end = time.perf_counter()
print("List duration:  ", end - start, "s")

start = time.perf_counter()
for item in t:
    a = item
end = time.perf_counter()
print("Tuple duration: ", end - start, "s")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Dictionaries

                            {{0-1}}
********************************************************************

Dictionaries werden zur Speicherung von Schlüssel Werte Paaren genutzt. Ein dictionary ist eine Sammlung von geordneten (entsprechend der Reihenfolge der "Einlagerung"), veränderlichen Einträgen, für die Schlüssel werden keine Duplikate zugelassen.

> Ein Telefonbuch ist das traditionelle Beispiel für eine Implementierung des Dictonaries. Anhand der Namen werden die Telefonnummern zugeordnet.

<!--style="width: 70%;"-->
```ascii
   
 Listen: Zugriff auf Elemente über Index       Dictonary: Zugriff auf Elemente über Schlüssel

 Index                                        Schlüssel
 +---------------+     +---------+            +---------------+     +---------+
 |       0       |---->| `Hello` |            | `erstes Wort` |---->| `Hello` |
 +---------------+     +---------+            +---------------+     +---------+

 +---------------+     +---------+            +---------------+     +---------+
 |       1       |---->| `World` |            | `zweites Wort`|---->| `World` |
 +---------------+     +---------+            +---------------+     +---------+

 +---------------+     +---------+            +---------------+     +---------+  
 |       2       |---->| ...     |            | `drittes Wort`|---->| ...     |
 +---------------+     +---------+            +---------------+     +---------+

       ....                                        ....
```

********************************************************************

                            {{1-2}}
********************************************************************

```python  dictonary.py
capitals = {"France": "Paris",
            "Italy": "Rome",
            "UK": "London"}

print(capitals)

print("UK" in capitals)

capitals["Germany"] = "Berlin"  # add a single value

more_capitals = {"Belgium": "Brussels",
                 "Poland": "Warsaw",}

capitals.update(more_capitals)  # add a single or multiple new entries 
                                # contained in a dictionary
print(capitals)

another_dict_with_capitals = {"France": "Paris",  # France is in this dict too!
                              "Spain": "Madrid",}
capitals = capitals | another_dict_with_capitals  # union of the two dicts
print(capitals)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

```python  wrongdictonary.py
oldtimer =	{"brand": "VW",
             "model": "Käfer",
             "year": 1964,
             "year": 2020
}
print(oldtimer)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

********************************************************************

                            {{2-3}}
********************************************************************

> Nehmen wir an, Sie entwerfen ein Verzeichnis der Studierenden aus Freiberg. Sie wollen die Paarung Studierendenname zu Matrikel als Dictonary umsetzen. Einer Ihrer Kommilitonen schlägt vor, dafür zwei Listen zu verwenden und die Verknüpfung über den Index zu realisieren. Was meinen Sie dazu? 

```python  goodSolution.py
students = {"von Cotta": 12, 
            "Humboldt": 17,
            "Zeuner": 233}

student = "von Cotta"
print(f"Student  {student} ({students[student]})")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

```python  badSolution.py
names = ["von Cotta", "Humboldt", "Zeuner"]
matrikel = [12, 17, 233]

i = 1
print(f"Student  {names[i]} ({matrikel[i]})")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


********************************************************************

### Sets

Ein Set ist eine Sammlung, die ungeordnet, unveränderlich (in Bezug auf exisiterende Einträge) und nicht indiziert ist. Eine Kernidee ist das Verbot von Duplikaten. 

```python  set.py
fruits = {"apple", "banana", "cherry", "lemon", "apple"}
print(fruits)

vegetables_list = ["carrot", "broccoli", "asparagus", "carrot"]
vegetables = set(vegetables_list)
print(vegetables)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Die Leistungsfähigkeit von Sets resultiert aus den zugehörigen Mengenoperationen.

```python  set.py
a = {1,2,3,4,5,6}
b = {2,4,6,7,8,9}
even = {2,4,6,8,}

print(8 in a)     # ist 8 Element von a?
print(even < b)   # ist even eine Teilmenge von b?
print(a | b)      # Vereinigung von a und b
print(a & b)      # Schnittmenge von a und b
print(b - a)      # welche Einträge existieren in b die nicht in a präsent sind
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Über den Elementen eines Sets ist keine Reihenfolge festgelegt

+  ... im Gegensatz zu Sequenz-Datentypen wie Listen, Zeichenketten oder Tupel,   
   die eine Indizierung unterstützen, d.h. Zugriff auf Elemente mit ganzzahligem Index, z.B. `my_todo_list[3]`

+  (nicht nur) bei `print`-Ausgaben ist es jedoch oft wünschenswert, die Elemente 
   eines Sets in eine feste / vorhersagbare Reihenfolge zu bringen. 
   Dies kann z.B. mit der builtin-Funktion `sorted()` erfolgen 

```python
fruits = {"banana", "cherry", "apple", "lemon", "apple"}
print("Set of fruits:", fruits)  # Reihenfolge der Elemente nicht definiert
sorted_fruits = sorted(fruits)  # liefert sortierte Liste
print("List of fruits:", sorted_fruits)  

vegetables = ["carrot", "broccoli", "asparagus", "broccoli", "carrot"]
unique_vegetables = set(vegetables)  # Duplikate werden entfernt
sorted_unique_vegetables = sorted(unique_vegetables)
print("\nVegetables (no duplicates, sorted):", sorted_unique_vegetables)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


### Zusammenfassung 

                            {{0-1}}
********************************************************************

```python     DataTypeExample.py
for i in ['a','b','c']:     # Liste
  print(i, end=",")
print()

for i in "abc":             # String
  print(i, end=",")
print()

for i in ('a','b','c'):     # Tupel
  print(i, end=",")
print()

for i in {0:"a", 1:"b"}:    # Dictionary
  print(i, end=",")
print()
  
for i in {'a','b','c','c'}: # Set
  print(i, end=",")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


********************************************************************

                            {{1-2}}
********************************************************************

Gegeben sei eine Liste der Studiengangsbezeichnungen für die Studierenden dieser Vorlesung. Leiten Sie aus der Liste ab

1. wie viele Studierende eingeschrieben sind?
2. wie viele Studiengänge in der Veranstaltung präsent sind?
3. wie viele Studierende zu den Studiengängen gehören?

```python
# Angabe der Studiengänge der 2022 eingeschriebenen Teilnehmer in der 
# Veranstaltung
study_programs = [
  "S-UWE", "S-WIW", "S-GÖ", "S-VT", "S-GÖ", "S-BAF", "S-VT",
  "S-WWT", "S-NT", "S-WIW", "S-ET", "S-WWT", "S-MB", "S-WIW",
  "S-FWK", "F1-INF", "S-WIW", "S-BWL", "S-WIW", "S-MAG",
  "F2-ANCH", "S-MAG", "S-WWT", "S-NT", "S-ACW", "S-GTB",
  "S-WIW", "F2-ANCH", "S-GTB", "S-GÖ", "S-GBG", "S-GM",
  "S-MAG", "S-GTB", "S-WIW", "S-WIW", "S-FWK", "S-WIW",
  "S-MAG", "S-GBG", "S-GÖ", "S-BAF", "S-BAF", "S-NT", "S-GÖ",
  "S-WWT", "S-GBG", "S-WWT", "S-GBG", "S-ERW", "S-WWT",
  "S-WIW", "S-NT", "S-WIW", "S-GÖ", "S-WIW", "S-GM",
  "S-GBG", "F1-INF", "S-WIW", "S-WWT", "S-ACW", "S-WIW",
  "S-WWT", "S-ACW", "S-INA", "S-FWK", "S-GTB", "S-WIW",
  "S-MORE", "S-WIW", "S-GÖ", "S-BWL", "S-CH", "S-WIW",
  "F2-ANCH", "S-WIW", "S-ACW", "S-ET", "S-ET", "S-GÖ",
  "S-GÖ"
]

# zu 1
print(len(study_programs))                  # Länge der Liste

# zu 2
print(len(set(study_programs)))             # Anzahl Studiengänge
                                            # als Größe des Sets

# zu 3
print({i:study_programs.count(i)            # (Studiengang:Häufigkeit)
       for i in study_programs})            #  als "Dictonary" Comprehension
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


********************************************************************

## Eigene Funktionen

> Das kennen wir schon ... aber noch  mal zur Sicherheit 

_Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine, möglicherweise wiederverwendbare Codeelemente zerlegen._

**Bessere Lesbarkeit**

Der Quellcode eines Programms kann schnell mehrere tausend Zeilen umfassen. Beim
Linux Kernel sind es sogar über 15 Millionen Zeilen und Windows 11, das ebenfalls
zum Großteil in C geschrieben wurde, umfasst schätzungsweise über 60 Millionen 
Zeilen. Ein modernes Auto enthält sogar über 100 Millionen Zeilen Code. Um dennoch die Lesbarkeit des Programms zu gewährleisten, ist die Modularisierung unerlässlich.

**Wiederverwendbarkeit**

In fast jedem Programm tauchen die gleichen Problemstellungen mehrmals auf. Oft
gilt dies auch für unterschiedliche Applikationen. Da nur Parameter und
Rückgabetyp für die Benutzung einer Funktion bekannt sein müssen, erleichtert
dies die Wiederverwendbarkeit. Um die Implementierungsdetails muss sich der
Entwickler dann nicht mehr kümmern.

**Wartbarkeit**

Fehler lassen sich durch die Modularisierung leichter finden und beheben.
Darüber hinaus ist es leichter, weitere Funktionalitäten hinzuzufügen oder zu
ändern.

In allen 3 Aspekten ist der Vorteil in der Kapselung der Funktionalität zu
suchen.

### Syntax

> Funktionsdefinition starten immer mit dem Schlüsselwort **def**. Typen für Parameter oder Rückgabewerte müssen nicht notwendigerweise angegeben werden! Es gelten die üblichen Einrückungsregeln.

```python
def funktionsname(arg1, arg2, ...):
  <anweisungen>
```

```python  FunctionExample.py
import math

def print_pi():
  print(math.pi) 
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


### Parameterübergabe

```python
def halbiere(zahl):
  zahl = zahl / 2
  print(zahl)

zahl = 5
print( halbiere(zahl) )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Python erlaubt analog zu C++ die Vergabe von Standardparametern beim Funktionsaufruf.

### Returnwerte

> Mit **return** kann **ein** Rückgabewert festgelegt und die Funktion beendet werden. Der Rückgabewert kann auch ein Tupel, eine Liste oder ein beliebiges anderes Objekt sein. Tupel können später wieder in einzelne Variablen augetrennt werden.

```python
def halbiere(zahl):
  zahl = zahl / 2
  return zahl

zahl = 5
print(halbiere(zahl))
print(zahl)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Der Parameter `zahl` wird als _Call-by-Assignment_ übergeben. Die Zuweisung eines neuen Wertes ändert nicht die gleichnamige Variable außerhalb der Funktion!

`return` erlaubt formal lediglich einen Rückgabewert. Wie handhaben wir dann die Situation, wenn es mehrere sind?

+  Python erlaubt nach einem `return` mehrere Rückgabewerte. Die Rückgabe erfolgt
   formal als *ein* Tupel

```python
def sumAndMultiplyTo(n):
  sum = 0
  prod = 1
  for i in range(1,n+1):
    sum = sum + i
    prod = prod * i
  return sum,prod

result = sumAndMultiplyTo(10)
print( type(result) )
print(result)

x,y = sumAndMultiplyTo(10)
print(x)
print(y)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

## Typ-Hinweise für Variablen

__Der Interpreter ignoriert die Typhinweise und führt den Code aus ...__

```python
def my_function(numbers: list[int]) -> int:
    return sum(numbers)

numbers = [1, 2, 3, 4, 5]
print(my_function(numbers))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

__Die Entwicklungsumgebung (oder ein externer Type Checker) meckert ...__

![alt-text](images/09_Python/ScreenshotTypeHinting.png)

## Beispiel der Woche

Wir nutzen das Newton-Verfahren zur näherungsweisen Berechnung einer Nullstelle. Gesucht wird die Quadratwurzel einer Zahl *a*.

Funktion $f(x) = x^2 - a$, so dass für die Nullstelle gilt: $x^2 = a$

1. In jedem Schritt berechnen wir $x_{n+1} = x_n - f(x_n)/f'(x_n)$.
2. Für unseren Fall: $x_{n+1} = \frac{1}{2} (x_n + \frac{a}{x_n})$
3. Wir beenden die Iteration, wenn $|x_{n+1} - x_n| < \varepsilon$

```python newton.py
def square_root(start, a, verbose=False, eps=0.00000001):
  xn = a
  while True:
    if verbose: print(xn)

    # x = xn - (xn**2 - a) / (2*xn)
    # oder:
    x = (xn + a/xn) / 2

    if abs(x-xn) < eps:
      break
    xn = x

  return x

if __name__ == "__main__":
  a = float( input("Value for a (to compute sqrt(a)): ") )
  x = float( input("Inital value for x: ") )
  verbose_output = input("Show all iterations (y/n)? ")
  if verbose_output == 'y':
    verbose_output = True
  else:
    verbose_output = False
  result = square_root(x, a, verbose_output)
  print(f"The zero point of y=x^2-{a} is", result)
  print(f"I.e. the square root of {a} is {result}")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Welches Problem sehen Sie?

# Quiz
## Weitere Datentypen
### Tupel oder Liste?
> Welche Vorteile hat der Datentyp `Tupel` gegenüber dem Datentyp `Liste`?
[[ ]] `Tupel` sind einfacher zu erstellen.
[[X]] Iterationen über `Tupel` sind schneller als Iterationen über `Listen`
[[ ]] `Tupel` können mehr Elemente enthalten
[[X]] `Tupel`benötigen weniger Speicherbedarf

{{1}}
********************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
a = (9, 2)
print(a[0])
```
[(X)] 9
[( )] 2
[( )] Das Programm endet mit einem Error
********************************************************************

{{2}}
********************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
a = (9, 2)
a[0] = 7
print(a[0])
```
[( )] 9
[( )] 7
[( )] 2
[(X)] Das Programm endet mit einem Error
********************************************************************

### Dictionaries
> Wie lautet die Ausgabe dieses Programms?
```python
# Hier werden Noten gespeichert
grades = {"Peter": 1.0,
          "Franz": 3.0,
          "Max": 1.7,
          "Jonas": 2.3}

examples = {"Kurt": 1.3,
            "Bernd": 3.3}

examples["Michi"] = 2.0

grades.update(examples)
print(grades["Michi"])

```
[(X)] 2.0
[( )] Das Programm endet mit einem Error

### Sets
> Wie viele Elemente befinden sich im Set `st`?
```python
st = {"Franz", "Peter", "Franz", "Michi", "Peter"}
print(len(st))
```
[[3]]

{{1}}
********************************************************************
> Wie lautet die Ausgabe dieser Funktion? (Bitte geben Sie die Antwort ohne geschweifte Klammern an)
```python
a = {1,2,3,4}
b = {7,4,6,7}

print(sorted(b - a))
```
[[6, 7]]
<script>
let input = "@input"

input == "6, 7" || input == "6,7"
</script>
********************************************************************

{{2}}
********************************************************************
> Wie lautet die Ausgabe dieser Funktion? (Bitte geben Sie die Antwort ohne geschweifte Klammern an)
```python
a = {1,2,3,4}
b = {7,4,6,7}

print(b & a)
```
[[4]]
********************************************************************

{{3}}
********************************************************************
> Wie lautet die Ausgabe dieser Funktion? (Bitte geben Sie die Antwort ohne geschweifte Klammern an)
```python
a = {1, 2, 3, 4}
b = {7, 4, 6, 7}

print(b < a)
```
[( )] True
[(X)] False
[( )] {1, 2, 3}
********************************************************************

{{4}}
********************************************************************
> Wie lautet die Ausgabe dieser Funktion? (Bitte geben Sie die Antwort ohne geschweifte Klammern oder Leerzeichen an)
```python
a = {1,2,3,4}
b = {7,4,6,7}

print(sorted(b | a))
```
[[1,2,3,4,6,7]]
********************************************************************

## Eigene Funktionen
### Syntax
> Mit welchem Schlüsselwort starten Funktionsdefinitionen in Python?
[[def]]

### Parameterübergabe
> Wie lautet die Ausgabe dieses Programms auf 2 Nachkommastellen gerundet?
```python
from math import pi

def to_rad(num):
  rad = num * (pi / 180)
  return rad

deg = 90
print(to_rad(deg))
```
[[1.57]]

### Returnwerte
> Wie lautet die Ausgabe dieses Programms? Bitte geben Sie die Antwort ohne Klammern an.
```python
def get_min_max(a):
    return (min(a), max(a))

a = (10, 47, 18, 1, 33, 20)
result = get_min_max(a)
print(result)
```
[[1, 47]]
<script>
let input = "@input"

input == "1, 47" || input == "1,47"
</script>

{{1}}
********************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
def modify_number(a):
    a = -1
    return

a = 42
modify_number(a)
print(a)
```
[[42]]
********************************************************************

