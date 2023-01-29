<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.5
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DatenAnalyse.md)

# Daten- und Zeitreihenanalysen

| Parameter                | Kursinformationen                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Veranstaltung:**       | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                    |
| **Semester**             | `Wintersemester 2022/23`                                                                                                                                                                       |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                                              |
| **Inhalte:**             | `Datenanalyse mit dem Python Paket Pandas`                                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DatenAnalyse.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DatenAnalyse.md) |
| **Autoren**              | @author                                                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------


**Fragen an die heutige Veranstaltung ...**

* 

---------------------------------------------------------------------

Organisatorisches
========================




## Motivation

                           {{0-1}}
****************************************************************************

> Aufgabe: Dokumentieren Sie die zeitliche Verteilung des Erscheinens von Vögeln an einer Futterstelle. Zu welcher Tages / Nachtzeit ist die Aktivität am größten?

![instruction-set](./images/11_DatenAnalyse/Vogelhaus.jpg "Vogelhaus (Fotograph Sagar Kumar Singh [Pexels](https://www.pexels.com/de-de/foto/regentropfen-vogel-holzern-hangen-10301518/))")<!-- width="80%" -->

****************************************************************************

                           {{1-2}}
****************************************************************************
<!--
style="width: 100%; min-width: 620px; max-width: 920px;"
-->
```ascii 
                            Datenlogger                    Speichermedium         Auswertung
                            +------------------------+
                            |                        |     +---------------+
                       +    |         +-----------+  |  +->| Speicherkarte |      +-------------------+ 
       Umgebung-       |\   | Sensor- | Controll- |  |  |  +---------------+      | Einlesen          |  
       phänomene       | +--|-------->| Software  |--|--+                         | Analyse           |
                       |/   | signale |           |  |  |  +---------------+      | Diagrammerzeugung |
                       +    |         +-----------+  |  +->| Datenserver   |      | ...               |   
                            |                        |     +---------------+      +-------------------+
                            |                        |                             ^ 
                            +------------------------+     +--------------+        |          .....
                                                           | ...          |\       | .... ....     .
                                                           | 12:30 Temp 12+-+      |.    .
                                                           | 12:40 Temp 13  |      |
                                                           +----------------+      +------------------>
                                                                          
```

Und der Code für den Datenlogger? Wir werten den Beschleunigungssensor unseres Controllerboards aus.

```cpp
#include "Sensor.h"
#include "RGB_LED.h"

DevI2C i2c(D14,D15);
LSM6DSLSensor sensor(i2c,D4,D5);
int xAxesData[3];

void setup() {
    Serial.begin(115200);         //Baudrate der Seriellen Schnittstelle
    sensor.init(NULL);            //Start des Sensors
    sensor.enableAccelerator();   //Aktivierung des Beschleunigungssensors
}

void loop() {
    sensor.getXAxes(xAxesData);  //Lesen der Daten
    Serial.printf("; %d; %d; %d\n",xAxesData[0],xAxesData[1],xAxesData[2]);
                                 //Ausgabe der Daten via Serielle 
                                 //Schnittstelle
    delay(10);
}
```

> Aufgabe: Bewerten Sie die Implementierung! Welche Nachteile sehen Sie?

****************************************************************************

                           {{2-3}}
****************************************************************************

