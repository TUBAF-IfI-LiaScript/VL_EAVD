"""Kurslandkarte: Daten und Seite erzeugen.

Abschnitte (Foliennummern) werden automatisch aus den Vorlesungen gelesen,
Begriffe, Beziehungen und didaktische Fäden sind unten kuratiert.

Aufruf aus dem Repository-Wurzelverzeichnis:

    python3 kurslandkarte/erzeuge.py

Schreibt docs/kurslandkarte/kurslandkarte.json und docs/kurslandkarte/index.html.
"""
import datetime, json, re, glob, os

HIER = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HIER)
ZIEL = os.path.join(REPO, "docs", "kurslandkarte")
STAND = datetime.date.today().strftime("%d.%m.%Y")

# ---- Abschnitte automatisch (LiaScript-Foliennummer = Position der Überschrift)
sections = {}
for f in sorted(glob.glob(os.path.join(REPO, "[01][0-9]_*.md"))):
    vl = int(os.path.basename(f)[:2])
    s = open(f, encoding="utf-8").read()
    s = s[s.find("-->") + 3:]
    s = re.sub(r"^(`{3,4}).*?\n.*?\n\1", "", s, flags=re.S | re.M)
    heads = [m.group(2).strip().replace("`", "") for m in re.finditer(r"^(#{1,6}) +(.+)$", s, re.M)]
    sections[vl] = {"datei": os.path.basename(f), "abschnitte": heads}

STATUS = {v: "ausgearbeitet" for v in range(15)}
STATUS[8] = "Rumpf"
for v in range(10, 15):
    STATUS[v] = "Gerüst"

