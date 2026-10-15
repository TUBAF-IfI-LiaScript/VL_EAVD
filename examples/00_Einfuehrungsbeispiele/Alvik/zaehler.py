"""Personenzähler mit dem Arduino Alvik: Auswertung und Live-Histogramm.

Live (Roboter per USB angeschlossen, mpremote installiert):

    python zaehler.py --live

Eine aufgezeichnete Rohdatendatei erneut abspielen (z. B. 20-fach schnell):

    python zaehler.py --abspielen rohdaten_2026-10-19.csv --tempo 20

Der Roboter liefert nur Rohdaten (alvik_messung.py). Erkannt und gezählt wird
hier, damit live und beim Abspielen genau dieselbe Auswertung läuft.

Aufbau: Der Roboter steht an einem Türrahmen und schaut auf einen Hintergrund
in etwa 1–1,5 m (gegenüberliegender Rahmen, Wand, Stuhl). Zonen ohne
Hintergrund halten bei dieser Firmware ihren letzten Wert fest.
"""
import argparse
import datetime as dt
import os
import queue
import signal
import subprocess
import sys
import threading
import time

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.ticker import MaxNLocator

HIER = os.path.dirname(os.path.abspath(__file__))
SPALTEN = ["links", "mitte_links", "mitte", "mitte_rechts", "rechts", "oben", "unten"]
INNEN = [1, 2, 3]            # mitte_links, mitte, mitte_rechts
ANTEIL = 0.8                 # belegt, wenn näher als 80 % des Hintergrunds
NACHLAUF_MS = 400            # so lange müssen alle Zonen frei sein
HINTERGRUND_N = 60           # Messungen für den gleitenden Hintergrund
MAX_DAUER_MS = 6000          # länger belegt: keine Person, sondern neuer Hintergrund
REIN_VON = "links"           # wer zuerst links auftaucht, kommt herein


