<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md
-->

# Vorlesung III - Operatoren

**Fragen an die heutige Veranstaltung ...**

* Wonach lassen sich Operatoren unterscheiden?
* Welche unterschiedliche Bedeutung haben `x++` und `++x`?
* Erläutern Sie den Begriff unärer, binärer und tertiärer Operator.
* Unterscheiden Sie Zuweisung und Anweisung.
* Was bedeutet rechtsassoziativ und linksassoziativ?
* Welche Funktion erfüllen Bit-Operationen?
* Wie werden Shift-Operatoren genutzt?
* Wie können boolsche Variablen in C ausgedrückt werden?

---------------------------------------------------------------------
Hier geht es zur interaktiven Version des Kurses [LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/CCourse/master/03_Operatoren.md#1)

---------------------------------------------------------------------
{{1}}
**Wie weit sind wir schon gekommen?**

{{1}}
ANSI C (C89)/ Schlüsselwörter:

{{1}}
| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | `auto`         | `double` | `int`      | struct   | break      |
|             | else           | `long`   | switch     | case     | enum       |
|             | `register`     | typedef  | `char`     | `extern` | return     |
|             | union          | `const`  | `float`    | `short`  | `unsigned` |
|             | continue       | for      | `signed`   | `void`   | default    |
|             | goto           | `sizeof` | `volatile` | do       | if         |
|             | static         | while    |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | inline   | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

{{1}}
Standardbibliotheken

{{1}}
| Name         | Bestandteil | Funktionen                           |
|:-------------|:------------|:-------------------------------------|
| `<stdio.h>`  |             | Input/output                         |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite |
| `<float.h>`  |             | Parameter der Floatwerte             |
| `<limits.h>` |             | Größe der Basistypen                 |

    {{1}}
[C standard library header files](https://en.cppreference.com/w/c/header)


## 2. Operatoren

> Ein Ausdruck ist eine Kombination aus Variablen, Konstanten, Operatoren und
> Rückgabewerten von Funktionen. Die Auswertung eines Ausdrucks ergibt einen
> Wert.

**Zahl der beteiligten Operationen**

Man unterscheidet in der Sprache C *unäre*, *binäre* und *ternäre* Operatoren

| Operator           | Operanden | Beispiel                |
|:-------------------|:---------:|:------------------------|
| Unäre Operatoren   |     1     | `&` Adressoperator      |
|                    |           | `sizeof` Größenoperator |
| Binäre Operatoren  |     2     | `+`, `-`, `%`           |
| Ternäre Operatoren |     3     | `?` Bedingungsoperator  |

Es gibt auch Operatoren, die, je nachdem wo sie stehen, entweder unär oder binär
sind. Ein Beispiel dafür ist der `-`-Operator, der ein Vorzeichen (unär) und
eine arithmetische Operation (binär) repräsentieren kann.

**Position**

Des Weiteren wird unterschieden, welche Position der Operator einnimmt:
* *Infix* – der Operator steht zwischen den Operanden.
* *Präfix* – der Operator steht vor den Operanden.
* *Postfix* – der Operator steht hinter den Operanden.

`+` und `-` können alle drei Rollen einnehmen:

```cpp
a = b + c; // Infix
a = -b;    // Präfix
a = b++;   // Postfix
```

{{1}}
**Assoziativität**  

{{1}}
|Linksassoziativ  | Auswertung von links nach rechts |
|Rechtsassoziativ | Auswertung von rechts nach links |

    {{2}}
**Funktion**

    {{2}}
* Zuweisung
* Arithmetische Operatoren
* Logische Operatoren
* Bit-Operationen
* Bedingungsoperator


### Zuweisungsoperator

Der Zuweisungsoperator `=` ist von seiner mathematischen Bedeutung zu trennen -
einer Variablen wird ein Wert zugeordnet. Damit macht dann auch `x=x+1` Sinn.

```cpp                     Pointer.c
#include <stdio.h>

int main() {
   int zahl1 = 10;
   int zahl2 = 20;
   int ergeb;
   // Zuweisung des Ausdrucks 'zahl1 + zahl2'
   ergeb = zahl1 + zahl2;

   printf("%d + %d = %d\n", zahl1, zahl2, ergeb);
   return 0;
}
```
  @Rextester.C

Die Zuweisungsoperation ist rechtsassoziativ. Der Ausdruck wird von rechts nach
links ausgewertet.

```cpp                     AssociationDirection.c
#include <stdio.h>

int main() {
  int a, b;
  a = 5;
  a = b = a + 1;
  printf("a = %d, b=%d\n", a, b);
}
```
  @Rextester.C

{{1}}
> **Achtung:** Verwechseln Sie nicht den Zuweisungsoperator `=` mit dem
> Vergleichsoperator `==`. Der Compiler kann die Fehlerhaftigkeit kaum erkennen
> und generiert Code, der ein entsprechendes Fehlverhalten zeigt.

{{1}}
```cpp                            EqualSign.c
#include <stdio.h>

int main(){
  int x, y;
  x = 15;             // Zuweisungsoperator
  y = x = x + 5;
  printf("x=%d und y=%d\n",x, y);

  y = x == 20;        // Gleichheitsoperator
  printf("x=%d und y=%d\n",x, y);
  return 0;
}
```
@Rextester.C

### Inkrement und Dekrement

Mit den `++` und `--` -Operatoren kann ein L-Wert um eins erhöht bzw. um
eins vermindert werden. Man bezeichnet die Erhöhung um eins auch als Inkrement,
die Verminderung um eins als Dekrement. Ein Inkrement einer Variable `x`
entspricht `x = x + 1`, ein Dekrement einer Variable `x` entspricht `x = x - 1`.

```cpp                            IncrementDecrement.c
#include <stdio.h>

int main(){
  int x, result;
  x = 5;
  result = 2 * ++x;   // Gebrauch als Präfix
  printf("x=%d und result=%d\n",x, result);
  result = 2 * x++;   // Gebrauch als Postfix
  printf("x=%d und result=%d\n",x, result);
  return 0;
}
```
@Rextester.C

Welche Variante sollte ich benutzen, wenn ich einfach nur eine Variable
inkrementieren möchte?

In C ist die Wahl beliebig, in C++ sollte immer die Präfixvariante genutzt
werden. Siehe die Diskussion unter
[stackoverflow](https://stackoverflow.com/questions/24886/is-there-a-performance-difference-between-i-and-i-in-c)
und Scott Meyer "More Effective C++".

### Binäre arithmetische Operatoren

| Operator | Bedeutung                    | Ganzzahlen   | Gleitkommazahlen |
|:--------:|:-----------------------------|:-------------|:-----------|
| `+`      | Additon                      | x            | x          |
| `-`      | Subtraktion                  | x            | x          |
| `*`      | Multiplikation               | x            | x          |
| `/`      | Division                     | x            | x          |
| `%`      | Modulo (Rest einer Division) | x            |            |

```cpp                            calcExamples.c
#include <stdio.h>

int main(){
  int zahl1,zahl2;
  int ergeb;
  zahl1=10;
  zahl2=20;
  printf("Zahl 1= %d\n",zahl1);
  printf("Zahl 2= %d\n",zahl2);

  // Moeglichkeit 1: zuerst Berechnung, dann Ausgabe
  ergeb=zahl1+zahl2;
  printf("Summe der Zahlen:%d\n",ergeb);
  // Moeglichkeit 2: Berechnung direkt für die Ausgabe
  printf("%d - %d = %d\n", zahl1, zahl2, zahl1-zahl2);
  return 0;
}
```
@Rextester.C


{{1}}
> **Achtung:** Divisionsoperationen werden für Ganzzahlen und Gleitkommazahlen
> unterschiedlich realisiert.

{{1}}
* Wenn zwei Ganzzahlen wie z. B. $4/3$ dividiert werden, erhalten wir das
  Ergebnis 1 zurück, der nicht ganzzahlige Anteil der Lösung bleibt
  unbeachtet. Um diesen aber ggf. zu erfassen, kann der verbleibende Rest mit
  dem Modulo Operator `%` bestimmt werden.
* Für Fließkommazahlen wird die Division wie erwartet realisiert.  

{{1}}
```cpp                                  moduloExample.c
#include <stdio.h>

int main(){
  int timestamp, sekunden, minuten;

  timestamp = 345; //[s]
  printf("Zeitstempel %d [s]\n", timestamp);
  minuten=timestamp/60;
  sekunden=timestamp%60;
  printf("Besser lesbar = %d min. %d sek.\n", minuten, sekunden);
  return 0;
}
```
@Rextester.C

{{1}}
> **Achtung:** Der Rechenoperator Modulo mit dem `%` Zeichen hat nichts mit dem
> Formatierungszeichen in `printf("%d")` und `scanf("%f")` zu tun.

{{2}}
Die arithmetischen Operatoren lassen sich in verkürzter Schreibweise wie folgt
darstellen:

{{2}}
| Operation | Bedeutung                    |
|:---------:|:-----------------------------|
|   `+=`    | `a+=b` äquivalent zu `a=a+b` |
|   `-=`    | `a-=b` äquivalent zu `a=a-b` |
|   `*=`    | `a*=b` äquivalent zu `a=a*b` |
|   `/=`    | `a/=b` äquivalent zu `a=a/b` |
|   `%=`    | `a%=b` äquivalent zu `a=a%b` |

{{2}}
```cpp             shortenedOperators.c
#include <stdio.h>

int main() {
   int x=2, y=4, z=6;
   printf("x=%d y=%d z=%d\n", x, y, z);

   printf("x = x+y =%d\n", x+=y);
   printf("z = z+y =%d\n", z+=y);
   printf("z = z+x =%d\n", z+=x);
   printf("x=%d y=%d z=%d\n", x, y, z);
   return 0;
}
```
@Rextester.C

{{2}}
> **Achtung:** Verlieren Sie bei langen Berechnungsketten nicht den Überblick!
> Insbesondere die verkürzte Schreibweise forciert dies.

### Logische Operatoren

Kern der Logik sind Aussagen, die wahr oder falsch sein können.


| Operation | Bedeutung           |
|:---------:|:--------------------|
|    `<`    | kleiner als         |
|    `>`    | größer als          |
|   `<=`    | kleiner oder gleich |
|   `>=`    | größer oder gleich  |
|   `==`    | gleich              |
|   `!=`    | ungleich            |

```cpp                                       LogicOperators.c
#include <stdio.h>

int main(){
  int x = 15;
  printf("x = %d \n", x);
  printf("Aussage x > 5 ist %d \n", x > 5);
  printf("Aussage x == 5 ist %d \n", x == -15);
  return 0;
}
```
@Rextester.C

{{1}}
Und wie lassen sich logische Aussagen verknüpfen?

{{1}}
| Operation | Bedeutung |
|:---------:|:----------|
|   `&&`    | UND       |
|   `||`    | ODER      |
|   `!`     | NICHT     |

{{1}}
```cpp                                       Logic.c
#include <stdio.h>
//typedef int bool;
//#define true 1
//#define false 0

int main(){
  int x = 15;
  // Hier folgt eine logische Aussage in Abhaengigkeit von
  // deren Aussage die Ausgabe erfolgt
  //    |
  //    v
  if (x > 5 && x<20) {
    printf("Aussage ist wahr!\n");
  }else{
    printf("Aussage ist falsch!\n");
  }
  return 0;
}
```
@Rextester.C

{{1}}
Anmerkung: Seit dem C99-Standard finden Sie in der Headerdatei `<iso646.h>`
einige Makros `and`, `or`, `xor`, die Sie als alternative Schreibweise für
logische Operatoren und Bit-Operatoren nutzen können.

### Bit-Operationen

Bitoperatoren verknüpfen logische Aussagen oder manipulieren einzelne Bits in
binären Zahlendarstellungen.

| Operation   | Bedeutung            |
|:------------|:---------------------|
| `&`, `&=`   | bitweises und        |
| `|`, `|=`   | bitweises oder       |
| `^`, `^=`   | bitweises xor        |
| `~`         | bitweises Komplement |

Bei der hardwarenahen Programmierung gilt es häufig Konfigurationen von
Komponenten des Prozessors über einzelne Bits zu setzen oder auszulesen.

**Auslesen**

Im Beispiel sehen Sie ein fiktives Konfigurationsregister eines Analog-Digital-Wandlers

| 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
|:-----|:-----|:-----|:-----|:-----|:-----|:-----|:-----|
| XXXX | 8Bit Ausgabe | 10Bit Ausgabe | Loop Modus | XXXX | Start Wandlung | Wandlung Fertig | XXXX |

|7 |XXXX            |
|6 |8 Bit Ausgabe   |
|5 |10 Bit Ausgabe  |
|4 |Loop Modus      |
|3 |XXXX            |
|2 |Start Wandlung  |
|1 |Wandlung Fertig |
|0 |XXXX            |

{{1}}
Wie können wir die Wandlung starten, sprich das 3. Bit setzen?

{{1}}
```cpp                                       Logic.c
#include <stdio.h>

int main(){
  int x = 64;  //'0b01000000'
  // Here we need some magic ...
  if (x == 68)
    printf("Wandlung gestartet!\n");
  else
    printf("Nein, das passte nicht!\n");
  return 0;
}
```
@Rextester.C

{{2}}
Der Analog-Digital-Wandler wurde gestartet, nun wollen wir prüfen, ob die
Wandlung abgeschlossen ist. Wie können wir auslesen, ob das 2. Bit (Wandlung
Fertig) gesetzt ist?

{{2}}
```cpp                                       Logic.c
#include <stdio.h>

int main(){
  int x = 66;  //'0b01000010'
  printf("Pruefe ADC-Status ... \n");
  if (0) // Here we need some magic ...
    printf("Wandlung beendet!\n");
  else
    printf("Irgendwas stimmt nicht!\n");
  return 0;
}
```
@Rextester.C

{{2}}
Anmerkung: Üblicherweise würde man keine "festen" Werte für die set und test
Methoden verwenden. Vielmehr werden dafür durch die Hersteller entsprechende
Makros bereitgestellt, die eine Portierbarkeit erlauben.

{{3}}
**Unterschied zu den logischen Operatoren**

{{3}}
```cpp                     ArrayExample.c
#include <stdio.h>

int main() {
  if (1 && 2) printf("Aussage 1 ist wahr\n");
  else printf("Aussage 1 ist falsch\n");
  if (1 & 2) printf("Aussage 2 ist wahr\n");
  else printf("Aussage 2 ist falsch\n");
  return 0;
}
```
@Rextester.C

{{3}}
| Operator | Bedeutung         | Rückgabewert  |
|:---------|:------------------|---------------|
| `&&`     | logischer *und* - Operator | {0,1}  |
|          | Ganzzahlen ungleich "0" werden als *wahr* interpretiert, "0" als *falsch* |  |
| `&`      | bitweiser *und* -  Operator | `int`  |
|          | Sofern eine Übereinstimmung an einer Stelle auftritt, ergibt sich die zugehörige Ganzzahl als Ergebnis. |  |


### Shift Operatoren

Die Operatoren `<<` und `>>` dienen dazu, den Inhalt einer Variablen bitweise um
einige Stellen nach links bzw. nach rechts zu verschieben.

```cpp                            IncrementDecrement.c
#include <stdio.h>

int main(){
  printf("%d \n", 15 << 1);
  return 0;
}
```
@Rextester.C

Und wozu braucht man das? Zum einen beim Handling einzelner Bits, wie es heute
beim *Beispiel des Tages* gezeigt wird. Zum anderen zur Realisierung von
Multiplikations- und Divisionsoperationen mit Faktoren/Divisoren $2^n$.

```cpp                            Bit_Test.c
int Bit_Test(BYTE val, BYTE bit) {
   BYTE test_val = 0x01;    /* dezimal 1 / binär 0000 0001 */
   /* Bit an entsprechende Pos. schieben */
   test_val = (test_val << bit);
   /* 0=Bit nicht gesetzt; 1=Bit gesetzt */
   if ((val & test_val) == 0)
      return 0;      /* nicht gesetzt */
   else
      return 1;      /* gesetzt */
}
```

### Bedingungsoperator

Der Bedingungsoperator liefert in Abhängigkeit von der Gültigkeit einer
logischen Aussage einen von zwei möglichen Ergebniswerten zurück. Folglich hat
er drei Operanden:

* die Bedingung
* den Wert für eine gültige Aussage
* den Wert für eine falsche Aussage

```cpp
bedingung ? wert_wenn_wahr : wert_wenn_falsch
```

Die damit formulierbaren Anweisungen sind äquivalent zu `if`-Statements.

```cpp                     ConditionStatements.c
// Falls a größer als b ist, wird a zurückgegeben, ansonsten b.
if (a > b)
   return a;
 else
   return b;

// analog
return (a > b) ? a : b;
```

Aussagen mit dem Bedingungsoperator sind nicht verkürzte Schreibweise für
`if-else` Anweisungen. Es sind zwei offenkundige Unterschiede zu
berücksichtigen:

* Der Bedingungsoperator generiert einen Ergebniswert und kann daher z.B. in
  Formeln und Funktionsaufrufen verwendet werden.
* Bei `if`-Anweisungen kann der `else`-Teil entfallen, der Bedingungsoperator
  verlangt stets eine Angabe von beiden Ergebniswerten.

### `sizeof` - Operator

Der Operator `sizeof` ermittelt die Größe eines Datentyps (in Byte) zur
Kompiliertzeit.

* `sizeof` ist keine Funktion, sondern ein Operator.
* `sizeof` wird häufig zur dynamischen Speicherreservierung verwendet.

```cpp
#include <stdio.h>

int main(){
  double wert=0.0;
  printf("%ld %ld %ld\n", sizeof(0),sizeof(double),sizeof(wert));
return 0;
}
```
@Rextester.C


### Vorrangregeln

Konsequenterweise bildet auch die Programmiersprache C eigene Vorrangregeln ab,
die grundlegende mathematische Definitionen "Punktrechnung vor Strichrechnung"
realisieren. Die Liste der unterschiedlichen Operatoren macht aber weitere
Festlegungen notwendig.

**Prioritäten**

In welcher Reihung erfolgt beispielsweise die Abarbeitung des folgenden
Ausdruckes?

```cpp
 c = sizeof(x) + ++a / 3;
```

Für jeden Operator wurde eine Priorität definiert, die die Reihung der
Ausführung regelt.

[Liste der Vorrangregeln](https://de.wikibooks.org/wiki/C-Programmierung:_Liste_der_Operatoren_nach_Priorit%C3%A4t)

Im Beispiel bedeutet dies:

```cpp
c = sizeof(x) + ++a  / 3;
//    |       |  |   |
//    |       |  |   |--- Priorität 13
//    |       |  |--- Priorität 14
//    |       |--- Priorität 12
//    |--- Priorität 14

c = (sizeof(x)) + ((++a) / 3);
```
{{1}}
**Assoziativität**

{{1}}
Für Operatoren mit der gleichen Priorität ist die Reihenfolge (Assoziativität)
der Auswertung von Bedeutung.

{{1}}
```cpp
a = 4 / 2 / 2;

// von rechts nach links (FALSCH)
// 4 / (2 / 2)   // ergibt 4

// von links nach rechts ausgewertet
// (4 / 2) / 2   // ergibt 1
```

{{2}}
**Nebenwirkungen**

{{2}}
C-Programme können sogenannte Nebenwirkungen (engl. side effects) besitzen. Als
Nebenwirkungen bezeichnet man die Veränderung des Zustandes des Rechnersystems
durch das Programm. Diese Reihung der Realisierung ist teilweise undefiniert.

{{2}}
```c
x = a() + b() – c();
```


## Beispiel des Tages

Das folgende Codebeispiel realisiert die binäre Ausgabe einer Zahl in der
Konsole. Für die bessere Handhabung wurde die eigentliche Ausgabe in einer
eigenen Funktion `int2binOutput` organisiert. Dieser Funktion wird der
darzustellende Wert als Parameter `n` übergeben.

Zunächst wird ermittelt, wieviele Bits die Zahl umfasst. Natürlich ließe sich
hier auch ein fester Wert hinterlegen, garantiert aber eine weitgehende
Unabhänigkeit von der konkreten Architektur. Die binäre Zahlendarstellung muss
nun von vorn beginnend durchlaufen werden und geprüft werden, ob an dieser
Stelle eine 1 oder eine 0 steht. Dazu wird der Zahlenwert `i` mal nach rechts
geschoben und das dann niederwertigste Bit mit einer 1 verglichen (und-Operator
  `&`).
Sofern das Bit gleich eins ist, wird eine "1" ausgegeben, sonst eine "0".
Dieser Vorgang wird kontinuierlich für einen immer kleiner werdende Index `i`
ausgeführt, bis dieser 0 erreicht.

Um die Lesbarkeit zu steigern wird nach 8 Bit ein Leerzeichen eingefügt. Dazu
wird in Zeile 10 geprüft, ob die Division mit 8 einen Rest generiert.

```cpp                     printbinaries.c
#include<stdio.h>

void int2binOutput(int n) {
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
@Rextester.C
