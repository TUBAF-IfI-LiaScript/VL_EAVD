# Beispiele zu Vorlesung 06: Dateien lesen

Die Programme aus [Vorlesung 06](../../06_DateienLesen.md) zum Ausführen auf Ihrem Rechner. Sie brauchen nur Python, keine Zusatzpakete.

| Datei | Inhalt |
| :---- | :----- |
| `ausschnitt.txt` | fünf aufeinanderfolgende Tage (9. bis 13. März 1893) aus der Fichtelberg-Datei, mit einem Fehlwert `-999` |
| `fehlwerte.py` | liest `ausschnitt.txt`, überspringt die Kopfzeile, erkennt `-999` |
| `frosttage.py` | Frosttage pro Jahr auf dem Fichtelberg, Mittelwerte für 1891–1920, 1961–1990 und 1995–2024 |
| `auswertung.py` | das lange Skript: Fichtelberg und Freiberg als kopierte Blöcke, schreibt `fichtelberg_jahre.csv` und `freiberg_jahre.csv` |

## Ausführen

Öffnen Sie in Visual Studio Code **diesen Ordner** (`examples/06_DateienLesen`) und starten Sie ein Programm, zum Beispiel im Terminal:

```
python frosttage.py
```

Die Programme lesen die DWD-Dateien aus `../../data/`, also aus dem Ordner `data` des Repositorys. Das klappt nur, wenn das Terminal in diesem Ordner steht. Meldet Python `FileNotFoundError`, prüfen Sie den Arbeitsordner: `cd examples/06_DateienLesen` (siehe Abschnitt „Typische Fehlvorstellung: Die Datei liegt doch daneben“).

Daten: Deutscher Wetterdienst, Stationen 01358 (Fichtelberg) und 01441 (Freiberg), Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
