<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP.__eval
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s }}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);

    try {
        var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
        var info = log[1] + " " + log[4];

        if (info.length > 80)
          info = info.substring(0,76) + "..."

        error.add_detail(0, info, "error", log[2]-1, log[3]);
    } catch(e) {}

    throw error;
    }
</script>
@end


@JSCPP.eval: @JSCPP.__eval(@input, )

@JSCPP.eval_input: @JSCPP.__eval(@input,`@input(1)`)

@output: <pre class="lia-code-stdout">@0</pre>

@output_: <pre class="lia-code-stdout" hidden="true">@0</pre>


script:   https://ajax.googleapis.com/ajax/libs/jquery/1.11.3/jquery.min.js

@Rextester.__eval
<script>
//var result = null;
var error  = false;

console.log = function(e){ send.lia("log", JSON.stringify(e), [], true); };

function grep_(type, output) {
  try {
    let re_s = ":(\\d+):(\\d+): "+type+": (.+)";

    let re_g = new RegExp(re_s, "g");
    let re_i = new RegExp(re_s, "i");

    let rslt = output.match(re_g);

    let i = 0;
    for(i = 0; i < rslt.length; i++) {
        let e = rslt[i].match(re_i);

        rslt[i] = { row : e[1]-1, column : e[2], text : e[3], type : type};
    }
    return [rslt];
  } catch(e) {
    return [];
  }
}

$.ajax ({
    url: "https://rextester.com/rundotnet/api",
    type: "POST",
    timeout: 10000,
    data: { LanguageChoice: @0,
            Program: `@input`,
            Input: `@1`,
            CompilerArgs : @2}
    }).done(function(data) {
        if (data.Errors == null) {
            let warnings = grep_("warning", data.Warnings);

            let stats = "\n-------Stat-------\n"+data.Stats.replace(/, /g, "\n");

            if(data.Warnings)
              stats = "\n-------Warn-------\n"+data.Warnings + stats;

            send.lia("log", data.Result+stats, warnings, true);
            send.lia("eval", "LIA: stop");

        } else {
            let errors = grep_("error", data.Errors);

            let stats = "\n-------Stat-------\n"+data.Stats.replace(/, /g, "\n");

            if(data.Warning)
              stats = data.Errors + data.Warnings + stats;
            else
              stats = data.Errors + data.Warnings + stats;

            send.lia("log", stats, errors, false);
            send.lia("eval", "LIA: stop");
        }
    }).fail(function(data, err) {
        send.lia("log", err, [], false);
        send.lia("eval", "LIA: stop");
    });

"LIA: wait"
</script>
@end


@Rextester.eval: @Rextester.__eval(6, ,"-Wall -std=gnu99 -O2 -o a.out source_file.c")

@Rextester.eval_params: @Rextester.__eval(6, ,"@0")

@Rextester.eval_input: @Rextester.__eval(6,`@input(1)`,"-Wall -std=gnu99 -O2 -o a.out source_file.c")

-->

# Vorlesung IX - Dynamische Speicherverwaltung

**Fragen an die heutige Veranstaltung ...**

*


---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/09_DynamischeSpeicherverwaltung.md

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


## 0. Wiederholung

Fehler in C Programmen lassen sich in 5 Gruppen aufteilen:

 1. **Lexikalische-Fehler** - bezeichnen falsch geschriebene Worte im Programmcode.

 Indikatoren: Compiler-Fehler "was not declared in this scope" oder Linker-Fehler  "undefined reference to"

```cpp                    LexicalischeFehler.c
#include <stdio.h>
#include <stdlib.h>

int Main(void) {
  int x = 10, y=10;
  printf("%d", myfunction(x,y));
  return EXIT_SUCCESS;
}

int myFunction(int x, int y){
  return x+y;
}
```
@Rextester.eval

 2. **Syntax-Fehler** - (englisch syntax error) im Allgemeinen sind Verstöße gegen die  Satzbauregeln einer Sprache. Programme mit Syntaxfehlern werden von einem  Compiler oder Interpreter zurückgewiesen.

Häufigste Typen: fehlende Semikolon, Klammern, Definitionen

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int x = 10
  y = 15;
  printf("%d", x+y);
  return EXIT_SUCCESS;
```
@Rextester.eval

 3. **Semantische-Fehler** - (englisch semantic errors) umfassen falsche Deklarationen, die aber keinen syntaktischen Fehler begründen.

Vorkommen: Verwechslung von Operatoren, inkorrekte Annahmen zur Bedeutung von Variablen

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int i = 5;
  if (i = 6){
  	printf("Wert gleich 6!");
  }else{
  	printf("Wert ungleich 6");
  }
  return EXIT_SUCCESS;
}
```
@Rextester.eval

 4. **Laufzeit-Fehler** - (englisch runtime error) sind Fehler, die während der Laufzeit eines Computerprogramms auftreten. Laufzeitfehler führen zum Absturz des ausgeführten Programms, zu falschen Ergebnissen oder zu nicht vorhersehbarem Verhalten des Programms, z. B. wenn durch falsche/inkonsistente Daten Variablen überschrieben oder mit ungültigen Werten gefüllt werden.