# ---- Begriffe: id, Name, Linie, VL, Abschnitt, Ebene, Code?, Erklärung, Fehlvorstellung
B = [
    # --- Erhebung
    ("zaehler", "Personenzähler", "erhebung", 0, 2, 1, 0, "Ein Ultraschallsensor an der Hörsaaltür zählt Eintretende — das Einstiegsbeispiel mit echten Messdaten.", None),
    ("annahmen", "Annahmen im Messprogramm", "erhebung", 0, 16, 2, 0, "Messbereich, Entprellzeit, fehlender Richtungssinn: Was im Code steht, bestimmt, was gezählt wird.", "„Es funktioniert, also zählt es richtig.“"),
    ("sensorlog", "Sensorprotokoll", "erhebung", 1, 5, 2, 0, "Die Textzeilen des Personenzählers — mühsam in der Tabellenkalkulation auszuwerten (Aufgabe 2).", None),
    ("micropy", "MicroPython", "erhebung", 8, 3, 1, 0, "Python auf dem Mikrocontroller — dieselbe Sprache, andere Hardware.", None),
    ("sensor", "Sensor", "erhebung", 8, 3, 1, 0, "Wandelt eine physikalische Größe in eine Zahl um — mit Genauigkeit, Messort und Ausfallrisiko.", None),
    ("seriell", "serielle Ausgabe", "erhebung", 8, 4, 2, 0, "Der Mikrocontroller schickt Messwerte als Textzeilen an den Rechner, dort werden sie mitgeschrieben.", None),
    ("messfehler", "Messfehler", "erhebung", 8, 5, 1, 0, "Annahmen im Messprogramm werden verletzt — sichtbar im Datenstrom, aber ohne Fehlermeldung.", "„Ein Sensor misst, was draufsteht.“"),
    ("zeitstempel", "Zeitstempel", "erhebung", 8, 5, 2, 0, "Entsteht beim Empfang oder Schreiben — nicht unbedingt im Moment des Ereignisses.", "„Ein Zeitstempel ist die Zeit des Ereignisses.“"),
    ("messdatei", "eigene Messdatei", "erhebung", 8, 6, 2, 0, "Die in der Demonstration aufgezeichneten Daten kommen im Januar als Analysebeispiel zurück.", None),

    # --- Denken & Kontrollfluss
    ("blockly", "Blöcke oder Text", "denken", 0, 9, 2, 0, "Zwei Ansichten auf dasselbe Programm: Blöcke zusammenschieben oder Python tippen.", None),
    ("algo", "Algorithmus", "denken", 1, 8, 1, 0, "Eindeutige, ausführbare Handlungsvorschrift aus endlich vielen Schritten.", None),
    ("terminierung", "Eindeutigkeit & Terminierung", "denken", 1, 8, 2, 0, "Jeder Schritt hat genau eine Auslegung; die Ausführung endet nach endlich vielen Schritten.", None),
    ("sprache", "Programmiersprache", "denken", 1, 9, 2, 0, "Kompromiss zwischen menschlicher Lesbarkeit und maschineller Eindeutigkeit.", "„Der Rechner versteht, was ich meine.“"),
    ("pseudo", "Pseudocode", "denken", 1, 10, 1, 0, "Algorithmus in strukturierter Alltagssprache, bevor man ihn programmiert.", None),
    ("ablauf", "Ablaufdiagramm", "denken", 1, 10, 2, 0, "Grafische Form eines Algorithmus mit Entscheidungen und Rücksprüngen.", None),
    ("interpreter", "Interpreter", "denken", 2, 3, 2, 0, "Liest das Programm Zeile für Zeile, führt aus — oder bricht mit einer Fehlermeldung ab.", None),
    ("print", "print", "denken", 2, 5, 1, 1, "Gibt Werte auf dem Bildschirm aus.", None),
    ("operatoren", "Rechenoperatoren", "denken", 2, 6, 2, 0, "+ - * / sowie // (ganzzahlig), % (Rest), ** (Potenz). 18900801 // 10000 ergibt das Jahr.", None),
    ("variable", "Variable", "denken", 2, 7, 1, 0, "Ein Name, unter dem sich ein Programm einen Wert merkt.", "„Eine Variable merkt sich die Rechnung — wie eine Formel in der Tabellenkalkulation.“"),
    ("zuweisung", "Zuweisung =", "denken", 2, 8, 1, 0, "Rechts wird gerechnet, links wird das Ergebnis abgelegt. Lies = als „wird zu“.", "„= ist eine Gleichung.“"),
    ("trace", "Programm im Kopf ausführen", "denken", 2, 8, 2, 0, "Tabelle mit einer Spalte pro Variable, eine Zeile pro Schritt — die zentrale Klausurfähigkeit.", None),
    ("namen", "Variablennamen", "denken", 2, 10, 2, 0, "Buchstaben, Ziffern, Unterstrich; nicht mit Ziffer beginnen; sprechend wählen.", "„Der Rechner versteht, was ein Name bedeutet.“"),
    ("vergleich", "Vergleich / bool", "denken", 2, 14, 1, 0, "Vergleiche wie minimum < 0 liefern True oder False.", "= weist zu, == vergleicht."),
    ("kommentar", "Kommentar", "denken", 2, 15, 2, 0, "Alles hinter # ist für Menschen. Gute Kommentare erklären das Warum.", None),
    ("fehlermeldung", "Fehlermeldung", "denken", 2, 16, 1, 0, "Von unten nach oben lesen: was (NameError, TypeError, ValueError, SyntaxError) und wo.", None),
    ("uebertragbar", "Browser = eigener Rechner", "denken", 3, 3, 2, 0, "Die Beispiele laufen eins zu eins in Visual Studio Code — einzige Ausnahme ist open_url.", None),
    ("if", "if", "denken", 3, 4, 1, 1, "Führt Anweisungen nur aus, wenn eine Bedingung gilt.", None),
    ("einrueckung", "Einrückung", "denken", 3, 5, 2, 0, "In Python ist die Einrückung die Struktur: Sie bestimmt, was zu if oder for gehört.", None),
    ("else", "else", "denken", 3, 6, 2, 1, "Genau einer von zwei Blöcken wird ausgeführt.", None),
    ("elif", "elif", "denken", 3, 7, 2, 1, "Mehrere Fälle nacheinander prüfen; der erste zutreffende gewinnt.", "Die Reihenfolge der Fälle zählt: ein spezieller Fall hinter einem allgemeinen wird nie erreicht."),
    ("logik", "and / or / not", "denken", 3, 8, 2, 1, "Bedingungen verknüpfen, z. B. minimum != -999 and minimum < 0.", None),
    ("for", "for-Schleife", "denken", 3, 9, 1, 1, "Wiederholt einen Block für jeden Wert einer Folge.", None),
    ("zaehlmuster", "Zählmuster", "denken", 3, 10, 1, 0, "Zähler vor der Schleife anlegen, in der Schleife bedingt erhöhen, danach ausgeben.", "Zähler in der Schleife anlegen: Er wird in jedem Durchlauf zurückgesetzt."),
    ("schleifenvar", "Schleifenvariable", "denken", 3, 12, 2, 0, "Bekommt in jedem Durchlauf den nächsten Wert — und behält nach der Schleife den letzten.", "„Nach der Schleife ist die Schleifenvariable weg.“"),
    ("summe", "Aufsummieren", "denken", 4, 3, 1, 0, "Summe und Anzahl in der Schleife fortschreiben.", None),
    ("extrem", "Extremwert suchen", "denken", 4, 5, 1, 0, "Den bisher besten Wert (und seine Position) merken und bei Bedarf ersetzen.", "Startwert 0 statt erstem Wert — im Juli findet man so keinen kältesten Tag."),
    ("zustand", "Zustand verfolgen", "denken", 4, 6, 1, 0, "Laufende Serie und längste Serie getrennt merken. Längste Frostperiode 2024: 25 Tage.", None),
    ("while", "while", "denken", 4, 11, 1, 1, "Wiederholt, solange eine Bedingung gilt.", None),
    ("endlos", "Endlosschleife", "denken", 4, 11, 2, 0, "Wird die Bedingung nie falsch, endet while nie — die Terminierung aus VL 01.", None),
    ("funktion", "Funktion", "denken", 7, 3, 1, 0, "Benannter, wiederverwendbarer Block: def ist_frosttag(minimum).", "„def führt die Funktion aus.“"),
    ("parameter", "Parameter & Argument", "denken", 7, 5, 2, 0, "Beim Aufruf wird der Wert übergeben, nicht der Name.", "„Der übergebene Wert muss so heißen wie der Parameter.“"),
    ("return", "return", "denken", 7, 5, 1, 1, "Gibt ein Ergebnis an den Aufrufer zurück; danach endet die Funktion.", "„print gibt etwas zurück.“"),
    ("lokal", "lokale Variable", "denken", 7, 8, 2, 0, "Variablen in einer Funktion existieren nur während des Aufrufs.", "„Lokale Variablen gibt es auch nach dem Aufruf.“"),
    ("mehrrueck", "mehrere Rückgabewerte", "denken", 7, 9, 2, 0, "jahr, maximum, minimum = zerlege_zeile(zeile) — die Reihenfolge muss stimmen.", None),
    ("assert", "assert", "denken", 7, 11, 2, 1, "Prüft eine Funktion an den Grenzen: genau 0,0 °C, knapp darunter, Fehlwert.", None),
    ("modul", "Modul / import", "denken", 9, 3, 1, 0, "Eine Python-Datei, deren Funktionen andere Programme nutzen: import dwd.", "„import holt nur die Funktionen.“"),
    ("namemain", "__name__", "denken", 9, 4, 2, 1, "if __name__ == \"__main__\": — Testcode, der beim Import nicht läuft.", None),
    ("stdlib", "Standardbibliothek", "denken", 9, 6, 1, 0, "Module, die Python mitbringt: statistics, datetime, math, os.", None),
    ("datetime", "datetime", "denken", 9, 6, 2, 1, "Aus \"19101210\" wird ein Datum, mit dem man rechnen kann — die Lücke umfasst 1756 Tage.", None),
    ("pip", "Pakete & pip", "denken", 9, 7, 2, 0, "Externe Pakete installiert man mit pip install; fehlt eines: ModuleNotFoundError.", None),
    ("zellen", "Zellen in VS Code", "denken", 10, 3, 2, 0, "Mit # %% markierte Abschnitte einzeln ausführen, Diagramme im interaktiven Fenster — die Datei bleibt ein normales Skript.", None),

    # --- Datentypen & -strukturen
    ("dezimalpunkt", "Dezimalpunkt", "typen", 2, 6, 2, 0, "Python schreibt 6.26. print(6,26 + 1) gibt ohne Fehlermeldung 6 27 aus.", "„6,26 ist eine Zahl.“"),
    ("typ", "Datentyp", "typen", 2, 11, 1, 0, "int, float, str, bool — der Typ bestimmt, was man mit einem Wert tun kann.", "„Was wie eine Zahl aussieht, ist eine Zahl.“"),
    ("umwandlung", "Typumwandlung", "typen", 2, 12, 1, 0, "float(\"-14.1\"), int(\"1890\"), str(1213) — nötig, weil aus Dateien immer Text kommt.", "float(\"6,26\") scheitert."),
    ("text", "Text (str)", "typen", 2, 13, 2, 0, "Zusammensetzen, len, Zeichen herausschneiden: datum[0:4] ist das Jahr.", None),
    ("round", "round", "typen", 4, 11, 2, 1, "Rundet für die Ausgabe: round(mittel, 2).", None),
    ("float", "Gleitkommazahl", "typen", 4, 12, 1, 0, "Kommazahlen werden binär gespeichert und sind nicht exakt: 0.1 + 0.2 == 0.3 ist False.", "„Kommazahlen sind exakt.“"),
    ("liste", "Liste", "typen", 5, 3, 1, 0, "Mehrere Werte in fester Reihenfolge.", None),
    ("append", "append", "typen", 5, 3, 2, 1, "Hängt einen Wert an — das Sammelmuster.", None),
    ("index", "Index & Slice", "typen", 5, 4, 1, 0, "liste[0] erster, liste[-1] letzter Wert, liste[2:5] die Indizes 2 bis 4.", None),
    ("indexerror", "IndexError", "typen", 5, 4, 2, 1, "Zugriff außerhalb der Liste — der häufigste Listenfehler.", None),
    ("range", "range", "typen", 5, 5, 1, 1, "Folge ganzer Zahlen, z. B. range(2015, 2025). Der Endwert ist nicht enthalten.", "„range ist eine Liste.“"),
    ("parallel", "zusammengehörige Listen", "typen", 5, 7, 2, 0, "daten[i] und maxima[i] gehören zum selben Tag.", "„bester enthält die höchste Temperatur“ — es ist ein Index."),
    ("textvergleich", "Text vergleichen", "typen", 5, 11, 2, 0, "Texte werden Zeichen für Zeichen verglichen.", "„\"9.5\" > \"28.1\" ist falsch.“ Es ist wahr."),
    ("dict", "Dictionary", "typen", 6, 8, 1, 0, "Ordnet Schlüsseln Werte zu: {\"1947\": 119}. Ein Durchlauf, ein Eintrag pro Jahr.", None),
    ("keyerror", "KeyError, in, get", "typen", 6, 8, 2, 0, "Nach einem fehlenden Schlüssel kann man nicht fragen; vorher mit in prüfen oder get verwenden.", None),
    ("typbilanz", "Zwischenbilanz Datentypen", "typen", 6, 13, 2, 0, "int, float, str, bool, list, range, dict — mit Herkunft im Datensatz und typischer Falle.", None),
    ("none", "None", "typen", 7, 6, 2, 1, "Der Wert „nichts“ — Rückgabe einer Funktion ohne return.", None),
    ("array", "NumPy-Array", "typen", 10, 2, 1, 0, "Rechnet elementweise: (minima < 0).sum() ersetzt das Zählmuster.", "„Ein Array ist dasselbe wie eine Liste.“"),
    ("dataframe", "DataFrame", "typen", 11, 3, 1, 0, "Tabelle aus beschrifteten Spalten; jede Spalte verhält sich wie ein Array.", None),
    ("nan", "NaN", "typen", 11, 4, 1, 1, "So stellt pandas „kein Wert“ dar, z. B. aus -999 per na_values.", "„NaN ist null.“"),
    ("datumstyp", "Datumsspalte", "typen", 11, 6, 2, 0, "MESS_DATUM mit pd.to_datetime in ein Datum umwandeln.", None),

    # --- Daten & Dateien
    ("dwd", "DWD-Datensatz", "daten", 1, 2, 1, 0, "Klimareihe Fichtelberg seit 1890, rund 48.000 Zeilen — der rote Faden.", None),
    ("tabkalk", "Tabellenkalkulation", "daten", 1, 3, 1, 0, "Drei Aufgaben: leicht, mühsam, praktisch aussichtslos.", None),
    ("rohformat", "Rohformat", "daten", 1, 6, 2, 0, "Semikolons, Leerzeichen, Datum ohne Trennzeichen, Dezimalpunkt, eor-Spalte.", None),
    ("fehlwert", "Fehlwert -999", "daten", 3, 8, 1, 1, "So kennzeichnet der DWD „nicht gemessen“. -999 < 0 ist wahr — und trotzdem kein Frosttag.", None),
    ("openurl", "open_url", "daten", 3, 13, 2, 1, "Holt eine Datei aus dem Repository in den Browser — funktioniert nur dort.", None),
    ("open", "Datei öffnen", "daten", 6, 3, 1, 0, "with open(datei) as f: — Zeile für Zeile, jede als Text.", None),
    ("strip", "readline & strip", "daten", 6, 3, 2, 1, "Eine Zeile lesen; Leerzeichen und Zeilenumbruch am Rand entfernen.", None),
    ("split", "split", "daten", 6, 4, 1, 1, "Zerlegt eine Zeile am Trennzeichen in eine Liste von Texten.", "„Die Zeile ist schon eine Tabelle.“"),
    ("kopfzeile", "Kopfzeile", "daten", 6, 6, 2, 0, "Mit f.readline() überspringen — sonst scheitert float an \"TXK\".", None),
    ("luecke", "Lücke", "daten", 6, 7, 1, 0, "Fehlende Tage fehlen ganz, statt als -999 zu erscheinen. Fichtelberg: 1910 bis 1915.", "„Jeder Tag hat eine Zeile.“"),
    ("schreiben", "Datei schreiben", "daten", 6, 11, 1, 0, "open(..., \"w\") und f.write — ohne automatischen Zeilenumbruch.", None),
    ("langesskript", "das lange Skript", "daten", 6, 12, 2, 0, "Fichtelberg und Freiberg als kopierte Blöcke — funktioniert, ist aber schwer zu ändern.", None),
    ("pfad", "Pfad", "daten", 9, 8, 1, 0, "Relative Pfade gelten ab dem aktuellen Arbeitsverzeichnis.", "„Ein Dateiname bezieht sich auf den Ordner des Programms.“"),
    ("readcsv", "read_csv", "daten", 11, 2, 1, 1, "Liest die Rohdatei in einer Anweisung — was in VL 06 rund 50 Zeilen gekostet hat.", None),
    ("vollstaendig", "vollständige Jahre", "daten", 12, 4, 2, 0, "Jahre mit Lücken erkennen und ausschließen, bevor man vergleicht.", None),
    ("merge", "Stationen verbinden", "daten", 12, 5, 2, 0, "Fichtelberg und Chemnitz über das Datum zusammenführen.", None),
    ("stationswechsel", "Stationswechsel", "daten", 14, 2, 1, 0, "Freiberg misst ab 2015 an anderem Ort mit anderem Gerät — gleiche Datei, andere Messung.", None),
    ("metadaten", "Metadaten", "daten", 14, 3, 1, 0, "Gerät, Messtag, Betreiber, Qualitätsstufe — was die Daten selbst verschweigen.", None),
    ("referenz", "Referenzstation", "daten", 14, 4, 2, 0, "Chemnitz als Vergleich: Verhältnis Freiberg/Chemnitz 1,13 vorher, 0,96 nachher.", None),

    # --- Analyse & Darstellung
    ("kreislauf", "Datenkreislauf", "analyse", 0, 4, 2, 0, "Frage, Erhebung, Aufbereitung, Analyse, Visualisierung, Dokumentation — meist mehrere Runden.", None),
    ("lohnt", "Programm oder Tabelle?", "analyse", 1, 12, 1, 0, "Viele Daten, sperrige Formate, Wiederholung, Nachvollziehbarkeit: dann lohnt ein Programm.", None),
    ("kenntage", "Frost-, Eis-, Sommertag", "analyse", 3, 7, 2, 0, "DWD-Kenntage: Frosttag = Minimum unter 0 °C, Eistag = Maximum unter 0 °C, Sommertag = Maximum ab 25 °C.", None),
    ("mittel", "Mittelwert", "analyse", 4, 4, 1, 0, "Summe durch Anzahl — nur über gültige Werte, und die Anzahl gehört dazu.", "„Ein Mittelwert gilt, egal wie viele Werte fehlen.“"),
    ("hochrechnung", "Hochrechnung", "analyse", 4, 11, 2, 0, "Bei +0,05 °C pro Jahr läge das Mittel 2059 bei 8 °C — nur unter dieser Annahme.", "„Rechnerisch korrekt heißt inhaltlich richtig.“"),
    ("statistik", "statistics", "analyse", 9, 6, 2, 1, "mean, median, stdev für Listen von Messwerten.", None),
    ("notebook", "Jupyter Notebook lesen", "analyse", 10, 4, 2, 0, "Verbreitetes Format in Wissenschaft und Projekten; in der Vorlesung nur zum Lesen vorgestellt, nicht als Werkzeug.", "„Was im Notebook steht, ist das, was gerechnet wurde.“"),
    ("vektor", "elementweise rechnen", "analyse", 10, 2, 2, 0, "Eine Anweisung für alle Werte statt einer Schleife: minima.mean().", None),
    ("filter", "Filtern", "analyse", 11, 5, 1, 0, "df[df[\"TNK\"] < 0] — Zeilen nach einer Bedingung auswählen.", None),
    ("groupby", "groupby", "analyse", 12, 3, 1, 1, "Gruppiert Zeilen, z. B. nach Jahr, und fasst jede Gruppe zusammen.", None),
    ("diagrammform", "Diagrammform", "analyse", 13, 2, 2, 0, "Zeitreihe als Linie, Vergleich als Balken, Verteilung als Histogramm.", None),
    ("diagramm", "Diagramm", "analyse", 13, 3, 1, 0, "Achsen, Einheiten, Titel — ein Diagramm muss ohne Begleittext lesbar sein.", None),
    ("trend", "Trend", "analyse", 13, 4, 1, 0, "Lineare Trendlinie — die Herleitung der 0,05 °C pro Jahr aus VL 04.", None),
    ("irref", "Irreführende Darstellung", "analyse", 13, 5, 1, 0, "Abgeschnittene Achsen, ausgewählte Zeiträume.", None),
    ("qualitaet", "Datenqualität", "analyse", 14, 2, 1, 0, "Kann ich meinem Ergebnis trauen? Lücken, Brüche, Metadaten, Referenz.", None),
    ("reproduzierbar", "Reproduzierbarkeit", "analyse", 14, 5, 2, 0, "Kann ich meine eigene Rechnung wiederholen? Skript statt Handarbeit.", None),
    ("pruefung", "Prüfungsvorbereitung", "analyse", 14, 7, 2, 0, "Musteraufgaben zu allen Aufgabentypen aus VL 00.", None),
]

