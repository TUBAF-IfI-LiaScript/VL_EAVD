<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md

-->

# Vorlesung XI - Standardbibliotheken

**Fragen an die heutige Veranstaltung ...**

* Welche Konzepte sind in der Standardbibliothek implementiert, die die Zeit abbilden?
* Welche Vor- und Nachteile haben diese Formate?
* Benennen Sie die unterschiedlichen Befehle mit denen der Programmablauf beendet werden kann.
* Erläutern Sie die Besonderheit beim Umgang mit `strings` verglichen mit anderen Arrays.
* Nach welchem Algorithmus arbeitet die `qsort` funktion, die Bestandteil der Standardbibliothek ist.
* Wie setzen Sie das `assert` Makro im Rahmen Ihres Entwicklungsprozesses ein?
* Welche Aspkekte sind bei der Nutzung von Zufallszahlen auf der Basis der `rand` zu berücksichtigen.
* Wie mappen Sie die Ausgaben von `rand` auf einen beliebigen Bereich von Werten?

---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/11_Standardbibliothek.md

---------------------------------------------------------------------

**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

| Standard    |                |          |            |          |            |
|:------------|:---------------|:---------|:-----------|:---------|:-----------|
| **C89/C90** | auto           | `double` | `int`      | `struct` | `break`    |
|             | `else`         | `long`   | `switch`   | `case`   | `enum`     |
|             | register       | typedef  | `char`     | extern   | return     |
|             | union          | const    | `float`    | `short`  | `unsigned` |
|             | `continue`     | `for`    | `signed`   | `void`   | `default`  |
|             | `goto`         | `sizeof` | volatile   | `do`     | `if`       |
|             | static         | `while`  |            |          |            |
| **C99**     | `_Bool`        | _Complex | _Imaginary | inline   | restrict   |
| **C11**     | _Alignas       | _Alignof | _Atomic    | _Generic | _Noreturn  |
|             |_Static\_assert | \_Thread\_local | |   |          |            |

---

Standardbibliotheken

| Name         | Bestandteil | Funktionen                              |
|:-------------|:------------|:----------------------------------------|
| `<stdio.h>`  |             | Input/output (`printf`)                 |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite    |
| `<float.h>`  |             | Parameter der Floatwerte                |
| `<limits.h>` |             | Größe der Basistypen                    |
| `<fenv.h>`   |             | Verhalten bei Typumwandlungen           |
| `<string.h>` |             | Stringfunktionen                        |
| `<math.h>`   |             | Mathematische Funktionen und Konstanten |

https://en.cppreference.com/w/c/header


## 1. Standardbibliothek als Ganzes

Die Standardbibliothek umfasst Funktionen und Makros, die für die Entwicklung
vereinfachen, bzw. die Anpassung auf die konkrete Architektur übernehmen.

| Name         | Bestandteil | Funktionen                              |
|:-------------|:------------|:----------------------------------------|
| `<stdio.h>`  |             | Input/output (`printf`)                 |
| `<stdint.h>` | (seit C99)  | Integer Datentypen mit fester Breite    |
| `<float.h>`  |             | Parameter der Floatwerte                |
| `<limits.h>` |             | Größe der Basistypen                    |
| `<fenv.h>`   |             | Verhalten bei Typumwandlungen           |
| `<string.h>` |             | Stringfunktionen                        |
| `<math.h>`   |             | Mathematische Funktionen und Konstanten |

Wie werden die entsprechenden Funktionen genutzt?

```cpp                     libusage.c
int main(void)
{
    printf("Hello World\n");

    return(EXIT_SUCCESS);
}
```@Rextester.C

In folgendem Beispiel werden mathematische Funktionen der `math.h` genutzt. Aus
historischen Gründen muss dabei im Fall einer echten Berechnung zur Laufzeit
die entsprechende Bibliothek gelinkt werden.

```cpp                     mathOperations.c
#include <stdio.h>
#include <math.h>

int main(void)
{
    double a=3.14;
    printf("Sin von 3.14 %f\n", sin(a));
    return 0;
}
```

In der vorliegenden Form erfolgt die Berechnung statisch zur Compilezeit.
Wandeln Sie das Beispiel so ab, dass eine "echte" Berechnung notwenig wird.

```bash @output
▶ gcc experiments.c
/tmp/cctWOjnA.o: In function `main':
experiments.c:(.text+0x34): undefined reference to `pow'
collect2: error: ld returned 1 exit status
```

