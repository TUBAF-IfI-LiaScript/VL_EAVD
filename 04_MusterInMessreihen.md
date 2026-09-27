<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Muster in Messreihen: Aufsummieren, Extremwerte suchen, Zustand über Schleifendurchläufe merken, range, while und break — bis zur längsten Frostperiode auf dem Fichtelberg.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

@style
.flex-container {
    display: flex;
    flex-wrap: wrap;
    align-items: stretch;
    gap: 20px;
}

.flex-child {
    flex: 1;
    min-width: 260px;
}
@end

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_MusterInMessreihen.md)

# Muster in Messreihen

| Parameter                | Kursinformationen                                                                                                                                              |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                              |
| **Inhalte:**             | `Aufsummieren, Mittelwert, Extremwertsuche, Zustand über Durchläufe, range, while, break`                                                                      |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_MusterInMessreihen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_MusterInMessreihen.md) |
| **Autoren**              | @author                                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie lang war 2024 die längste ununterbrochene Frostperiode auf dem Fichtelberg?_

**Fragen an die heutige Veranstaltung ...**

* Wie berechnet man einen Mittelwert, wenn Fehlwerte in den Daten stecken?
* Wie findet man den kältesten Tag — und nicht nur die tiefste Temperatur?
* Wie merkt sich ein Programm etwas über mehrere Schleifendurchläufe hinweg?
* Wann braucht man eine `while`-Schleife, und was kann dabei schiefgehen?

--------------------------------------------------------------------------------

## Rückblick

    --{{0}}--
Letzte Woche haben Sie das Zählmuster kennengelernt: ein Zähler vor der Schleife, eine Bedingung in der Schleife, das Ergebnis danach. Heute lernen Sie drei weitere Muster, die nach demselben Prinzip funktionieren.

Letzte Woche: das **Zählmuster**.

```python
frosttage = 0                       # vor der Schleife: anlegen
for minimum in minima:
    if minimum < 0:
        frosttage = frosttage + 1   # in der Schleife: fortschreiben
print(frosttage)                    # nach der Schleife: nutzen
```

Heute kommen drei weitere Muster hinzu. Alle folgen demselben Bauplan: **Etwas vor der Schleife anlegen, in der Schleife fortschreiben, danach nutzen.** Nur _was_ man sich merkt, ändert sich.

<!-- data-type="none" -->
| Muster                   | Was man sich merkt                             | Beispiel heute                   |
| :----------------------- | :--------------------------------------------- | :------------------------------- |
| Zählen                   | eine Anzahl                                    | Frosttage (VL 03)                |
| Aufsummieren             | eine Summe                                     | Monatsmittel                     |
| Extremwert suchen        | den bisher besten Wert                         | kältester Tag                    |
| Zustand verfolgen        | eine laufende Serie und die bisher längste     | längste Frostperiode             |

## Muster 1: Aufsummieren

    --{{0}}--
Beginnen wir mit dem Mittelwert. Das war Ihre Vorbereitungsaufgabe. Ein Mittelwert ist eine Summe geteilt durch eine Anzahl, also brauchen wir beides.

Der Mittelwert ist die Summe aller Werte, geteilt durch ihre Anzahl. Die Summe bauen wir Schritt für Schritt auf:

```` @BlocklyId(summe, runner=summe hideRunner height=360)
# Tagesmittel vom 1. bis 7. Januar 2024
tagesmittel = [-1.2, -0.5, 1.6, -0.1, -0.5, -2.0, -8.9]

summe = 0
anzahl = 0

for wert in tagesmittel:
    summe = summe + wert
    anzahl = anzahl + 1

print("Mittelwert:", summe / anzahl)
````

```python
# runner: summe
```
@Pyodide.eval

> Python kennt dafür auch fertige Funktionen: `sum(tagesmittel)` und `len(tagesmittel)`. Warum dann selbst schreiben? Weil die fertigen Funktionen nicht wissen, was ein **Fehlwert** ist.

### Mittelwert mit Fehlwerten

                                     {{0-1}}
