# Läuft auf dem Arduino Alvik (MicroPython).
# Gibt jede neue Messung der Abstandssensoren als Textzeile über USB aus:
#
#   ms;links;mitte_links;mitte;mitte_rechts;rechts;oben;unten
#
# ms = Millisekunden seit dem Start des Roboters (er hat keine Uhr),
# Abstände in Millimetern, leeres Feld = kein Messwert.
# Der Roboter fährt nicht. Gestartet wird vom Laptop aus mit
#   mpremote connect /dev/ttyACM0 run alvik_messung.py

from arduino_alvik import ArduinoAlvik
from time import ticks_ms, sleep_ms

PAUSE_MS = 50   # nicht kleiner: sonst bremst die Schleife das Auslesen aus

alvik = ArduinoAlvik()
alvik.begin()
alvik.left_led.set_color(0, 1, 0)
alvik.right_led.set_color(0, 1, 0)


def als_text(wert):
    return "" if wert is None else str(int(wert))


print("# alvik_messung")
print("ms;links;mitte_links;mitte;mitte_rechts;rechts;oben;unten")
letzte = None
try:
    while True:
        werte = alvik.get_distance("mm") + (alvik.get_distance_top("mm"),
                                            alvik.get_distance_bottom("mm"))
        if werte != letzte:
            print(str(ticks_ms()) + ";" + ";".join(als_text(w) for w in werte))
            letzte = werte
        sleep_ms(PAUSE_MS)
finally:
    alvik.left_led.set_color(0, 0, 0)
    alvik.right_led.set_color(0, 0, 0)
    alvik.stop()