Der Aufruf des Compilers muss dann entsprechend angepasst werden:

```bash @output
▶ gcc experiments.c -lm
```

> The functions in stdlib.h and stdio.h have implementations in libc.so (or libc.a for static linking), which is linked into your executable by default (as if -lc were specified). GCC can be instructed to avoid this automatic link with the -nostdlib or -nodefaultlibs options.


### time.h

Die Definitionsdatei <time.h> vereinbart Typen und Funktionen zum Umgang mit
Datum und Uhrzeit. Manche Funktionen verarbeiten die Ortszeit, die von der
Kalenderzeit zum Beispiel wegen einer Zeitzone abweicht. Zwei Methoden - time
und clock können benutzt werden, um den aktuellen Zeitwert auszulesen und auf
einen der folgenden Datentypen abzubilden:

| Name      | Format                                      |
|:----------|:--------------------------------------------|
| `clock_t` | Relatives Format zur Zeitangabe bezogen auf den Prozess |
| `time_t`  | Sekunden seit dem 1. Januar 1970 00:00 UTC  |
| `tm`      | struct mit Einträgen für Sekunden - Jahre   |

Die Darstellung von `tm` umfasst dabei folgende Elemente

| Member	| Type|	Meaning	Range |
| `tm_sec`	| int	| seconds after the minute	0-61|
| `tm_min`| int	| minutes after the hour	0-59|
| `tm_hour`	| int	| hours since midnight	0-23|
| `tm_mday`	| int	| day of the month	1-31|
| `tm_mon`	| int	| months since January	0-11|
| `tm_year`	| int	| years since 1900|
| `tm_year`	| int	| years since 1900|
| `tm_wday`	| int	| days since Sunday	0-6|
| `tm_yday`	| int	| days since January 1	0-365|
| `tm_isdst`| int	| Daylight Saving Time flag|

Die Funktionen

```cpp
time_t time(time_t *tloc);
clock_t clock(void);
```

liefern als Rückgabewert eine Zeitangabe. `localtime()` wandelt die Kalenderzeit der Adresse time_t \*zeitzeiger in lokale Ortszeit um, `gmtime()` dagegen wandelt die Kalenderzeit in die UTC-Zeit.

**Anwendung I - Laufzeitmessung mit clock()**

```cpp                     printDuration.c
#include <stdio.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>

int main(void) {
  clock_t start = clock();
  long result = 0;
  int i;
  for(i=0; i<1000000; ++i){
      result = result + 1;
      result = log(pow(result, 2));
  }
  printf("%d Additionen von 1 ergeben %ld\n", i-1, result);
  clock_t end = clock();
  double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

  printf("Der Rechner braucht dafür %f Sekunden \n", cpu_time_used);
  printf("Die Taktrate beträgt %ld Ticks/Sekunde \n",  CLOCKS_PER_SEC);
  return EXIT_SUCCESS;
}
```@Rextester.eval(@C,false, ,`-Wall -std=gnu99 -O2 -lm -o a.out source_file.c`)

Welchen Fehler sehen Sie den gedanklichen Fehler im obrigen Programm?

**Anwendung II - Zeitbestimmung mit time()**

Die Funktion `time_t time(time_t *arg)` gibt die aktuelle Kalenderzeit als
Epochenausdruck zurück. Die Funktion `ctime(&current_time)` bildet sie auf einen  
string ab.

```cpp                     printTime.c
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    time_t current_time;
    char* c_time_string;
    /* Obtain current time. */
    current_time = time(NULL);
    printf("Current time is %ld \n", current_time);

    if (current_time == ((time_t)-1)){
        printf("Failure to obtain the current time.\n");
        exit(EXIT_FAILURE);
    }

    /* converts a time_t value to a textual representation */
    c_time_string = ctime(&current_time);
    if (c_time_string == NULL){
        printf("Failure to convert the current time.\n");
        exit(EXIT_FAILURE);
    }
    printf("Current time is %s", c_time_string);
    return(EXIT_SUCCESS);
}
```@Rextester.C

**Anwendung 3 - Ausgabe von Zeitformaten**

