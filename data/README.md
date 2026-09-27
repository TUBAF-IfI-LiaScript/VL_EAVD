# Datensätze

Alle Messreihen stammen vom Deutschen Wetterdienst (DWD), [Climate Data Center](https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/daily/), und stehen unter der Lizenz [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Die Dateien sind unverändert übernommen (Stand: Abruf September 2026), abgeleitete Dateien sind als solche gekennzeichnet.

Fehlwerte sind in allen DWD-Dateien mit `-999` kodiert. Die Spaltenbedeutung beschreibt der DWD in den `DESCRIPTION_*.pdf`-Dateien des jeweiligen Produktverzeichnisses.

## `fichtelberg/` — Station 01358, 1213 m

Roter Faden der Veranstaltung.

| Datei                                             | Inhalt                                      | Zeitraum            | Zeilen |
| :------------------------------------------------ | :------------------------------------------ | :------------------ | -----: |
| `produkt_klima_tag_18900801_20251231_01358.txt`   | Klima-Tageswerte (KL), Rohformat            | 01.08.1890 – 31.12.2025 | 47.595 |
| `fichtelberg_2024.csv`                            | **abgeleitet:** Jahr 2024, Spalten Datum, Tagesmittel (`TMK`), Minimum (`TNK`), Maximum (`TXK`), Dezimalkomma — für die Tabellenkalkulation in Vorlesung 01 | 2024 | 366 |
| `2024_tagesmittel.txt`, `2024_minimum.txt`, `2024_maximum.txt` | **abgeleitet:** je eine Spalte 2024, ein Wert pro Zeile, Dezimalpunkt — für VL 03/04 | 2024 | 366 |
| `2015_2024_datum.txt`, `2015_2024_maximum.txt` | **abgeleitet:** Datum (JJJJ-MM-TT) und Tagesmaximum `TXK`, ein Wert pro Zeile — für VL 05 | 2015–2024 | 3.653 |
| `Metadaten_Geographie_01358.txt`                  | Stationshistorie (Lage, Höhe)               |                     |        |

Besonderheiten: Lücken vom 11.12.1890 bis 31.03.1891 und vom 11.12.1910 bis 30.09.1915; einzelne `-999` in den Temperaturspalten.

## `freiberg/` — Station 01441

Lokaler Zusatzdatensatz für Übungen und für den Stationsvergleich in Vorlesung 14.

| Datei                                             | Inhalt                                      | Zeitraum            | Zeilen |
| :------------------------------------------------ | :------------------------------------------ | :------------------ | -----: |
| `produkt_klima_tag_19450701_19930430_01441.txt`   | Klima-Tageswerte (KL), Rohformat            | 01.07.1945 – 30.04.1993 | 17.410 |
| `produkt_nieder_tag_19450701_20251231_01441.txt`  | Niederschlags-Tageswerte (RR), Rohformat    | 01.07.1945 – 31.12.2025 | 21.242 |
| `Metadaten_Geographie_01441.txt`                  | Stationshistorie (Lage, Höhe)               |                     |        |
| `Metadaten_Geraete_Niederschlagshoehe_01441.txt`  | eingesetzte Niederschlagsmesser             |                     |        |
| `Metadaten_Parameter_nieder_tag_01441.txt`        | Datenquelle und Tagesdefinition je Zeitraum |                     |        |
| `Metadaten_Stationsname_Betreibername_01441.txt`  | Betreiber je Zeitraum                       |                     |        |

Besonderheiten:

* Die Klimastation wurde im April 1993 geschlossen. Seit Dezember 2014 misst an einem **neuen Standort** (416 m statt 380 m, rund 5 km weiter westlich) nur noch Niederschlag.
* Niederschlag: Lücke von Mai 1993 bis März 2015, dazu einzelne fehlende Tage (u. a. Juni 2015, August 2022).
* Klima: Tagesminimum `TNK` fehlt 1948 vollständig, 1946, 1950 und 1951 teilweise.

**Der Standortwechsel als Lehrbeispiel (Vorlesung 14).** Vor und nach der Lücke steht dieselbe Stationsnummer mit identischem Dateiformat — gemessen wird aber etwas anderes:

| Merkmal                    | bis 1993                                        | ab 2015                                          |
| :------------------------- | :---------------------------------------------- | :----------------------------------------------- |
| Standort                   | 380 m, 13,34° O                                 | 416 m, 13,27° O                                  |
| Messgerät                  | Hellmann, manuell abgelesen                     | PLUVIO, ab 2020/22 rain[e]H3 (Wägung, elektronisch) |
| Messtag                    | 07:00 bis 07:00 Uhr Folgetag (Ortszeit)         | aus der SYNOP-Meldung von 06 UTC                 |
| Betreiber                  | Wetterdienst, 1950–1990 Meteorologischer Dienst der DDR, ab 1991 DWD | DWD                                              |
| Qualitätsniveau `QN_6`     | 1, 5, 9, 10                                     | 3, 9                                             |
| Niederschlagsform `RSF`    | Codes 0, 1, 4, 6, 7, 8                          | nur 0 und 4                                      |
| Schneehöhe `SH_TAG`        | nahezu vollständig                              | an 43 % der Tage `-999`                          |
| mittlere Jahressumme       | 758 mm (1946–1992)                              | 668 mm (2016–2025)                               |

Ob der Rückgang Klima oder Messung ist, lässt sich mit Freiberg allein nicht entscheiden. Der Vergleich mit Chemnitz (`../chemnitz/`) klärt es: In 1976–1987, als beide Stationen Hellmann-Geräte nutzten und Chemnitz bereits am heutigen Ort stand, lag Freiberg in jedem Jahr über Chemnitz (Verhältnis 1,02–1,26, Mittel 1,13). Für 2016–2025 liegt das Verhältnis bei 0,96 — bei praktisch unveränderter Chemnitzer Jahressumme (1976–1992: 686 mm, 2016–2025: 691 mm).

## `chemnitz/` — Station 00853

Referenzstation für den Freiberger Standortwechsel.

| Datei                                             | Inhalt                                      | Zeitraum            | Zeilen |
| :------------------------------------------------ | :------------------------------------------ | :------------------ | -----: |
| `produkt_klima_tag_18820101_20251231_00853.txt`   | Klima-Tageswerte (KL), Rohformat; Niederschlag in `RSK` | 01.01.1882 – 31.12.2025 | 39.841 |
| `Metadaten_Geographie_00853.txt`                  | Stationshistorie (Lage, Höhe)               |                     |        |
| `Metadaten_Geraete_Niederschlagshoehe_00853.txt`  | eingesetzte Niederschlagsmesser             |                     |        |
| `Metadaten_Stationsname_Betreibername_00853.txt`  | Betreiber je Zeitraum                       |                     |        |

Besonderheiten:

* Lücken von Juni 1901 bis Dezember 1934 und von März 1945 bis Mai 1946.
* Standortwechsel im Mai 1976 (357 m → 416 m). Das Verhältnis Freiberg/Chemnitz springt dabei von 1,04 (1946–1975) auf 1,13 — auch die Referenz ist also nicht über den ganzen Zeitraum homogen.
* Gerätewechsel am heutigen Standort: Hellmann → NG 200 (1988) → PLUVIO (2006) → rain[e]H3 (2019).
