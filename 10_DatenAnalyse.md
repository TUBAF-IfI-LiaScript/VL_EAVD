<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de & jung@informatik.tu-freiberg.de
version:  1.0.0
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/10_DatenAnalyse.md)

# Datenanalyse mit Python

| Parameter                | Kursinformationen                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                              |
| **Inhalte:**             | `Datenanalyse mit dem Python Paket Pandas`                                                                                                                     |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_DatenAnalyse.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/10_DatenAnalyse.md) |
| **Autoren**              | @author                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------


**Fragen an die heutige Veranstaltung ...**

* Wie unterstützt das `numpy` Paket das Arbeiten mit großen wissenschaftlichen Datensätzen?
* Welche Datenformate sind für den Daten Austausch zwischen Mikrocontroller und Python Script üblich?
* Wie unterstützt das `pandas` Paket die wissenschaftliche Analyse von Datensätzen?
* Wie ändert sich der Analyseprozess verglichen mit der Verwendung einer Tabellenkalkulation?

## NumPy

NumPy (Numerical Python) ist eine grundlegende Bibliothek im Python-Ökosystem.

NumPy bietet leistungsstarke Werkzeuge für die effiziente Arbeit mit Arrays und Matrizen. 

Stellen Sie es sich als Pythons Methode vor, mathematische Operationen auf großen Datensätzen schnell und effektiv durchzuführen.

NumPy wird insbesondere bei der Datenanalyse, beim wissenschaftlichem Rechnen, der Bildverarbeitung und maschinellem Lernen verwendet, oft im Zusammenspiel mit weiteren Bibliotheken wie `pandas` und `matplotlib`.

> NumPy ist nicht Teil von Pythons Standardbibliothek und muss daher nachinstalliert werden. Hierfür gibt es verschiedene Methoden, die in den Übungen näher erklärt werden.

### NumPy: Effiziente, n-dimensionale Arrays

Ein wesentlicher Grund für die Existenz von NumPy liegt in der Unterstützung effizienter mathematischer Operationen auf n-dimensionalen Arrays (1D-Vektoren, 2D-Matrizen, nD-Tensoren).

- *N-dimensionale Arrays (ndarray)*: NumPy Arrays sind wesentlich effizienter als Python-Listen bei der Durchführung mathematischer Operationen auf großen Datenmengen. Python-Listen können beliebige Datentypen enthalten, wodurch sie für numerische Berechnungen weniger optimiert sind.

- *Effiziente Implementierung in C*: NumPy ist in C implementiert und nutzt auch C-Datentypen für Zahlen wie `uint8` oder `float32`. In Python sind `int` und `float` dagegen keine primitiven Datentypen sondern vollwertige Objekte, was sie oft komfortabler, aber auch weniger effizient macht.

- *Elementweise Operationen*: NumPy ermöglicht mathematische Operation auf ganzen Arrays, ohne dass explizit Schleifen durchlaufen werden müssen (z.B. `for`-Schleifen). Dies nennt man auch *Vektorisierung*.

