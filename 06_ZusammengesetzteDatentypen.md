<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.1.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/06_ZusammengesetzteDatentypen.md)

# Zusammengesetzte Datentypen

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Vorlesung Prozedurale Programmierung`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2021/22`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Verwendung von enums und structs in C-Programmen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/06_ZusammengesetzteDatentypen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/06_ZusammengesetzteDatentypen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Was sind *Arrays*, `struct`s und `enum`s?
* Erklären Sie den Unterschied zwischen Initalisierung und Zuweisung von Variablen!
* Wie vergleichen Sie zwei `structs`?

---------------------------------------------------------------------

**Wie weit waren wir gekommen?**

```cpp                 zusammenfassung.c
#include <stdio.h>

void get10Values(int max, int * array){
  for (int i=0; i<10; i++){
    array[i] =  rand() % max;
  }
}

void count(int * array, int * o, int * e){
  for (int i=0; i<10; i++){
    switch(array[i]%2)
    {
      case 0 :
          (*o)++;
          break;
      case 1 :
          (*e)++;
          break;
    }
  }
}

int main(void) {
  int values [] = {0,0,0,0,0,0,0,0,0,0};
  get10Values(200, values);
  for (int i=0; i<10; i++){
    printf("%d %4d\n", i, values[i]);
  }
  int o = 0, e = 0;
  count(values, &o, &e);
  printf("\nResults %d, %d", o, e);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

## Exkurs: Präcompiler Direktiven

Ein Präprozessor (seltener auch Präcompiler) ist ein Computerprogramm, das Eingabedaten vorbereitet und zur weiteren Bearbeitung an ein anderes Programm weitergibt. Der Präprozessor wird häufig von Compilern oder Interpretern dazu verwendet, einen Eingabetext zu konvertieren und das Ergebnis im eigentlichen Programm weiter zu verarbeiten.

Da sich der C-Präprozessor nicht auf die Beschreibung der Sprache C stützt, sondern ausschließlich seine ihm bekannten Anweisungen erkennt und bearbeitet, kann er auch als reiner Textersetzer für andere Zwecke verwendet werden.

![instruction-set](./images/00_Einfuehrung/compilerElements.png)<!-- width="100%" -->

Der C-Präprozessor realisiert dabei die

+ Zusammenfassung von Strings
+ Löschung von Zeilenumbrüchen und Kommentaren (Ersetzung durch Leerzeichen)
+ Whitespace-Zeichen zwischen Tokens werden gelöscht.
+ Kopieren der Header- und Quelldateien in den Quelltext kopieren (`#include`)
+ Einbinden von Konstanten (`#define`)
+ Extrahieren von Codebereichen mit einer bedingten Kompilierung (`#ifdef`, `#elseif`, ...)

Letztgenannte 3 Abläufe werden durch den Entwickler spezifiziert. Dazu bedient er
sich sogenannter Direktiven. Sie beginnen mit # und müssen nicht mit einem Semikolon abgeschlossen werden. Eventuell vorkommende Sonderzeichen in den Parametern müssen nicht escaped werden.

```c
#Direktive Parameter
```

### #include

Include-Direktiven kennen Sie bereits aus unseren Beispielprogrammen. Damit binden
wir Standardbibliotheken oder eigenen Source-Datei ein.
Es gibt zwei Arten der `#include`-Direktive, nämlich

```c
#include <Datei.h>
#include "Datei.h"
```

Die erste Anweisung sucht die Datei im Standard-Include-Verzeichnis des Compilers, die zweite Anweisung sucht die Datei zuerst im Verzeichnis, in der sich die aktuelle Sourcedatei befindet; sollte dort keine Datei mit diesem Namen vorhanden sein, sucht sie ebenfalls im Standard-Include-Verzeichnis.

Mit dem Präprozessoraufruf werden die Inhalte der Header-Files in unseren Code
kopiert. Dieser wird dadurch um ein vielfaches größer, umfasst nun aber alle
Funktionsdeklarationen, die genutzt werden sollen.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  printf("Präprozessorkrams \n")
  return EXIT_SUCCESS;
}
```

```
▶ gcc experiments.c -E -o experiments_pre.txt
```

```c
...
# 1 "/usr/include/x86_64-linux-gnu/bits/types.h" 1 3 4
# 27 "/usr/include/x86_64-linux-gnu/bits/types.h" 3 4
# 1 "/usr/include/x86_64-linux-gnu/bits/wordsize.h" 1 3 4
# 28 "/usr/include/x86_64-linux-gnu/bits/types.h" 2 3 4

