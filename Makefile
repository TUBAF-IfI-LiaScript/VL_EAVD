# Kurslandkarte und PDFs der freigegebenen Vorlesungen (FREIGEGEBEN in kurslandkarte/erzeuge.py)
#   make         PDFs, dann Karte (die Karte verlinkt vorhandene PDFs)
#   make pdf     PDFs mit dem LiaScript-Exporter (liaex) nach docs/pdf/
#   make karte   Kurslandkarte nach docs/kurslandkarte/
# Ein PDF wird neu erzeugt, wenn seine Vorlesung neuer ist.

FREI := $(shell python3 kurslandkarte/erzeuge.py --freigegeben)
PDFS := $(patsubst %.md,docs/pdf/%.pdf,$(FREI))

all: pdf karte

pdf: $(PDFS)

docs/pdf/%.pdf: %.md
	@mkdir -p docs/pdf
	liaex -i $< -f pdf -o docs/pdf/$* --pdf-timeout 30000

karte:
	python3 kurslandkarte/erzeuge.py

.PHONY: all pdf karte
