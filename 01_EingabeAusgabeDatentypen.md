<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.1
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner


-->

# Grundlagen der Sprache C

Die interaktive Version des Kurses ist unter diesem [Link](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/01_EingabeAusgabeDatentypen.md#1) zu finden.

**Fragen an die heutige Veranstaltung ...**

* Durch welche Parameter ist eine Variable definiert?
* Erklären Sie die Begriffe Deklaration, Definition und Initialisierung im
  Hinblick auf eine Variable!
* Worin unterscheidet sich die Zahldarstellung von ganzen Zahlen (`int`) von den
  Gleitkommazahlen (`float`).
* Welche Datentypen kennt die Sprache C?
* Erläutern Sie für `char` und `int` welche maximalen und minimalen Zahlenwerte
  sich damit angeben lassen.
* Ist `printf` ein Schlüsselwort der Programmiersprache C?
* Welche Beschränkung hat `getchar`

> **Vorwarnung:** Man kann Variablen nicht ohne Ausgaben und Ausgaben nicht ohne
>Variablen erklären. Deshalb wird im folgenden immer wieder auf einzelne Aspekte
> vorgegriffen. Nach der Vorlesung sollte sich dann aber ein Gesamtbild ergeben.

## Zeichensätze

Sie können in einem C-Programm folgende Zeichen verwenden:

* Dezimalziffern

  `0 1 2 3 4 5 6 7 8 9`

* Buchstaben des englischen Alphabets

  `A B C D E F G H I J K L M N O P Q R S T U V W X Y Z`

  `a b c d e f g h i j k l m n o p q r s t u v w x y z`

* Grafiksymbole

  `!"%&/()[]{}\?='#+*~-_.:,`

  ```cpp                     SpecialSigns.c
  #include <stdio.h>

  int main() {
      printf("Einen schönen Tag für Sie!");
      //printf("Einen sch\x94nen Tag f\x81r Sie!");
      return 0;
  }
  ```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


## Variablen

> *Ein Rechner ist eigentlich ziemlich dumm, dass aber viele Millionen mal pro*
> *Sekunde*
>
>Zitat - Quelle gesucht!

```cpp                     Calculator.c
#include<stdio.h>

int main(void) {
  printf("%d",43 + 17);
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Unbefriedigende Lösung, jede neue Berechnung muss in den Source-Code integriert
und dieser dann kompiliert werden. Ein Taschenrechner wäre die bessere Lösung!

```cpp                     QuadraticEquation.c
#include<stdio.h>

int main(void) {
  int x;
  x = 5;
  printf("f(%d) = %d \n",x, 3*x*x + 4*x + 8);
  x = 9;
  printf("f(%d) = %d ",x, 3*x*x + 4*x + 8);
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
Ein Programm manipuliert Daten, die in Variablen organisiert werden.

{{1}}
Eine Variable ist ein **abstrakter Behälter** für Inhalte, welche im
Verlauf eines Rechenprozesses benutzt werden. Im Normalfall wird eine Variable
im Quelltext durch einen Namen bezeichnet, der die Adresse im Speicher
repräsentiert. Alle Variablen müssen vor Gebrauch vereinbart werden.

{{1}}
Mit `const` kann bei einer Vereinbarung der Variable festgelegt werden, dass
ihr Wert sich nicht ändert.

{{1}}
```c
const double e = 2.71828182845905;
```
{{1}}
Weiterer wenig verwendete Typqualifikator ist `volatile`. Er gibt an, dass der
Wert der Variable sich jederzeit z. B. durch andere Prozesse ändern kann.

{{2}}
Kennzeichen einer Variable:

{{2}}
1. Name
2. Datentyp
3. Wert
4. Adresse
5. Gültigkeitraum


### Zulässige Variablennamen

Der Name kann Zeichen, Ziffern und den Unterstrich enthalten. Dabei ist zu
beachten:

* Das erste Zeichen muss ein Buchstabe sein, der Unterstrich ist auch möglich.
* C betrachte Groß- und Kleinschreibung - `Zahl` und `zahl` sind also
  unterschiedliche Variablennamen.
* Schlüsselworte (`auto`, `goto`, `return`, etc.) sind als Namen unzulässig.

| Name            | Zulässigkeit                                   |
|:----------------|:-----------------------------------------------|
| `gcc`           | erlaubt                                        |
| `a234a_xwd3`    | erlaubt                                        |
| `speed_m_per_s` | erlaubt                                        |
| `double`        | nicht zulässig (Schlüsselwort)                 |
| `robot.speed`   | nicht zulässig (`.` im Namen)                  |
| `3thName`       | nicht zulässig (Ziffer als erstes Zeichen)     |
| `x y`           | nicht zulässig (Leerzeichen im Variablennamen) |

```cpp                     QuadraticEquation.c
#include<stdio.h>

int main(void) {
  int return = 5;
  printf("Unsere Variable hat den Wert %d \n", x);
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

> Vergeben Sie die Variablennamen mit Sorgfalt. Für jemanden der Ihren Code liest, sind diese wichtige Informationsquellen!
> [Link](https://wiki.c2.com/?BadVariableNames)

Neben der Namensgebung selbst unterstützt auch eine entsprechende Notationen die Lesbarkeit. In Programmen sollte ein Format konsistent verwendet werden.

| Bezeichnung            | denkbare Variablennamen                            |
|:---------------------- |:-------------------------------------------------- |
| CamelCase (upperCamel) | `YouLikeCamelCase`, `HumanDetectionSuccessfull`    |
|           (lowerCamel) | `youLikeCamelCase`, `humanDetectionSuccessfull`    |
| underscores            | `I_hate_Camel_Case`, `human_detection_successfull` |

In der Vergangenheit wurden die Konventionen (zum Beispiel durch Microsoft "Ungarische Notation") verpflichtend durchgesetzt. Heute dienen eher die generellen Richtlinien des Clean Code in Bezug auf die Namensgebung.

### Datentypen

Welche Informationen lassen sich mit Blick auf einen Speicherauszug im Hinblick
auf die Daten extrahieren?

{{0-1}}
| Adresse | Speicherinhalt |
|         | binär          |
| 0010    | 0000 1100      |
| 0011    | 1111 1101      |
| 0012    | 0001 0000      |
| 0013    | 1000 0000      |

{{1-2}}
| Adresse | Speicherinhalt | Zahlenwert |
|         |                |  (Byte)    |
| 0010    | 0000 1100      | 12         |
| 0011    | 1111 1101      | 253 (-3)   |
| 0012    | 0001 0000      | 16         |
| 0013    | 1000 0000      | 128 (-128) |

{{2}}
| Adresse | Speicherinhalt | Zahlenwert | Zahlenwert | Zahlenwert   |
|         |                |  (Byte)    | (2 Byte)   | (4 Byte)     |
| 0010    | 0000 1100      | 12         |            |              |
| 0011    | 1111 1101      | 253 (-3)   | 3325       |              |
| 0012    | 0001 0000      | 16         |            |              |
| 0013    | 1000 0000      | 128 (-128) | 4224       | 217911424    |


{{3}}
Der dargestellte Speicherauszug kann aber auch eine Kommazahl (Floating Point)
umfassen und repräsentiert dann den Wert `3.8990753E-31`

{{4}}
Folglich bedarf es eines expliziten Wissens um den Charakter der Zahl, um eine
korrekte Interpretation zu ermöglichen. Dabei erfolgt die Einteilung nach:

{{4}}
* Wertebereichen (größte und kleinste Zahl)
* ggf. vorzeichenbehaftet Zahlen
* ggf. gebrochene Werte

#### Ganze Zahlen, `char` und `_Bool`

Ganzzahlen sind Zahlen ohne Nachkommastellen mit und ohne Vorzeichen. In C gibt
es folgende Typen für Ganzzahlen:

| Schlüsselwort    | Benutzung                       | Mindestgröße       |
|:-----------------|:--------------------------------|:-------------------|
| `char`           | 1 Byte bzw. 1 Zeichen           | 1 Byte (min/max)   |
| `short int`      | Ganzahl (ggf. mit Vorzeichen)   | 2 Byte             |
| `int`            | Ganzahl (ggf. mit Vorzeichen)   | "natürliche Größe" |
| `long int`       | Ganzahl (ggf. mit Vorzeichen)   |                    |
| `long long int`  | Ganzahl (ggf. mit Vorzeichen)   |                    |
| `_Bool`          | boolsche Variable               | 1 Bit              |

``` c
signed char <= short <= int <= long <= long long
```

Gängige Zuschnitte für `char` oder `int`

| Schlüsselwort    | Wertebereich               |
|:-----------------|:---------------------------|
| `signed char`    | -128 bis 127               |
| `char`           | 0 bis 255 (0xFF)           |
| `signed int`     | 32768 bis 32767            |
| `int`            | 65536 (0xFFFF)             |

Wenn die Typ-Spezifizierer (`long` oder `short`) vorhanden sind kann auf die
`int` Typangabe verzichtet werden.

```c
short int a; // entspricht short a;
long int b;  // äquivalent zu long b;
```

Standardmäßig wird von vorzeichenbehafteten Zahlenwerten ausgegangen. Somit wird
das Schlüsselwort `signed` eigentliche nicht benötigt

```cpp
int a;  //  signed int a;
unsigned long long int b;
```

#### Sonderfall `char`

Für den Typ `char` ist der mögliche Gebrauch und damit auch die Vorzeichenregel
zwiespältig:

* Wird `char` dazu verwendet einen **numerischen Wert** zu speichern und die
  Variable nicht explizit als vorzeichenbehaftet oder vorzeichenlos vereinbart,
  dann ist es implementierungsabhängig, ob `char` vorzeichenbehaftet ist oder
  nicht.
* Wenn ein Zeichen gespeichert wird, so garantiert der Standard, dass der
  gespeicherte Wert der nicht negativen Codierung im **Zeichensatz** entspricht.

```cpp
char c = 'M';  // =  1001101 (ASCII Zeichensatz)
char c = 77;   // =  1001101
char s[] = "Eine kurze Zeichenkette";
```

> **Achtung:** Anders als bei einigen anderen Programmiersprachen unterscheidet
> C zwischen den verschiedenen Anführungsstrichen.

![C logo](./images/01_EinAusgabeDatentypen/ASCII_Zeichensatz.jpeg)<!--
style=" width: 80%;
        max-width: 600px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->
Quelle: [ASCII-Tabelle](http://www.chip.de/webapps/ASCII-Tabelle_50073950.html)

    --{{1}}--
Erweiterung erfährt `char` mit der Überarbeitung des C-Standards 1994. Hier
wurde das Konzept eines breiten Zeichens (engl. *wide character*) eingeführt,
das auch Zeichensätze aufnehmen kann, die mehr als 1 Byte für die Codierung
eines Zeichen benötigen (beispielsweise Unicode-Zeichen). Siehe `wchar_t` oder
`wprintf`.

#### Sonderfall `Bool`
Seit dem C99 Standard existiert ein spezieller Datentyp `_Bool` für binäre
Variablen. Zuvor konnte das Wertepaar `true` (für wahr) und `false` (für falsch)
verwendet werden, die in der Headerdatei `<stdbool.h>` mit der Konstante 1 und 0 definiert sind.

```cpp                     BoolExample.c
#include <stdio.h>
#include <stdbool.h>

int main() {
   _Bool a = true;
   _Bool b = false;
   _Bool c = 45;

   printf("a = %i, b = %i, c = %i\n", a, b, c);
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Sinnvoll sind boolsche Variablen insbesondere im Kontext von logischen
Ausdrücken. Diese werden zum späteren Zeitpunkt eingeführt.

#### Architekturspezifische Ausprägung (Integer Datentypen)

Der Operator `sizeof` gibt Auskunft über die Größe eines Datentyps oder einer
Variablen in Byte.

```cpp                     sizeof.c
#include <stdio.h>

int main(void)
{
  int x;
  printf("x umfasst %d Byte.", (unsigned int)sizeof x);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


```cpp                     sizeof_example.c
#include <stdio.h>
#include <limits.h>   /* INT_MIN und INT_MAX */

int main(void) {
   printf("int size : %d Byte\n", (unsigned int) sizeof( int ) );
   printf("Wertebereich von %d bis %d\n", INT_MIN, INT_MAX);
   printf("char size : %d Byte\n", (unsigned int) sizeof( char ) );
   printf("Wertebereich von %d bis %d\n", CHAR_MIN, CHAR_MAX);
   return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{1}}
Die implementierungspezifische Werte, wie die Grenzen des Wertebereichs der
ganzzahlinen Datentypen sind in `limits.h` definiert, z.B.

{{1}}
| Makro    | Wert                   |
|:---------|:-----------------------|
|CHAR_MIN  |-128                    |
|CHAR_MAX  |+127                    |
|SHRT_MIN  |-32768                  |
|SHRT_MAX  |+32767                  |
|INT_MIN   |-2147483648             |
|INT_MAX   |+2147483647             |
|LONG_MIN  |-9223372036854775808    |
|LONG_MAX  |+9223372036854775807    |


#### Was passiert bei der Überschreitung des Wertebereiches

> Der Arithmetische Überlauf (arithmetic overflow) tritt auf, wenn das Ergebnis
> einer Berechnung für den gültigen Zahlenbereich zu groß ist, um noch richtig
> interpretiert werden zu können.

![instruction-set](./images/01_EinAusgabeDatentypen/2Komplement.png)<!--
style=" width: 80%;
        max-width: 500px;
        min-width: 250px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

Quelle: [Arithmetischer Überlauf (Autor: WissensDürster)](https://de.wikipedia.org/wiki/Arithmetischer_%C3%9Cberlauf#/media/File:4Bi-2Komplement.svg)

{{1}}
```cpp                     Overflow.c
#include <stdio.h>
#include <limits.h>   /* SHRT_MIN und SHRT_MAX */

int main(){
  short a = 30000;
  unsigned short d;   //      0 bis 65535
  signed short c;     // -32768 bis 32767
  printf("unsigned short - Wertebereich von %d bis %d\n", 0, USHRT_MAX);
  printf("short - Wertebereich von %d bis %d\n", SHRT_MIN, SHRT_MAX);
  c = 3000 + a;
  printf("c=%d\n", c);
  d = 3000 + a;
  printf("c=%d\n", d);
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{1}}
Ganzzahlüberläufe in der fehlerhaften Bestimmung der Größe eines
Puffers oder in der Adressierung eines Feldes können es einem Angreifer
ermöglichen den Stack zu überschreiben.

#### Fließkommazahlen

Fließkommazahlen sind Zahlen mit Nachkommastellen (reelle Zahlen).
Im Gegensatz zu Ganzzahlen gibt es bei den Fließkommazahlen keinen Unterschied
zwischen vorzeichenbehafteten und vorzeichenlosen Zahlen. Alle Fließkommazahlen
sind in C immer vorzeichenbehaftet.

In C gibt es zur Darstellung reeller Zahlen folgende Typen:

| Schlüsselwort    | Mindestgröße            |
|:-----------------|:------------------------|
| `float`          | 4 Byte                  |
| `double`         | 8 Byte                  |
| `long double`    | je nach Implementierung |

``` c
float <= double <=  long double
```

Gleitpunktzahlen werden halb logarithmisch dargestellt. Die Darstellung basiert
auf die Zerlegung in drei Teile: ein Vorzeichen, eine Mantisse und einen
Exponenten zur Basis 2.

Zur Darstellung von Fließkommazahlen sagt der C-Standard nichts aus. Zur
konkreten Realisierung ist die Headerdatei `float.h` auszuwerten.

|                        |`float`           |`double`                |
|:-----------------------|:-----------------|------------------------|
| kleinste positive Zahl |1.1754943508e-38  |2.2250738585072014E-308 |
| Wertebereich           |±3.4028234664e+38 |±1.7976931348623157E+308|

{{1}}
> **Achtung:** Fließkommazahlen bringen einen weiteren Faktor mit
>  - die Unsicherheit

{{1}}
```cpp                     float_precision.c
#include<stdio.h>
#include<float.h>

int main(void) {
	printf("float Genauigkeit  :%d \n", FLT_DIG);
	printf("double Genauigkeit :%d \n", DBL_DIG);
	float x = 0.1;
  if (x == 0.1) {
    printf("Gleich\n");
  }else{
    printf("Ungleich\n");
  }
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{2}}
Potenzen von 2 (zum Beispiel $2^{-3}=0.125$) können im Unterschied zu `0.1` präzise im Speicher abgebildet werden. Können Sie erklären?


#### Datentyp `void`

`void` wird im C-Standard als „unvollständiger Typ“ bezeichnet,
umfasst eine leere Wertemenge und wird verwendet überall dort, wo kein
Wert vorhanden oder benötigt wird.

Anwendungsbeispiele:

* Rückgabewert einer Funktion
* Parameter einer Funktion
* anonymer Zeigertyp `void*`

```cpp
int main(void) {
	//Anweisungen
  return 0;
}
```

```cpp
void funktion(void) {
	//Anweisungen
}
```

### Wertspezifikation

Zahlenliterale können in C mehr als Ziffern umfassen!

| Gruppe                | zulässige Zeichen                     |
| --------------------- | --------------------------------------|
|*decimal-digits*       |`0` `1` `2` `3` `4` `5` `6` `7` `8` `9`|
|*octal-prefix*         |`0`                                    |
|*octal-digits*         |`0` `1` `2` `3` `4` `5` `6` `7`        |
|*hexadecimal-prefix*   |`0x` `0X`                              |
|*hexadecimal-digits*   |`0` `1` `2` `3` `4` `5` `6` `7` `8` `9`|
|                       |`a` `b` `c` `d` `e` `f`                |
|                       |`A` `B` `C` `D` `E` `F`                |
|*unsigned-suffix*      |`u` `U`                                |
|*long-suffix*          |`l` `L`                                |
|*long-long-suffix*     |`ll` `LL`                              |
|*fractional-constant*  |`.`                                    |
|*exponent-part*        |`e` `E`                                |
|*binary-exponent-part* |`p` `P`                                |
|*sign*                 |`+` `-`                                |
|*floating-suffix*      |`f` `l` `F` `L`                        |



|  Zahlentyp | Dezimal       | Oktal         | Hexadezimal  |
|:-----------|:--------------|---------------|--------------|
| Eingabe    | x             | x             | x            |
| Ausgabe    | x             | x             | x            |
| Beispiel   | `12`          | `011`         | `0x12`       |
|            | `0.123`       |               | `0X1a`       |
|            | `123e-2`      |               | `0xC.68p+2`  |
|            | `1.23F`       |               |              |

> Erkennen Sie jetzt die Bedeutung der Compilerfehlermeldung `error: invalid suffix "abc" on integer constant` aus dem ersten Beispiel der Vorlesung?

{{1}}
`Variable = (Vorzeichen)(Zahlensystem)[Wert](Typ);`

{{1}}
| Literal      | Bedeutung                              |
|:-------------|:---------------------------------------|
| 12           | Ganzzahl vom Typ `int`                 |
| -234L        | Ganzzahl vom Typ `signed long`         |
| 100000000000 | Ganzzahl vom Typ `long`                |
| 011          | Ganzzahl also oktale Zahl (Wert $9_d$) |
| 0x12         | Ganzzahl ($18_d$)                      |
| 1.23F        | Fließkommazahl vom Typ `float`         |
| 0.132        | Fließkommazahl vom Typ `double`        |
| 123e-2       | Fließkommazahl vom Typ `double`        |
| 0xC.68p+2    | hexadizimale Fließkommazahl vom Typ `double` |

{{1}}
```cpp                     NumberFormats.c
#include <stdio.h>

int main(void)
{
  int x=020;
  int y=0x20;
  printf("x = %d\n", x);
  printf("y = %d\n", y);
  printf("Rechnen mit Oct und Hex z = %d", x + y);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


### Adressen

> **Merke:** Einige Anweisungen, wie z.B. `scanf`, verwenden Adressen von
> Variablen.

Um einen Zugriff auf die Adresse einer Variablen zu haben, kann man den Operator
`&` nutzen. Gegenwärtig ist noch nicht klar, warum dieser Zugriff erforderlich
ist, wird aber in einer der nächsten Veranstaltungen verdeutlicht.

```cpp                     Pointer.c
#include <stdio.h>

int main(void)
{
  int x=020;
  printf("%p\n",&x);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### Sichtbarkeit und Lebensdauer von Variablen

**Automatische Lebensdauer**

Die Lebensdauer einer Variablen gilt bis zum Ende des Anweisungsblockes,
in dem sie definiert wurde.

```cpp                           lifespan.c
#include<stdio.h>

int main(void){
  {
    int v;
    v = 2;
    printf("%d", v);
  }
  printf("%d", v);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Die automatischen Variablen können mit dem Schlüsselwort `auto` deklariert
werden, aber auch ohne Schlüsselwort sind "lokale" Variable "automatisch".

**Statische Lebensdauer**

Die Variable wird einmal deklariert, initialisiert und existiert während der
gesamten Programmausführung.

`static`-Variablen behalten ihren Wert nach dem Verlassen des Funktionsblocks, weil sie nicht im Stacksegment, sondern im Datensegment gespeichert werden.
Diese Interpretation des Schlüsselworts `static` gilt aber nur für die innerhalb eines Funktionsblocks definierten Variablen. Eine besondere Bedeutung haben die
`static`-Variablen im Zusammenhang mit Funktionen, werden deswegen in der
Funktionen gewidmeten Vorlesung behandelt.

    {{1}}
Nicht diskutiert wird an dieser Stellen die Lebensdauer von thread- und
allocated-Variablen.

    {{1}}
**`register`-Variablen**

    {{1}}
Das Schlüsselwort `register` weist den Compiler an, eine Variable so lange wie
möglich im Prozessorregister zu halten. Die Entscheidung darüber trifft der
Compiler letztendlich selbst.

#### Lokale Variablen

Bis C99 musste eine Variable immer am Anfang eines Anweisungsblocks vereinbart
werden. Nun genügt es, die Variable unmittelbar vor der ersten Benutzung zu
vereinbaren.

Variablen *leben* innerhalb einer Funktion, einer Schleife oder einfach nur
innerhalb eines durch geschwungene Klammern begrenzten Blocks von Anweisungen.

Wird eine Variable/Konstante z. B. im Kopf einer Schleife vereinbart, gehört sie
laut C99-Standard zu dem Block, in dem auch der Code der Schleife steht.
Folgender Codeausschnitt soll das verdeutlichen:

```cpp                           visibility.c
#include<stdio.h>

int main(void)
{
  int v = 1;
  int w = 5;
  {
    int v;
    v = 2;
    printf("%d\n", v);
    printf("%d\n", w);
  }
  printf("%d\n", v);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

#### lobale Variablen

Muss eine Variable immer innerhalb von `main` definiert werden? Nein, allerdings
sollten globale Variablen vermieden werden.

```cpp                           visibility.c
#include<stdio.h>

int v = 1; /*globale Variable*/

int main(void)
{
  printf("%d\n", v);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Sichtbarkeit und Lebensdauer spielen beim Definieren neuer Funktionen eine
wesentliche Rolle und werden in einer weiteren Vorlesung in diesem
Zusammenhang nochmals behandelt.

### Definition vs. Deklaration vs. Initialisierung

... oder andere Frage, wie kommen Name, Datentyp, Adresse usw. zusammen?

> Deklaration ist nur die Vergabe eines Namens und eines Typs für die Variable.
> Definition ist die Reservierung des Speicherplatzes. Initialisierung ist die
> Zuweisung eines ersten Wertes.


> **Merke:** Jede Definition ist gleichzeitig eine Deklaration aber nicht
> umgekehrt!

```cpp                     DeclarationVSDefinition.c
extern int a;      // Deklaration
int i;             // Definition + Deklaration
int a,b,c;
i = 5;             // Initialisierung
```

Das Schlüsselwort `extern` in obigem Beispiel besagt, dass die Definition der
Variablen `a` irgendwo in einem anderen Modul des Programms liegt. So deklariert
man Variablen, die später beim Binden (Linken) aufgelöst werden. Da in diesem
Fall kein Speicherplatz reserviert wurde, handelt es sich um keine Definition.

### Typische Fehler

**Fehlende Initialisierung**

```cpp                     MissingInitialisation.c
#include<stdio.h>

void foo() {
  int a;     // <- Fehlende Initialisierung
  printf("a=%d ", a);
}

int main(void) {
  int x = 5;
  printf("x=%d ", x);
  int y;     // <- Fehlende Initialisierung
  printf("y=%d ", y);
  foo();
	return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
**Redeklaration**

{{1}}
```cpp                     Redeclaration.c
#include<stdio.h>

int main(void) {
  int x;
  int x;
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{2}}
**Falsche Zahlenliterale**

{{2}}
```cpp                     wrong_float.c
#include<stdio.h>

int main(void) {
  float a=1,5;   /* FALSCH  */
  float b=1.5;   /* RICHTIG */
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


{{3}}
**Was passiert wenn der Wert zu groß ist?**

{{3}}
```cpp                     TooLarge.c
#include<stdio.h>

int main(void) {
  short a;
  a = 0xFFFF + 2;
  printf("Schaun wir mal ... %hi\n", a);
	return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

## Compiler

**Warnings**

> **Hinweis:** Unterschiedliche Compiler verwenden unterschieldliche
> Konfigurationen und generieren unterschiedliche Ergebnisse!

| Name               | Bezeichnung                                                                                                                     |
|:------------------ |:------------------------------------------------------------------------------------------------------------------------------- |
| Gnu C Compiler     | Linux "Standard" C Compiler (auch in cygwin)                                                                                    |
|                    | [Dokumentation](https://gcc.gnu.org/onlinedocs/gcc/Option-Summary.html)                                                         |
|                    | [Erläuterung zu den Warning Konfigurationen](https://kristerw.blogspot.com/2017/09/useful-gcc-warning-options-not-enabled.html) |
| Microsoft Compiler | enthalten im Microsoft Studio                                                                                                   |
|                    | [Dokumentation](https://msdn.microsoft.com/de-de/library/19z1t1wy.aspx)                                                         |

> Repli.it unterstützt automatisch keine Warnings diese müssen Sie ggf. manuell angeben.

**Zeilennummern**

> Aktivieren Sie in Ihrem Editor in jedem Fall die Zeilennummern!

## Input-/ Output Operationen

Ausgabefunktionen wurden bisher genutzt, um den Status unserer Programme zu
dokumentieren. Nun soll dieser Mechanismus systematisiert und erweitert werden.

![EVA-Prinzip](./images/01_EinAusgabeDatentypen/EVA-Prinzip.png)<!--
style=" width: 100%;
        max-width: 600px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->
Quelle: [EVA-Prinzip (Autor:  Deadlyhappen)](https://de.wikipedia.org/wiki/EVA-Prinzip#/media/File:EVA-Prinzip.svg)

### `printf`

Die Bibliotheksfunktion `printf` dient dazu, eine Zeichenkette (engl. *String*)
auf der Standardausgabe auszugeben. In der Regel ist die Standardausgabe der
Bildschirm. Über den Rückgabewert liefert `printf` die Anzahl der ausgegebenen
Zeichen. Wenn bei der Ausgabe ein Fehler aufgetreten ist, wird ein negativer
Wert zurückgegeben.

Als erstes Argument von `printf` sind **nur Strings** erlaubt. Bei folgender
Zeile gibt der Compiler beim Übersetzen deshalb eine Warnung oder einen Fehler
aus:

```c
printf(55);      // Falsch
printf("55");    // Korrekt
```

Dabei kann der String um entsprechende Parameter erweitert werden. Jeder
Parameter nach dem String wird durch einen Platzhalter in dem selben
repäsentiert.

```cpp                             printf_example.c
#include <stdio.h>

int main(){
  //       _________________________________
  //       |                               |
  printf("%i plus %2.2f ist gleich %s.\n", 3, 2.0, "Fuenf");
  //      <------------------------>
  //        String mit Referenzen
  //            auf Parameter
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

                                 {{1-3}}
| Zeichen        | Umwandlung                                              |
|:---------------|:--------------------------------------------------------|
| `%d` oder `%i` | `int`                                                   |
| `%c`           | einzelnes Zeichen                                       |
| `%e` oder `%E` | `double` im Format `[-]d.ddd e±dd` bzw. `[-]d.ddd E±dd` |
| `%f`           | `double` im Format `[-]ddd.ddd`                         |
| `%o`           | `int` als Oktalzahl ausgeben                            |
| `%p`           | die Adresse eines Zeigers                               |
| `%s`           | Zeichenkette ausgeben                                   |
| `%u`           | `unsigned int`                                          |
| `%x` oder `%X` | `int` als Hexadezimalzahl ausgeben                      |
| `%%`           | Prozentzeichen                                          |


{{2-3}}
Welche Formatierungmöglichkeiten bietet `printf` noch?

{{2-3}}
+ die Feldbreite
+ ein Flag
+ durch einen Punkt getrennt die Anzahl der Nachkommstellen (Längenangabe) und
  an letzter Stelle schließlich
+ das Umwandlungszeichen selbst (siehe Tabelle oben)

#### Feldbreite

Die Feldbreite definiert die Anzahl der nutzbaren Zeichen, sofern diese nicht
einen größeren Platz beanspruchen.

```cpp                             printf_numbercount.c
#include <stdio.h>

int main(){
  printf("rechtsbuendig      : %5d, %5d, %5d\n",34, 343, 3343);
  printf("linksbuendig       : %-5d, %-5d, %-5d\n",34, 343, 3343);
  printf("Zu klein gedacht   : %5d\n", 234534535);
  //printf("Ohnehin besser     : %*d", 12, 234534535);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

#### Formatierungsflags

| Flag              | Bedeutung                           |
|:------------------|:------------------------------------|
| `-`               | linksbündig justieren               |
| `+`               | Vorzeichen ausgeben                 |
| Leerzeichen       | Leerzeichen                         |
| `0`               | numerische Ausgabe mit 0 aufgefüllt |
| `#`               | für `%x` wird ein x in die Hex-Zahl eingefügt, für `%e`oder `%f` ein Dezimaltrenner (.) |

```cpp                             printf_flag_examples.c
#include <stdio.h>

int main(){
  printf("012345678901234567890\n");
  printf("Integer: %+11d\n", 42);
	printf("Integer: %+11d\n", -4242);
  printf("Integer: %-e\n", 42.2345);
  printf("Integer: %-g\n", 42.2345);
  printf("Integer: %#x\n", 42);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

#### Genauigkeit

 Bei `%f` werden standardmäßig 6 Nachkommastellen ausgegeben. Mit `%a.bf` kann
 eine genauere Spezifikation erfolgen. `a` steht für die Feldbreite, `b` für die
 Nachkommastellen.

```cpp                             printf_flag_examples.c
#include <stdio.h>

int main(){
  float a = 142.23443513452352;
  printf("Float Wert: %f\n", a);
  printf("Float Wert: %9.3f\n", a);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

#### Escape-Sequenzen

| Sequenz | Bedeutung             |
|:--------|:----------------------|
| `\n`    | newline               |
| `\b`    | backspace             |
| `\r`    | carriage return       |
| `\t`    | horizontal tab        |
| `\\\`   | backslash             |
| `\'`    | single quotation mark |
| `\"`    | double quotation mark |

```cpp                             printf_esc_sequences.c
#include <stdio.h>

int main(){
  printf("123456789\r");
  printf("ABCD\n\n");
	printf("Vorname \t Name \t\t Alter \n");
	printf("Andreas \t Mustermann\t 42 \n\n");
	printf("Manchmal braucht man auch ein \"\\\"\n");
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### `getchar`

Die Funktion `getchar()` liest Zeichen für Zeichen aus einem Puffer. Dies
geschieht aber erst, wenn die Enter-Taste gedrückt wird.

```c    GetChar.c
#include <stdio.h>

int main(){
	char c;
	printf("Mit welchem Buchstaben beginnt ihr Vorname? ");
	c = getchar();
	printf("\nIch weiss jetzt, dass Ihr Vorname mit '%c' beginnt.\n", c);
	return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Problem: Es lassen sich immer nur einzelne Zeichen erfassen, die durch
Enter-Taste bestätigt wurden. Als flexiblere Lösung lässt sich `scanf` anwenden.

### `scanf`

Format-String der `scanf`-Anweisung kann folgendes enthalten:

* % specifier
* count  of input characters
* length modifier (`hh` `h` `l` `ll`)
* conversion specifier

```c    Scanf.c
#include <stdio.h>

int main(){
  int i;
  float a;
  char b;
  printf("Bitte folgende Werte eingeben %%c %%f %%d: ");
  int n=scanf("%c %f %d", &b, &a, &i);
  printf("\n%c %f %d\n", b, a, i);
  return 0;
}
```
@LIA.evalWithDebug(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


## Ausblick

```cpp                     GoodBy.c
#include<stdio.h>

int main() {
  printf("... \t bis \n\t\t zum \n\t\t\t");
  printf("naechsten \n\t\t\t\t\t mal! \n");
	return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)