typedef unsigned char __u_char;
typedef unsigned short int __u_short;
typedef unsigned int __u_int;
typedef unsigned long int __u_long;
...

# 4 "experiments.c"
int main(void) {
  printf("Präprozessorkrams \n")
  return
# 6 "experiments.c" 3 4
        0
# 6 "experiments.c"
                    ;
}
```

Warum muss vermieden werden, dass headerfiles kreuzweise eingebunden werden?

### #define

`#define` kann in drei verschiedenen Arten genutzt werden, um ein Symbol überhaupt
zu definieren, einen konkreten Wert zuzuordnen oder aber

```c
#define SYMBOL
#define KONSTANTE Wert
#define MAKRO(Parameter ...) Ausdruck
```

```c Macros.c
#include <stdio.h>
#include <stdlib.h>

#define MATH_PI 3.14
#define VOLLKREIS MATH_PI*2
#define HALBIEREN(wert) ((wert) / 2)
#define MAX_VALUE(a,b) ((a >= b) ? (a) : (b))

int main(void)
{
  float r=5;
  printf("Kreisfläche %f\n", r * r * MATH_PI);
  printf("Kreisumfang %f\n", r * VOLLKREIS);
  printf("Halber Wert von Pi %f\n", HALBIEREN(MATH_PI));
  printf("Vergleich %f\n", MAX_VALUE(MATH_PI, r));
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

In allen Fällen erfolgt lediglich eine Textersetzung im Programmcode! Dies kann
auch auf weitergehende Codefragmente ausgedehnt werden.

```cpp  Macros.c
#include <stdio.h>
#include <stdlib.h>

#define TAUSCHE(a, b, typ) { typ temp; temp=b; b=a; a=temp; }

