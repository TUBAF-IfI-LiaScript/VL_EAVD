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


# Vorlesung VIII - Input Output Operationen

**Fragen an die heutige Veranstaltung ...**

*

---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/08_InputOutput.md

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
``` bash stdin
2
3
4
```
@Rextester.eval_input

Darauf aufbauend lassen sich mit scanf komplexe "Muster" ausdrücken, die
Eingaben auf eine Übereinstimmung hin prüfen.

```cpp
#include <stdio.h>

int main(void)
{
  int tag, monat, jahr;
  char vorname[20]= "";
  int eval;
  printf("Bitte geben Sie ihr Geburtsdatum ein [TT.MM.JJJJ]: ");
  eval = scanf("%d.%d.%d %s", &tag, &monat, &jahr, vorname);
  printf("Erfolgreich eingelesene Eingaben: %d", eval);
  if (eval == 4){
    printf("\n%s, geboren am %04d-%02d-%02d\n", vorname, jahr, monat, tag);
  }else{
    printf("Hier stimmt was nicht!");
  }
  return 0;
}
```
``` bash stdin
20.05.2018 Alexander
```
@Rextester.eval_input

Folgende Zeichen werden bei `scanf()` als Eingabefelder akzeptiert:

+ alle Zeichen bis zum nächsten Whitespace
+ bis zu einer bestimmten Feldbreite von n-Zeichen
+ alle Zeichen, bis zum ersten Zeichen, welches nicht mehr in entsprechendes Format konvertiert werden konnte.

## 1. Eingabe aus Dateien

Ein- und Ausgaben, ob zu oder von physischen Geräten wie Terminals und
Laufwerken oder von Dateien oder zu Dateien, werden in logische Datenströme
abgebildet. Ziel sind einheitliche Eigenschaften und Zugriffsmechanismen für
verschiedenen Ein- und Ausgänge.

Ein Textstrom besteht aus einer oder mehreren Zeilen. Eine Zeile in einem
Textstrom umfasst null oder mehr Zeichen plus einem abschließenden neuen
Zeilenzeichen. Unix übernahm ein standardmäßiges internes Format für alle Textströme. Jede Textzeile wird durch ein neues Zeilenzeichen abgeschlossen. Das erwartet jedes Programm, wenn es Text liest, und das erzeugt jedes Programm, wenn es Text schreibt. (Dies ist die grundlegendste Konvention, und wenn sie nicht den Anforderungen eines textorientierten Peripheriegeräts entspricht, das an eine Unix-Maschine angeschlossen ist, erfolgt die Korrektur an den Rändern des Systems. Nichts dazwischen muss geändert werden. ) Die Zeichenfolge, die in einen Textstrom eingeht oder aus einem Textstrom austritt, muss möglicherweise geändert werden, um bestimmten Konventionen zu entsprechen. Dies führt zu einem möglichen Unterschied zwischen den Daten, die in einen Textstrom eingegeben werden, und den Daten, die ausgegeben werden. In einigen Implementierungen wird beispielsweise ein Leerzeichen aus der Ausgabe entfernt, wenn ein Leerzeichen in der Eingabe vor einem Zeilenumbruch steht. Wenn die Daten nur aus druckbaren Zeichen und Steuerzeichen wie horizontaler Tabulator und Zeilenumbruch bestehen, sind Eingabe und Ausgabe eines Textstroms im Allgemeinen gleich.

Verglichen mit einem Textstrom ist ein binärer Strom ziemlich einfach. Ein binärer Strom ist eine geordnete Folge von Zeichen, die interne Daten transparent aufzeichnen kann. Daten, die in einen binären Datenstrom geschrieben werden, müssen immer den Daten entsprechen, die bei derselben Implementierung ausgelesen werden. Bei binären Datenströmen kann jedoch eine implementierungsdefinierte Anzahl von Nullzeichen an das Ende des Datenstroms angehängt werden. Es gibt keine weiteren Konventionen, die berücksichtigt werden müssen.

Nichts unter Unix hindert das Programm daran, beliebige 8-Bit-Binärcodes in eine geöffnete Datei zu schreiben oder unverändert aus einem geeigneten Repository zurückzulesen. Daher hat Unix die seit langem bestehende Unterscheidung zwischen Textströmen und Binärströmen verwischt.


### Stream-Handling

```c
#include <stdio.h>
FILE *fopen(const char *pfadname, const char *mode);
FILE *freopen(const char *pfadname, const char *mode, FILE *stream);
```

