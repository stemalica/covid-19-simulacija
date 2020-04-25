from crtac import *
from pygame.locals import *
from boje import *
from random import random
import time
import sys

# moze ici od 20 do min(size_z, size_y)
razmak = 40
sansa_zaraze = 0.8 * 400 / (razmak * razmak)
print("sirina zaraze: ", sansa_zaraze)

broj_ljudi_kolona = int((size_y - razmak) / (razmak + 5)) + 1
broj_ljudi_red = int((size_x - razmak) / razmak) + 1

ljudi = [[Boja.zelena for j in range(broj_ljudi_kolona)]
         for i in range(broj_ljudi_red)]

# Postavi jednog covjeka za izvor koji je u sredini ekrana
izvor_x = int(broj_ljudi_red / 2 - 1)
izvor_y = int(broj_ljudi_kolona / 2 - 1)
ljudi[izvor_x][izvor_y] = Boja.crvena


def crtaj_ljude():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            crtaj_osobu(i * razmak + razmak / 2,
                        j * (razmak + 5) + razmak / 2, ljudi[i][j])


def sirenje_zaraze_covjek(i, j):
    if i - 1 >= 0:
        if ljudi[i - 1][j] == Boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i - 1][j] = Boja.zuta
    if j - 1 >= 0:
        if ljudi[i][j - 1] == Boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i][j - 1] = Boja.zuta
    if i + 1 < len(ljudi):
        if ljudi[i + 1][j] == Boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i + 1][j] = Boja.zuta
    if j + 1 < len(ljudi[0]):
        if ljudi[i][j + 1] == Boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i][j + 1] = Boja.zuta


# Proči po svim ljudima i proširiti zarazu
def sirenje_zaraze():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Boja.crvena:
                sirenje_zaraze_covjek(i, j)


def osvjezi_zarazeni():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Boja.zuta:
                ljudi[i][j] = Boja.crvena


def broj_zarazenih():
    zarazeni = 0
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Boja.crvena:
                zarazeni = zarazeni + 1
    return zarazeni


dan = 0
svi_zarazeni = False
while True:
    prikazi_tekst("Dan: " + str(dan), "Zarazeni: " + str(broj_zarazenih()))
    crtaj_ljude()

    osvjezi_zarazeni()
    sirenje_zaraze()
    dan = dan + 1

    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

    if broj_zarazenih() == broj_ljudi_kolona * broj_ljudi_red and not svi_zarazeni:
        print("Svi ljudi su zaraženi u " + str(dan) + " dana.")
        svi_zarazeni = True