int main(void) {
	int zahla=4, zahlb=7;
	printf("zahl A: %d\nzahl B: %d\n", zahla, zahlb);
 	TAUSCHE(zahla, zahlb, int);
	printf("zahl A: %d\nzahl B: %d\n", zahla, zahlb);
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Im Standard-C müssen bereits einige Makros im Präprozessor vordefiniert sein. Die Namen der vordefinierten Makros beginnen und enden jeweils mit zwei Unterstrichen. Die wichtigsten vordefinierten Makros sind in der folgenden Tabelle aufgelistet.

| Define    | Bedeutung                                         |
|:----------|:--------------------------------------------------|
|`__LINE__` 	| Zeilennummer innerhalb der aktuellen Quellcodedatei |
|`__FILE__` 	|Name der aktuellen Quellcodedatei  |
|`__DATE__` 	|Datum, wann das Programm compiliert wurde (als Zeichenkette)|
|`__STDC__` 	|Liefert eine 1, wenn sich der Compiler nach dem Standard-C richtet. |
|`__STDC_VERSION__` | 	Liefert die Zahl 199409L, wenn sich der Compiler nach dem  C95-Standard richtet; die Zahl 199901L, wenn sich der Compiler nach dem C99-Standard richtet. Ansonsten ist dieses Makro nicht definiert.|

Daneben gibt es weitere vordefinierte Makros, die das Betriebssystem zurückgeben.

```c       SystemMacros.c
#include <stdio.h>
#include <stdlib.h>

#define TAUSCHE(a, b, typ) { typ temp; temp=b; b=a; a=temp; }

int main(void) {
  printf("Programm wurde compiliert am ");
  printf("%s um %s.\n", __DATE__, __TIME__);

  printf("Diese Programmzeile steht in Zeile ");
  printf("%d in der Datei %s.\n", __LINE__, __FILE__);

  #ifdef __STDC__
  printf("Standard-C-Compiler!\n");
  #else
  printf("Kein Standard-C-Compiler!\n");
  #endif
  return EXIT_SUCCESS;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


## Aufzählungen

Enumerationen, kurz `enum`, dienen der Definition bestimmter Sets von Elementen,
die eine Variable überhaupt annehmen kann. Wenn wir zum Beispiel die Farben
einer Ampel in einem Programm handhaben wollen, sind dies lediglich "Rot", "Gelb"
und "Grün". Im Schachspiel sind nur die Figuren "Bauer", "Pferd", "Springer",
"Turm", "Dame" und "König" definiert.

Nun, dass können wir doch wunderbar mit unseren Präprozessordirektiven umsetzen!

```cpp     Motivation.c
#include <stdio.h>

#define MONDAY     1
#define TUESDAY    2
#define WEDNESDAY  3
#define THURSDAY   4
#define FRIDAY     5
#define SATURDAY   6
#define SUNDAY     7

int main(void) {
  int day  = SATURDAY;
  printf("Wochentag: %d\n", day);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

Allerdings ist das Ganze recht unflexibel und der Evaluation des Compilers entzogen.

Die Definition eines Aufzählungsdatentyps `enum` hat die Form wie im folgenden
Beispiel:

```cpp     Motivation.c
#include <stdio.h>

enum card {KARO, HERZ, PIK, KREUZ};            // Beispiel der Farben beim Skat
// const int kreuz=0, pik=1, karo=2, herz=3;   // Analoge Anweisung

int main(void) {
  enum card karte = KARO;
  printf("Wert der Karte: %d\n", karte);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
Möglicherweise sollen den Karten aber auch konkrete Werte zugeordnet werden,
die bestimmte Wertigkeiten reflektieren.

{{1}}
```cpp    enum.c
#include <stdio.h>

// Beispiel der Farben beim Skat
enum card {KARO=9, HERZ=10, PIK=11, KREUZ=12};

int main(void) {
  enum card karte = KARO;
  printf("Wert der Karte: %d\n", karte);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

{{1}}
An dieser Stelle sind Sie aber frei, was die eigentlichen Werte angeht. Es sind
zum Beispiel Konfigurationen möglich wie

{{1}}
```cpp
enum { KARO=9, HERZ=10, PIK=11, KREUZ=12};
enum { KARO=9, HERZ, PIK, KREUZ};            // Gleiches Resultat
enum { KARO=9, HERZ, PIK=123, KREUZ};        // implizit kreuz = 124
```

{{2}}
```cpp    enumApp.c
#include <stdio.h>

enum textformat
{
    RED = 1,
    BOLD = 2,
    ITALIC = 4,
    EXCLAMATION = 8
};

void printColor(const char text[], enum textformat chosenFormat)
{
    if (chosenFormat & RED){
        printf("Rot - ");
    }
    if (chosenFormat & BOLD){
        printf("Fett - ");
    }
    if (chosenFormat & ITALIC){
        printf("Kursiv -");
    }
    printf("%s", text);
    if (chosenFormat & EXCLAMATION)
    {
        printf(" !!!\n");
    }
}

int main(void) {
  const char text[]  = "Bergakademie Freiberg";
   enum textformat chosenFormat = RED | EXCLAMATION;
  printColor(text, chosenFormat);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

## Typdefinition mit `typedef`

Mit Hilfe des Schlüsselworts `typedef` kann für einen Datentyp, einschließlich
eines `struct`-Datentyps, ein neuer Bezeichner definiert werden:

```c
typedef Typendefinition Bezeichner;
```

Zum Beispiel kann der Datentyp `String` definiert und zur einfacheren
Variablendeklaration verwendet werden:

```
typedef char* string;
sring s = "Hallo";
```

> **Achtung!** Hinter `string` verbirgt sich noch immer ein `char *` und nicht etwa ein "echter" String-Datentyp.

Auf ein `enum` angewandt vermeidet man damit die Wiederholung des Keywords `enum`

```c
enum Day { monday=1, tuesday, ...};
void printDay(enum Day day);

// mit typdef
enum day_enum { monday=1, tuesday,...};
typedef enum day_enum Day;
void printDay(Day day);
// Alternativ in einem Rutsch
typedef enum { monday=1, tuesday,...} Day;
```

Und konkret am Beispiel:

```cpp    enumApp.c
#include <stdio.h>

enum textformat
{
    RED = 1,
    BOLD = 2,
    ITALIC = 4,
    EXCLAMATION = 8
};

typedef enum textformat format;

void printColor(const char text[], format chosenFormat)
{
    if (chosenFormat & RED){
        printf("Rot - ");
    }
    if (chosenFormat & BOLD){
        printf("Fett - ");
    }
    if (chosenFormat & ITALIC){
        printf("Kursiv -");
    }
    printf("%s", text);
    if (chosenFormat & EXCLAMATION)
    {
        printf(" !!!\n");
    }
}

int main(void) {
  const char text[]  = "Bergakademie Freiberg";
  format chosenFormat = RED | EXCLAMATION;
  printColor(text, chosenFormat);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

## Strukturen

Mit `struct` werden zusammengehörige Variablen unterschiedlicher Datentypen und
Bedeutung in einem Konstrukt zusammengefasst. Damit wird für den Entwickler der
Zusammenhang deutlich. Die Variablen der Struktur werden als Komponenten (engl.
members) bezeichnet.

Beispiele:

```cpp
struct datum
{
  int tag;
  char monat[10];
  int jahr;
};


struct Student
{
  int Matrikel;
  char name[20];
  char vorname[25];
};  // <- Hier steht ein Semikolon!
```

### Deklaration, Definition, Initialisierung und Zugriff

Und wie erzeuge ich Variablen dieses erweiterten Types, wie werden diese
initialisiert und wie kann ich auf die einzelnen Komponenten zugreifen?

Der Bespiel zeigt, dass die Definition der Variable unmittelbar nach der
`struct`-Definition oder mit einer gesonderten Anweisung mit einer vollständigen,
partiellen Initialisierung bzw. ohne Initialisierung erfolgen kann.

Die nachträgliche Veränderung einzelner Komponenten ist über Zugriff mit Hilfe
des Punkt-Operators möglich.

```cpp                           structExample.c
#include <stdio.h>
#include <string.h>

int main() {
  struct datum
  {
      int tag;
      char monat[10];
      int jahr;
  } geburtstag_1 = {18, "April", 1986};              // <- Initialisierung
                                                     //    Variable geburtstag_1
  struct datum geburtstag_2 = {13, "Januar", 2013};  // <- Initialisierung
                                                     //    Variable geburtstag_2
  geburtstag_2.tag = 13;                             // Zuweisungen
  geburtstag_2.jahr =1803;
  strcpy(geburtstag_2.monat, "April");

  // Unvollstaendige Initialisierung
  struct datum geburtstag_3 ={.monat = "September"}; // <- partielle Initialisierung

  printf("Person A wurde am %2d. %-10s %4d geboren.\n", geburtstag_1.tag, geburtstag_1.monat, geburtstag_1.jahr);
  printf("Person B wurde am %2d. %-10s %4d geboren.\n", geburtstag_2.tag, geburtstag_2.monat, geburtstag_2.jahr);
  printf("Person C wurde am %2d. %-10s %4d geboren.\n", geburtstag_3.tag, geburtstag_3.monat, geburtstag_3.jahr);
  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### Vergleich von `struct`-Variablen

Der C-Standard kennt keine Methodik um `struct`s in einem Rutsch auf Gleichheit
zu prüfen. Entsprechend ist es an jedem Entwickler eine eigene Funktion dafür zu
schreiben. Diese kann unterschiedliche Aspekte des `struct`s adressieren.

Im nachfolgenden Beispiel werden zur Überprüfung der Gleichheit die `tag`und
`monat` vergliehen. Der Vergleich wird dadurch vereinfacht, dass
wir für die Repräsentation des Monats ein `enum` verwenden. Damit entfällt
aufwändigerer Vergleich der Strings.

```cpp                           structExample.c
#include <stdio.h>

enum MONAT {Januar, Februar, Maerz, April, Mai};

struct datum
{
    int tag;
    enum MONAT monat;
    int jahr;
};

int main() {
  struct datum person_1 = {10, Januar, 2013};
  struct datum person_2 = {10, Maerz, 1956};
  person_2.monat = Januar;

  if ((person_1.tag == person_2.tag) && (person_1.monat == person_2.monat))
      printf("Oha, der gleiche Geburtstag im Jahr!\n");
  else
      printf("Ungleiche Geburtstage!\n");
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)

### Arrays und Funktionen

Wie erfolgt die Übergabe von `struct`s an Funktionen?

```cpp                           structExample.c
#include <stdio.h>

enum MONAT {Januar, Februar, Maerz, April, Mai};

struct datum
{
    int tag;
    enum MONAT monat;
    int jahr;
};

int vergleich(????){

}

int main() {
  struct datum person_1 = {10, Januar, 2013};
  struct datum person_2 = {10, Maerz, 1956};
  if (vergleich(person_1, person_2)){
    printf("Person 1 ist nach Person 2 geboren");
  }
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)


### Arrays von Strukturen

Natürlich lassen sich die beiden erweiterten Datenformate auf der Basis von
`struct` und Arrays miteinander kombinieren.

```cpp      ArrayOfStruct.c
#include <stdio.h>
#include <string.h>

#define ENTRIES 3

int main() {

  enum {Jan, Feb, Maerz, April, Mai, Juni, Juli, Aug, Sept, Okt, Nov, Dez};

  char months[12][20] = {"Januar", "Februar", "Maerz", "April",
                         "Mai", "Juni", "Juli", "August", "September",
                         "Oktober", "November", "Dezember"};

  struct datum
  {
      unsigned char tag;     // wert < 31
      unsigned char monat;   // wert < 12
      short jahr;            // wert < 2048
  };

  struct datum geburtstage [ENTRIES] = {{18, April, 1986},
                                        {12, Mai, 1820}};

  geburtstage[2].tag = 5;
  geburtstage[2].monat = Sept;
  geburtstage[2].jahr = 1905;

  for (int i=0; i<ENTRIES; i++)
    printf("%2d. %-10s %4d\n", geburtstage[i].tag,
                               months[geburtstage[i].monat],
                               geburtstage[i].jahr);

  return 0;
}
```
@LIA.eval(`["main.c"]`, `gcc -Wall main.c -o a.out`, `./a.out`)



## Beispiel des Tages

Generieren Sie mit einem C-Programm Dateien im Excelformat, um diese dann weiter
verarbeiten zu können. Dazu nutzen wir die Bibliothek `libxlsxwriter`, deren
Dokumentation und Quellcode Sie unter

[https://libxlsxwriter.github.io/index.html](https://libxlsxwriter.github.io/index.html)

finden. Die Dokumentation für die im Beispiel verwendeten Funktionen findet sich
dann für `lxw_workbook` auf der Seite

[https://libxlsxwriter.github.io/workbook_8h.html](https://libxlsxwriter.github.io/workbook_8h.html#a1cf96608a23ee4eb0e8467c15240d00b)

```cpp
#include "xlsxwriter.h"
/* Some data we want to write to the worksheet. */
struct expense {
    char item[32];
    int  cost;
};
struct expense expenses[] = {
    {"Rent", 1000},
    {"Gas",   100},
    {"Food",  300},
    {"Gym",    50},
};
int main() {
    /* Create a workbook and add a worksheet. */
    lxw_workbook  *workbook  = workbook_new("tutorial01.xlsx");
    lxw_worksheet *worksheet = workbook_add_worksheet(workbook, NULL);
    /* Start from the first cell. Rows and columns are zero indexed. */
    int row = 0;
    int col = 0;
    /* Iterate over the data and write it out element by element. */
    for (row = 0; row < 4; row++) {
        worksheet_write_string(worksheet, row, col,     expenses[row].item, NULL);
        worksheet_write_number(worksheet, row, col + 1, expenses[row].cost, NULL);
    }
    /* Write a total using a formula. */
    worksheet_write_string (worksheet, row, col,     "Total",       NULL);
    worksheet_write_formula(worksheet, row, col + 1, "=SUM(B1:B4)", NULL);
    /* Save the workbook and free any allocated memory. */
    return workbook_close(workbook);
}
```

![Resultat](./images/06_ZusammengesetzteDatentypen/excelLib.png)
