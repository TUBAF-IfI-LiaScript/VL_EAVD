<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.2.2
language: de
narrator: Deutsch Female

comment:  Muster in Messreihen: ganze Spalte, Spalte mit Bedingung, Extremwerte, Blöcke und Zustände, dazu while und break — bis zur längsten Frostperiode auf dem Fichtelberg.

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
| **Inhalte:**             | `Aufsummieren, Mittelwert, Extremwertsuche, Zustand über Durchläufe, while, break`                                                                      |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_MusterInMessreihen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/04_MusterInMessreihen.md) |
| **Autoren**              | @author                                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie lang war 2024 die längste ununterbrochene Frostperiode auf dem Fichtelberg?_

**Fragen an die heutige Veranstaltung ...**

* Wie berechnet man einen Mittelwert, wenn Fehlwerte in den Daten stecken?
* Wie findet man den kältesten Tag — und nicht nur die tiefste Temperatur?
* Wie merkt sich ein Programm etwas über mehrere Schleifendurchläufe hinweg?
* Wann braucht man `while` statt `for`, und was kann dabei schiefgehen?
* Wie beendet man eine Schleife, sobald das Gesuchte gefunden ist?

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=4" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

--{{0}}--
Heute geht es um die Frage, was sich ein Programm merken muss. Letzte Woche war es eine Zahl, die mitzählt. Heute kommen eine Summe, ein Bestwert und schließlich ein Zustand dazu, der vom bisherigen Verlauf abhängt. Damit beantworten wir eine Frage, die mit einer einzigen Formel nicht zu lösen ist: Wie lange hielt der Frost am Stück an? Im Live Hacking sehen Sie dabei bewusst auch die Irrwege, denn genau so entsteht ein Programm.

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

Heute kommen weitere Muster hinzu. Alle folgen demselben Bauplan: **Etwas vor der Schleife anlegen, in der Schleife fortschreiben, danach nutzen.** Nur _was_ man sich merkt, ändert sich.

--{{0}}--
Die drei Stellen vor, in und nach der Schleife finden Sie heute in jedem Programm wieder. Achten Sie bei jedem neuen Beispiel darauf, was vor der Schleife angelegt wird: Daran erkennen Sie, was sich das Programm merkt.

## Muster & Analysen

Eine Messreihe ist eine Spalte der Tabelle, in Python eine Liste. Die Muster unterscheiden sich darin, **wie viel das Programm über die anderen Werte wissen muss**:

<!-- data-type="none" -->
| Muster                | Jeder Wert …                          | Das Programm merkt sich …           | Beispiel                    |
| :-------------------- | :------------------------------------ | :---------------------------------- | :-------------------------- |
| Ganze Spalte erfassen | zählt gleich viel                     | Summe und Anzahl                    | Wochenmittel                |
| Spalte mit Bedingung  | zählt nur, wenn er die Bedingung erfüllt | Summe und Anzahl der passenden Werte | Frosttage (VL 03), Mittel ohne Fehlwert |
| Extremwerte           | wird mit dem bisher besten verglichen | den Bestwert und wann er auftrat    | kältester Tag               |
| Blöcke und Zustände   | hängt von seinen Vorgängern ab        | die laufende Serie und die längste  | längste Frostperiode        |

Von oben nach unten muss sich das Programm mehr merken. Sortieren Sie die Spalte um, bleiben Summe, Mittel und Bestwert gleich. Die längste Frostperiode nicht: **Bei Blöcken zählt die Reihenfolge.**

--{{0}}--
In der Tabellenkalkulation hat jedes der ersten drei Muster eine fertige Formel: `SUMME` und `MITTELWERT`, `ZÄHLENWENN` und `MITTELWERTWENN`, `MIN` und `MAX`. Für Blöcke gibt es keine, dort braucht man eine Hilfsspalte, wie wir bei der längsten Frostperiode sehen werden. Wenn Sie später ein eigenes Programm schreiben, fragen Sie sich zuerst, welches Muster passt. Dann wissen Sie auch, was vor die Schleife gehört.

