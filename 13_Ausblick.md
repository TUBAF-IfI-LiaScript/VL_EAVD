<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female


script: https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.js

link:   https://cdn.jsdelivr.net/chartist.js/latest/chartist.min.css

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

# Vorlesung XI - Anwendung auf abstrakte Algorithmen

**Fragen an die heutige Veranstaltung ...**

* Was ist ein Algorithmus und über welche Merkmale lässt er sich ausdrücken.
* Nennen Sie Beispiele für Algorithmen aus dem täglichen Leben.
* Wie erfolgt die Transformation des Algorithmus auf eine Programmiersprache?
* Was bedeutet der Begriff der Komplexität eines Algorithmus?
* Welchem fundamentalen Konzept der Informatik unterliegen der Quicksort Algorithmus und die binäre Suche?

---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/12_Algorithmen.md

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

## 0. Mehr als eine Datei ...



## 1. Grafische Benutzerinterfaces

Eventgesteuerte Programmabarbeitung


### GTK Konzepte

![GTKArchitektur](./img/GTK-Architecture.png)

### Hello World Beispiele

## 2. C und C++, dass klingt doch sehr ähnlich

```cpp    HelloWorld.cpp
#include <iostream>
using namespace std;

int main()
{
    cout << "Hello, World!";
    return 0;
}
```
Was ist jetzt das besondere? Im Beispiel ändert sich lediglich die API der Ausgaben und die _includes_ haben kein ".h" mehr?

Analog zu C ist C++ eine von der ISO genormte Programmiersprache. Sie wurde ab 1979 von Bjarne Stroustrup  bei AT&T als Erweiterung der Programmiersprache C entwickelt.
C++ erweitert die Abstraktionsmöglichkeiten erlaubt aber trotzdem eine
maschinennahe Programmierung. Der Standard definiert auch eine Standardbibliothek, zu der wiederum verschiedene Implementierungen existieren.

| Jahr | Entwicklung                                         |
|:-----|:----------------------------------------------------|
| 1979 | „C with Classes“ -  Klassenkonzept mit Datenkapselung, abgeleitete Klassen, ein strenges Typsystem, Inline-Funktionen und Standard-Argumente |
| 1983 | "C++" - Überladen von Funktionsnamen und Operatoren, virtuelle Funktionen, Referenzen, Konstanten, eine änderbare Freispeicherverwaltung |
| 1985 | Referenzversion                                     |
| 1989 | Version 2.0 - Mehrfachvererbung, abstrakte Klassen, statische Elementfunktionen, konstante Elementfunktionen|
| 1998  | ISO/IEC 14882:1998 oder C++98                      |
| ...   | Kontinuierliche Erweiterungen C++11, C++17, ...    |

Oft geäußerte Kritik an der Sprache umfasst beispielsweise:

+ C++ sei zu low-level-mäßig aufgebaut
+ C++ ist sehr komplex
+ Geschwindigkeitsvorteil als fehlendes Argument für Anwendungsentwickler

> “In C++ it’s harder to shoot yourself in the foot, but when you do, you blow off your whole leg.” \[Bjarne Stroustrup\]

### Objektorientierte Programmierung

Wo sind wir? C erlaubt es abstrakte Datentypen für einen spezifischen Anwendungsfall zu entwickeln, diese mit ener dosierten Lebensdauer und Geltungsbereich zu versehen.

```cpp
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Students {
   char  name[50];
   int   matrikel;
} student;

void printEntry(struct Students student){
  printf("Der Student %s hat die Matrikel %d", student.name, student.matrikel);
}

int main(void) {
  struct Students student1;
  strcpy(student1.name,"Humboldt");
  student1.matrikel = 12345;
  printEntry(student1);
  return EXIT_SUCCESS;
}
```
@Rextester.eval

Was wollen wir gern erreichen:

+ Kapselung - Strukturierung eines Programms in mehrere voneinander unabhängig operierenden Objekten, die "ihre" Daten bündeln
+ Geheimnisprinzip - die internen Daten eines Objekts sollen dem Benutzer verborgen werden. Sofern notwendig gibt es aber Funktionen, die notwendige Zugriffe lenken
+ Vererbung - Wiederverwendung von Code soll durch die Übernahme von Objektkonfigurationen realisiert werden. Vererbung ermöglicht die  Erweiterung bestehender Objekt um speziellere Funktionalität aber auch die Weitergabe entlang einer Hierarchie von Oberklassen
+ Polymorphie Durch Subtyping kann anstelle eines Basistyps eine beliebige davon abgeleitete Klasse
verwendet werden. Durch dynamisches Binden der Methodenaufrufe des Objekts kommen die
in der abgeleiteten Klasse überschriebenen Methoden zur Laufzeit anstelle derjenigen aus der
Basisklasse zur Ausführung. Hierdurch wird es einfach einmal geschriebene Algorithmen auf
neue Objekte mit passender Schnittstelle anzuwenden, ohne die bestehende Implementierung
anzupassen.
+ Überladung Da Objektklassen auf Oberklassen implizit konvertiert werden, wird Überladung be-
sonders nützlich. Diese erlaubt mehrere sematisch ähnliche Funktionen mit unterschiedlicher
Signatur unter einen Namen zu gruppieren. Die Auswahl der konkret aufgerufenen Funktion
wird zur Compilezeit durch die Typen der Parametervariablen getroffen.

