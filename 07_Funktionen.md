<!--

author:   Sebastian Zug & Bernhard Jung
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment:  Funktionen: Wiederkehrende Schritte benennen, Parameter und Rückgabewerte, lokale Variablen — das lange Skript aus Vorlesung 06 wird zerlegt.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md
          https://github.com/liascript/CodeRunner

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md)

# Funktionen

| Parameter                | Kursinformationen                                                                                                                              |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                |
| **Semester**             | @config.semester                                                                                                                               |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                              |
| **Inhalte:**             | `def, Parameter, return, None, mehrere Rückgabewerte, lokale Variablen, Funktionen testen`                                                     |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/07_Funktionen.md) |
| **Autoren**              | @author                                                                                                                                        |

--------------------------------------------------------------------------------

**Leitfrage:** _Wie vermeide ich, alles dreimal zu schreiben?_

**Fragen an die heutige Veranstaltung ...**

* Wie definiert und ruft man eine Funktion?
* Was ist der Unterschied zwischen `print` und `return`?
* Warum sind Variablen in einer Funktion "lokal"?
* Wie prüft man, ob eine Funktion richtig rechnet?

--------------------------------------------------------------------------------

## Rückblick

Das lange Skript aus Vorlesung 06 wertet zwei Stationen aus — mit zwei fast identischen Blöcken. Ihre Vorbereitungsaufgabe war, den 1948-Fehler zu beheben: Jahre mit zu wenigen Messungen sollen keinen Frostwert bekommen.

> **An wie vielen Stellen mussten Sie ändern?** An zwei — und bei einer dritten Station wären es drei. Jede Kopie ist eine Stelle, an der man eine Korrektur vergessen kann.

Heute geben wir wiederkehrenden Schritten einen **Namen** und schreiben sie nur noch **einmal**.

## Eine Funktion definieren

```` @BlocklyId(frostfunktion, runner=frostfunktion hideRunner height=300)
def ist_frosttag(minimum):
    return minimum != -999 and minimum < 0

print(ist_frosttag(-3.5))
print(ist_frosttag(2.1))
print(ist_frosttag(-999))
````

```python
# runner: frostfunktion
```
@Pyodide.eval

<!-- data-type="none" -->
| Teil                  | Bedeutung                                                      |
| :-------------------- | :------------------------------------------------------------- |
| `def`                 | Hier beginnt eine Funktionsdefinition.                         |
| `ist_frosttag`        | Der Name — er sagt, **was** die Funktion tut.                   |
| `(minimum)`           | Der **Parameter**: ein Platzhalter für den Wert beim Aufruf.    |
| `return ...`          | Das **Ergebnis**, das die Funktion an den Aufrufer zurückgibt.  |
| `ist_frosttag(-3.5)`  | Der **Aufruf**: `minimum` bekommt den Wert `-3.5`.              |

> Die Bedingung aus Vorlesung 03 steht jetzt an **einer** Stelle. Ändert sich die Definition eines Frosttags oder die Kodierung der Fehlwerte, ändern wir genau eine Zeile.

### Typische Fehlvorstellung: `def` führt die Funktion aus

> **Typische Fehlvorstellung:** _„Sobald Python die Zeile mit `def` erreicht, läuft die Funktion.“_

```python
def begruessung():
    print("Hallo Fichtelberg!")

print("Programmstart")
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[( )] `Hallo Fichtelberg!` und dann `Programmstart`
[(X)] nur `Programmstart`
[( )] eine Fehlermeldung, weil `begruessung` nie aufgerufen wird
***
`def` **definiert** die Funktion nur — wie ein Rezept, das man ins Kochbuch schreibt. Gekocht wird erst beim Aufruf `begruessung()`. Ohne Aufruf passiert nichts, und das ist auch kein Fehler.
***

## Parameter und Rückgabewert

Eine Funktion kann mehrere Parameter haben — und mit **beliebigen** Werten aufgerufen werden:

```python
def zaehle_unter(werte, grenze):
    anzahl = 0
    for wert in werte:
        if wert != -999 and wert < grenze:
            anzahl = anzahl + 1
    return anzahl