```python  numpy_arrays.py
import numpy as np

# Ansatz mit Python Listen (langsam)
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result_list = []
for i in range(len(list1)):
    result_list.append(list1[i] + list2[i])
print(result_list)  # Output: [5, 7, 9]

# Ansatz mit NumPy Arrays (schnell)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result_array = array1 + array2  # Elementweises Addieren!
print(result_array)  # Output: [5 7 9]
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

NumPy wird näher in zwei einführenden *Jupyther Notebooks* erläutert (im Verzeichnis notebooks):

- Einführung in Numpy [numpy\_01\_intro.ipynb](notebooks/numpy_01_intro.ipynb)
- Bildverarbeitung mit Numpy [numpy\_02\_image_processing.ipynb](notebooks/numpy_02_image_processing.ipynb)


---------------------------------------------------------------------

## Motivation: Datenanalyse mit Python / Pandas

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
                       +    | Sensor- | Controll- |  |  +->| Speicherkarte |      +-------------------+ 
       Umgebung-       |\   |-------->| Software  |--|--+                         | Einlesen          |  
       phänomene       | +--| signale |           |  |  |  +---------------+      | Analyse           |
                       |/   |         +-----------+  |  +->| Datenserver   |      | Diagrammerzeugung |
                       +    |                        |     +---------------+      +-------------------+
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
    delay(10);                   //10ms warten
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

Nutzen Sie die Importfunktion für csv-Dateien Ihres Office-Programs (Excel, LibreOffice Calc, ...)

### Lösungsansatz 2: Python nativ

Python kann die Textdateien umittelbar einlesen

1. Öffnen der Datei für das Lesen
2. Zeilenweises einlesen der Daten

    * Erfassen der Spaltennamen aus der ersten Zeile
    * Zerlegen anhand des `delimiter` (hier `;`)
    * Ablegen in einer vorbereiteten Datenstruktur  

3. Schließen der Datei

   * durch `open()` ... `close()`
   * oder besser durch Verwendung von `with open() as`,
     was Datei automatisch schließt, siehe Beispiel unten.

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

# Einlesen der Daten
with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';',)
    list_of_dict = list(csv_reader)

# "Analyse" und Ausgabe
print(f"{len(list_of_dict)} Datensätze gelesen!")
for row in list_of_dict:
	print(row)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

> __Aufgabe:__ Bestimmen Sie die vorkommenden Maxima pro Spalte oder berechnen Sie die Differenz zwischen zwei benachbarten Werten einer Beschleunigungsachse.

### Lösungsansatz 3: Python mit Pandas 

[pandas](https://pandas.pydata.org/) ist eine für die Programmiersprache Python geschriebene Softwarebibliothek zur Datenmanipulation und -analyse, die insbesondere Datenstrukturen und Operationen zur Manipulation von numerischen Tabellen und Zeitreihen bietet. Es handelt sich um freie Software.

Der Name leitet sich von dem Begriff "_panel data_" ab, einem Begriff aus der Ökonometrie für Datensätze, die Beobachtungen über mehrere Zeiträume für dieselben Personen enthalten.

Der Code zum Paket kann unter [Link](https://github.com/pandas-dev/pandas) eingesehen und bearbeitet werden.

> __Achtung:__ Mit der Verwendung von pandas ändert sich unser Blick auf den Code. Bislang haben wir Prozedural oder Objektorientiert programmiert. Jetzt ändert sich unser Blick - wir denken in Datenstrukturen und wenden Methoden darauf an.

## Pandas Grundlagen

Pandas kennt zwei grundsätzliche Datentypen [Series]() und [DataFrame]()

|                   | Pandas Series                                                                 | Pandas DataFrame                                                                                      |
| ----------------- | ----------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| Format            | Eindimensional                                                                | Zweidimensional (Tabellen)                                                                                      |
| Datentypen        | Homogen - Reihenelemente müssen vom gleichen Datentyp sein.                   | Heterogen - DataFrame-Elemente können unterschiedliche Datentypen haben.                              |
| Zahl der Einträge | Größenunveränderlich - Einmal erstellt, kann die Größe nicht geändert werden. | Größenveränderlich - Elemente können in einem bestehenden DataFrame gelöscht oder hinzugefügt werden. |

Wir betrachten zunächst die grundsätzliche Arbeitsweise für _Series_ Daten.

```python    PandasSeries.py
import pandas as pd
import numpy as np

# Zufallszahlen mit dem Paket "numpy"
s_1 = pd.Series(np.random.randn(5))
print(s_1)

# Zufallszahlen und individuelle Indizes 
s_2 = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s_2)

# Für unseren Datensatz: Z Beschleunigungsdaten mit Zeitstempel als Index
data = {"09:28:52.419": 1016, "09:28:52.430": 1017, "09:28:52.441": 1017}
s_3 = pd.Series(data)
print(s_3)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> __Achtung:__ Im letztgenannten Beispiel `s_3` werden die Indizes nicht als Datum interpretiert sonder als Text. Realistisch wäre hier noch eine Transformation notwendig!

