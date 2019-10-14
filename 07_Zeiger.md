<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md
-->


# Vorlesung VII - Zeiger

**Fragen an die heutige Veranstaltung ...**

* Erklären Sie die Idee des Zeigers in der Programmiersprache C.
* Welche Vorteile ergeben sich, wenn eine Variable nicht mit dem gti Wert
  sondern über die Adresse übergeben wird?
* Welche Funktion hat der Adressoperator `&`?
* Welche Gefahr besteht bei der Initialisierung von Zeigern?
* Was ist ein `NULL`-Zeiger und wozu wird er verwendet?
* Wie gibt man die Adresse, auf die ein Zeiger gerichtet ist, mit `printf` aus?
* Erläutern Sie die mehrfache Nutzung von `*` im Zusammenhang mit der Arbeit
  von Zeigern.
* In welchem Kontext ist die Typisierung von Zeigern von Bedeutung?

---------------------------------------------------------------------
Aktuelle Vorlesung im Versionsmanagementsystem GitHub:

[https://github.com/SebastianZug/CCourse/blob/master/07_Zeiger.md](https://github.com/SebastianZug/CCourse/blob/master/07_Zeiger.md)

---------------------------------------------------------------------

**Wie weit sind wir schon gekommen?**


| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | `auto`         | `double` | `int`      | `struct` | `break`    |
|             | `else`         | `long`   | `switch`   | `case`   | `enum`     |
|             | `register`     | `typedef`| `char`     | `extern` | `return`   |
|             | union          | `const`  | `float`    | `short`  | `unsigned` |
|             | `continue`     | `for`    | `signed`   | `void`   | `default`  |
|             | `goto`         | `sizeof` | `volatile` | `do`     | `if`       |
|             | `static`       | `while`  |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | `inline` | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

---

{{1}}
Standardbibliotheken

{{1}}
| Name         | Bestandteil | Funktionen                           |
|:-------------|:------------|:-------------------------------------|
| `<stdio.h>`  |             | Input/output                         |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite |
| `<float.h>`  |             | Parameter der Floatwerte             |
| `<limits.h>` |             | Größe der Basistypen                 |
| `<fenv.h>`   |             | Verhalten bei Typumwandlungen        |

{{1}}
[C standard library header files](https://en.cppreference.com/w/c/header)


## 0. Arrays & Schleifen

Realisieren Sie eine Look-Up-Table für die Berechnung des Sinus von Gradwerten.

Quelle: [http://www2.hs-fulda.de/~klingebiel/c-stdlib/math.htm](http://www2.hs-fulda.de/~klingebiel/c-stdlib/math.htm)

``` c
#include <stdio.h>
#define _USE_MATH_DEFINES
#include <math.h>

int main(void) {
  double sin_values[360] = {0};
  for(int i=0; i<360; i++) {
    sin_values[i] = sin(i*M_PI/180);
  }

  int angle = 90;
  printf("sin %d, %lf\n",angle, sin_values[angle]);
  return 0;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)

````
 ┏━━━━━━━┳━━━━━━━┳━━━━━━━┳╸╸╸╸╸╸╸┳━━━━━━━┳━━━━━━━┳╸╸╸╸╸╸╸
 ┃ Index ┃   0   ┃   1   ┃       ┃   89  ┃   90  ┃
 ┣━━━━━━━╋━━━━━━━╋━━━━━━━╋╸╸╸╸╸╸╸╋━━━━━━━╋━━━━━━━╋╸╸╸╸╸╸╸
 ┃ Wert  ┃ 0.000 ┃ 0.017 ┃       ┃ 0.999 ┃ 1.000 ┃
 ┗━━━━━━━┻━━━━━━━┻━━━━━━━┻╸╸╸╸╸╸╸┻━━━━━━━┻━━━━━━━┻╸╸╸╸╸╸╸
````

## 1 Zeiger in C

Bisher umfassten unserer Variablen als Datencontainer Zahlen oder Buchstaben.
Das Konzept des Zeigers (englisch Pointer) erweitert das Spektrum der Inhalte
auf Adressen.

An dieser Adresse können entweder Daten, wie Variablen oder Objekte, aber auch
Programmcodes (Anweisungen) stehen. Durch Dereferenzierung des Zeigers ist es
möglich, auf die Daten oder den Code zuzugreifen.


<!--
style=" width: 70%;
        max-width: 400x;
        min-width: 400px;
        display: block;
        margin-left: auto;
        margin-right: auto;"
-->
````
  Variablen-     Speicher-      Inhalt
  name           addresse
                                ┏━━━━━━━━━━┓
                 0000           ┃          ┃
                                ┣━━━━━━━━━━┫
                 0001           ┃          ┃
                                ┣━━━━━━━━━━┫
  a   ------>    0002       +---┃ 00001007 ┃
                          z |   ┣━━━━━━━━━━┫
                 0003     e |   ┃          ┃
                          i |   ┣━━━━━━━━━━┫
                 ....     g |   ┃          ┃
                          t |   ┣━━━━━━━━━━┫
                 1005       |   ┃          ┃
                          a |   ┣━━━━━━━━━━┫
                 1006     u |   ┃          ┃
                          f |   ┣━━━━━━━━━━┫
  b   ------>    1007    <--+   ┃ 01101101 ┃
                                ┣━━━━━━━━━━┫
                 1008           ┃          ┃
                                ┣━━━━━━━━━━┫
                 ....           ┃          ┃
````


Welche Vorteile ergeben sich aus der Nutzung von Zeigern, bzw. welche
Programmiertechniken lassen sich realiseren:
* dynamische Verwaltung von Speicherbereichen,
* Übergabe von Datenobjekte an Funktionen via "call-by-reference" [^1],
* Übergabe von Funktionen als Argumente an andere Funktionen,
* Umsetzung rekursiver Datenstrukturen wie Listen und Bäume.

[^1]: Der Vollständigkeithalber sei erwähnt, dass C anders als C++ keine Referenzen im eigentlichen Sinne kennt. Hier ist die Übergabe der Adresse einer Variablen als Parameter gemeint und nicht das Konstrukt "Reference".

### Definition von Zeigern

Die Definition eines Zeigers besteht aus dem Datentyp des Zeigers und dem
gewünschten Zeigernamen. Der Datentyp eines Zeigers besteht wiederum aus dem
Datentyp des Werts auf den gezeigt wird sowie aus einem Asterisk. Ein Datentyp
eines Zeigers wäre also z. B. `double*`.

``` c
/* kann eine Adresse aufnehmen, die auf einen Wert vom Typ Integer zeigt */
int* zeiger1;
/* das Leerzeichen kann sich vor oder nach dem Stern befinden */
float *zeiger2;
/* ebenfalls möglich */
char * zeiger3;
/* Definition von zwei Zeigern */
int *zeiger4, *zeiger5;
/* Definition eines Zeigers und einer Variablen vom Typ Integer */
int *zeiger6, ganzzahl;
```

### Initialisierung

> **Merke:** Zeiger müssen vor der Verwendung initialisiert werden.

Der Zeiger kann initialisiert werden durch die Zuweisung:
* der Adresse einer Variable, wobei die Adresse mit Hilfe des Adressoperators
  `&` ermittelt wird,
* eines Arrays,
* eines weiteren Zeigers oder
* des Wertes von `NULL`.

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a = 0;
  int * ptr_a = &a;       /* mit Adressoperator */

  int feld[10];
  int * ptr_feld = feld;  /* mit Array */

  int * ptr_b = ptr_a;    /* mit weiterem Zeiger */

  int * ptr_Null = NULL;  /* mit NULL */

  printf("Pointer ptr_a    %p\n", ptr_a);
  printf("Pointer ptr_feld %p\n", ptr_feld);
  printf("Pointer ptr_b    %p\n", ptr_b);
  printf("Pointer ptr_Null %p\n", ptr_Null);
  return EXIT_SUCCESS;
}
```
@Rextester.C


{{1}}
Die konkrete Zuordnung einer Variablen im Speicher wird durch den Compiler und
das Betriebssystem bestimmt. Entsprechend kann die Adresse einer Variablen nicht
durch den Programmierer festgelegt werden. Ohne Manipulationen ist die Adresse
einer Variablen über die gesamte Laufzeit des Programms unveränderlich, ist aber
bei mehrmaligen Programmstarts unterschiedlich.

{{1}}
Ausgaben von Pointer erfolgen mit `printf("%p", ptr)`, es wird dann eine
hexadezimale Adresse ausgegeben.

{{1}}
Zeiger können mit dem "Wert" `NULL` als ungültig markiert werden. Eine
Dereferenzierung führt dann meistens zu einem Laufzeitfehler nebst
Programmabbruch. NULL ist ein Macro und wird in mehreren Header-Dateien
definiert (mindestens in `stddef.h`). Die Definition ist vom Standard
implementierungsabhängig vorgegeben und vom Compilerhersteller passend
implementiert, z. B.

{{1}}
``` c
#define NULL 0
#define NULL 0L
#define NULL (void *) 0
```

{{2}}
Und umgekehrt, wie erhalten wir den Wert, auf den der Pointer zeigt? Hierfür
benötigen wir den *Inhaltsoperator* `*`.

{{2}}
``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a = 15;
  int * ptr_a = &a;
  printf("Wert von a                     %d\n", a);
  printf("Pointer ptr_a                  %p\n", ptr_a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", *ptr_a);
  *ptr_a = 10;
  printf("Wert von a                     %d\n", a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", *ptr_a);
  return EXIT_SUCCESS;
}
```
@Rextester.C


### Fehlerquellen

Fehlender Adressopertor bei der Zuweisung

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a = 5;
  int * ptr_a;
  ptr_a = a;
  printf("Pointer ptr_a                  %p\n", ptr_a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", *ptr_a);
  return EXIT_SUCCESS;
}
```
@Rextester.C

{{1}}
Fehlender Dereferenzierungsoperator beim Zugriff

{{1}}
``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a = 5;
  int * ptr_a = &a;
  printf("Pointer ptr_a                  %p\n", (void*)ptr_a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", ptr_a);
  return EXIT_SUCCESS;
}
```
@Rextester.C

{{2}}
Uninitialierte Pointer zeigen "irgendwo ins nirgendwo"!

{{2}}
``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int * ptr_a;
  *ptr_a = 10;
  // korrekte Initalisierung
  // int * ptr_a = NULL;
  // Prüfung auf gültige Adresse
  // if (ptr_a != NULL) *ptr_a = 10;
  printf("Pointer ptr_a                  %p\n", (void*)ptr_a);
  printf("Wert hinter dem Pointer ptr_a  %d\n", *ptr_a);
  return EXIT_SUCCESS;
}
```
@Rextester.C

### Zeigerarithmetik

Zeiger können manipuliert werden, um variabel auf Inhalte im Speicher zuzugreifen.
Wie groß ist aber eigentlich ein Zeiger und warum muss er typisiert werden?

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char   *v;
  int    *w;
  float  *x;
  double *y;
  void   *z;

  printf("char\t int\t float\t double\t void\n");
  printf("%lu\t %lu\t %lu\t %lu\t %lu \n",
      sizeof(v),sizeof(w), sizeof(x), sizeof(y), sizeof(z));
  printf("%lu\t %lu\t %lu\t %lu\t %lu \n",
      sizeof(*v),sizeof(*w), sizeof(*x), sizeof(*y), sizeof(*z));
   return EXIT_SUCCESS;
}
```
@Rextester.C

{{1}}
Die Zeigerarithmetik erlaubt:

{{1}}
* Ganzzahl-Additionen
* Ganzzahl-Substraktionen
* Inkrementierungen `ptr_i--;`
* Dekrementierungen `ptr_i++;`

{{1}}
Der Compiler wertet dabei den Typ der Variablen aus und inkrementiert bzw.
dekrementiert die Adresse entsprechend.

{{1}}
``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a[] = {0,1,2,3,4,5};
  int *ptr_a = a;
  printf("Pointer ptr_a               %p\n", ptr_a);
  int *ptr_b;
  ptr_b = ptr_a + 1;
  ptr_b ++;
  printf("Pointer ptr_b               %p\n", ptr_b);
  printf("Differenz ptr_b -  ptr_a    %ld\n", (long)(ptr_b - ptr_a));
  printf("Differenz ptr_b -  ptr_a    %ld\n", (long)ptr_b - (long)ptr_a);

  printf("Wert hinter Pointer ptr_b   '%d'\n", *ptr_b);

  return EXIT_SUCCESS;
}
```
@Rextester.C


{{2}}
Was bedeutet das im Umkehrschluss? Eine falsche Deklaration bewirkt ein
falsches "Bewegungsmuster" über dem Speicher.

{{2}}
``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a[] = {6,7,8,9};
  char * ptr_a = a;
  for (int i=0; i<sizeof(a)/sizeof(int)*4; i++){
      printf("ptr_a %p -> ", ptr_a);
      printf("%d\n", *ptr_a);
      ptr_a++;
  }
  return EXIT_SUCCESS;
}
```
@Rextester.C


### Vergleiche von Zeigern

Pointer können natürlich nicht nur manipuliert sondern auch verglichen werden.
Dabei sei noch mal darauf verwwiesen, dass dabei die Adressen und nicht die
Werte evaluiert werden.

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  int a[] = {6,7,6,9};
  int * ptr_a = a;
  int * ptr_b = &a[2];
  printf("ptr_a %p -> %d \n", (void*)ptr_a, *ptr_a);
  printf("ptr_b %p -> %d \n", (void*)ptr_b, *ptr_b);
  if (*ptr_a == *ptr_b) printf("Werte sind gleich!\n");
  // Im Unterschied dazu
  if (ptr_a == ptr_b) printf("Adressen sind gleich!\n");
  else printf("Adressen sind ungleich!\n");
  ptr_a += 2;
  printf("Nun zeigt ptr_a auf %p\n", (void*)ptr_a);
  if (ptr_a == ptr_b) printf("Jetzt sind die Adressen gleich!\n");
  else printf("Adressen sind ungleich!\n");
  return EXIT_SUCCESS;
}
```
@Rextester.C


### Zeiger auf Felder
<!--
comment: sizeof(char) == 1 ... deshalb kann dieser Anteil entfallen
         sizeof(text)/sizeof(char)
         Die Warning Message deutet darauf hin, dass nicht klar ist, ob
         char ein Vorzeichen hat. Ein Ersetzen mit int illustriert dies.
         Danach kann unsigned eingefügt werden ...
-->

Es gibt zwei Möglichkeiten auf ein Array zuzugreifen, über den Indexoperator
`[]` oder die Zeiger-basierte Adressierung der Elemente.

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  char text[] = "ProzProg\0";
  char *ptr_text = text;

  // Indizierte Adressierung
  for(int i=0; i<sizeof(text); i++) {
    printf("%c ", text[i]);
  }
  // Zeiger + Offset
  for(int i=0; i<sizeof(text); i++) {
    printf("%c ", *(ptr_text + i));
  }
  // Verschiebung des Zeigers
  for(int i=0; i<sizeof(text); i++, ptr_text++) {
    printf("%c ", *(ptr_text));
  }
  return EXIT_SUCCESS;
}
```
@Rextester.C


**Achtung:** Es gibt erhebliche Unterschiede bei der Zeiger-basierten
Adressierung von Arrays im Hinblick auf das "Ziel".

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int arr[5] = {0};
  printf("Zeiger auf arr    %p\n", arr);
  printf("Zeiger auf arr[0] %p\n", &arr[0]);
  printf("Zeiger &arr       %p\n", &arr);

  printf("Zeiger auf arr+1  %p\n", arr+1);
  printf("Zeiger &arr+1     %p\n", &arr+1);
  return EXIT_SUCCESS;
}
```
@Rextester.C


Offenbar zeigt der Pointer `arr` auf den ersten Eintrag des Arrays und verschiebt
sich entsprechend dem Datentyp `int` um 4 Byte. Anders für die Referenz auf das
gesamte Array `&arr`. Hier wird bei der Inkrementierung das gesamte Array
übersprungen. Folglich erreicht man den letzten Eintrag mit

``` c
int *ptr_last_entry = (&arr + 1) - 1;
```

### Zeiger für die Parameterübergrabe
Mit Hilfe des Zeigers wird in C die "call-by-reference"- Parameterübergabe
realisiert. In der Liste der formalen Parameter wird ein Zeiger eines
passenden Typs definiert. Beim Funktionsaufruf wird als Argument statt
Variable eine Adresse übergeben. Beachten Sie, dass für den Zugriff auf den Inhalt des Zeigers (einer Adresse) der Inhaltsoperator `*` benötigt wird.

``` c
#include <stdio.h>
#include <stdlib.h>

void inkrementieren(int *variable){
  (*variable)++;
}

int main(void) {
  int a=0;
  inkrementieren(&a);
  printf("a = %d\n", a);
  inkrementieren(&a);
  printf("a = %d\n", a);
  return EXIT_SUCCESS;
}
```
@Rextester.C


Die Adresse einer Variable wird mit dem Adressenoperator `&`
ermittelt. Weiterhin kann an den Zeiger-Parameter eine Array-Variable
übergeben werden.

``` c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double sinussatz(double *lookup_sin, int angle, double opositeSide){
  printf("Größe des Arrays %ld\n", sizeof(*lookup_sin));
  return opositeSide*lookup_sin[angle];
}

int main(void) {
  double sin_values[360] = {0};
  for(int i=0; i<360; i++) {
    sin_values[i] = sin(i*M_PI/180);
  }
  printf("Größe des Arrays %ld\n", sizeof(sin_values));
  printf("Result =  %lf \n",sinussatz(sin_values, 30, 20));
  return EXIT_SUCCESS;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)

Der Vorteil der Verwendung der Zeiger als Parameter besteht darin, dass
in der Funktion mehrere Variablen auf eine elegante Weise verändert
werden können. Die Funktion hat somit quazi mehrere Ergebnisse.

``` c
#include <stdio.h>
#include <stdlib.h>

void tauschen(char *anna, char *hanna){
  char h=*anna;
  *anna=*hanna;
  *hanna=h;
}

int main(void) {
  char anna='A',hanna='H';
  printf("%c und %c\n", anna,hanna);
  tauschen(&anna,&hanna);
  printf("%c und %c\n", anna,hanna);;
  return EXIT_SUCCESS;
}
```
@Rextester.C

### Zeiger als Rückgabewerte

Analog zur Bereitstellung von Parametern entsprechend dem "call-by-reference"
Konzept können auch Rückgabewerte als Pointer vorgesehen sein. Allerdings
sollen Sie dabei aufpassen ...

``` c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int * doCalc(int *wert) {
  int a = *wert + 5;
  return &a;
}

int main(void) {
  int b = 5;
  printf("Irgendwas stimmt nicht %d", * doCalc(&b) );
  return EXIT_SUCCESS;
}
```
@Rextester.C

Mit dem Beenden der Funktion werden deren lokale Variablen vom Stack gelöscht.
Um diese Situation zu handhaben können Sie zwei Lösungsansätze realisieren.

**Variante 1**  Sie übergeben den Rückgabewert in der Parameterliste.

``` c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

void kreisflaeche(double durchmesser, double *flaeche) {
  *flaeche = M_PI * pow(durchmesser / 2, 2);
  // Hier steht kein return !
}

int main(void) {
  double wert = 5.0;
  double flaeche = 0;
  kreisflaeche(wert, &flaeche);
  printf("Die Kreisfläche beträgt für d=%3.1lf[m] %3.1lf[m²] \n", wert, flaeche);
  return EXIT_SUCCESS;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)

{{1}}
**Variante 2** Rückgabezeiger adressiert mit `static` bezeichnete Variable. Aber Achtung: funktieoniert nicht bei rekursiven Aufrufen.

{{1}}
``` c
#include <stdio.h>
#include <stdlib.h>

int* cumsum(int wert) {
  static int sum = 0;
  sum += wert;
  return &sum;
}

int main(void) {
  int wert = 2;
  int *sum;
  sum=cumsum(wert);
  sum=cumsum(wert);
  printf("Die Summe ist : %d\n", *sum);
  sum=cumsum(wert);
  printf("Die Summe ist : %d\n", *sum);
  return EXIT_SUCCESS;
}
```
@Rextester.C

{{2}}
**Variante 3** Für den Rückgabezeiger wird der Speicherplatz mit `malloc` dynamisch angelegt (dazu später mehr).

{{2}}
``` c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

double* kreisflaeche(double durchmesser) {
  double *flaeche=(double*)malloc(sizeof(double));
  *flaeche = M_PI * pow(durchmesser / 2, 2);
  return flaeche;
}

int main(void) {
  double wert = 5.0;
  double *flaeche;
  flaeche=kreisflaeche(wert);
  printf("Die Kreisfläche beträgt für d=%3.1lf[m] %3.1lf[m²] \n", wert, *flaeche);
  return EXIT_SUCCESS;
}
```
@Rextester.eval(@C, false, ,`-Wall -std=gnu99 -O2 -o a.out source_file.c -lm`)

### `void`-Zeiger

`void`-Zeiger ist zu jedem anderen Daten-Zeiger kompatibel und wird
verwendet, wenn der Datentyp des Zeigers noch nicht feststeht.
In C ist die implizite und explizite Typumwandlung des `void`-Zeigers in einen anderen Typ möglich.

```c
int a=5;
void *pv=&a;
int *pi=pv;
int *pii=(int*)pv;
```
Vorwiegend findet ein `void`-Zeiger Anwendung in Funktionen, die mit
unterschiedlichen Zeigern aufgerufen werden bzw. unterschiedliche Zeiger
als einen Rückgabewert liefern.

Beispiele:
* Die Funktion `memcmp()` (`<string.h>`) zum Vergleichen von Zeichenketten erlaubt die Verwendung mit `char*` und `int*`.
* Das Ergebnis der Funktion `malloc()` (`<stdlib.h>`) zum Bereistellen des Speicherplatzes kann in `char*`, `int*`, `double*` usw. umgewandelt werden.

```c
int memcmp (const void*, const void*, size_t);
void *malloc(size_t size);
```

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
   char str1[]="abcde";
   char str2[]="ABCDE";

   if(memcmp(str1,str2, sizeof(str1)) == 0)
      printf("Strings sind gleich\n");
   else
      printf("Strings sind nicht gleich\n");

   return EXIT_SUCCESS;
}
```
@Rextester.C


## 2. Beispiel der Woche

Gegeben ist ein Array, dass eine sortierte Reihung von Ganzzahlen umfasst.
Geben Sie alle Paare von Einträgen zurück, die in der Summe 18 ergeben.

Die intuitive Lösung entwirft einen kreuzweisen Verleich aller Kombinationen
der Einträge im Array. Haben Sie eine bessere Idee?

```c
#include <stdio.h>
#include <stdlib.h>

#define ZIELWERT 18

int main(void)
{
  int a[] = {1, 2, 5, 7, 9, 10, 12, 13, 16, 17, 18, 21, 25};
  int *ptr_left = a;
  int *ptr_right = (int *)(&a + 1) - 1;
  printf("Value left %3d right %d\n-----------------------\n", *ptr_left, * ptr_right);
  do{
    printf("Value left %3d right %d", *ptr_left, * ptr_right);
    if (*ptr_right + *ptr_left == ZIELWERT){
       printf(" -> TREFFER");
    }
    printf("\n");
    if (*ptr_right + *ptr_left >= ZIELWERT) ptr_right--;
    else ptr_left++;
  }while (ptr_right != ptr_left);
  return EXIT_SUCCESS;
}
```
@Rextester.C