# ---- Beziehungen: von, nach, Beschriftung
R = [
    # Einstieg
    ("zaehler", "sensorlog", "erzeugt"), ("zaehler", "annahmen", "beruht auf"), ("sensorlog", "tabkalk", "ausgewertet mit"),
    ("kreislauf", "lohnt", "je Runde die Frage"), ("tabkalk", "lohnt", "Grenzen zeigen"), ("dwd", "rohformat", "liegt vor im"),
    ("tabkalk", "algo", "motiviert"), ("algo", "terminierung", "erfordert"), ("algo", "pseudo", "notiert als"),
    ("pseudo", "ablauf", "oder als"), ("algo", "sprache", "formuliert in"), ("blockly", "print", "gleiches Programm wie"),
    # VL 02
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
    ("zaehler", "micropy", "läuft auf"), ("micropy", "while", "while True"), ("micropy", "sensor", "steuert"),
    ("sensor", "seriell", "sendet über"), ("sensor", "messfehler", "Risiko"), ("annahmen", "messfehler", "verletzt ergibt"),
    ("seriell", "zeitstempel", "erhält"), ("seriell", "messdatei", "mitgeschrieben als"),
    # VL 09
    ("funktion", "modul", "wandert in"), ("modul", "namemain", "Testcode unter"), ("modul", "stdlib", "gleiches Prinzip"),
    ("stdlib", "datetime", "enthält"), ("stdlib", "statistik", "enthält"), ("datetime", "luecke", "findet"),
    ("mittel", "statistik", "fertig in"), ("modul", "pip", "externe per"), ("pfad", "open", "entscheidet über"),
    # Phase 2
    ("pip", "array", "installiert"), ("zellen", "notebook", "ähnlich, aber ohne versteckten Zustand:"), ("modul", "array", "import wie"),
    ("liste", "array", "wird zu"), ("zaehlmuster", "vektor", "ersetzt durch"), ("array", "vektor", "ermöglicht"),
    ("array", "dataframe", "Spalte ist ein"), ("open", "readcsv", "in einer Anweisung"), ("zellen", "readcsv", "Arbeitsweise für"),
    ("readcsv", "dataframe", "erzeugt"), ("fehlwert", "nan", "wird zu"), ("none", "nan", "ähnlich:"),
    ("datetime", "datumstyp", "in pandas:"), ("dataframe", "filter", "auswählen mit"), ("dict", "groupby", "Prinzip hinter"),
    ("tabkalk", "groupby", "Aufgabe 3 gelöst mit"), ("luecke", "vollstaendig", "prüfen auf"), ("groupby", "vollstaendig", "nur über"),
    ("vollstaendig", "merge", "dann"), ("diagrammform", "diagramm", "bestimmt"), ("groupby", "diagramm", "Ergebnis als"),
    ("diagramm", "trend", "zeigt"), ("hochrechnung", "trend", "Grundlage"), ("trend", "irref", "Gefahr"),
    ("merge", "referenz", "Grundlage für"), ("stationswechsel", "metadaten", "belegt durch"), ("referenz", "stationswechsel", "entlarvt"),
    ("stationswechsel", "qualitaet", "Beispiel für"), ("luecke", "qualitaet", "prüfen"), ("nan", "qualitaet", "zählen, nicht ignorieren"),
    ("messfehler", "qualitaet", "Ursache für"), ("messdatei", "readcsv", "eingelesen mit"), ("notebook", "reproduzierbar", "Gefahr für"), ("reproduzierbar", "qualitaet", "Teil von"), ("trace", "pruefung", "Aufgabentyp"),
]

