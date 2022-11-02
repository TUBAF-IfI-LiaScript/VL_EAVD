<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner


-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md)

# Grundlagen der Sprache C

| Parameter                 | Kursinformationen                                                                                                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**        | `Einführung in das wissenschaftliche Programmieren`                                                                                                                                                                                           |
| **Semester**              | `Wintersemester 2022/23`                                                                                                                                                                                                         |
| **Hochschule:**           | `Technische Universität Freiberg`                                                                                                                                                                                                |
| **Inhalte:**              | `Ein- und Ausgabe / Variablen`                                                                                                                                                                                               |
| **Link auf Repository: ** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/01_EingabeAusgabeDatentypen.md) |
| **Autoren**               | @author                                                                                                                                                                                                                          |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

---------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Durch welche Parameter ist eine Variable definiert?
* Erklären Sie die Begriffe Deklaration, Definition und Initialisierung im
  Hinblick auf eine Variable!
* Worin unterscheidet sich die Zahldarstellung von ganzen Zahlen (`int`) von den
  Gleitkommazahlen (`float`).
* Welche Datentypen kennt die Sprache C++?
* Erläutern Sie für `char` und `int` welche maximalen und minimalen Zahlenwerte
  sich damit angeben lassen.
* Ist `printf` ein Schlüsselwort der Programmiersprache C++?
* Welche Beschränkung hat `getchar`

> **Vorwarnung:** Man kann Variablen nicht ohne Ausgaben und Ausgaben nicht ohne
>Variablen erklären. Deshalb wird im folgenden immer wieder auf einzelne Aspekte
> vorgegriffen. Nach der Vorlesung sollte sich dann aber ein Gesamtbild ergeben.

---------------------------------------------------------------------


```cpp                     GoodBy.cpp
#include <iostream>

int main() {
  std::cout << "... \t bis \n\t\t zum \n\t\t\t";
  std::cout << "naechsten \n\t\t\t\t\t mal! \n";
	return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ main.cpp -o a.out`, `./a.out`)


<!--START_SKIP_IN_PDF-->
## Quizze
