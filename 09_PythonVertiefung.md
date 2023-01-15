<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.5
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_PythonVertiefung.md)

# Objektorientierung in Python

| Parameter                | Kursinformationen                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Veranstaltung:**       | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                    |
| **Semester**             | `Wintersemester 2022/23`                                                                                                                                                                       |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                                              |
| **Inhalte:**             | `Erweiterte Konzepte der Programmiersprache Python`                                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_PythonVertiefung.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/09_PythonVertiefung.md) |
| **Autoren**              | @author                                                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------


**Fragen an die heutige Veranstaltung ...**

* 

---------------------------------------------------------------------

## Weitere Datentypen 

Sie haben bereits Listen (`list`), `range` Objekte und Text (``string`) als Datenstruktur kennengelernt - im Weiteren existieren daneben vier weitere Sequenzdatentypen: byte sequences (`bytes` objects), byte arrays (`bytearray` objects) und `tuples`.
Dazu kommen `dictionaries` und `sets` als Containertypen. 

| Datentyp | Besonderheit | Syntax |
|----------|--------------|--------|
| `list`  | veränderliche Sequenz von (beliebigen) Daten | `l = ["grün", 1, True]` |
 |  |  | `l[0] = 4` |
| `strings` | Darstellung von Zeichenketten | `s="Hello World"` |
| `bytes` | Unveränderbare Folge von Elementen | `t1 = (1, 2, 3)` |
| `bytearray` | Unveränderbare Folge von Elementen | `t1 = (1, 2, 3)` |
| `tupel` | Unveränderbare Folge von Elementen | `t1 = (1, 2, 3)` |
| `range` | iterierbare, unveränderbare Folge von Elementen | `r = range(3, 20, 2)` |

### Tupel oder Liste?

Warum ein Tupel anstelle einer Liste verwenden?

+ Die Programmausführung ist beim Iterieren eines Tupels schneller als bei der entsprechenden Liste - Dies wird wahrscheinlich nicht auffallen, wenn die Liste oder das Tupel klein ist.

+ Der Speicherbedarf eines Tupels fällt in der Regel geringer aus, als bei einer Listendarstellung ein und des selben Inhaltes.

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

l=list(range(10000001))
t=tuple(range(10000001))

start = time.time_ns()
for i in range(len(t)):
    a = t[i]
end = time.time_ns()
print("Tuple duration: ", end - start)

start = time.time_ns()
for i in range(len(l)):
    a = l[i]
end = time.time_ns()
print("List duration : ", end - start)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Dictionaries

Dictionaries werden zur Speicherung von Schlüssel Werte Paaren genutzt. Ein dictionary ist eine Sammlung von geordneten (entsprechend der Reihenfolge der "Einlagerung"), veränderlichen Einträgen, für die Schlüssel werden keine Dublikate zugelassen.


<!--style="width: 100%;"-->
```ascii
   
 Listen                                     Dictonary

 Index                                      Schlüssel
 +---------------+     +---------+          +---------------+     +---------+
 |       0       |---->| `Hello` |          | `erstes Wort` |---->| `Hello` |
 +---------------+     +---------+          +---------------+     +---------+

 +---------------+     +---------+          +---------------+     +---------+
 |       1       |---->| `World` |          | `zweites Wort`|---->| `World` |
 +---------------+     +---------+          +---------------+     +---------+

 +---------------+     +---------+          +---------------+     +---------+  
 |       2       |---->| ...     |          | `drittes Wort`|---->| ...     |
 +---------------+     +---------+          +---------------+     +---------+

       ....                                      ....
```

```python  dictonary.py
capital_city = {"France": "Paris",
                "Italy": "Rome",
                "England": "London"}

print(capital_city)
print(capital_city.has_key("England"))

capital_city["Germany"] = "Berlin"  # add a single value

examples = {"Belgium": "Bruessels",
            "Poland": "Warsaw"}

capital_city.update(examples)       # add a single or multiple new entries 
                                    # contained in a dictionary
print(capital_city)

```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

```python  dictonary.py
oldtimer =	{"brand": "Ford",
             "model": "Mustang",
             "year": 1964,
             "year": 2020
}
print(oldtimer)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


> Nehmen wir an, Sie entwerfen ein Verzeichnis der Studierenden aus Freiberg. Sie wollen die Paarung Studierendenname zu Matrikel als Dictornary umsetzen. Einer Ihrer Kommilitonen schlägt vor, dafür zwei Listen zu verwenden und die Verknüpfung über den Index zu realsieren. Was meinen Sie dazu? 

```python  badSolution.py
names = ["von Cotta", "Humboldt", "Zeuner"]
matrikel = [12, 17, 233]

i = 1
print("Student ", names[i], " (",  matrikel[i], ")" )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Sets



### Zusammenfassung 

```python
for i in ['a','b','c']:
  print(i, end=",")
for i in "abc":
  print(i, end=",")

for i in [5,7,9]:
  print(i, end=",")
for i in [3.4,7.9,6.78]:
  print(i, end=",")

for i in ('x','y','z'):
  print(i, end=",")

for i in {0:"a", 1:"b"}:  # Was ist das??
  print(i, end=",")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


## Eigene Funktionen
Wiederholung:
========================
> Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine, möglicherweise wiederverwendbare Codeelemente zerlegen.

**Bessere Lesbarkeit**

Der Quellcode eines Programms kann schnell mehrere tausend Zeilen umfassen. Beim
Linux Kernel sind es sogar über 15 Millionen Zeilen und Windows, das ebenfalls
zum Großteil in C geschrieben wurde, umfasst schätzungsweise auch mehrere
Millionen Zeilen. Um dennoch die Lesbarkeit des Programms zu gewährleisten, ist
die Modularisierung unerlässlich.

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

{{1}}
<section>
Syntax:
========================

> Funktionsdefinition starten immer mit dem Schlüsselwort **def**. Typen für Parameter oder Rückgabewerte müssen nicht angegeben werden! Optional ist dies dennoch möglich (Teil der nächsten Vorlesung). Es gelten die üblichen Einrückungsregeln.

```python
def funktionsname(arg1, arg2, ...):
  <anweisungen>
```

```python
def exec_menu():
  print("-"*15)
  print(" 1: Daten eingeben\n 2: Summe ausgeben\n 3: Daten löschen\n 4: Beenden")
  opt = int(input("Wählen Sie eine Programmfunktion:"))
```
</section>

### Parameterübergabe
> Die Parameter im Funktionskopf sind lokale Variablen innerhalb der Funktion.

Beachten Sie folgendes Beispiel:

```python
def halbiere(zahl):
  zahl = zahl / 2
  return zahl

zahl = 5
print( halbiere(zahl) )
print( zahl )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Der Parameter *zahl* der Funktion ist eine lokale Variable. Die Zuweisung eines neuen Wertes ändert nicht die gleichnamige Variable außerhalb der Funktion! Sind die als Parameter übergebenen Objekte unveränderbar (z.B. Zahlen, Strings, Tupel), dann haben Veränderungen innerhalb der Funktion keine Auswirkungen auf Objekte außerhalb.

{{1}}
<section>
> Veränderbare Objekte (z.B. Listen), können in der Funktion modifiziert werden. D.h. die Veränderungen sind auch außerhalb der Funktion wirksam!

```python
def verdopple(liste):
  liste.extend(liste)
  return liste

liste = [5,10,15]
print( verdopple(liste) )
print( liste )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

|||
| Unveränderbare Objekte (immutable): | int, float, string, bool, decimal, complex, tuple, range, frozenset, bytes |
| Veränderbare Objekte (mutable): | list, dictionary, set, Nutzerdefinierte Objekte |

</section>

### Returnwerte
> Mit **return** kann **ein** Rückgabewert festgelegt und die Funktion beendet werden. Der Rückgabewert kann auch ein Tupel, eine Liste oder ein beliebiges anderes Objekt sein. Tupel können später wieder in einzelne Variablen augetrennt werden.

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
print(x, y)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)




## Typ-Hinweise für Variablen


## Beispiel der Woche

Quadratwurzel mit Newton-Verfahren
==================================
Wir nutzen das Newton-Verfahren zur näherungsweisen Berechnung einer Nullstelle. Gesucht wird die Quadratwurzel einer Zahl *a*.

Funktion $f(x) = x^2 - a$, so dass für die Nullstelle gilt: $x^2 = a$

1. In jedem Schritt berechnen wir $x_{n+1} = x_n - f(x_n)/f'(x_n)$.
2. Für unseren Fall: $x_{n+1} = \frac{1}{2} (x_n + \frac{a}{x_n})$
3. Wir beenden die Iteration, wenn $|x_{n+1} - x_n| < \varepsilon$

```python
def square_root(a, output=False, eps=0.00000001):
  xn = a
  while True:
    if output: print(xn)

    # x = xn - (xn**2 - a) / (2*xn)
    # oder:
    x = (xn + a/xn) / 2

    if abs(x-xn) < eps:
      break
    xn = x

  return x

if __name__ == "__main__":
  x = float( input("Enter value for x:") )
  output = input("Show all outputs (y/n)?")

  result = square_root(x, output=='y')
  print("sqrt(",x,") =", result)

```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)
