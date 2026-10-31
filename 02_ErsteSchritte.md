<!--

author:   Sebastian Zug & Bernhard Jung & Claude Code (Opus 5.5)
email:    sebastian.zug@informatik.tu-freiberg.de & bernhard.jung@informatik.tu-freiberg.de
version:  2.3.0
language: de
narrator: Deutsch Female

comment:  Erste Schritte in Python: Ausgabe, Rechnen, Variablen, Datentypen und das Lesen von Fehlermeldungen — am Beispiel der Fichtelberg-Messreihe.

logo:     ./images/Readme/Wetterstation.png

import:   https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md
          https://raw.githubusercontent.com/jh-488/lia-blockly/main/README.md
          https://raw.githubusercontent.com/LiaTemplates/Pyodide/master/README.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md)

# Erste Schritte in Python

| Parameter                | Kursinformationen                                                                                                                                  |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Veranstaltung:**       | @config.lecture                                                                                                                                    |
| **Semester**             | @config.semester                                                                                                                                   |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                  |
| **Inhalte:**             | `Uhrzeiten in der Tabellenkalkulation, Von der Frage zum Pseudocode, Interpreter, Ausgabe, Rechnen, Variablen, Datentypen, Typumwandlung, Fehlermeldungen`                                                             |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/02_ErsteSchritte.md) |
| **Autoren**              | @author                                                                                                                                            |

--------------------------------------------------------------------------------

**Leitfrage:** _Was macht der Rechner mit „-1,9“ aus unserer Datei?_

**Fragen an die heutige Veranstaltung ...**

* Wie wird aus einem Programmtext etwas, das der Rechner ausführt?
* Wie speichert ein Programm Werte, und wie rechnet es damit?
* Warum ist `"6,26"` etwas anderes als `6.26`?
* Was sagt mir eine Fehlermeldung — und wie gehe ich damit um?

> **Zum Nacharbeiten: die Ansicht „Lehrbuch“.** Im Hörsaal zeigen die Folien nur die Kernbotschaften. Die Erklärungen dazu stehen im Lehrbuch: oben rechts auf das Symbol mit den Schiebereglern klicken und „Lehrbuch“ wählen.

<!-- kurslandkarte:knopf-start -->

<a href="https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/#termin=2" style="display: inline-block; padding: 0.5em 1.1em; background-color: #00718A; color: #ffffff; text-decoration: none; font-family: 'IBM Plex Sans', 'Segoe UI', system-ui, sans-serif; font-weight: 600;">🗺️ Diese Vorlesung in der Kurslandkarte →</a>

<!-- kurslandkarte:knopf-ende -->

--{{0}}--
Heute schreiben Sie Ihre ersten Zeilen Python. Wir beginnen mit der Tabellenkalkulation und dem Pseudocode, damit der Übergang kein Sprung wird. Am Ende nehmen wir eine echte Zeile aus unserer Datei auseinander. Sie werden dabei Fehlermeldungen sehen, manche mit Absicht. Das ist kein Zeichen dafür, dass etwas schiefläuft, sondern Teil der Arbeit.

> Alle Beispiele laufen heute direkt im Browser. Sie müssen nichts installieren.

--------------------------------------------------------------------------------

## Rückblick

Ihre Hausaufgabe: _Den wärmsten Tag in `fichtelberg_2024.csv` finden, ohne `MAX` zu benutzen._ Eine mögliche Lösung:

``` text
Merke dir den ersten Tag als "bisher wärmster".
Für jeden weiteren Tag:
    Wenn sein Maximum höher ist als das des bisher wärmsten:
        Merke dir diesen Tag als "bisher wärmster".
Gib den bisher wärmsten Tag aus.
```

> Darin stecken schon fast alle Zutaten eines Programms: Man muss sich etwas **merken** (heute), etwas **vergleichen** und etwas **wiederholen** (nächste Woche). Heute kümmern wir uns um das Merken und Rechnen.

--{{0}}--
Ihre Formulierung darf anders aussehen, wichtig ist der Ablauf. `MAX` macht es im Grunde genauso: Es geht alle Werte durch und merkt sich den bisher größten. Sie haben also von Hand aufgeschrieben, was die Funktion Ihnen sonst abnimmt.

### Rückblick: Uhrzeiten in der Tabellenkalkulation

In Aufgabe 2 war der Zeitstempel die größte Hürde. Für die Tabellenkalkulation ist eine Uhrzeit eine **Zahl**, nämlich der Bruchteil eines Tages: 12:00 Uhr ist 0,5. Erst als Zahl lässt sie sich vergleichen.

<!-- data-type="none" -->
| Schritt                     | Formel (in A2 steht der Text `2026-10-19T16:15:27`) | Ergebnis                           |
| :-------------------------- | :-------------------------------------------------- | :--------------------------------- |
| 1. Uhrzeit abspalten        | `=TEIL(A2;12;8)` in C2                              | `16:15:27`, aber noch Text         |
| 2. in eine Uhrzeit umwandeln | `=ZEITWERT(C2)` in D2                              | `0,6774`, als Uhrzeit formatiert `16:15:27` |
| 3. vergleichen              | `=D2>=ZEIT(16;15;0)`                                | `WAHR`                             |

Alle Durchgänge `rein` ab 16:15 auf einmal: `=ZÄHLENWENNS(B2:B32;"rein";D2:D32;">="&ZEIT(16;15;0))` ergibt **8**.

> Hat LibreOffice den Zeitstempel beim Öffnen schon als Datum mit Uhrzeit erkannt (rechtsbündig), entfallen Schritt 1 und 2. Die Uhrzeit allein liefert dann `=REST(A2;1)`.

