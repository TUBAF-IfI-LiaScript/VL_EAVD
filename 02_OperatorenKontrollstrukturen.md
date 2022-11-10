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

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/02_Operatoren.md)

# Operatoren

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Einführung in das wissenschaftliche Programmieren`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2022/23`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Operatoren / Kontrollstrukturen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/02_Operatoren.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/02_Operatoren.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Wonach lassen sich Operatoren unterscheiden?
* Welche unterschiedliche Bedeutung haben `x++` und `++x`?
* Erläutern Sie den Begriff unärer, binärer und tertiärer Operator.
* Unterscheiden Sie Zuweisung und Anweisung.
* Was bedeutet rechtsassoziativ und linksassoziativ?
* Welche Fallstricke lauern bei expliziter und impliziter Typumwandlung?
* Wann sollte man eine explizite Umwandlung vornehmen?
* Wie lassen sich Kontrollflüsse grafisch darstellen?
* Welche Konfigurationen erlaubt die `for`-Schleife?
* In welchen Funktionen (Verzweigungen, Schleifen) ist Ihnen das Schlüsselwort
  `break` bekannt?
* Worin liegt der zentrale Unterschied der `while` und `do-while` Schleife?
* Recherchieren Sie Beispiele, in denen `goto`-Anweisungen Bugs generierten.

---------------------------------------------------------------------


## Operatoren-Überblick

> Ein Ausdruck ist eine Kombination aus Variablen, Konstanten, Operatoren und
> Rückgabewerten von Funktionen. Die Auswertung eines Ausdrucks ergibt einen
> Wert.

**Zahl der beteiligten Operationen**

Man unterscheidet in der Sprache C/C++ *unäre*, *binäre* und *ternäre* Operatoren

<!-- data-type="none" -->
| Operator           | Operanden | Beispiel                |
|:-------------------|:---------:|:------------------------|
| Unäre Operatoren   |     1     | `&` Adressoperator      |
|                    |           | `sizeof` Größenoperator |
| Binäre Operatoren  |     2     | `+`, `-`, `%`           |
| Ternäre Operatoren |     3     | `?` Bedingungsoperator  |

Es gibt auch Operatoren, die, je nachdem wo sie stehen, entweder unär oder binär
sind. Ein Beispiel dafür ist der `-`-Operator.

```cpp
b = -a; // ein Vorzeichen (unär)
b = a-2; // arithmetische Operation (binär)
```

       {{1}}
******************************************************************************

**Position**

Des Weiteren wird unterschieden, welche Position der Operator einnimmt:

- *Infix* – der Operator steht zwischen den Operanden.
- *Präfix* – der Operator steht vor den Operanden.
- *Postfix* – der Operator steht hinter den Operanden.

`+` und `-` können alle drei Rollen einnehmen:

```cpp
a = b + c; // Infix
a = -b;    // Präfix
a = b++;   // Postfix
```
******************************************************************************

       {{2}}
******************************************************************************
**Assoziativität**

| Linksassoziativ                  | Rechtsassoziativ                 |
| -------------------------------- | -------------------------------- |
| Auswertung von links nach rechts | Auswertung von rechts nach links |


******************************************************************************

       {{3}}
******************************************************************************
**Funktion des Operators**

* Zuweisung
* Arithmetische Operatoren
* Logische Operatoren
* Bit-Operationen
* Bedingungsoperator

******************************************************************************

## Zuweisungsoperator

Der Zuweisungsoperator `=` ist von seiner mathematischen Bedeutung zu trennen -
einer Variablen wird ein Wert zugeordnet. Damit macht dann auch `x=x+1` Sinn.

```cpp                     zuweisung.cpp
#include <iostream>
using namespace std;

int main() {
   int zahl1 = 10;
   int zahl2 = 20;
   int ergeb;
   // Zuweisung des Ausdrucks 'zahl1 + zahl2'
   ergeb = zahl1 + zahl2;

   cout<<zahl1<<" + "<<zahl2<<" = "<<ergeb<<"\n";
   return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Die Zuweisungsoperation ist rechtsassoziativ. Der Ausdruck wird von rechts nach
links ausgewertet.

```cpp                     AssociationDirection.cpp
#include <iostream>
using namespace std;

