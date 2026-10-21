# Kurslandkarte

Interaktive Übersicht über Begriffe, Zusammenhänge und didaktische Fäden der Vorlesung für Studierende — in drei Ansichten: Vorlesungen (Wochenraster nach Blöcken, Standard auf dem Handy), Metrokarte und Zeitleiste. „Sie sind hier“ ergibt sich aus dem Datum. Veröffentlicht über GitHub Pages aus dem Ordner `docs/`.

| Datei | Inhalt |
| :---- | :----- |
| `erzeuge.py` | Kuratierte Kursdaten (Termine, Begriffe, Beziehungen, Fäden) und Aufruf des Kerns |
| `invivis/` | Kopie des gemeinsamen Kerns [invivis Kurslandkarte](https://github.com/TUBAF-IfI-LiaScript/invivis-kurslandkarte) (`kern.py`, `vorlage.html`, `startseite.html`) – **nicht hier ändern**, Verbesserungen im Kern-Repository machen und mit `uebernehmen.py` verteilen |
| `../docs/index.html` | erzeugt: Startseite des Kurses („Diese Woche“, Kurslandkarte, Lernziele, Organisation, Kontakt) |
| `../docs/kurslandkarte/kurslandkarte.json` | erzeugt: alle Daten, u. a. für das Projekt invivis |
| `../docs/kurslandkarte/index.html` | erzeugt: die veröffentlichte Seite |

## Aktualisieren

Nach Änderungen an Vorlesungen oder Begriffen im Wurzelverzeichnis des Repositorys:

```bash
python3 kurslandkarte/erzeuge.py          # Karte und Startseite
python3 kurslandkarte/erzeuge.py --pdf    # vorher fehlende/veraltete PDFs nach `docs/pdf/` (liaex)
```

Kacheln und Startseite verlinken die PDFs aus `docs/pdf/`; sie werden mit eingecheckt.

Begriffe verweisen in `erzeuge.py` auf den **Titel** ihres Abschnitts (ohne Backticks); das Skript liest die Abschnitte automatisch aus den Vorlesungsdateien und ermittelt daraus die LiaScript-Foliennummer. Verschieben sich Abschnitte, bleiben die Links deshalb richtig. Das Skript bricht ab, wenn ein Abschnittstitel nicht mehr existiert, eine Beziehung auf einen unbekannten Begriff verweist oder ein Faden nicht chronologisch verläuft. Die erzeugten Dateien in `docs/` werden mit eingecheckt.

## Nach jeder Vorlesung: Begriffe freischalten

Die Karte zeigt nur die Begriffe freigegebener Vorlesungen; für alle anderen Termin, Titel und Leitfrage (aus dem Semesterplan in `00_Motivation.md`). Vorbereitete Begriffe kommender Vorlesungen werden nicht veröffentlicht, auch nicht in den Daten der Seite: `erzeuge.py` schreibt nur Begriffe, Beziehungen, Fäden, Anwendungen und Abschnittstitel freigegebener Vorlesungen nach `docs/`.

1. Antworten der Abschlussfrage „Ihre Begriffe für die Kurslandkarte“ aus dem LiaScript-Klassenzimmer sichern.
2. Mit der vorbereiteten Liste in `erzeuge.py` abgleichen: Begriffe umbenennen, ergänzen, studentische Anwendungen mit `herkunft="studierende"` aufnehmen. Regel: Schlagworte sind fachunabhängig, Konkretes ist eine Anwendung.
3. Die Vorlesung in `FREIGEGEBEN` eintragen, `make` (= `python3 kurslandkarte/erzeuge.py --pdf`: erzeugt das PDF der Vorlesung mit `liaex` nach `docs/pdf/` und danach die Karte, die es verlinkt), PDF und Karte committen.

## Datenmodell

* **Vorlesung:** `vl`, `datei`, `datum` (Termin, ISO), `kurz` (Kurztitel), `leitfrage` (aus dem Semesterplan in VL 00), `freigegeben`, `pdf` (Link auf `docs/pdf/`, nur wenn freigegeben und vorhanden), `status`, `abschnitte`; Termine und Kurztitel stehen in `TERMINE` in `erzeuge.py`
* **Begriff:** `id`, `name`, `linie` (Kategorie), `vl`, `abschnitt` (in `erzeuge.py` der Abschnittstitel, im JSON die Foliennummer), `ebene` (1 = Kernbegriff, 2 = Detailbegriff), `code`, `erklaerung`, `fehlvorstellung`
* **Beziehung:** `von`, `nach`, `text` (Beschriftung der Kante, gelesen als „von … text … nach“)
* **Anwendung:** `id` (beginnt mit `a_`), `titel`, `fach`, `vl`, `abschnitt` (in `erzeuge.py` der Abschnittstitel, im JSON die Foliennummer), `datensatz`, `schlagworte` (Liste von Begriffs-ids), `herkunft` (`lehrende` oder `studierende`). Anwendungen sind konkrete Fragen an echte Daten; sie erscheinen in der Ansicht „Vorlesungen“ unter den Begriffen, und jeder Begriff nennt im Seitenfeld, in welchen Anwendungen er vorkommt.
* **Schlagwort statt Beispiel:** Begriffe sind fachunabhängig und in einem Satz erklärbar (z. B. „Bildverarbeitung“); das Konkrete („Körner im Dünnschliff“) ist eine Anwendung.
* **Faden:** `id`, `name`, `beschreibung`, `stationen` (chronologische Folge von Begriffs-ids)