--{{0}}--
Intern zählt die Tabellenkalkulation die Tage seit Ende 1899. Der 19. Oktober 2026 ist Tag 46.314, und 16:15:27 Uhr ist der Bruchteil 0,6774 dieses Tages; zusammen ergibt das 46.314,6774. REST(A2;1) teilt durch 1 und behält nur den Rest, also den Tagesanteil. TEIL(A2;12;8) zählt dagegen Zeichen: ab dem zwölften Zeichen acht Stück. Das funktioniert nur, solange alle Zeitstempel genau gleich aufgebaut sind.

### Typische Fehlvorstellung: Sieht aus wie eine Uhrzeit, ist eine Uhrzeit

> **Typische Fehlvorstellung:** _„Was wie eine Uhrzeit aussieht, kann ich auch wie eine Uhrzeit vergleichen.“_

Schritt 2 lässt sich doch sparen? In Spalte C steht schon `16:15:27`:

``` text
=C2>=ZEIT(16;15;0)
```

Legen Sie sich fest, **bevor** Sie die Auflösung ansehen: Für wie viele der 31 Zeilen liefert diese Formel `WAHR`?

[( )] 12, alle Durchgänge ab 16:15
[( )] 8, nur die mit `rein`
[(X)] 31, alle
[( )] keine, sondern eine Fehlermeldung
***
Für alle 31. `16:15:27` in Spalte C ist **Text**, und beim Vergleich stuft die Tabellenkalkulation Text immer höher ein als jede Zahl. Das Ergebnis ist durchgehend `WAHR`, ohne Warnung. Richtig wären 12.

Dasselbe passiert, wenn man ein Datum mit Uhrzeit direkt mit `ZEIT(16;15;0)` vergleicht: 46.314,67 ist immer größer als 0,68.
***

> Text ist nicht Zahl, auch wenn er genauso aussieht. Genau darum geht es heute auch in Python.

--{{0}}--
LibreOffice und Excel verhalten sich hier gleich: Text gilt beim Vergleich als größer als jede Zahl. Eine Fehlermeldung wäre hilfreicher, kommt aber nicht. Ein Hinweis darauf ist die Ausrichtung in der Zelle: Text steht links, Zahlen und Uhrzeiten stehen rechts. Im Abschnitt „Datentypen“ sehen Sie, dass Python strenger ist: Text plus Zahl bricht dort sofort mit einer Fehlermeldung ab.

## Von der Frage zum Pseudocode

Jede Auswertung beginnt mit einer Frage an einen Datensatz. Vier Fragen an sich selbst führen von dort zum Pseudocode:

<!-- data-type="none" -->
| Fragen Sie sich ...                    | im Beispiel                                        |
| :------------------------------------- | :------------------------------------------------- |
| 1. Was steht in **einer** Zeile?       | eine Person: Nachname, Vorname, Studiengang        |
| 2. Was muss ich mir **merken**?        | eine Anzahl, zu Beginn 0                           |
| 3. Was tue ich mit **jeder** Zeile?    | Beginnt der Nachname mit „A“, die Anzahl erhöhen   |
| 4. Was gebe ich am **Ende** aus?       | die Anzahl                                         |

**Beispiel:** _Wie viele Personen auf der Teilnehmerliste haben einen Nachnamen, der mit A beginnt?_

``` text
Setze anzahl auf 0.
Für jede Zeile der Teilnehmerliste:
    Wenn der Nachname mit "A" beginnt:
        Erhöhe anzahl um 1.
Gib anzahl aus.
```

> Frage 2 ist die wichtigste: Was man sich merken muss, wird heute zur **Variablen**.

--{{0}}--
Die vier Fragen sind ein Rezept für den Anfang, kein Gesetz. Frage 1 klingt banal, entscheidet aber, worüber die Wiederholung läuft: über Personen, Tage, Messpunkte oder Buchungen. Frage 3 enthält fast immer eine Bedingung, und die muss man ganz genau formulieren. Wie genau, zeigt die nächste Folie.

### Was heißt „beginnt mit A“?

Auf der Teilnehmerliste stehen unter anderem diese vier Nachnamen. Legen Sie sich fest, **bevor** Sie die Auflösung ansehen: Welche zählt der Algorithmus, wenn er **genau** das tut, was dasteht?

[[X]] Ahrens
[[ ]] Åberg
[[ ]] von Arnim
[[ ]] auf der Heide
***
Nur „Ahrens“. Der Rechner vergleicht Zeichen, keine Absichten: Å ist ein anderes Zeichen als A, „auf der Heide“ beginnt mit einem kleinen a und „von Arnim“ mit einem v.

Ob das so gemeint war, entscheiden Sie, und zwar in der Bedingung. Sollen alle vier zählen, muss dort etwa stehen: „Wenn der Nachname ohne Namenszusatz wie *von* oder *auf der* mit A, a oder Å beginnt“.
***

> Eindeutig heißt nicht: so gemeint. Der Algorithmus beantwortet genau die Frage, die in ihm steht.

--{{0}}--
Dasselbe Problem kennen Sie aus Vorlesung 01: Der Algorithmus mit der verrutschten Zeile war eindeutig und ausführbar, er beantwortete nur eine andere Frage als gemeint. Bei echten Daten stecken solche Fälle überall, etwa Groß- und Kleinschreibung, Leerzeichen am Anfang oder Sonderzeichen. Deshalb lohnt es sich, vor dem Programmieren ein paar echte Zeilen anzusehen.

### Üben: Fragen aus Ihrem Fach

**⏱ 5 Minuten, zu zweit.** Wählen Sie eine Frage, am besten aus Ihrem Fach. Gehen Sie die vier Fragen durch und schreiben Sie Pseudocode.

