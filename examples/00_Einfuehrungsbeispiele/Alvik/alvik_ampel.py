# Läuft auf dem Arduino Alvik (MicroPython). Testprogramm zur Aufstellung:
# Die LEDs zeigen, ob die Frontzonen etwas näher als GRENZE_MM sehen.
#   linke LED  rot: links oder mitte_links (oder mitte) erkennt etwas
#   rechte LED rot: rechts oder mitte_rechts (oder mitte) erkennt etwas
#   grün: nichts erkannt
# Zusätzlich wird jede neue Messung wie in alvik_messung.py ausgegeben.
# Der Roboter fährt nicht.

from arduino_alvik import ArduinoAlvik
from time import ticks_ms, sleep_ms

GRENZE_MM = 1200
PAUSE_MS = 50

alvik = ArduinoAlvik()
alvik.begin()


def erkannt(wert):
    # 0 bedeutet bei dieser Firmware meist "kein Ziel"
    return wert is not None and 0 < wert < GRENZE_MM


def setze(led, belegt):
    if belegt:
        led.set_color(1, 0, 0)
    else:
        led.set_color(0, 1, 0)


print("# alvik_ampel, Grenze", GRENZE_MM, "mm")
print("ms;links;mitte_links;mitte;mitte_rechts;rechts;oben;unten")
letzte = None
try:
    while True:
        l, cl, c, cr, r = alvik.get_distance("mm")
        werte = (l, cl, c, cr, r, alvik.get_distance_top("mm"),
                 alvik.get_distance_bottom("mm"))
        setze(alvik.left_led, erkannt(l) or erkannt(cl) or erkannt(c))
        setze(alvik.right_led, erkannt(r) or erkannt(cr) or erkannt(c))
        if werte != letzte:
            print(str(ticks_ms()) + ";" + ";".join(
                "" if w is None else str(int(w)) for w in werte))
            letzte = werte
        sleep_ms(PAUSE_MS)
finally:
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)
    alvik.stop()