*******************************************************************************

Angenommen, am 3. Januar ist das Thermometer ausgefallen:

```python
tagesmittel = [-1.2, -0.5, -999, -0.1, -0.5, -2.0, -8.9]

print("Mittelwert:", sum(tagesmittel) / len(tagesmittel))
```
@Pyodide.eval

Ein Wochenmittel von rund -145 °C. Offensichtlich falsch — aber bei 47.595 Werten und einem einzigen `-999` wäre der Fehler viel kleiner und kaum zu bemerken.

*******************************************************************************

                                     {{1}}
*******************************************************************************

Korrigieren Sie das Programm so, dass Fehlwerte weder in die Summe noch in die Anzahl eingehen.

```python
tagesmittel = [-1.2, -0.5, -999, -0.1, -0.5, -2.0, -8.9]

summe = 0
anzahl = 0

for wert in tagesmittel:
    summe = summe + wert
    anzahl = anzahl + 1

print("Mittelwert:", summe / anzahl)
```
@Pyodide.eval

<details>
<summary>**Lösung**</summary>

```python
for wert in tagesmittel:
    if wert != -999:
        summe = summe + wert
        anzahl = anzahl + 1
```

Das Ergebnis ist -2,2 °C, gemittelt über **sechs** Tage. Das sollte man dazuschreiben: Ein Mittelwert über sechs von sieben Tagen ist etwas anderes als ein Wochenmittel.

</details>

*******************************************************************************

## Muster 2: Extremwert suchen

    --{{0}}--
In Vorlesung 02 haben Sie in Pseudocode beschrieben, wie man den wärmsten Tag findet. Jetzt setzen wir das in Python um, für den kältesten Tag.

Erinnern Sie sich an den Pseudocode aus Vorlesung 02? _"Merke dir den ersten Tag als bisher wärmsten ..."_ In Python, für den kältesten Tag:

```python
# Tiefsttemperaturen vom 1. bis 14. Januar 2024
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9,
          -14.1, -12.1, -11.1, -10.2, -8.3, -7.5, -6.5]

kaeltester_wert = minima[0]         # der erste Wert der Liste
kaeltester_tag = 1

tag = 0
for minimum in minima:
    tag = tag + 1
    if minimum < kaeltester_wert:
        kaeltester_wert = minimum
        kaeltester_tag = tag

print("Kältester Tag: Tag", kaeltester_tag, "im Januar mit", kaeltester_wert, "°C")
```
@Pyodide.eval

Zwei Dinge sind neu:

* `minima[0]` ist der **erste** Wert der Liste. Python zählt ab 0 — genau wie bei den Zeichen in einem Text (Vorlesung 02).
* Wir merken uns **zwei** Dinge: den Wert und den Tag, an dem er auftrat. Beide werden **gemeinsam** aktualisiert.

> `min(minima)` liefert auch -14,1. Aber nicht, **wann** das war. Sobald die Frage "an welchem Tag?" lautet, brauchen Sie das Muster.

**Ausprobieren:** Warum startet man mit dem ersten Wert der Liste und nicht mit `kaeltester_wert = 0`? Probieren Sie es aus — und denken Sie dabei an den Juli.

## Zahlenfolgen mit `range`

Manchmal will man nicht über eine Liste laufen, sondern über eine Folge von Zahlen — etwa über Jahre oder Tage:

```python
for jahr in range(2020, 2025):
    print(jahr)
```
@Pyodide.eval

<!-- data-type="none" -->
| Aufruf              | erzeugt                     |
| :------------------ | :-------------------------- |
| `range(5)`          | 0, 1, 2, 3, 4               |
| `range(2020, 2025)` | 2020, 2021, 2022, 2023, 2024 |
| `range(0, 366, 7)`  | 0, 7, 14, ..., 364          |

> Der Endwert ist **nicht** enthalten. `range(2020, 2025)` endet bei 2024. Das ist gewöhnungsbedürftig, hat aber einen Vorteil: `range(n)` liefert genau `n` Zahlen.

