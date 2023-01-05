<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  1.0.5
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/liaTemplates/PyScript/main/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DataAnalysePandas.md)

# Daten- und Zeitreihenanalysen

| Parameter                | Kursinformationen                                                                                                                                                                              |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Veranstaltung:**       | `Prozedurale Programmierung / Einführung in die Informatik`                                                                                                                                    |
| **Semester**             | `Wintersemester 2022/23`                                                                                                                                                                       |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                                                              |
| **Inhalte:**             | `Datenanalyse mit dem Python Paket Pandas`                                                                                                                                                    |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DataAnalysePandas.md](https://github.com/TUBAF-IfI-LiaScript/VL_ProzeduraleProgrammierung/blob/master/11_DataAnalysePandas.md) |
| **Autoren**              | @author                                                                                                                                                                                        |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------


**Fragen an die heutige Veranstaltung ...**

* 

---------------------------------------------------------------------

## Motivation


## Pandas Grundlagen

```python
import pandas as pd
import numpy as np

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
print(s)
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)


## Visualisierung mit pandas 

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series(np.random.randn(5), index=["a", "b", "c", "d", "e"])
s.plot.bar()
plt.savefig('foo.png')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

## Beispiel der Woche
