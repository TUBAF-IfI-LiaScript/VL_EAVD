# Personenzähler mit dem Arduino Alvik

Einstiegsbeispiel für Vorlesung 00 („Wann erscheinen Sie?“): Der Alvik steht an der Hörsaaltür, zählt Ein- und Austretende über seinen Abstandssensor und der Laptop zeigt live, wann wer gekommen ist.

| Datei | läuft auf | Aufgabe |
| :---- | :-------- | :------ |
| `alvik_messung.py` | Roboter (MicroPython) | gibt jede neue Messung der Abstandszonen als Textzeile über USB aus, fährt nicht |
| `zaehler.py` | Laptop (Python 3) | startet `alvik_messung.py`, schreibt Rohdaten und Zählungen, erkennt Durchgänge und Richtung, zeigt das Diagramm |
| `alvik_ampel.py` | Roboter | Hilfe beim Aufstellen: LEDs rot, wenn eine Zone etwas näher als 1,2 m sieht |

## Aufbau

* Roboter seitlich an einen Türrahmen stellen, Blick quer durch die Tür auf den **gegenüberliegenden Rahmen oder eine Wand in etwa 1–1,5 m**. Ohne Hintergrund in Reichweite hält die Firmware den letzten Wert einer Zone fest (siehe unten).
* Mit `--rein-von links` (Standard) zählt als „rein“, wer – von hinter dem Roboter gesehen – von links nach rechts vorbeigeht.
* USB-Kabel zum Laptop. Der Roboter muss eingeschaltet sein.
* In den ersten Sekunden niemand vor dem Roboter: Das Programm lernt dann den Hintergrund.

## Start

```bash
pip install -r requirements.txt
python zaehler.py --live --beginn 16:15
```

Das Fenster zeigt links die Personen je 2 Minuten (rein nach rechts, raus nach links, Uhrzeit nach unten), rechts die drei inneren Zonen mit gelerntem Hintergrund. Beim Schließen des Fensters wird das Programm auf dem Roboter beendet.

Im aktuellen Ordner entstehen

* `rohdaten_JJJJ-MM-TT.csv` – jede Messung: `empfangen;ms_roboter;links;mitte_links;mitte;mitte_rechts;rechts;oben;unten` (Abstände in mm),
* `zaehlungen_JJJJ-MM-TT.csv` – jeder erkannte Durchgang: `zeit;richtung` (`rein`, `raus`, `unklar`).

Rückfallebene ohne Roboter, z. B. 20-fach schnell:

```bash
python zaehler.py --abspielen rohdaten_2026-10-19.csv --tempo 20
```

## Wie gezählt wird

* Genutzt werden nur die drei inneren Zonen; die äußeren schauen oft am Hintergrund vorbei.
* Hintergrund je Zone: unteres Fünftel der letzten 60 freien Messungen. Belegt ist eine Zone, wenn sie näher als 80 % ihres Hintergrunds misst.
* Ein Durchgang endet, wenn alle drei Zonen 400 ms frei sind. Die Richtung ergibt sich daraus, ob `mitte_links` oder `mitte_rechts` zuerst belegt war.
* Ist etwas länger als 6 s „im Weg“, ist es keine vorbeigehende Person: Die aktuellen Werte werden neuer Hintergrund, nichts wird gezählt.

## Was wir über den Sensor gelernt haben (15.10.2026)

Getestet mit Firmware 1.1.1, Bibliothek 1.1.4, MicroPython 1.28.

* Die Firmware ([Arduino_AlvikCarrier](https://github.com/arduino-libraries/Arduino_AlvikCarrier), `src/sensor_tof_matrix.h`) betreibt den VL53L7CX mit 4×4 Feldern bei 30 Hz. Jede der fünf Frontzonen ist im Wesentlichen **ein** Feld derselben Zeile (etwa 15° × 15°).
* Neue Werte kommen etwa 13-mal pro Sekunde – aber nur, wenn das Programm den Roboter nicht ständig abfragt. Bei 5 ms Pause zwischen den Abfragen kommen nur 2 pro Sekunde an, bei 50 ms rund 13.
* Sieht eine Zone kein Ziel, behält sie ihren letzten Wert, teils über Minuten auf den Millimeter genau. Eine Hand, die weggezogen wird, „bleibt“ dann stehen. Mit einem Hintergrund in 1–1,5 m tritt das nicht auf.
* Die Zeilen kommen am Laptop gepuffert an. Die Empfangszeit ist deshalb nicht die Messzeit; `zaehler.py` rechnet die Roboterzeit in die Uhrzeit um.
* Test mit Stuhl in 1,2 m als Hintergrund: 6 von 6 Durchgängen mit richtiger Richtung erkannt.
* Test im Hörsaal FOR-0270 (18.10.2026): Roboter an der Tischkante vor der Tür, Hintergrund gut 2 m entfernt; eine Person allein wurde zuverlässig in beiden Richtungen gezählt.
