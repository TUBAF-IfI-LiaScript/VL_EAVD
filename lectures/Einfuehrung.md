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

# Vorlesung I - Einführung

## Fragen an die Veranstaltung ...

* Wie wird ein textuelles Programm in einen ausführbaren Code transformiert?
* Was bedeutet der Begriff Hochsprache, was verbirgt ist ein Assembler?
* Woraus ergibt sich die Aktualität der Sprache C?
* Welche Eigenschaften grenzt C von anderen Programmiersprachen ab?
* Welche Aufgabe hat ein Compiler?
* Wordurch definieren sich verschiedene "Geschmacksrichtungen" im Entwicklungsprozess

## 1. Grundlegendes

### Wie arbeitet ein Rechner eigentlich?

Beispiel: Intel 4004 Architektur (1971) (Author Appaloosa):

![atmel](https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1190px-4004_arch.svg.png)<!--style="width: 100%"-->


### Was heißt das "Maschinensprache"?

Jeder Rechner hat einen spezifischen Satz von Befehlen, die durch "0" und "1"
ausgedrückt werden, die er überhaupt abarbeiten kann.

* Speicherauszug den Intel 4004:
  *           {{1}}
    *******************************
    | Adresse | Speicherinhalt |
    |:--------|:---------------|
    | 0000    | 1101 0101      |
    | 0002    | 1111 0010      |
    ********************************
  *        {{2}}
    *****************************************************
    | Adresse | Speicherinhalt | OpCode     | Mneomonik |
    |:--------|:---------------|:-----------|:----------|
    | 0000    | 1101 0101      | 1101 DDDD  | LD $5     |
    | 0002    | 1111 0010      | 1111 0010  | IAC       |
    *****************************************************


### Was heißt das "Maschinensprache"?

Jeder Rechner hat einen spezifischen Satz von Befehlen, die durch "0" und "1"
ausgedrückt werden, die er überhaupt abarbeiten kann.

Speicherauszug den Intel 4004:

    {{1-2}}
| Adresse | Speicherinhalt |
|:--------|:---------------|
| 0000    | 1101 0101      |
| 0002    | 1111 0010      |

    {{2}}
| Adresse | Speicherinhalt | OpCode     | Mneomonik |
|:--------|:---------------|:-----------|:----------|
| 0000    | 1101 0101      | 1101 DDDD  | LD $5     |
| 0002    | 1111 0010      | 1111 0010  | IAC       |


Unterstützung für die Interpretation aus dem Nutzerhandbuch, das das Instruction set beschreibt[^1]:

    {{3}}
![instruction-set](../img/4004_Instruction_set.png)<!-- width="100%" -->


[^1]: Intel 4004 Assembler (Quelle: http://e4004.szyc.org/asm.html)

### Aber möchte man so umfangreiche Programme schreiben?

Vorteil - ggf. sehr effizienter Code (Größe, Ausführungsdauer), der gut auf die Hardware abgestimmt ist

Nachteile

* systemspezifische Realisierung
* geringer Abstraktionsgrad, bereits einfache Konstrukte benötigen viele Codezeilen
* weitgehende semantische Analysen möglich

``` asm Assembly
.START ST
ST: MOV R1, #2
    MOV R2, #1
M1: CMP R2, #20
    BGT M2
    MUL R1, R2
    INI R2
    JMP M1
M2: JSR PRINT
.END
```

``` fortran Fortran
A:=2;
FOR I:=1 TO 20 LOOP
    A:=A*I;
END LOOP;
PRINT(A);
```

> Eine höhere Programmiersprache ist eine Programmiersprache zur Abfassung eines
> Computerprogramms, die in **Abstraktion und Komplexität** von der Ebene der
> Maschinensprachen deutlich entfernt ist. ... Die Befehle müssen durch
> **Interpreter oder Compiler** in Maschinensprache übersetzt werden.

https://de.wikipedia.org/wiki/Liste_von_Programmiersprachen

### Compiliervorgang

FALSCHES BILD! richtig ist Compiler Struktur.png

> Ein **Compiler** (auch Kompiler; von englisch für zusammentragen bzw. lateinisch
> compilare ‚aufhäufen‘) ist ein Computerprogramm, das Quellcodes einer bestimmten
> Programmiersprache in eine Form übersetzt, die von einem Computer (direkter)
> ausgeführt werden kann.

<img src="https://github.com/liaScript/CCourse/blob/master/img/4004_Instruction_set.png" alt="drawing" width="500"/>

<span style="font-family:Papyrus; font-size:0.5em;">Source:
<a href="https://medium.com/@vietkieutie/what-happens-when-you-type-gcc-main-c-2a136896ade3">https://medium.com/@vietkieutie/what-happens-when-you-type-gcc-main-c-2a136896ade3</a> Intel 4004 Assembler</span>

## 2. Warum also C?

### Historische Einordnung

### Eigenschaften von C
