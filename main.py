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

# Zadatak 1. Broj ljudi
# Prebrojimo koliko ljudi možemo prikazati na ekranu.
# Nakon toga isprintaj koliko ih može biti. Spremimo broj u varijablu "broj_ljudi"

# Zadatak 2. Lista ljudi
# Kreirajte listu "ljudi" s odgovarajućim brojem ljudi gdje svaki ima element ima vrijednost "boja.zelena"

# Zadatak 3. Crtanje ljudi
# Napiši funkciju "crtaj_ljude()" koja će prikazati sve ljude horizontalno na sredini ekrana.


# Zadatak 4. Izvor zaraze
# Postavite središnjeg čovjeka kao izvora zaraze tako da mu postavite boju na "boja.crvena"


def sirenje_zaraze_covjek(i):
    if i - 1 >= 0:
        if ljudi[i - 1] == boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i - 1] = boja.narancasta
    if i + 1 < len(ljudi):
        if ljudi[i + 1] == boja.zelena and random() > 1 - sansa_zaraze:
            ljudi[i + 1] = boja.narancasta


def osvjezi_zarazeni():
    for i in range(broj_ljudi):
        if ljudi[i] == boja.narancasta:
            ljudi[i] = boja.crvena


# Zadatak 5. Širenje zaraze
# Napiši funkciju "sirenje_zaraze()" koja će proći po svim ljudima i provjeriti jesu li zaraženi.
# Ako jesu, pozvati funckiju "sirenje_zaraze_covjek(i)". Argument funkcije "sirenje_zaraze_covjek()" je indeks
# zaraženog čovjeka.


# Zadatak 6. Broj zaraženih
# Napiši funkciju "broj_zarazenih()" koje će prebrojati koliko ljudi je zaraženo.


# Zadatak 7. Dan kada su svi zaraženi
# Samo jednom ispisati dan kada su svi ljudi zaraženi.
dan = 0
while True:
    # prikazi_tekst("Dan: " + str(dan), "Zaraženi: " + str(broj_zarazenih()))
    # crtaj_ljude()
    # osvjezi_zarazeni()
    # sirenje_zaraze()

    dan = dan + 1

    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