## Muster 3: Zustand verfolgen

    --{{0}}--
Jetzt kommt die Leitfrage. Die längste Frostperiode ist schwieriger als alles bisher, weil der Zähler nicht nur hochzählt, sondern auch wieder auf null fällt.

Jetzt die Leitfrage: **Wie lang war die längste ununterbrochene Frostperiode?**

Das ist schwieriger als alles bisher. Ob ein Tag die Serie verlängert, hängt davon ab, **was vorher war**. Man muss sich einen **Zustand** merken.

> **Live Hacking.** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam — inklusive der Irrwege. Die drei Versuche unten dokumentieren, was dabei typischerweise passiert.

### Versuch 1

                                     {{0-1}}
*******************************************************************************

Naheliegend: Frosttage zählen, wie letzte Woche.

```python
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, 0.3, -2.0]

serie = 0
for minimum in minima:
    if minimum < 0:
        serie = serie + 1

print("Längste Frostperiode:", serie)
```
@Pyodide.eval

Ergebnis: 6. Richtig wäre 3 (4. bis 6. Tag). **Was fehlt?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Serie muss **abbrechen**, wenn ein frostfreier Tag kommt. Ohne das zählen wir einfach wieder alle Frosttage.

*******************************************************************************

### Versuch 2

                                     {{0-1}}
*******************************************************************************

Also: bei frostfreiem Tag zurücksetzen.

```python
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, 0.3, -2.0]

serie = 0
for minimum in minima:
    if minimum < 0:
        serie = serie + 1
    else:
        serie = 0

print("Längste Frostperiode:", serie)
```
@Pyodide.eval

Ergebnis: 1. **Was ist jetzt passiert?**

*******************************************************************************

                                     {{1}}
*******************************************************************************

`serie` ist die **laufende** Serie. Am Ende steht darin nur die letzte — und die ist einen Tag lang. Die längste Serie ist unterwegs verloren gegangen, weil wir sie nirgends aufbewahrt haben.

*******************************************************************************

### Versuch 3

                                     {{0-1}}
*******************************************************************************

Wir brauchen **zwei** Variablen: die laufende Serie und die längste bisher.

```` @BlocklyId(serie, runner=serie hideRunner height=440)
minima = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, 0.3, -2.0]

serie = 0
laengste = 0

for minimum in minima:
    if minimum < 0:
        serie = serie + 1
        if serie > laengste:
            laengste = serie
    else:
        serie = 0

print("Längste Frostperiode:", laengste, "Tage")
````

```python
# runner: serie
```
@Pyodide.eval

*******************************************************************************

                                     {{1}}
*******************************************************************************

**Im Kopf ausführen:**

<!-- data-type="none" -->
| Tag | `minimum` | Frost? | `serie` | `laengste` |
| :-: | --------: | :----: | :-----: | :--------: |
| –   | –         | –      | 0       | 0          |
| 1   | -1.9      | ja     | 1       | 1          |
| 2   | -2.4      | ja     | 2       | 2          |
| 3   | 0.1       | nein   | 0       | 2          |
| 4   | -1.7      | ja     | 1       | 2          |
| 5   | -1.7      | ja     | 2       | 2          |
| 6   | -4.2      | ja     | 3       | 3          |
| 7   | 0.3       | nein   | 0       | 3          |
| 8   | -2.0      | ja     | 1       | 3          |

> Das Muster "Extremwert suchen" steckt hier **innerhalb** des Musters "Zustand verfolgen": `laengste` ist der größte Wert, den `serie` je angenommen hat.

*******************************************************************************

### Die Antwort

    --{{0}}--
Jetzt lassen wir dasselbe Programm über alle 366 Tage laufen.

Dasselbe Programm, alle 366 Tage:

