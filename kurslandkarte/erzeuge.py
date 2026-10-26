"""Kurslandkarte EAVD: Kursdaten.

Begriffe, Beziehungen, Anwendungen und didaktische Fäden sind hier kuratiert;
Prüfung, Karte und Startseite erzeugt der gemeinsame Kern invivis Kurslandkarte
(kurslandkarte/invivis/, nicht hier ändern). Abschnitte (Foliennummern) liest
der Kern automatisch aus den Vorlesungen.

Aufruf aus dem Repository-Wurzelverzeichnis:

    python3 kurslandkarte/erzeuge.py                 # Karte und Startseite
    python3 kurslandkarte/erzeuge.py --pdf           # vorher fehlende/veraltete PDFs freigegebener Vorlesungen mit liaex erzeugen
    python3 kurslandkarte/erzeuge.py --freigegeben   # für das Makefile: Dateien der freigegebenen Vorlesungen

Schreibt docs/kurslandkarte/kurslandkarte.json, docs/kurslandkarte/index.html und docs/index.html.
Nur Freigegebenes steht in der Seite: Begriffe kommender Vorlesungen verlassen das Repository nicht.
"""
import glob, os, re, sys

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
sys.path.insert(0, os.path.join(HIER, "invivis"))
import kern

ANZAHL = 15
DATEIEN = {int(os.path.basename(f)[:2]): os.path.basename(f) for f in glob.glob(os.path.join(REPO, "[01][0-9]_*.md"))}
assert sorted(DATEIEN) == list(range(ANZAHL)), sorted(DATEIEN)

STATUS = {v: "ausgearbeitet" for v in range(15)}
STATUS[8] = "Rumpf"

# ---- Termine (Montag der Vorlesung) und Kurztitel für die Karte
TERMINE = [
    ("2026-10-19", "Motivation"), ("2026-10-26", "Problem → Programm"),
    ("2026-11-02", "Erste Schritte"), ("2026-11-09", "Prüfen & Wiederholen"),
    ("2026-11-16", "Muster"), ("2026-11-23", "Daten sammeln"),
    ("2026-11-30", "Dateien lesen"), ("2026-12-07", "Funktionen"),
    ("2026-12-14", "Demo MicroPython"), ("2027-01-04", "Strukturieren"),
    ("2027-01-11", "NumPy"), ("2027-01-18", "pandas I"),
    ("2027-01-25", "pandas II"), ("2027-02-01", "Visualisierung"),
    ("2027-02-08", "Datenqualität"),
]
assert len(TERMINE) == 15

# ---- Freigabe: Begriffe einer Vorlesung erscheinen erst nach ihr in der Karte.
# Nach jeder Vorlesung: Vorschläge der Studierenden einarbeiten, dann hier ergänzen.
FREIGEGEBEN = {0, 1}
# PDFs schon vor der Vorlesung, damit Studierende darin mitschreiben können (Begriffe weiterhin erst nach Freigabe).
PDF_VORAB = {1, 2}
if "--freigegeben" in sys.argv:   # für das Makefile: Dateien der freigegebenen Vorlesungen
    print(" ".join(DATEIEN[v] for v in sorted(FREIGEGEBEN)))
    sys.exit()

# ---- Leitfragen aus dem Semesterplan in VL 00 (einzige Quelle)
_plan = open(os.path.join(REPO, "00_Motivation.md"), encoding="utf-8").read()
# (ganze Datei: die Termin-Zeilen „| TT.MM. | NN …“ kommen nur in der Semesterplan-Tabelle vor)
LEITFRAGE = {}
for _z in _plan.splitlines():
    _m = re.match(r"\| \d\d\.\d\d\. \| \[?(\d\d)", _z)
    if _m:
        LEITFRAGE[int(_m.group(1))] = _z.split("|")[-2].strip()
assert sorted(LEITFRAGE) == list(range(15)), ("Leitfragen im Semesterplan unvollständig", sorted(LEITFRAGE))

