<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Florian Richter
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de & Flo.Richter@informatik.tu-freiberg.de
version:  1.0.6
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md#10

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/08_PythonGrundlagen.md)

# Python Grundlagen

| Parameter                | Kursinformationen                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Veranstaltung:**       | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                    |
| **Semester**             | `Wintersemester 2022/23`                                                                                                                                                                       |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                                              |
| **Inhalte:**             | `Grundlagen der Programmiersprache Python`                                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/08_PythonGrundlagen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/08_PythonGrundlagen.md) |
| **Autoren**              | @author                                                                                                                                                                                        |


--------------------------------------------------------------------

![Python Logo](https://www.python.org/static/img/python-logo@2x.png "www.python.org")<!-- style="width:30%;" -->

**Fragen an die heutige Veranstaltung ...**

* Warum sollte man andere Programmiersprachen als C++ in Betracht ziehen?
* Welche Vorteile hat die Sprache **Python**?
* Wie unterscheidet sich der Syntax von C++?

**Beispiel-Literatur:**

 * [Schnellstart Python - Ein Einstieg ins Programmieren für MINT-Studierende](https://link.springer.com/book/10.1007/978-3-658-26133-7) (kostenloses E-Book für TUBAF-Studenten)
 * [Python 3 - Das umfassende Handbuch](https://openbook.rheinwerk-verlag.de/python/)

---------------------------------------------------------------------

## Motivation

> __Aufgabe__: Bestimmen Sie die maximalen Tages- und Nachttemperaturen pro Tag, Woche und Monat mit unserem Mikrocontroller über einem Jahr. Wie gehen Sie vor?

<!--
style="width: 100%; min-width: 620px; max-width: 920px;"
-->
```ascii 
                            Datenlogger
                            +------------------------------------------------+
                            |                             Arbeitsspeicher    |
                       +    |         +-----------+      +--------------+    |
       Umgebung-       |\   | Sensor- | Controll- |      | ...          |\   |         
       phänomene       | +--|-------->| Software  |--+-->| 12:30 Temp 12+-+  |
                       |/   | signale |           |      | 12:40 Temp 13  |  |
                       +    |         +-----------+      +----------------+  |
                            |                                     |          | 
                            |               +---------------------+          |
                            |               |    .----.                      |  +-> Serielle Schnittstelle
                            |               v    |    | täglich,             |  |            max    min
                            |         +-----------+   | wöchtentlich,        |  |   1.3.     10.5     -3.5
                            |         | Min/Max   |<--. monatlich            |  |   2.3.     11.0     -3.8
                            |         | Algo-     |                          |  |   ...
                            |         | rithmus   |--------------------------|--+   KW 9      9.2      1.3
                            |         +-----------+                          |      ...     
                            +------------------------------------------------+      März     12.3      2.7
```

> __Frage__: Welche Nachteile sehen Sie in dem Vorgehen?

{{1}}
+ Unser Controller hat keinen "festen Speicher" - die Daten würden im Arbeitsspeicher liegen und wären damit im Fall einer Stromunterbrechung verloren 

+ Eine Messung pro 10 Minuten bedeutet, dass pro Tag $6 \cdot 24 = 144$ Datensätze entstehen. Im Monat sind das etwa $30 \cdot 144 = 4320$. Wenn wir davon ausgehen, dass wir die Daten als 4 Byte breite Float Werte abbilden, würde dies für eienn Monat 17.280 Byte (16.8 kB) und für ein Jahr 210.240 Byte (205 kB) Speicherbedarf bedeuten. Unser Controller verfügt über 256 kB Arbeitsspeicher.

+ Die lokale Verarbeitung ist energieaufwändig. Wenn wir davon ausgehen, dass der Controller in einem Feldversuch möglichst lange mit einer Batterie betrieben werden soll, so müssen wir den Berechnungsaufwand reduzieren.

> __Lösungsansatz__: Wir kommunizieren die Rohdaten in eine Cloud und verarbeiten diese separat.

<!--
style="width: 100%; min-width: 620px; max-width: 920px;"
-->
```ascii 
                            Datenlogger                    Speichermedium         Auswertung
                            +------------------------+
                            |                        |     +---------------+
                       +    |         +-----------+  |  +->| Speicherkarte |      +-------------------+ 
       Umgebung-       |\   | Sensor- | Controll- |  |  |  +---------------+      | Einlesen          |  
       phänomene       | +--|-------->| Software  |--|--+                         | Analyse           |
                       |/   | signale |           |  |  |  +---------------+      | Diagrammerzeugung |
                       +    |         +-----------+  |  +->| Datenserver   |      | ...               |   
                            |                        |     +---------------+      +-------------------+
                            |                        |                             ^ 
                            +------------------------+     +--------------+        |          .....
                                                           | ...          |\       | .... ....     .
                                                           | 12:30 Temp 12+-+      |.    .
                                                           | 12:40 Temp 13  |      |
                                                           +----------------+      +------------------>
                                                                          
```

> Wir entkoppeln damit die Datenerzeugung und Auswertung! Welche Programmiersprache benutzen wir aber für die Auswertung? Warum nicht einfach weiter C++?

{{2}}
Python erleichtert die schnelle Entwicklung von Scripten zur Datenauswertung.

- Schnelles Ausprobieren durch:

  - Einfache Syntax, kurze Programme
  - Interpreter statt Compiler
  - Interaktivmodus
  - Keine Deklarierung von Datentypen
  - Automatisches Speichermanagement

- Plattformunabhängigkeit (Linux, Windows, MacOS und auch Mikrocontroller)
- Einfache Erweiterbarkeit, große Standardbibliothek und viele weitere frei verfügbare Module

            {{3}}
************************************

![Comic C++](./images/08_Python/comic.png "C++")

![Comic Python](./images/08_Python/comic_python.png "Python")

************************************

            {{3}}
```python
print("I will not throw paper airplanes in class\n" * 10)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Python Historie 

* *relativ* jung Sprache, Entwicklung 1990 in Amsterdam (vgl. C 1972, C++ 1979)
* Ziel sollte eine Sprache sein, die auch von Programmieranfängern einfach erlernt werden kann
* 2008 erschien Version 3.0 mit einer Komplettüberarbeitung und vielen Verbesserungen
* Aktuell sollte **mindestens Version 3.7** oder neuer verwendet werden (**3.11** ist die neueste Version)

  * Anaconda nutzt derzeit Version 3.9

> Achten Sie bei Ihren Recherchen auf das Alter Ihrer Quellen, bzw. die verwendete Python-Version. Man findet noch viele Anleitungen zu Python 2.7. Diese sind häufig jedoch **nicht mehr kompatibel** zu Python 3.

### Beispiele für den Einsatz von Python
Typische Einsatzszenarien sind z.B.:

* Kleine Server-Programme
* Schnelles entiwckeln von Scripten zur Datenauswertung
* Konvertierung / Formatierung von Dateien bzw. großen Datenmengen
* Numerische Berechnungen und Generierung von Diagrammen
* **Maschinelles Lernen** dank Bibliotheken, wie TensorFlow, scikit-learn oder PyTorch
* Python als Scriptsprache für Erweiterungen (z.B. **ParaView**, **QGIS**, Blender, Gimp)
* Programmierung auf dem RaspberryPi
* Etwas spezieller: Programmierung von Robotern mit ROS (Robot Operating System)
* ...

{{1}}
![QGIS mit Python Konsole](./images/08_Python/qgis.png "QGIS Python Konsole")
![Raspberry Pi 4B](./images/08_Python/raspberry4.jpg "www.raspberrypi.com")


### Entwicklungsumgebungen

**Wie installiere ich bei mir Python?**

Unter Linux und MacOS kann Python z.B. über die Kommandozeile bzw. Paketmanager installiert werden. Für Windows empfiehlt sich die Installation der Anaconda Distribution (auch für Linux und Mac verfügbar).

> Für Python gibt es viele verschiedene Entwicklungsumgebungen. In den Übungen nutzen wir aber weiterhin Visual Studio Code.

Anaconda nutzt als Standard-Editor **Spyder** (**S**cientific **PY**thon **D**evelopment **E**nvi**R**onment). Beliebt sind auch interaktive **Jupyter**-Dokumente (Notebooks).

![Spyder IDE](./images/08_Python/spyder.png "Spyder Editor")
![Interaktive Jupyter-Notebooks](./images/08_Python/jupyter.png "Jupyter Notebook")

## Elemente der Programmiersprache 
Welche Programmierparadigmen unterstützt Python?

* Imperativ?
* Prozedural?
* Objektorientiert?

```python
for i in range(10):
  print("Hallo Welt", i)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

{{1}}
************************************
Welche Programmierparadigmen unterstützt Python? -> **Alle 3** :-P

* Imperativ ✔️
* Prozedural ✔️
* Objektorientiert ✔️

```python
for i in range(10):
  print("Hallo Welt", i)
```

```python
def hallo():
     for i in range(10):
          print("Hallo Welt", i)
```

```python
class Hallo:
     def __init__(self):
          for i in range(10):
               print("Hallo Welt", i)
```
************************************

### Zuweisungen und Datentypen
> Python nutzt eine dynamische Typisierung, d.h. eine Variable wird erst zur Laufzeit mit Typ des zugewiesenen Werts assoziiert. Sie kann auch mit einem beliebigen neuen Datentypen überschrieben werden.

```python
a = 1
a += 3
type(a)

a = "hello"
type(a)

# Python kann ohne Hilfsvariable, 2 Variablen tauschen:
x, y = 3.0, -2.0
x, y = y, x
print(x, y)

# a = b
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

{{1}}
<section>
> Verkürzte Schreibweisen für Rechenoperationen, wie **+=** **-=** ***=** und **/=** existieren. Ein **++** oder **--** gibt es in Python aber nicht.

```python
x = 10
y = 5
x /= y
x += 8.5
x *= 4
print(x)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

</section>

### Standard Datentypen
> Die Standard-Datentypen von Python bringen neben elementaren Datentypen wie **int**, **float** und **bool** auch komplexere Datentypen mit, die uns bei der schnellen Implementierung von mathematischen Formeln oder großen Datenstrukturen helfen.

|||
|Numerisch | int, float, complex |
|Text | str |
|Sequenz | list, tuple, range |
|Weitere | z.B. bool, dict, set, bytearray |
|NoneType | None |

### Namenswahl für Variablen
> Namen von Variablen, Funktionen, Klassen,... bestehen aus Buchstaben, Ziffern, Underscore (_)

- Ziffer darf nicht am Anfang stehen
- Ab Python 3 sind auch Buchstaben außerhalb des ASCII-Bereichs erlaubt

  - Buchstaben aus Alphabeten fast aller Sprachen, z.B. ä, ö, ü, θ, π, ラ
  - nicht erlaubt sind Sonderzeichen wie €, $, @,§ sowie Emojis
  - guter Stil ist aber, trotzdem nur Zeichen aus ASCII-Bereich zu verwenden!

- lesbare aber nicht zu lange Namen

  - z.B. sum, value

- Hilfsvariablen, die man nur über kurze Strecken braucht, eher kurz:

  - z.B. i, j, x 

- mit Kleinbuchstaben beginnen, Worttrennung durch "_" oder Großbuchstaben, z.B.

  - input_text („Snake Case“), empfohlen in Style Guide for Python Code
  - inputText („Camel Case“)

- Variablen, die man im ganzen Programm braucht, eher länger:

  - z.B. input_text

Reservierte Bezeichner:
=======================
||||||
| False | await | else | import | pass |
| None | break | except | in | raise |
| True | class | finally | is | return |
| and | continue | for | lambda | try |
| as | def | from | nonlocal | while |
| assert | del | global | not | with |
| async | elif | if | or | yield |

Siehe auch Python Tutorial zum Thema Coding Style:

* https://docs.python.org/3/tutorial/controlflow.html#intermezzo-coding-style
* https://peps.python.org/pep-0008/

### Ausgabe
> Die **print**-Funktion ist unser Äquivalent zu std::cout aus C++. Beliebig viele Konstanten und Variablen können als Parameter übergeben werden. Die uns bereits bekannten Sonderzeichen **\\t** (Tabulator) und **\\n** (Neue Zeile) können wie gewohnt eingebaut werden.

```python
x = 3.141
y = x**2
print("5 * 5 =", 25)
print("x \t=\t", x, "\nx² \t=\t", y)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Mit dem optionalen Parameter *end=* können Sie den standardmäßigen Zeilumbruch durch ein anderes Zeichen ersetzen. Die erweiterte Formatierung von Ausgaben ist Teil der nächsten Vorlesung.

```python
print(x, y, z, end=",")
```

### Eingabe
> Ergebnis der **input**-Funktion ist immer ein **String**. Für die Verarbeitung als Zahl ist daher immer eine **Typenkonvertierung** erforderlich. Eine Eingabeaufforderung kann optional als Parameter übergeben werden.

**Falsch:**<!-- style="color:red" -->

```python
""" 
Liefert einen Fehler, da x ein String ist
"""
x = input("x eingeben:")
y = x**2
print("y = ", y)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

**Richtig:**<!-- style="color:darkgreen" -->

```python
x = float( input("x eingeben:") )
y = x**2
print("y = ", y)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Zusätzliche Module einbinden
> Mit **import** lassen sich Module einbinden. Ähnlich zu den Standard C++ Headern sind die Bestandteile der Python Module in einen Namensraum gekapselt.

```cpp
#include <cmath>

x = std::sin(M_PI)
std::cout << x;
```

```python
import math

x = math.sin(math.pi)
print(x)

#---- Formatiertes Beispiel:
print(f"{x:.5f}")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Bei Bedarf lassen sich alle oder einzelne Komponenten in den eigenen Namensraum importieren:

```python
from math import *       # Einfach, aber sollte wenn möglich vermieden werden
from math import sin,cos
```

Eine Umbennung ist alternativ auch möglich:

```python
import math as m
print(m.pi)
```

### Listen
> **In Python ist alles ein Objekt!** Z.B. auch elementare Datentypen, wie **Integer**. Komplexere Datentypen, wie Listen verfügen über Methoden zu deren Manipulation. Die Länge einer Liste fragen wir hingegen mit der **Funktion** **len** ab.

Der Aufruf von Methoden funktioniert wie in C++. Der Datentyp **list** verfügt über mehrere spezielle Methoden:

* reverse(), sort(), extend(), append(), remove(), clear(), ...

```python
liste = [4,2,3,1]
print( len(liste) )

liste.reverse()
print(liste)

liste.sort()
print(liste)

liste.append(7)
liste.extend([5,6])
print(liste)

liste.remove(3)
print(liste)

print( len(liste) )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### Listen-Indizierung
> Die Möglichkeiten Listenelemente zu indizieren sind sehr vielfältig in Python. Wir können beispielsweise auch vom Ende der Liste starten oder bestimmte Bereiche auswählen. **Wichtig:** Listen beginnen immer mit dem Index **0**.

```python
data = [10,20,50,200,300,350]

print( data[-1] )
print( data[1:] )
print( data[1:4] )
print( data[1:4:2] )
print( data[-3:] )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

## Konstrollstrukturen

Wiederholung:
=============

1. **Verzweigungen (Selektion):** In Abhängigkeit von einer Bedingung wird der Programmfluss an unterschiedlichen Stellen fortgesetzt.

  Beispiel: Wenn bei einer Flächenberechnung ein Ergebnis kleiner Null generiert wird, erfolgt eine Fehlerausgabe. Sonst wird im Programm fortgefahren.

2. **Schleifen (Iteration):** Ein Anweisungsblock wird so oft wiederholt, bis eine Abbruchbedingung erfüllt wird.

  Beispiel: Ein Datensatz wird durchlaufen um die Gesamtsumme einer Spalte zu bestimmen. Wenn der letzte Eintrag erreicht ist, wird der Durchlauf abgebrochen und das Ergebnis ausgegeben.

### Selektion mit if
> Auch in Python sind innerhalb einer Selektion mehrere Alternativen möglich. Eine **if**-Anweisung kann von beliebig vielen **elif** Zweigen gefolgt werden. Am Ende darf **höchstens** ein **else**-Zweig stehen.

<!--
style="width: 50%;"
-->
```ascii
             |
             v
             +
            / \
     +-----+ B +-----+
  ja |      \ /      | nein
     |       +       |
     v               v
  +-----+         +-----+
  | A 1 |         | A 2 |  
  +--+--+         +--+--+ 
     |               |
     +-------+-------+
             |
             v
          +-----+
          | A 3 |         
          +-----+             
```

Aufbau:
=======

- **if** – Schlüsselwort
- Bedingung -> kann zu True oder False evaluiert werden

  - auch komplexe Bedingungen, z.B. verknüpft mit **and** oder **or**
  - *if a > 5 and a < 10 :*

- Doppelpunkt ':'
- Anweisungen, die ausgeführt werden, falls Bedingung gilt (**eingerückt**)
- optionaler **else**-Zweig

```python
if Bedingung:
  Anweisung1
else:
  Anweisung2

Anweisung3
```

```python
if x == y:
  print("x and y are equal")
elif x < y:
  print("x is less than y")
else:
  print("x is greater than y")
```

> Achten Sie in Python immer auf eine korrekte und möglichst konsistente **Einrückung**!

### Kleines Beispiel

```python
a = int( input("Erste Zahl:") )
b = int( input("Zweite Zahl:") )

if a%2 == 0 and b%2 == 0:
  print("Beide Zahlen sind gerade!")
elif a%2 == 0:
  print("Nur die erste Zahl", a, "ist gerade!")
elif b%2 == 0:
  print("Nur die zweite Zahl", b, "ist gerade!")
else:
  print("Keine Zahl ist gerade!")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Erinnerung: Der **Modulo**-Operator **%** liefert den Rest einer ganzzahligen Division.

### Verschachtelte If-Anweisungen
> If-Anweisungen lassen sich beliebig verschachteln. Dabei ist wieder ganz besonders auf eine korrekte **Einrückung** zu achten!

**Beispiel: Tiere raten**

<!--style="width: 20%; float:left;"-->
```ascii
         .-----------------.
         |   can it fly?   |
         '--------+--------'
         n        |        y
         +--------+--------+   
         |                 |
         v                 v
.-----------------.     +--+---+
|  does it bark?  |     | bird |
'--------+--------'     +------+
   n     |     y
   +-----+-----+   
   |           |
   v           v
+--+--+     +--+--+
| cat |     | dog |
+--+--+     +--+--+
```
![Korrekte Einrückung](./images/08_Python/indentation.png "")<!--style="margin-left:20%; width: 30%;"-->



```python
if input("can it fly? ") == 'y':
  print("bird")
else:
  if input("does it bark? ") == 'y':
    print("dog")
  else:
    print("cat")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### While-Schleife
> In Python gibt es zwei Arten von Schleifen: **for** und **while** (abweisende Schleifen). Beide Schleifenarten kennen Sie auch aus C++. Erinnerung: eine while-Schleife wird **solange** ausgeführt, wie die Bedingung erfüllt ist (**True**).

<!--style="width: 30%;"-->
```ascii
             |
     +------>+
     |       |
     |       v
     |       +
     |      / \
     |     + B +-----+
     |      \ /      | nein
     |       +       v
     |       | ja
     |       v
     |     +---+
     |     | A |
     |     +-+-+
     +-------+
```

```python
while <bedingung>:
  <anweisungen>
```

Beispiel: Fibonacci-Zahlen < 100
================================

```python
a, b = 0, 1
while b < 100:
  print(b, end='|')
  a, b = b, a+b
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

### For-Schleife

                                 {{0-1}}
***************************************************************************

> For-Schleifen erlauben auch in Python eine Wiederholung mit festgelegten Start- und Endwerten. Die Syntax unterscheidet sich aber von C++. Das Schlüsselwort **in** ist ein fester Bestandteil und wird gefolgt von einer **Sequenz**.

```python
for <variable> in <sequenz>:
  <anweisungen>
```

Die Schreibweise ermöglicht ein sehr einfaches Abarbeiten von Listen und anderen indizierbaren Datenstrukturen:

{{1}}
<section>
Beispiele mit verschiedenen Sequenzen:

```python
for i in ['a','b','c']:
  print(i, end=",")
for i in "abc":
  print(i, end=",")

for i in [5,7,9]:
  print(i, end=",")
for i in [3.4,7.9,6.78]:
  print(i, end=",")

```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)
</section>

***************************************************************************

                                 {{1-2}}
***************************************************************************


> Die **range**-Funktion kann mit 1, 2 oder 3 Parametern aufgerufen werden. Sie wird hauptsächlich für for-Schleifen benötigt. **Wichtig:** der Endwert ist in der Menge **nicht** enthalten!

* **Signatur:** range([start,] stop[, step])

  * start, step sind optionale Parameter
  * 1 Parameter -> nur Endwert angeben (start=0, step=1)
  * 2 Parameter -> Start- und Endwert angeben (step=1)

* Ergebnis der Funktion ist ein **range-Objekt**, keine Liste! Es lässt sich aber in eine Liste konvertieren:
```python
x = range(0,5)
print(x, type(x))
print( list(x) )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Beispiele mit der range-Funktion:

```python
for x in range(5):
  print(x+1, end=" ")
print("\n")

for x in range(1,6):
  print(x, end=" ")
print("\n")

for x in range(20,-1,-2):
  print(x, end=" ")
print("\n")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

***************************************************************************

### Schleifen oder List Comprehension
> **List Comprehension** oder Listen-Abstraktion ermöglicht eine sehr kurze Schreibweise bei der Arbeit mit Listen. Es erinenrt etwas an mathematische Mengendefinitionen, wie \{ x² \| x ∈ ℕ ^ x < 20 }.

```python
square = [x**2 for x in range(20)]
print( square )

# alternative Darstellung mit einer Schleife
square = []
for x in range(20):
  square.append(x**2)
print( square )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

_List Comprehensions_ werden oft als "pythonischer" beschrieben als loops ( oder `map()`). Sie sind auch aussagekräftiger als Schleifen, was bedeutet, dass sie einfacher zu lesen und zu verstehen sind. Schleifen entwickeln einen Iterationsprozess, während Sie sich mit einem _List Comprehensions_ stattdessen auf das konzentrieren, was Sie in die Liste umsetzen wollen.

Beispiele:

```python
square = [x**2 for x in range(20)]
print( square )

cities = ["Dresden", "Freiberg", "Leipzig", "Frankenberg"]
print( [c.upper() for c in cities] )

# Nur Städte, die mit F beginnen
cities = ["Dresden", "Freiberg", "Leipzig", "Frankenberg"]
print( [c.upper() for c in cities if c[0] == "F"] )

# Wir können auch das Ergebnis manipulieren
cities = ["Dresden", "Freiberg", "Leipzig", "Frankenberg"]
print( [c.upper() if c != "Freiberg" else c.upper()+" (Sachs)" for c in cities if c[0] == "F"] )
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


### Und do-while???
> Eine Nichtabweisschleife oder do-while-Schleife existiert in Python **nicht**! Aber wir könne mit einer while-Schleife jede andere Schleifenart nachbilden.

<!--style="width: 30%;"-->
```ascii
             |
     +------>+
     |       |
     |     +---+
     |     | A |
     |     +-+-+
     |       |
     |       v
     |       +
     |      / \
     +-----+ B +-----+
            \ /      | nein
             +       v
```

Für den folgenden Workaround nutzen wir eine Endlosschleife. Auch wenn Endlosschleifen manchmal unabsichtlich verursacht werden und zu Fehlverhalten führen, können sie manchmal erwünscht sein (z.B. *main loops* von Menüs oder graphischen Benutzeroberflächen). Wie in C++ können wir mit **break** eine Schleife dennoch abbrechen.

{{1}}
<section>
Wir bauen uns eine do-while Schleife nach:

```python
while True:
  <anweisungen>

  if not <bedingung>:
    break
```
</section>

{{2}}
<section>
Ein Programmmenü als Typisches Beispiel:

```python
data = []
while True:
  print("-"*15, "\n 1: Daten eingeben\n 2: Summe ausgeben\n 3: Daten löschen\n 4: Beenden")
  opt = int(input("Wählen Sie eine Programmfunktion:"))

  if opt == 1:
    data.extend( float(x) for x in input("Zahlen mit Komma getrennt eingeben:").split(",") )
  elif opt == 2:
    print("Summe =", sum(data))
  elif opt == 3:
    data.clear()
  elif opt == 4:
    break
  else:
    print("Wählen Sie eine gültige Option!")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)
</section>

## Formatierte Ausgabe

                                    {{0-1}}
****************************************************************************************

Bislang haben wir uns mit dem "einfachen" `print` Mechanismus für einzelne Ausgabe zufrieden gegeben. Um aber gut lesbaren Code zu schreiben genügt dies nicht.

Wir erinnern uns an die von uns verwendenten C++ und Arduino-bezogenen Ausgabeformate ...

```cpp        c++output.cpp
#include <iostream>
#include <iomanip>

int main(){
  std::cout<<std::setbase(16)<< std::fixed<<55<<std::endl;
  std::cout<<std::setbase(10)<< std::fixed<<55<<std::endl;
  int a = 15;
  std::cout<<std::setbase(10)<< std::fixed<<55 + a <<std::endl;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


```cpp       ArduinoSerial.cpp
void setup() {
    Serial.begin(9600);

    // Variante 1: print / println Methoden von Serial
    Serial.println("Das ist ein Test");

    float gleitkommaZahl = 3.123456;
    Serial.print(gleitkommaZahl, 4); //liefert 3.1234
    Serial.print(" ");
    Serial.println(gleitkommaZahl, 6); //liefert 3.123456

    Serial.print(15, BIN); //liefert den Wert 1111
    Serial.print(" ");
    Serial.print(15, HEX); //liefert den Wert f
    Serial.print(" ");
    Serial.println(15, OCT); //liefert den Wert 17

    // Variante 2: sprintf Formatierte Ausgabe
    int zahl = 65;
    char buffer[100];
    sprintf(buffer, "Dezimal %05i Dezimal %5i Hexadezimal %x Character %c", zahl, zahl , zahl, zahl);
    Serial.println(buffer); 
}

void loop() {
}
```
@AVR8js.sketch

> Die für den Arduino gezeigte Variante mit `sprintf` oder ``printf` funktioniert natürlich auch unter C++ generell. Aus didaktischen Gründen wurde aber die `cout` Variante vorrangig genutzt. 

****************************************************************************************

                                    {{1-2}}
****************************************************************************************


Die Ausgabe in Python ist außerordentlich konfigurierbar. Man unterscheidet zwischen 

1. der `printf` motivierten Ausgabe mit dem String modulo operator (`%`)  und 
2. den Ausgaben mit `format()`
3. den `f-strings`.

`print` folgt dem Muster `%[flags][width][.precision]type` für die Spezifikation der Ausgabe. Die zugehörige Verwendung unter Python stellt sich wie folgt dar:

```python     prinf.py
print("Total students : %3d, Fak. 3 : %2d" % (80, 65))
print("Total students : %-5d, Fak. 3 : %05d" % (80, 65))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


`f-strings` integrieren eigenen Code direkt in die Ausgabe - dies reicht von der einfachen Benennung einer Variablen, über Operationen mit Variablen bis hin zu Bedingungen und Funktionsaufrufen.

```python
num1 = 83
num2 = 9
print(f"The product of {num1} and {num2} is {num1 * num2}.")

print(f"{num1} and {num2} are equal - {True if num1 == num2 else False}.")
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

****************************************************************************************
          
# Quiz
## Elemente der Programmiersprache
> Welche Programmierparadigmen unterstützt Python?
[[X]] Imperativ
[[X]] Prozedural
[[X]] Objektorientiert

### Zuweisung und Datentypen
> Der Variable `d` soll erstmalig der Wert `3.14` zugewiesen werden. Welche Umsetzung ist korrekt?
[( )] `float d = 3.14;`
[( )] `float d = 3.14`
[( )] `d = 3.14;`
[(X)] `d = 3.14`
[( )] `int d = 3.14;`

{{1}}
************************************************************************
> Sie haben der Variable `d` soeben erfolgreich `3.14` zugewiesen. Ist es möglich der Variable `d` nun einen Wert von einem anderen Datentyp zuzuweisen?
[(X)] Ja
[( )] Nein
************************************************************************

{{2}}
************************************************************************
> Wie können die Werte von den Variablen `x` und `y` in einer Zeile getauscht werden? Geben Sie die Lösung ohne Leerzeichen an.
[[x,y=y,x]]
<script>
let input = "@input".trim()

input == "x,y=y,x" || input == "y,x=x,y"
</script>
************************************************************************

{{3}}
************************************************************************
> Welche der folgenden Operatoren existieren in Python?
[[ ]] `++`
[[X]] `+`
[[X]] `-`
[[X]] `/`
[[X]] `+=`
[[X]] `*=`
[[ ]] `--`
************************************************************************

### Standard Datentypen
> Welche dieser beispielhaft angegebenen Datentypen existieren in Python?
[[X]] tupel
[[X]] dictionary
[[X]] set
[[X]] list
[[X]] None
[[X]] float
[[X]] int
[[X]] string
[[X]] complex

### Ausgabe
> Mit welcher Funktion können Konstanten und Variablen in Python in der Konsole ausgegeben werden?
[[print]]
<script>
let input = "@input".trim()

input == "print" || input == "print()" || input == "print ()"
</script>

{{1}}
************************************************************************
> Mit welchem Parameter kann der standardmäßige Zeilenumbruch nach der Ausgabe mit `print` durch andere Zeichen ersetzt werden?
[[end]]
<script>
let input = "@input".trim()

input == "end" || input == "end=" || input == "end ="
</script>
************************************************************************

### Eingabe
> Mit welcher Funktion können String-Variablen in Python in der Konsole eingegeben werden?
[[input]]
<script>
let input = "@input".trim()

input == "input" || input == "input()" || input == "input ()"
</script>

{{1}}
************************************************************************
> Liefert dieses Programm einen Fehler?
```python
x = input("x eingeben:")
y = x**2
print("y = ", y)
```
[(X)] Ja
[( )] Nein
************************************************************************

### Zusätzliche Module einbinden
> Mit welchem Schlüsselwort werden Module in Python eingebunden?
- [( )] `using`
- [(X)] `import`
- [( )] `#include`

{{1}}
************************************************************************
> Wodurch muss `[_____]` ersetzt werden, um `Pi` aus dem eingebundenen Modul `math` auszugeben?
```python
import math as m

print([_____].pi)
```
[[m]]
************************************************************************

{{2}}
************************************************************************
> Wodurch muss `[_____]` ersetzt werden um `Pi` aus dem eingebundenen Modul `math` auszugeben?
```python
from math import *

print([_____])
```
[[pi]]
************************************************************************

### Listen
> Wodurch muss `[_____]` ersetzt werden um die Länge der Liste `l` auszugeben?
```python
l = ['r', 6, 8.0]
print([_____](l))
```
[[len]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms? Geben Sie die Antwort ohne eckige Klammern oder Leerzeichen an.
```python
liste = [1, 7]

liste.append(2)
liste.sort()
liste.reverse()
liste.extend([5,6])
liste.remove(1)

print(liste)
```
[[7,2,5,6]]
************************************************************************

### Listen-Indizierung
> Wie lautet die Ausgabe dieses Programms?
```python
data = ['a', 'b', 'c', 'd', 'e', 'f']
print(data[2])
```
[[c]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms? Geben Sie die Antwort ohne eckige Klammern oder Leerzeichen an.
```python
data = ['a', 'b', 'c', 'd', 'e', 'f']
l = []
l.extend(data[-2])
l.extend(data[3:])
l.extend(data[-4:])
l.extend(data[::2])
print(l)
```
[[e,d,e,f,c,d,e,f,a,c,e]]
************************************************************************

## Kontrollstrukturen
### Selektion mit `if`
> Wie viele `elif` Zweige darf es maximal in einer `if`-Anweisung geben?
[( )] 0
[( )] 1
[(X)] beliebig viele

{{1}}
************************************************************************
> Wie viele `else` Zweige darf es maximal in einer `if`-Anweisung geben?
[( )] 0
[(X)] 1
[( )] beliebig viele
************************************************************************

{{2}}
************************************************************************
> Wodurch müssen die `[_____]` ersetzt werden?
```python
a = 3.4
if a > 9[_____]
  print('A')
else[_____]
  print('B')

print('C')
```
[[:]]
************************************************************************

{{3}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
a = 3.4
if a > 9:
  print('A')
elif a > 2:
  print('B')
else:
  print('C')
```
[[B]]
************************************************************************

{{4}}
************************************************************************
> Worauf muss bei verschachtelten `if`-Anweisungengen geachtet werden?
[( )] Die innere Anweisung muss in eckigen Klammern stehen
[( )] Alle beteiligten Anweisungen müssen einen `else`-Zweig enthalten
[(X)] Auf die richtige Einrückung aller Zweige der inneren Anweisung
************************************************************************

{{5}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
a = 3.4
if a > 9:
  print('A')
elif a > 2:
  if a < 3:
    print('B')
  else:
    print('C')
else:
  print('D')
```
[[C]]
************************************************************************

### `while`-Schleife
> Wodurch muss `[_____]` ersetzt werden?
```python
while True[_____]
  print('Und nochmal...')
```
[[:]]

### `for`-Schleife
> Wie lautet die Ausgabe dieses Programms?
```python
for x in [7, 8, 9]:
  print(x, end=",")
```
[[7,8,9,]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
for x in "Hallo":
  print(x, end="o")
```
[[Hoaololooo]]
************************************************************************

{{2}}
************************************************************************
> Was gibt die `range`-Funktion zurück?
[( )] Den Abstand zwischen zwei Punkten
[( )] Eine Liste von Integer-Werten
[(X)] Ein in die Liste von Integer-Werten konvertierbares `range`-Objekt
************************************************************************

{{3}}
************************************************************************
> Welche Parameter der `range`-Funktion sind optional?
[[X]] start
[[ ]] stop
[[X]] step
************************************************************************

{{4}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
for x in range(4):
  print(x, end=",")
```
[[0,1,2,3,]]
************************************************************************

{{5}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
for x in range(1,5):
  print(x, end=",")
```
[[1,2,3,4,]]
************************************************************************

{{6}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
for x in range(5,-1,-1):
  print(x, end=",")
```
[[5,4,3,2,1,0,]]
************************************************************************

### Schleifen oder List Comprehension
> Wie lautet die Ausgabe dieses Programms? Bitte geben Sie die Lösung ohne eckige Klammern oder Leerzeichen an.
```python
a = [x*2 for x in range(5)]
print(a)
```
[[0,2,4,6,8]]

{{1}}
************************************************************************
> Wie lautet die Ausgabe dieses Programms? Bitte geben Sie die Lösung ohne eckige Klammern oder Leerzeichen an.
```python
a = [0,1,2,3,4]
print([x*2 if x <= 2 else x for x in a])
```
[[0,2,4,3,4]]
************************************************************************
                   
