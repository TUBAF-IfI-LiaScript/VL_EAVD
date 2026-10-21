# Kurslandkarte und PDFs der freigegebenen Vorlesungen (FREIGEGEBEN in kurslandkarte/erzeuge.py)
#   make         fehlende/veraltete PDFs mit liaex nach docs/pdf/, dann Karte und Startseite
#   make karte   nur Karte und Startseite
# Ein PDF wird neu erzeugt, wenn seine Vorlesung neuer ist (gemeinsamer Kern invivis Kurslandkarte).

all:
	python3 kurslandkarte/erzeuge.py --pdf

karte:
	python3 kurslandkarte/erzeuge.py

.PHONY: all karte
