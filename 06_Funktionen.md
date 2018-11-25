<!--

author:   Sebastian Zug & André Dietrich
email:    zug@ovgu.de   & andre.dietrich@ovgu.de
version:  0.0.1
language: de
narrator: Deutsch Female

comment:  This is a very simple comment.
          Multiline is also okay.

translation: English   translation/english.md

script:   https://felixhao28.github.io/JSCPP/dist/JSCPP.es5.min.js

@JSCPP
<script>
  try {
    var output = "";
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s;}}});
    output;
  } catch (msg) {
    console.log(msg);
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

-->


# Vorlesung VI - Funktionen

**Fragen an die heutige Veranstaltung ...**

* todo

---------------------------------------------------------------------
Link auf die aktuelle Vorlesung im Versionsmanagementsystem GitHub

https://github.com/liaScript/CCourse/blob/master/06_Funktionen.md

---------------------------------------------------------------------

**Wie weit sind wir schon gekommen?**

ANSI C (C89)/ Schlüsselwörter:

|Standard   |            |            |            |             |            |             |
|:----------|:-----------|:-----------|:-----------|:------------|:-----------|:------------|
| C89/C90   | auto | <span style="color:blue">double</span> | <span style="color:blue">int</span> | <span style="color:blue">struct</span> | <span style="color:blue">break</span>|
|           | <span style="color:blue">else</span>  | <span style="color:blue">long</span> |  <span style="color:blue">switch</span> |  <span style="color:blue">case</span> | enum |
|           | register | typedef | <span style="color:blue">char</span> | extern | return |
|           | union | const | <span style="color:blue">float</span> | <span style="color:blue">short</span> | <span style="color:blue">unsigned</span>  |
|           |  <span style="color:blue">continue</span>  | <span style="color:blue">for</span>  | <span style="color:blue">signed</span> | <span style="color:blue">void</span> | default |
|           | <span style="color:blue">goto</span>  | <span style="color:blue">sizeof</span> | volatile | <span style="color:blue">do</span>  | <span style="color:blue">if</span> |
|           | static |  <span style="color:blue">while</span> |
| C99  | <span style="color:blue">_Bool</span>   | _Complex | _Imaginary | inline | restrict |
| C11  | _Alignas | _Alignof | _Atomic | _Generic |  _Noreturn|
|      |_Static\_assert | \_Thread\_local|

Standardbibliotheken

|Name       | Bestandteil| Funktionen                           |
|:----------|:-----------|:-------------------------------------|
|<stdio.h> 	|            | Input/output (printf)                |
|<stdint.h> |(seit C99)  | Integer Datentypen mit fester Breite |
|<float.h> 	|            | Parameter der Floatwerte             |
|<limits.h> |            | Größe der Basistypen                 |
|<fenv.h>   |            | Verhalten bei Typumwandlungen        |
|<string.h> |            | Stringfunktionen                     |
https://en.cppreference.com/w/c/header

---------------------------------------------------------------------

## 0. Wiederholung

**Initialisierung von n-dimensionalen Arrays**

```cpp                          nDimArray.c
#include <stdio.h>

int main() {
  if (0 && 2) printf("Aussage 1. ist war\n");
  else printf("Aussage 1. ist falsch\n");
  if (5 & 2) printf("Aussage 2. ist war\n");
  else printf("Aussage 2. ist falsch\n");
  return 0;
}
```
@JSCPP(@input, )



## 1. Definition von Funktionen



Prozedurale Programmierung Ideen und KOnzepte


### Was sind überhaupt Funtionen

Funktionen sind Unterprogramme, die ein Ausgangsproblem in kleine, möglicherweise
wiederverwendbare Codeelemente zerlegen.

```cpp                          standardabweichung.c
#include <stdio.h>

int main() {
  int a[] = {3,4,5,6,2,3,2,5,6,7,8,10};
  // Berechunung des Mittelwertes

  // Berechung der Varianz
  
  return 0;
}
```
@JSCPP(@input, )



## 2.  Globale, lokale und statische Variablen



## Beispiel des Tages

Berechnen Sie einen gleitenden Mittelwert und das Maximum aus folgender Zahlenreihe.
Geben Sie das Resultat in einem Graphen wieder.

```cpp                     magicSquare.c
#include <stdio.h>

int main(){

  return 0;
}
```
@JSCPP(@input, )