<!-- data-type="none" -->
| Fach                      | Eine Zeile des Datensatzes                                  | Frage                                                         |
| :------------------------ | :---------------------------------------------------------- | :------------------------------------------------------------ |
| Umwelt                    | Datum; Feinstaub im Tagesmittel in µg/m³                    | Hielt die Messstation den Grenzwert ein? Über 50 µg/m³ ist an höchstens 35 Tagen im Jahr erlaubt. |
| Werkstoffe                | Messpunkt eines Zugversuchs: Dehnung in %; Kraft in kN      | Bei welcher Dehnung trug die Probe die größte Kraft?          |
| Wirtschaft                | Datum; Filiale; Betrag in €                                 | Welchen Umsatz machte die Filiale Freiberg im März?           |
| Energie                   | Uhrzeit; Leistung in kW, alle 15 Minuten gemessen           | Wie viel Energie in kWh hat die Werkhalle an diesem Tag verbraucht? |
| _Schon Erfahrung?_        | Uhrzeit; Ereignis `start` oder `stopp` einer Maschine       | Wie lange lief die Maschine insgesamt?                        |

> Beim **Zugversuch** wird eine Materialprobe langsam auseinandergezogen, bis sie reißt. Die **Dehnung** sagt, um wie viel Prozent sie dabei länger geworden ist.

--{{0}}--
Jede Frage braucht ein anderes Muster: zählen und danach entscheiden, den größten Wert suchen, mit zwei Bedingungen aufsummieren, gewichtet aufsummieren und sich einen Zustand merken. In Vorlesung 04 bekommen diese Muster eigene Namen. Feinstaub sind winzige Staubteilchen in der Luft, die man einatmet. Für sie gilt in der EU tatsächlich: Das Tagesmittel darf höchstens an 35 Tagen im Jahr über 50 Mikrogramm pro Kubikmeter liegen.

### Lösungsvorschläge

Es gibt nicht die eine richtige Lösung. Prüfen Sie Ihre, indem Sie sie mit drei, vier erfundenen Zeilen von Hand ausführen.

<details>
<summary>**Umwelt: Grenzwert für Feinstaub**</summary>

``` text
Setze tage_darueber auf 0.
Für jede Zeile:
    Wenn der Feinstaub größer als 50 ist:
        Erhöhe tage_darueber um 1.
Wenn tage_darueber größer als 35 ist:
    Gib "Grenzwert überschritten" aus.
Sonst:
    Gib "Grenzwert eingehalten" aus.
```

Die Antwort ist keine Zahl, sondern ja oder nein: Nach der Wiederholung kommt noch eine Verzweigung.

</details>

<details>
<summary>**Werkstoffe: größte Kraft im Zugversuch**</summary>

``` text
Merke dir die erste Zeile als "bisher stärkste".
Für jede weitere Zeile:
    Wenn ihre Kraft größer ist als die der bisher stärksten:
        Merke dir diese Zeile als "bisher stärkste".
Gib die Dehnung der bisher stärksten Zeile aus.
```

Dasselbe Muster wie der wärmste Tag aus dem Rückblick, nur mit anderen Spalten.

</details>

<details>
<summary>**Wirtschaft: Umsatz einer Filiale**</summary>

``` text
Setze summe auf 0.
Für jede Zeile:
    Wenn die Filiale "Freiberg" ist und das Datum im März liegt:
        Addiere den Betrag zu summe.
Gib summe aus.
```

Gemerkt wird diesmal eine Summe statt einer Anzahl.

</details>

<details>
<summary>**Energie: Verbrauch an einem Tag**</summary>

``` text
Setze energie auf 0.
Für jede Zeile:
    Addiere die Leistung mal 0,25 zu energie.
Gib energie aus.
```

Jeder Messwert gilt für 15 Minuten, also 0,25 Stunden. Leistung in kW mal Zeit in Stunden ergibt Energie in kWh.

</details>

<details>
<summary>**Schon Erfahrung? Laufzeit einer Maschine**</summary>

``` text
Setze laufzeit auf 0.
Für jede Zeile:
    Wenn das Ereignis "start" ist:
        Merke dir die Uhrzeit als startzeit.
    Wenn das Ereignis "stopp" ist:
        Addiere (Uhrzeit minus startzeit) zu laufzeit.
Gib laufzeit aus.
```

Und wenn das Protokoll mit `stopp` beginnt oder zweimal hintereinander `start` steht? Solche Fälle muss Ihr Algorithmus entscheiden, wie die Zeilen mit `unklar` beim Personenzähler.

</details>

--{{0}}--
Achten Sie beim Vergleichen weniger auf die Formulierung als auf zwei Dinge: Haben Sie sich das Richtige gemerkt, also eine Anzahl, eine Summe oder eine ganze Zeile? Und steht jeder Schritt an der richtigen Stelle, innerhalb oder außerhalb der Wiederholung? Genau daran scheiterte letzte Woche die verrutschte Zeile.

## Vom Text zur Ausführung

Ein Prozessor versteht nur **Maschinenbefehle**. Zwischen Ihrem Programmtext und dem Prozessor steht deshalb ein Übersetzer, bei Python der **Interpreter**:

``` ascii
  +-----------------+        +------------------+        +--------------+
  | Programmtext    |        | Python-          |        |              |
  | frost.py        |------->| Interpreter      |------->|  Prozessor   |
  |                 |        | liest Zeile für  |        |              |
  | minimum = -3.5  |        | Zeile, prüft,    |        |              |
  | print(minimum)  |        | führt aus        |        |              |
  +-----------------+        +------------------+        +--------------+
                                      |
                                      v
                             Ausgabe oder Fehlermeldung
```