Variantenreichere Ausgaben von Zeitangaben können mit strftime` erzeugt werden.
Die möglichkeiten umfassen dabei:

| Format   | Bedeutung                                | Beispiel |
|:---------|:-----------------------------------------|:---------|
| %a       | abgekürzter Wochentagsname               |	Thu      |
| %A       | Wochentagsname                           | Thursday |
| %c       | volle Datums- und Zeitrepresentation    |	Thu Aug 23 14:55:02 2001 |
| %p       | AM oder PM Angabe 	PM                    | PM       |
| %W       | Wochennummer mit dem ersten Montag als ersten Tag der ersten Woche (00-53) | 	34  |

https://www.proggen.org/doku.php?id=c:lib:time:strftime

```cpp                     printTime.c
#include <time.h>
#include <stdlib.h>
#include <stdio.h>

int main(void)
{
    time_t current_time;
    struct tm * timeInfo;
    char        buffer[80];

    current_time = time(NULL);
    timeInfo = localtime( &current_time );

    printf("%d\n", timeInfo->tm_year);

    strftime( buffer, 80, "Es ist nun %H Uhr, %M Minuten.", timeInfo );
    printf("%s", buffer);
    strftime( buffer, 80, "%c", timeInfo );
    printf("%s", buffer);
    return(EXIT_SUCCESS);
}
```@Rextester.C

### assert.h

Mit dem assert-Makro aus dem Headerfile `assert.h` fügt man Testpunkte in ein Program ein,
die dann zur Laufzeit ausgewertet werden.

```cpp
void assert(int expression)
```

hat `expression` den Wert Null wenn ausgeführt wird, dann gibt der assert-Makro
auf `stderr` etwa folgende Meldung aus:

```bash @output
 Assertion failed: expression, file filename, line nnn
```

Anschließend wird die Ausführung durch Aufruf von abort abgebrochen. Der Dateiname der Programmquelle sowie die Zeilennummer stammen von den Prozessor-Makros `__FILE__` und `__LINE__`.

Wenn beim **Einfügen** von <assert.h> ein Makroname `NDEBUG` definiert ist, wird der assert-Makro ignoriert.

Beispiel: Entwickeln Sie eine Funktion, die die mathematische Funktion

$$f(a,b)=\sqrt{\frac{a}{b}}$$

implementiert

```cpp                     assertBeispiele.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
//#define NDEBUG
#include <assert.h>

float myFunktion(int a, int b);

int main(void){
    int a = 7;
    for (int b=-a; b<=a; b++){
      assert(a==b);
      printf("f(%2d, %2d) = %2.4f \n", a, b,  myFunktion(a, b));
    }
    return(EXIT_SUCCESS);
}

float myFunktion(int a, int b){
  // precondition
  assert(b==0);
  assert(a/b>0);
  double y = sqrt(a/b);
  return y;
}

```

Welchen Vorteile bringt das `assert` Makro gegenüber alternativen printf Ausgaben
mit sich? Wie könnte man ein gleiches Verhalten ohne Spuren im Code zu hinterlassen
mit printf umsetzen?

### stdlib.h

**Beenden eines Programmes**

`stdlib.h` umfasst unter anderem die Methoden zur Beendigung des Programms und
unterscheidet dabei zwischen

| exit | beliebige Position im Programmcode, führt zum Leeren der Puffer, dem Schließen von Datein, Löschung von Daten |
| abort | abnormaler Abbruch mit Fehlerausgabe  |
| return | kann nur am Ende der main stehen, Verhalten äquivalent zu exit |

Mit `aexit.h` kann das geordnete Verlassen eines Programmes koordiniert werden.
Dabei wird ein Stack von Funktionshandlern angelegt, die nach und nach abgearbeitet
werden. Die Programmbereiche, die nach dem exit-Aufruf folgen, werden logischerweise
nie ausgeführt.


```cpp                     aexitBeispiele.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char *memPtr;

void writeLogMessage(void) {
  time_t current_time;
  struct tm * timeInfo;
  char        buffer[80];

  current_time = time(NULL);
  timeInfo = localtime( &current_time );
  strftime( buffer, 80, "%c", timeInfo );
  printf("%s - Programmabbruch mit unbekannter Ursache\n", buffer);
}

void free_malloc(void) {
   /* Wurde überhaupt Speicher reserviert? */
   if(memPtr == NULL)
      printf("Kein Speicher war reserviert!!!\n");
   else {
      free(memPtr);
      printf("Speicher wurde freigegeben!!\n");
   }
}