Für die Konfiguration des Zeitstempels im Visual Studio Code wurde der Parameter _Arduino: Change Timestamp Format_ `%T.%L` [strftime Format](https://github.com/samsonjs/strftime#supported-specifiers) gesetzt.

Die Daten liegen als sogenannten _Comma-separated values_ in einer csv Datei vor. Sie sind eine bequeme Möglichkeit, Daten aus Tabellenkalkulationen und Datenbanken zu exportieren und sie in andere Programme zu importieren oder zu verwenden. CSV-Dateien lassen sich sehr einfach programmatisch bearbeiten. Jede Sprache, die die Eingabe von Textdateien und die Manipulation von Zeichenketten unterstützt (wie Python), kann direkt mit CSV-Dateien arbeiten. Nachteilig ist, dass alle Inhalte als Text angelegt werden und damit verschwenderisch mit dem Speicher umgehen.

Als Trenner wurde hier das `;` verwendet. 

```text 
09:28:52.419; -7; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
09:28:52.463; -16; -2; 1006               
09:28:52.474; -69; -160; 1057
09:28:52.485; 58; 136; 984
09:28:52.496; -10; -10; 1019
09:28:52.507; -11; -6; 1012
09:28:52.518; -5; 0; 1016
09:28:52.528; -9; -15; 1013
09:28:52.539; -9; -8; 1018
09:28:52.551; -8; -9; 1016
09:28:52.562; -8; -9; 1019
```

> + Wie groß ist das normale Rauschen der Messwerte?
> + Wann wurde die größte Änderung der Beschleunigung gemessen?
> + Stellen Sie die Verlauf in einem Diagramm dar, benennen Sie die Achsen, erzeugen Sie ein Gitter.

> __MEMO!__ Arbeiten Sie bei der Analyse immer auf Kopien der eigentlichen Daten. Im Fall einer "Kompromitierung" durch eine einfache Schreiboperation haben Sie immer noch den Originaldatensatz zur Verfügung.

****************************************************************************

### Lösungsansatz 1: Office Tabellenkalkulation

```text data.csv 
timestamp;X;Y;Z
09:28:52.419; -7; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```

Nutzen Sie die Importfunktion für csv-Dateien

### Lösungsansatz 2: Python nativ

Python kann die Textdateien umittelbar einlesen

1. Öffnen der Datei für das Lesen 
2. Zeilenweises einlesen der Daten 

    + Erfassen der Spaltennamen aus der ersten Zeile
    + Zerlegen anhand des `delimters` (hier `;`)
    + Ablegen in einer vorbereiteten Datenstruktur  

3. Schließen der Datei 
4. Analyse der Daten

Diese Schrittfolge können wir mit dem Standardpaket [csv](https://docs.python.org/3/library/csv.html) etwas vereinfachen.

```text data.csv 
timestamp;X;Y;Z
09:28:52.419; -7; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python readCSV.py
import csv

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';',)
    list_of_dict = list(csv_reader)

print(f"{len(list_of_dict)} Datensätze gelesen!")
for row in list_of_dict:
	print(row)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

> __Aufgabe:__ Bestimmen Sie die vorkommenden Maxima pro Spalte oder berechnen Sie die differenz zwischen zwei benachbarten Werten einer Beschleunigungsachse.

### Lösungsansatz 3: Python mit Pandas 

[pandas](https://pandas.pydata.org/) ist eine für die Programmiersprache Python geschriebene Softwarebibliothek zur Datenmanipulation und -analyse, die insbesondere Datenstrukturen und Operationen zur Manipulation von numerischen Tabellen und Zeitreihen bietet. Es handelt sich um freie Software.

Der Name leitet sich von dem Begriff "_panel data_" ab, einem Begriff aus der Ökonometrie für Datensätze, die Beobachtungen über mehrere Zeiträume für dieselben Personen enthalten.

+ __Skalierbarkeit__ - Pandas ist nur durch die Hardware begrenzt und kann größere Datenmengen verarbeiten. Excel ist aktuell auf 1.048.576 Zeilen und 16.384 Spalten beschränkt.
+ __Geschwindigkeit__ - Pandas arbeitet viel schneller als eine Tabellenkaklulation, was sich besonders bei der Arbeit mit größeren Datenmengen bemerkbar macht.
+ __Automatisierung__ - Viele der Aufgaben, die mit Pandas durchgeführt werden können, sind extrem einfach zu automatisieren, wodurch die Anzahl der langweiligen und sich wiederholenden Aufgaben, die täglich durchgeführt werden müssen, reduziert wird.
+ __Interpretierbarkeit__ - Eine Codesequenz aus Pandas ist übersichtlich und einfach zu interpretieren, da Tabellenkalkulationen Berechnungen pro Zelle ausführen, sind Fehler schwieriger zu identifizieren und zu beheben.
+ __Erweiterte Funktionen__ - Die Durchführung erweiterter statistischer Analysen und die Erstellung komplexer Visualisierungen ist sehr einfach.

Der Code zum Paket kann unter [Link](https://github.com/pandas-dev/pandas) eingesehen und bearbeitet werden.

## Pandas Grundlagen

Pandas kennt zwei grundsätzliche Datentypen [Series]() und [DataFrame]()

|     | Pandas Series                                                                                     | Pandas DataFrame                                                                                      |
| --- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Format    | Eindimensional                                                                                    | Zweidimensional                                                                                       |                                                                                                       
| Datentypen    | Homogen - Reihenelemente müssen vom gleichen Datentyp sein.                                       | Heterogen - DataFrame-Elemente können unterschiedliche Datentypen haben.                              |
| Zahl der Einträge    | Größenunveränderlich - Einmal erstellt, kann die Größe nicht geändert werden. | Größenveränderlich - Elemente können in einem bestehenden DataFrame gelöscht oder hinzugefügt werden. |

Wir betrachten zunächst die grundsätzliche Arbeitsweise für Series Daten.

```python    PandasSeries.py
import pandas as pd
import numpy as np

#Zufallszahlen mit dem Paket "numpy"
s_1 = pd.Series(np.random.randn(5))
print(s_1)

#Zufallszahlen und individuelle Indizes 
s_2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s_2)

# Für unseren Datensatz und die Z Beschleunigungsdaten
data = {"09:28:52.419": 1016, "09:28:52.430": 1017, "09:28:52.441": 1017}
s_3 = pd.Series(data)
print(s_3)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> __Achtung:__ Im letztgenannten Beispiel `s_3` werden die Indizes nicht als Datum interpretiert sonder als Text. Realistisch wäre hier noch eine Transformation notwendig!

```python    PandasDataFrame.py
import pandas as pd
import numpy as np

#Multidimensionales DataFrame mit identischen Datentypen
df_1 = pd.DataFrame(np.random.randn(6, 4))
print(df_1)
print()

#Variables Set von Daten unterschiedlicher Typen 
df_2 = pd.DataFrame(
    {
        "A": True,
        "B": pd.date_range("20230101", periods=4),
        "C": pd.Series(np.random.randn(4)),
        "D": np.random.randint(16, size=4),
        "E": pd.Categorical(["A", "A", "B", "C"]),
        "F": "foo",
    }
)
print(df_2)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Aufgabe: Evaluieren Sie mittel `print(df_2.dtypes)` die realsierten Datentypen für `df_2`. Worüber "stolpern" Sie?

### Arbeit mit Dataframes 

indizierung 

filterung 

säuberung von Daten 

### Visualisierung mit pandas 

Zeitlicher verlauf
Scatterplot 
Histogram

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s.plot.bar()
plt.savefig('foo.png')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


## Noch mal der Blick auf Excel 

| pandas      | Tabellenkalkulation |
| ----------- | ------------------- |
| `DataFrame` | _worksheet_         |
| `Series`    | _column_            |
| `Index`     | _row headings_      |
| `row`       | _row_               |
| `NaN`       | empty cell          |


```python 
df = pd.read_excel("./myExcelFile.xlsx", index_col=0)

df.to_excel("./myExcelFile.xlsx")

```

## Beipspiel der Woche

```text data.csv 
timestamp;X;Y;Z
09:28:52.419; -7; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python readCSV.py
import pandas as pd

df = pd.read_csv('data.csv', header = 1)  
print(df)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)