# ---- Begriffe: id, Name, Linie, VL, Abschnitt, Ebene, Code?, Erklärung, Fehlvorstellung
B = [
    # --- Erhebung
    ("zaehler", "Datenerhebung", "erhebung", 0, 'Praktische Inhalte', 1, 0, "Messdaten entstehen nicht von selbst: Ein Sensor wandelt etwas Physikalisches in Zahlen um, ein Programm entscheidet, was davon festgehalten wird.", None),
    ("annahmen", "Annahmen im Programm", "erhebung", 0, 'Wo soll das hinführen?', 2, 0, "Grenzwerte, Schwellen und Zeitfenster im Code legen fest, was als Ergebnis herauskommt — ohne dass eine Fehlermeldung darauf hinweist.", "„Es funktioniert, also stimmt das Ergebnis.“"),
    ("sensorlog", "Sensorprotokoll", "erhebung", 1, 'Aufgabe 2: Der Personenzähler', 2, 0, "Die Zeitstempel des Personenzählers — mühsam in der Tabellenkalkulation auszuwerten (Aufgabe 2).", None),
    ("micropy", "MicroPython", "erhebung", 8, 'Der Aufbau', 1, 0, "Python auf dem Mikrocontroller — dieselbe Sprache, andere Hardware.", None),
    ("sensor", "Sensor", "erhebung", 8, 'Der Aufbau', 1, 0, "Wandelt eine physikalische Größe in eine Zahl um — mit Genauigkeit, Messort und Ausfallrisiko.", None),
    ("seriell", "serielle Ausgabe", "erhebung", 8, 'Live: Wir messen', 2, 0, "Der Mikrocontroller schickt Messwerte als Textzeilen an den Rechner, dort werden sie mitgeschrieben.", None),
    ("messfehler", "Messfehler", "erhebung", 8, 'Was schiefgeht', 1, 0, "Annahmen im Messprogramm werden verletzt — sichtbar im Datenstrom, aber ohne Fehlermeldung.", "„Ein Sensor misst, was draufsteht.“"),
    ("zeitstempel", "Zeitstempel", "erhebung", 8, 'Was schiefgeht', 2, 0, "Entsteht beim Empfang oder Schreiben — nicht unbedingt im Moment des Ereignisses.", "„Ein Zeitstempel ist die Zeit des Ereignisses.“"),
    ("messdatei", "eigene Messdatei", "erhebung", 8, 'Die Daten kommen wieder', 2, 0, "Die in der Demonstration aufgezeichneten Daten kommen im Januar als Analysebeispiel zurück.", None),

    # --- Denken & Kontrollfluss
    ("blockly", "Programmdarstellung: Blöcke oder Text", "denken", 0, 'Blöcke oder Text', 2, 0, "Zwei Ansichten auf dasselbe Programm: Blöcke zusammenschieben oder Python tippen.", None),
    ("vorhersage", "Vorhersage vor dem Ausführen", "denken", 0, 'Typische Fehlvorstellungen', 1, 0, "Erst festlegen, was das Programm ausgeben wird, dann ausführen. Wer danebenliegt, sieht, wo das eigene Bild vom Programm nicht stimmt.", None),
    ("ki", "KI-Assistent", "denken", 0, 'Und was ist mit KI?', 1, 0, "Schreibt Code in Sekunden. Man muss aber sagen können, was man will, und prüfen können, ob das Ergebnis stimmt.", "„Die KI hat das Programm geschrieben, also stimmt es.“"),
    ("algo", "Algorithmus", "denken", 1, 'Algorithmen', 1, 0, "Eindeutige Handlungsvorschrift aus endlich vielen ausführbaren Schritten, die für jede passende Eingabe nach endlich vielen Schritten ein Ergebnis liefert.", None),
    ("terminierung", "Eindeutigkeit & Terminierung", "denken", 1, 'Algorithmen', 2, 0, "Jeder Schritt hat genau eine Auslegung; die Ausführung endet nach endlich vielen Schritten.", None),
    ("sprache", "Programmiersprache", "denken", 1, 'Warum der Rechner keine Alltagssprache versteht', 2, 0, "Kompromiss zwischen menschlicher Lesbarkeit und maschineller Eindeutigkeit.", "„Der Rechner versteht, was ich meine.“"),
    ("pseudo", "Pseudocode", "denken", 1, 'Algorithmen darstellen', 1, 0, "Algorithmus in strukturierter Alltagssprache, bevor man ihn programmiert.", None),
    ("ablauf", "Ablaufdiagramm", "denken", 1, 'Algorithmen darstellen', 2, 0, "Grafische Form eines Algorithmus mit Entscheidungen und Rücksprüngen.", None),
    ("bausteine", "Folge, Verzweigung, Wiederholung", "denken", 1, 'Drei Bausteine', 1, 0, "Aus diesen drei Bausteinen setzt sich jeder Algorithmus zusammen.", None),
    ("protokoll", "Ablaufprotokoll", "denken", 1, 'Einen Algorithmus von Hand ausführen', 2, 0, "Einen Algorithmus mit wenigen Werten von Hand ausführen und nach jedem Schritt den Zwischenstand notieren.", None),
    ("eingabe", "Eingabengetrieben oder der Reihe nach", "denken", 1, 'Eingabengetrieben oder der Reihe nach', 2, 0, "Die Tabelle rechnet neu, sobald sich ein Wert ändert; ein Skript läuft Zeile für Zeile in festgelegter Reihenfolge.", None),
    ("interpreter", "Interpreter", "denken", 2, 'Vom Text zur Ausführung', 2, 0, "Liest das Programm Zeile für Zeile, führt aus — oder bricht mit einer Fehlermeldung ab.", None),
    ("print", "print", "denken", 2, 'Die erste Anweisung', 1, 1, "Gibt Werte auf dem Bildschirm aus.", None),
    ("operatoren", "Rechenoperatoren", "denken", 2, 'Rechnen', 2, 0, "+ - * / sowie // (ganzzahlig), % (Rest), ** (Potenz). 18900801 // 10000 ergibt das Jahr.", None),
    ("variable", "Variable", "denken", 2, 'Variablen', 1, 0, "Ein Name, unter dem sich ein Programm einen Wert merkt.", "„Eine Variable merkt sich die Rechnung — wie eine Formel in der Tabellenkalkulation.“"),
    ("zuweisung", "Zuweisung =", "denken", 2, 'Das Gleichheitszeichen ist keine Gleichung', 1, 0, "Rechts wird gerechnet, links wird das Ergebnis abgelegt. Lies = als „wird zu“.", "„= ist eine Gleichung.“"),
    ("zeitwert", "Uhrzeit als Zahl", "typen", 2, 'Rückblick: Uhrzeiten in der Tabellenkalkulation', 2, 0, "Für die Tabellenkalkulation ist eine Uhrzeit der Bruchteil eines Tages (12:00 = 0,5). Erst als Zahl lässt sie sich vergleichen.", "„Was wie eine Uhrzeit aussieht, kann ich auch wie eine Uhrzeit vergleichen.“ Text gilt beim Vergleich als größer als jede Zahl."),
    ("vierfragen", "Von der Frage zum Pseudocode", "denken", 2, 'Von der Frage zum Pseudocode', 1, 0, "Vier Fragen: Was steht in einer Zeile? Was merke ich mir? Was tue ich mit jeder Zeile? Was gebe ich am Ende aus?", "„Eindeutig heißt so gemeint.“ — „beginnt mit A“ zählt weder „Åberg“ noch „auf der Heide“."),
    ("trace", "Programm im Kopf ausführen", "denken", 2, 'Das Gleichheitszeichen ist keine Gleichung', 2, 0, "Tabelle mit einer Spalte pro Variable, eine Zeile pro Schritt — die zentrale Klausurfähigkeit.", None),
    ("namen", "Variablennamen", "denken", 2, 'Namen wählen', 2, 0, "Buchstaben, Ziffern, Unterstrich; nicht mit Ziffer beginnen; sprechend wählen.", "„Der Rechner versteht, was ein Name bedeutet.“"),
    ("vergleich", "Vergleich / bool", "denken", 2, 'Vergleiche', 1, 0, "Vergleiche wie minimum < 0 liefern True oder False.", "= weist zu, == vergleicht."),
    ("kommentar", "Kommentar", "denken", 2, 'Kommentare', 2, 0, "Alles hinter # ist für Menschen. Gute Kommentare erklären das Warum.", None),
    ("fehlermeldung", "Fehlermeldung", "denken", 2, 'Fehlermeldungen lesen', 1, 0, "Von unten nach oben lesen: was (NameError, TypeError, ValueError, SyntaxError) und wo.", None),
    ("uebertragbar", "Browser = eigener Rechner", "denken", 3, 'Dieselben Beispiele auf Ihrem Rechner', 2, 0, "Die Beispiele laufen eins zu eins in Visual Studio Code — einzige Ausnahme ist open_url.", None),
    ("if", "if", "denken", 3, 'Entscheidungen: if', 1, 1, "Führt Anweisungen nur aus, wenn eine Bedingung gilt.", None),
    ("einrueckung", "Einrückung", "denken", 3, 'Einrückung ist Syntax', 2, 0, "In Python ist die Einrückung die Struktur: Sie bestimmt, was zu if oder for gehört.", None),
    ("else", "else", "denken", 3, 'Entweder – oder: else', 2, 1, "Genau einer von zwei Blöcken wird ausgeführt.", None),
    ("elif", "elif", "denken", 3, 'Mehrere Fälle: elif', 2, 1, "Mehrere Fälle nacheinander prüfen; der erste zutreffende gewinnt.", "Die Reihenfolge der Fälle zählt: ein spezieller Fall hinter einem allgemeinen wird nie erreicht."),
    ("logik", "and / or / not", "denken", 3, 'Bedingungen verknüpfen', 2, 1, "Bedingungen verknüpfen, z. B. minimum != -999 and minimum < 0.", None),
    ("for", "for-Schleife", "denken", 3, 'Wiederholen: for', 1, 1, "Wiederholt einen Block für jeden Wert einer Folge.", None),
    ("zaehlmuster", "Zählmuster", "denken", 3, 'Das Zählmuster', 1, 0, "Zähler vor der Schleife anlegen, in der Schleife bedingt erhöhen, danach ausgeben.", "Zähler in der Schleife anlegen: Er wird in jedem Durchlauf zurückgesetzt."),
    ("schleifenvar", "Schleifenvariable", "denken", 3, 'Typische Fehlvorstellung: Die Schleifenvariable', 2, 0, "Bekommt in jedem Durchlauf den nächsten Wert — und behält nach der Schleife den letzten.", "„Nach der Schleife ist die Schleifenvariable weg.“"),
    ("summe", "Aufsummieren", "denken", 4, 'Muster 1: Aufsummieren', 1, 0, "Summe und Anzahl in der Schleife fortschreiben.", None),
    ("extrem", "Extremwert suchen", "denken", 4, 'Muster 2: Extremwert suchen', 1, 0, "Den bisher besten Wert (und seine Position) merken und bei Bedarf ersetzen.", "Startwert 0 statt erstem Wert — im Juli findet man so keinen kältesten Tag."),
    ("zustand", "Zustand verfolgen", "denken", 4, 'Muster 3: Zustand verfolgen', 1, 0, "Laufende Serie und längste Serie getrennt merken. Längste Frostperiode 2024: 25 Tage.", None),
    ("while", "while", "denken", 4, 'while: Wiederholen, solange ...', 1, 1, "Wiederholt, solange eine Bedingung gilt.", None),
    ("endlos", "Endlosschleife", "denken", 4, 'while: Wiederholen, solange ...', 2, 0, "Wird die Bedingung nie falsch, endet while nie — die Terminierung aus VL 01.", None),
    ("funktion", "Funktion", "denken", 7, 'Eine Funktion definieren', 1, 0, "Benannter, wiederverwendbarer Block: def ist_frosttag(minimum).", "„def führt die Funktion aus.“"),
    ("parameter", "Parameter & Argument", "denken", 7, 'Parameter und Rückgabewert', 2, 0, "Beim Aufruf wird der Wert übergeben, nicht der Name.", "„Der übergebene Wert muss so heißen wie der Parameter.“"),
    ("return", "return", "denken", 7, 'Parameter und Rückgabewert', 1, 1, "Gibt ein Ergebnis an den Aufrufer zurück; danach endet die Funktion.", "„print gibt etwas zurück.“"),
    ("lokal", "lokale Variable", "denken", 7, 'Lokale Variablen', 2, 0, "Variablen in einer Funktion existieren nur während des Aufrufs.", "„Lokale Variablen gibt es auch nach dem Aufruf.“"),
    ("mehrrueck", "mehrere Rückgabewerte", "denken", 7, 'Mehrere Rückgabewerte', 2, 0, "jahr, maximum, minimum = zerlege_zeile(zeile) — die Reihenfolge muss stimmen.", None),
    ("assert", "assert", "denken", 7, 'Funktionen prüfen', 2, 1, "Prüft eine Funktion an den Grenzen: genau 0,0 °C, knapp darunter, Fehlwert.", None),
    ("modul", "Modul / import", "denken", 9, 'Ein eigenes Modul', 1, 0, "Eine Python-Datei, deren Funktionen andere Programme nutzen: import dwd.", "„import holt nur die Funktionen.“"),
    ("namemain", "__name__", "denken", 9, 'Typische Fehlvorstellung: import kopiert nur Funktionen', 2, 1, "if __name__ == \"__main__\": — Testcode, der beim Import nicht läuft.", None),
    ("stdlib", "Standardbibliothek", "denken", 9, 'Die Standardbibliothek', 1, 0, "Module, die Python mitbringt: statistics, datetime, math, os.", None),
    ("datetime", "datetime", "denken", 9, 'Die Standardbibliothek', 2, 1, "Aus \"19101210\" wird ein Datum, mit dem man rechnen kann — die Lücke umfasst 1756 Tage.", "„Ein Datum ist eine Zahl.“ 19110101 - 19101231 ergibt 8870."),
    ("pip", "Pakete & pip", "denken", 9, 'Externe Pakete', 2, 0, "Externe Pakete installiert man mit pip install; fehlt eines: ModuleNotFoundError.", None),
    ("zellen", "Zellen in VS Code", "denken", 10, 'Zellen in Visual Studio Code', 2, 0, "Mit # %% markierte Abschnitte einzeln ausführen, Diagramme im interaktiven Fenster — die Datei bleibt ein normales Skript.", None),

    # --- Datentypen & -strukturen
    ("dezimalpunkt", "Dezimalpunkt", "typen", 2, 'Rechnen', 2, 0, "Python schreibt 6.26. print(6,26 + 1) gibt ohne Fehlermeldung 6 27 aus.", "„6,26 ist eine Zahl.“"),
    ("typ", "Datentyp", "typen", 2, 'Datentypen', 1, 0, "int, float, str, bool — der Typ bestimmt, was man mit einem Wert tun kann.", "„Was wie eine Zahl aussieht, ist eine Zahl.“"),
    ("umwandlung", "Typumwandlung", "typen", 2, 'Text ist nicht Zahl', 1, 0, "float(\"-14.1\"), int(\"1890\"), str(1213) — nötig, weil aus Dateien immer Text kommt.", "float(\"6,26\") scheitert."),
    ("text", "Text (str)", "typen", 2, 'Mit Text arbeiten', 2, 0, "Zusammensetzen, len, Zeichen herausschneiden: datum[0:4] ist das Jahr.", None),
    ("round", "round", "typen", 4, 'while: Wiederholen, solange ...', 2, 1, "Rundet für die Ausgabe: round(mittel, 2).", None),
    ("float", "Gleitkommazahl", "typen", 4, 'Typische Fehlvorstellung: Kommazahlen sind exakt', 1, 0, "Kommazahlen werden binär gespeichert und sind nicht exakt: 0.1 + 0.2 == 0.3 ist False.", "„Kommazahlen sind exakt.“"),
    ("liste", "Liste", "typen", 5, 'Listen anlegen und füllen', 1, 0, "Mehrere Werte in fester Reihenfolge.", None),
    ("append", "append", "typen", 5, 'Listen anlegen und füllen', 2, 1, "Hängt einen Wert an — das Sammelmuster.", None),
    ("index", "Index & Slice", "typen", 5, 'Zugriff über den Index', 1, 0, "liste[0] erster, liste[-1] letzter Wert, liste[2:5] die Indizes 2 bis 4.", None),
    ("indexerror", "IndexError", "typen", 5, 'Zugriff über den Index', 2, 1, "Zugriff außerhalb der Liste — der häufigste Listenfehler.", None),
    ("range", "range", "typen", 5, 'Zahlenfolgen mit range', 1, 1, "Folge ganzer Zahlen, z. B. range(2015, 2025). Der Endwert ist nicht enthalten.", "„range ist eine Liste.“"),
    ("parallel", "zusammengehörige Listen", "typen", 5, 'Zusammengehörige Werte', 2, 0, "daten[i] und maxima[i] gehören zum selben Tag.", "„bester enthält die höchste Temperatur“ — es ist ein Index."),
    ("textvergleich", "Text vergleichen", "typen", 5, 'Typische Fehlvorstellung: Zahlen als Text vergleichen', 2, 0, "Texte werden Zeichen für Zeichen verglichen.", "„\"9.5\" > \"28.1\" ist falsch.“ Es ist wahr."),
    ("dict", "Dictionary", "typen", 6, 'Das Dictionary', 1, 0, "Ordnet Schlüsseln Werte zu: {\"1947\": 119}. Ein Durchlauf, ein Eintrag pro Jahr.", None),
    ("keyerror", "KeyError, in, get", "typen", 6, 'Das Dictionary', 2, 0, "Nach einem fehlenden Schlüssel kann man nicht fragen; vorher mit in prüfen oder get verwenden.", None),
    ("typbilanz", "Zwischenbilanz Datentypen", "typen", 6, 'Zwischenbilanz: Datentypen', 2, 0, "int, float, str, bool, list, range, dict — mit Herkunft im Datensatz und typischer Falle.", None),
    ("none", "None", "typen", 7, 'Typische Fehlvorstellung: print gibt etwas zurück', 2, 1, "Der Wert „nichts“ — Rückgabe einer Funktion ohne return.", None),
    ("array", "NumPy-Array", "typen", 10, 'NumPy-Arrays', 1, 0, "Rechnet elementweise: (minima < 0).sum() ersetzt das Zählmuster.", "„Ein Array ist dasselbe wie eine Liste.“"),
    ("maske", "Maske", "typen", 10, 'Zählen und Filtern mit Masken', 1, 0, "Ein Vergleich mit einem Array liefert True/False pro Wert: (minima < 0).sum() zählt, minima[minima < 0] filtert.", None),
    ("maskenlogik", "& statt and", "typen", 10, 'Versuch 1', 2, 1, "Masken verknüpft man elementweise mit & und |, jeweils mit Klammern.", "„and funktioniert auch mit Arrays.“ — ValueError: truth value … is ambiguous."),
    ("dataframe", "DataFrame", "typen", 11, 'Der DataFrame', 1, 0, "Tabelle aus beschrifteten Spalten; jede Spalte verhält sich wie ein Array.", None),
    ("nan", "NaN", "typen", 11, 'Fehlende Werte: NaN', 1, 1, "So stellt pandas „kein Wert“ dar, z. B. aus -999 per na_values.", "„NaN ist null.“"),
    ("datumstyp", "Datumsspalte", "typen", 11, 'Datum', 2, 0, "MESS_DATUM mit pd.to_datetime in ein Datum umwandeln.", None),

    # --- Daten & Dateien
    ("werkzeug", "Erst von Hand, dann mit Werkzeug", "daten", 0, 'Erst mühsam, dann mit Werkzeug', 2, 0, "Dieselbe Frage zweimal: mit rund 50 eigenen Zeilen und mit einer Anweisung aus einer Bibliothek. Wer den mühsamen Weg kennt, weiß, was das Werkzeug abnimmt.", None),
    ("dwd", "DWD-Datensatz", "daten", 1, 'Unsere Datensätze', 1, 0, "Klimareihe Fichtelberg seit 1890, rund 48.000 Zeilen — der rote Faden.", None),
    ("tabkalk", "Tabellenkalkulation", "daten", 1, 'Drei Aufgaben', 1, 0, "Drei Aufgaben: leicht, mühsam, praktisch aussichtslos.", None),
    ("versionen", "Versionsverwaltung", "daten", 1, 'Tabellenkalkulation und Skript im Vergleich', 2, 0, "Hebt jeden Stand einer Datei auf, mit Datum und Grund der Änderung. Bei Skripten sieht man genau, welche Zeile sich geändert hat.", None),
    ("rohformat", "Rohformat", "daten", 1, 'Aufgabe 3: 135 Jahre Frost', 2, 0, "Semikolons, Leerzeichen, Datum ohne Trennzeichen, Dezimalpunkt, eor-Spalte.", None),
    ("fehlwert", "Fehlwert -999", "daten", 3, 'Bedingungen verknüpfen', 1, 1, "So kennzeichnet der DWD „nicht gemessen“. -999 < 0 ist wahr — und trotzdem kein Frosttag.", None),
    ("openurl", "open_url", "daten", 3, 'Die Antwort auf die Leitfrage', 2, 1, "Holt eine Datei aus dem Repository in den Browser — funktioniert nur dort.", None),
    ("open", "Datei öffnen", "daten", 6, 'Eine Datei öffnen', 1, 0, "with open(dateiname) as datei: — Zeile für Zeile, jede als Text.", None),
    ("strip", "readline & strip", "daten", 6, 'Eine Datei öffnen', 2, 1, "Eine Zeile lesen; Leerzeichen und Zeilenumbruch am Rand entfernen.", None),
    ("split", "split", "daten", 6, 'Eine Zeile zerlegen', 1, 1, "Zerlegt eine Zeile am Trennzeichen in eine Liste von Texten.", "„Die Zeile ist schon eine Tabelle.“"),
    ("kopfzeile", "Kopfzeile", "daten", 6, 'Kopfzeile und Fehlwerte', 2, 0, "Mit datei.readline() überspringen — sonst scheitert float an \"TXK\".", None),
    ("luecke", "Lücke", "daten", 6, 'Typische Fehlvorstellung: Jeder Tag hat eine Zeile', 1, 0, "Fehlende Tage fehlen ganz, statt als -999 zu erscheinen. Fichtelberg: 1910 bis 1915.", "„Jeder Tag hat eine Zeile.“"),
    ("schreiben", "Datei schreiben", "daten", 6, 'Ergebnisse schreiben', 1, 0, "open(..., \"w\") und datei.write — ohne automatischen Zeilenumbruch.", None),
    ("langesskript", "das lange Skript", "daten", 6, 'Live Hacking: Das lange Skript', 2, 0, "Fichtelberg und Freiberg als kopierte Blöcke — funktioniert, ist aber schwer zu ändern.", None),
    ("lueckensuche", "Lücken finden", "daten", 9, 'Die Funktion finde_luecken', 2, 0, "Mit datetime alle Stellen melden, an denen mehr als ein Tag fehlt — Chemnitz: 33 Jahre, Freiberg: ein einzelner Tag 1977.", None),
    ("pfad", "Pfad", "daten", 9, 'Typische Fehlvorstellung: Pfade', 1, 0, "Relative Pfade gelten ab dem aktuellen Arbeitsverzeichnis.", "„Ein Dateiname bezieht sich auf den Ordner des Programms.“"),
    ("loadtxt", "loadtxt", "daten", 10, 'Live Hacking: Wie viel wärmer ist es geworden?', 2, 1, "NumPy liest die Rohdatei direkt: Trennzeichen, Kopfzeile überspringen, Spalten auswählen — aber ohne Spaltennamen.", None),
    ("readcsv", "read_csv", "daten", 11, 'Von der Mühsal zum Werkzeug', 1, 1, "Liest die Rohdatei in einer Anweisung — was in VL 06 rund 50 Zeilen gekostet hat.", None),
    ("spaltenname", "Spaltennamen", "daten", 11, 'Versuch 2', 2, 0, "Jedes Zeichen zählt, auch Leerzeichen: \" TNK\" ist nicht \"TNK\". skipinitialspace=True entfernt sie.", "„Eine Spalte heißt so, wie ich sie lese.“"),
    ("vollstaendig", "vollständige Jahre", "daten", 12, 'Typische Fehlvorstellung: Jedes Jahr zählt gleich', 2, 0, "Jahre mit Lücken erkennen und ausschließen, bevor man vergleicht: 1890 hat nur 132 gemessene Tage.", "„Jede Zeile der Ergebnistabelle ist ein vergleichbares Jahr.“"),
    ("merge", "Stationen verbinden", "daten", 12, 'Zwei Stationen verbinden', 2, 0, "Fichtelberg und Chemnitz über das Datum zusammenführen.", None),
    ("stationswechsel", "Stationswechsel", "daten", 14, 'Freiberg zieht um', 1, 0, "Freiberg misst ab 2015 an anderem Ort mit anderem Gerät — gleiche Datei, andere Messung.", None),
    ("metadaten", "Metadaten", "daten", 14, 'Die Metadaten', 1, 0, "Gerät, Messtag, Betreiber, Qualitätsstufe — was die Daten selbst verschweigen.", None),
    ("referenz", "Referenzstation", "daten", 14, 'Die Referenzstation', 2, 0, "Chemnitz als Vergleich: Verhältnis Freiberg/Chemnitz 1,13 (1976–1987), 0,95 (2016–2025) — bei gleichbleibendem Chemnitzer Niederschlag.", None),
    ("inhomogen", "Inhomogenität", "daten", 14, 'Typische Fehlvorstellung: Gleiche Station, gleiche Messung', 2, 0, "Ein Bruch in einer Messreihe durch Ortswechsel, Gerätewechsel oder geänderte Messvorschrift — in den Daten selbst unsichtbar.", "„Dieselbe Stationsnummer und dasselbe Dateiformat bedeuten dieselbe Messung.“"),

    # --- Analyse & Darstellung
    ("kreislauf", "Datenkreislauf", "analyse", 0, 'Warum ist die Veranstaltung zentral?', 2, 0, "Frage, Erhebung, Aufbereitung, Analyse, Visualisierung, Dokumentation — meist mehrere Runden.", None),
    ("schliff", "Bildverarbeitung", "analyse", 0, 'Praktische Inhalte', 2, 0, "Ausblick: Ein Bild ist eine Tabelle aus Helligkeitswerten. Schwelle setzen, zusammenhängende Flecken zählen, Größen messen.", "„Das Programm erkennt, was im Bild ist.“ Es erkennt nur, was heller ist als die Schwelle."),
    ("lohnt", "Programm oder Tabelle?", "analyse", 1, 'Wann lohnt sich ein Programm?', 1, 0, "Viele Daten, sperrige Formate, Wiederholung, Nachvollziehbarkeit: dann lohnt ein Programm.", None),
    ("kenntage", "Frost-, Eis-, Sommertag", "analyse", 3, 'Mehrere Fälle: elif', 2, 0, "DWD-Kenntage: Frosttag = Minimum unter 0 °C, Eistag = Maximum unter 0 °C, Sommertag = Maximum ab 25 °C.", None),
    ("mittel", "Mittelwert", "analyse", 4, 'Mittelwert mit Fehlwerten', 1, 0, "Summe durch Anzahl — nur über gültige Werte, und die Anzahl gehört dazu.", "„Ein Mittelwert gilt, egal wie viele Werte fehlen.“"),
    ("hochrechnung", "Hochrechnung", "analyse", 4, 'while: Wiederholen, solange ...', 2, 0, "Bei +0,05 °C pro Jahr läge das Mittel 2059 bei 8 °C — nur unter dieser Annahme.", "„Rechnerisch korrekt heißt inhaltlich richtig.“"),
    ("statistik", "statistics", "analyse", 9, 'Die Standardbibliothek', 2, 1, "mean, median, stdev für Listen von Messwerten.", None),
    ("notebook", "Jupyter Notebook lesen", "analyse", 10, 'Exkurs: Jupyter Notebooks lesen', 2, 0, "Verbreitetes Format in Wissenschaft und Projekten; in der Vorlesung nur zum Lesen vorgestellt, nicht als Werkzeug.", "„Was im Notebook steht, ist das, was gerechnet wurde.“"),
    ("vektor", "elementweise rechnen", "analyse", 10, 'NumPy-Arrays', 2, 0, "Eine Anweisung für alle Werte statt einer Schleife: minima.mean().", None),
    ("filter", "Filtern", "analyse", 11, 'Auswählen und Filtern', 1, 0, "df[df[\"TNK\"] < 0] — Zeilen nach einer Bedingung auswählen.", None),
    ("idxmin", "idxmin & loc", "analyse", 11, 'Versuch 4', 2, 1, "Zeile des kleinsten Werts finden und einzelne Werte über Zeile und Spaltenname holen.", None),
    ("groupby", "groupby", "analyse", 12, 'groupby: Teilen, Anwenden, Zusammenfügen', 1, 1, "Gruppiert Zeilen, z. B. nach Jahr, und fasst jede Gruppe zusammen.", None),
    ("summemittel", "Mittel statt Summe", "analyse", 12, 'Versuch 2', 2, 0, "Gruppen mit unterschiedlich vielen Elementen vergleicht man über das Mittel, nicht die Summe — die 2020er haben erst sechs Jahre.", None),
    ("inversion", "Inversionswetterlage", "analyse", 12, 'Zwei Stationen verbinden', 2, 0, "Im Mittel ist Chemnitz 5 °C wärmer als der Fichtelberg — am 12.01.1964 war der Gipfel 11,9 °C wärmer. Mittelwerte verdecken Extreme.", None),
    ("diagrammform", "Diagrammform", "analyse", 13, 'Die richtige Form', 2, 0, "Zeitreihe als Linie, Vergleich als Balken, Verteilung als Histogramm.", None),
    ("diagramm", "Diagramm", "analyse", 13, 'Ein Diagramm bauen', 1, 0, "Achsen, Einheiten, Titel — ein Diagramm muss ohne Begleittext lesbar sein.", None),
    ("trend", "Trend", "analyse", 13, 'Trend', 1, 0, "Lineare Trendlinie — die Herleitung der 0,05 °C pro Jahr aus VL 04.", "„Die Daten haben einen Trend.“ Ab 1891: 0,15 °C, ab 1975: 0,50 °C, ab 2010: 1,18 °C pro Jahrzehnt — der Zeitraum gehört immer dazu."),
    ("irref", "Irreführende Darstellung", "analyse", 13, 'Irreführende Darstellungen', 1, 0, "Balkenachse nicht ab null, ausgewählte Zeiträume, überbrückte Lücken, fehlende Einheit oder Quelle.", None),
    ("glatt", "gleitendes Mittel", "analyse", 13, 'Versuch 3', 2, 0, "Jeder Wert wird durch das Mittel der umliegenden Jahre ersetzt — Ausreißer mitteln sich heraus, der langfristige Verlauf bleibt.", None),
    ("diagrammluecke", "Lücken im Diagramm", "analyse", 13, 'Versuch 2', 2, 0, "Eine Linie verbindet Punkte auch über fehlende Jahre hinweg; reindex setzt NaN ein und unterbricht sie.", "„Eine durchgehende Linie zeigt durchgehende Daten.“"),
    ("qualitaet", "Datenqualität", "analyse", 14, 'Kann ich meinem Ergebnis trauen?', 1, 0, "Sechs Prüffragen: Fehlwerte, fehlende Zeilen, Zahl der Werte, vergleichbare Gruppen, Messänderungen, ehrliche Grafik.", None),
    ("reproduzierbar", "Reproduzierbarkeit", "analyse", 14, 'Reproduzierbarkeit', 2, 0, "Kann ich meine eigene Rechnung wiederholen? Skript statt Handarbeit.", None),
    ("pruefung", "Prüfungsvorbereitung", "analyse", 14, 'Prüfungsvorbereitung', 2, 0, "Musteraufgaben zu allen Aufgabentypen aus VL 00.", None),
]

