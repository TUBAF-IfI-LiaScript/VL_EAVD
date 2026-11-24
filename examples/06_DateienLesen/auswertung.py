"""Das lange Skript: zwei Stationen als kopierte Blöcke. Wird in Vorlesung 07
in Funktionen zerlegt.
Aus Vorlesung 06 „Dateien lesen“. Starten im Ordner examples/06_DateienLesen."""

# ---- Fichtelberg ----------------------------------------------------------
hoechst = {}
frost = {}
with open("../../data/fichtelberg/"
          "produkt_klima_tag_18900801_20251231_01358.txt") as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        minimum = float(teile[16])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
        if jahr not in frost:
            frost[jahr] = 0
        if minimum != -999 and minimum < 0:
            frost[jahr] = frost[jahr] + 1

with open("fichtelberg_jahre.csv", "w") as datei:
    datei.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        datei.write(jahr + ";" + str(hoechst[jahr]) + ";"
                    + str(frost[jahr]) + "\n")

# ---- Freiberg -------------------------------------------------------------
hoechst = {}
frost = {}
with open("../../data/freiberg/"
          "produkt_klima_tag_19450701_19930430_01441.txt") as datei:
    datei.readline()
    for zeile in datei:
        teile = zeile.split(";")
        jahr = teile[1][0:4]
        maximum = float(teile[15])
        minimum = float(teile[16])
        if maximum != -999:
            if jahr not in hoechst or maximum > hoechst[jahr]:
                hoechst[jahr] = maximum
        if jahr not in frost:
            frost[jahr] = 0
        if minimum != -999 and minimum < 0:
            frost[jahr] = frost[jahr] + 1

with open("freiberg_jahre.csv", "w") as datei:
    datei.write("jahr;maximum;frosttage\n")
    for jahr in hoechst:
        datei.write(jahr + ";" + str(hoechst[jahr]) + ";"
                    + str(frost[jahr]) + "\n")

# ---- Kontrolle ------------------------------------------------------------
for name in ["fichtelberg_jahre.csv", "freiberg_jahre.csv"]:
    with open(name) as datei:
        zeilen = datei.readlines()
    print(name, len(zeilen) - 1, "Jahre, erste Zeile:", zeilen[1].strip())