### Ganze Spalte erfassen

Der Mittelwert ist die Summe aller Werte, geteilt durch ihre Anzahl. Die Summe bauen wir Schritt für Schritt auf:

```` @BlocklyId(summe, runner=summe hideRunner height=520)
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

--{{0}}--
`summe` und `anzahl` wachsen bei jedem Durchlauf, erst nach der Schleife wird geteilt. Teilt man schon in der Schleife, bekommt man nach jedem Tag ein Zwischenergebnis, aber nicht das Mittel der Woche. `sum` und `len` rechnen genau dasselbe, nur ohne die Möglichkeit, einzelne Werte auszulassen.

### Spalte mit Bedingung

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

Das Ergebnis ist -2,2 °C, gemittelt über **sechs** Tage (Python zeigt `-2.1999999999999997`, warum, klärt „Typische Fehlvorstellung: Kommazahlen sind exakt“). Das sollte man dazuschreiben: Ein Mittelwert über sechs von sieben Tagen ist etwas anderes als ein Wochenmittel.

</details>

*******************************************************************************

--{{0}}--
Ein einziger Fehlwert unter Tausenden verschiebt das Mittel nur um einen Bruchteil eines Grades. Genau das macht ihn gefährlich: Das Ergebnis sieht plausibel aus.

--{{1}}--
Die Bedingung `wert != -999` steht vor beiden Zeilen, also wird ein Fehlwert weder addiert noch gezählt. Vergisst man sie bei `anzahl`, teilt man durch sieben statt durch sechs, und das Mittel wird zu warm.

### Extremwerte

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

print("Kältester Tag:", kaeltester_tag, "mit", kaeltester_wert, "°C")
```
@Pyodide.eval

Zwei Dinge sind neu:

* `minima[0]` ist der **erste** Wert der Liste. Python zählt ab 0 — genau wie bei den Zeichen in einem Text (Vorlesung 02).
* Wir merken uns **zwei** Dinge: den Wert und den Tag, an dem er auftrat. Beide werden **gemeinsam** aktualisiert.

> `min(minima)` liefert auch -14,1. Aber nicht, **wann** das war. Sobald die Frage "an welchem Tag?" lautet, brauchen Sie das Muster.

**Ausprobieren:** Warum startet man mit dem ersten Wert der Liste und nicht mit `kaeltester_wert = 0`? Probieren Sie es aus — und denken Sie dabei an den Juli.

--{{0}}--
Warum nicht mit 0 starten? Im Juli liegt das Minimum auf dem Fichtelberg nie unter 0 °C, 2024 war der tiefste Wert 4,5 °C. Mit dem Startwert 0 fände das Programm keinen kälteren Tag und meldete 0 °C an Tag 1, einen Wert, den es nie gab. Mit dem ersten Wert der Liste kann das nicht passieren.

### Blöcke und Zustände

Jetzt die Leitfrage: **Wie lang war die längste ununterbrochene Frostperiode?**

Das ist schwieriger als alles bisher. Ob ein Tag die Serie verlängert, hängt davon ab, **was vorher war**. Man muss sich einen **Zustand** merken. Fürs Geoingenieurwesen zählt genau das: Je länger der Frost am Stück, desto tiefer friert der Baugrund.

> **Live Hacking.** Diesen Abschnitt entwickeln wir in der Vorlesung gemeinsam — inklusive der Irrwege. Die drei Versuche unten dokumentieren, was dabei typischerweise passiert.

--{{0}}--
Ein Zustand ist das, was sich ein Programm vom bisherigen Verlauf merkt. Vergleichen Sie es mit einer Treppe: Wer mitzählt, wie viele Stufen er schon am Stück gestiegen ist, muss nach jedem Absatz wieder bei null anfangen.

#### Versuch 1

Naheliegend: Frosttage zählen, wie letzte Woche.

```python
# Tiefsttemperaturen vom 19. bis 28. März 2024
minima = [-0.9, 1.6, 1.0, -0.2, -3.7, -4.2, -2.8, -3.7, 1.4, -1.0]

