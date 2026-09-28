<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Muster in Messreihen: Aufsummieren, Extremwerte suchen, Zustand über Schleifendurchläufe merken und while — bis zur längsten Frostperiode auf dem Fichtelberg.

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
| **Inhalte:**             | `Aufsummieren, Mittelwert, Extremwertsuche, Zustand über Durchläufe, while`                                                                      |
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

## Muster 3: Zustand verfolgen

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

```python
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

Dasselbe Programm, alle 366 Tage — die Werte holen wir wie in Vorlesung 03 aus dem Repository:

```python
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
       "VL_EAVD/master/data/fichtelberg/2024_minimum.txt")
text = open_url(url).read()

serie = 0
laengste = 0
for wert in text.split():
    if float(wert) < 0:
        serie = serie + 1
        if serie > laengste:
            laengste = serie
    else:
        serie = 0

print("Längste Frostperiode 2024:", laengste, "Tage")
```
@Pyodide.eval

> [!NOTE]
> Wie in Vorlesung 03: `open_url` funktioniert nur hier im Browser. Auf Ihrem Rechner lesen Sie Dateien ab Vorlesung 06 mit `open()`.

Lesen Sie das Ergebnis ab und tragen Sie es ein:

Die längste Frostperiode 2024 dauerte [[25]] Tage.
***
Vom 4. bis zum 28. Januar 2024 lag das Minimum auf dem Fichtelberg durchgehend unter 0 °C. Wann die Periode lag, verrät das Programm noch nicht — das ist Ihre Vorbereitungsaufgabe.
***

> **Und in der Tabellenkalkulation?** Möglich ist es — mit einer Hilfsspalte `=WENN(C2<0; D1+1; 0)` und einem `MAX` darüber. Das ist genau unser Algorithmus, nur in Zellen verteilt. Wer darauf kommt, hat algorithmisch gedacht.

## `while`: Wiederholen, solange ...

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

`round(mittel, 2)` rundet auf zwei Nachkommastellen — ohne sehen Sie Werte wie `8.009999999999994`. Warum das so ist, klärt der nächste Abschnitt.

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

### Typische Fehlvorstellung: Kommazahlen sind exakt

> **Typische Fehlvorstellung:** _„Der Rechner rechnet mit Kommazahlen genau so exakt wie mit ganzen Zahlen.“_

```python
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt die zweite Zeile aus?

[( )] `True`
[(X)] `False`
[( )] eine Fehlermeldung
***
Der Rechner speichert Kommazahlen im **Binärsystem**. Viele Zahlen, die im Dezimalsystem kurz sind, lassen sich dort nicht exakt darstellen — so wie 1/3 im Dezimalsystem nicht: 0,3333… bricht irgendwo ab. `0.1` ist intern also ein ganz klein wenig mehr oder weniger als 0,1, und diese winzigen Abweichungen summieren sich. Daher auch das `8.009999999999994` im `while`-Beispiel.

Zwei Konsequenzen für die Praxis:

* **Zur Ausgabe runden:** `round(wert, 2)`.
* **Kommazahlen nicht mit `==` vergleichen.** Stattdessen prüfen, ob der Abstand klein genug ist: `abs(a - b) < 0.001`.
***


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

[( )] `for minimum in minima: print(minimum)`
[(X)] `x = 1` und dann `while x > 0: x = x + 1`
[( )] `x = 10` und dann `while x > 0: x = x - 3`
***
`x` wird immer größer, `x > 0` bleibt für immer wahr. Bei `x = x - 3` wird `x` irgendwann -2, und die Schleife endet.
***

## Nächste Woche

Bisher stand jede Messreihe von Hand im Programm. In der nächsten Vorlesung **sammeln** wir Ergebnisse in Listen — und beantworten:

> _Welches war der wärmste Tag jedes Jahres?_

**Zur Vorbereitung**

- [ ] Erweitern Sie Versuch 3 so, dass auch der **erste** Tag der längsten Frostperiode ausgegeben wird.
- [ ] **Vorzeitig abbrechen:** Mit `break` verlässt man eine Schleife sofort. Finden Sie damit den **ersten Herbstfrost** 2024: den ersten Tag nach Tag 182 (30. Juni) mit einem Minimum unter 0 °C. Zur Kontrolle: Es ist Tag 285.
- [ ] Zählen Sie die **Frost-Tau-Wechsel** 2024 (Minimum unter 0 °C, Maximum über 0 °C). Welche zweite Liste brauchen Sie dafür?
