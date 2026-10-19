# Körner im Dünnschliff

Ausblick in Vorlesung 00: Ein Dünnschliff unter gekreuzten Polarisatoren wird mit einer Helligkeitsschwelle ausgewertet – Anzahl, Durchmesser und Flächenanteil der hellen Körner.

* `duennschliff.py` – Auswertung in drei Zellen (`# %%`) für Visual Studio Code
* `duennschliff_xpol.png` – Bild aus dem Fundus von Prof. Heide, TU Bergakademie Freiberg (760 × 1000 Pixel, Maßstab 2000 µm ≈ 80 Pixel)

```bash
pipenv install                   # einmalig: Umgebung aus Pipfile.lock
pipenv run python duennschliff.py
```

Wer kein pipenv nutzt: `pip install numpy matplotlib scipy`.

Ergebnis mit `SCHWELLE = 0.45`: 40 Körner, mittlerer Durchmesser (Median) 657 µm, rund 13 % der Probenfläche. Bei 0,35 sind es 48 Körner (21 %), bei 0,55 nur 32 (11 %).

Die Abbildung in der Vorlesung (`images/00_Motivation/duennschliff_auswertung.png`) entsteht aus der letzten Zelle.