# ---- Beziehungen: von, nach, Beschriftung
R = [
    # Einstieg
    ("vorhersage", "annahmen", "deckt auf"), ("ki", "vorhersage", "Antwort prüfen durch"), ("ki", "annahmen", "trifft eigene"),
    ("vorhersage", "trace", "geübt mit"), ("werkzeug", "open", "von Hand:"), ("werkzeug", "readcsv", "mit Werkzeug:"),
    ("zaehler", "sensorlog", "erzeugt"), ("zaehler", "annahmen", "beruht auf"), ("sensorlog", "tabkalk", "ausgewertet mit"),
    ("kreislauf", "lohnt", "je Runde die Frage"), ("schliff", "array", "Bild ist ein"), ("schliff", "maske", "Schwelle ergibt eine"), ("tabkalk", "lohnt", "Grenzen zeigen"), ("dwd", "rohformat", "liegt vor im"),
    ("tabkalk", "algo", "motiviert"), ("algo", "terminierung", "erfordert"), ("algo", "pseudo", "notiert als"),
    ("pseudo", "ablauf", "oder als"), ("algo", "sprache", "formuliert in"),
    ("algo", "bausteine", "besteht aus"), ("bausteine", "if", "Verzweigung wird zu"), ("bausteine", "for", "Wiederholung wird zu"),
    ("pseudo", "protokoll", "geprüft mit"), ("protokoll", "trace", "in Python:"), ("tabkalk", "eingabe", "rechnet"),
    ("eingabe", "variable", "anders als eine Formel:"), ("tabkalk", "versionen", "fehlt der"), ("versionen", "reproduzierbar", "unterstützt"), ("blockly", "print", "gleiches Programm wie"),
    # VL 02
    ("pseudo", "vierfragen", "entsteht mit"), ("tabkalk", "zeitwert", "Hürde in Aufgabe 2:"), ("zeitwert", "typ", "Beispiel für"), ("zeitwert", "datetime", "in Python:"), ("vierfragen", "variable", "was ich mir merke, wird zur"),
    ("sprache", "interpreter", "ausgeführt vom"), ("interpreter", "fehlermeldung", "meldet"), ("variable", "zuweisung", "entsteht durch"),
    ("variable", "namen", "braucht"), ("variable", "print", "ausgegeben mit"), ("zuweisung", "trace", "nachvollziehen mit"),
    ("operatoren", "zuweisung", "rechts vom ="), ("dezimalpunkt", "operatoren", "Voraussetzung für"), ("variable", "typ", "hat einen"),
    ("typ", "umwandlung", "ändern durch"), ("typ", "text", "z. B."), ("umwandlung", "fehlermeldung", "ValueError bei"),
    ("typ", "vergleich", "bool ist ein"), ("kommentar", "variable", "erklärt"),
    # VL 03
    ("pseudo", "if", "wird zu"), ("pseudo", "for", "wird zu"), ("vergleich", "if", "steuert"), ("if", "einrueckung", "Block per"),
    ("if", "else", "ergänzt durch"), ("else", "elif", "erweitert zu"), ("vergleich", "logik", "verknüpft mit"),
    ("elif", "kenntage", "unterscheidet"), ("for", "einrueckung", "Block per"), ("if", "zaehlmuster", "Teil von"),
    ("for", "zaehlmuster", "Teil von"), ("for", "schleifenvar", "belegt"), ("zaehlmuster", "trace", "nachvollziehen mit"),
    ("dwd", "fehlwert", "enthält"), ("fehlwert", "logik", "ausschließen mit"), ("openurl", "uebertragbar", "Ausnahme von"),
    # VL 04
    ("zaehlmuster", "summe", "verallgemeinert zu"), ("zaehlmuster", "extrem", "verallgemeinert zu"), ("summe", "mittel", "liefert"),
    ("fehlwert", "mittel", "verfälscht"), ("extrem", "zustand", "steckt in"), ("for", "while", "Alternative"),
    ("while", "endlos", "Gefahr"), ("terminierung", "endlos", "verletzt durch"), ("while", "hochrechnung", "berechnet"),
    ("float", "round", "ausgeben mit"), ("float", "vergleich", "kein == bei"),
    # VL 05
    ("liste", "for", "durchlaufen von"), ("liste", "append", "wächst mit"), ("zaehlmuster", "append", "Sammelmuster statt Zähler"),
    ("liste", "index", "Zugriff per"), ("text", "index", "gleiche Schreibweise"), ("index", "indexerror", "außerhalb:"),
    ("index", "range", "gültige Indizes"), ("range", "parallel", "durchläuft"), ("index", "parallel", "verbindet"),
    ("split", "textvergleich", "liefert Text für"), ("textvergleich", "umwandlung", "vermeiden durch"), ("liste", "dict", "Schlüssel statt Position"),
    # VL 06
    ("openurl", "open", "ersetzt durch"), ("open", "strip", "mit"), ("open", "split", "Zeile zerlegen mit"),
    ("split", "liste", "liefert eine"), ("split", "umwandlung", "liefert Text für"), ("open", "kopfzeile", "überspringt"),
    ("dwd", "luecke", "enthält"), ("dict", "keyerror", "Falle"), ("dict", "luecke", "fehlender Eintrag bei"),
    ("open", "schreiben", "Gegenstück"), ("schreiben", "tabkalk", "öffnen in"), ("open", "langesskript", "Teil von"),
    ("dict", "typbilanz", "vervollständigt"),
    # VL 07
    ("langesskript", "funktion", "zerlegt in"), ("funktion", "parameter", "hat"), ("funktion", "return", "liefert mit"),
    ("return", "none", "ohne return:"), ("funktion", "lokal", "hat"), ("return", "mehrrueck", "auch"),
    ("funktion", "assert", "geprüft mit"), ("kenntage", "funktion", "z. B. ist_frosttag"),
    # VL 08
    ("zaehler", "micropy", "z. B. mit"), ("micropy", "while", "while True"), ("micropy", "sensor", "steuert"),
    ("sensor", "seriell", "sendet über"), ("sensor", "messfehler", "Risiko"), ("annahmen", "messfehler", "verletzt ergibt"),
    ("seriell", "zeitstempel", "erhält"), ("seriell", "messdatei", "mitgeschrieben als"),
    # VL 09
    ("funktion", "modul", "wandert in"), ("modul", "namemain", "Testcode unter"), ("modul", "stdlib", "gleiches Prinzip"),
    ("stdlib", "datetime", "enthält"), ("stdlib", "statistik", "enthält"), ("datetime", "lueckensuche", "ermöglicht"), ("luecke", "lueckensuche", "systematisch:"), ("lueckensuche", "vollstaendig", "Grundlage für"),
    ("mittel", "statistik", "fertig in"), ("modul", "pip", "externe per"), ("pfad", "open", "entscheidet über"),
    # Phase 2
    ("pip", "array", "installiert"), ("zellen", "notebook", "ähnlich, aber ohne versteckten Zustand:"), ("modul", "array", "import wie"),
    ("liste", "array", "wird zu"), ("array", "maske", "Vergleich liefert"), ("logik", "maskenlogik", "für Arrays:"), ("maske", "maskenlogik", "verknüpft mit"), ("maske", "filter", "gleiche Idee in pandas"), ("fehlwert", "maske", "ausschließen mit"), ("open", "loadtxt", "in einer Anweisung:"), ("loadtxt", "readcsv", "mit Spaltennamen:"), ("readcsv", "spaltenname", "Falle"), ("extrem", "idxmin", "in pandas:"), ("dataframe", "idxmin", "nutzt"), ("zaehlmuster", "vektor", "ersetzt durch"), ("array", "vektor", "ermöglicht"),
    ("array", "dataframe", "Spalte ist ein"), ("open", "readcsv", "in einer Anweisung"), ("zellen", "readcsv", "Arbeitsweise für"),
    ("readcsv", "dataframe", "erzeugt"), ("fehlwert", "nan", "wird zu"), ("none", "nan", "ähnlich:"),
    ("datetime", "datumstyp", "in pandas:"), ("dataframe", "filter", "auswählen mit"), ("dict", "groupby", "Prinzip hinter"),
    ("tabkalk", "groupby", "Aufgabe 3 gelöst mit"), ("luecke", "vollstaendig", "prüfen auf"), ("groupby", "vollstaendig", "nur über"),
    ("vollstaendig", "merge", "dann"), ("groupby", "summemittel", "Falle"), ("merge", "inversion", "zeigt"), ("mittel", "summemittel", "statt Summe:"), ("diagrammform", "diagramm", "bestimmt"), ("groupby", "diagramm", "Ergebnis als"),
    ("diagramm", "trend", "zeigt"), ("hochrechnung", "trend", "Grundlage"), ("trend", "irref", "Gefahr"), ("diagramm", "glatt", "ergänzt durch"), ("luecke", "diagrammluecke", "im Diagramm:"), ("diagrammluecke", "irref", "Beispiel für"),
    ("merge", "referenz", "Grundlage für"), ("stationswechsel", "metadaten", "belegt durch"), ("referenz", "stationswechsel", "entlarvt"), ("stationswechsel", "inhomogen", "erzeugt"), ("inhomogen", "referenz", "erkennbar mit"),
    ("stationswechsel", "qualitaet", "Beispiel für"), ("luecke", "qualitaet", "prüfen"), ("nan", "qualitaet", "zählen, nicht ignorieren"),
    ("messfehler", "qualitaet", "Ursache für"), ("messdatei", "readcsv", "eingelesen mit"), ("notebook", "reproduzierbar", "Gefahr für"), ("reproduzierbar", "qualitaet", "Teil von"), ("trace", "pruefung", "Aufgabentyp"),
]