serie = 0
for minimum in minima:
    if minimum < 0:
        serie = serie + 1

print("Längste Frostperiode:", serie)
```
@Pyodide.eval

Richtig wäre 5 (22. bis 26. März). Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt es aus?

                                     {{1}}
*******************************************************************************

Ergebnis: 7, also alle Frosttage. **Was fehlt?** Die Serie muss **abbrechen**, wenn ein frostfreier Tag kommt. Ohne das zählen wir einfach wieder alle Frosttage.

*******************************************************************************

#### Versuch 2

Also: bei frostfreiem Tag zurücksetzen.

```python
# Tiefsttemperaturen vom 19. bis 28. März 2024
minima = [-0.9, 1.6, 1.0, -0.2, -3.7, -4.2, -2.8, -3.7, 1.4, -1.0]

serie = 0
for minimum in minima:
    if minimum < 0:
        serie = serie + 1
    else:
        serie = 0

print("Längste Frostperiode:", serie)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Kommt jetzt 5 heraus?

                                     {{1}}
*******************************************************************************

Ergebnis: 1. `serie` ist die **laufende** Serie. Am Ende steht darin nur die letzte — und die ist einen Tag lang. Die längste Serie ist unterwegs verloren gegangen, weil wir sie nirgends aufbewahrt haben.

*******************************************************************************

--{{1}}--
`serie` ist ein Gedächtnis für den Augenblick, kein Gedächtnis für das Beste. Diesen Unterschied macht Versuch 3 sichtbar.

#### Versuch 3

Wir brauchen **zwei** Variablen: die laufende Serie und die längste bisher.

