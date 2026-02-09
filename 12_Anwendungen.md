<!--

author:   Sebastian Zug & André Dietrich & Galina Rudolf
email:    sebastian.zug@informatik.tu-freiberg.de & andre.dietrich@ovgu.de & Galina.Rudolf@informatik.tu-freiberg.de
version:  2.0.0
language: de
narrator: Deutsch Female

comment: Einführung in die Programmierung für Nicht-Informatiker
logo: ./img/LogoCodeExample.png

import: https://github.com/liascript/CodeRunner
        https://raw.githubusercontent.com/TUBAF-IfI-LiaScript/VL_EAVD/master/config.md

-->

[![LiaScript](https://raw.githubusercontent.com/LiaScript/LiaScript/master/badges/course.svg)](https://liascript.github.io/course/?https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_Anwendungen.md)

# Finale Anwendung: Blumentopf-Monitor

| Parameter                | Kursinformationen                                                                                                                                            |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Veranstaltung:**       | @config.lecture                                                                                                                                              |
| **Semester**             | @config.semester                                                                                                                                             |
| **Hochschule:**          | `Technische Universität Freiberg`                                                                                                                            |
| **Inhalte:**             | `Integrierte Anwendung - Blumentopf-Monitoring`                                                                                                              |
| **Link auf Repository:** | [https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_Anwendungen.md](https://github.com/TUBAF-IfI-LiaScript/VL_EAVD/blob/master/12_Anwendungen.md) |
| **Autoren**              | @author                                                                                                                                                      |

![](https://media.giphy.com/media/26tn33aiTi1jkl6H6/source.gif)

--------------------------------------------------------------------

**Fragen an die heutige Veranstaltung ...**

* Wie lassen sich objektorientierte Konzepte (Klassen, Vererbung, Polymorphismus) auf ein reales Sensorproblem anwenden?
* Wie kann man mit Python externe Datenquellen (APIs) abfragen und auswerten?
* Wie verbinden wir Hardwaremessungen (C++) mit Datenanalyse (Python)?

---------------------------------------------------------------------

## Motivation

> _Muss ich morgen meine Pflanze auf der Terasse gießen?_

![](https://img.ccnull.de/1000000/preview/1000132_22ecab9b1198c39f271aa4d0335497b6.jpg "... um zu vermeiden, dass sie vertrocknet oder überwässert wird. Quelle: Tim Reckmann ccnull.de CC-BY 2.0")<!-- style="width: 40%;" -->

> **Wie gehen wir vor?**

Diese einfache Frage führt uns durch die heutige Veranstaltung und fasst die Inhalte des gesamten Semesters zusammen.

### Lösungsansatz

 Um sie zu beantworten, brauchen wir:

1. **Den Ist-Zustand** - Wie feucht ist der Boden? Wie schwer ist der Topf? → C++ / Arduino
2. **Die Prognose** - Wird es in den nächsten Tagen regnen? → Python / API

```ascii

 Datenquelle 1: Sensoren (C++)          Datenquelle 2: Wetter (Python)

 Blumentopf        Arduino              Open-Meteo API
 +--------+      +---------+            +-------------+
 | Feuchte|----->|         |            |  Regen-     |
 | oben   | A0   |  C++    |            |  vorhersage |
 |--------|      |  OOP    |            +------+------+
 | Feuchte|----->|         |                   |
 | unten  | A1   |         |                   v
 |--------|      |         |            +------+------+
 | Waage  |----->|         |            | Analyse +   |
 +--------+ A2   |         |            | Diagramm    |
                 +----+----+            +------+------+
                      |                        |
                      v                        v
               +------+------------------------+------+
               |                                      |
               |      Giessbedarf-Entscheidung        |
               |   Feuchtigkeit + Gewicht + Regen     |
               |                                      |
               +--------------------------------------+                                                                            .
```


<!-- data-type="none" -->
| Teil | Sprache | Thema | Wiederholte Konzepte |
|------|---------|-------|---------------------|
| 1    | C++     | Sensorik mit Arduino | Klassen, Vererbung, Polymorphismus, Zeiger |
| 2    | Python  | Regenvorhersage via API | Bibliotheken, Dictionaries, Pandas, Matplotlib |

### Sensoren

Für den ersten Teil verwenden wir drei analoge Sensoren:

+ **2x [AZ-Delivery Hygrometer v1.2](https://www.az-delivery.de/products/bodenfeuchte-sensor-modul-v1-2)** - kapazitive Feuchtesensoren, die die Bodenfeuchtigkeit an verschiedenen Positionen im Topf messen (oben und unten). Der Sensor arbeitet kapazitiv, d.h. er misst die Dielektrizitätskonstante des Bodens, die sich mit dem Wassergehalt ändert. Da kein Strom durch den Boden fließt, korrodiert die Sonde nicht - im Gegensatz zu resistiven Sensoren.

https://cdn.shopify.com/s/files/1/1509/1638/files/Hygrometer_V1.2_Sensor_Modul_Datenblatt_AZ-Delivery_Vertriebs_GmbH.pdf?v=1608545956

+ **1x [FSR 406](https://www.circuits-diy.com/how-to-measure-force-using-fsr406-force-sensor-and-arduino/) (Force Sensing Resistor)** - sitzt _unter_ dem Blumentopf und misst das Gewicht über den ausgeübten Druck. Ein schwerer Topf (= viel Wasser) erzeugt mehr Kraft als ein leichter (= trocken). Der FSR ist ein Widerstand, dessen Wert mit zunehmender Kraft sinkt: ohne Last > 1 MΩ, bei maximaler Kraft ca. 200 Ω. Über einen Spannungsteiler mit einem 10 kΩ Widerstand entsteht ein analoges Signal für den Arduino.

https://cdn.sparkfun.com/assets/c/4/6/8/b/2010-10-26-DataSheet-FSR406-Layout2.pdf

### Regenvorhersage

Für die zweite Datenquelle nutzen wir die [Open-Meteo API](https://open-meteo.com/). Open-Meteo ist ein freier Wetterdienst, der Vorhersagen für jeden Ort der Welt bereitstellt - kostenlos und ohne Registrierung.

Über die Webseite lässt sich interaktiv eine Abfrage zusammenstellen:

1. **Ort wählen** - z.B. Freiberg (Sachsen), Koordinaten: 50.91°N, 13.34°E
2. **Variablen auswählen** - z.B. tägliche Niederschlagssumme und Regenwahrscheinlichkeit
3. **URL generieren** - Die Webseite erzeugt eine URL, die alle Parameter enthält

Die Idee einer API (_Application Programming Interface_): Statt eine Webseite im Browser zu öffnen, stellt unser Programm die gleiche Anfrage automatisiert und erhält maschinenlesbare Daten zurück.

## Teil 1: Objektorientierte Sensorik (C++)

```ascii
         TEIL 1 !
         
 Datenquelle 1: Sensoren (C++)          Datenquelle 2: Wetter (Python)

 Blumentopf        Arduino              Open-Meteo API
 +--------+      +---------+            +-------------+
 | Feuchte|----->|         |            |  Regen-     |
 | oben   | A0   |  C++    |            |  vorhersage |
 |--------|      |  OOP    |            +------+------+
 | Feuchte|----->|         |                   |
 | unten  | A1   |         |                   v
 |--------|      |         |            +------+------+
 | Waage  |----->|         |            | Analyse +   |
 +--------+ A2   |         |            | Diagramm    |
                 +----+----+            +------+------+
                      |                        |
                      v                        v
               +------+------------------------+------+
               |                                      |
               |      Giessbedarf-Entscheidung        |
               |   Feuchtigkeit + Gewicht + Regen     |
               |                                      |
               +--------------------------------------+                                                                            .
```

### Analoge Sensoren am Multimeter

> Was bedeutet es, wenn wir von einem Analogen Sensor sprechen?

Was passiert, wenn wir die Sensorausgänge mit dem Multimeter vermessen?

<!-- Hier Fotos der Multimeter-Messungen einfügen:

![Multimeter am Feuchtesensor](./images/12_Anwendung/Multimeter_Feuchtesensor.jpg)
![Multimeter am Drucksensor](./images/12_Anwendung/Multimeter_Drucksensor.jpg)

-->

<!-- data-type="none" -->
| Sensor        | Zustand 1                  | Zustand 2                  | Einheit        |
| ------------- | -------------------------- | -------------------------- | -------------- |
| Feuchtesensor | Trocken: ~3.2V (≈ 650)     | Feucht: ~2.0V (≈ 410)      | % Feuchtigkeit |
| Drucksensor   | Leerer Topf: ~1.6V (≈ 330) | Voller Topf: ~3.5V (≈ 720) | Gramm          |

Die Spannung am Sensorausgang ist proportional zur gemessenen physikalischen Größe. Der ADC des Arduino wandelt diese Spannung in einen digitalen Rohwert um:

$$\text{Rohwert} = \frac{U_{sensor}}{5V} \cdot 1023$$

**Beobachtung:** Alle Sensoren liefern einen analogen Rohwert (0–1023), aber jeder Sensor interpretiert diesen Wert anders. Das ist ein idealer Anwendungsfall für **Vererbung**!

### Ansatz ohne Objektorientierung

Zunächst ein naiver Ansatz - was wäre, wenn wir einfach Funktionen verwenden?

```cpp                     OhneOOP.cpp
#include <iostream>```ascii
         TEIL 1 !
         
 Datenquelle 1: Sensoren (C++)          Datenquelle 2: Wetter (Python)

 Blumentopf        Arduino              Open-Meteo API
 +--------+      +---------+            +-------------+
 | Feuchte|----->|         |            |  Regen-     |
 | oben   | A0   |  C++    |            |  vorhersage |
 |--------|      |  OOP    |            +------+------+
 | Feuchte|----->|         |                   |
 | unten  | A1   |         |                   v
 |--------|      |         |            +------+------+
 | Waage  |----->|         |            | Analyse +   |
 +--------+ A2   |         |            | Diagramm    |
                 +----+----+            +------+------+
                      |                        |
                      v                        v
               +------+------------------------+------+
               |                                      |
               |      Giessbedarf-Entscheidung        |
               |   Feuchtigkeit + Gewicht + Regen     |
               |                                      |
               +--------------------------------------+                                                                            .
```
#include <cmath>
using namespace std;

// Simulation von analogRead (normalerweise Hardware!)
int simulateRead(int pin) {
    int values[] = {650, 420, 300};
    return values[pin];
}

float readMoisture(int pin, int dryVal, int wetVal) {
    // Lineare Kalibrierung des kapazitiven Sensors
    int raw = simulateRead(pin);
    float pct = (float)(dryVal - raw) / (dryVal - wetVal) * 100.0;
    if (pct < 0) pct = 0;
    if (pct > 100) pct = 100;
    return pct;
}

float readWeight(int pin, float scaleFactor) {
    int raw = simulateRead(pin);
    // FSR 406: logarithmische Kennlinie!
    // Aus Datenblatt: Widerstand sinkt logarithmisch mit Kraft
    if (raw <= 0) return 0;
    return scaleFactor * log(raw + 1);
    // Lineare Variante (vereinfacht, physikalisch ungenau):
    // return (float)raw / 1023.0 * maxWeight;
}

int main() {
    cout << "Feuchtigkeit oben: "
         << readMoisture(0, 800, 400) << " %" << endl;
    cout << "Feuchtigkeit unten: "
         << readMoisture(1, 820, 380) << " %" << endl;
    cout << "Gewicht: "
         << readWeight(2, 250) << " g" << endl;
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

Das funktioniert, aber:

+ Für jeden neuen Sensortyp brauchen wir eine neue Funktion
+ Die Kalibrierungswerte (`dryVal`, `wetVal`, `maxWeight`) werden als lose Parameter herumgereicht
+ Es gibt keinen Zusammenhang zwischen Pin, Name und Kalibrierung

> **Erinnerung VL 5:** Klassen bündeln Daten und Methoden zu einer Einheit und schützen die Daten vor unbeabsichtigtem Zugriff (_Kapselung_).

### Basisklasse `AnalogSensor`

Wir entwerfen eine gemeinsame Basisklasse für alle analogen Sensoren:

```cpp                     BasisKlasse.cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int analogRead(int pin) {
    int values[] = {650, 420, 300};
    if (pin >= 0 && pin < 3) return values[pin];
    return 0;
}

class AnalogSensor {
  protected:                      // Zugriff für abgeleitete Klassen!
    int _pin;
    string _name;
    int _rawValue;

  public:
    AnalogSensor(int pin, string name)
        : _pin(pin), _name(name), _rawValue(0) {}

    int readRaw() {
        _rawValue = analogRead(_pin);
        return _rawValue;
    }

    virtual float getValue() = 0;  // Rein virtuell!

    virtual void print() {
        cout << _name << ": " << getValue() << endl;
    }

    string getName() { return _name; }
    int getPin()     { return _pin; }

    virtual ~AnalogSensor() {}
};

int main(){
    // AnalogSensor s(0, "Test");  // Fehler - abstrakte Klasse!
    cout << "AnalogSensor ist abstrakt - "
         << "kann nicht direkt instanziiert werden." << endl;
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Erinnerung VL 6:** Das Schlüsselwort `protected` erlaubt abgeleiteten Klassen den Zugriff, verbietet ihn aber von außen. `virtual ... = 0` macht die Methode _rein virtuell_ und die Klasse damit _abstrakt_.

Welche Konzepte stecken in dieser Klasse?

- [[ ]] Destruktor
- [[X]] Konstruktor mit Initialisierungsliste
- [[X]] Kapselung (protected/public)
- [[ ]] Mehrfachvererbung
- [[X]] Rein virtuelle Methode
- [[X]] Virtuelle Methode

### Abgeleitete Klassen

Nun leiten wir zwei spezialisierte Klassen ab - eine für die Feuchtesensoren und eine für den Drucksensor (Waage):

```cpp                     Vererbung.cpp
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int analogRead(int pin) {
    int values[] = {650, 420, 300};
    if (pin >= 0 && pin < 3) return values[pin];
    return 0;
}

class AnalogSensor {
  protected:
    int _pin;
    string _name;
    int _rawValue;
  public:
    AnalogSensor(int pin, string name)
        : _pin(pin), _name(name), _rawValue(0) {}
    int readRaw() {
        _rawValue = analogRead(_pin);
        return _rawValue;
    }
    virtual float getValue() = 0;
    virtual void print() {
        cout << _name << ": " << getValue() << endl;
    }
    string getName() { return _name; }
    virtual ~AnalogSensor() {}
};

// ---- Feuchtesensor ----
    float pct = (float)(dryVal - raw) / (dryVal - wetVal) * 100.0;
    if (pct < 0) pct = 0;
    if (pct > 100) pct = 100;
    return pct;
}

float readWeight(int pin, float scaleFactor) {
    int raw = simulateRead(pin);
    // FSR 406: logarithmische Kennlinie!
    // Aus Datenblatt: Widerstand sinkt logarithmisch mit Kraft
class MoistureSensor : public AnalogSensor {
  private:
    int _dryValue;   // ADC-Wert bei trockenem Boden
    int _wetValue;   // ADC-Wert bei nassem Boden

  public:
    MoistureSensor(int pin, string name, int dryVal, int wetVal)
        : AnalogSensor(pin, name),     // Basisklassen-Konstruktor!
          _dryValue(dryVal),
          _wetValue(wetVal) {}

    float getValue() override {
        readRaw();
        float pct = (float)(_dryValue - _rawValue)
                   / (_dryValue - _wetValue) * 100.0;
        if (pct < 0)   pct = 0;
        if (pct > 100) pct = 100;
        return pct;
    }

    void print() override {
        cout << _name << ": " << getValue() << " %" << endl;
    }
};

// ---- Drucksensor / Waage (FSR 406) ----
class PressureSensor : public AnalogSensor {
  private:
    float _scaleFactor;   // Kalibrierungsfaktor (Gramm)

  public:
    PressureSensor(int pin, string name, float scaleFactor)
        : AnalogSensor(pin, name),
          _scaleFactor(scaleFactor) {}

    float getValue() override {
        readRaw();
        // FSR 406: logarithmische Kennlinie!
        // Aus Datenblatt: Widerstand sinkt logarithmisch mit Kraft
        if (_rawValue <= 0) return 0;
        return _scaleFactor * log(_rawValue + 1);
        // Lineare Variante (vereinfacht, physikalisch ungenau):
        // return (float)_rawValue / 1023.0 * _scaleFactor;
    }

    void print() override {
        cout << _name << ": " << getValue() << " g" << endl;
    }
};

int main() {
    MoistureSensor m1(0, "Feuchtigkeit oben", 800, 400);
    MoistureSensor m2(1, "Feuchtigkeit unten", 820, 380);
    PressureSensor waage(2, "Topfgewicht", 250);

    m1.print();
    m2.print();
    waage.print();
    return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> **Erinnerung VL 6:** Beim Aufruf des Konstruktors einer abgeleiteten Klasse wird _zuerst_ der Konstruktor der Basisklasse aufgerufen. `override` markiert explizit, dass eine virtuelle Methode überschrieben wird.

Beachten Sie: Beide Klassen erben `readRaw()` und `getName()` von `AnalogSensor`, aber implementieren `getValue()` und `print()` unterschiedlich! Der `MoistureSensor` rechnet in Prozent um, der `PressureSensor` in Gramm.

## Teil 2: Regenvorhersage mit Python

```ascii
                                                TEIL 2 !
         
 Datenquelle 1: Sensoren (C++)          Datenquelle 2: Wetter (Python)

 Blumentopf        Arduino              Open-Meteo API
 +--------+      +---------+            +-------------+
 | Feuchte|----->|         |            |  Regen-     |
 | oben   | A0   |  C++    |            |  vorhersage |
 |--------|      |  OOP    |            +------+------+
 | Feuchte|----->|         |                   |
 | unten  | A1   |         |                   v
 |--------|      |         |            +------+------+
 | Waage  |----->|         |            | Analyse +   |
 +--------+ A2   |         |            | Diagramm    |
                 +----+----+            +------+------+
                      |                        |
                      v                        v
               +------+------------------------+------+
               |                                      |
               |      Giessbedarf-Entscheidung        |
               |   Feuchtigkeit + Gewicht + Regen     |
               |                                      |
               +--------------------------------------+                                                                            .
```


### Was ist eine API?

> Eine **API** (Application Programming Interface) ist eine Schnittstelle, über die Programme miteinander kommunizieren. Wir nutzen die von [Open-Meteo API](https://open-meteo.com/) vorgegebene Schnittstelle, um Wetterdaten abzufragen.

Das Prinzip:

1. Wir senden eine **Anfrage** (HTTP GET) mit Parametern (Ort, gewünschte Daten)
2. Der Server antwortet mit **JSON-Daten** (strukturiertes Textformat, ähnlich einem Python-Dictionary)
3. Wir verarbeiten die Daten mit **Pandas** und visualisieren mit **Matplotlib**

```ascii
 Python-Skript                                Open-Meteo Server
 +---------------------+                      +---------------------+
 |                     |  1. HTTP GET         |                     |
 | url = `…?           +--------------------->+  Wetterdatenbank    |
 |  latitude=50.91&    |  latitude=50.91      |                     |
 |  longitude=13.34&   |  longitude=13.34     |  Freiberg: 50.91°N  |
 |  daily=precip…`     |  daily=precip_sum    |            13.34°E  |
 |                     |                      |  Berlin: …          |
 |                     |  2. JSON-Antwort     |  London: …          |
 | data = json.loads() +<---------------------+  Paris: …           |
 |                     |  {`daily`:           |                     |
 | df = DataFrame(data)|    {`time`:[…],      |                     |
 |                     |     `precip`:[…]}}   |                     |
 +---------------------+                      +---------------------+
         |
         v
 +---------------------+
 | Pandas + Matplotlib |
 | Analyse & Diagramm  |
 +---------------------+                                                                                                               .
```

> Beispiel-URL für Freiberg (7-Tage-Vorhersage):
>
> `https://api.open-meteo.com/v1/forecast?latitude=50.91&longitude=13.34&daily=precipitation_sum,precipitation_probability_max&timezone=Europe/Berlin&forecast_days=7`

> Probieren Sie es in Ihrem Browser aus! Das Ergebnis ist eine lange Textzeile im JSON-Format.

```json
{
 "latitude":50.92,"longitude":13.339998,
 "generationtime_ms":0.11014938354492188,
 "utc_offset_seconds":3600,
 "timezone":"Europe/Berlin",
 "timezone_abbreviation":"GMT+1",
 "elevation":415.0,
 "daily_units":{"time":"iso8601","precipitation_sum":"mm","precipitation_probability_max":"%"},
 "daily":
 {
   "time":["2026-02-09","2026-02-10","2026-02-11","2026-02-12","2026-02-13","2026-02-14","2026-02-15"],
   "precipitation_sum":[0.00,0.00,4.50,5.10,1.70,2.30,3.70],
   "precipitation_probability_max":[0,5,78,80,75,43,29]
 }
}
```

> **Erinnerung VL 8:** Dictionaries (`dict`) speichern Schlüssel-Wert-Paare - genau so ist auch das JSON-Format aufgebaut!

### Datenabfrage

```python                  apiAbfrage.py
import json
  public:
    PressureSensor(int pin, string name, float scaleFactor)
        : AnalogSensor(pin, name),
          _scaleFactor(scaleFactor) {}

    float getValue() override {
        readRaw();
        // FSR 406: logarithmische Kennlinie!
        // Aus Datenblatt: Widerstand sinkt logarithmisch mit Kraft
        if (_rawValue <= 0) return 0;
        return _scaleFactor * log(_rawValue + 1);
        // Lineare Variante (vereinfacht, physikalisch ungenau):
        // return (float)_rawValue / 1023.0 * _scaleFactor;
import urllib.request

# Koordinaten von Freiberg (Sachsen)
latitude = 50.91
longitude = 13.34

# API-URL zusammenbauen
url = ("https://api.open-meteo.com/v1/forecast?"
       "latitude={}&longitude={}"
       "&daily=precipitation_sum,precipitation_probability_max"
       "&timezone=Europe/Berlin"
       "&forecast_days=7").format(latitude, longitude)

print("Anfrage an:", url)
print()

# Daten abrufen
response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())
print(data)

# Ergebnis anzeigen
print("Tägliche Vorhersage:")
for i in range(len(data['daily']['time'])):
    print("  {} - Niederschlag: {:5.1f} mm, Wahrsch.: {:3d}%".format(
        data['daily']['time'][i],
        data['daily']['precipitation_sum'][i],
        data['daily']['precipitation_probability_max'][i]
    ))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> **Erinnerung VL 7+8:** `str.format()` fügt Werte in Strings ein. `json.loads()` wandelt einen JSON-String in ein Python-Dictionary um. Der Zugriff auf verschachtelte Daten erfolgt über verkettete Schlüssel: `data['daily']['time']`.

### Datenverarbeitung mit Pandas

```python                  pandasVerarbeitung.py
import json
import urllib.request
import pandas as pd

# Daten von Open-Meteo abrufen
url = ("https://api.open-meteo.com/v1/forecast?"
       "latitude=50.91&longitude=13.34"
       "&daily=precipitation_sum,precipitation_probability_max"
       "&timezone=Europe/Berlin"
       "&forecast_days=7")

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

# Dictionary -> DataFrame
df = pd.DataFrame({
    'Datum': data['daily']['time'],
    'Niederschlag_mm': data['daily']['precipitation_sum'],
    'Regenwahrsch_pct': data['daily']['precipitation_probability_max']
})

print(df)
print()

# Zusammenfassung
print("Gesamtniederschlag (7 Tage): {:.1f} mm".format(
    df['Niederschlag_mm'].sum()))
print("Max. Regenwahrscheinlichkeit: {}%".format(
    df['Regenwahrsch_pct'].max()))
print("Regentage (> 1mm): {}".format(
    (df['Niederschlag_mm'] > 1).sum()))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> **Erinnerung VL 10:** Ein `DataFrame` kann direkt aus einem Dictionary erstellt werden. Methoden wie `.sum()`, `.max()` und Vergleichsoperationen auf Spalten aggregieren bzw. filtern Daten.

### Visualisierung

```python                  visualisierung.py
import json
import urllib.request
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Daten abrufen
url = ("https://api.open-meteo.com/v1/forecast?"
       "latitude=50.91&longitude=13.34"
       "&daily=precipitation_sum,precipitation_probability_max"
       "&timezone=Europe/Berlin"
       "&forecast_days=7")

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

df = pd.DataFrame({
    'Datum': data['daily']['time'],
    'Niederschlag_mm': data['daily']['precipitation_sum'],
    'Regenwahrsch_pct': data['daily']['precipitation_probability_max']
})

# Visualisierung
fig, ax = plt.subplots(figsize=(10, 5))

farben = ['steelblue' if n > 1 else 'lightgray'
          for n in df['Niederschlag_mm']]
ax.bar(df['Datum'], df['Niederschlag_mm'], color=farben)
ax.set_xlabel('Datum')
ax.set_ylabel('Niederschlag (mm)')
ax.set_title('Regenvorhersage fuer Freiberg - naechste 7 Tage')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('foo.png')
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> **Erinnerung VL 11:** `plt.subplots()` erzeugt eine Abbildung mit Achsen. `ax.bar()` erstellt ein Balkendiagramm. Die Farbliste wird mit einer List Comprehension (VL 8) dynamisch erzeugt.

## Teil 3: Gießen oder nicht?

```ascii       
 Datenquelle 1: Sensoren (C++)          Datenquelle 2: Wetter (Python)

 Blumentopf        Arduino              Open-Meteo API
 +--------+      +---------+            +-------------+
 | Feuchte|----->|         |            |  Regen-     |
 | oben   | A0   |  C++    |            |  vorhersage |
 |--------|      |  OOP    |            +------+------+
 | Feuchte|----->|         |                   |
 | unten  | A1   |         |                   v
 |--------|      |         |            +------+------+
 | Waage  |----->|         |            | Analyse +   |
 +--------+ A2   |         |            | Diagramm    |
                 +----+----+            +------+------+
                      |                        |
                      v                        v
               +------+------------------------+------+
               |                                      |
   TEIL 3      |      Giessbedarf-Entscheidung        |
               |   Feuchtigkeit + Gewicht + Regen     |
               |                                      |
               +--------------------------------------+                                                                            .
```


Jetzt verbinden wir die Sensordaten (C++) mit der Wettervorhersage (Python). In der Praxis würde der Arduino die aktuellen Messwerte per Serial oder WiFi an den PC übertragen.

```python                  entscheidung.py
import json
import urllib.request

# --- Simulierte Sensordaten vom Arduino ---
# (In der Praxis per Serial/WiFi uebertragen)
feuchtigkeit_oben  = 25.0    # Prozent
feuchtigkeit_unten = 45.0    # Prozent
topfgewicht        = 1200.0  # Gramm

# Referenzwerte fuer den Topf
LEERGEWICHT = 800    # Trockener Topf + trockene Erde
VOLLGEWICHT = 1800   # Topf + nasse Erde

# --- Regenvorhersage von Open-Meteo ---
url = ("https://api.open-meteo.com/v1/forecast?"
       "latitude=50.91&longitude=13.34"
       "&daily=precipitation_sum"
       "&timezone=Europe/Berlin"
       "&forecast_days=3")

response = urllib.request.urlopen(url)
data = json.loads(response.read().decode())

regen_2_tage = sum(data['daily']['precipitation_sum'][1:3])

# --- Entscheidungslogik ---
def muss_ich_giessen(feuchtigkeit, gewicht, regen_erwartet):
    wasseranteil = (gewicht - LEERGEWICHT) / (VOLLGEWICHT - LEERGEWICHT) * 100

    if feuchtigkeit > 60:
        return "Nein - Boden ist feucht genug ({:.0f}%).".format(feuchtigkeit)
    elif wasseranteil > 50:
        return "Nein - Topf ist noch schwer genug ({:.0f}g).".format(gewicht)
    elif feuchtigkeit <= 30 and regen_erwartet > 5:
        return "Abwarten - {:.1f}mm Regen erwartet.".format(regen_erwartet)
    else:
        return "Ja - bitte giessen!"

# --- Ausgabe ---
print("=== Blumentopf-Status ===")
print("Feuchtigkeit oben:  {:5.1f} %".format(feuchtigkeit_oben))
print("Feuchtigkeit unten: {:5.1f} %".format(feuchtigkeit_unten))
print("Topfgewicht:        {:5.0f} g".format(topfgewicht))
wasseranteil = (topfgewicht - LEERGEWICHT) / (VOLLGEWICHT - LEERGEWICHT) * 100
print("Wasseranteil:       {:5.0f} %".format(wasseranteil))
print()

print("=== Regenvorhersage ===")
for i in range(len(data['daily']['time'])):
    print("  {} : {:.1f} mm".format(
        data['daily']['time'][i],
        data['daily']['precipitation_sum'][i]))
print()

mittlere_feuchtigkeit = (feuchtigkeit_oben + feuchtigkeit_unten) / 2
print("=== Empfehlung ===")
print("-> " + muss_ich_giessen(
    mittlere_feuchtigkeit, topfgewicht, regen_2_tage))
```
@LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

> **Erinnerung VL 4+7:** Funktionen kapseln wiederverwendbare Logik. `muss_ich_giessen()` nimmt Parameter entgegen, verarbeitet sie mit `if/elif/else` und gibt einen String zurück.

> Verändern Sie die simulierten Sensorwerte (`feuchtigkeit_oben`, `topfgewicht`) und beobachten Sie, wie sich die Empfehlung ändert!


## Rückblick

                              {{0-1}}
******************************************************************************

Ein Blick zurück in den Oktober ... mit welchen Zielen waren wir gestartet:

<!-- style="background-color: rgba(255, 255, 0, 0.5);"-->
> Vorlesung 0
>
> + __Anwendungssicht__
>
>   _Wir möchten Sie in die Lage versetzen einfache Messaufgaben (mit einem Mikrocontroller) zu realisieren und die Daten auszuwerten._
>
> + __Algorithmische Perspektive__
>
>   _Wir möchten Sie dazu ertüchtigen den Algorithmusbegriff der Informatik zu durchdringen und anwenden zu können._
>
> + __Konzeptionelle Perspektive__
>
>   _Sie erlernen grundlegende Elemente der prozeduralen und der objektorientierten Programmierung._
>
> + __Umsetzungssicht__
>
>   _Wir vermitteln Grundkenntnisse in den Programmiersprachen C++ und Python._

******************************************************************************

                              {{1-2}}
******************************************************************************

Das heutige Beispiel hat all diese Ziele zusammengeführt:

<!-- data-type="none" -->
| Ziel                       | Umsetzung im Blumentopf-Beispiel                           | Vorlesungen |
| -------------------------- | ---------------------------------------------------------- | ----------- |
| Anwendungssicht            | Sensoren auslesen, Daten analysieren, Entscheidung treffen | 0–12        |
| Algorithmische Perspektive | Kalibrierung, Mittelwertbildung, Entscheidungslogik        | 2, 4        |
| Konzeptionelle Perspektive | Klassen, Vererbung, Polymorphismus                         | 5, 6, 9     |
| C++ Grundkenntnisse        | Arduino-Programm mit OOP-Architektur                       | 1–6         |
| Python Grundkenntnisse     | API-Abfrage, Pandas, Matplotlib                            | 7–11        |

Was konnten / wollten wir dabei nicht leisten:

+ Der Softwareentwicklungsprozess ist weitgehend unberücksichtigt geblieben.
+ Sie haben die Programmiersprachen C++ und Python nur in den Grundkonzepten kennen gelernt.
+ Die unterschiedlichen Programmiertechniken von C++ für Mikrocontroller und Desktop-Anwendungen wurden nicht vertieft.
+ ...

> Wenn Sie Lust auf mehr "Software" haben, bietet die Veranstaltung _Softwareentwicklung_ im kommenden Semester einen guten Ansatzpunkt!

******************************************************************************


## Klausurvorbereitung

Gehen Sie bitte von folgenden Aufgabentypen für die Klausur aus:

+ Korrektur eines Programmes: _Finden Sie Fehler im nachfolgenden Codebeispiel ..._
+ Entwerfen eines Programmes / Ergänzen von Methoden: _Erweitern Sie den Code um eine Methode XY ..._
+ Analyse eines Programmes: _Welchen Wert gibt das Programm mit dem Erreichen der Zeile N aus?_
+ Konzeptionelle Fragen: _Nennen Sie drei Ganzzahldatentypen in C++._

### A1: Korrektur eines Programms

_Die folgende Funktion soll den Mittelwert der Messwerte in einem Array berechnen. Die Implementierung enthält syntaktische und logische Fehler. Schreiben Sie das korrigierte Programm auf._

```cpp                     Aufgabe1.cpp
#include <iostream>

float mittelwert(int messwerte, int n)
{
  float summe;
  for (i=1;i<=n;i++)
  {
    summe =+ messwerte[i];
  }
  return summe * n;
}

int main(void)
{
  int daten[5] = {120, 350 280, 410, 190};
  float ergebnis
  ergebnis = mittelwert(daten,5)
  std::cout<<"Mittelwert: "<<ergebnis<<"\n";
  return 0;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

> Machen Sie sich bewusst, dass Sie in der Klausur keine Möglichkeit haben, den Compiler "zu befragen". Üben Sie daher das Lesen von Code. Tauschen Sie dazu Programme aus den Übungen untereinander aus und evaluieren Sie diese.

                            {{1-2}}
**********************************
<!-- data-type="none" -->
| Zeile | Fehler | Typ | Korrektur |
|-------|--------|-----|-----------|
| 3 | `int messwerte` kann nicht indiziert werden | Syntaktisch | `int messwerte[]` oder `int* messwerte` |
| 5 | `summe` wird nicht initialisiert | Logisch | `float summe = 0;` |
| 6 | `i` ist nicht deklariert | Syntaktisch | `int i` bzw. `for (int i=...)` |
| 6 | Schleife startet bei `i=1` statt `i=0` | Logisch | `i=0` (Arrays beginnen bei 0) |
| 6 | Bedingung `i<=n` greift über das Array hinaus | Logisch | `i<n` |
| 8 | `=+` ist kein zusammengesetzter Operator | Syntaktisch | `+=` |
| 10 | `summe * n` berechnet nicht den Mittelwert | Logisch | `summe / n` |
| 15 | Komma fehlt zwischen `350` und `280` | Syntaktisch | `350, 280` |
| 16 | Semikolon nach `ergebnis` fehlt | Syntaktisch | `float ergebnis;` |
| 17 | Semikolon am Zeilenende fehlt | Syntaktisch | `mittelwert(daten,5);` |

**********************************

### A2: Erweitern eines C++-Programms

_Gegeben ist die folgende Basisklasse `AnalogSensor`:_

```cpp          Aufgabe2.cpp
class AnalogSensor {
  protected:
    int _pin;
    std::string _name;
  public:
    AnalogSensor(int pin, std::string name)
        : _pin(pin), _name(name) {}
    virtual float getValue() = 0;
    virtual void print() {
        std::cout << _name << ": " << getValue() << std::endl;
    }
    virtual ~AnalogSensor() {}
};
```

_Leiten Sie eine Klasse `TemperatureSensor` von `AnalogSensor` ab, die folgende Anforderungen erfüllt:_

+ _Die Klasse speichert zusätzlich einen Offset-Wert (`float`) zur Kalibrierung._
+ _`getValue()` berechnet die Temperatur nach: $T = \frac{\text{Rohwert} \cdot 500.0}{1023.0} - \text{Offset}$_
+ _`print()` gibt den Namen, die Temperatur und die Einheit "°C" aus._
+ _Folgende Anweisungen in `main` sollen möglich sein:_

```cpp
int main() {
    TemperatureSensor t(3, "Raumtemperatur", 2.5);
    t.print();   // z.B. "Raumtemperatur: 22.3 °C"
    std::cout << t.getValue() << std::endl;
}
```

                            {{1-2}}
**********************************

```cpp          Loesung2.cpp
#include <iostream>
#include <string>

// Simulation von analogRead()
int analogRead(int pin) {
    int values[] = {650, 420, 300, 512};
    return values[pin % 4];
}

class AnalogSensor {
  protected:
    int _pin;
    std::string _name;
  public:
    AnalogSensor(int pin, std::string name)
        : _pin(pin), _name(name) {}
    virtual float getValue() = 0;
    virtual void print() {
        std::cout << _name << ": " << getValue() << std::endl;
    }
    virtual ~AnalogSensor() {}
};

class TemperatureSensor : public AnalogSensor {
    float _offset;
  public:
    TemperatureSensor(int pin, std::string name, float offset)
        : AnalogSensor(pin, name), _offset(offset) {}

    float getValue() override {
        int raw = analogRead(_pin);
        return raw * 500.0 / 1023.0 - _offset;
    }

    void print() override {
        std::cout << _name << ": " << getValue() << " °C" << std::endl;
    }
};

int main() {
    TemperatureSensor t(3, "Raumtemperatur", 2.5);
    t.print();
    std::cout << t.getValue() << std::endl;
}
```
@LIA.eval(`["main.cpp"]`, `g++ -Wall main.cpp -o a.out`, `./a.out`)

**********************************

### A3: Kurze Fragestellungen

1. Markieren Sie alle Ganzzahldatentypen in folgender Aufstellung.

   - [( )] std::string
   - [(X)] short
   - [( )] float
   - [( )] bool

2. Welchen Inhalt gibt das folgende Codefragment aus?

   ```cpp
   int werte[] = {10, 20, 30, 40, 50};
   int summe = 0;
   for (int i = 0; i < 5; i += 2)
       summe += werte[i];
   std::cout << summe;
   ```

   [[90]]

3. Was bedeutet das Schlüsselwort `virtual` vor einer Methode in C++?

   [[Die Methode kann in abgeleiteten Klassen ueberschrieben werden und der Aufruf wird zur Laufzeit aufgeloest (dynamische Bindung).]]

4. Schreiben Sie den folgenden C++-Code als Python-Code:

   ```cpp
   int werte[] = {10, 20, 30, 40, 50};
   int summe = 0;
   for (int i = 0; i < 5; i += 2)
       summe += werte[i];
   std::cout << summe;
   ```

   ```python
   werte = [10, 20, 30, 40, 50]

   ```
   @LIA.eval(`["main.py"]`, `none`, `python3 main.py`)

5. Welches Konzept nutzt C++, um die Member einer Klasse vor dem Zugriff aus anderen Klassen zu schützen?

   [[Kapselung]]

6. Mit Hilfe welcher Methoden werden C++-Objekte erstellt?

   - [( )] Destruktoren
   - [(X)] Konstruktoren
   - [( )] private Methoden
   - [( )] `new`


## Finale Worte

> Vielen Dank für Ihre Beteiligung während der Übungen und der Vorlesungen und toi toi toi für die anstehenden Prüfungen!