Zwei Dinge sollten Sie sich merken:

1. Der Interpreter arbeitet **von oben nach unten**, eine Anweisung nach der anderen.
2. Stößt er auf etwas, das er nicht versteht, **bricht er ab** und sagt Ihnen, wo und warum.

--{{0}}--
Maschinenbefehle sind sehr einfache Anweisungen wie „lade Wert“, „addiere“ oder „springe“, gespeichert als Bitmuster. Von Hand schreibt das heute kaum noch jemand. Der Interpreter ist selbst ein Programm. Auf Ihrem Rechner haben Sie ihn in der ersten Übung installiert, hier im Browser läuft eine eigene Fassung davon, sie heißt Pyodide.

### Warum Python?

> Python ist nicht die schnellste Sprache und nicht die einzige. Für unsere Zwecke — Daten einlesen, aufbereiten, auswerten, darstellen — ist sie aber die naheliegendste.

--{{0}}--
Python ist gut lesbar: Programme sehen fast aus wie der Pseudocode von letzter Woche. In der Wissenschaft ist es so verbreitet, dass es für fast jede Fachfrage eine fertige Bibliothek gibt. Es reicht vom Mikrocontroller in Vorlesung 08 bis zur Datenanalyse mit pandas, und es kostet nichts und läuft auf jedem Rechner.

## Die erste Anweisung

Die Anweisung `print` gibt etwas aus. Was ausgegeben werden soll, steht in runden Klammern. Text steht in Anführungszeichen.

> Nutzen Sie die Schaltflächen über dem Editor, um zwischen **Blöcken** und **Text** zu wechseln. Beide zeigen dasselbe Programm.

```` @BlocklyId(hallo, runner=hallo hideRunner height=240)
print("Hallo Fichtelberg!")
print("Höhe der Station in Metern:")
print(1213)
````

```python
# runner: hallo
```
@Pyodide.eval

**Ausprobieren**

* Ergänzen Sie eine Zeile, die das Jahr des Messbeginns (1890) ausgibt.
* Was passiert, wenn Sie bei `"Hallo Fichtelberg!"` ein Anführungszeichen weglassen?
* `print` kann mehrere Dinge auf einmal ausgeben, getrennt durch Kommas: `print("Höhe:", 1213, "m")`

--{{0}}--
`print` bringt Python schon mit. Die Anführungszeichen sagen Python, dass Text folgt, den es nicht deuten soll; die Zahl `1213` steht deshalb ohne. Blöcke nutzen wir nur am Anfang: Sie verhindern Schreibfehler, sodass Sie sich auf den Ablauf konzentrieren können. Nach Vorlesung 07 arbeiten wir nur noch im Text.

## Rechnen

<!-- data-type="none" -->
| Operator | Bedeutung             | Beispiel   | Ergebnis |
| :------: | :-------------------- | :--------- | :------- |
| `+`      | Addition              | `3 + 4`    | `7`      |
| `-`      | Subtraktion           | `3 - 4`    | `-1`     |
| `*`      | Multiplikation        | `3 * 4`    | `12`     |
| `/`      | Division              | `7 / 2`    | `3.5`    |
| `//`     | ganzzahlige Division  | `7 // 2`   | `3`      |
| `%`      | Rest der Division     | `7 % 2`    | `1`      |
| `**`     | Potenz                | `2 ** 10`  | `1024`   |

Es gilt Punkt- vor Strichrechnung, Klammern gehen vor.

```python
print(3 + 4 * 2)
print((3 + 4) * 2)
print(7 / 2)
print(7 // 2)
print(18900801 // 10000)
```
@Pyodide.eval

> Die letzte Zeile ist kein Zufall: Das DWD-Datum `18900801` ganzzahlig durch `10000` geteilt ergibt das Jahr. Genau diesen Trick nutzt die Vier-Zeilen-Lösung aus der letzten Vorlesung.

                                     {{1}}
*******************************************************************************

> [!WARNING]
> **Dezimalpunkt, nicht Dezimalkomma!** Python ist eine englischsprachige Sprache. `6.26` ist eine Zahl. `6,26` ist etwas völlig anderes:

```python
print(6.26 + 1)
print(6,26 + 1)
```
@Pyodide.eval

Die zweite Zeile gibt `6 27` aus. Python hat zwei Werte gesehen — `6` und `26 + 1` — und beide ausgegeben. **Keine Fehlermeldung, aber ein falsches Ergebnis.** Das ist die gefährlichste Art von Fehler.

*******************************************************************************

--{{0}}--
`/` liefert immer eine Kommazahl, auch bei `8 / 2`. `%` liefert den Rest einer Division. Damit prüft man zum Beispiel, ob eine Zahl gerade ist: `n % 2` ergibt dann 0.

--{{1}}--
Python liest das Komma als Trennzeichen zwischen zwei Werten, genau wie in `print("Höhe:", 1213)`. Deutsche Zahlen in Dateien sind deshalb eine ständige Falle. Am Ende der Vorlesung begegnet sie uns wieder.

## Variablen

Eine **Variable** ist ein Name, unter dem sich ein Programm einen Wert merkt.

```` @BlocklyId(variablen, runner=variablen hideRunner height=300)
tagesmittel = 6.26
minimum = -14.1
maximum = 26.9

spanne = maximum - minimum
print("Temperaturspanne 2024:", spanne)
````

```python
# runner: variablen
```
@Pyodide.eval

--{{0}}--
Die Werte stammen aus dem Jahr 2024: Jahresmittel, tiefstes Minimum und höchstes Maximum. Eine Variable ähnelt einer benannten Zelle in der Tabellenkalkulation, mit einem wichtigen Unterschied, den Sie gleich sehen werden. Eine Variable entsteht in dem Moment, in dem ihr zum ersten Mal ein Wert zugewiesen wird.