```python
# Tiefsttemperaturen vom 19. bis 28. März 2024
minima = [-0.9, 1.6, 1.0, -0.2, -3.7, -4.2, -2.8, -3.7, 1.4, -1.0]

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

                                     {{1}}
*******************************************************************************

**Im Kopf ausführen:** Füllen Sie `serie` und `laengste` aus, **bevor** Sie die Lösung aufklappen. Genau solche Ablaufprotokolle kommen in der Klausur vor.

<!-- data-type="none" -->
| Tag   | `minimum` | Frost? | `serie` | `laengste` |
| :---: | --------: | :----: | :-----: | :--------: |
| –     | –         | –      | 0       | 0          |
| 19.3. | -0.9      | ja     |         |            |
| 20.3. | 1.6       | nein   |         |            |
| 21.3. | 1.0       | nein   |         |            |
| 22.3. | -0.2      | ja     |         |            |
| 23.3. | -3.7      | ja     |         |            |
| 24.3. | -4.2      | ja     |         |            |
| 25.3. | -2.8      | ja     |         |            |
| 26.3. | -3.7      | ja     |         |            |
| 27.3. | 1.4       | nein   |         |            |
| 28.3. | -1.0      | ja     |         |            |

<details>
<summary>**Lösung**</summary>

<!-- data-type="none" -->
| Tag   | `minimum` | Frost? | `serie` | `laengste` |
| :---: | --------: | :----: | :-----: | :--------: |
| –     | –         | –      | 0       | 0          |
| 19.3. | -0.9      | ja     | 1       | 1          |
| 20.3. | 1.6       | nein   | 0       | 1          |
| 21.3. | 1.0       | nein   | 0       | 1          |
| 22.3. | -0.2      | ja     | 1       | 1          |
| 23.3. | -3.7      | ja     | 2       | 2          |
| 24.3. | -4.2      | ja     | 3       | 3          |
| 25.3. | -2.8      | ja     | 4       | 4          |
| 26.3. | -3.7      | ja     | 5       | 5          |
| 27.3. | 1.4       | nein   | 0       | 5          |
| 28.3. | -1.0      | ja     | 1       | 5          |

Achten Sie auf den 20. und den 27. März: `serie` fällt auf 0 zurück, `laengste` bleibt stehen. Am 22. März beginnt eine neue Serie, `laengste` wächst erst wieder, als sie die alte übertrifft.

</details>

> Das Muster „Extremwerte“ steckt hier **innerhalb** des Musters „Blöcke und Zustände“: `laengste` ist der größte Wert, den `serie` je angenommen hat.

*******************************************************************************

--{{1}}--
Die Tabelle ist ein Ablaufprotokoll wie in Vorlesung 03. Testen Sie solche Programme immer auch mit einer Serie ganz am Ende der Liste, dort verstecken sich gern Fehler. Das gilt besonders für Code, den eine KI vorschlägt: Ein häufiger Fehler ist, `laengste` nur im `else`-Zweig zu aktualisieren. Dann geht eine Serie am Listenende verloren, und die Testliste hier fände den Fehler nicht, weil ihre längste Serie in der Mitte liegt.

#### Die Antwort

Dasselbe Programm, alle 366 Tage — die Werte holen wir wie in Vorlesung 03 aus dem Repository, dem Ablageort der Kursdateien. Quelle: Deutscher Wetterdienst, Station 01358, Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

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

> [!NOTE] Nur im Browser
> Wie in Vorlesung 03: `open_url` funktioniert nur hier im Browser. Auf Ihrem Rechner lesen Sie Dateien ab Vorlesung 06 mit `open()`.

Lesen Sie das Ergebnis ab und tragen Sie es ein:

Die längste Frostperiode 2024 dauerte [[25]] Tage.
***
Vom 4. bis zum 28. Januar 2024 lag das Minimum auf dem Fichtelberg durchgehend unter 0 °C. Wann die Periode lag, verrät das Programm noch nicht — das ist Ihre Vorbereitungsaufgabe.
***

> **Und in der Tabellenkalkulation?** Möglich ist es — mit einer Hilfsspalte: in E2 `=WENN(C2<0; 1; 0)`, ab E3 `=WENN(C3<0; E2+1; 0)` nach unten gezogen, in einer freien Zelle (etwa G1) `=MAX(E:E)`. Das ist genau unser Algorithmus, nur in Zellen verteilt. Wer darauf kommt, hat algorithmisch gedacht.

--{{0}}--
Die Antwort: 25 Tage, vom 4. bis zum 28. Januar 2024. Die Liste mit zehn Werten war zum Verstehen da, die Datei mit 366 Werten zum Antworten. Am Programm hat sich dabei nichts geändert.

## `while`: Wiederholen, solange ...

Die `for`-Schleife läuft über eine bekannte Menge von Werten. `while` wiederholt dagegen, _solange eine Bedingung gilt_.

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

`round(mittel, 2)` rundet auf zwei Nachkommastellen — ohne sehen Sie Werte wie `8.009999999999994`. Warum das so ist, klärt der Abschnitt „Typische Fehlvorstellung: Kommazahlen sind exakt“ am Ende.

> **Der Unterschied zu `for`:** Wie oft die Schleife läuft, wissen wir vor dem Start nicht, denn genau das ist ja die Frage. Erst am Ende steht fest: 35 Durchläufe. `for` braucht die Menge der Werte vorher, `while` nur eine Bedingung zum Aufhören.

                                     {{1}}
*******************************************************************************

> [!WARNING] Achtung
> **Die Schleife muss enden.** Setzen Sie `trend = 0` oder `trend = -0.05` und überlegen Sie **vorher**, was passiert. (Führen Sie es besser nicht aus. Hängt das Programm, laden Sie die Seite neu; in Visual Studio Code beendet `Strg+C` das Programm.)
>
> Das ist die Eigenschaft **Terminierung** aus Vorlesung 01. Bei `for` über eine feste Liste ist sie garantiert, solange man die Liste in der Schleife nicht verlängert. Bei `while` müssen Sie selbst sicherstellen, dass die Bedingung irgendwann falsch wird.

*******************************************************************************

                                     {{2}}
*******************************************************************************

> [!CAUTION] Vorsicht
> Rechnerisch korrekt heißt nicht inhaltlich richtig. Ob ein Trend der letzten 50 Jahre für die nächsten 35 gilt, sagt dieses Programm nicht. Es sagt nur, was **unter dieser Annahme** folgt. Wer Ergebnisse weitergibt, muss die Annahme mitliefern.

*******************************************************************************

--{{0}}--
Die 0,05 °C pro Jahr stammen aus einer Ausgleichsgeraden durch die Jahresmittel von 1975 bis 2024, genau sind es 0,049 °C. Wer gut rechnet, kommt hier auch ohne Schleife aus: (8,0 − 6,26) / 0,05 = 34,8, also 35 Jahre. Das klappt aber nur, solange der Zuwachs jedes Jahr gleich ist. Beschleunigt sich die Erwärmung oder hängt der nächste Schritt vom Ergebnis des vorigen ab, gibt es keine einfache Formel mehr, die Schleife funktioniert dagegen unverändert. `while` prüft die Bedingung vor jedem Durchlauf. Ist sie schon zu Beginn falsch, läuft die Schleife kein einziges Mal.

--{{1}}--
Eine Endlosschleife erkennen Sie daran, dass nichts passiert und der Knopf nicht wieder frei wird. Das Programm meldet keinen Fehler, es rechnet einfach immer weiter.

--{{2}}--
Diese Warnung gilt für jede Hochrechnung, nicht nur für Temperaturen. Schreiben Sie zu einem solchen Ergebnis immer dazu, welche Annahme darin steckt.

### Üben: Fehler finden bei `while`

**⏱ 7 Minuten, zu zweit.** Alle sechs Programme sollen wie oben `Im Jahr 2059 …` ausgeben. Drei melden einen Fehler, drei laufen ohne Meldung falsch. Überlegen Sie bei diesen: Wie oft läuft die Schleife?

**1.**

```python
jahr = 2024
mittel = 6.26
trend = 0.05
while mittel > 8.0:
    jahr = jahr + 1
    mittel = mittel + trend
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