### Elemente Objektorientierter Programmierung im Beispiel

Klassen erweitern das Konzept der `structs` und verschmelzen Daten und Methoden
in einem "Objekt" und deklarieren den individuellen Zugriff. Die wichtigste Eigenschaft einer Klasse ist, dass es sich um einen Typ handelt!

```cpp
class class_name {
  access_specifier_1:
    member1;
  access_specifier_2:
    member2;
  ...
}object_name;

class_name instance_name;
```
Wenn `class_name`  ein gültiger Bezeichner für die Klasse ist, ist `object_name` eine optionale Liste von Namen für Objekte dieser Klasse. Der Hauptteil der Deklaration kann _member_ enthalten, die entweder Daten- oder Funktionsdeklarationen sein können und jeweils einem Zugriffsbezeichner `access_spefier`.

Ein Zugriffsbezeichner ist eines der folgenden drei Schlüsselwörter: `private`, `public` oder `protected`. Diese Bezeichner ändern die Zugriffsrechte für die *member*, die ihnen nachfolgen:

+ `private` *member* einer Klasse sind nur von anderen *members* derselben Klasse (oder von ihren "Freunden") aus zugänglich.
+ `protected`  *member*  sind von anderen  *member*  derselben Klasse (oder von ihren "Freunden") aus zugänglich, aber auch von Mitgliedern ihrer abgeleiteten Klassen.
+ `public` *member*  sind öffentliche  *member*  von überall her zugänglich, wo das Objekt sichtbar ist.

**Einführungsbeispiel**

```cpp
#include <iostream>
using namespace std;

class Rectangle {
  private:     // nicht nötig, default Konfiguration
    int width, height;
  public:
    void set_values (int,int);          // Deklaration
    int area() {return width*height;}   // Deklaration und Defintion
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}

int main () {
  Rectangle rect;
  rect.set_values (3,4);
  cout << "area: " << rect.area();
  return 0;
}
```
@Rextester.eval

Folgender Code zeigt eine beispielhafte Implementierung einer Klasse "Rectangle".
Die einzigen  *member* von rect, auf die von außerhalb der Klasse nicht zugegriffen werden kann, sind _width_ und _height_, da sie über einen privaten Zugriff verfügen und nur von anderen Mitgliedern derselben Klasse aus referenziert werden können.

In diesem Beispiel wird der Bereichsoperator (`::` zwei Doppelpunkte) eingeführt. Hier wird es bei der Definition der Funktion _set_values_ ​​verwendet, um ein Member einer Klasse außerhalb der Klasse selbst zu definieren.

Lassen Sie uns einige Experimente machen:

+ Legen Sie eine weitere Instanz der Klasse `Rectangle` an!
+ Versuchen Sie aus der `main()` Funktion heraus auf die `private` Variablen width oder height zuzugreifen.
+ Implementieren Sie eine weitere Funktion, die feststellt, ob es sich um ein Quadrat handelt.
+ Was passiert, wenn Sie die Flächenberechnung aufrufen, bevor Sie width and height initialisiert haben?

**Konstruktoren**

Das Verhalten ist unbestimmt! Wir müssen also dafür sorgen, dass vor der Verwendung
einer Klasseninstanz alle notwendigen Membervariablen ein Wert zugewiesen wurde.
Diese Aufgabe übernehmen sogenannte Konstruktoren.

```cpp
class_name::class_name(parameter){
    // initalisiert die Variablen
}
```
Diese Konstruktorfunktion wird wie eine reguläre Memberfunktion deklariert,
jedoch mit einem Namen, der mit dem Klassennamen übereinstimmt. Die Parameterliste
wird bei der Deklaration einer Instanz übergeben. Es gibt keinen
Rückgabewert!

Ändern Sie das nachfolgende Beispiel ab, so dass wir statt `set_values` einen
Konstruktor benutzen.

```cpp
#include <iostream>
using namespace std;

class Rectangle {
  private:     // nicht nötig, default Konfiguration
    int width, height;
  public:
    void set_values (int,int);          // Deklaration
    int area() {return width*height;}   // Deklaration und Defintion
};

void Rectangle::set_values (int x, int y) {
  width = x;
  height = y;
}

int main () {
  Rectangle rect;
  rect.set_values (3,4);
  cout << "area: " << rect.area();
  return 0;
}
```
@Rextester.eval





## 3. Anwendung auf der Mikrocontrolerebene

## That's alll

Vielen Dank für Ihre Teilnahme an der Veranstaltung!
