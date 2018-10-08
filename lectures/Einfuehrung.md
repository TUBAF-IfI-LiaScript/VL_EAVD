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

Beispiel: Intel 4004 Architektur (1971)

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/4004_arch.svg/1190px-4004_arch.svg.png" alt="drawing" width="500"/>

<span style="font-family:Papyrus; font-size:0.5em;">Source:
<a href="https://commons.wikimedia.org/wiki/File:4004_arch.svg">https://commons.wikimedia.org/wiki/File:4004_arch.svg</a> (Author Appaloosa)</span>

### Was heißt das "Maschinensprache"?

* Jeder Rechner hat einen spezifischen Satz von Befehlen, die er überhaupt abarbeiten kann.

   Befehl für den Intel 4004:

    ldm $5 // "1101 0101"
    iac    // "1111 0010"
