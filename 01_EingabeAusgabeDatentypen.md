<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner


-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md)

# Grundlagen der Sprache C

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Einführung in das wissenschaftliche Programmieren`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2022/23`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Ein- und Ausgabe / Variablen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Durch welche Parameter ist eine Variable definiert?
* Erklären Sie die Begriffe Deklaration, Definition und Initialisierung im
  Hinblick auf eine Variable!
* Worin unterscheidet sich die Zahldarstellung von ganzen Zahlen (`int`) von den
  Gleitkommazahlen (`float`).
* Welche Datentypen kennt die Sprache C++?
* Erläutern Sie für `char` und `int` welche maximalen und minimalen Zahlenwerte
  sich damit angeben lassen.
* Ist `printf` ein Schlüsselwort der Programmiersprache C++?
* Welche Beschränkung hat `getchar`

> **Vorwarnung:** Man kann Variablen nicht ohne Ausgaben und Ausgaben nicht ohne
>Variablen erklären. Deshalb wird im folgenden immer wieder auf einzelne Aspekte
> vorgegriffen. Nach der Vorlesung sollte sich dann aber ein Gesamtbild ergeben.

---------------------------------------------------------------------


```cpp                     GoodBy.cpp
#include <iostream>

int main() {
  std::cout << "... \t bis \n\t\t zum \n\t\t\t";
  std::cout << "naechsten \n\t\t\t\t\t mal! \n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ main.cpp -o a.out`, `./a.out`)

Unbefriedigende Lösung, jede neue Berechnung muss in den Source-Code integriert
und dieser dann kompiliert werden. Ein Taschenrechner wäre die bessere Lösung!

```cpp                     QuadraticEquation.cpp
#include<iostream>

int main() {
  int x;
  x = 5;
  std::cout <<"f("<<x<<") = "<<3*x*x + 4*x + 8<<" \n";
  x = 9;
  std::cout <<"f("<<x<<") = "<<3*x*x + 4*x + 8<<" \n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

                                    {{1}}
******************************************************************

Ein Programm manipuliert Daten, die in Variablen organisiert werden.

Eine Variable ist ein **abstrakter Behälter** für Inhalte, welche im
Verlauf eines Rechenprozesses benutzt werden. Im Normalfall wird eine Variable
im Quelltext durch einen Namen bezeichnet, der die Adresse im Speicher
repräsentiert. Alle Variablen müssen vor Gebrauch vereinbart werden.

Kennzeichen einer Variable:

1. Name
2. Datentyp
3. Wert
4. Adresse
5. Gültigkeitraum

******************************************************************

                                  {{2}}
******************************************************************
Mit `const` kann bei einer Vereinbarung der Variable festgelegt werden, dass
ihr Wert sich nicht ändert.

```cpp
const double e = 2.71828182845905;
```

Ein weiterer Typqualifikator ist `volatile`. Er gibt an, dass der
Wert der Variable sich jederzeit z. B. durch andere Prozesse ändern kann.

******************************************************************

### Zulässige Variablennamen

Der Name kann Zeichen, Ziffern und den Unterstrich enthalten. Dabei ist zu
beachten:

* Das erste Zeichen muss ein Buchstabe sein, der Unterstrich ist auch möglich.
* C++ betrachte Groß- und Kleinschreibung - `Zahl` und `zahl` sind also
  unterschiedliche Variablennamen.
* Schlüsselworte (`class`, `for`, `return`, etc.) sind als Namen unzulässig.

| Name            | Zulässigkeit                                   |
|:----------------|:-----------------------------------------------|
| `gcc`           | erlaubt                                        |
| `a234a_xwd3`    | erlaubt                                        |
| `speed_m_per_s` | erlaubt                                        |
| `double`        | nicht zulässig (Schlüsselwort)                 |
| `robot.speed`   | nicht zulässig (`.` im Namen)                  |
| `3thName`       | nicht zulässig (Ziffer als erstes Zeichen)     |
| `x y`           | nicht zulässig (Leerzeichen im Variablennamen) |

```cpp                     QuadraticEquation.cpp
#include<iostream>

