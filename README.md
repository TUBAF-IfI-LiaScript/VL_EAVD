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
    JSCPP.run(`@0`, `@1`, {stdio: {write: s => { output += s.replace(/\n/g, "<br>");}}});
    output;
  } catch (msg) {
    var error = new LiaError(msg, 1);
    var log = msg.match(/(.*)\nline (\d+) \(column (\d+)\):.*\n.*\n(.*)/);
    var info = log[1] + " " + log[4];

    if (info.length > 80)
      info = info.substring(0,76) + "..."

    error.add_detail(0, info, "error", log[2]-1, log[3]);

    throw error;
  }
</script>
@end


-->

# C-Kurs

![C logo](img/logo.png)

See the interactive version at
[https://LiaScript.github.io](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/README.md)

## Beispiel

Ausführbarer C Code sieht wie folgt aus, der Titel kann weggelassen werden.

```cpp                     HelloWorld.c
#include<stdio.h>

int main() {
	printf("Hello World\\n");
	return 0;
}
```
@JSCPP(@input, )

Das folgende Beispiel illustriert die Übergabe von Argumenten über die "Commandozeile".

```cpp                     ExtendedHelloWorld.c
#include<stdio.h>

int main( int argc, char *argv[]){
  if( argc == 2 ) {
     printf("The argument supplied is %s\n", argv[1]);
  }
  else if( argc > 2 ) {
     printf("Too many arguments supplied.\n");
  }
  else {
     printf("One argument expected.\n");
  }
}
```
``` text                  stdin
TestInput
```
@JSCPP(@input,`@input(1)`)


## Zielstellung der Veranstaltung

     + Grundlegendes Verständnis von (hardwarenaher) Programmierung
     + Elementare Fähigkeiten in der Programmiersprache C
     + Anwendung von Programmiertools im Entwicklungsprozess

## Literaturempfehlungen



## Vorlesungsinhalte

[1. Einführung](https://LiaScript.github.io/course/?https://raw.githubusercontent.com/liaScript/CCourse/master/lectures/Einfuehrung.md)