```python
minima_2024 = [
     -1.9,  -2.4,   0.1,  -1.7,  -1.7,  -4.2, -11.9, -14.1, -12.1, -11.1, -10.2,  -8.3,
     -7.5,  -6.5,  -8.3,  -9.0,  -9.5,  -8.5, -10.6, -10.5,  -7.8,  -1.9,  -2.4,  -0.9,
     -3.1,  -3.3,  -4.4,  -4.4,   1.8,   2.3,  -2.4,  -3.3,  -3.8,   0.2,   1.4,   0.0,
     -1.0,  -4.1,  -3.0,   2.4,   2.6,   0.2,  -0.8,  -3.2,  -2.4,   3.5,   4.6,   1.1,
     -0.7,  -0.4,  -0.6,  -0.8,   0.4,  -3.0,  -3.2,  -1.8,  -1.8,  -1.5,  -1.7,  -2.1,
      2.6,   1.3,   1.2,   2.5,   0.1,  -4.7,  -5.2,  -5.4,  -3.4,  -0.5,   0.2,   0.1,
     -0.7,   2.4,   4.1,  -2.4,  -2.6,  -2.1,  -0.9,   1.6,   1.0,  -0.2,  -3.7,  -4.2,
     -2.8,  -3.7,   1.4,  -1.0,  -0.6,   9.7,   8.8,   0.5,   0.9,   0.4,   1.5,   3.1,
      7.8,  14.4,  14.0,   0.4,   0.4,   1.5,   5.0,   6.8,   6.0,  -2.7,  -3.2,  -3.1,
     -3.0,  -2.6,  -3.6,  -5.4,  -6.9,  -7.6,  -4.0,  -3.8,  -2.6,   3.1,   4.7,   5.4,
      8.4,   7.0,   6.3,   5.3,   4.9,   6.5,   6.4,   3.2,   3.3,   4.0,   5.4,   7.2,
      6.8,   6.7,   5.9,   5.5,   5.9,   5.7,   5.3,   6.6,   6.7,   9.2,   7.8,   6.9,
      8.3,   8.1,   8.3,   9.9,   4.9,   4.8,   7.9,   7.4,   9.4,   8.4,   5.6,   4.9,
      8.8,   7.1,   8.8,   9.0,   6.1,   6.5,   2.7,   2.8,   4.0,   5.5,   7.8,   6.6,
      9.9,  10.2,   7.2,   6.3,  11.4,   8.4,   9.9,   9.2,   9.4,  12.9,  14.3,  13.6,
     12.9,  10.4,   6.5,   5.9,   5.6,   4.5,   7.7,  11.1,   6.8,   7.9,  13.2,  14.3,
     13.5,  14.1,   9.5,   9.2,  13.5,  10.2,   9.6,  10.5,  13.3,  14.7,  15.8,  11.0,
     10.6,   9.1,   7.7,  11.8,  12.8,   8.9,   8.4,  10.0,  14.6,  14.0,   9.7,   9.0,
      9.9,   8.0,   9.6,  14.3,  11.6,  10.9,  10.8,  12.5,  12.2,  16.9,  15.2,  14.8,
     13.9,  14.7,  13.0,   8.7,  10.6,   7.1,   7.0,  11.7,  14.2,  10.0,   8.9,  10.3,
     13.2,  15.8,  14.1,  13.0,  14.6,  15.1,  15.1,  16.1,  13.9,  12.7,  12.8,  13.8,
      8.2,   6.6,   3.6,   2.3,   1.7,   2.7,   1.9,   3.8,   9.0,   9.4,   8.0,   7.0,
      7.3,  10.5,  10.4,   7.5,   7.5,   7.7,   4.5,   1.0,   0.9,   0.8,   4.3,   3.4,
      2.4,   3.1,   1.8,   1.2,   4.1,   8.0,   6.5,   3.8,  -0.2,  -0.1,   1.0,  -0.3,
     -0.4,   0.8,   2.5,   4.7,   7.0,   6.4,   8.5,   3.2,   2.4,   3.4,   8.9,   5.4,
      7.6,   7.2,   6.7,   5.9,   3.8,   2.6,  -1.9,  -2.0,   3.3,   5.7,  -1.7,  -1.8,
     -1.4,   3.1,   1.4,   1.0,  -3.9,  -3.2,  -2.9,  -1.8,  -3.4,  -3.6,  -3.9,  -3.3,
     -5.8,  -8.3,  -9.2,  -9.0,  -4.3,   6.3,   0.6,  -1.0,  -2.0,  -5.2,  -5.2,   1.2,
      1.2,  -3.6,  -5.0,  -6.2,  -3.7,  -3.8,  -2.7,  -4.6,  -4.2,  -6.2,  -4.0,  -3.1,
     -7.6,  -4.5,   0.1,  -0.8,  -0.8,  -2.5,  -5.0,  -5.5,  -4.9,  -6.0,  -5.2,  -5.7,
     -1.1,   4.4,   5.0,   0.2,  -0.6,  -1.9
]

serie = 0
laengste = 0
tag = 0
ende = 0

for minimum in minima_2024:
    tag = tag + 1
    if minimum < 0:
        serie = serie + 1
        if serie > laengste:
            laengste = serie
            ende = tag
    else:
        serie = 0

print("Längste Frostperiode:", laengste, "Tage, endete an Tag", ende, "des Jahres")
```
@Pyodide.eval

