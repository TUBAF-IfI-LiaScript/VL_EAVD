# Beispiele zu Vorlesung 07: Funktionen

Die Programme aus [Vorlesung 07](../../07_Funktionen.md) zum Ausführen auf Ihrem Rechner. Sie brauchen nur Python, keine Zusatzpakete.

| Datei | Inhalt |
| :---- | :----- |
| `frosttage_stationen.py` | Ergebnis des Live Hackings: `auswerten` und `mittel_frost`, Frosttage 1961–1990 und 1995–2024 für Fichtelberg, Chemnitz und Freiberg |
| `auswertung.py` | das lange Skript aus Vorlesung 06, vollständig in Funktionen zerlegt (Höchstwerte, Frosttage, Messtage, Ergebnisdateien) für drei Stationen |
| `pruefen.py` | `assert`-Prüfungen an den Grenzen für `ist_frosttag` und `mittel_frost` |

## Ausführen

Öffnen Sie in Visual Studio Code **diesen Ordner** (`examples/07_Funktionen`) und starten Sie ein Programm, zum Beispiel im Terminal:

```
python frosttage_stationen.py
```

Die Programme lesen die DWD-Dateien aus `../../data/`, also aus dem Ordner `data` des Repositorys. Das klappt nur, wenn das Terminal in diesem Ordner steht. Meldet Python `FileNotFoundError`, prüfen Sie den Arbeitsordner (Vorlesung 06, „Typische Fehlvorstellung: Die Datei liegt doch daneben“).

`auswertung.py` schreibt drei Dateien `*_jahre.csv` in diesen Ordner.

Daten: Deutscher Wetterdienst, Stationen 01358 (Fichtelberg), 00853 (Chemnitz) und 01441 (Freiberg), Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