### Das Gleichheitszeichen ist keine Gleichung

                                     {{0-1}}
*******************************************************************************

In der Mathematik ist `x = x + 1` ein Widerspruch. In Python ist es eine ganz normale Anweisung:

```python
zaehler = 0
zaehler = zaehler + 1
zaehler = zaehler + 1
print(zaehler)
```
@Pyodide.eval

> **Lesen Sie `=` als "wird zu".** Rechts wird zuerst ausgerechnet, dann wird das Ergebnis unter dem Namen links abgelegt. Der alte Wert ist danach weg.

*******************************************************************************

                                     {{1}}
*******************************************************************************

**Programme im Kopf ausführen**

Die wichtigste Fähigkeit dieses Kurses — und eine typische Klausuraufgabe — ist, ein Programm Zeile für Zeile im Kopf nachzuvollziehen. Dazu legt man eine Tabelle an, eine Spalte pro Variable:

```python
a = 5
b = a * 2
a = a + b
b = b - 1
print(a, b)
```

<!-- data-type="none" -->
| nach Zeile | `a`  | `b`  |
| :--------- | :--- | :--- |
| 1          | 5    | –    |
| 2          | 5    | 10   |
| 3          | 15   | 10   |
| 4          | 15   | 9    |

Die Ausgabe lautet also `15 9`.

*******************************************************************************

--{{0}}--
`zaehler = zaehler + 1` wird Ihnen ab nächster Woche ständig begegnen: So zählt ein Programm mit. Rechts steht der alte Wert, links landet der neue.

--{{1}}--
Das ist das Ablaufprotokoll aus Vorlesung 01, jetzt für Python. Eine Zeile pro Anweisung, eine Spalte pro Variable. Die Zeile mit `print` ändert keine Variable, deshalb fehlt sie in der Tabelle.

### Typische Fehlvorstellung: Variablen rechnen nach

> **Typische Fehlvorstellung:** _„Eine Variable merkt sich die Rechnung — wie eine Formel in der Tabellenkalkulation.“_

```python
minimum = -3.5
maximum = 2.6
spanne = maximum - minimum
maximum = 8.0
print(spanne)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[(X)] `6.1`
[( )] `11.5`
[( )] eine Fehlermeldung, weil `maximum` zweimal belegt wird
***
In der Tabellenkalkulation würde `=B2-B1` sofort neu rechnen, wenn sich `B2` ändert. In Python nicht: In Zeile 3 wird die Differenz **einmal** ausgerechnet und das Ergebnis `6.1` unter `spanne` abgelegt. Welche Rechnung dahintersteckt, weiß `spanne` danach nicht mehr — und dass sich `maximum` später ändert, bemerkt sie nicht.

Soll `spanne` den neuen Wert berücksichtigen, muss man die Zeile `spanne = maximum - minimum` erneut ausführen.
***

--{{0}}--
Hier zeigt sich der Unterschied aus Vorlesung 01: Die Tabellenkalkulation ist eingabengetrieben, ein Skript läuft der Reihe nach. Python merkt sich das Ergebnis einer Rechnung, nicht ihren Weg.

### Namen wählen

Ein Variablenname

* besteht aus Buchstaben, Ziffern und dem Unterstrich `_`,
* beginnt **nicht** mit einer Ziffer,
* unterscheidet Groß- und Kleinschreibung: `Minimum` und `minimum` sind zwei verschiedene Variablen,
* darf kein reserviertes Wort wie `if`, `for`, `while` oder `True` sein.

<!-- data-type="none" -->
| Name            | erlaubt? | gut?                                                     |
| :-------------- | :------: | :------------------------------------------------------- |
| `tagesmittel`   | ja       | ja — sagt, was drin ist                                  |
| `t`             | ja       | nur für ganz kurze Rechnungen                            |
| `max_temp_2024` | ja       | ja — Wörter trennt man mit `_`                           |
| `2024_max`      | **nein** | beginnt mit einer Ziffer                                 |
| `höhe`          | ja       | besser `hoehe` — Umlaute machen früher oder später Ärger |

> Ein guter Name spart einen Kommentar. `x = 1213` erklärt nichts, `stationshoehe_m = 1213` alles.

> **Typische Fehlvorstellung:** _„Der Rechner versteht, was ein Name bedeutet.“_
>
> `frosttage = 0` zählt keine Frosttage. `mittelwert = 0` berechnet keinen Mittelwert. Namen sind nur Etiketten für Sie und andere Menschen. Was in einer Variable steht, bestimmen ausschließlich die Anweisungen, die Sie schreiben.

--{{0}}--
Python kennt rund 35 reservierte Wörter, einige davon lernen Sie nächste Woche kennen. Visual Studio Code färbt sie ein, Sie können sie also nicht übersehen. Umlaute sind erlaubt, machen aber Ärger, sobald Dateien zwischen Rechnern wandern.

## Datentypen

Jeder Wert hat einen **Datentyp**. Der Typ entscheidet, was man mit dem Wert tun kann.

<!-- data-type="none" -->
| Typ     | Bedeutung                    | Beispiel aus unserem Datensatz |
| :------ | :--------------------------- | :----------------------------- |
| `int`   | ganze Zahl                   | `1358` (Stations-ID)           |
| `float` | Kommazahl                    | `-14.1` (Minimum in °C)        |
| `str`   | Text (Zeichenkette)          | `"Fichtelberg"`                |
| `bool`  | Wahrheitswert                | `True` (war es ein Frosttag?)  |

Mit `type(...)` können Sie jeden Wert nach seinem Typ fragen:

```python
print(type(1358))
print(type(-14.1))
print(type("Fichtelberg"))
print(type(-14.1 < 0))
print(type("18900801"))
```
@Pyodide.eval

--{{0}}--
Der DWD schreibt die Stations-ID mit führender Null: `01358`. Als `int` geht die Null verloren, und ohne Anführungszeichen meldet Python sogar einen `SyntaxError`. Kennziffern wie Postleitzahlen sind deshalb Text, auch wenn sie aus Ziffern bestehen. `float` steht für Gleitkommazahl, `bool` ist nach dem Mathematiker George Boole benannt.

### Text ist nicht Zahl

                                     {{0-1}}
*******************************************************************************

Wenn Sie eine Datei einlesen (Vorlesung 06), bekommen Sie immer **Text**. Auch wenn er aussieht wie eine Zahl:

```python
minimum_aus_datei = "-14.1"
print(minimum_aus_datei + 1)
```
@Pyodide.eval

Python weigert sich — zu Recht. Was soll `"-14.1" + 1` sein?

*******************************************************************************

                                     {{1}}
*******************************************************************************

Die Lösung ist eine **Typumwandlung**:

<!-- data-type="none" -->
| Umwandlung    | Beispiel           | Ergebnis     |
| :------------ | :----------------- | :----------- |
| `float(...)`  | `float("-14.1")`   | `-14.1`      |
| `int(...)`    | `int("1890")`      | `1890`       |
| `str(...)`    | `str(1213)`        | `"1213"`     |
| `int(...)`    | `int(6.9)`         | `6` — schneidet ab, rundet nicht! |

```python
minimum_aus_datei = "-14.1"
minimum = float(minimum_aus_datei)
print(minimum + 1)

