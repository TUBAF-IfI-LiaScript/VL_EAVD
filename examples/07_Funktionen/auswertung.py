"""Das lange Skript aus Vorlesung 06, in Funktionen zerlegt.

Wertet jede Station aus und schreibt eine Datei <station>_jahre.csv mit
Höchstwert und Frosttagen pro Jahr. Jahre mit weniger als MINDESTTAGE
Messtagen bekommen keinen Frostwert. Starten Sie das Programm in diesem
Ordner, die Daten liegen in ../../data/.
"""

MINDESTTAGE = 300          # weniger Messtage: kein Frostwert

STATIONEN = {
    "fichtelberg": ("../../data/fichtelberg/"
                    "produkt_klima_tag_18900801_20251231_01358.txt"),
    "freiberg": ("../../data/freiberg/"
                 "produkt_klima_tag_19450701_19930430_01441.txt"),
    "chemnitz": ("../../data/chemnitz/"
                 "produkt_klima_tag_18820101_20251231_00853.txt"),
}


def zerlege_zeile(zeile):
    """Liefert Jahr, Tagesmaximum und Tagesminimum einer DWD-Zeile."""
    teile = zeile.split(";")
    return teile[1][0:4], float(teile[15]), float(teile[16])


def auswerten(dateiname):
    """Höchstwert, Frosttage und Messtage pro Jahr."""
    hoechst = {}
    frost = {}
    messtage = {}
    with open(dateiname) as datei:
        datei.readline()
        for zeile in datei:
            jahr, maximum, minimum = zerlege_zeile(zeile)
            if jahr not in frost:
                frost[jahr] = 0
                messtage[jahr] = 0
            if maximum != -999:
                if jahr not in hoechst or maximum > hoechst[jahr]:
                    hoechst[jahr] = maximum
            if minimum != -999:
                messtage[jahr] = messtage[jahr] + 1
                if minimum < 0:
                    frost[jahr] = frost[jahr] + 1
    return hoechst, frost, messtage


def schreibe_ergebnis(name, hoechst, frost, messtage):
    """Eine Zeile pro Jahr; ohne Frostwert, wenn zu wenig gemessen wurde."""
    with open(name, "w") as datei:
        datei.write("jahr;maximum;frosttage\n")
        for jahr in hoechst:
            if messtage[jahr] >= MINDESTTAGE:
                datei.write(jahr + ";" + str(hoechst[jahr]) + ";"
                            + str(frost[jahr]) + "\n")
            else:
                datei.write(jahr + ";" + str(hoechst[jahr]) + ";\n")


for station in STATIONEN:
    hoechst, frost, messtage = auswerten(STATIONEN[station])
    schreibe_ergebnis(station + "_jahre.csv", hoechst, frost, messtage)
    print(station, len(hoechst), "Jahre ausgewertet")