# ---- Anwendungen: konkrete Fragen an echte Daten, die Schlagworte nutzen
# id, Titel, Fach, VL, Abschnittstitel, Datensatz, [Schlagwort-ids], Herkunft
A = [
    ("a_tuer", "Personenzähler an der Hörsaaltür", "Messtechnik", 0, 'Praktische Inhalte',
     "Zählungen des Alvik-Roboters (zaehlungen_JJJJ-MM-TT.csv)", ["zaehler", "annahmen"], "lehrende"),
    ("a_schliff", "Körner im Dünnschliff", "Geologie", 0, 'Praktische Inhalte',
     "Mikroskopbild einer hauchdünn geschliffenen Gesteinsscheibe, durch zwei gekreuzte Lichtfilter (Polarisationsfilter) betrachtet, sodass die Mineralkörner hell oder farbig leuchten. Bild aus der Lehrsammlung von Prof. Heide, TU Bergakademie Freiberg", ["schliff", "annahmen"], "lehrende"),
    ("a_frost_bloecke", "Frosttage einer Januarwoche, als Blöcke und als Python", "Klima", 0, 'Blöcke oder Text',
     "Tiefsttemperaturen Fichtelberg", ["blockly"], "lehrende"),
]

# ---- Didaktische Fäden (Metrolinien): jede Folge ist eine Kette von „baut auf“-Schritten
F = [
    ("wiederverwenden", "Nicht alles neu schreiben", "Einmal gelösten Code wiederverwenden: erst als Muster, dann als eigene Funktion, als eigene Datei und schließlich als fertiges Paket von anderen.",
     ["pseudo", "zaehlmuster", "langesskript", "funktion", "modul", "pip", "array"]),
    ("struktur", "Viele Werte aufbewahren", "Vom einzelnen Wert über die Liste und das Nachschlagen per Schlüssel bis zur Tabelle mit benannten Spalten.",
     ["variable", "liste", "index", "dict", "array", "dataframe"]),
    ("zaehlen", "Vom Zählen zur Zusammenfassung", "Wie aus einer Schleife, die von Hand mitzählt, am Ende eine einzige Zeile wird, die Werte pro Jahr zusammenfasst.",
     ["zaehlmuster", "summe", "mittel", "dict", "vektor", "groupby", "diagramm"]),
    ("fehlwert", "Wenn ein Wert fehlt", "„Nicht gemessen“ sieht jedes Mal anders aus: als -999, als fehlende Zeile, als NaN. Und jedes Mal muss man es behandeln.",
     ["dwd", "fehlwert", "logik", "mittel", "luecke", "nan", "vollstaendig", "qualitaet"]),
    ("tabelle", "Vom Text zur Tabelle", "Eine Datei ist zunächst nur Text. Wie daraus eine Tabelle mit Spalten und Zahlen wird.",
     ["dwd", "text", "umwandlung", "open", "split", "readcsv", "dataframe"]),
    ("messung", "Kann ich den Daten trauen?", "Wie Messdaten entstehen und warum man ihnen nicht blind trauen darf.",
     ["zaehler", "sensorlog", "sensor", "messfehler", "messdatei", "readcsv", "stationswechsel", "qualitaet"]),
]