Die längste Frostperiode 2024 dauerte [[25]] Tage.
***
Vom 4. bis zum 28. Januar 2024 lag das Minimum auf dem Fichtelberg durchgehend unter 0 °C. Tag 28 des Jahres ist der 28. Januar.
***

> **Und in der Tabellenkalkulation?** Möglich ist es — mit einer Hilfsspalte `=WENN(C2<0; D1+1; 0)` und einem `MAX` darüber. Das ist genau unser Algorithmus, nur in Zellen verteilt. Wer darauf kommt, hat algorithmisch gedacht.

## `while`: Wiederholen, solange ...

    --{{0}}--
Die for-Schleife wiederholt für jeden Wert einer Liste. Manchmal weiß man aber vorher nicht, wie oft man wiederholen muss. Dann braucht man die while-Schleife.

Die `for`-Schleife läuft über eine bekannte Menge von Werten. Manchmal weiß man aber vorher nicht, **wie oft** wiederholt werden muss. Dann hilft `while`: _Wiederhole, solange die Bedingung gilt._

Seit 1975 ist das Jahresmittel auf dem Fichtelberg im Schnitt um etwa **0,05 °C pro Jahr** gestiegen. 2024 lag es bei 6,26 °C.

> _Wann würde der Fichtelberg bei gleichbleibendem Trend ein Jahresmittel von 8 °C erreichen?_

