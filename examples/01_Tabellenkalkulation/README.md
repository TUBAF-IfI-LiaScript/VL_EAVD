# Lösungen zu Vorlesung 01: Tabellenkalkulation

Lösungen der Aufgaben 1 und 2 aus [Vorlesung 01](../../01_VomProblemZumProgramm.md) als LibreOffice-Tabellen (`.ods`, öffnen auch Excel und Google Sheets). Klicken Sie auf eine Ergebniszelle, um die Formel zu sehen; daneben steht sie jeweils auch als Text.

| Datei | Daten | Inhalt |
| :---- | :---- | :----- |
| `Aufgabe1_Fichtelberg_Loesung.ods` | `data/fichtelberg/fichtelberg_2024.csv` | Jahresmittel, Frosttage |
| `Aufgabe2_Personenzaehler_Loesung.ods` | `examples/00_Einfuehrungsbeispiele/Alvik/zaehlungen_2026-10-19.csv` | Zählung gesamt und nach 16:15, Durchgänge je Minute |
| `VL01_Daten.zip` | alle drei Datensätze aus VL 01 | zum Herunterladen statt Anzeigen im Browser, mit `LIESMICH.txt` (Quellen, Lizenz) |
| `Loop.ods` | zwölf Zufallszahlen | Vorlage ohne Formeln für den Abschnitt „Ist das schon programmieren?“: Bedingung `=WENN(A2<0; 1; 0)` nach unten ziehen, dann `=SUMME(B2:B13)` (Ergebnis: 7) |

In Aufgabe 2 erkennt LibreOffice den Zeitstempel `2026-10-19T16:15:27` beim Öffnen als Datum mit Uhrzeit; die Uhrzeit liefern dann `STUNDE`, `MINUTE` und `SEKUNDE`. Bleibt er Text (z. B. in Excel), hilft `=ZEITWERT(TEIL(A2;12;8))`.