int main() {
  int a, b;
  a = 5;
  a = b = a + 1;   // kein guter Stil!
  cout<<"a = "<<a<<", b = "<<b<<"\n";
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
> **Achtung:** Verwechseln Sie nicht den Zuweisungsoperator `=` mit dem
> Vergleichsoperator `==`. Der Compiler kann die Fehlerhaftigkeit kaum erkennen
> und generiert Code, der ein entsprechendes Fehlverhalten zeigt.

{{1}}
```cpp                            EqualSign.cpp
#include <iostream>
using namespace std;

int main(){
  int x, y;
  x = 15;             // Zuweisungsoperator
  y = x = x + 5;
  cout<<"x="<<x<<" und y="<<y<<"\n";

  y = x == 20;        // Gleichheitsoperator
  cout<<"x="<<x<<" und y="<<y<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

## Inkrement und Dekrement

Mit den `++` und `--` -Operatoren kann ein L-Wert um eins erhöht bzw. um
eins vermindert werden. Man bezeichnet die Erhöhung um eins auch als Inkrement,
die Verminderung um eins als Dekrement. Ein Inkrement einer Variable `x`
entspricht `x = x + 1`, ein Dekrement einer Variable `x` entspricht `x = x - 1`.

```cpp                            IncrementDecrement.cpp
#include <iostream>
using namespace std;

int main(){
  int x, result;
  x = 5;
  result = 2 * ++x;   // Gebrauch als Präfix
  cout<<"x="<<x<<" und result="<<result<<"\n";
  result = 2 * x++;   // Gebrauch als Postfix
  cout<<"x="<<x<<" und result="<<result<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


## Arithmetische Operatoren

| Operator | Bedeutung                    | Ganzzahlen   | Gleitkommazahlen |
|:--------:|:-----------------------------|:-------------|:-----------|
| `+`      | Additon                      | x            | x          |
| `-`      | Subtraktion                  | x            | x          |
| `*`      | Multiplikation               | x            | x          |
| `/`      | Division                     | x            | x          |
| `%`      | Modulo (Rest einer Division) | x            |            |

```cpp                            calcExamples.c
#include <iostream>
using namespace std;

int main(){
  int zahl1,zahl2;
  int ergeb;
  zahl1=10;
  zahl2=20;
  cout<<"Zahl 1= "<<zahl1<<"\n";
  cout<<"Zahl 2= "<<zahl2<<"\n";

  // Moeglichkeit 1: zuerst Berechnung, dann Ausgabe
  ergeb=zahl1+zahl2;
  cout<<"Summe der Zahlen:"<<ergeb<<"\n";
  // Moeglichkeit 2: Berechnung direkt für die Ausgabe
  cout<<zahl1<<" - "<<zahl2<<" = "<<zahl1-zahl2<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{1}}
> **Achtung:** Divisionsoperationen werden für Ganzzahlen und Gleitkommazahlen
> unterschiedlich realisiert.

{{1}}
* Wenn zwei Ganzzahlen wie z. B. $4/3$ dividiert werden, erhalten wir das
  Ergebnis 1 zurück, der nicht ganzzahlige Anteil der Lösung bleibt
  unbeachtet.
* Für Fließkommazahlen wird die Division wie erwartet realisiert.

{{1}}
```cpp                                  division.cpp
#include <iostream>
using namespace std;

int main(){
  int timestamp, minuten;

  timestamp = 345; //[s]
  cout<<"Zeitstempel "<<timestamp<<" [s]\n";
  minuten=timestamp/60;
  cout<<timestamp<<" [s] entsprechen "<<minuten<<" Minuten\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
> Die Modulo Operation generiert den Rest einer Divisionsoperation bei ganzen Zahlen.

{{2}}
```cpp                                  moduloExample.cpp
#include <iostream>
using namespace std;

int main(){
  int timestamp, sekunden, minuten;

  timestamp = 345; //[s]
  cout<<"Zeitstempel "<<timestamp<<" [s]\n";
  minuten=timestamp/60;
  sekunden=timestamp%60;
  cout<<"Besser lesbar = "<<minuten<<" min. "<<sekunden<<" sek.\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{3}}
Die arithmetischen Operatoren lassen sich in verkürzter Schreibweise wie folgt
darstellen:

{{3}}
| Operation | Bedeutung                    |
|:---------:|:-----------------------------|
|   `+=`    | `a+=b` äquivalent zu `a=a+b` |
|   `-=`    | `a-=b` äquivalent zu `a=a-b` |
|   `*=`    | `a*=b` äquivalent zu `a=a*b` |
|   `/=`    | `a/=b` äquivalent zu `a=a/b` |
|   `%=`    | `a%=b` äquivalent zu `a=a%b` |

{{3}}
```cpp             shortenedOperators.cpp
#include <iostream>
using namespace std;

int main() {
   int x=2, y=4, z=6;
   cout<<"x="<<x<<" y="<<y<<" z="<<z<<"\n";

   cout<<"x = x+y ="<<(x+=y)<<"\n";
   cout<<"z = z+y ="<<(z+=y)<<"\n";
   cout<<"z = z+x ="<<(z+=x)<<"\n";
   cout<<"x="<<x<<" y="<<y<<" z="<<z<<"\n";
   return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{3}}
> **Achtung:** Verlieren Sie bei langen Berechnungsketten nicht den Überblick!
> Insbesondere die verkürzte Schreibweise forciert dies.

## Vergleichsoperatoren

Kern der Logik sind Aussagen, die wahr oder falsch sein können.


| Operation | Bedeutung           |
|:---------:|:--------------------|
|    `<`    | kleiner als         |
|    `>`    | größer als          |
|   `<=`    | kleiner oder gleich |
|   `>=`    | größer oder gleich  |
|   `==`    | gleich              |
|   `!=`    | ungleich            |

```cpp                                       LogicOperators.cpp
#include <iostream>
using namespace std;

int main(){
  int x = 15;
  cout<<"x = "<<x<<" \n";
  cout<<"Aussage x > 5 ist "<< (x>5) << " \n";
  cout<<"Aussage x == 5 ist "<< (x==-15) << " \n";
  return 0;
}
```
@LIA.evalWithDebug(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Merke:** Der Rückgabewert einer Vergleichsoperation ist `bool`. Dabei bedeutet
> `false` eine ungültige und `true` eine gültige Aussage. Vor 1993 wurde ein logischer Datentyp in C++ durch
> `int` simuliert. Aus der Gründen der Kompatibilität wird `bool` überall,
> wo wie hier nicht ausdrücklich `bool` verlangt wird in `int` (Werte `0` und `1`) umgewandelt.


## Logische Operatoren

    {{0-1}}
********************************************************************************

Und wie lassen sich logische Aussagen verknüpfen? Nehmen wir an, dass wir aus den Messdaten zweier Sensoren ein Alarmsignal generieren wollen. Nur wenn die Temperatur _und_ die Luftfeuchte in einem bestimmten Fenster liegen, soll dies nicht  passieren.

| Operation | Bedeutung |
|:---------:|:----------|
|   `&&`    | UND       |
|   `||`    | ODER      |
|   `!`     | NICHT     |

Das ODER wird durch senkrechte Striche repräsentiert (Altgr+`<` Taste) und nicht durch große `I`!

Wir wollen (willkürlich) festlegen, dass für die Temperatur ein Wert zwischen -10 und -20 Grad toleriert wird und die Luftfeuchte mit 40 bis 60 Prozent.

```cpp                                       Logic.cpp
#include <iostream>
using namespace std;

int main(){
  float Temperatur = -30;     // Das sind unsere Probewerte
  float Feuchte = 65;

  // Vergleichsoperationen und Logische Operationen
  bool TempErgebnis = ....    // Hier sind Sie gefragt!

  // Ausgabe
  if ... {
    cout<<"Die Messwerte kannst Du vergessen!";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)
********************************************************************************

    {{1-2}}
********************************************************************************
Anmerkung: C++ bietet für logische Operatoren und Bit-Operatoren Synonyme  `and`, `or`, `xor`.
Die Synonyme sind Schlüsselwörter, wenn Compiler-Einstellungen /permissive- oder /Za (Spracherweiterungen deaktivieren) angegeben werden. Sie sind keine Schlüsselwörter, wenn Microsoft-Erweiterungen aktiviert sind. Die Verwendung der Synonyme kann die Lesbarkeit deutlich erhöhen.
********************************************************************************

## Bit-Operationen

Bitoperatoren verknüpfen logische Aussagen oder manipulieren einzelne Bits in
binären Zahlendarstellungen.

| Operation   | Bedeutung            |
|:------------|:---------------------|
| `&`, `&=`   | bitweises und        |
| `|`, `|=`   | bitweises oder       |
| `^`, `^=`   | bitweises xor        |
| `~`         | bitweises Komplement |

## Shift Operatoren

Die Operatoren `<<` und `>>` dienen dazu, den Inhalt einer Variablen bitweise um
einige Stellen nach links bzw. nach rechts zu verschieben.

## Bedingungsoperator

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

## `sizeof` - Operator

Der Operator `sizeof` ermittelt die Größe eines Datentyps (in Byte) zur
Kompiliertzeit.

* `sizeof` ist keine Funktion, sondern ein Operator.
* `sizeof` wird häufig zur dynamischen Speicherreservierung verwendet.

```cpp      sizeof.cpp
#include <iostream>
using namespace std;

int main(){
  double wert=0.0;
  cout<<sizeof(0)<<" "<<sizeof(double)<<" "<<sizeof(wert);
return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


## Vorrangregeln

Konsequenterweise bildet auch die Programmiersprache C/C++ eigene Vorrangregeln ab,
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
Für Operatoren mit der gleichen Priorität ist für die Reihenfolge der Auswertung die Assoziativität das zweite Kriterium.

{{1}}
```cpp
a = 4 / 2 / 2;

// von rechts nach links (FALSCH)
// 4 / (2 / 2)   // ergibt 4

// von links nach rechts ausgewertet
// (4 / 2) / 2   // ergibt 1
```

> **Merke:** Setzen Sie Klammern, um alle Zweifel auszuräumen


## ... und mal praktisch

Folgender Code nutzt die heute besprochenen Operatoren um die Eingaben von zwei
Buttons auf eine LED abzubilden. Nur wenn beide Taster gedrückt werden, beleuchte das rote Licht für 3 Sekunden.

<div>
  <wokwi-pushbutton color="green" pin="10" ></wokwi-pushbutton>
  <wokwi-led        color="red"   pin="13"></wokwi-led>
  <wokwi-pushbutton color="red"   pin="11" ></wokwi-pushbutton>
  <span id="simulation-time"></span>
</div>
```cpp    ButtonSynch.cpp
const int button_A_pin = 10;
const int button_B_pin = 11;
const int led_pin = 13;

int buttonAState;
int buttonBState;

void setup(){
  pinMode(button_A_pin, INPUT);
  pinMode(button_B_pin, INPUT);
  pinMode(led_pin, OUTPUT);
  Serial.begin(9600);
 }

void loop() {
  Serial.println("Wait one second for A ");
  delay(1000);
  buttonAState = digitalRead(button_A_pin);
  Serial.println ("... and for B");
  delay(1000);
  buttonBState = digitalRead(button_B_pin);

  if ( buttonAState && buttonBState){
    digitalWrite(led_pin, HIGH);
    delay(3000);
  }
  else
  {
    digitalWrite(led_pin, LOW);
  }
}
```
@AVR8js.sketch

Wie würden Sie den Code so erweitern, dass die LED bei einem einzelnen Tastendruck (A ODER B) für 1 und bei beiden synchron betätigten Tastern für 5 Sekunden aktiv wird?

## Cast-Operatoren

> *Casting* beschreibt die Konvertierung eines Datentypen in einen anderen. Dies
> kann entweder automatisch durch den Compiler vorgenommen oder durch den
> Programmierer angefordert werden.

Im erst genannten Fall spricht man von

* impliziten Typumwandlung, im zweiten von
* expliziter Typumwandlung.

Es wird bei Methoden vorausgesetzt, dass der Compiler eine Typumwandlung auch
wirklich unterstützt. Eine Typumwandlung kann einschränkend oder erweiternd
sein!

### Implizite Datentypumwandlung

Operanden dürfen in C/C++ eine Variable mit unterschiedlichen Datentyp verknüpfen.
Die implizite Typumwandlung generiert einen gemeinsamen Datentyp, der in einer
Rangfolge am weitesten oben steht. Das Ergebnis ist ebenfalls von diesem Typ.

1. `char` -> `short` -> `int` -> `long` -> `long long` / `float` -> `double` -> `long double`
2. Die Rangfolge bei ganzzahligen Typen ist unabhängig vom Vorzeichen.


Dabei sind einschränkende Konvertierungskonfigurationen kritisch zu sehen:

* Bei der Umwandlung von höherwertigen Datentypen in niederwertigere Datentypen
  kann es zu Informationsverlust kommen.
* Der Vergleich von `signed`- und `unsigned`-Typen kann zum falschen Ergebnis
  führen. So kann beispielsweise `-1 > 1U` wahr sein.

```cpp                     NumberFormats.cpp
#include <iostream>
using namespace std;

int main()
{
  int i = -1;
  unsigned int limit = 200;

  if ( i > limit ){
    cout<<" i > limit!!! \n";
  }
  else{
    cout<<"Kein Problem!\n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
**Konvertierung zum `int`-Typ**

{{1}}
Beim Konvertieren des Wertes von einem in das andere `int`-Typ

{{1}}
* bleibt der Wert unverändert, wenn die Darstellung im Zieltyp möglich ist,
* anderenfalls ist das Ergebnis implementierungabhängig bzw. führt zu einer
  Fehlermeldung

{{2}}
**Vermischen von Ganzzahl und Gleitkommawerten**

{{2}}
* Die Division zweier `int`-Werte gibt immer nur einen Ganzzahlanteil zurück.
  Hier findet keine automatische Konvertierung in eine Gleitpunktzahl statt.
* Bei der Umwandlung von ganz großen Zahlen (beispielsweise `long long`) in
  einen Gleitpunkttyp kann es passieren, dass die Zahl nicht mehr darzustellbar ist.

{{2}}
```cpp                     NumberFormats.cpp
#include <iostream>
using namespace std;

int main()
{
  float f=3.14;
  int i=f;
  cout<<"float value = "<<f<<"/ Integer-Anteil "<<i<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{3}}
> **Achtung:** Implizite Typumwandlungen bergen erhebliche Risiken in sich!

{{3}}
```cpp                     Overflow.cpp
#include <iostream>
using namespace std;

int main()
{
  float f = -3.14;
  unsigned int i = f;
  cout<<"float value = "<<f<<" / Integer-Anteil "<<i<<" \n";
  return 0;
  }
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


### Explizite Datentypumwandlung

Anders als bei der impliziten Typumwandlung wird bei der expliziten
Typumwandlung der Zieldatentyp konkret im Code angegeben.

Neben der klassischen C-Typumwandlung stellt C++-Standard vier verschiedene Cast-Operatoren bereit:

+ reinterpret_cast
+ const_cast
+ static_cast
+ dynamic_cast

```cpp
(Zieltyp) ausdruck;
reinterpret_cast<Typ>(ausdruck)
const_cast<Typ>(ausdruck)
static_cast<Typ>(ausdruck)
dynamic_cast<Typ*>(ausdruck)
```

```cpp                    VolumeSphere.cpp
#include <iostream>
using namespace std;

int main()
{
  int i = 3;
  int j = 4;
  cout<<"int i / int j   = "<<i/j<<" \n";
  cout<<"float(i / j)    = "<<(float)(i/j)<<" \n";
  cout<<"float(i / j)    = "<<(float)i/j<<" \n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

```cpp   
const char* str = "hello";
int i = static_cast<int>(str);//error C2440: 'static_cast' : cannot
                              // convert from 'const char *' to 'int'
int j = (int)str; // C-style cast. Did the programmer really intend
                  // to do this?
int k = reinterpret_cast<int>(str);// Programming intent is clear.
                                   // However, it is not 64-bit safe.
```

`reinterpret_cast`, `static_cast` und `const_cast` bewirken dasselbe wie `(Zieltyp)ausdruck`.
static_cast wird verwendet für Umwandlungen, die nur zur Kompilierzeit überprüft werden und
eine entsprechende Fehlermeldung ausgeben, falls das nicht möglich ist.
const_cast gilt der Umwandlung zwischen konstanten und nicht konstanten Daten.
dynamic_cast wird für sichere, zur Laufzeit zu prüfende Umwandlungen von Zeigern auf eine Basisklasse von einer abgeleiteten Klasse verwendet.

[https://learn.microsoft.com/de-de/cpp/cpp/type-conversions-and-type-safety-modern-cpp](https://learn.microsoft.com/de-de/cpp/cpp/type-conversions-and-type-safety-modern-cpp?view=msvc-170)

# Kontrollfluss

Bisher haben wir Programme entworfen, die eine sequenzielle Abfolge von
Anweisungen enthielt.

![Modelle](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuG8pkAmSIulJ3k_9A2hDIozEoibFpbOmjCOcQeHLr1Yhg8arqFJy0Yw7rBmKe5K0 "Lineare Ausführungskette")

Diese Einschränkung wollen wir nun mit Hilfe weiterer Anweisungen überwinden:

1. **Verzweigungen (Selektion)**: In Abhängigkeit von einer Bedingung wird der
   Programmfluss an unterschiedlichen Stellen fortgesetzt.

   Beispiel: Wenn bei einer Flächenberechnung ein Ergebnis kleiner Null
   generiert wird, erfolgt eine Fehlerausgabe. Sonst wird im Programm
   fortgefahren.

2. **Schleifen (Iteration)**: Ein Anweisungsblock wird so oft wiederholt, bis
   eine Abbruchbedingung erfüllt wird.

   Beispiel: Ein Datensatz wird durchlaufen um die Gesamtsumme einer Spalte zu
   bestimmen. Wenn der letzte Eintrag erreicht ist, wird der Durchlauf
   abgebrochen und das Ergebnis ausgegeben.

3. Des Weiteren verfügt C/C++ über **Sprünge**: die Programmausführung wird mit Hilfe von Sprungmarken an einer anderen Position fortgesetzt. Formal sind sie jedoch nicht notwendig. Statt die nächste Anweisung auszuführen, wird (zunächst) an eine ganz andere Stelle im Code gesprungen.

### Verzweigungen

Verzweigungen entfalten mehrere mögliche Pfade für die Ausführung des Programms.

Darstellungsbeispiele für mehrstufige Verzweigungen (`switch`)

![Modelle](https://www.plantuml.com/plantuml/png/SoWkIImgAStDuG8pk3BJ53IIy_DICaioy_CK73KLIZ9IynGqAbEBDRaK5An2KYjA50ojkL9pYbDHbJfXLMfa3MGMb-GNOD7XZ5M7CJR3NR0gDO4eLT38oo_9oCnBHyY0X86IGErfN63R7O1ia2S1)<!-- width="60%" -->

![instruction-set](./images/03_Kontrollfluss/NassiMehrfAusw1.png "Nassi-Shneiderman-Diagramm [^1]")

[^1]: [Nassi-Shneiderman-Diagramm (Autor Renzsorf)](https://de.wikipedia.org/wiki/Nassi-Shneiderman-Diagramm)

#### `if`-Anweisungen

Im einfachsten Fall enthält die `if`-Anweisung eine einzelne bedingte
Anweisung oder einen Anweisungsblock. Sie kann mit `else` um eine Alternative
erweitert werden.

Zum Anweisungsblock werden die Anweisungen mit geschweiften Klammern (`{` und
`}`) zusammengefasst.

```cpp
if(Bedingung) Anweisung;  // <- Einzelne Anweisung

if(Bedingung){            // <- Beginn Anweisungsblock
   Anweisung;
   Anweisung;
}                         // <- Ende Anweisungsblock
```

       {{1}}
************************************************************************

Optional kann eine alternative Anweisung angegeben werden, wenn die Bedingung
nicht erfüllt wird:

```cpp
if(Bedingung){
  Anweisung;
}else{
  Anweisung;
}
```

Mehrere Fälle können verschachtelt abgefragt werden:


```cpp
if(Bedingung)
  Anweisung;
else
  if(Bedingung)
    Anweisung;
  else
    Anweisung;
    Anweisung;     //!!!
```

> **Merke**: An diesem Beispiel wird deutlich, dass die Klammern für die
> Zuordnung elementar wichtig sind. Die letzte Anweisung gehört NICHT zum zweite
> `else` Zweig sondern zum ersten!

************************************************************************

       {{2}}
************************************************************************
**Weitere Beispiele für Bedingungen**

Die Bedingungen können als logische UND arithmetische Ausdrücke
formuliert werden.

| Ausdruck     | Bedeutung                                       |
| ------------ | ----------------------------------------------- |
| `if (a)`     | `if (a != 0)`                                   |
| `if (!a)`    | `if (a == 0)`                                   |
| `if (a > b)` | `if (!(a <= b))`                                |
| `if ((a-b))` | `ìf (a != b)`                                   |
| `if (a || b)` | $a>0$ oder $b>0$                               |

************************************************************************

        {{3}}
************************************************************************

**Mögliche Fehlerquellen**

1. Zuweisungs- statt Vergleichsoperator in der Bedingung (kein Compilerfehler)
2. Bedingung ohne Klammern (Compilerfehler)
3. `;` hinter der Bedingung (kein Compilerfehler)
4. Multiple Anweisungen ohne Anweisungsblock
5. Komplexität der Statements

************************************************************************

       {{4}}
************************************************************************

**Beispiel**

Nehmen wir an, dass wir einen kleinen Roboter aus einem Labyrinth fahren lassen
wollen. Dazu gehen wir davon aus, dass er bereits an einer Wand steht. Dieser soll er mit der "Linke-Hand-Regel" folgen. Dabei wird von einem einfach zusammenhängenden Labyrith ausgegangen.

Die nachfolgende Grafik illustriert den Aufbau des Roboters und die vier möglichen Konfigurationen des Labyrinths, nachdem ein neues Feld betreten wurde.

![robotMaze.jpeg](./images/03_Kontrollfluss/robotMaze.jpeg)<!--
style=" width: 80%;
        max-width: 600px;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->

| Fall | Bedeutung                                                                                                                         |
| ---- | --------------------------------------------------------------------------------------------------------------------------------- |
| 1.   | Die Wand knickt nach links weg. Unabhängig von WG und WR folgt der Robter diesem Verlauf.                                         |
| 2.   | Der Roboter folgt der linksseitigen Wand.                                                                                         |
| 3.   | Die Wand blockiert die Fahrt. Der Roboter dreht sich nach rechts, damit liegt diese Wandelement nun wieder zu seiner linken Hand. |
| 4.   | Der Roboter folgt dem Verlauf nach einer Drehung um 180 Grad.                                                                     |

<!-- data-type="none" -->
| WL  | WG  | WR  | Fall | Verhalten                  |
|:--- |:--- |:--- | ---- |:-------------------------- |
| 0   | 0   | 0   | 1    | Drehung Links, Vorwärts    |
| 0   | 0   | 1   | 1    | Drehung Links, Vorwärts    |
| 0   | 1   | 0   | 1    | Drehung Links, Vorwärts    |
| 0   | 1   | 1   | 1    | Drehung Links, Vorwärts    |
| 1   | 0   | 0   | 2    | Vorwärts                   |
| 1   | 0   | 1   | 2    | Vorwärts                   |
| 1   | 1   | 0   | 3    | Drehung Rechts, Vorwärts   |
| 1   | 1   | 1   | 4    | Drehung 180 Grad           |

************************************************************************

{{5}}
************************************************************************
```cpp                     IfExample.c
#include <iostream>
using namespace std;

int main(){
  int WL, WG, WR;
  WL = 0; WG = 1; WR =1;
  if (!WL)                         // Fall 1
    cout<<"Drehung Links\n";
  if ((WL) && (!WG))                // Fall 2
      cout<<"Vorwärts\n";
  if ((WL) && (WG) && (!WR))         // Fall 3
    cout<<"Drehung Rechts\n";
  if ((WL) && (WG) && (WR))          // Fall 4
    cout<<"Drehung 180 Grad\n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

**Sehen Sie mögliche Vereinfachungen des Codes?**

************************************************************************

#### Zwischenfrage

```cpp                     Test.cpp
#include <iostream>
using namespace std;

int main()
{
    int Punkte = 45;
    int Zusatzpunkte = 15;
    if (Punkte + Zusatzpunkte >= 50)
    {
       cout<<"Test ist bestanden!\n";
       if (Zusatzpunkte >= 15)
       {
          cout<<"Alle Zusatzpunkte geholt!\n";
       }else{
           if(Zusatzpunkte > 8) {
               cout<<"Respektable Leistung\n";
           }
       }
    }else{
       cout<<"Leider durchgefallen!\n";
    }
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


#### `switch`-Anweisungen

> [*Too many ifs - I think I switch* ](http://www.peacesoftware.de/ckurs7.html)
>
> Berndt Wischnewski

Eine übersichtlichere Art der Verzweigung für viele, sich ausschließende
Bedingungen wird durch die `switch`-Anweisung bereitgestellt. Sie wird in der
Regel verwendet, wenn eine oder einige unter vielen Bedingungen ausgewählt
werden sollen. Das Ergebnis der "expression"-Auswertung soll eine Ganzzahl
(oder `char`-Wert) sein. Stimmt es mit einem "const_expr"-Wert
überein, wird die Ausführung an dem entsprechenden `case`-Zweig fortgesetzt.
Trifft keine der Bedingungen zu, wird der `default`-Fall aktiviert.

```cpp
switch(expression)
 {
   case const-expr: Anweisung break;
   case const-expr:
      Anweisungen
      break;
   case const-expr: Anweisungen break;
   default: Anweisungen
 }
```

{{1}}
```cpp                     SwitchExample.cpp
#include <iostream>
using namespace std;

int main() {
  int a=50, b=60;
  char op;
  cout<<"Bitte Operator definieren (+,-,*,/): ";
  cin>>op;

  switch(op) {
    case '+':
      cout<<a<<" + "<<b<<" = "<<a+b<<" \n";
      break;
    case '-':
      cout<<a<<" - "<<b<<" = "<<a-b<<" \n";
      break;
    case '*':
      cout<<a<<" * "<<b<<" = "<<a*b<<" \n";
      break;
    case '/':
      cout<<a<<" / "<<b<<" = "<<a/b<<" \n";
      break;
    default:
      cout<<op<<"? kein Rechenoperator \n";
  }
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{2}}
Im Unterschied zu einer `if`-Abfrage wird in den unterschiedlichen Fällen immer
nur auf Gleichheit geprüft! Eine abgefragte Konstante darf zudem nur einmal
abgefragt werden und muss ganzzahlig oder `char` sein.

{{2}}
```cpp
// Fehlerhafte case Blöcke
switch(x)
{
   case x < 100: // das ist ein Fehler
     y = 1000;
  break;

  case 100.1: // das ist genauso falsch
     y = 5000;
     z = 3000;
  break;
}
```

{{3}}
Und wozu brauche ich das `break`? Ohne das `break` am Ende eines Falls werden
alle darauf folgenden Fälle bis zum Ende des `switch` oder dem nächsten `break`
zwingend ausgeführt.

{{3}}
```cpp                     SwitchBreak.cpp
#include <iostream>
using namespace std;

int main() {
  int a=5;

  switch(a) {
    case 5:   // Multiple Konstanten
    case 6:
    case 7:
      cout<<"Der Wert liegt zwischen 4 und 8\n";
    case 3:
      cout<<"Der Wert ist 3 \n";
      break;
    case 0:
      cout<<"Der Wert ist 0 \n";
    default: cout<<"Wert in keiner Kategorie\n";}

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{4}}
Unter Ausnutzung von `break` können Kategorien definiert werden, die aufeinander
aufbauen und dann übergreifend "aktiviert" werden.

{{4}}
```cpp                     CharClassification.cpp
#include <iostream>
using namespace std;

int main() {
  char ch;
  cout<<"Geben Sie ein Zeichen ein :  ";
  cin>>ch;

  switch(ch)
  {
      case 'a':
      case 'A':
      case 'e':
      case 'E':
      case 'i':
      case 'I':
      case 'o':
      case 'O':
      case 'u':
      case 'U':
          cout<<"\n\n"<<ch<<" ist ein Vokal.\n\n";
          break;
      default:
          cout<<ch<<" ist ein Konsonant.\n\n";
  }
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


### Schleifen

Schleifen dienen der Wiederholung von Anweisungsblöcken – dem sogenannten
Schleifenrumpf oder Schleifenkörper – solange die Schleifenbedingung als
Laufbedingung gültig bleibt bzw. als Abbruchbedingung nicht eintritt. Schleifen,
deren Schleifenbedingung immer zur Fortsetzung führt oder die keine
Schleifenbedingung haben, sind *Endlosschleifen*.

Schleifen können verschachtelt werden, d.h. innerhalb eines Schleifenkörpers
können weitere Schleifen erzeugt und ausgeführt werden. Zur Beschleunigung des
Programmablaufs werden Schleifen oft durch den Compiler entrollt (*Enrollment*).

Grafisch lassen sich die wichtigsten Formen in mit der Nassi-Shneiderman
Diagrammen wie folgt darstellen:

* Iterationssymbol

<!--
style="width: 80%; min-width: 420px; max-width: 720px;"
-->
```ascii
   +---------------------------------------------------------------------+
   |                                                                     |
   |  zähle [Variable] von [Startwert] bis [Endwert], mit [Schrittweite] |
   | +-------------------------------------------------------------------+
   | |                                                                   |
   | |  Anweisungsblock 1                                                |
   +-+-------------------------------------------------------------------+     .
```

* Wiederholungsstruktur mit vorausgehender Bedingungsprüfung

<!--
style="width: 80%; min-width: 420px; max-width: 720px;"
-->
```ascii
   +--------------------------+
   |                          |
   |  solange Bedingung wahr  |
   | +------------------------+
   | |                        |
   | |  Anweisungsblock 1     |
   +-+------------------------+                                                .
```

* Wiederholungsstruktur mit nachfolgender Bedingungsprüfung

<!--
style="width: 80%; min-width: 420px; max-width: 720px;"
-->
```ascii
   +-+------------------------+
   | |                        |
   | |  Anweisungsblock 1     |
   | +------------------------+
   |                          |
   |   solange Bedingung wahr |
   +--------------------------+                                                .
```

Die Programmiersprache C/C++ kennt diese drei Formen über die Schleifenkonstrukte
`for`, `while` und `do while`.

#### `for`-Schleife

Der Parametersatz der `for`-Schleife besteht aus zwei Anweisungsblöcken und einer
Bedingung, die durch Semikolons getrennt werden. Mit diesen wird ein
**Schleifenzähler** initiert, dessen
Manipulation spezifiziert und das Abbruchkriterium festgelegt. Häufig wird die
Variable mit jedem Durchgang inkrementiert oder dekrementiert, um dann anhand
eines Ausdrucks evaluiert zu werden. Es wird überprüft, ob die Schleife
fortgesetzt oder abgebrochen werden soll. Letzterer Fall tritt ein, wenn dieser
den Wert false (falsch) annimmt.

```cpp
// generisches Format der for-Schleife
for(Initialisierung; Bedingung; Reinitialisierung) {
   // Anweisungen
}

// for-Schleife als Endlosschleife
for(;;){
   // Anweisungen
}
```

```cpp                     ForLoopExample.cpp
#include <iostream>
using namespace std;

int main(){
	int i;
  for (i = 1; i<10; i++)
    cout<<i<<" ";

  cout<<"\nNach der Schleife hat i den Wert "<<i<<"\n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)


{{1}}
**Beliebte Fehlerquellen**

{{1}}
* Semikolon hinter der schließenden Klammer von `for`
* Kommas anstatt Semikolons zwischen den Parametern von `for`
* fehlerhafte Konfiguration von Zählschleifen
* Nichtberücksichtigung der Tatsache, dass die Zählvariable nach dem Ende der
  Schleife über dem Abbruchkriterium liegt

{{1}}
```cpp                     SemicolonAfterFor.cpp
#include <iostream>
using namespace std;

int main(){
  int i;
  for (i = 1; i<10; i++);
    cout<<i<<" ";

  cout<<"Das ging jetzt aber sehr schnell ... \n"<<i;
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


#### `while`-Schleife

Während bei der `for`-Schleife auf ein n-maliges Durchlaufen Anweisungsfolge
konfiguriert wird, definiert die `while`-Schleife nur eine Bedingung für den
Fortführung/Abbruch.

```cpp
// generisches Format der while-Schleife
while (Bedingung)
  Anweisungen;

while (Bedingung){
    Anweisungen;
    Anweisungen;
}
```

```cpp                     count_plus.cpp
#include <iostream>
using namespace std;

int main(){
  char c;
  int zaehler = 0;
  cout<<"Pluszeichenzähler - zum Beenden \"_\" [Enter]\n";
  cin>>c;
  while(c != '_')
  {
    if(c == '+')
      zaehler++;
      cin>>c;
  }
  cout<<"Anzahl der Pluszeichen: "<<zaehler<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
Dabei soll erwähnt werden, dass eine `while`-Schleife eine `for`-Schleife
ersetzen kann.

{{1}}
```cpp
// generisches Format der while-Schleife
i = 0;
while (i<10){
   // Anweisungen;
   i++;
}

for (i=0; i<10; i++){
   // Anweisungen;
}
```

#### `do-while`-Schleife

Im Gegensatz zur `while`-Schleife führt die `do-while`-Schleife die Überprüfung
des Abbruchkriteriums erst am Schleifenende aus.

```cpp
// generisches Format der while-Schleife
do
   Anweisung;
 while (Bedingung);
```

Welche Konsequenz hat das? Die `do-while`-Schleife wird in jedem Fall einmal
ausgeführt.

{{1}}
```cpp                     count_plus.cpp
#include <iostream>
using namespace std;

int main(){
  char c;
  int zaehler = 0;
  cout<<"Pluszeichenzähler - zum Beenden \"_\" [Enter]\n";
  do
  {
    cin>>c;
    if(c == '+')
      zaehler++;
  }while(c != '_');
  cout<<"Anzahl der Pluszeichen: "<<zaehler<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

### Kontrolliertes Verlassen der Anweisungen

Bei allen drei Arten der Schleifen kann zum vorzeitigen Verlassen der Schleife
 `break` benutzt werden. Damit wird aber nur die unmittelbar umgebende Schleife
 beendet!

```cpp                     breakForLoop.cpp
#include <iostream>
using namespace std;

int main(){
	int i;
  for (i = 1; i<10; i++){
      if (i == 5) break;
      cout<<i<<" ";
  }
  cout<<"\nUnd vorbei ... i ist jetzt "<<i<<"\n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{1}}
Eine weitere wichtige Eingriffsmöglichkeit für Schleifenkonstrukte bietet
`continue`. Damit wird nicht die Schleife insgesamt, sondern nur der aktuelle
Durchgang gestoppt.

{{1}}
```cpp                     continueForLoop.cpp
#include <iostream>
using namespace std;

int main(){
	int i;
  for (i = -5; i<6; i++){
      if (i == 0) continue;
      cout<<12. / i<<"\n";
  }
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

{{2}}
Durch `return`- Anweisung wird das Verlassen einer Funktion veranlasst (genaues
in der Vorlesung zu Funktionen).

### GoTo or not GoTo?

`Goto` erlaubt es Sprungmarken (Labels) zu definieren und bei der Anweisung, die
diese referenziert, die Ausführung fortzusetzen. Konsequenterweise ist damit aber
eine nahezu beliebige Auflösung der Ordnung des Codes möglich.

>  *Use of `goto` statement is highly discouraged in any programming language*
>  *because it makes difficult to trace the control flow of a program, making*
>  *the program hard to understand and hard to modify. Any program that uses a*
> * `goto` can be rewritten to avoid them.*
>
> [Tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_goto_statement.html)

```cpp                     gotoExample.cpp
#include <iostream>
using namespace std;

int main(){
	int i=0;
  label:
       cout<< i <<" ";
       i++;
       if (i <= 10) goto label;
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Ein wichtiger Fehler, der häufig immer mit goto in Verbindung gebracht wird, hat
aber eigentlich nichts damit zu tun
[Apple-SSL Bug](http://www.spiegel.de/netzwelt/web/goto-fail-apples-furchtbarer-fehler-a-955154.html)


## Darstellung von Algorithmen

* Nassi-Shneiderman-Diagramme
* [Flußdiagramme](https://de.wikipedia.org/wiki/Programmablaufplan)

Beispiel - Wechseln der Räder

![Programmablaufplan.png](https://www.plantuml.com/plantuml/png/LL2_JeSm4Dxx5ETlWe74mOc6oAIBamukBYTSxKKev7gD2G_cvCQBMQk6S5Fx_VdwzVgeA9hcoPI30MWPEhYn1lAmW-gPWv88iQC0EB-4E_IoKNgxhK5znggmr0RA2As4-dV9KK-35qolMJJjdv62FQX7744nnS6VuCE1OMCwazmqzlGIV7YU22hkkkjSXsCfywkXCB8pnGSFoUaeQNY7LVOlzn_QNkwJ4lnyIAykraHTLjDdOzx7Dm00)<!--
style="width: 50%;
       max-width: 330px;
       display: block;
       margin-left: auto;
       margin-right: auto;" -->

## Beispiel des Tages

Das Codebeispiel des Tages führt die Berechnung eines sogenannten magischen
Quadrates vor.

Das Lösungsbeispiel stammt von der Webseite https://rosettacode.org, die für das
Problem [magic square](https://rosettacode.org/wiki/Magic_squares_of_odd_order#C) und
viele andere "Standardprobleme" Lösungen in unterschiedlichen Sprachen präsentiert.
Sehr lesenswerte Sammlung!

```cpp                     magicSquare.cpp
#include <iostream>
using namespace std;

int f(int n, int x, int y)
{
  return (x + y*2 + 1) % n;
}

int main() {
  int i, j, n;

  //Input must be odd and not less than 3.
  n = 5;
  if (n < 3 || (n % 2) == 0) return 2;

  for (i = 0; i < n; i++) {
    for (j = 0; j < n; j++){
      cout<<f(n, n - j - 1, i)*n + f(n, j, i) + 1<<"\t";
      //fflush(stdout);
    }
    cout<<"\n";
  }
  cout<<"\nMagic Constant: "<<(n*n+1)/2*n<<".\n";

  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)