int main() {
  int x = 5;
  std::cout<<"Unsere Variable hat den Wert "<<x<<" \n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> Vergeben Sie die Variablennamen mit Sorgfalt. Für jemanden der Ihren Code liest, sind diese wichtige Informationsquellen!
> [Link](https://wiki.c2.com/?BadVariableNames)

                                  {{1}}
******************************************************************

Neben der Namensgebung selbst unterstützt auch eine entsprechende Notationen die Lesbarkeit. In Programmen sollte ein Format konsistent verwendet werden.

| Bezeichnung            | denkbare Variablennamen                            |
|:---------------------- |:-------------------------------------------------- |
| CamelCase (upperCamel) | `YouLikeCamelCase`, `HumanDetectionSuccessfull`    |
|           (lowerCamel) | `youLikeCamelCase`, `humanDetectionSuccessfull`    |
| underscores            | `I_hate_Camel_Case`, `human_detection_successfull` |

In der Vergangenheit wurden die Konventionen (zum Beispiel durch Microsoft "Ungarische Notation") verpflichtend durchgesetzt. Heute dienen eher die generellen Richtlinien des Clean Code in Bezug auf die Namensgebung.

******************************************************************

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

#### Ganze Zahlen, `char` und `bool`

Ganzzahlen sind Zahlen ohne Nachkommastellen mit und ohne Vorzeichen. In C/C++ gibt
es folgende Typen für Ganzzahlen:

<!-- data-type="none" -->
| Schlüsselwort    | Benutzung                       | Mindestgröße       |
|:-----------------|:--------------------------------|:-------------------|
| `char`           | 1 Byte bzw. 1 Zeichen           | 1 Byte (min/max)   |
| `short int`      | Ganzahl (ggf. mit Vorzeichen)   | 2 Byte             |
| `int`            | Ganzahl (ggf. mit Vorzeichen)   | "natürliche Größe" |
| `long int`       | Ganzahl (ggf. mit Vorzeichen)   |                    |
| `long long int`  | Ganzahl (ggf. mit Vorzeichen)   |                    |
| `bool`           | boolsche Variable               | 1 Byte              |

``` cpp
signed char <= short <= int <= long <= long long
```

Gängige Zuschnitte für `char` oder `int`

<!-- data-type="none" -->
| Schlüsselwort    | Wertebereich               |
|:-----------------|:---------------------------|
| `signed char`    | -128 bis 127               |
| `char`           | 0 bis 255 (0xFF)           |
| `signed int`     | 32768 bis 32767            |
| `int`            | 65536 (0xFFFF)             |

Wenn die Typ-Spezifizierer (`long` oder `short`) vorhanden sind kann auf die
`int` Typangabe verzichtet werden.

```cpp
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
> C/C++ zwischen den verschiedenen Anführungsstrichen.

![ASCII-Zeichensatz](./images/01_EinAusgabeDatentypen/ASCII_Zeichensatz.jpeg "ASCII Zeichensatz [^ASCII]")<!-- width="80%" -->

[^ASCII]: [ASCII-Tabelle](http://www.chip.de/webapps/ASCII-Tabelle_50073950.html)

#### Sonderfall `bool`
Auf die Variablen von Datentyp `bool` können Werte `true` (1) und `false` (0)
gespeichert werden. Eine implizite Umwandlung der ganzen Zahlen zu den Werten 0 und 1 ist ebenfalls möglich.

```cpp                     BoolExample.cpp
#include <iostream>

int main() {
   bool a = true;
   bool b = false;
   bool c = 45;

   std::cout<<"a = "<<a<<" b = "<<b<<" c = "<<c<<"\n";
   return 0;
}
```
@LIA.eval(`["main.c"]`, `g++ -Wall main.c -o a.out`, `./a.out`)

Sinnvoll sind boolsche Variablen insbesondere im Kontext von logischen
Ausdrücken. Diese werden zum späteren Zeitpunkt eingeführt.

#### Architekturspezifische Ausprägung (Integer Datentypen)

Der Operator `sizeof` gibt Auskunft über die Größe eines Datentyps oder einer
Variablen in Byte.

```cpp                     sizeof.cpp
#include <iostream>

int main(void)
{
  int x;
  std::cout<<"x umfasst " <<sizeof(x)<<" Byte.";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


```cpp                     sizeof_example.c
#include <iostream>
#include <limits.h>   /* INT_MIN und INT_MAX */

int main(void) {
   std::cout<<"int size: "<< sizeof(int)<<" Byte\n";
   std::cout<<"Wertebereich von "<< INT_MIN<<" bis "<< INT_MAX<< "\n";
   std::cout<<"char size : "<< sizeof(char) <<" Byte\n";
   std::cout<<"Wertebereich von "<< CHAR_MIN<<" bis "<<CHAR_MAX<<"\n";
   return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{1}}
Die implementierungspezifische Werte, wie die Grenzen des Wertebereichs der
ganzzahlinen Datentypen sind in `limits.h` definiert, z.B.

{{1}}
<!-- data-type="none" -->
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
```cpp                     Overflow.cpp
#include <iostream>
#include <limits.h>   /* SHRT_MIN und SHRT_MAX */

int main(){
  short a = 30000;

  std::cout<<"Berechnung von 30000+3000 mit:\n\n";

  signed short c;     // -32768 bis 32767
  std::cout<<"(signed) short c - Wertebereich von "<<SHRT_MIN<<" bis "<<SHRT_MAX<<"\n";
  c = 3000 + a;      // ÜBERLAUF!
  std::cout<<"c="<<c<<"\n";

  unsigned short d;   //      0 bis 65535
  std::cout<<"unsigned short d - Wertebereich von "<<0<<" bis "<<USHRT_MAX<<"\n";

  d = 3000 + a;
  std::cout<<"d="<<d<<"\n";
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{1}}
Ganzzahlüberläufe in der fehlerhaften Bestimmung der Größe eines
Puffers oder in der Adressierung eines Feldes können es einem Angreifer
ermöglichen den Stack zu überschreiben.

#### Fließkommazahlen

Fließkommazahlen sind Zahlen mit Nachkommastellen (reelle Zahlen).
Im Gegensatz zu Ganzzahlen gibt es bei den Fließkommazahlen keinen Unterschied
zwischen vorzeichenbehafteten und vorzeichenlosen Zahlen. Alle Fließkommazahlen
sind in C/C++ immer vorzeichenbehaftet.

In C/C++ gibt es zur Darstellung reeller Zahlen folgende Typen:

<!-- data-type="none" -->
| Schlüsselwort    | Mindestgröße            |
|:-----------------|:------------------------|
| `float`          | 4 Byte                  |
| `double`         | 8 Byte                  |
| `long double`    | je nach Implementierung |

``` c++
float <= double <=  long double
```

Gleitpunktzahlen werden halb logarithmisch dargestellt. Die Darstellung basiert
auf die Zerlegung in drei Teile: ein Vorzeichen, eine Mantisse und einen
Exponenten zur Basis 2.

Zur Darstellung von Fließkommazahlen sagt der C/C++-Standard nichts aus. Zur
konkreten Realisierung ist die Headerdatei `float.h` auszuwerten.

<!-- data-type="none" -->
|                        |`float`           |`double`                |
|:-----------------------|:-----------------|------------------------|
| kleinste positive Zahl |1.1754943508e-38  |2.2250738585072014E-308 |
| Wertebereich           |±3.4028234664e+38 |±1.7976931348623157E+308|

{{1}}
> **Achtung:** Fließkommazahlen bringen einen weiteren Faktor mit
>  - die Unsicherheit

{{1}}
```cpp                     float_precision.cpp
#include<iostream>
#include<float.h>

int main(void) {
	std::cout<<"float Genauigkeit  :"<<FLT_DIG<<" \n";
	std::cout<<"double Genauigkeit :"<<DBL_DIG<<" \n";
	float x = 0.1;
  if (x == 0.1) {   // <- das ist ein double "0.1"
  //if (x == 0.1f) {   // <- das ist ein float "0.1"
   std::cout<<"Gleich\n";
  }else{
    std::cout<<"Ungleich\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Potenzen von 2 (zum Beispiel $2^{-3}=0.125$) können im Unterschied zu `0.1` präzise im Speicher abgebildet werden. Können Sie erklären?


#### Datentyp `void`

`void` wird als „unvollständiger Typ“ bezeichnet,
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

Zahlenliterale können in C/C++ mehr als Ziffern umfassen!

<!-- data-type="none" -->
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


<!-- data-type="none" -->
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
```cpp                     NumberFormats.cpp
#include<iostream>

int main(void)
{
  int x=020;
  int y=0x20;
  std::cout<<"x = "<<x<<"\n";
  std::cout<<"y = "<<y<<"\n";
  std::cout<<"Rechnen mit Oct und Hex x + y = "<< x + y;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


### Adressen

> **Merke:** Einige Anweisungen in C/C++ verwenden Adressen von
> Variablen.

Jeder Variable in C++ wird eine bestimmten Position im Hauptspeicher zugeordnet. Diese Position nennt man Speicheradresse.
Solange eine Variable gültig ist, bleibt sie an dieser Stelle im Speicher.
Um einen Zugriff auf die Adresse einer Variablen zu haben, kann man den Operator
`&` nutzen.

```cpp                     Pointer.cpp
#include <iostream>

int main(void)
{
  int x=020;
  std::cout<<&x<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Sichtbarkeit und Lebensdauer von Variablen

**Lokale Variablen**

Variablen *leben* innerhalb einer Funktion, einer Schleife oder einfach nur
innerhalb eines durch geschwungene Klammern begrenzten Blocks von Anweisungen von der Stelle ihrer Definition bis zum Ende des Blocks.
Beachten Sie, dass die Variable vor der ersten Benutzung vereinbart werden muss.

Wird eine Variable/Konstante z. B. im Kopf einer Schleife vereinbart, gehört sie
zu dem Block, in dem auch der Code der Schleife steht.
Folgender Codeausschnitt soll das verdeutlichen:

```cpp                           visibility.cpp
#include<iostream>

int main(void)
{
  int v = 1;
  int w = 5;
  {
    int v;
    v = 2;
    std::cout<<v<<"\n";
    std::cout<<w<<"\n";
  }
  std::cout<<v<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

**Globale Variablen**

Muss eine Variable immer innerhalb von `main` definiert werden? Nein, allerdings
sollten globale Variablen vermieden werden.

```cpp                           visibility.cpp
#include<iostream>

int v = 1; /*globale Variable*/

int main(void)
{
  std::cout<<v<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

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

```cpp                     DeclarationVSDefinition.cpp
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

```cpp                     MissingInitialisation.cpp
#include<iostream>

void foo() {
  int a;     // <- Fehlende Initialisierung
  std::cout<<"a="<<a<<"\n";
}

int main(void) {
  int x = 5;
  std::cout<<"x="<<x<<"\n";
  int y;     // <- Fehlende Initialisierung
  std::cout<<"y="<<y<<"\n";
  foo();
	return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
**Redeklaration**

{{1}}
```cpp                     Redeclaration.cpp
#include<iostream>

int main(void) {
  int x;
  int x;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{2}}
**Falsche Zahlenliterale**

{{2}}
```cpp                     wrong_float.cpp
#include<iostream>

int main(void) {
  float a=1,5;   /* FALSCH  */
  float b=1.5;   /* RICHTIG */
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{3}}
**Was passiert wenn der Wert zu groß ist?**

{{3}}
```cpp                     TooLarge.cpp
#include<iostream>

int main(void) {
  short a;
  a = 0xFFFF + 2;
  std::cout<<"Schaun wir mal ... "<<a<<"\n";
	return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

**Ein- und Ausgabe**

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

Für Ein- und Ausgabe stellt C++ das Konzept der Streams bereit, dass nicht nur für elementare Datentypen gilt, sondern auch auf die neu definierten Datentypen (Klassen) erweitert werden kann.
Unter Stream wird eine Folge von Bytes verstanden.

Als Standard werden verwendet:

+ `std::cin` für die Standardeingabe (Tastatur),
+ `std::cout` für die Standardausgabe (Console) und
+ `std::cerr` für die Standardfehlerausgabe (Console)

> **Achtung:** Das `std::` ist ein zusätzlicher Indikator für eine bestimmte Implementierung, ein sogenannter Namespace. Um sicherzustellen, dass eine spezifische Funktion, Datentyp etc. genutzt wird stellt man diese Bezeichnung dem verwendenten Element zuvor. Mit `using namespace std;` kann man die permanente Nennung umgehen.

Stream-Objekte  werden durch
`#include <iostream>`
bekannt gegeben. Definiert werden sie als Komponente der Standard Template Library (STL) im Namensraum `std`.

Mit Namensräumen können Deklarationen und Definitionen unter einem Namen zusammengefasst und gegen andere Namen abgegrenzt werden.

```cpp   iostream.cpp
#include <iostream>

int main(void) {
  char hanna[]="Hanna";
  char anna[]="Anna";
  std::cout << "C++ stream: " << "Hallo "<< hanna << ", " << anna <<std::endl;
  return 0;
}
```

### Ausgabe

Der Ausgabeoperator `<<` formt automatisch die Werte der Variablen in die Textdarstellung der benötigten Weite um.
Der Rückgabewert des Operators ist selbst ein Stream-Objekt (Referenz), so dass ein weiterer Ausgabeoperator darauf angewendet werden kann. Damit ist die Hintereinanderschaltung
von Ausgabeoperatoren möglich.

```cpp
std::cout<<55<<"55"<<55.5<<true;    
```

Welche Formatierungmöglichkeiten bietet der Ausgabeoperator noch?

Mit Hilfe von in `<iomanip>` definierten Manipulatoren können besondere Ausgabeformatierungen erreicht werden.

| Manipulator         | Bedeutung                      |
|:--------------------|:-------------------------------|  
| setbase(int B)      | Basis 8, 10 oder 16 definieren |
| setfill(char c)     | Füllzeichen festlegen |
| setprecision(int n) | Flisskommaprezession |
| setw(int w)         | Breite setzen |


```cpp                             manipulatoren1.c
#include <iostream>
#include <iomanip>
int main(){
  std::cout<<std::setbase(16)<< std::fixed<<55<<std::endl;
  std::cout<<std::setbase(10)<< std::fixed<<55<<std::endl;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Achtung:** Die Manipulatoren wirken auf alle daruf folgenden Ausgaben.

#### Feldbreite

Die Feldbreite definiert die Anzahl der nutzbaren Zeichen, sofern diese nicht
einen größeren Platz beanspruchen.

Der Manipulator `right` sorgt im Beispiel für eine rechtsbündige Ausrichtung der Ausgabe,
wegen `setw(5)` ist die Ausgabe fünf Zeichen breit, wegen `setfill('0')` werden
nicht benutzte Stellen mit dem Zeichen 0 aufgefüllt, `endl` bewirkt die Ausgabe eines Zeilenumbruchs.

```cpp                             manipulatoren2.c
#include <iostream>
#include <iomanip>
int main(){

  std::cout<<std::right<< std::fixed<<std::setw(5)<<55<<std::endl;
  std::cout<<std::right<< std::fixed<<std::setfill('0')<<std::setw(5)<<55<<std::endl;
  std::cout<<std::left<< std::fixed<<std::setw(5)<<55<<std::endl;
  std::cout<<std::setw(5)<<"Zu klein gedacht: "<<234534535<<std::endl;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

#### Genauigkeit

```cpp   genauigkeit.cpp
#include <iostream>
#include <iomanip>
#include <math.h>
using namespace std;
int main() {
  for (int i = 12; i > 1; i -=3) {
    cout << setprecision(i) << fixed << M_PI << endl;
  }
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

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

```cpp  esc_sequences.c
#include <iostream>
using namespace std;
int main(){
  cout << "123456789\r";
  cout << "ABCD\n\n";
	cout << "Vorname \t Name \t\t Alter \n";
	cout << "Andreas \t Mustermann\t 42 \n\n";
	cout << "Manchmal braucht man auch ein \"\\\"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Eingabe

Für die Eingabe stellt iostream den Eingabeoperator `>>` zur Verfügung.
Der Rückgabewert des Operators ist ebenfalls eine Referenz auf ein Stream-Objekt (Referenz), so dass
auch hier eine Hintereinanderschaltung von Operatoren möglich ist.

```cpp    istream.cpp
#include <iostream>

int main(){
  int i;
  float a;
  char b;
  std::cout<<"Bitte Werte eingeben : ";
  std::cin>>b>>a>>i;
  std::cout<<b<<" "<<a<<" "<<i;
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

<!--START_SKIP_IN_PDF-->
## Quizze
