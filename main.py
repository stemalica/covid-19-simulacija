from crtac import *
from pygame.locals import *
import boja
from random import random
import time
import sys

print("Veličina ekrana: " + str(size_x) + "," + str(size_y))

# moze ici od 20 do min(size_z, size_y)
razmak = 40
sansa_zaraze = 0.9 * 20 / razmak
print("Šansa zaraze: ", sansa_zaraze)

# 1. Prebroji koliko ljudi možemo prikazati na ekranu. Nakon toga isprintaj koliko ih može biti
broj_ljudi = int(size_x / razmak)

# 2. Kreirajte listu "ljudi" s odgovarajućim brojem ljudi gdje svaki ima
ljudi = [boja.zelena] * broj_ljudi


# 3. Napiši funkciju crtaj_ljude koja će prikazati sve ljude horizontalno na sredini ekrana
def crtaj_ljude():
    for i in range(broj_ljudi):
        crtaj_osobu(i * razmak + razmak / 2.0, size_y / 2.0, ljudi[i])


# 4. Postavi jednog covjeka za izvor koji je u sredini ekrana
izvor_pozicija = int(broj_ljudi / 2 - 1)
ljudi[izvor_pozicija] = boja.crvena


def sirenje_zaraze_covjek(i):
    if i - 1 >= 0:
        if ljudi[i - 1] == boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i - 1] = boja.narancasta
    if i + 1 < len(ljudi):
        if ljudi[i + 1] == boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i + 1] = boja.narancasta


# 5. Širenje zaraze. Napiši funkciju `sirenje_zaraze()` koja će proći po svim ljudima i provjeriti jesu li zaraženi.
# Ako je, pozvati funckiju `sirenje_zaraze_covjek`
def sirenje_zaraze():
    for i in range(broj_ljudi):
        if ljudi[i] == boja.crvena:
            sirenje_zaraze_covjek(i)


# 6. Napiši funkciju za provjeru broja zaraženih.
def broj_zarazenih():
    zarazeni = 0
    for i in range(broj_ljudi):
        if ljudi[i] == boja.crvena:
            zarazeni = zarazeni + 1
    return zarazeni


# 7. Dodatak. Trenutno ne vidimo tko je zadnji zaraženi i ljudi koji su trenutnog dana bili zaraženi mogu istog dana
# zaraziti druge. Potrebno dodati jedan međukorak s kojim se pamti ljude koji su trenutno zaraženi (boje.narancasta)
def osvjezi_zarazeni():
    for i in range(broj_ljudi):
        if ljudi[i] == boja.narancasta:
            ljudi[i] = boja.crvena


dan = 0
svi_zarazeni = False
while True:
    prikazi_tekst("Dan: " + str(dan), "Zaraženi: " + str(broj_zarazenih()))
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

    if broj_zarazenih() == broj_ljudi and not svi_zarazeni:
        print("Svi ljudi su zaraženi u " + str(dan) + " dana.")
        svi_zarazeni = True
