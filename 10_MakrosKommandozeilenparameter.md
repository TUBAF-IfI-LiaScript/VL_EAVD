<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female


script:  https://cdnjs.cloudflare.com/ajax/libs/echarts/4.1.0/echarts-en.min.js

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



@Rextester.pipe
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
    data: { LanguageChoice: 6,
            Program: `@input(0)`,
            Input: `@1`,
            CompilerArgs : "-Wall -std=gnu99 -O2 -o a.out source_file.c"}
    }).done(function(data) {
        if (data.Errors == null) {
            let warnings = grep_("warning", data.Warnings);

            let stats = "\n-------Stat-------\n"+data.Stats.replace(/, /g, "\n");

            if(data.Warnings)
              stats = "\n-------Warn-------\n"+data.Warnings + stats;

            send.lia("log", data.Result+stats, warnings, true);

            @input(1)

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

script:   https://cdn.rawgit.com/davidedc/Algebrite/master/dist/algebrite.bundle-for-browser.js

@algebrite.eval:    <script> Algebrite.run(`@input`) </script>
-->

# Vorlesung IX - Dynamische Speicherverwaltung

**Fragen an die heutige Veranstaltung ...**

*


---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/10_MakrosKommandozeilenparamter.md

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

### Debugging mit PellesC

https://forum.pellesc.de/index.php?topic=4194.0

Debugging mit PellesC

### Aufruf eines Programms

Bei der Verwendung von PellesC klicken Sie in der Regel auf einen Button, um
das Programm auszuführen. Sie können dies aber natürlich genauso auf der Kommandozeile
realisieren.

![Intetral](./img/PellesCAusfuehrung.jpeg)<!-- width="90%" -->[^1]

## 1. Kommandozeilenargumente

In vielen Fällen genügt es aber nicht, lediglich ein Programm zu starten, häufig
wollen Sie zusätzliche Parameter übergeben, die das Verhalten der Ausführung
bestimmen.

Beispiele:

+ Parameter für Berechnungen - Sie legen die Randbedingungen oder Startwerte einer Integralberechnung fest.
+ Filterkriterien - Sie suchen in unserem Namensdatenbank nach einer spezifischen Konfiguration von Datensätzen ("Alle weiblichen Vornamen, deren Träger zwischen 1955 und 1965 gebohren und mit G beginnen.")
+ Name der Datei, in die die Ausgaben geschrieben werden

Anwendungsfall gcc (C-Compiler)

Das Programm kennt eine Vielzahl von Eingabeparametern, die sich teilweise
gegenseitig bedingen.

1. Aufruf ohne Parameter - Fehler
``` bash @output
▶ gcc
gcc: fatal error: no input files
compilation terminated.
```

2. Abfordern der Versions- und Parameterkonfiguration
``` bash @output
▶ gcc -v
Using built-in specs.
COLLECT_GCC=gcc
COLLECT_LTO_WRAPPER=/usr/lib/gcc/x86_64-linux-gnu/5/lto-wrapper
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --with-pkgversion='Ubuntu 5.4.0-6ubuntu1~16.04.10' ...
Thread model: posix
gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10)
```

3. Aufruf der Hilfe
``` bash @output
▶ gcc --help
Usage: gcc [options] file...
Options:
  -pass-exit-codes         Exit with highest error code from a phase
  --help                   Display this information
  --target-help            Display target specific command line options
  --help={common|optimizers|params|target|warnings|[^]{joined|separate|undocumented}}[,...]
                           Display specific types of command line options
  (Use '-v --help' to display command line options of sub-processes)
  --version                Display compiler version information
  -dumpspecs               Display all of the built in spec strings
  -dumpversion             Display the version of the compiler
...
```
Das Verhalten des Programmes verändert sich in Abhänigkeit von der Wahl der
Kommandozeilenparameter.

``` bash @output
▶ gcc main.c
▶ gcc main.c -o main.out
```

### Erfassen der Parameter

```c
int main(int argc, char *argv[]) { /* ... */ } // anstatt
int main{void}
```

Dei zwei Parameter mit den Namen argc und argv. Die Namen dieser Parameter sind
NICHT vorgeschrieben und können beliebig angepasst werden. Allerdings sind
diese in vielen Programmiersprachen üblich, so dass der Lesefluss dadurch ggf.
gestört werden würde.

Die einzelnen Argumente, die dem Programm übergeben werden, müssen immer durch mindestens ein Leerzeichen getrennt sein.

| Name      | Datentyp                       | Inhalt                |
|:----------|:-------------------------------|:----------------------|
| argc      | integer                        | Zähler der Argumente  |
| acgv      | Pointer auf array von Pointern | Parameter             |


```cpp         InputArgs.c
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
   int i;

   printf("%d Parameter eingelesen\n", argc);

   for(i=0; i < argc; i++) {
      printf("argv[%d] = %s ", i, argv[i]);
      printf("\n");
   }
   return EXIT_SUCCESS;
}
```
``` bash @output
▶ ./a.out das ist ein Test
5 Parameter eingelesen
argv[0] = ./a.out
argv[1] = das
argv[2] = ist
argv[3] = ein
argv[4] = Test
▶
▶ ./a.out Leerzeichen als Trenner 4 5 6
7 Parameter eingelesen
argv[0] = ./a.out
argv[1] = Leerzeichen
argv[2] = als
argv[3] = Trenner
argv[4] = 4
argv[5] = 5
argv[6] = 6
```

### Überprüfungen

```c              CheckCommandlineParameters.c
#include <stdio.h>

int main( int argc, char *argv[] )  {
   if( argc == 2 ) {
      printf("Parameter erfasst - \"%s\"\nEs kann weitergehen ...", argv[1]);
   }
   else if( argc > 2 ) {
      printf("Zu viele Parameter!.\n");
   }
   else {
      printf("Erwartet einen Parameter!.\n");
   }
}
```

Ist das Format der Parameter korrekt?

## 2. Makros

## 3. Beispiel der Woche

Der folgende Code implementiert unterschiedliche Formen der numerische
Integration für Funktionen mit einer veränderlichen. Im Beispiel wurde

$$
f(x) = 2x^2 - 14
$$

gewählt und das bestimmte Integral in den Grenzen von 1 bis 10 für variierende
Schrittweiten bestimmt. Die exakte Lösung lässt sich mit Hilfe eines
Algebra-Systemes mittels des Befehls `defint` bestimmen.

Die Lösung umfasst sowohl das linksseitige als auch das rechtsseitige
Integral.

![Intetral](./img/Integrals.jpeg)<!-- width="90%" -->[^1]

[^1]: Bilder aus den Vorlesungsunterlagen von Lia Vas, University of the Sciences, Philadelphia

```Maxima
f=2*x^2-14
defint(f,x,1,10)
```
@algebrite.eval

```cpp                          Integral.c
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct samples{
  double x;
  double y;
};

double myFunction(double x){
  return 2 * x * x - 14;
}

struct samples * generateValues(double from, double to, int number){
  struct samples * values;
  values = malloc((number + 1) * sizeof(*values));
  double resolution = (to - from)/ number;
  for (int i=0; i <= number; i++){
      values[i].x = from + i * resolution;
      values[i].y = myFunction(values[i].x);
  }
  return values;
}

double int_leftrect(struct samples * values, int number){
   double resolution = (values[number].x - values[0].x)/ number;
   double sum = 0;
   for (int i=0; i < number; i++){
      //printf("%f %f\n", values[i].x, values[i].x);
       sum = sum + values[i].y * resolution;
   }
   return sum;
}

double int_rightrect(struct samples * values, int number){
   double resolution = (values[number].x - values[0].x)/ number;
   double sum = 0;
   for (int i=1; i <=number; i++){
       sum = sum + values[i].y * resolution;
   }
   return sum;
}

double int_trapez(struct samples * values, int number){
   double resolution = (values[number].x - values[0].x)/ number;
   double sum = 0;
   for (int i=0; i <number; i++){
       sum = sum + (values[i].y + values[i+1].y)/2 * resolution;
   }
   return sum;
}

int main(void) {
  struct samples * values;
  double from = 1;
  double to = 10;
  for (int number=3; number<150; number++){
    values = generateValues(from, to, number);
    printf("n = %3d - Integral = %f, %f, %f\n", number,
                                       int_leftrect(values, number),
                                       int_rightrect(values, number),
                                       int_trapez(values, number));
  }
  return EXIT_SUCCESS;
}
```
``` javascript -Analyse.js
let samples = data.Result.match(/[0-9.]+/g);

let label;
let series_1 = [];
let series_2 = [];
let series_3 = [];

for(let i=0; i<samples.length; i++) {
  //samples[i] = parseFloat(samples[i]);
  let value = parseFloat(samples[i]);
  switch (i % 4)
  {
    case 0:  label = value; break;
    case 1:  series_1.push([label, value]); break;
    case 2:  series_2.push([label, value]); break;
    case 3:  series_3.push([label, value]);
  }
}

let chart = echarts.init(document.getElementById('pipe_chart'));


let option = {
  title : {
    text: 'Original Data ',
    subtext: 'True coefficients'
  },
  toolbox: {
    show : true,
    feature : {
      mark : {show: true},
      dataZoom : {show: true},
      dataView : {show: true, readOnly: false},
      restore : {show: true},
      saveAsImage : {show: true}
    }
  },
  legend: {
      data:['series_1','series_2','series_3']
  },
  xAxis : [{
    type : 'value',
    scale: true,
    axisLabel : { formatter: '{value}' }
  }],
  yAxis : [{
    type : 'value',
    scale: true,
    axisLabel : { formatter: '{value}'}
  }],
  series : [{
    name: 'series_1',
    type: 'line',
    data: series_1,
  }, {
    name: 'series_2',
    type: 'line',
    data: series_2,
  },
  {
    name: 'series_3',
    type: 'line',
    data: series_3,
  }]
};


chart.setOption(option);
```
@Rextester.pipe

<div class="persistent" id="pipe_chart" style="position: relative; width:100%; height:400px;"></div>
