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

# 2. Kreirajte listu "ljudi" s odgovarajućim brojem ljudi gdje svaki ima

# 3. Napiši funkciju `crtaj_ljude` koja će prikazati sve ljude horizontalno na sredini ekrana

# 4. Postavi jednog covjeka za izvor koji je u sredini ekrana

# 5. Širenje zaraze. Napiši funkciju `sirenje_zaraze()` koja će proći po svim ljudima i provjeriti jesu li zaraženi.
# Ako je, pozvati funckiju `sirenje_zaraze_covjek`

# 6. Napiši funkciju za provjeru broja zaraženih.

# 7. Dodatak. Trenutno ne vidimo tko je zadnji zaraženi i ljudi koji su trenutnog dana bili zaraženi mogu istog dana
# zaraziti druge. Potrebno dodati jedan međukorak s kojim se pamti ljude koji su trenutno zaraženi (boje.narancasta)

# 8. Domaća zadaća. Ispisati dan kada su svi ljudi zaraženi samo jednom.
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