# ---- Didaktische Fäden (Metrolinien): jede Folge ist eine Kette von „baut auf“-Schritten
F = [
    ("wiederverwenden", "Wiederverwenden", "Vom Muster über die Funktion zum Modul und zur fremden Bibliothek.",
     ["pseudo", "zaehlmuster", "langesskript", "funktion", "modul", "pip", "array"]),
    ("struktur", "Daten ordnen", "Vom einzelnen Wert über Listen und Dictionaries bis zum DataFrame.",
     ["variable", "liste", "index", "dict", "array", "dataframe"]),
    ("zaehlen", "Vom Zählen zur Aggregation", "Wie aus einer Schleife mit Zähler am Ende eine Zeile groupby wird.",
     ["zaehlmuster", "summe", "mittel", "dict", "vektor", "groupby", "diagramm"]),
    ("fehlwert", "Der Fehlwert", "Wie „nicht gemessen“ in jeder Phase anders aussieht — und jedes Mal behandelt werden muss.",
     ["dwd", "fehlwert", "logik", "mittel", "luecke", "nan", "vollstaendig", "qualitaet"]),
    ("tabelle", "Vom Text zur Tabelle", "Wie aus Textzeilen einer Datei eine Tabelle mit Spalten und Typen wird.",
     ["dwd", "text", "umwandlung", "open", "split", "readcsv", "dataframe"]),
    ("messung", "Von der Messung zum Urteil", "Wie Messdaten entstehen — und warum man ihnen nicht blind trauen darf.",
     ["zaehler", "sensorlog", "sensor", "messfehler", "messdatei", "readcsv", "stationswechsel", "qualitaet"]),
]

