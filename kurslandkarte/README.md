# Kurslandkarte

Interaktive Übersicht über Begriffe, Zusammenhänge und didaktische Fäden der Vorlesung — in zwei Varianten (Metrokarte und Zeitleiste). Entwurf zur Diskussion; veröffentlicht über GitHub Pages aus dem Ordner `docs/`.

| Datei | Inhalt |
| :---- | :----- |
| `erzeuge.py` | Kuratierte Daten (Begriffe, Beziehungen, Fäden) und Erzeugung von Daten und Seite |
| `vorlage.html` | Ansicht; `%%DATEN%%` und `%%STAND%%` werden beim Erzeugen ersetzt |
| `../docs/kurslandkarte/kurslandkarte.json` | erzeugt: alle Daten, u. a. für das Projekt invivis |
| `../docs/kurslandkarte/index.html` | erzeugt: die veröffentlichte Seite |

## Aktualisieren

Nach Änderungen an Vorlesungen oder Begriffen im Wurzelverzeichnis des Repositorys:

```bash
python3 kurslandkarte/erzeuge.py
```

Begriffe verweisen in `erzeuge.py` auf den **Titel** ihres Abschnitts (ohne Backticks); das Skript liest die Abschnitte automatisch aus den Vorlesungsdateien und ermittelt daraus die LiaScript-Foliennummer. Verschieben sich Abschnitte, bleiben die Links deshalb richtig. Das Skript bricht ab, wenn ein Abschnittstitel nicht mehr existiert, eine Beziehung auf einen unbekannten Begriff verweist oder ein Faden nicht chronologisch verläuft. Die erzeugten Dateien in `docs/` werden mit eingecheckt.

## Datenmodell

* **Begriff:** `id`, `name`, `linie` (Kategorie), `vl`, `abschnitt` (in `erzeuge.py` der Abschnittstitel, im JSON die Foliennummer), `ebene` (1 = Kernbegriff, 2 = Detailbegriff), `code`, `erklaerung`, `fehlvorstellung`
* **Beziehung:** `von`, `nach`, `text` (Beschriftung der Kante, gelesen als „von … text … nach“)
* **Faden:** `id`, `name`, `beschreibung`, `stationen` (chronologische Folge von Begriffs-ids)