KURS = {
    "titel": "Erhebung, Analyse und Visualisierung digitaler Daten",
    "name": "TU Bergakademie Freiberg · Wintersemester 2026/27",
    "hochschule": "TU Bergakademie Freiberg",
    # Entwurf – vom Dozenten durchzusehen
    "beschreibung": "Daten erheben, mit Python auswerten und anschaulich darstellen – vom ersten Programm über Dateien und Funktionen bis zur Analyse mit NumPy und pandas.",
    "basis": "https://liascript.github.io/course/?https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/",
    "pages": "https://tubaf-ifi-liascript.github.io/VL_EAVD/",
    "repo": "https://github.com/TUBAF-IfI-LiaScript/VL_EAVD",
    "speicher": "eavd-map",
    "autoren": "Sebastian Zug, Ines Aubeln & Claude Code (Opus 5.5)",
    "feedback": 'Begriff fehlt oder ist unklar? Sagen Sie es in der Abfrage am Ende jeder Vorlesung oder im OPAL-Forum. <a href="https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/issues/new?title=Kurslandkarte%3A%20&amp;labels=kurslandkarte" target="_blank" rel="noopener">GitHub ↗</a>',
    "status": {"ausgearbeitet": "", "Rumpf": "Rumpf"},
    "anwendung_daten": "Daten", "start_ansicht": "liste",
    "kontakt": 'Prof. Dr.-Ing. Sebastian Zug<br>Lehrstuhl für Softwaretechnologie und Robotik, TU Bergakademie Freiberg<br><a href="mailto:sebastian.zug@informatik.tu-freiberg.de">sebastian.zug@informatik.tu-freiberg.de</a>',
}

