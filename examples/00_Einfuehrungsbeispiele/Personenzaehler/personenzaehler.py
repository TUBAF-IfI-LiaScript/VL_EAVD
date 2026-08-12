# Personenzähler mit Ultraschallsensor (HC-SR04)
#
# MicroPython-Portierung von Personenzaehler.ino
# Getestet auf ESP32; für andere Boards ggf. die Pin-Nummern anpassen.

from machine import Pin, time_pulse_us
import time

PIN_TRIGGER = 12
PIN_ECHO = 13

# Überwachungsbereich in cm
RANGE_MIN = 60      # Untere Grenze
RANGE_MAX = 200     # Obere Grenze

DEBOUNCE_TIME = 1000        # ms - Mindestzeit zwischen Zählungen
STABILIZATION_DELAY = 50    # ms

trigger = Pin(PIN_TRIGGER, Pin.OUT)
echo = Pin(PIN_ECHO, Pin.IN)

person_detected = False
people_count = 0
last_count_time = 0


def get_distance():
    """Misst die Entfernung in cm.

    Gibt 0 zurück, wenn kein Echo ankommt (Timeout nach 25 ms, ca. 4 m).
    """
    trigger.value(0)
    time.sleep_us(2)
    trigger.value(1)
    time.sleep_us(10)
    trigger.value(0)

    duration = time_pulse_us(echo, 1, 25000)
    if duration < 0:            # Timeout: nichts im Messbereich
        return 0
    return duration // 58


print("Person Counter with defined range started")

while True:
    distance = get_distance()
    current_time = time.ticks_ms()

    # Prüfen, ob sich etwas im Überwachungsbereich befindet
    in_range = RANGE_MIN <= distance <= RANGE_MAX

    # Eintritt in den Bereich erkannt
    if in_range and not person_detected:
        person_detected = True
        print("Person entered monitoring zone")

    # Verlassen des Bereichs
    if not in_range and person_detected:
        if time.ticks_diff(current_time, last_count_time) > DEBOUNCE_TIME:
            people_count += 1
            last_count_time = current_time
            print("Person counted. Total =", people_count)
        person_detected = False

    time.sleep_ms(STABILIZATION_DELAY)