+ Als Pfadangabe (pfadname) sind alle zulässigen Strings erlaubt. Die maximale Stringlänge für pfadname ist in der Konstante FILENAME_MAX deklariert.

  > Unter Windows wird der Dateipfad mit den schrägen Strichen nach hinten
  > (Backslash) geschrieben, z.B. „C:\\BAF\\daten.txt“. Unter Linux-Systemen wird
  > statt dem Backslash der normale Slash verwendet, z.B. „/home/BAF/daten.txt“.

+ Mit modus geben Sie an, wie auf den Stream zugegriffen wird. Bei einem Fehler erhalten Sie hingegen den NULL-Zeiger zurück.

  | Modus     | Beschreibung                                                  |
  |:----------|:--------------------------------------------------------------|
  |"r"        | Textdatei zum lesen und eröffnen                              |
  |"w"	      | Textdatei zum Schreiben erzeugen; gegebenenfalls alten Inhalt wegwerfen|
  |"a"	      | anfügen; Textdatei zum Schreiben am Dateiende eröffnen oder erzeugen|
  |"r+"	      | Textdatei zum Ändern eröffnen (Lesen und Schreiben)|
  |"w+"	      | Textdatei zum Ändern erzeugen; gegebenenfalls alten Inhalt wegwerfen|


Die Angaben können kombiniert werden „rw“ öffnet eine Datei zum Lesen und
Schreiben. Wichtig für die Arbeit ist der append Modus, der als Schreibmodus die
ursprünglichen Daten der Datei unverändert belässt und neue Daten am Ende der
Datei einfügt.

ACHTUNG:
+ Existiert eine Datei und wird diese im Schreibmodus geöffnet, so wird der komplette Inhalt ohne Meldung gelöscht.
+ Existiert eine Datei nicht und wird versucht diese im Schreibmodus zu öffnen, so wird automatisch eine neue leere Datei erzeugt.

``` c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
  FILE *fp;    // Dateizeiger erstellen
  fp = fopen("ProzProg.txt", "w"); // <- der Modus definiert das
                                   //    Verhalten des Programms

  if(fp == NULL) {
  	printf("Upps, die Datei exisitiert nicht!\n");
  }else {
  	printf("Alles gut, Datei gefunden.\n");
  	fclose(fp);
  }
  return EXIT_SUCCESS;
}
```
@Rextester.eval_params(-Wall -std=gnu99 -O2 -o a.out source_file.c -lm)


### Standard-Datenströme
```c
#include <stdio.h>
extern FILE *stderr;
extern FILE *stdin;
extern FILE *stdout;
```



### Stream-Operationen




### Weiterführende Dateioperationen

remove entfernt die angegebene Datei, so daß ein anschließender Versuch, sie zu eröffnen, fehlschlagen wird. Die Funktion liefert bei Fehlern einen von Null verschiedenen Wert.

  int rename(const char *oldname, const char *newname)

rename ändert den Namen einer Datei und liefert nicht Null, wenn der Versuch fehlschlägt.

  FILE *tmpfile(void)

tmpfile erzeugt eine temporäre Datei mit Zugriff "wb+", die automatisch gelöscht wird, wenn der Zugriff abgeschlossen wird, oder wenn das Programm normal zu Ende geht. tmpfile liefert einen Datenstrom oder NULL, wenn die Datei nicht erzeugt werden konnte.

  char *tmpnam(char s[L_tmpnam])


## Beispiel der Woche


```cpp
  #include <stdio.h>

  #define FILENAME "Text.txt"

  int main()
  {
   FILE *fp;

   fp=fopen(FILENAME, "w");
   fprintf(fp, "Prozedurale Programmierung vermittelt die\n");
   fprintf(fp, "Grundlagen der C Programmierung");
   fclose(fp);

   char ch;
   int linecount, wordcount, charcount;

   // Initialize counter variables
   linecount = 0;
   wordcount = 0;
   charcount = 0;

   // Open file in read-only mode
     fp = fopen(FILENAME,"r");

     // If file opened successfully, then write the string to file
     if ( fp )
     {
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
      }
     else
        {
           printf("Failed to open the file\n");
          }

      printf("Lines : %d \n", linecount);
      printf("Words : %d \n", wordcount);
      printf("Characters : %d \n", charcount);
  return(0);
  }
```
@Rextester.eval_params(-Wall -std=gnu99 -O2 -o a.out source_file.c -lm)