wert_aus_tabelle = "6,26"
print(float(wert_aus_tabelle))
```
@Pyodide.eval

Die letzte Zeile scheitert. Ändern Sie sie so, dass sie funktioniert.

> **Tipp:** Texte haben eine Methode `replace`: `"a,b".replace(",", ".")` ergibt `"a.b"`.

<details>
<summary>**Lösung**</summary>

```python
print(float(wert_aus_tabelle.replace(",", ".")))
```

Solche Reparaturen gehören zum Alltag der Datenaufbereitung. Sie werden uns noch oft begegnen.

</details>

*******************************************************************************

--{{0}}--
Für Python ist eine Datei zunächst nur eine lange Folge von Zeichen. Von Spalten und Zahlen weiß es nichts, das ist Ihre Aufgabe.

--{{1}}--
`int(6.9)` schneidet ab, `int("6.9")` scheitert dagegen mit einem `ValueError`, weil in einem Text für `int` kein Punkt stehen darf. Runden können Sie mit `round(6.9)`.

### Mit Text arbeiten

Texte kann man zusammensetzen, nach ihrer Länge fragen und Teile herausschneiden:

```python
station = "Fichtelberg"
print("Station " + station)
print(len(station))

datum = "18900801"
jahr = datum[0:4]
monat = datum[4:6]
print(jahr, monat)
```
@Pyodide.eval

> `datum[0:4]` bedeutet: die Zeichen ab Position 0 bis **vor** Position 4. Python beginnt beim Zählen immer bei **0**.

--{{0}}--
Stellen Sie sich die Positionen als Striche zwischen den Zeichen vor: `[0:4]` schneidet von Strich 0 bis Strich 4. So lässt sich die Länge direkt ablesen, 4 minus 0 sind vier Zeichen. Eine negative Position zählt von hinten, `station[-1]` ist das letzte Zeichen.

### Vergleiche

Vergleiche liefern einen Wahrheitswert — `True` oder `False`:

<!-- data-type="none" -->
| Operator | Bedeutung            | Beispiel       | Ergebnis |
| :------: | :------------------- | :------------- | :------- |
| `<`      | kleiner              | `-14.1 < 0`    | `True`   |
| `>`      | größer               | `-14.1 > 0`    | `False`  |
| `<=`     | kleiner oder gleich  | `0 <= 0`       | `True`   |
| `==`     | gleich               | `-999 == -999` | `True`   |
| `!=`     | ungleich             | `5.2 != -999`  | `True`   |

```python
minimum = -3.5
frosttag = minimum < 0
print("Frosttag?", frosttag)
```
@Pyodide.eval

> Achtung: `=` weist zu, `==` vergleicht. Die Verwechslung ist einer der häufigsten Anfängerfehler.
>
> Mit diesen Wahrheitswerten trifft ein Programm **Entscheidungen** — darum geht es in der nächsten Vorlesung.

--{{0}}--
Vorsicht bei zwei Vergleichen: `"10" < "9"` ist `True`, weil Text Zeichen für Zeichen verglichen wird. Wandeln Sie deshalb vor dem Vergleichen um. Und `0.1 + 0.2 == 0.3` ist `False`, weil Kommazahlen im Rechner nicht exakt gespeichert werden. Kommazahlen sollte man deshalb nicht mit `==` auf exakte Gleichheit prüfen.

## Kommentare

Alles hinter einem `#` ignoriert der Interpreter. Kommentare sind für Menschen:

```python
fehlwert = -999      # So kennzeichnet der DWD "nicht gemessen"
minimum = -999

# Ein Fehlwert ist kein Frost, auch wenn -999 < 0 ist!
print(minimum < 0)
```
@Pyodide.eval

> Gute Kommentare erklären, **warum** etwas so ist — nicht **was** dasteht. `zaehler = zaehler + 1  # erhöhe zaehler um 1` hilft niemandem.