```python    PandasDataFrame.py
import pandas as pd
import numpy as np

# Multidimensionales DataFrame mit identischen Datentypen
df_1 = pd.DataFrame(np.random.randn(6, 4))
print(df_1)
print()

# Variables Set von Daten unterschiedlicher Typen 
df_2 = pd.DataFrame(
    {
        "A": True,
        "B": pd.date_range("20260101", periods=4),
        "C": pd.Series(np.random.randn(4)),
        "D": np.random.randint(16, size=4),
        "E": pd.Categorical(["A", "A", "B", "C"]),
        "F": "foo",
    }
)
print(df_2)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Aufgabe: Evaluieren Sie mittels `print(df_2.dtypes)` die realsierten Datentypen für `df_2`. Worüber "stolpern" Sie?

### Arbeiten mit Dataframes

Welche Aufgaben lassen sich nun mit Hilfe von Pandas über den Daten realisieren?

Einblicke in die Struktur von Dataframes
----------------

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python df_structure.py
import pandas as pd

# CSV-Datei einlesen
# Header-Info in erster Zeile (0 ist auch Default)
df = pd.read_csv('data.csv', header = 0, sep=";") 

print("-- Anzahl Zeilen und Spalten:", df.shape)
print("-- Spaltennamen:", df.keys().values)
print("-- Datentypen der Spalten:\n", df.dtypes)
print("-- Erste 5 Zeilen:\n", df.head(5))
# print("-- Letzte 5 Zeilen:\n", df.tail(5))
# print(df)  # Ausgabe des gesamten DataFrames 
             # (kann bei grossen Dateien unübersichtlich sein)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

Indizierung 
----------------

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python index.py
import pandas as pd

df = pd.read_csv('data.csv', header = 0, sep=";")

# Auswahl von Spalten
s: pd.Series = df.timestamp  # oder: s = df['timestamp']
print(s)
print("-- timestep 9:", df.timestamp[9])
print("-- Slice von timestamps:")
print(df.timestamp[5:8])

# Auswahl von Zeilen
print("-- Auswahl von Zeilen")
print(df[2:4])
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

Filtern 
----------------

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python filter.py
import pandas as pd

df = pd.read_csv('data.csv', header = 0, sep=";")  
print(df)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

Statistische Beschreibung 
----------------

Die Erzeugung deskriptiver Statistiken ist oft ein erster Schritt bei der Datenanalyse.

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python describe.py
import pandas as pd

df = pd.read_csv('data.csv', header = 0, sep=";")  
print(df.describe())
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)


Nutzung
----------------

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
09:28:52.430; -9; -8; 1017
09:28:52.441; -9; -8; 1017
09:28:52.452; -9; -8; 1017
```
```python describe.py
import pandas as pd

df = pd.read_csv('data.csv', header = 0, sep=";")  
print(df)
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)



### Visualisierung mit pandas

                            {{0-1}}
**********************************************************************************************

Pandas ist unmittelbar mit der Bibliothek matplotlib verknüpft. Damit können wir die matplotlib-Methoden nahtlos nutzen.

![](https://raw.githubusercontent.com/PatrikHlobil/Pandas-Bokeh/master/docs/Images/Startimage.gif)

_Beispiele der Visualisierung von Pandas 'PatrikHlobil' [Link](https://github.com/PatrikHlobil/Pandas-Bokeh/raw/master/docs/Images/Startimage.gif)_


```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
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
09:28:52.572; -8; -8; 1015
09:28:52.583; -8; -8; 1015
09:28:52.595; -9; -7; 1017
09:28:52.606; -9; -8; 1016
09:28:52.617; -8; -9; 1016
09:28:52.628; -7; -9; 1018
```
```python readCSV.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', header = 0, sep=";")  
df.plot()
plt.savefig('foo.png')
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

| Anpassung                      | API                                                                                      |                                                   |
| ------------------------------ | ---------------------------------------------------------------------------------------- | ------------------------------------------------- |
| Linientyp der Datendarstellung | [pyplot.plot](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html)     | `plt.plot(a, b, 'ro:')`                           |
| Achsenlabel hinzufügen         | [pyplot.xlabel](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.xlabel.html) | `plt.xlabel('my data', fontsize=14, color='red')` |
| Titel einfügen                 |  [pyplot.title](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.title.html)                                                                                       | `plt.title(r'$\sigma_i=15$')`                     |
| Gitter einfügen                |  [pyplot.grid](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.grid.html)                                                                                        | `plt.grid()`                                      |
| Legende                        |  [pyplot.legend](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html)                                                                                        | `plt.plot(a, b, 'ro:', label="Data")`             |
|                                |                                                                                          | `plt.legend()`                                    |
| Speichern                      |  [pyplot.savefig](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html)                                                                                        | `plt.savefig('foo.png') `                         |

> Merke: Mit dem zusätzlichen Parameter `styple='o:'` können Sie die Konfiguration der Darstellung anpassen.

**********************************************************************************************

                            {{1-2}}
**********************************************************************************************

> Aufgabe 1:  Weisen Sie grafisch nach, dass es einen starken Zusammenhang zwischen den 3 Beschleunigungsdaten gibt! 
>
> Aufgabe 2: Geben Sie die Daten einer Achse in einem Histogramm aus! Schreiben Sie als Text den maximalen und den Minimalen Wert in die Mitte des Diagrams.