```python
jahr = 2024
mittel = 6.26
trend = 0.05          # °C pro Jahr

while mittel < 8.0:
    jahr = jahr + 1
    mittel = mittel + trend

print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

`round(mittel, 2)` rundet auf zwei Nachkommastellen — ohne sehen Sie Werte wie `8.009999999999994`. Warum das so ist, klären wir in einer späteren Vorlesung.

                                     {{1}}
*******************************************************************************

> [!WARNING]
> **Die Schleife muss enden.** Setzen Sie `trend = 0` oder `trend = -0.05` und überlegen Sie **vorher**, was passiert. (Führen Sie es besser nicht aus — oder seien Sie bereit, die Seite neu zu laden.)
>
> Das ist die Eigenschaft **Terminierung** aus Vorlesung 01. Bei `for` ist sie garantiert, weil die Liste endlich ist. Bei `while` müssen Sie selbst sicherstellen, dass die Bedingung irgendwann falsch wird.

*******************************************************************************

                                     {{2}}
*******************************************************************************

> [!CAUTION]
> Rechnerisch korrekt heißt nicht inhaltlich richtig. Ob ein Trend der letzten 50 Jahre für die nächsten 35 gilt, sagt dieses Programm nicht. Es sagt nur, was **unter dieser Annahme** folgt. Wer Ergebnisse weitergibt, muss die Annahme mitliefern.

*******************************************************************************

### Vorzeitig abbrechen: `break`

Manchmal will man eine Schleife verlassen, sobald man gefunden hat, was man sucht. **Wann gab es 2024 den ersten Frost im Herbst?**

```python
minima_2024 = [
     -1.9,  -2.4,   0.1,  -1.7,  -1.7,  -4.2, -11.9, -14.1, -12.1, -11.1, -10.2,  -8.3,
     -7.5,  -6.5,  -8.3,  -9.0,  -9.5,  -8.5, -10.6, -10.5,  -7.8,  -1.9,  -2.4,  -0.9,
     -3.1,  -3.3,  -4.4,  -4.4,   1.8,   2.3,  -2.4,  -3.3,  -3.8,   0.2,   1.4,   0.0,
     -1.0,  -4.1,  -3.0,   2.4,   2.6,   0.2,  -0.8,  -3.2,  -2.4,   3.5,   4.6,   1.1,
     -0.7,  -0.4,  -0.6,  -0.8,   0.4,  -3.0,  -3.2,  -1.8,  -1.8,  -1.5,  -1.7,  -2.1,
      2.6,   1.3,   1.2,   2.5,   0.1,  -4.7,  -5.2,  -5.4,  -3.4,  -0.5,   0.2,   0.1,
     -0.7,   2.4,   4.1,  -2.4,  -2.6,  -2.1,  -0.9,   1.6,   1.0,  -0.2,  -3.7,  -4.2,
     -2.8,  -3.7,   1.4,  -1.0,  -0.6,   9.7,   8.8,   0.5,   0.9,   0.4,   1.5,   3.1,
      7.8,  14.4,  14.0,   0.4,   0.4,   1.5,   5.0,   6.8,   6.0,  -2.7,  -3.2,  -3.1,
     -3.0,  -2.6,  -3.6,  -5.4,  -6.9,  -7.6,  -4.0,  -3.8,  -2.6,   3.1,   4.7,   5.4,
      8.4,   7.0,   6.3,   5.3,   4.9,   6.5,   6.4,   3.2,   3.3,   4.0,   5.4,   7.2,
      6.8,   6.7,   5.9,   5.5,   5.9,   5.7,   5.3,   6.6,   6.7,   9.2,   7.8,   6.9,
      8.3,   8.1,   8.3,   9.9,   4.9,   4.8,   7.9,   7.4,   9.4,   8.4,   5.6,   4.9,
      8.8,   7.1,   8.8,   9.0,   6.1,   6.5,   2.7,   2.8,   4.0,   5.5,   7.8,   6.6,
      9.9,  10.2,   7.2,   6.3,  11.4,   8.4,   9.9,   9.2,   9.4,  12.9,  14.3,  13.6,
     12.9,  10.4,   6.5,   5.9,   5.6,   4.5,   7.7,  11.1,   6.8,   7.9,  13.2,  14.3,
     13.5,  14.1,   9.5,   9.2,  13.5,  10.2,   9.6,  10.5,  13.3,  14.7,  15.8,  11.0,
     10.6,   9.1,   7.7,  11.8,  12.8,   8.9,   8.4,  10.0,  14.6,  14.0,   9.7,   9.0,
      9.9,   8.0,   9.6,  14.3,  11.6,  10.9,  10.8,  12.5,  12.2,  16.9,  15.2,  14.8,
     13.9,  14.7,  13.0,   8.7,  10.6,   7.1,   7.0,  11.7,  14.2,  10.0,   8.9,  10.3,
     13.2,  15.8,  14.1,  13.0,  14.6,  15.1,  15.1,  16.1,  13.9,  12.7,  12.8,  13.8,
      8.2,   6.6,   3.6,   2.3,   1.7,   2.7,   1.9,   3.8,   9.0,   9.4,   8.0,   7.0,
      7.3,  10.5,  10.4,   7.5,   7.5,   7.7,   4.5,   1.0,   0.9,   0.8,   4.3,   3.4,
      2.4,   3.1,   1.8,   1.2,   4.1,   8.0,   6.5,   3.8,  -0.2,  -0.1,   1.0,  -0.3,
     -0.4,   0.8,   2.5,   4.7,   7.0,   6.4,   8.5,   3.2,   2.4,   3.4,   8.9,   5.4,
      7.6,   7.2,   6.7,   5.9,   3.8,   2.6,  -1.9,  -2.0,   3.3,   5.7,  -1.7,  -1.8,
     -1.4,   3.1,   1.4,   1.0,  -3.9,  -3.2,  -2.9,  -1.8,  -3.4,  -3.6,  -3.9,  -3.3,
     -5.8,  -8.3,  -9.2,  -9.0,  -4.3,   6.3,   0.6,  -1.0,  -2.0,  -5.2,  -5.2,   1.2,
      1.2,  -3.6,  -5.0,  -6.2,  -3.7,  -3.8,  -2.7,  -4.6,  -4.2,  -6.2,  -4.0,  -3.1,
     -7.6,  -4.5,   0.1,  -0.8,  -0.8,  -2.5,  -5.0,  -5.5,  -4.9,  -6.0,  -5.2,  -5.7,
     -1.1,   4.4,   5.0,   0.2,  -0.6,  -1.9
]