# ---- Blöcke (Hintergrund der Karte, Überschriften im Raster) und Themengebiete
BLOECKE = {1: ("Einstieg", "ph1"), 2: ("Grundlagen am Datensatz", "ph2"), 3: ("Zäsur", "ph3"),
           4: ("Grundlagen", "ph2"), 5: ("Datenanalyse", "ph4")}
BLOCK_VON = {0: 1, 3: 2, 8: 3, 9: 4, 10: 5}   # erste Vorlesung eines Blocks
LINIEN = [
    ("denken", "Programme & Abläufe", "c1"), ("typen", "Werte & Sammlungen", "c2"),
    ("daten", "Daten & Dateien", "c3"), ("erhebung", "Daten erheben", "c4"),
    ("analyse", "Auswerten & Darstellen", "c5"),
]

T, blk = [], 1
for v in range(ANZAHL):
    blk = BLOCK_VON.get(v, blk)
    T.append((v, f"VL {v:02d}", TERMINE[v][0], TERMINE[v][1], DATEIEN[v], STATUS[v], blk))

kern.erzeuge(
    repo=REPO, kurs=KURS, termine=T, bloecke=BLOECKE, linien=LINIEN,
    begriffe=B, beziehungen=R, faeden=F, anwendungen=A, leitfragen=LEITFRAGE, freigegeben=FREIGEGEBEN,
    karte="docs/kurslandkarte", startseite="docs/index.html", vorschau="keine", pdf_ordner="docs/pdf", pdf_termine=FREIGEGEBEN | PDF_VORAB,
)