Beispiele: Division durch null, Adressierung von Speicherbereichen außerhalb
eines Arrays, Endlosschleifen

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  for (int i = 5; i>=0; i--){
      printf("Ergebnis %d\n", 100/i );
  }
  return EXIT_SUCCESS;
}
```
``` bash @output
▶ ./a.out
Ergebnis 20
Ergebnis 25
Ergebnis 33
Ergebnis 50
Ergebnis 100
[1]    19533 floating point exception (core dumped)  ./a.out
```

 5. **Logische-Fehler** - Das Programm arbeitet in jedem Fall ohne Abbruch, realisiert aber nicht die gewünschte Funktionalität.

```cpp                     LogischerFehler.c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int values [] = {0,1,2,3,4,5,6,7,8,9,10};
  float sum = 0.;
  int i;
  for (i = 0; i < 10; i++){
      sum += values[i];
  }
  printf("%f", sum/i );
  return EXIT_SUCCESS;
}
```
@Rextester.eval

### Arrays als statisches Speicherelement
<!--
comment: Beispielcode um Schleife ergänzen, zum Beispiel Multiplikation aller Elemente
-->

```cpp                          nDimArray.c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int myArray[] = {0, 10, 20, 30};
  printf("%d %d = Inhalt des ersten und zweiten Eintrages", myArray[0], myArray[1]);
  printf("Pointer auf den ersten Eintrag %p", myArray);
  return EXIT_SUCCESS;
}
```
@Rextester.eval

<!--
style="width: 70%; max-width: 460px; display: block; margin-left: auto; margin-right: auto;"
-->
````
 Speicherauszug

 index    int-Breite

          ┣━━━━━━━━━┫
   0      ┃       0 ┃  <- myArray
          ┣━━━━━━━━━┫
   1      ┃      10 ┃
          ┣━━━━━━━━━┫
   2      ┃      20 ┃
          ┣━━━━━━━━━┫
   3      ┃      30 ┃
          ┣━━━━━━━━━┫
````

Entwickeln Sie einen Algorithmus für einen Parkautomaten, der Münzen wechselt

```cpp
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
  unsigned int gebuehr, zahlung, rueckgabe;
  printf("Bitte die Parkgebühr in Cent angeben:\n");
  scanf("%d",&gebuehr);
  printf("Bitte den eingezahlten Betrag in Cent angeben:\n");
  scanf("%d",&zahlung);
  rueckgabe = zahlung - gebuehr;
  printf("Resultierende Ausgabe %d Cent\n\n", rueckgabe);

  int muenzen [] = {1, 2, 5, 10, 20, 50, 100};
  int anteil = 0;

  for (int i = 0; i < 7; i++){
    anteil = rueckgabe / muenzen[i];
    if (anteil){
      rueckgabe = rueckgabe - anteil;
    }
    printf("%3i Cent %3d mal\n", muenzen[i], anteil);
  }
  return EXIT_SUCCESS;
}
```
``` bash stdin
382
500
```
@Rextester.eval_input

Was ist an dieser Lösung unbefriedigend und welche Änderungen sollten vollzogen
werden?

| Problem                             | Lösungsansatz                             |
|:------------------------------------|:------------------------------------------|
| Offenbar werden alle Beträge in 1 Cent Münzen ausgezahlt. | Denkfehler im Algorithmus? |
| Die Anzahl der Münznominale ist explizit im Programmcode enthalten. | Spezifikation der Array-Größe als Variable |
| Die Ausgabe erfolgt lediglich in der Konsole, eine Speicherung ist nicht vorgesehen. | Variable für die Rückgabe anlegen |
| Das Programm ist monolitisch aufgebaut. | Kapselung der Methode in einer Funktion |

Lösungsvorlage

```cpp
#include <stdio.h>
#include <stdlib.h>

// Funktion "Restgeld" einfügen
//
// Eingabeparameter: gebuehr, zahlung, muenzen (aufsteigende Reihung!)
// Ausgabeparameter: anzahl