tag = 0
for minimum in minima_2024:
    tag = tag + 1
    if tag > 182 and minimum < 0:        # ab Juli
        print("Erster Herbstfrost an Tag", tag)
        break

print("Suche beendet.")
```
@Pyodide.eval

> Tag 285 ist der 11. Oktober. `break` verlässt die **innerste** Schleife sofort; das Programm macht nach ihr weiter.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
werte = [4, 7, 2, 7, 1]
groesster = werte[0]
position = 0
i = 0
for w in werte:
    if w > groesster:
        groesster = w
        position = i
    i = i + 1
print(groesster, position)
```

[[7 1]]
[[?]] Beachten Sie: Die Bedingung ist `>`, nicht `>=`.
***
Die 7 an Position 1 wird übernommen. Die zweite 7 an Position 3 ist nicht **größer**, sondern gleich — sie ersetzt die erste deshalb nicht. Mit `>=` wäre die Ausgabe `7 3`.
***

**Welche Aussagen über die Serien-Suche (Versuch 3) stimmen?**

[[X]] `serie` muss bei einem frostfreien Tag auf 0 gesetzt werden.
[[X]] `laengste` darf bei einem frostfreien Tag **nicht** zurückgesetzt werden.
[[ ]] Man könnte auf `laengste` verzichten und am Ende `serie` ausgeben.
[[X]] Beide Variablen müssen vor der Schleife angelegt werden.

**Welche dieser Schleifen endet nicht?**

[( )] `for jahr in range(1890, 2026): print(jahr)`
[(X)] `x = 1` und dann `while x > 0: x = x + 1`
[( )] `x = 10` und dann `while x > 0: x = x - 3`
[( )] `for minimum in minima_2024: break`
***
`x` wird immer größer, `x > 0` bleibt für immer wahr. Bei `x = x - 3` wird `x` irgendwann -2, und die Schleife endet.
***

**Wie viele Zahlen erzeugt `range(1890, 2026)`?**

[[136]]
[[?]] Der Endwert ist nicht enthalten.
***
2026 − 1890 = 136 Zahlen: 1890, 1891, ..., 2025.
***

## Nächste Woche

Bisher stand jede Messreihe von Hand im Programm. In der nächsten Vorlesung **sammeln** wir Ergebnisse in Listen — und beantworten:

> _Welches war der wärmste Tag jedes Jahres?_

**Zur Vorbereitung**

- [ ] Erweitern Sie Versuch 3 so, dass auch der **erste** Tag der längsten Frostperiode ausgegeben wird.
- [ ] Finden Sie mit einer Schleife und `break` den **letzten** Frosttag im Frühjahr 2024. Warum ist das mit `break` schwieriger als der erste im Herbst?
- [ ] Zählen Sie die **Frost-Tau-Wechsel** 2024 (Minimum unter 0 °C, Maximum über 0 °C). Welche zweite Liste brauchen Sie dafür?
