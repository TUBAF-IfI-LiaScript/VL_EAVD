<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.2
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://github.com/LiaTemplates/AVR8js/main/README.md#10
        https://raw.githubusercontent.com/liascript-templates/plantUML/master/README.md

-->

# Zusammengesetzte Datentypen

Die interaktive Version des Kurses ist unter diesem [Link](https://liascript.github.io/course/?https://raw.githubusercontent.com/SebastianZug/VL_ProzeduraleProgrammierung/master/06_ZusammengesetzteDatentypen.md#1) zu finden.

**Wie weit waren wir gekommen?**



**Inhalt der heutigen Veranstaltung**

*

**Fragen an die heutige Veranstaltung ...**

*

## Motivation

Test

## Beispiel des Tages

Generieren Sie mit einem C-Programm Dateien im Excelformat, um diese dann weiter
verarbeiten zu können. Dazu nutzen wir die Bibliothek `libxlsxwriter`, deren
Dokumentation und Quellcode Sie unter

[https://libxlsxwriter.github.io/index.html](https://libxlsxwriter.github.io/index.html)

finden. Die Dokumentation für die im Beispiel verwendeten Funktionen findet sich
dann für `lxw_workbook` auf der Seite

[https://libxlsxwriter.github.io/workbook_8h.html](https://libxlsxwriter.github.io/workbook_8h.html#a1cf96608a23ee4eb0e8467c15240d00b)


```cpp
#include "xlsxwriter.h"
/* Some data we want to write to the worksheet. */
struct expense {
    char item[32];
    int  cost;
};
struct expense expenses[] = {
    {"Rent", 1000},
    {"Gas",   100},
    {"Food",  300},
    {"Gym",    50},
};
int main() {
    /* Create a workbook and add a worksheet. */
    lxw_workbook  *workbook  = workbook_new("tutorial01.xlsx");
    lxw_worksheet *worksheet = workbook_add_worksheet(workbook, NULL);
    /* Start from the first cell. Rows and columns are zero indexed. */
    int row = 0;
    int col = 0;
    /* Iterate over the data and write it out element by element. */
    for (row = 0; row < 4; row++) {
        worksheet_write_string(worksheet, row, col,     expenses[row].item, NULL);
        worksheet_write_number(worksheet, row, col + 1, expenses[row].cost, NULL);
    }
    /* Write a total using a formula. */
    worksheet_write_string (worksheet, row, col,     "Total",       NULL);
    worksheet_write_formula(worksheet, row, col + 1, "=SUM(B1:B4)", NULL);
    /* Save the workbook and free any allocated memory. */
    return workbook_close(workbook);
}
```

![Resultat](./images/06_ZusammengesetzteDatentypen/excelLib.png)