# ---------------------------------------------------------------- Erkennung
class Erkennung:
    """Erkennt Durchgänge und ihre Richtung aus den drei inneren Zonen."""

    def __init__(self, rein_von=REIN_VON):
        self.rein_von = rein_von
        self.verlauf = [[] for _ in INNEN]   # letzte freie Messungen je Zone
        self.ereignis = None                 # {Zone: erste Belegung in ms}
        self.beginn = None                   # Beginn des laufenden Ereignisses
        self.frei_seit = None

    def hintergrund(self, k):
        # unteres Fünftel statt Median: Sieht eine Zone den Hintergrund nur
        # zeitweise (Lücken, Kanten), zählt der nahe Wert
        werte = sorted(self.verlauf[k])
        return werte[len(werte) // 5] if len(werte) >= 10 else None

    def belegt(self, k, wert):
        h = self.hintergrund(k)
        return h is not None and 0 < wert < ANTEIL * h

    def messung(self, ms, werte):
        """Verarbeitet eine Messung; gibt 'rein', 'raus', 'unklar' oder None."""
        innen = [werte[i] for i in INNEN]
        belegt = [self.belegt(k, w) for k, w in enumerate(innen)]
        if any(belegt):
            if self.ereignis is None:
                self.ereignis, self.beginn = {}, ms
            if ms - self.beginn > MAX_DAUER_MS:
                # z. B. Stuhl verschoben: aktuelle Werte als Hintergrund übernehmen
                self.verlauf = [[w] * 10 if w > 0 else [] for w in innen]
                self.ereignis = self.frei_seit = None
                return None
            for k, b in enumerate(belegt):
                if b and k not in self.ereignis:
                    self.ereignis[k] = ms
            self.frei_seit = None
            return None
        for k, w in enumerate(innen):        # freie Messung: Hintergrund lernen
            if w > 0:
                self.verlauf[k] = (self.verlauf[k] + [w])[-HINTERGRUND_N:]
        if self.ereignis is None:
            return None
        if self.frei_seit is None:
            self.frei_seit = ms
        if ms - self.frei_seit < NACHLAUF_MS:
            return None
        ergebnis = self.richtung(self.ereignis)
        self.ereignis = None
        return ergebnis

    def richtung(self, erste):
        links, rechts = erste.get(0), erste.get(2)
        if links is None or rechts is None or links == rechts:
            return "unklar"
        von = "links" if links < rechts else "rechts"
        return "rein" if von == self.rein_von else "raus"


# ------------------------------------------------------------------ Quellen
def zeile_lesen(text):
    """'ms;l;cl;c;cr;r;o;u' -> (ms, [werte]) oder None für andere Zeilen."""
    teile = text.strip().split(";")
    if len(teile) != 8 or not teile[0].isdigit():
        return None
    return int(teile[0]), [int(t) if t else 0 for t in teile[1:]]


def live(ziel, prozess):
    """Liest die Zeilen von alvik_messung.py, das auf dem Roboter läuft."""
    for text in prozess.stdout:
        gelesen = zeile_lesen(text)
        if gelesen:
            ziel.put((time.time(),) + gelesen)


def abspielen(ziel, datei, tempo):
    """Liest eine Rohdatendatei und gibt sie im Originaltakt (× tempo) aus."""
    start_ms = start_t = None
    with open(datei, encoding="utf-8") as f:
        f.readline()
        for text in f:
            teile = text.strip().split(";")
            empfangen = dt.datetime.fromisoformat(teile[0]).timestamp()
            ms, werte = int(teile[1]), [int(t) if t else 0 for t in teile[2:]]
            if start_ms is None:
                start_ms, start_t = ms, time.time()
            warten = start_t + (ms - start_ms) / 1000 / tempo - time.time()
            if warten > 0:
                time.sleep(warten)
            ziel.put((empfangen, ms, werte))


# ------------------------------------------------------------------- Anzeige
def main():
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    quelle = p.add_mutually_exclusive_group(required=True)
    quelle.add_argument("--live", action="store_true")
    quelle.add_argument("--abspielen", metavar="DATEI")
    p.add_argument("--tempo", type=float, default=1.0)
    p.add_argument("--beginn", default="16:15", help="Vorlesungsbeginn HH:MM")
    p.add_argument("--rein-von", choices=["links", "rechts"], default=REIN_VON,
                   help="Von welcher Seite kommt, wer hereinkommt (Blick hinter dem Roboter)")
    p.add_argument("--port", default="/dev/ttyACM0")
    p.add_argument("--mpremote", default="mpremote")
    a = p.parse_args()

    eingang = queue.Queue()
    if a.live:
        heute = dt.date.today().isoformat()
        rohdatei = open(f"rohdaten_{heute}.csv", "a", encoding="utf-8")
        zaehldatei = open(f"zaehlungen_{heute}.csv", "a", encoding="utf-8")
        if rohdatei.tell() == 0:
            rohdatei.write("empfangen;ms_roboter;" + ";".join(SPALTEN) + "\n")
        if zaehldatei.tell() == 0:
            zaehldatei.write("zeit;richtung\n")
        befehl = [a.mpremote, "connect", a.port, "run", os.path.join(HIER, "alvik_messung.py")]
        prozess = subprocess.Popen(befehl, stdout=subprocess.PIPE, text=True, bufsize=1)
        faden = threading.Thread(target=live, args=(eingang, prozess), daemon=True)
    else:
        rohdatei = zaehldatei = prozess = None
        faden = threading.Thread(target=abspielen, args=(eingang, a.abspielen, a.tempo), daemon=True)
    faden.start()

    erkennung = Erkennung(a.rein_von)
    versatz = None              # Uhrzeit - Roboterzeit, kleinster gesehener Wert
    zeiten, zaehler, letzte = {"rein": [], "raus": []}, {"rein": 0, "raus": 0, "unklar": 0}, [None]
    uhr = {"start": None, "jetzt": None}       # Zeit der ersten und letzten Messung

    fig, (oben, unten) = plt.subplots(2, 1, figsize=(11, 8), height_ratios=[3, 1])
    fig.canvas.manager.set_window_title("Personenzähler")

    def aktualisieren(_):
        nonlocal versatz
        while not eingang.empty():
            empfangen, ms, werte = eingang.get()
            # Zeilen kommen gepuffert an: der kleinste Abstand ist der echte
            versatz = min(versatz, empfangen - ms / 1000) if versatz else empfangen - ms / 1000
            zeit = dt.datetime.fromtimestamp(versatz + ms / 1000)
            uhr["start"] = uhr["start"] or zeit
            uhr["jetzt"] = zeit
            if rohdatei:
                rohdatei.write(dt.datetime.fromtimestamp(empfangen).isoformat(timespec="milliseconds")
                               + f";{ms};" + ";".join(map(str, werte)) + "\n")
            letzte[0] = werte
            ergebnis = erkennung.messung(ms, werte)
            if ergebnis:
                zaehler[ergebnis] += 1
                if ergebnis in zeiten:
                    zeiten[ergebnis].append(zeit)
                if zaehldatei:
                    zaehldatei.write(f"{zeit.isoformat(timespec='seconds')};{ergebnis}\n")
                    zaehldatei.flush()
        if rohdatei:
            rohdatei.flush()     # bei einem Absturz bleiben die Rohdaten erhalten
        if prozess and prozess.poll() is not None and not fig.get_suptitle():
            # mpremote endet, wenn das Kabel abgezogen wird – sonst bliebe die
            # Anzeige einfach stehen
            fig.suptitle("Verbindung zum Roboter verloren – Kabel prüfen, "
                         "Fenster schließen, neu starten", color="#c2462e",
                         fontweight="bold")
        if uhr["start"]:
            zeichnen(oben, unten, a.beginn, uhr, zeiten, zaehler, letzte[0], erkennung)

    animation = FuncAnimation(fig, aktualisieren, interval=200, cache_frame_data=False)
    plt.show()
    if prozess:
        # wie Strg+C: mpremote unterbricht das Programm auf dem Roboter,
        # der schaltet die LEDs aus und hält an
        prozess.send_signal(signal.SIGINT)
        try:
            prozess.wait(timeout=5)
        except subprocess.TimeoutExpired:
            prozess.kill()
    for d in (rohdatei, zaehldatei):
        if d:
            d.close()


FENSTER = 2                    # Minuten pro Balken
DAUER = 30                     # Zeitraum in Minuten; danach wächst die Achse


def minuten(t, bezug):
    return (t - bezug).total_seconds() / 60


def zeichnen(oben, unten, beginn, uhr, zeiten, zaehler, werte, erkennung):
    """Oben: Zeit nach rechts ab Start, rein nach oben, raus nach unten. Unten: Zonen.

    Die ersten 30 Minuten füllen sich von links; danach wird die Achse länger,
    damit die Ankunftsphase auch am Ende der Vorlesung sichtbar bleibt.
    """
    oben.clear()
    start = uhr["start"].replace(second=0, microsecond=0)
    ende = max(DAUER, (int(minuten(uhr["jetzt"], start)) // FENSTER + 1) * FENSTER)
    grenzen = list(range(0, ende + 1, FENSTER))
    anzahl = {}
    for richtung, liste in zeiten.items():
        anzahl[richtung] = [0] * (len(grenzen) - 1)
        for t in liste:
            m = minuten(t, start)
            if 0 <= m < ende:
                anzahl[richtung][int(m // FENSTER)] += 1
    mitten = [g + FENSTER / 2 for g in grenzen[:-1]]
    oben.bar(mitten, anzahl["rein"], width=FENSTER * 0.9, color="#3a6ea5", label="rein")
    oben.bar(mitten, [-n for n in anzahl["raus"]], width=FENSTER * 0.9,
             color="#e08a2c", label="raus")
    hoehe = max([5] + anzahl["rein"] + anzahl["raus"]) + 1
    oben.set_ylim(-hoehe, hoehe)
    oben.set_xlim(0, ende)
    oben.axhline(0, color="black", lw=0.8)
    jetzt = minuten(uhr["jetzt"], start)
    oben.axvline(jetzt, color="grey", lw=1, ls="--")
    h, m = map(int, beginn.split(":"))
    vorlesung = minuten(start.replace(hour=h, minute=m), start)
    if 0 <= vorlesung <= ende:
        oben.axvline(vorlesung, color="#c2462e", lw=2)
        oben.text(vorlesung + 0.2, hoehe * 0.88, f"Beginn {beginn}", color="#c2462e")
    marken = grenzen[::max(2, len(grenzen) // 8 // 2 * 2)]
    oben.set_xticks(marken)
    oben.set_xticklabels([(start + dt.timedelta(minutes=g)).strftime("%H:%M") for g in marken])
    oben.set_xlabel("Uhrzeit")
    oben.yaxis.set_major_locator(MaxNLocator(integer=True))
    oben.set_yticks(oben.get_yticks())
    oben.set_yticklabels([str(abs(int(y))) for y in oben.get_yticks()])
    oben.set_ylabel(f"Personen je {FENSTER} Minuten\n\u2193 raus | rein \u2191")
    oben.legend(loc="upper right")
    oben.set_title(f"Wann erscheinen Sie?   rein: {zaehler['rein']}   raus: {zaehler['raus']}"
                   f"   unklar: {zaehler['unklar']}")
    unten.clear()
    if werte:
        namen = ["mitte_links", "mitte", "mitte_rechts"]
        abstand = [werte[i] / 10 for i in INNEN]
        grund = [(erkennung.hintergrund(k) or 0) / 10 for k in range(3)]
        farben = ["#c2462e" if erkennung.belegt(k, werte[i]) else "#3a6ea5"
                  for k, i in enumerate(INNEN)]
        unten.barh(namen[::-1], abstand[::-1], color=farben[::-1])
        unten.scatter(grund[::-1], namen[::-1], marker="|", s=400, color="black")
        unten.set_xlim(0, 250)
        unten.set_xlabel("Abstand je Zone in cm (Strich: Hintergrund, rot: belegt)")


if __name__ == "__main__":
    main()
