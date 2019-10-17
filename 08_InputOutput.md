<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  0.0.1
language: de
narrator: Deutsch Female

import: https://raw.githubusercontent.com/liaScript/rextester_template/master/README.md
-->


# Vorlesung VIII - Input- und Output-Operationen

**Fragen an die heutige Veranstaltung ...**

* Welche Bedeutung haben die Standard-Datenströme `stdin` und `stdout`?
* Was versteht man unter dem wahlfreien Zugriff auf Dateiinhalte?
* Was sind binäre Dateien, nennen Sie Beispiele?
* Welche Bedeutung haben die unterschieldlichen Modi, mit denen eine Datei geöffnet werden kann?
* Was bedeutet EOF?
* Welchen Datentyp hat FILE? Welche Informationen sind darin codiert?

---------------------------------------------------------------------
Hier geht es zur interaktiven Version des Kurses [LiaScript](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/CCourse/master/08_InputOutput.md#1)

---------------------------------------------------------------------

**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

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
| `<string.h>` |             | Stringfunktionen                        |
| `<math.h>`   |             | Mathematische Funktionen und Konstanten |

{{1}}
[C standard library header files](https://en.cppreference.com/w/c/header)

## 0. Wiederholung Ein- und Ausgabe auf der Konsole
<!--
comment: hier in der online session die scanf Zeilen zu einer zusammenfassen
-->

**Ein- und Ausgabe auf der Konsole**

```cpp
#include <stdio.h>

int main(void)
{
  int a,b,c;

  printf("Bitte Länge des Quaders eingeben:\n");
  scanf("%d",&a);
  printf("Bitte Breite des Quaders eingeben:\n");
  scanf("%d",&b);
  printf("Bitte Höhe des Quaders eingeben:\n");
  scanf("%d",&c);
  printf("Quaderoberfläche:\n%d\n", 2 * (a * b + a * c + b * c));
  return 0;
}
```
``` text                  stdin
2 3 4
```
@Rextester.C(false,`@input(1)`)


Darauf aufbauend lassen sich mit scanf komplexe "Muster" ausdrücken, die
Eingaben auf eine Übereinstimmung hin prüfen.

```cpp
#include <stdio.h>

int main(void)
{
  int tag, monat, jahr;
  char vorname[20]= "";
  int eval;
  printf("Bitte geben Sie ihr Geburtsdatum ein [TT.MM.JJJJ]: \n");
  eval = scanf("%d.%d.%d+%s", &tag, &monat, &jahr, vorname);
  printf("Erfolgreich eingelesene Eingaben: %d\n", eval);
  if (eval == 4){
    printf("\n%s, geboren am %04d-%02d-%02d\n", vorname, jahr, monat, tag);
  }else{
    printf("Hier stimmt was nicht!");
  }
  return 0;
}
```
``` bash stdin
20.05.2018+Alexander
```
@Rextester.eval_input

Folgende Zeichen werden bei `scanf` als Eingabefelder akzeptiert:

+ alle Zeichen bis zum nächsten Whitespace oder dem angegebenen Trennungselement
+ bis zu einer bestimmten Feldbreite von n-Zeichen
+ alle Zeichen, bis zum ersten Zeichen, welches nicht mehr in entsprechendes Format konvertiert werden konnte.

## 1. Ein- und Ausgabeoperationen

Ein- und Ausgabeoperationen im Sinne des C Standards beziehen sich auf die
Interaktion mit dem Nutzer über Dateien und den Bildschirm.

> Der C-Standard definiert keine Festlegungen für grafische Oberflächen!
> Allerdings besteht eine Vielzahl von Bibliotheken, mit deren Hilfe grafische
> Anwendungen realisiert werden können.

Die Ein- und Ausgabe wird unter C über das Konzept des Streams realisiert.
Ziel sind einheitliche Eigenschaften und Zugriffsmechanismen für verschiedenen
Ein- und Ausgänge. Dabei werden zwei Varianten unterschieden:

+ *Stream im Textmodus* - Ein Textstrom besteht aus einer oder mehreren Zeilen, die durch ein Zeilenzeichen abgeschlossen werden. Diese können sichtbaren Zeichen und Steuercodes umfassen.

| Kürzel | ASCII Code | Bedeutung                                             |
|:-------|:-----------|:------------------------------------------------------|
| \n     |     0a     | (new line) = bewegt den Cursor auf die Anfangsposition der nächsten Zeile.|
| \t     |     09     | (horizontal tab) = Setzt den Tabulator auf die nächste horizontale Tabulatorposition. Wenn der Cursor bereits die letzte Tabulatorposition erreicht hat, dann ist das Verhalten unspezifiziert (vorausgesetzt eine letzte Tabulatorposition existiert).|
| \a     |     07     | (alert) = gibt einen hör- oder sichtbaren Alarm aus, ohne die Position des Cursors zu ändern |
| \b     |     08     | (backspace) = Setzt den Cursor ein Zeichen zurück. Wenn sich der Cursor bereits am Zeilenanfang befindet, dann ist das Verhalten unspezifiziert.|
| \r     |     0D     | (carriage return, dt. Wagenrücklauf) = Setzt den Cursor an den Zeilenanfang|
| \f     |     0C     | (form feed) = Setzt den Cursor auf die Startposition der nächsten Seite. |
| \v     |     0B     | (vertical tab) = Setzt den Cursor auf die nächste vertikale Tabulatorposition. Wenn der Cursor bereits die letzte Tabulatorposition erreicht hat, dann ist das Verhalten unspezifiziert (wenn eine solche existiert). |
| \\0     |           | ist die Endmarkierung einer Zeichenkette  |


```

A1
B2
C3

```

``` bash @output
▶ hexdump -C Text.txt
00000000  0a 41 31 0a 42 32 0a 43  33 0a                    |.A1.B2.C3.|
0000000a
```

{{1}}
![alt-text](img/ASCII_Zeichensatz.jpeg)<!-- width="90%" -->

* *Stream im Binärmodus* - Ein binärer Strom ist eine geordnete Folge von Nullen und Einsen ohne spezifische Festlegungen zu Zeilenumbrüchen etc. Zahlenwerte werden entsprechend ihrer Speicherrepräsentation abgelegt, es findet keine automatische Konvertierung statt. Der Vorteil des Binärmodus liegt in der kompakten Darstellung.

### Standard-Datenströme

Die bisherigen Ein- und Ausgaben mittels `printf` und `scanf` erfolgten über
den Standard-Datenströmen.

* stdin - Die Standardeingabe (standard input) ist üblicherweise mit der Tastatur verbunden. Der Stream wird zeilenweise gepuffert.
* stdout - Die Standardausgabe (standard output) ist mit dem Bildschirm verknüpft und ebenfalls zeilenweise gepuffert.
* stderr - Die Standardfehlerausgabe (standard error output) ist analog zu stdout mit dem Bildschirm verbunden.

![alt-text](/img/Stdstreams.png)<!-- width="90%" --> [^1]

[^1]: https://de.wikipedia.org/wiki/Standard-Datenstr%C3%B6me#/media/File:Stdstreams-notitle.svg
     Autor Danielpr85

```cpp
#include <stdio.h>
#include <stdlib.h>

int main () {
  fprintf(stdout, "%s\n", "Textausgabe zum stdout");
  fprintf(stderr, "%s\n", "Textausgabe zum stdout");
  printf("Textausgabe zum stdout\n");
  return(0);
}
```

``` bash @output
▶ ./a.out
Textausgabe zum stdout
Textausgabe zum stderr
Textausgabe zum stdout
```

Einige Betriebssysteme (wie zum Beispiel DOS) stellten weitere Datenstromtypen
vor und betteten Drucker und serielle Schnittstellen in das Konzept ein.
Alle drei Standard-Datenströme können umgelenkt werden. Dies kann innerhalb des
Programmes durch entsprechende Standardfunktionen `freopen` erfolgen.

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void) {
   printf("Diese Zeichen landen auf dem Bildschirm\n");
   freopen("log.txt","a+",stdout); // <- Die Erläuterung zu diesen Parametern
                                   //    folgt gleich.
   printf("Dieser Text steht in der Datei \"log.txt\"\n");
   return EXIT_SUCCESS;
}
```

Alternativ kann aber auch beim Aufruf eines Programms in der Kommandozeile eine
Umleitung erfolgen.

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void) {
   printf("Diese Zeichen landen im stdout\n");
   return EXIT_SUCCESS;
}
```

``` bash @output
▶ gcc experiments.c
▶ ./a.out > text.txt
▶ cat text.txt
Diese Zeichen landen im stdout
```

### Stream-Generierung

Nun wollen wir neue Datenströme spezifizieren und konzentrieren uns dabei auf
Dateien.

```c
#include <stdio.h>
FILE *fopen(const char *pfadname, const char *mode);
FILE *freopen(const char *pfadname, const char *mode, FILE *stream);
```

Was steckt hinter dem `FILE` struct, das in `stdio.h` deklariert ist?

* Puffer mit Anfangsadresse, aktuellem Zeiger und Größe,
* Status des Stroms
* Filename
+ ...

Als Pfadangaben (Pfadnamen) sind alle zulässigen Bezeichner erlaubt. Die maximale Länge für den Pfadnamen ist in der Konstante `FILENAME_MAX` deklariert.

> Unter Windows wird der Dateipfad mit den schrägen Strichen nach hinten
> (Backslash) geschrieben, z.B. “C:\\BAF\\daten.txt“. Unter Linux-Systemen wird
> statt dem Backslash der normale Slash verwendet, z.B. “/home/BAF/daten.txt“.

Mit Modus geben Sie an, wie auf den Stream zugegriffen wird. Die Funktionen
liefern als Ergebnis einen FILE-Zeiger, bei einem Fehler erhalten Sie hingegen
den NULL-Zeiger zurück.

| Modus     | Beschreibung                                                  |
|:----------|:--------------------------------------------------------------|
|"r"        | Textdatei zum Lesen und Eröffnen                              |
|"w"	      | Textdatei zum Schreiben erzeugen; gegebenenfalls alten Inhalt wegwerfen|
|"a"	      | anfügen; Textdatei zum Schreiben am Dateiende eröffnen oder erzeugen|
|"r+"	      | Textdatei zum Ändern eröffnen (Lesen und Schreiben)|
|"w+"	      | Textdatei zum Ändern erzeugen; gegebenenfalls alten Inhalt wegwerfen|

Die Angaben können kombiniert werden `"rw"` öffnet eine Datei zum Lesen und
Schreiben. Wichtig für die Arbeit ist der append-Modus, der als Schreibmodus die
ursprünglichen Daten der Datei unverändert belässt und neue Daten am Ende der
Datei einfügt.

ACHTUNG:

* Existiert eine Datei und wird diese im Schreibmodus `"w"` geöffnet, so wird der komplette Inhalt ohne Meldung gelöscht.

* Existiert eine Datei nicht und wird versucht diese im Schreibmodus zu öffnen, so wird automatisch eine neue leere Datei erzeugt.

Wie werden Datenströme warum geschlossen?

* Wenn sich ein Programm beendet, schließen sich automatisch alle noch offenen Streams.

* Die Anzahl der geöffneten Dateien ist begrenzt und wird in der Standard-Library `stdio.h` mit der Konstante `FOPEN_MAX` festgelegt. Mit `fclose` kann wieder ein FILE-Zeiger freigegeben werden.

* Wenn eine Datei im Schreibmodus geöffnet wurde, wird diese erst beschrieben, wenn der Puffer voll ist oder die Schreiboperation explizit angefordert wird. Beendet sich das Programm aber mit einem Fehler, dann sind die Daten im Puffer verloren.

``` c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  FILE *fp;    // Dateizeiger erstellen
  fp = fopen("ProzProg.txt", "r"); // <- der Modus definiert das
                                   //    Verhalten des Programms w -> r
  if(fp == NULL) {
  	printf("Upps, die Datei exisitiert nicht!\n");
  }else {
  	printf("Alles gut, Datei gefunden.\n");
  	fclose(fp);
  }
  return EXIT_SUCCESS;
}
```

### Stream-Operationen

Ausgehend von den vordefinierten Standardstreams definiert die Standardbibliothek
`stdio.h` folgende Funktionen für

| Standard-Stream | mit Streamnamen | Bedeutung                                       |
|:----------------|:----------------|:------------------------------------------------|
| printf          | fprintf         | Formatierte Ausgabe                             |
| vprintf          | vfprintf        | Formatierte Ausgabe mit variabler Argumentliste |
| scanf           | fscanf          | Formatierte Eingabe                             |
| putchar         | putc, fputc     | Zeichenausgabe                                  |
| getchar         | getc, fgetc     | Zeicheneingabe                                  |
| gets (gets_s)            | fgets           | String-Eingabe                                  |
| puts            | fputs           | String-Ausgabe                                  |
| perror          |                 | String-Ausgabe an stderr                        |


Um beim Lesen des Ende einer Datei aufzuzeigen, bietet die `stdio.h` einen
speziellen end-of-file Indikator.  Dieser gibt eine Wert ungleich 0 zurück,
wenn das Zeilenende erreicht ist.

**Anwendung I - Iterativies Durchlaufen des Streams**

``` c
#include <stdio.h>

int main () {
   FILE *fp;
   int c;

   fp = fopen("text.txt","r");
   if(fp == NULL) {
      perror("Error in opening file");
      return(-1);
   }
   while(1) {
      c = fgetc(fp);
      if( feof(fp) ) {
         printf("<-\n");
         break ;
      }
      printf("%c", c);
   }
   fclose(fp);
   return(0);
}
```

**Fehlerquelle Buffergröße**

Im Zusammenhang mit dem Lesen von Eingaben wird die Notwendigkeit eines
effektiven Monitorings deutlich. Das folgende Beispiel mappt die Eingaben des
Nutzers auf ein `char` Array mit 8 Einträgen. Die folgenden Aussagen beziehen
sich auf die rextester Architektur, auf Ihrem eigenen Rechner können die Ergebnisse,
da die Ablage und Organisation der Daten nicht im Standard spezifiziert sind,
auch anders aussehen.

Für beide Variablen wurde Speicher auf dem Stack allokiert. Wenn die Länge
der Eingaben die Kapazität des Arrays überschreitet, geschehen zwei Dinge:

* Zum einen werden Inhalte von `nextString` oder von dem überlangen Eingabestring überschrieben.

* Wird die Eingabe so lang, dass die Größe mit dem Stackframe kollidiert, wird das Programm beendet.

| Input           | Größe | Resultat |
|-----------------|------|---------------------------------------|
| Das.ist         |  7+1 | Gültige Eingabe entsprechend der Größe von `string`.|
| Das.ist.ein.Tes | 15+1 | Die Terminierung steht an der 16. Stelle und damit nicht im Array.|
| Das.ist.ein.Test | 16+1 | Die Terminierung der Eingabe wird auf den ersten Eintrag von `nextString` geschoben. Damit scheint dieses Array leer.|
| Das.ist.ein.Test! | 16+x+1 | Alle weiteren Zeichen erscheinen in `nextString`.|
| Das.ist.ein.Test!Der.Input.ist.zu.groß.. | 41+1 | Die Framegrenze wird überschritten. Das System crashed.|

<!--
style="width: 80%; max-width: 460px; display: block; margin-left: auto; margin-right: auto;"
-->
````
          ╭              ===========
          ╎  Variablen       ...
          ╎              ┣━━━━━━━━━┫
          ╎  count       ┃       0 ┃
          ╎              ┣━━━━━━━━━┫
          ╎                  ...
 Stack    ╎              ┣━━━━━━━━━┫
 frame  < ╎  string      ┃         ┃  "Wuchsrichtung"
          ╎              ┣━━━━━━━━━┫       des
          ╎                  ...      Stackspeichers
          ╎              ┣━━━━━━━━━┫        ▲
          ╎  nextstring  ┃ 0 1 2 3 ┃        ┃
          ╎              ┃ 4 5 6 7 ┃        ┃
          ╎              ┣━━━━━━━━━┫
          ╎                  ...        niedrigere
          ╰              ===========     Adressen
````

```cpp
#include <stdio.h>
#include <stdlib.h>
#define SIZEOFSTRING 4

int main(void) {

  int count = 0;
  char string[SIZEOFSTRING] = {0};
  char nextString[] = "x-x-x-x-";

  printf("\"string\"     liegt bei %p und reicht bis %p\n", string, string + SIZEOFSTRING);
  printf("\"nextString\" liegt bei %p und reicht bis %p\n", nextString, &nextString[7]);
  printf("Gesamtspeicherbereich %d\n", (int)(&nextString[7]-string));

  count = scanf("%s", string);
  printf("Zeichen: %d\n", count);
  printf("Inhalt von \"string\"    : %s\n", string);
  printf("Inhalt von \"nextstring\": %s\n", nextString);
  return EXIT_SUCCESS;
}
```
``` bash stdin
Das.ist.ein.Test!
```
@Rextester.eval_input

> People (and especially beginners) should never use scanf("%s") or gets() or any other functions that do not have buffer overflow protection, unless you know for certain that the input will always be of a specific format (and perhaps not even then).

> Remember that scanf stands for "scan formatted" and there's precious little less formatted than user-entered data. It's ideal if you have total control of the input data format but generally unsuitable for user input.

```cpp
#include <stdio.h>
#include <stdlib.h>

#define MAX_NAME_SZ 10

int main(void) {
   char string[MAX_NAME_SZ];
   if( fgets(string, MAX_NAME_SZ, stdin)!=NULL ) {
      printf("Ihre Eingabe: \"%s\"\n",string);
   }
   return EXIT_SUCCESS;
}
```
``` bash stdin
Das ist ein Test.
```
@Rextester.eval_input

**Anwendung von `perror`**

```cpp
#include <stdio.h>
#include <errno.h>

extern int errno ;

int main (){
  int sys_nerr;
  for (size_t i = 0; i < 10; i++) {
    printf("%*zu = %s\n", 3, i, sys_errlist[i]);
  }

  FILE * pFile;
  pFile = fopen ("unexist.ent","rb");
  if (pFile == NULL) {
    perror ("The following error occurred");
    printf( "Value of errno: %d\n", errno );
  } else {
    fclose (pFile);
  }
  return 0;
}
```

``` bash @output
▶ ./a.out
  0 = Success
  1 = Operation not permitted
  2 = No such file or directory
  3 = No such process
  4 = Interrupted system call
  5 = Input/output error
  6 = No such device or address
  7 = Argument list too long
  8 = Exec format error
  9 = Bad file descriptor

The following error occurred: No such file or directory
Value of errno: 2
```

### Weiterführende Dateioperationen

**Dateioperationen**

```c
int rename(const char *oldname, const char *newname)
```
Die Funktion `rename` ändert den Namen einer Datei und liefert nicht Null, wenn
der Versuch fehlschlägt.

```c
int remove(const char *filename);
```
Die Funktion `remove` entfernt die angegebene Datei, so dass ein anschließender Versuch, sie
zu eröffnen, fehlschlagen wird. Die Funktion liefert bei Fehlern einen von Null verschiedenen Wert.

```c
FILE *tmpfile(void)
```
Die Funktion `tmpfile` erzeugt eine temporäre Datei mit Zugriff "wb+", die automatisch gelöscht wird, wenn der Zugriff abgeschlossen wird, oder wenn das Programm normal zu Ende geht. Funktion liefert einen Datenstrom oder NULL, wenn
die Datei nicht erzeugt werden konnte.

```c
char *tmpnam(char s[L_tmpnam])
```
Die Funktion `tmpnam` generiert einen zufälligen Dateinamen, der im Ordner noch nicht
vorkommt. Damit kann sichergestellt werden, dass Daten mit jeweils neuen
Dateinamen abgespeichert werden.

```c
#include <stdio.h>

int main () {
  char buffer[L_tmpnam];
  char *ptr;

  tmpnam(buffer);
  printf("Temporary name 1: %s\n", buffer);

  ptr = tmpnam(NULL);
  printf("Temporary name 2: %s\n", ptr);

  return(0);
}
```

``` bash @output
▶ ./a.out
Temporary name 1: /tmp/fileB8A3W0
Temporary name 2: /tmp/fileZObkAs
```

**Wahlfreier Zugriff**

```c
void rewind(FILE *stream)
```
Die Funktion  `rewind` setzt die Lese-/Schreibposition für einen Datenstrom
zurück auf den Anfang.

```c
int fseek(FILE *stream, long int offset, int whence)
```
Die Funktion `fseek` setzt die Lese-/Schreibposition für einen Datenstrom mit
einem Offset bezogen auf `SEEK_SET` (Dateianfang), `SEEK_CUR` (aktuelle Position) oder `SEEK_END` (letzte Position).

Diese Varianten können zum Beispiel zur Bestimmung der Größe einer Datei
kombiniert werden:

```c
long fsize(FILE *fp) {
    fseek(fp, 0, SEEK_END);  // Position auf letztes Datenelement im Stream
    long bytes = ftell(fp);  // gibt die akutelle Position im Stream zurück
    rewind(fp);              // zurücksetzen der aktuellen Position auf den
                             // Anfang
    return bytes;
}
```
Diese Lösung ist vollständig transparent und übertragbar. Alternative Lösungen
greifen auf Betriebssystem-spezifische Lösungen zurück.

### Anwendung

Das folgende Beispiel illustriert die Anwendung des Streamkonzepts. Eine Datei
wird geöffnet und bis zum Ende der Datei durchlaufen.

```c
#include <stdio.h>

#define FILENAME "Text.txt"

int main(void){
  FILE *fp;

  fp=fopen(FILENAME, "w");
  fprintf(fp, "Prozedurale Programmierung vermittelt die\n");
  fprintf(fp, "Grundlagen der C Programmierung");
  fclose(fp);

  int ch, linecount=0, wordcount=0, charcount=0;

  // Open file in read-only mode
  fp = fopen(FILENAME,"r");
  if ( fp ){
    //Repeat until End Of File character is reached.
    while ((ch=getc(fp)) != EOF) {
      // Increment character count if NOT new line or space
      if (ch != ' ' && ch != '\n') { ++charcount; }

      // Increment word count if new line or space character
      if (ch == ' ' || ch == '\n') { ++wordcount; }

      // Increment line count if new line character
      if (ch == '\n') { ++linecount; }
    }

    if (charcount > 0) {
      ++linecount;
      ++wordcount;
    }
  }else{
    printf("Failed to open the file\n");
  }
  fclose(fp);
  printf("Lines : %3d Words : %4d Characters : %4d \n", linecount, wordcount, charcount);
  return(0);
}
```

## 2. Beispiel der Woche

Für die Vereinigten Staaten liegen umfangreiche Datensätze zur Namensgebung von
Neugeborenen seit 1880 vor. Eine entsprechende csv-Datei (comma separated file)
befindet sich im Unterverzeichnis "data" des Projektordners, sie umfasst 258.000 Einträge. Diese
sind wie folgt gegliedert:

```
1880,"John",0.081541,"boy"
1880,"William",0.080511,"boy"
1880,"James",0.050057,"boy"
```

Die erste Spalte gibt das Geburtsjahr, die zweite den Vornamen, die Dritte den
Anteil der mit diesem Vornamen benannten Kinder und die vierte das Geschlecht an.

Der Datensatz steht zum Download unter
https://osf.io/d2vyg/
bereit. Bitte entfernen Sie nach dem Herunterladen per Texteditor die erste Zeile (Tabellenkopf).

Lesen Sie aus den Daten die jeweils am häufigsten vergebenen Vornamen aus und
bestimmen Sie deren Anteil innerhalb des Jahrganges.

```cpp
// Read baby names from US
// the file is available in the project folder /data

#include <stdio.h>
#include <stdlib.h>
#define FILENAME "./data/baby-names.csv"

int main(int argc, char *argv[])
{
  FILE *in = fopen(FILENAME,"r");
  if(in==NULL){
    perror("File open error");
    exit(EXIT_FAILURE);
  }

  unsigned int year, year_old = 0;
  int count = 0;
  char name[24];
  float prob;
  char sex[7];
  do{
    if (fscanf(in,"%d,%[^,],%f,%s", &year, name, &prob, sex) == 4) {
      count++;
      if (year != year_old) {
        if (year%10==0) {
          printf("%d,%10s,%1.4f,%s\n", year, name, prob, sex);
        }
        year_old = year;
      }
    }
  } while (!feof(in));
  printf("\n%d Datensätze gelesen\n", count);
  fclose(in);
  return 0;
}
```

```bash @output_
▶ ./a.out
1880,    "John",0.0815,"boy"
1890,    "John",0.0710,"boy"
1900,    "John",0.0606,"boy"
1910,    "John",0.0549,"boy"
1920,    "John",0.0517,"boy"
1930,  "Robert",0.0550,"boy"
1940,   "James",0.0527,"boy"
1950,   "James",0.0473,"boy"
1960,   "David",0.0397,"boy"
1970, "Michael",0.0448,"boy"
1980, "Michael",0.0370,"boy"
1990, "Michael",0.0304,"boy"
2000,   "Jacob",0.0165,"boy"
1880,    "Mary",0.0724,"girl"
1890,    "Mary",0.0599,"girl"
1900,    "Mary",0.0526,"girl"
1910,    "Mary",0.0544,"girl"
1920,    "Mary",0.0571,"girl"
1930,    "Mary",0.0550,"girl"
1940,    "Mary",0.0476,"girl"
1950,   "Linda",0.0457,"girl"
1960,    "Mary",0.0247,"girl"
1970,"Jennifer",0.0252,"girl"
1980,"Jennifer",0.0328,"girl"
1990, "Jessica",0.0226,"girl"
2000,   "Emily",0.0130,"girl"

258000 Datensätze gelesen
```