**2.**

```python
jahr = 2024
mittel = 6.26
trend = 0.05
While mittel < 8.0:
    jahr = jahr + 1
    mittel = mittel + trend
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

**3.**

```python
jahr = 2024
mittel = 6.26
trend = 0.05
while mittel < 8.0:
    mittel = mittel + trend
jahr = jahr + 1
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

**4.**

```python
jahr = 2024
mittel = 6,26
trend = 0.05
while mittel < 8.0:
    jahr = jahr + 1
    mittel = mittel + trend
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

**5.**

```python
jahr = 2024
mittel = 6.26
trend = 0.05
while mittel < 8.0
    jahr = jahr + 1
    mittel = mittel + trend
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```
@Pyodide.eval

**6.** Dieses Programm bitte **nicht** ausführen, nur im Kopf:

```python
jahr = 2024
mittel = 6.26
trend = 0.05
while mittel < 8.0:
    jahr = jahr + 1
    mittel + trend
print("Im Jahr", jahr, "läge das Mittel bei", round(mittel, 2), "°C")
```

<details>
<summary>**Lösung**</summary>

1. Ausgabe `Im Jahr 2024 … 6.26 °C`: `6.26 > 8.0` ist schon zu Beginn falsch, die Schleife läuft kein einziges Mal. Die Bedingung beschreibt, wann **weitergerechnet** wird, nicht das Ziel.
2. `SyntaxError: invalid syntax`, der Pfeil zeigt auf `mittel`: `While` mit großem W kennt Python nicht. Schlüsselwörter werden kleingeschrieben. Die Meldung zeigt dorthin, wo Python nicht mehr weiterkommt, der Fehler steht oft kurz davor.
3. Ausgabe `Im Jahr 2025 … 8.01 °C`: `jahr = jahr + 1` ist nicht eingerückt und läuft erst nach der Schleife, genau einmal.
4. `TypeError: '<' not supported between instances of 'tuple' and 'float'`: Mit Komma ist `6,26` keine Kommazahl, sondern ein Paar aus 6 und 26 (Vorlesung 02). Python schreibt Kommazahlen mit Punkt.
5. `SyntaxError: expected ':'`: Wie bei `if` und `for` endet die Kopfzeile von `while` mit einem Doppelpunkt.
6. Endlosschleife: `mittel + trend` rechnet, speichert aber nichts. `mittel` bleibt 6.26, die Bedingung bleibt wahr. In Vorlesung 03 kam bei demselben Fehler mit `for` einfach 0 heraus, bei `while` endet das Programm nie.

</details>

--{{0}}--
Die Syntaxfehler findet Python für Sie, gefährlich sind die anderen drei. Bei `while` gibt es zwei neue Arten, falsch zu liegen: Die Schleife läuft gar nicht, oder sie hört nie auf. Beides meldet Python nicht. Prüfen Sie deshalb vor dem Ausführen zwei Fragen: Ist die Bedingung am Anfang wahr? Und ändert sich in der Schleife etwas, das die Bedingung irgendwann falsch macht?

### `for` oder `while`?

Beide Schleifen wiederholen. Welche passt, hängt davon ab, **woher das Ende kommt**:

<!-- data-type="none" -->
| Aufgabe                                      | Schleife          | Das Ende kommt …                     |
| :------------------------------------------- | :---------------- | :----------------------------------- |
| jeden Wert einer Liste oder Datei ansehen    | `for`             | von selbst, nach dem letzten Wert    |
| den ersten Treffer in einer Liste suchen     | `for` mit `break` | beim Treffer (nächster Abschnitt)    |
| wiederholen, bis ein Ziel erreicht ist       | `while`           | erst, wenn die Bedingung falsch wird |

**Faustregel:** Gehen Sie Werte durch, nehmen Sie `for`. Hängt das Ende vom Rechnen ab, nehmen Sie `while`.

Auch die Suche nach dem ersten Frosttag geht mit `while`:

```python
minima = [3.2, 1.5, -0.4, 2.1, -1.8]

