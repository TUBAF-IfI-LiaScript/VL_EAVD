<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

comment:  This is a very simple comment.
          Multiline is also okay.

translation: English   translation/english.md

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s.replace(/\n/g, "<br>");}}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);
    var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
    var info = log[1] + " " + log[4];

    if (info.length > 80)
      info = info.substring(0,76) + "..."

    error.add_detail(0, info, "error", log[2]-1, log[3]);

    throw error;
  }
</script>
@end

-->

# Vorlesung III - Operatoren

**Fragen an die heutige Veranstaltung ...**

+


**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

|Standard    | Schlüsselwörter |
|:----------|:-----------|:-----------|:-----------|:------------|:-----------|:------------|
| C89/C90    | auto | <span style="color:blue">double</span> | <span style="color:blue">int</span> | struct | break|
|           | else  | <span style="color:blue">long</span> | switch | case | enum |
|           | register | typedef | <span style="color:blue">char</span> | extern | return |
|           | union | const | <span style="color:blue">float</span> | <span style="color:blue">short</span> | <span style="color:blue">unsigned</span>  |
|           | continue | for | <span style="color:blue">signed</span> | <span style="color:blue">void</span> | default |
|           | goto | sizeof | volatile | do | if |
|           | static |  while|
| C99  | _Bool | _Complex | _Imaginary | inline | restrict |
| C11  | _Alignas | _Alignof | _Atomic | _Generic |  _Noreturn|
|      |_Static\_assert | \_Thread\_local|

Standardbibliotheken

|Name       | Bestandteil| Funktionen                           |
|:----------|:-----------|:-------------------------------------|
|<stdio.h> 	|            | Input/output (printf)                |
|<stdint.h> |(seit C99)  | Integer Datentypen mit fester Breite |
|<float.h> 	|            | Parameter der Floatwerte             |
|<limits.h> |            | Größe der Basistypen                 |

https://en.cppreference.com/w/c/header

## 0. Wiederholung

**Warnings mit PellesC**

Bilder zur Konfiguration mit folgendem beispiel

```cpp                     Pointer.c
#include<stdio.h>

int main() {
  unsigned int v = -5;
  printf("%u\n", v);
	return 0;
}
```

Hinweis: *Unterschiedliche Compiler verwenden unterschieldliche Konfigurationen und generieren unterschiedliche Ergebnisse!*