int main(void) {
   memPtr =(char *) malloc(10000);
   if(memPtr==NULL)
      printf("Konnte keinen Speicher reservieren\n");

   if(atexit (free_malloc) != 0)
      printf("Konnte Funktionshandler nicht einrichten\n");
   atexit(writeLogMessage);
   /* Hier passieren viele Operationen über unserem Array. */

   exit(EXIT_FAILURE);
   printf("Wird nicht mehr ausgegeben\n");
   return EXIT_SUCCESS;
}
```@Rextester.C

**Erzeugung von Zufallszahlen**

Für das Testen eines Algorithmus werden häufig Zufallszahlen herangezogen, um
variierende Eingangsdaten zu simulieren. Die Funktion

```cpp
int rand(void);
```

gibt dafür einen Wert zwischen 0 und `RAND_MAX` zurück. Damit sind entsprechend
nur Gleichverteilungen möglich. Andere Konfigurationen lassen sich über eine
entsprechende Modulo-Operation realisieren

```cpp
rand() % ((y + 1) - x) + x   // x<= out <=y
```

```c randomValues.c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
   printf("Der Wert von RAND_MAX beträgt %d\n", RAND_MAX);
   for(int i = 0; i < 5; i++)
      printf("Die Zufallszahl lautet %d \n", rand());
   return EXIT_SUCCESS;
}
```@Rextester.C

Starten Sie das Programm mehrfach und beobachten Sie die Entwicklung der
Werte. Welchen Nachteil hat dieser Ansatz?

Die Funktion überwindet diese Einschränkung und generiert Zufallswerte
ausgehend von einem Startwert

```cpp
void srand(unsigned int startwert);
```

Integrieren Sie diese Funtion in das obrige Beispiel und evaluieren Sie das
Verhalten! Welcher Startwert bietet sich an, um eine kontinuierlich veränderliche
Folge von Zufallswerten zu generieren?

```cpp
srand(time(NULL));
```

**Sortieren und Suchen**

Die Standardbibliothek umfasst eine Suchfunktion, die es erlaubt Arrays nach
beliebigen Kriterien zu sortieren. Der Name `qsort()` deutet dabei an, dass der
Quicksort-Algorithmus zum EInsatz kommt. Die Vergleichsoperation, die vom
Anwender zu implementieren ist, akzeptiert als Übergabewerte Zeiger auf zwei
Einträge im Array und setzt diese in Beziehung. Bei einem negativen Rückgabewert ist das
erste Element kleiner, für einen positiven Wert größer als das zweite Übergabewert. Für den Wert 0 liegt
Gleichheit vor.

```c
void qsort(
   void *array,        // Anfangsadresse des Vektors
   size_t n,           // Anzahl der Elemente zum Sortieren
   size_t size,        // Größe des Datentyps, der sortiert wird
   int (*vergleich_func)(const void*, const void*)   );
```

```c  sort.c
#include <stdio.h>
#include <stdlib.h>

int values[] = { 88, 56, 100, 2, 25 };

int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int main (void) {
   int n;
   printf("Before sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%d ", values[n]);
   }

   qsort(values, 5, sizeof(int), cmpfunc);

   printf("\nAfter sorting the list is: \n");
   for( n = 0 ; n < 5; n++ ) {
      printf("%d ", values[n]);
   }

   return(EXIT_SUCCESS);
}
```@Rextester.C

Eine analoge Funktion steht für die Suche in sortierten Listen bereit. `bsearch()`
durchsucht diese und gibt einen Pointer zurück, der mit dem Suchkriterium
übereinstimmt.

**Ausführung von Kommandozeilenaufrufen**

In der `stdlib` bietet C die Möglichkeit Kommandozeilenbefehle auszuführen.
Damit lässt sich zum Beispiel sehr komfortabel auf das Dateisystem zurückgreifen
aber auch andere Programme starten und deren Ergebnisse erfassen.

```c runDir.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
  char command[50];
  strcpy(command, "dir" );
  system(command);
  return EXIT_SUCCESS;
}
```@Rextester.C


```cpp   generateCodeAndCompile.c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char programmCode[] = "#include <stdio.h> \n int main(){printf(\"C-Code Datei generiert und kompiliert!\"); return 0;}";