i = 0
while minima[i] >= 0:
    i = i + 1

print("Erster Frost an Tag", i + 1)
```
@Pyodide.eval

Ergebnis: Tag 3. Ändern Sie die Liste in `[3.2, 1.5, 2.1]`, also ohne Frosttag. Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was passiert?

[( )] Es gibt `Erster Frost an Tag 0` aus.
[(X)] Es bricht mit einer Fehlermeldung ab.
[( )] Die Schleife läuft endlos.
***
`IndexError: list index out of range`. Nach dem dritten Wert ist `i` gleich 3, und `minima[3]` gibt es nicht. Eine `for`-Schleife hört dagegen am Listenende von selbst auf. Wie man sie schon beim ersten Treffer anhält, zeigt der nächste Abschnitt mit `break`.
***

--{{0}}--
Jede `for`-Schleife lässt sich mit `while` und einem Zähler nachbauen, aber dann müssen Sie selbst ans Weiterzählen und ans Listenende denken. Vergessen Sie `i = i + 1`, läuft die Schleife endlos. Mit `for` kann Ihnen beides nicht passieren. Deshalb: `while` nur dann, wenn Sie vorher wirklich nicht wissen, wie oft wiederholt wird, wie bei der Frage nach dem Jahr mit 8 °C.

## Vorzeitig abbrechen: `break`

Manche Fragen suchen nicht den besten, sondern den **ersten** Wert. Sobald er gefunden ist, muss die Schleife nicht weiterlaufen: `break` beendet sie sofort.

```python
minima = [3.2, 1.5, -0.4, 2.1, -1.8]

tag = 0
for minimum in minima:
    tag = tag + 1
    if minimum < 0:
        print("Erster Frost an Tag", tag)
        break

print("Fertig.")
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Wie oft wird `tag = tag + 1` ausgeführt?