--{{0}}--
Das Programm zeigt das Problem, löst es aber noch nicht: `-999` ist kleiner als 0 und zählt damit als Frost. Wie man das verhindert, lernen Sie nächste Woche. In Visual Studio Code macht `Strg+/`, auf deutscher Tastatur oft `Strg+#`, aus markierten Zeilen Kommentare. So schaltet man Zeilen vorübergehend ab.

## Fehlermeldungen lesen

Fehler sind normal — auch nach Jahren der Programmiererfahrung. Entscheidend ist, die Meldung zu **lesen**, statt sie wegzuklicken.

```python
stationshoehe = 1213
print("Die Station liegt auf", stationshoe, "m Höhe")
```
@Pyodide.eval

Eine Python-Fehlermeldung lesen Sie **von unten nach oben**:

``` text
Traceback (most recent call last):
  File "<exec>", line 2, in <module>          ← wo: Zeile 2
NameError: name 'stationshoe' is not defined  ← was: diesen Namen gibt es nicht
```

Die häufigsten Fehler am Anfang:

<!-- data-type="none" -->
| Fehler         | Bedeutung                                        | typische Ursache                          |
| :------------- | :----------------------------------------------- | :---------------------------------------- |
| `SyntaxError`  | Der Text ist kein gültiges Python                | Klammer oder Anführungszeichen vergessen  |
| `NameError`    | Diesen Namen kennt Python nicht                  | Tippfehler, Variable noch nicht angelegt  |
| `TypeError`    | Diese Operation passt nicht zu diesem Typ        | `"-14.1" + 1`                             |
| `ValueError`   | Der Typ stimmt, der Wert aber nicht              | `float("6,26")`                           |

> **Und dann?** Lesen, Zeile anschauen, Hypothese bilden, ändern, erneut ausführen. Hilft das nicht: die letzte Zeile der Meldung in eine Suchmaschine kopieren. Sie sind garantiert nicht die erste Person mit diesem Fehler.

--{{0}}--
Traceback heißt Rückverfolgung. In Visual Studio Code steht statt `<exec>` der Pfad Ihrer Datei. Auch ein KI-Assistent kann eine Meldung erklären. Prüfen Sie seinen Vorschlag aber wie jedes andere Ergebnis: Können Sie sagen, warum er das Problem löst?

### Typische Fehlvorstellung: Der Fehler steht in der gemeldeten Zeile

> Aus Ihren Antworten in Vorlesung 00: _„… praktisch leider oft mini Schreibfehler, die niemand findet“_

> **Typische Fehlvorstellung:** _„Der Fehler steht in der Zeile, die Python meldet.“_

```python
minimun = -3.5
maximum = 0.7
spanne = maximum - minimum
print("Spanne:", spanne)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: In welcher Zeile müssen Sie etwas ändern?

[( )] in Zeile 3, denn dort meldet Python den Fehler
[(X)] in Zeile 1
[( )] in Zeile 4
***
Python meldet Zeile 3: `NameError: name 'minimum' is not defined. Did you mean: 'minimun'?` Dort wird `minimum` zum ersten Mal **benutzt**. Der Tippfehler steckt aber in Zeile 1, wo `minimun` angelegt wurde.

Python zeigt, wo es nicht weiterkommt, nicht, wo der Fehler entstanden ist. Der Zusatz `Did you mean: 'minimun'?` führt direkt zur Ursache. Lesen Sie die Meldung deshalb bis zum Ende.
***

                                    --{{0}}--
Bei einem `NameError` lohnt immer der Blick nach oben: Wo wurde der Name angelegt, und ist er dort genauso geschrieben? Ähnlich bei Klammern: Fehlt eine schließende Klammer, meldet Python `'(' was never closed` und zeigt auf die öffnende. Die Suche beginnt also an der gemeldeten Stelle, endet aber oft weiter oben.

## Die Antwort auf die Leitfrage

So steht der 1. Januar 2024 in `fichtelberg_2024.csv`, die Spalten sind Datum, Tagesmittel, Minimum und Maximum:

```python
zeile = "2024-01-01;-1,2;-1,9;-0,7"

stueck = zeile[16:20]
print(stueck, type(stueck))

minimum = float(stueck.replace(",", "."))
print(minimum, minimum < 0)
```
@Pyodide.eval

> Für den Rechner ist `-1,9` zunächst nur Text. Erst wenn wir das richtige Stück **herausschneiden**, das Komma **ersetzen** und **umwandeln**, wird daraus eine Zahl, mit der man rechnen und vergleichen kann. In diesen Zeilen steckt die ganze heutige Vorlesung.

--{{0}}--
Warum Position 16? Das Datum belegt zehn Zeichen, dann folgen ein Semikolon, vier Zeichen Tagesmittel und noch ein Semikolon. Sehen Sie die Parallele zum Anfang der Vorlesung? Abspalten, umwandeln, vergleichen: Das waren dieselben drei Schritte wie bei den Uhrzeiten in der Tabellenkalkulation. Nur schreiben Sie sie jetzt selbst auf.

### Typische Fehlvorstellung: Was für eine Zeile stimmt, stimmt für alle

> **Typische Fehlvorstellung:** _„Läuft das Programm für eine Zeile richtig, läuft es für jede richtig.“_

Dasselbe Programm, sechs Tage später:

```python
zeile = "2024-01-07;-8,9;-11,9;-4,2"