januar = [-1.9, -2.4, 0.1, -1.7, -1.7, -4.2, -11.9]
print("Frosttage:", zaehle_unter(januar, 0))
print("Strenger Frost:", zaehle_unter(januar, -10))
```
@Pyodide.eval

> Das ist das Zählmuster aus Vorlesung 03 — jetzt mit einem Namen und mit einstellbarer Grenze. Eine Funktion ist ein **Muster, das man wiederverwenden kann**.

### Typische Fehlvorstellung: `print` gibt etwas zurück

> **Typische Fehlvorstellung:** _„Was eine Funktion ausgibt, kann ich weiterverwenden.“_

```python
def mittelwert(werte):
    print(sum(werte) / len(werte))

m = mittelwert([2.5, -1.5, 0.5])
print("Ergebnis:", m)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was gibt die letzte Zeile aus?

[( )] `Ergebnis: 0.5`
[(X)] `Ergebnis: None`
[( )] eine Fehlermeldung, weil `mittelwert` nichts zurückgibt
***
`print` zeigt den Wert nur auf dem Bildschirm an — für Sie, nicht für das Programm. Zurückgegeben wird nur, was hinter `return` steht. Fehlt `return`, gibt die Funktion den besonderen Wert **`None`** zurück: "nichts".

Die Zahl `0.5` erscheint trotzdem auf dem Bildschirm — aus dem `print` **in** der Funktion. Das macht den Fehler so tückisch. Spätestens bei `m + 1` gibt es einen `TypeError`.

Richtig: `return sum(werte) / len(werte)`.
***

### Typische Fehlvorstellung: Namen müssen passen

> **Typische Fehlvorstellung:** _„Der Wert, den ich übergebe, muss genauso heißen wie der Parameter.“_

Die Funktion `zaehle_unter(werte, grenze)` von oben. Welche Aufrufe funktionieren?

[[X]] `zaehle_unter(januar, 0)`
[[X]] `zaehle_unter([-3.0, 1.0], -1)`
[[X]] `zaehle_unter(werte=januar, grenze=0)`
[[ ]] Nur Aufrufe, bei denen die übergebene Liste `werte` heißt.
***
Beim Aufruf wird der **Wert** übergeben, nicht der Name. In der Funktion heißt er dann `werte` — egal, wie er außerhalb hieß oder ob er überhaupt einen Namen hatte. Die dritte Variante nennt die Parameter ausdrücklich; das macht lange Aufrufe lesbarer.
***

## Lokale Variablen

Variablen, die **in** einer Funktion entstehen, existieren nur während des Aufrufs:

```python
def zaehle_frost(werte):
    anzahl = 0
    for wert in werte:
        if wert != -999 and wert < 0:
            anzahl = anzahl + 1
    return anzahl

ergebnis = zaehle_frost([-1.9, 0.1, -4.2])
print(ergebnis)
print(anzahl)
```
@Pyodide.eval

Die letzte Zeile scheitert mit `NameError`: `anzahl` ist eine **lokale** Variable der Funktion. Nach dem Aufruf ist sie verschwunden — nur der Rückgabewert kommt heraus.

> Das ist kein Mangel, sondern der eigentliche Nutzen: Eine Funktion kann intern beliebige Namen verwenden, ohne Variablen im restlichen Programm zu überschreiben. Man muss beim Lesen des Hauptprogramms nicht wissen, wie sie innen aussieht.

## Mehrere Rückgabewerte

Eine Zeile der DWD-Datei liefert uns drei Dinge: Jahr, Maximum, Minimum. Eine Funktion kann alle drei auf einmal zurückgeben:

```python
def zerlege_zeile(zeile):
    teile = zeile.split(";")
    return teile[1][0:4], float(teile[15]), float(teile[16])

zeile = "  1358;19101209;-999;-999;-999; 1; 2.7; 1;-999; 100; 7.0; 5.9; 863.90; 1.4; 89.00; 4.3; -2.8;-999;eor"
jahr, maximum, minimum = zerlege_zeile(zeile)
print(jahr, maximum, minimum)
```
@Pyodide.eval