[( )] 2-mal
[(X)] 3-mal
[( )] 5-mal
***
Dreimal. An Tag 3 liegt das Minimum zum ersten Mal unter 0: Python gibt den Tag aus und verlässt mit `break` die Schleife. Tag 4 und 5 werden gar nicht mehr angesehen, `-1.8` löst also keine zweite Ausgabe aus. Weiter geht es **nach** der Schleife, mit `print("Fertig.")`.
***

--{{0}}--
`break` steht fast immer in einem `if`: Erst wenn die Bedingung erfüllt ist, soll die Schleife enden. Es verlässt nur die Schleife, in der es steht, nicht das ganze Programm. Was nach der Schleife kommt, läuft ganz normal weiter.

### Der erste Herbstfrost

_An welchem Tag gab es 2024 nach dem 30. Juni (Tag 182) den ersten Frost?_ Ein erster Versuch ohne `break`:

```python
from pyodide.http import open_url

url = ("https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/"
       "VL_EAVD/master/data/fichtelberg/2024_minimum.txt")
text = open_url(url).read()

tag = 0
herbstfrost = 0
for wert in text.split():
    tag = tag + 1
    if tag > 182 and float(wert) < 0:
        herbstfrost = tag

print("Erster Herbstfrost: Tag", herbstfrost)
```
@Pyodide.eval

Ist das wirklich der **erste** Herbstfrost? Legen Sie sich fest, **bevor** Sie das Programm ausführen.

                                     {{1}}
*******************************************************************************

Ergebnis: Tag 366, der 31. Dezember. Ohne `break` überschreibt jeder weitere Frosttag den gemerkten Wert. Am Ende steht der **letzte** darin, nicht der erste.

Ergänzen Sie unter `herbstfrost = tag` die Zeile `break` und führen Sie das Programm erneut aus. Dann hört die Suche beim ersten Treffer auf: Tag **285**, der 11. Oktober 2024.

*******************************************************************************

--{{1}}--
Auch dieser Fehler läuft ohne Meldung durch, das Ergebnis sieht sogar plausibel aus: Ende Dezember ist Frost ganz normal. Erst die Frage, ob das wirklich der erste Frost sein kann, deckt ihn auf. `herbstfrost = 0` vor der Schleife bedeutet „noch nichts gefunden“. Steht nach der Schleife immer noch 0, gab es keinen Treffer. Prüfen Sie das, bevor Sie das Ergebnis weiterverwenden. Mit `break` läuft die Schleife außerdem nur 285 statt 366 Mal, bei großen Dateien spart das Zeit.

## Typische Fehlvorstellung: Kommazahlen sind exakt

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
`False`. `0.1 + 0.2` ergibt `0.30000000000000004`, also knapp daneben. Warum, zeigt die nächste Folie.
***

### Warum Kommazahlen ungenau sind

Der Rechner speichert jede Zahl im **Zweiersystem**, mit einer festen Zahl von Stellen. Exakt geht das nur bei Brüchen aus Halben, Vierteln, Achteln und so weiter:

<!-- data-type="none" -->
| Dezimal | als Bruch | im Zweiersystem      |
| :-----: | :-------: | :------------------- |
| 0,5     | 1/2       | 0,1₂ (eine Hälfte)   |
| 0,25    | 1/4       | 0,01₂                |
| 0,75    | 3/4       | 0,11₂                |
| 0,1     | 1/10      | 0,000110011001100…₂  |

Bei 0,1 wiederholt sich `0011` endlos. Der Rechner schneidet nach etwa 16 Ziffern ab, so wie Sie 1/3 als 0,333 aufschreiben und dann 3 · 0,333 = 0,999 erhalten.

```python
print(0.5 + 0.25 == 0.75)   # Halbe und Viertel: exakt
print(0.1 * 3)              # Zehntel: abgeschnitten
print(0.1 * 3 == 0.3)
```
@Pyodide.eval

