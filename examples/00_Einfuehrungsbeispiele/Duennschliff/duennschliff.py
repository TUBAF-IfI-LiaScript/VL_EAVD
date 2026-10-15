# %% Körner in einem Dünnschliff zählen und messen
# Bild: Dünnschliff unter gekreuzten Polarisatoren,
#       Fundus von Prof. Heide, TU Bergakademie Freiberg
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

bild = plt.imread("duennschliff_xpol.png")[:, :, :3]
grau = bild.mean(axis=2)            # Helligkeit: 0 schwarz ... 1 weiß
grau[900:, 640:] = 0                # Maßstab unten rechts ausblenden
UM_PRO_PIXEL = 2000 / 80            # Maßstab: 2000 µm sind 80 Pixel

# %% Annahme: Ein Korn ist alles, was heller ist als die Schwelle
SCHWELLE = 0.45
hell = ndimage.binary_opening(grau > SCHWELLE, iterations=2)  # Krümel weg
koerner, _ = ndimage.label(hell)            # zusammenhängende Flecken
flaeche = np.bincount(koerner.ravel())[1:]  # Pixel je Fleck
flaeche = flaeche[flaeche >= 150]           # sehr kleine Flecken weg
durchmesser = 2 * np.sqrt(flaeche / np.pi) * UM_PRO_PIXEL
probe = ndimage.binary_closing(grau > 0.12, iterations=5)  # Gestein
print(len(flaeche), "Körner, mittlerer Durchmesser (Median):",
      round(np.median(durchmesser)), "µm")
print("Anteil an der Probe:", round(100 * flaeche.sum() / probe.sum()), "%")

# %% Darstellung
fig, ax = plt.subplots(1, 3, figsize=(15, 6))
ax[0].imshow(bild)
ax[0].set_title("Dünnschliff")
ax[1].imshow(hell, cmap="gray")
ax[1].set_title(f"heller als {SCHWELLE}")
ax[2].hist(durchmesser, bins=range(0, 3001, 200), edgecolor="white")
ax[2].set_xlabel("Durchmesser in µm")
ax[2].set_ylabel("Anzahl Körner")
ax[2].set_title("Korngrößen")
for a in ax[:2]:
    a.axis("off")
plt.tight_layout()
plt.show()