| Name            | Bezeichnung                                 |
|:----------------|:--------------------------------------------|
| Gnu C Compiler  | Linux "Standard" C Compiler (auch in cygwin)|
|                 | [Dokumentation](https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html)|
|                 | [Erläuterung zu den Warning Konfigurationen](https://kristerw.blogspot.com/2017/09/useful-gcc-warning-options-not-enabled.html) |
| LLC (in PellesC) | `Local C Compiler` or `Little C Compiler`   |
|                 | [Dokumentation](https://sites.google.com/site/lccretargetablecompiler/lccmanpage) |
| Microsoft Compiler | enthalten im Microsoft Studio              |
|                    | [Dokumentation](https://msdn.microsoft.com/de-de/library/19z1t1wy.aspx) |

### Zahlenliterale

**Ganzzahlenliterale**

`Variable = (Vorzeichen)(Zahlensystem)[Wert](Typ);`

| Literal  |  Bedeutung                |
|:---------|:--------------------------|
| 345      | Ganzzahl 345 vom Typ `int`  |
| -234L     | Ganzzahl 234 vom Typ `signed long` |
| 100000000000 | Ganzahl vom Typ `long`  |
| 011       | Ganzzahl also oktale Zahl (Wert $9_d$) |
| 0x12      | Ganzzahl ($18_d$) |

**Gleitkommazahlenliterale**

| Literal  |  Bedeutung                |
|:---------|:--------------------------|
| 123.34f   | Fließkommazahl vom Typ `float` |
| 0.132     | Fließkommazahl vom Typ `double` |
| 132e-3    | |
| .132      | |

### Scanf Beispiel

hier fehlt es noch

## 1. Zusammengesetzte Datentypen

enum


## 2. Operatoren

> Ein Ausdruck ist eine Kombination aus Variablen, Konstanten, Operatoren und Rückgabewerten von Funktionen. Die Auswertung eines Ausdrucks ergibt einen Wert.

**Zahl der beteiligten Operationen**

Man unterscheidet in der Sprache C *unäre*, *binäre* und *ternäre* Operatoren

| Operator           | Operanden | Beispiel                |
|:-------------------|:----------|:------------------------|
| Unäre Operatoren   | 1         | `&` Adressoperator      |
|                    |           | `sizeof` Größenoperator |
| Binäre Operatoren  | 2         | `+`, `-`, `%`           |
| Ternäre Operatoren | 3         | `?` Bedingungsoperator  |

Es gibt auch Operatoren, die, je nachdem wo sie stehen, entweder unär oder binär sind. Ein Beispiel dafür ist `-`, dass ein Vorzeichen (unär) und arithmetische Operationen (binär) repräsentieren kann.

**Position**

Des Weiteren wird unterschieden, welche Position der Operator einnimmt:

+ *Infix* – der Operator steht zwischen den Operanden.
+ *Präfix* – der Operator steht vor den Operanden.
+ *Postfix* – der Operator steht hinter den Operanden.

Wiederum können `+` und `-` alle drei Rollen einnehmen:

```cpp
a = b + c; // Infix
a = -b;    // Präfix
a = b ++;  // Postfix
```

**Funktion**

+ Arithmetische Operatoren
+ Logische Operatoren
+ ...


** Assoziativität ?????? **


```cpp                     Pointer.c
#include <stdio.h>

int main(void) {
   int zahl1 = 10;
   int zahl2 = 20;
   int ergeb;

   // Möglichkeit 1: eigenstaendige Berechnung
   ergeb = zahl1 + zahl2;
   printf("%d + %d = %d\n", zahl1, zahl2, ergeb);

   // Möglichkeit 2: mit Anzeige und Berechnung am Ende der
   // printf'-Anweisung
   printf("%d * %d = %d\n", zahl1, zahl2, zahl1*zahl2);

   return 0;
}
```
@JSCPP(@input, )


### Arithmetische Operatoren

#### Inkrement und Dekrement

Mit den ++ - und -- -Operatoren kann ein L-Wert um eins erhöht bzw. um eins vermindert werden. Man bezeichnet die Erhöhung um eins auch als Inkrement, die Verminderung um eins als Dekrement. Ein Inkrement einer Variable x entspricht x = x + 1, ein Dekrement einer Variable x entspricht x = x - 1.

```cpp                            IncrementDecrement.c
#include <stdio.h>

int main(){
  int x, result;
  x = 15;
  result = ++x;   // Gebrauch als Präfix
  printf("x=%d und result=%d\n",x, result);
  result = x++;   // Gebrauch als Postfix
  printf("x=%d und result=%d\n",x, result);
  return 0;
}
```
@JSCPP(@input, )

Welche Variante sollte ich benutzen, wenn ich einfach nur eine Variable inkrementieren möchte?

```cpp                            IncrementDecrement.c
#include <stdio.h>

int main(){
  int x = 15;
  x++;              // Variante I
  printf("x=%d \n",x);
  ++x;              // Variante II
  printf("x=%d \n",x);
  return 0;
}
```
@JSCPP(@input, )

In C ist die Wahl beliebig, in C++ sollte immer die Präfixvariante genutzt werden. Siehe die Diskussion unter [stackoverflow](https://stackoverflow.com/questions/24886/is-there-a-performance-difference-between-i-and-i-in-c) und Scott Meyer "More Effective C++".

#### Shift-Operationen

Die Operatoren `<<` und `>>` dienen dazu, den Inhalt einer Variablen bitweise um 1 nach links bzw. um 1 nach rechts zu verschieben.

```cpp                            IncrementDecrement.c
#include <stdio.h>

// diese Funktion dient nur der Visualisierung
// Zahl in binaerer Form als char array
int bin(const char *input) {
    int pos = 0;
    int val = 0;
    while (input[pos]) {
    	val <<=1;
    	val |= (input[pos] - '0') & 0x1;
    	pos++;
    }
    return val;
}

int main(){
  int x = 15;
  char [15] output;
  printf("x=%s \n",output);
  return 0;
}
```
@JSCPP(@input, )

100000000
00000000
00000000
00010001

| Operator | Bedeutung         | Ganzzahl     | Gleitkomma |
|:---------|:------------------|:-------------|:-----------|
| +        | Additon           | x            | x          |
| -        | Subtraktion       | x            | x          |
| \*        | Multiplikation    | x            | x          |
| /        | Division          | x (Ganzzahl) | x          |
| %        | Modulo (Rest einer Division) | x       |        |

### Logische Operatoren


#### Vorrangregeln









## Beispiel des Tages




```cpp                     printbinaries.c
#include<stdio.h>

int int2binOutput(int n) {
  int i;
  for(i= (sizeof n) * 8 -1; i>=0; i--) {
      if ((n >> i) & 1)
          printf("1");
      else
          printf("0");
      if (i % 8 == 0)
          printf(" ");
  }
  printf("\n");
}

int main(){
  int x = 254;
  int2binOutput(x);
  return 0;
}
```
@JSCPP(@input, )