ids = {b[0] for b in B}
assert len(ids) == len(B), "doppelte id"
vl_of = {x[0]: x[3] for x in B}
for fid, _, _, st in F:
    for x in st:
        assert x in {y[0] for y in B}, (fid, x)
    for u, v in zip(st, st[1:]):
        assert vl_of[u] <= vl_of[v], ("Faden nicht chronologisch", fid, u, v)
for a, b, _ in R:
    assert a in ids and b in ids, (a, b)
for b in B:
    heads = sections[b[3]]["abschnitte"]
    assert 1 <= b[4] <= len(heads), (b[0], b[3], b[4], len(heads))

out = {
    "stand": STAND,
    "vorlesungen": [
        {"vl": v, "datei": sections[v]["datei"], "status": STATUS[v], "abschnitte": sections[v]["abschnitte"]}
        for v in range(15)
    ],
    "begriffe": [
        {"id": b[0], "name": b[1], "linie": b[2], "vl": b[3], "abschnitt": b[4], "ebene": b[5],
         "code": bool(b[6]), "erklaerung": b[7], "fehlvorstellung": b[8]}
        for b in B
    ],
    "beziehungen": [{"von": a, "nach": b, "text": t} for a, b, t in R],
    "faeden": [{"id": f, "name": n, "beschreibung": d, "stationen": st} for f, n, d, st in F],
}
os.makedirs(ZIEL, exist_ok=True)
text = json.dumps(out, ensure_ascii=False, indent=1)
open(os.path.join(ZIEL, "kurslandkarte.json"), "w", encoding="utf-8").write(text + "\n")
seite = open(os.path.join(HIER, "vorlage.html"), encoding="utf-8").read()
seite = seite.replace("%%DATEN%%", text.replace("</", "<\\/")).replace("%%STAND%%", STAND)
open(os.path.join(ZIEL, "index.html"), "w", encoding="utf-8").write(seite)
e1 = sum(1 for b in B if b[5] == 1)
print(f"{len(B)} Begriffe ({e1} Kern, {len(B)-e1} Detail), {len(R)} Beziehungen")
for b in []:
    print(f"  VL{b[3]:02d} #{b[4]:<2} {sections[b[3]]['abschnitte'][b[4]-1][:34]:34s} <- {b[1]}")