Die drei Werte links vom `=` werden der Reihe nach mit den drei Rückgabewerten belegt. Die Reihenfolge muss stimmen — Python prüft nicht, ob `maximum` wirklich das Maximum bekommt.

## Live Hacking: Das lange Skript zerlegen

> **Live Hacking.** In der Vorlesung zerlegen wir das lange Skript aus Vorlesung 06 Schritt für Schritt. Das Ergebnis finden Sie unten; `main.py` ist eingeklappt.

Das Hauptprogramm am Ende der Datei ist jetzt fünf Zeilen lang und liest sich fast wie Pseudocode:

```python
for station, datei in [("fichtelberg", DATEI_FICHTELBERG),
                       ("freiberg", DATEI_FREIBERG)]:
    hoechst, frost, gemessen = auswerten(datei)
    schreibe_ergebnis(station + "_jahre.csv", hoechst, frost, gemessen)
    print(station, len(hoechst), "Jahre ausgewertet")
```

```python -hole_daten.py
import os
import urllib.request

basis = "https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/"
for datei in ["data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt",
              "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"]:
    os.makedirs(os.path.dirname(datei), exist_ok=True)
    urllib.request.urlretrieve(basis + datei, datei)
```
```python -main.py
DATEI_FICHTELBERG = "data/fichtelberg/produkt_klima_tag_18900801_20251231_01358.txt"
DATEI_FREIBERG = "data/freiberg/produkt_klima_tag_19450701_19930430_01441.txt"
MINDESTTAGE = 300          # weniger gemessene Tage: kein Frostwert


def zerlege_zeile(zeile):
    """Liefert Jahr, Tagesmaximum und Tagesminimum einer DWD-Zeile."""
    teile = zeile.split(";")
    return teile[1][0:4], float(teile[15]), float(teile[16])


def auswerten(datei):
    """Höchstwert, Frosttage und gemessene Tage pro Jahr."""
    hoechst = {}
    frost = {}
    gemessen = {}
    with open(datei) as f:
        f.readline()
        for zeile in f:
            jahr, maximum, minimum = zerlege_zeile(zeile)
            if jahr not in frost:
                frost[jahr] = 0
                gemessen[jahr] = 0
            if maximum != -999:
                if jahr not in hoechst or maximum > hoechst[jahr]:
                    hoechst[jahr] = maximum
            if minimum != -999:
                gemessen[jahr] = gemessen[jahr] + 1
                if minimum < 0:
                    frost[jahr] = frost[jahr] + 1
    return hoechst, frost, gemessen


def schreibe_ergebnis(name, hoechst, frost, gemessen):
    """Eine Zeile pro Jahr; ohne Frostwert, wenn zu wenig gemessen wurde."""
    with open(name, "w") as f:
        f.write("jahr;maximum;frosttage\n")
        for jahr in hoechst:
            if gemessen[jahr] >= MINDESTTAGE:
                f.write(jahr + ";" + str(hoechst[jahr]) + ";" + str(frost[jahr]) + "\n")
            else:
                f.write(jahr + ";" + str(hoechst[jahr]) + ";\n")


for station, datei in [("fichtelberg", DATEI_FICHTELBERG),
                       ("freiberg", DATEI_FREIBERG)]:
    hoechst, frost, gemessen = auswerten(datei)
    schreibe_ergebnis(station + "_jahre.csv", hoechst, frost, gemessen)
    print(station, len(hoechst), "Jahre ausgewertet")

with open("freiberg_jahre.csv") as f:
    zeilen = f.readlines()
print("Freiberg 1947-1949:", [z.strip() for z in zeilen[3:6]])
```
@LIA.eval(`["hole_daten.py", "main.py"]`, `none`, `sh -c "python3 hole_daten.py && python3 main.py"`)

**Was sich geändert hat**