```text -data.csv 
timestamp;X;Y;Z
09:28:52.353; -8; -9; 1016
09:28:52.364; -9; -8; 1017
09:28:52.375; -9; -8; 1017
09:28:52.386; -8; -8; 1016
09:28:52.397; -9; -8; 1017
09:28:52.408; -9; -8; 1018
09:28:52.419; -9; -8; 1016
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
09:28:52.572; -8; -8; 1015
09:28:52.583; -8; -8; 1015
09:28:52.595; -9; -7; 1017
09:28:52.606; -9; -8; 1016
09:28:52.617; -8; -9; 1016
09:28:52.628; -7; -9; 1018
```
```python ScatterPlot.py
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv', header = 0, sep=";")  
# Hier sind sie gefragt ...
plt.savefig('foo.png')
```
@LIA.eval(`["data.csv", "main.py"]`, `none`, `python3 main.py`)

**********************************************************************************************

## Noch immer von Excel überzeugt?

+ __Skalierbarkeit__ - Pandas ist nur durch die Hardware begrenzt und kann größere Datenmengen verarbeiten. Excel ist aktuell auf 1.048.576 Zeilen und 16.384 Spalten beschränkt.
+ __Geschwindigkeit__ - Pandas arbeitet viel schneller als eine Tabellenkaklulation, was sich besonders bei der Arbeit mit größeren Datenmengen bemerkbar macht.
+ __Automatisierung__ - Viele der Aufgaben, die mit Pandas durchgeführt werden können, sind extrem einfach zu automatisieren, wodurch die Anzahl der langweiligen und sich wiederholenden Aufgaben, die täglich durchgeführt werden müssen, reduziert wird.
+ __Interpretierbarkeit__ - Eine Codesequenz aus Pandas ist übersichtlich und einfach zu interpretieren, da Tabellenkalkulationen Berechnungen pro Zelle ausführen, sind Fehler schwieriger zu identifizieren und zu beheben.
+ __Erweiterte Funktionen__ - Die Durchführung erweiterter statistischer Analysen und die Erstellung komplexer Visualisierungen ist sehr einfach.
+ __Kompatibilität mit Excel-Dateien__ - _xslx_-Dateien können mit [read_excel()](https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html) eingelesen werden (d.h. ein Zwischenschritt mit Konvertierung zu CSV ist nicht notwendig).


| pandas      | Tabellenkalkulation |
| ----------- | ------------------- |
| `DataFrame` | _worksheet_         |
| `Series`    | _column_            |
| `Index`     | _row headings_      |
| `row`       | _row_               |
| `NaN`       | empty cell          |


```python 
# Einlesen einer Excel Datei in Pandas
df = pd.read_excel("./myExcelFile.xlsx", index_col=0)

# Schreiben einer Excel Datei aus Pandas
df.to_excel("./myExcelFile.xlsx")
```

## Beispiel der Woche