int main(void) {
  printf("Schreibe den Code in Datei ...\n");
  FILE * fp;
  fp = fopen ("myCode.c","w");
  fprintf (fp, programmCode);
  fclose (fp);

  char command[50];
  printf("Kompiliere ...\n");
  strcpy(command, "gcc myCode.c -o myCode.out" );
  system(command);
  printf("Führe aus ...\n");
  strcpy(command, "./myCode.out" );
  system(command);
  return EXIT_SUCCESS;
}
```
``` bash @output
▶ ./a.out
Schreibe den Code in Datei ...
Kompiliere ...
Führe aus ...
C-Code Datei generiert und kompiliert!%
```
### string.h

In der Definitionsdatei `string.h` werden Gruppen von Funktionen für Zeichenketten vereinbart. Für unsere Veranstaltung sind dabei folgende von Bedeutung:

| Befehl               | Bedeutung                                              |
|:--------------------|:-------------------------------------------------------|
| `char *strcpy(s,ct)`	|Zeichenkette ct in Vektor s kopieren, inklusive '\0'; liefert s.|
|`char *strncpy(s,ct,n)`	|höchstens n Zeichen aus ct in s kopieren; liefert s. Mit '\0' auffüllen, wenn ct weniger als n Zeichen hat.|
|`char *strcat(s,ct)`	| Zeichenkette ct hinten an die Zeichenkette s anfügen; liefert s.|
|`char *strncat(s,ct,n)` |	höchstens n Zeichen von ct hinten an die Zeichenkette s anfügen und s mit '\0' abschließen; liefert s.|
|`int strcmp(cs,ct)` |Zeichenketten cs und ct vergleichen; liefert <0 wenn cs<ct, 0 wenn cs==ct,oder >0, wenn cs>ct.|
|`char *strchr(cs,c)`	 |liefert Zeiger auf das erste c in cs oder NULL, falls nicht vorhanden.|
|`char *strrchr(cs,c)` |	liefert Zeiger auf das letzte c in cs, oder NULL, falls nicht vorhanden, |
|`char *strpbrk(cs,ct)`	| liefert Zeiger auf die Position in cs, an der irgendein Zeichen aus ct erstmals vorkommt, oder NULL, falls keines vorkommt. |
|`size_t strlen(cs)` |	liefert Länge von cs (ohne '\0'). |
|`char *strerror(n)` |	liefert Zeiger auf Zeichenkette, die in der Implementierung für Fehler n definiert ist. |

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void){
  char text[80];
  strcpy(text, "Es werden nur zehn Zeichen ");
  printf("%s\n", text);
  strncat(text, "angehaengt, der Rest nicht.", 10);
  printf("%s\n", text);
  printf("%d\n", strcmp(text, "Es werden "));    // compare
  printf("%s\n", strpbrk(text, "aou"));          // first match

 printf("------------------------------------\n");

  char trennzeichen[] = " ";
  char *wort;
  wort = strtok(text, trennzeichen);         // split to tokens
  while(wort != NULL) {
      printf("%s\n", wort);
      wort = strtok(NULL, trennzeichen);
  }
  return EXIT_SUCCESS;
}
```@Rextester.C


## 2. Beispiel der Woche

Berechnen Sie die die Distanz zwischen dem aktuellen Datum und einem beliebigen
Zeitwert, der mittels Tag, Monat, Jahr definiert wird.

```cpp
/* time2.c
http://openbook.rheinwerk-verlag.de/c_von_a_bis_z/019_c_zeitroutinen_001.htm
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(void) {
   int tag, monat, jahr;
   int aux = 0;

   printf("Bitte gib Deinen Geburtstag ein!\n");
   printf("Tag : ");
   aux = scanf("%d", &tag);
   printf("Monat : ");
   aux = aux + scanf("%d", &monat);
   printf("Jahr (jjjj) : ");
   aux = aux + scanf("%d", &jahr);
   printf("%d.%d.%d\n", tag, monat, jahr);

   if (aux==0){
     struct tm birthday_tm;
     birthday_tm.tm_mon  = monat -1;
     birthday_tm.tm_yday  = tag;
     birthday_tm.tm_year = jahr - 1900;
     birthday_tm.tm_hour = 0;
     birthday_tm.tm_min = 0;
     birthday_tm.tm_sec = 1;
     birthday_tm.tm_isdst = -1;

     long birthday = mktime(&birthday_tm);
     time_t tnow = time(&tnow);

     double diff_t = tnow -birthday;
     printf("%f Sekunden \n ... hier machen Sie weiter :-)", diff_t);
   }
   return EXIT_SUCCESS;
}
```
``` bash stdin
9
11
1965
```
@Rextester.C