<!-- data-type="none" -->
| Vorher (VL 06)                                   | Nachher                                                        |
| :----------------------------------------------- | :------------------------------------------------------------- |
| zwei kopierte Blöcke                              | eine Funktion `auswerten`, zweimal aufgerufen                   |
| 1948-Korrektur an zwei Stellen                    | eine Konstante `MINDESTTAGE`, eine Bedingung                    |
| dritte Station: 25 Zeilen kopieren                | dritte Station: ein Eintrag in der Liste                        |
| um das Programm zu verstehen, alles lesen         | Hauptprogramm lesen, Funktionen nur bei Bedarf                  |

> Die Texte in dreifachen Anführungszeichen direkt unter `def` heißen **Docstrings**. Sie beschreiben, was die Funktion tut — und erscheinen, wenn man `help(auswerten)` aufruft.

## Funktionen prüfen

Eine Funktion mit klarem Ein- und Ausgang lässt sich einzeln prüfen. `assert` bricht mit einer Fehlermeldung ab, wenn eine Bedingung **nicht** erfüllt ist:

```python
def ist_frosttag(minimum):
    return minimum != -999 and minimum < 0

assert ist_frosttag(-0.1) == True
assert ist_frosttag(0.0) == False
assert ist_frosttag(-999) == False
print("Alle Prüfungen bestanden.")
```
@Pyodide.eval

Ändern Sie die Funktion zu `return minimum < 0` und führen Sie die Prüfungen erneut aus. Welche schlägt fehl?

> Gute Prüffälle liegen **an den Grenzen**: genau 0,0 °C, knapp darunter, und der Fehlwert. Genau dort stecken die Fehler, die man beim Draufschauen übersieht.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
def verdopple(x):
    x = x * 2
    return x

x = 5
y = verdopple(x)
print(x, y)
```

[( )] `10 10`
[(X)] `5 10`
[( )] `5 5`
[( )] eine Fehlermeldung, weil `x` zweimal vorkommt
***
Das `x` in der Funktion ist ein **anderes** `x` als das im Hauptprogramm — ein lokaler Parameter, der beim Aufruf den Wert 5 bekommt. Die Funktion ändert nur ihr eigenes `x`. Das `x` draußen bleibt 5.
***

**Welche Aussagen stimmen?**

[[X]] Eine Funktion ohne `return` gibt `None` zurück.
[[ ]] `print` in einer Funktion gibt den Wert an den Aufrufer zurück.
[[X]] Nach `return` wird der Rest der Funktion nicht mehr ausgeführt.
[[X]] Eine Funktion muss definiert sein, bevor sie aufgerufen wird.
[[ ]] Lokale Variablen einer Funktion sind nach dem Aufruf im Hauptprogramm verfügbar.

**Ergänzen Sie die Funktion.**

Die Funktion soll den Mittelwert aller gültigen Werte zurückgeben — oder `None`, wenn es keinen gültigen Wert gibt.

```python
def mittel_ohne_fehlwerte(werte):
    summe = 0
    anzahl = 0
    for wert in werte:
        if wert != -999:
            summe = summe + wert
            anzahl = anzahl + 1
    # ... Ihre Ergänzung
```

<details>
<summary>**Lösung**</summary>

```python
    if anzahl == 0:
        return None
    return summe / anzahl
```

Ohne die Prüfung gäbe es bei einem Jahr ohne Messwerte eine Division durch null — genau der Fall Freiberg 1948.

</details>

## Nächste Woche

Nächste Woche ist **Demonstration**: Ein Mikrocontroller misst, MicroPython steuert ihn. Bis hierher kamen alle Daten fertig aus einer Datei — dann sehen Sie, wie sie entstehen.

Im Januar geht es mit Vorlesung 09 weiter: Die Funktionen von heute wandern in eine eigene Datei, ein **Modul**.

**Zur Vorbereitung**

- [ ] Fügen Sie dem Programm aus dem Live Hacking eine dritte Station hinzu: Chemnitz (`data/chemnitz/produkt_klima_tag_18820101_20251231_00853.txt`). Wie viele Zeilen ändern Sie?
- [ ] Schreiben Sie eine Funktion `laengste_frostperiode(minima)` mit dem Muster aus Vorlesung 04 und prüfen Sie sie mit `assert`.
- [ ] Schreiben Sie für `zaehle_unter` drei `assert`-Prüfungen, darunter eine mit einer leeren Liste.
