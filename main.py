from crtac import *
from random import random
import time

# moze ici od 20 do min(size_z, size_y)
razmak = 40
sansa_zaraze = 0.8 * 400 / (razmak * razmak)
print("sirina zaraze: ", sansa_zaraze)

broj_ljudi_kolona = int((size_y - razmak) / (razmak + 5)) + 1
broj_ljudi_red = int((size_x - razmak) / razmak) + 1
izvor_x = int(broj_ljudi_red / 2 - 1)
izvor_y = int(broj_ljudi_kolona / 2 - 1)

ljudi = [[Color.green for j in range(broj_ljudi_kolona)]
         for i in range(broj_ljudi_red)]

ljudi[izvor_x][izvor_y] = Color.red


def crtaj_ljude():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            crtaj_osobu(i * razmak + razmak / 2,
                        j * (razmak + 5) + razmak / 2, ljudi[i][j])


def sirenje_zaraze(i, j):
    if i - 1 >= 0:
        if ljudi[i - 1][j] == Color.green and random() > 1 - sansa_zaraze:
            ljudi[i - 1][j] = Color.yellow
    if j - 1 >= 0:
        if ljudi[i][j - 1] == Color.green and random() > 1 - sansa_zaraze:
            ljudi[i][j - 1] = Color.yellow
    if i + 1 < len(ljudi):
        if ljudi[i + 1][j] == Color.green and random() > 1 - sansa_zaraze:
            ljudi[i + 1][j] = Color.yellow
    if j + 1 < len(ljudi[0]):
        if ljudi[i][j + 1] == Color.green and random() > 1 - sansa_zaraze:
            ljudi[i][j + 1] = Color.yellow


# Proci po svim ljudima i provjerit jel su zarazeni?
def update():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Color.red:
                sirenje_zaraze(i, j)


def update_zarazeni():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Color.yellow:
                ljudi[i][j] = Color.red


def broj_zarazenih():
    zarazeni = 0
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            if ljudi[i][j] == Color.red:
                zarazeni = zarazeni + 1
    return zarazeni


dan = 0
while True:
    prikazi_tekst("Dan: " + str(dan), "Zarazeni: " + str(broj_zarazenih()))
    crtaj_ljude()

    update_zarazeni()
    update()
    dan = dan + 1

    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