stueck = zeile[16:20]
minimum = float(stueck.replace(",", "."))
print(minimum)
```
@Pyodide.eval

Legen Sie sich fest, **bevor** Sie das Programm ausführen: Was wird ausgegeben?

[( )] `-11.9`
[(X)] `-11.0`
[( )] eine Fehlermeldung
***
Das Minimum beträgt `-11,9`, ist aber ein Zeichen länger als `-1,9`. An den Positionen 16 bis 19 steht deshalb nur `-11,`, und daraus macht Python ohne Beschwerde `-11.0`.

Über das ganze Jahr 2024 trifft `[16:20]` in 134 von 366 Zeilen den richtigen Wert. In 227 Zeilen bricht das Programm mit einem Fehler ab. In 5 Zeilen läuft es durch und liefert einen falschen Wert.
***

--{{0}}--
Das ist derselbe Fehlertyp wie das Komma in `print(6,26 + 1)`: keine Meldung, aber ein falsches Ergebnis. Deshalb reicht es nicht, ein Programm an einer einzigen Zeile zu prüfen. Die saubere Lösung lernen Sie in Vorlesung 06 kennen: `split(";")` zerlegt eine Zeile an den Semikolons, egal wie lang die Zahlen sind.

## Kontrollfragen

**Was gibt dieses Programm aus?**

```python
x = 4
y = x + 3
x = y * 2
y = x - y
print(x, y)
```

[[14 7]]
[[?]] Legen Sie eine Tabelle mit einer Spalte für `x` und einer für `y` an.
***
| nach Zeile | `x` | `y` |
| :--------- | :-- | :-- |
| 1          | 4   | –   |
| 2          | 4   | 7   |
| 3          | 14  | 7   |
| 4          | 14  | 7   |

In Zeile 4 wird `y` zu `14 - 7 = 7` — der Wert bleibt also zufällig gleich.
***

**Finden Sie alle Fehler.**

```python
Tagesmittel = 6.26
spanne = 26,9 - -14.1
print("Mittel:" tagesmittel)
```

[[X]] Zeile 2: `26,9` muss `26.9` heißen
[[X]] Zeile 3: Zwischen `"Mittel:"` und dem Namen fehlt ein Komma
[[X]] Zeile 3: `tagesmittel` ist klein geschrieben, angelegt wurde `Tagesmittel`
[[ ]] Zeile 2: `- -14.1` ist nicht erlaubt
***
`- -14.1` ist korrekt und bedeutet "minus minus 14,1", also plus 14,1. Der Fehler in Zeile 2 erzeugt übrigens **keine** Fehlermeldung — `spanne` wird einfach ein Paar aus zwei Werten.
***

### Weitere Kontrollfragen zum Nacharbeiten

**Welchen Typ haben die folgenden Werte?**

[ [int] [float] [str] [bool] ]
[ (X)   ( )     ( )   ( )    ] `1890`
[ ( )   (X)     ( )   ( )    ] `-0.5`
[ ( )   ( )     (X)   ( )    ] `"-0.5"`
[ ( )   ( )     ( )   (X)    ] `-0.5 < 0`
[ ( )   (X)     ( )   ( )    ] `7 / 7`
[ (X)   ( )     ( )   ( )    ] `18900801 // 10000`

**Welche Fehlermeldung erzeugt `print("Frosttage: " + 127)`?**

[( )] `SyntaxError`
[( )] `NameError`
[(X)] `TypeError`
[( )] `ValueError`
***
Text und Zahl lassen sich nicht mit `+` verbinden. Richtig wäre `print("Frosttage: " + str(127))` oder einfacher `print("Frosttage:", 127)`.
***

**Welche Zeilen sind gültige Zuweisungen?**

[[X]] `hoehe = 1213`
[[ ]] `1213 = hoehe`
[[ ]] `hoehe + 1 = neue_hoehe`
[[X]] `neue_hoehe = hoehe + 1`
[[X]] `hoehe = hoehe + 1`
***
Links vom `=` steht immer **genau ein Name** — dort wird das Ergebnis abgelegt. Rechts steht der Ausdruck, der zuerst ausgerechnet wird. Anders als in der Mathematik lässt sich eine Zuweisung nicht "umdrehen".
***

## Ihre Begriffe für die Kurslandkarte

Die [Kurslandkarte](https://tubaf-ifi-liascript.github.io/VL_EAVD/kurslandkarte/) wächst mit dem Semester. Wir schlagen die Begriffe vor, Sie ergänzen, was fehlt: Aus Ihren Datenwünschen in Vorlesung 00 sind so schon die ersten Anwendungen geworden. Nehmen Sie sich dafür jetzt fünf Minuten.

**Welches Wort von heute müssten Sie jemandem aus Ihrem Semester erklären können?**

[[___ ___ ___]]

**Welche Daten aus Ihrem Fach würden Sie gern so auswerten?**

[[___ ___ ___]]

## Nächste Woche

Ab der nächsten Vorlesung arbeiten wir zusätzlich mit Python auf Ihrem eigenen Rechner.

**Zur Vorbereitung**

- [ ] Falls in der ersten Übung noch nicht geschehen: Installieren Sie Python (mindestens Version 3.12) von [python.org](https://www.python.org/downloads/) und [Visual Studio Code](https://code.visualstudio.com/) mit der Erweiterung _Python_. Die Anleitung steht auf Blatt 1, Teil B.
- [ ] Schreiben Sie eine Datei `hallo.py` mit einer `print`-Anweisung und führen Sie sie aus.
- [ ] Probieren Sie: Wie rechnet man in Python eine Temperatur von °C in °F um? ($F = C \cdot 1{,}8 + 32$)

> Wenn die Installation nicht klappt: Bringen Sie Ihren Laptop in die Übung mit. Dort helfen wir.

**Zur Übung**

Blatt 2 (Bohrkerne vermessen) steht nach der Vorlesung in [OPAL](https://bildungsportal.sachsen.de/opal/auth/RepositoryEntry/469368834). Versuchen Sie sich **vor** der Übung an den Aufgaben, gern auch zu zweit. Besprochen wird es in der Übung ab dem 09.11.