--{{0}}--
Der Fehler ist winzig: `0.1` steht im Speicher als 0,1000000000000000055…, die Abweichung liegt in der 18. Nachkommastelle. Für Temperaturen mit einer Nachkommastelle spielt das keine Rolle. Daher kam auch das `8.009999999999994` im `while`-Beispiel: 35-mal wurde `0.05` addiert, und `0.05` ist im Zweiersystem ebenfalls nicht exakt.

### Richtig mit Kommazahlen umgehen

Das betrifft jedes Programm, das mit Messwerten rechnet. Drei Regeln:

1. **Für die Ausgabe runden:** `round(wert, 2)`.
2. **Gerechnete Kommazahlen nicht mit `==` vergleichen.** Prüfen Sie stattdessen, ob der Abstand klein genug ist: `abs(a - b) < 0.001`. `abs` ist der Betrag, also der Wert ohne Vorzeichen.
3. **Werte direkt aus der Datei dürfen Sie vergleichen**, wie in Vorlesung 03 mit 0,0. Ungenau wird es erst beim Rechnen.

```python
summe = 0.1 + 0.2
print(summe == 0.3)               # exakte Gleichheit: scheitert
print(abs(summe - 0.3) < 0.001)   # Abstand klein genug?
print(round(summe, 2) == 0.3)     # beide Seiten gerundet
print(round(summe, 2))            # für die Ausgabe
```
@Pyodide.eval

> **Schon Erfahrung?** Setzen Sie im `while`-Beispiel `mittel = 6.25`. Rechnerisch erreicht das Mittel 2059 genau 8,0 °C, das Programm meldet aber 2060. Warum? Und wie bauen Sie die Bedingung um, damit 2059 herauskommt? Zweite Stufe: Was passiert mit `mittel = 6.26` und `while abs(mittel - 8.0) >= 0.001:`?

--{{0}}--
Wie klein ist „klein genug“? Das hängt von den Daten ab. Temperaturen stehen mit einer Nachkommastelle in der Datei, ein Abstand unter 0,001 ist also sicher gleich. Runden auf beiden Seiten ist die einfachere Variante, wenn klar ist, auf wie viele Stellen es ankommt. Warum Werte aus der Datei unproblematisch sind: Python macht aus dem Text `0.0` immer dieselbe Zahl im Speicher. Erst wenn gerechnet wird, können die winzigen Reste auftreten.

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

[( )] `7 3`
[(X)] `7 1`
[( )] `1 4`
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

## Ihre Begriffe für die Kurslandkarte

Die [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) wächst mit dem Semester. Wir schlagen die Begriffe vor, Sie ergänzen, was fehlt: Aus Ihren Datenwünschen in Vorlesung 00 sind so schon die ersten Anwendungen geworden. Nehmen Sie sich dafür jetzt fünf Minuten.

**Welches Wort von heute müssten Sie jemandem aus Ihrem Semester erklären können?**

[[___ ___ ___]]

**Welche Daten aus Ihrem Fach würden Sie gern so auswerten?**

[[___ ___ ___]]

## Nächste Woche

Bisher stand jede Messreihe von Hand im Programm. In der nächsten Vorlesung **sammeln** wir Ergebnisse in Listen — und beantworten:

> _Welches war der wärmste Tag jedes Jahres?_

**Zur Vorbereitung**

- [ ] Erweitern Sie Versuch 3 so, dass auch der **erste** Tag der längsten Frostperiode ausgegeben wird.
- [ ] **Mit `break`:** An welchem Tag lag das Minimum 2024 zum ersten Mal über 10 °C? Zur Kontrolle: Es ist Tag 98, der 7. April.
- [ ] Zählen Sie die **Frost-Tau-Wechsel** 2024 (Minimum unter 0 °C, Maximum über 0 °C). Sie kennen sie aus Vorlesung 03: Gefrierendes Wasser sprengt Gestein und Beton. Welche zweite Liste brauchen Sie dafür?

**Zur Übung**

Blatt 4 (Niedrigwasser der Elbe) steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 23.11.