Der Deutsche Wetterdienst bietet auf seinen [Webseiten](https://www.dwd.de/DE/leistungen/cdc/cdc_ueberblick-klimadaten.html) eine vielzahl von historischen Datensätzen. Wir wollen unsere Pandas Kenntnisse nutzen, um uns darin zu orientieren und dann "Licht in den Nebel bringen".

Die historischen Aufzeichnungen zu verschiedenen Stationen in Deutschland finden sich in der [Datenbank](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/weather_phenomena/historical/). 

> Aufgabe 1: Finden Sie die Stationsnummern von sächsischen Stationen in der Übersicht der Wetterstationen. 

Den [Originaldatensatz](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/weather_phenomena/historical/wetter_tageswerte_Beschreibung_Stationen.txt) des deutschen Wetterdienstes können wir nicht verwenden - dieser ist als csv nicht ohne größeren Aufwand zu lesen. Daher wurde diese Datei aus didaktischen Gründen angepasst und liegt im Repository unter der angegebenen URL bereit.

```python findweatherstations.py
import pandas as pd

url="https://raw.githubusercontent.com/" + \
    "TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/" + \
    "master/examples/11_DatenAnalyse/" + \
    "Wetterdaten/wetter_tageswerte_Beschreibung_Stationen.txt"

df=pd.read_csv(url, sep=';', header = 0)  
#df=pd.read_csv("wetter_tageswerte_Beschreibung_Stationen.txt", sep=';', header = 0)  
df['Bundesland'] = df['Bundesland'].str.strip()
df['Stationsname'] = df['Stationsname'].str.strip()
df_sachsen = df[df.Bundesland  == "Sachsen"]
print(df_sachsen)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

Leider reicht der Freiberger Datensatz nur über wenige Jahre. Wir entscheiden uns für die weitere Untersuchung für die Daten aus Görlitz.

> Aufgabe 2: Laden Sie den Görlitzer Datensatz in einen Dataframe und zählen Sie die Nebeltage. Visualisieren Sie das Ergebnis.

Der avisierte Datensatz für die Station "1684" [heruntergeladen](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/weather_phenomena/historical/). Die Datei `wetter_tageswerte_01684_18800101_20181231_hist.zip` liefert als gepackter Ordner mehrere Datensets. Neben der eigentlichen Datendatei werden auch Stationskerndaten und Erhebungstechnik dokumentiert. 

```python extractFogObservations.py
import pandas as pd
import matplotlib.pyplot as plt

url="https://raw.githubusercontent.com/" + \
    "TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/" + \
    "master/examples/11_DatenAnalyse/" + \
    "Wetterdaten/" + \
    "wetter_tageswerte_01684_18800101_20181231_hist/" + \
    "produkt_wetter_tag_18800101_20181231_01684.txt"

df=pd.read_csv(url, sep=';', header = 0)  

df["JAHR"]=df["MESS_DATUM"]/10000
df["JAHR"] = df["JAHR"].astype('int')

df_fog = df[df.NEBEL!=-999]

print(f"{df_fog.NEBEL.count()} Tage im Datensatz, {df_fog.NEBEL.sum()} mit Nebel.")

ax = plt.axes()
df_fog.groupby("JAHR").NEBEL.sum().plot.bar(ax=ax)
ax.xaxis.set_major_locator(plt.MaxNLocator(20))
plt.ylabel("Häufigkeit von Nebelbeobachtungen")
plt.title("Nebeltage über Görlitz")
plt.grid()

#plt.show()  
plt.savefig('foo.png') # notwendig für die Ausgabe in LiaScript
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> Aufgabe: Evaluieren Sie, welche Parameter sich in den vergangenen Jahren signifikant verändert haben.

# Quiz
## CSV-Dateien
> Wofür steht *CSV*?
[( )] *Common System Variables*
[( )] *Colorful Systematic Visualization*
[(X)] *Comma-separated values*
[( )] *Critical Signal Version*

### Python nativ
> Wie lautet die Ausgabe des folgenden Programms, das die Daten aus der Datei data.csv einliest?
```text data.csv 
timestamp;X;Y;Z
09:28:52.419;-7;-8;1016
09:28:52.430;-9;-8;1017
09:28:52.441;-9;-8;1017
09:28:52.452;-9;-8;1017
```

```python
import csv

with open('data.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter=';',)
    list_of_dict = list(csv_reader)

for row in list_of_dict:
	print(row['X'], end=",")
```
[[-7,-9,-9,-9,]]

## Pandas Grundlagen
> Ordnen Sie *Pandas Series* und *Pandas Dataframes* die richtigen Eigenschaften zu.
[[*Pandas Series*]  [*Pandas Dataframe*]]
[(X)                ( )                 ] Eindimensional
[( )                (X)                 ] Zweidimensional
[( )                (X)                 ] Heterogene Datentypen
[(X)                ( )                 ] Homogene Datentypen
[(X)                ( )                 ] Größenunveränderlich
[( )                (X)                 ] Größenveränderlich

### Arbeit mit Dataframes
> Wie lautet die Ausgabe dieses Programms?
```python
import pandas as pd

a = [5, 7, 2, 7, 6]

s_1 = pd.Series(a, index=["a", "b", "c", "d", "e"])
print(s_1["c"])
```
[[2]]

{{1}}
**********************************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```python
import pandas as pd

d = {
    'A': [1,4,2,5],
    'B': [2,5,3,6],
    'C': [3,6,4,7],
    'D': [4,7,5,8]
}

s_1 = pd.Series(d)
print(s_1['C'][2])
```
[[4]]
**********************************************************************************************

{{2}}
**********************************************************************************************
> Wie lautet die Ausgabe dieses Programms?
```csv data.csv
title,FSK
Toy Story,0
Jumanji,12
Grumpier Old Men,6
Waiting to Exhale,12
Father of the Bride Part II,0
Heat,16
Sabrina,6
Tom and Huck,6
Sudden Death,16
GoldenEye,16
The Amerian President,6
Dracula: Dead and Loving It,12
Balto,0
Nixon,12
Cutthroat Island,12
```

```python
import pandas as pd

df = pd.read_csv('data.csv')
print(df['title'][9])
```
[[GoldenEye]]
**********************************************************************************************