int main(void)
{
  unsigned int gebuehr, eingabe;
  printf("Bitte die Parkgebühr in Cent angeben:\n");
  scanf("%d",&gebuehr);
  printf("Bitte den eingezahlten Betrag in Cent angeben:\n");
  scanf("%d",&eingabe);

  unsigned int muenzen [] = {1, 2, 5, 10, 20, 50, 100, 200};
  unsigned int anzahl []  = {0, 0, 0, 0, 0, 0, 0};
  unsigned char n = sizeof(muenzen) / sizeof(int);

  Restgeld(gebuehr, eingabe, muenzen, anzahl, n);

  for (int i = 0; i < n; i++){
    if (anzahl[i]){
      printf("%3d Cent - %3d x\n", muenzen[i], anzahl[i]);
    }
  }
  return EXIT_SUCCESS;
}
```
``` bash stdin
382
500
```
@Rextester.eval_input

<!--
```cpp
#include <stdio.h>
void Restgeld(unsigned int gebuehr, unsigned int zahlung,
              unsigned int * muenzen,
              unsigned int * anzahl,
              unsigned char elemente ){

  unsigned int rueckgabe = zahlung - gebuehr;
  unsigned int anteil = 0;
  printf("Resultierende Ausgabe %d Cent\n\n", rueckgabe);
  for (int i = elemente - 1; i >= 0; i--){
    anteil = rueckgabe / muenzen[i];
    if (anteil){
       rueckgabe = rueckgabe - anteil * muenzen[i];
       anzahl[i] = anteil;
    }
  }
}
```
-->

Allerdings ist die Lösung im Hinblick auf die Veränderung der Münzeinteilung
immer noch unbefriedigend. Eine Anpassung der Münznominale muss immer auch eine
Adaption des Rückgabewertes einschließen. Hier wäre eine dynamische Lösung
wünschenswert.

### Dynamische Arrays

Im Gegensatz zum statischen Arrays, deren Größen zum Zeitpunkt der Übersetzung
festgelegt werden, führt der C99-Standard das Konzept variabler Array-Größen ein.
Bei der Definition eines Feldes kann dessen Größe durch einen beliebigen
ganzzahligen Ausdruck bestimmt werden.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* reverse_string(char* in_out){
  unsigned int len = strlen(in_out);
  char tmp[len + 1]; // VLA für String und Nullterminierung
  strcpy(tmp, in_out);
  for (int i = 0; i < len; i++)
    in_out[i] = tmp[len - i - 1];
  return in_out;
}

int main(void){
  char tmp[] = "Das ist ein Test fuer VLA";
  printf("%s\n", reverse_string(tmp));
  	return 0;
}
```
@Rextester.eval

Eigenschaften:

+ VLAs können nicht initialisiert werden
+ die Größe kann nur einmalig bei der Definition festgelegt werden
+ VLAs können nur innerhalb von Funktionen angelegt werden (außerhalb von Funktionen müssen Feldgrößen auch in C99 zum Zeitpunkt der Übersetzung bekannt sein)
+ entsprechend werden VLAs auf dem Stack abgelegt -> Aufrufe von malloc() und free() entfallen

ACHTUNG: Das Verhalten für Arrays, die größer als der noch verfügbare Stack
sind ist unbestimmt!

> Linus Torvalds: "USING VLA'S IS ACTIVELY STUPID! It generates much more code, and much _slower_ code (and more fragile code), than just using a fixed key size would have done." [^1]

> With the in-development Linux 4.20 kernel, Linux kernel is effectively VLA-free. [^2]

... Im Gegensatz zu C99 ist die Implementierung von VLAs bei C11-konformen Compilern freigestellt. Die Verfügbarkeit kann über das Define `__STDC_NO_VLA__` abgefragt werden, das den Integerwert 1 aufweist, sofern VLAs nicht unterstützt werden.


[^1] https://lkml.org/lkml/2018/3/7/621

[^2] https://www.phoronix.com/scan.php?page=news_item&px=Linux-Kills-The-VLA


## 2. Dynamische Speicherallokation

Die Mechanismen der Memory Allocation erlauben eine variable Anforderung UND Freigabe von
Speicherplatz zur Laufzeit. Im Unterschied zu den lokalen Variablen von Funktionen (Stack) oder  globalen Variablen (Datensegment) werden diese im Heap-Speicher abgelegt.

![alt-text](img/memoryLayoutC.jpg)<!-- width="90%" --> [^1]

[^1]: https://www.geeksforgeeks.org/memory-layout-of-c-program/
     Autor Narendra Kangralkar






Mit dem Parameter size wird die Größe des Speicherbedarfs in Byte übergeben. Der Rückgabewert ist ein void-Zeiger auf den Anfang des Speicherbereichs oder ein NULL-Zeiger, wenn kein freier Speicher mehr zur Verfügung steht. Der void-Zeiger soll aussagen, dass der Datentyp des belegten Speicherbereichs unbekannt ist.



Bei erfolgreichem Aufruf liefert die Funktion `malloc()` die Anfangsadresse mit der Größe size Bytes vom Heap zurück. Da die Funktion einen void-Zeiger zurückliefert, hängt diese nicht von einem Datentyp ab.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
  char *msg = malloc (4);
  strcpy (msg, "Hello World!");
  printf ("%s\n", msg);
  return EXIT_SUCCESS;
}
```
@Rextester.eval

## 3. Beispiel der Woche
