from crtac import *
import numpy as np
import time

# moze ici od 20 do min(size_z, size_y)
razmak = 120

broj_ljudi_kolona = int((size_y - razmak) / (razmak + 5)) + 1
broj_ljudi_red = int((size_x - razmak) / razmak) + 1
ljudi = [[Color.blue for j in range(broj_ljudi_kolona)]
         for i in range(broj_ljudi_red)]

def crtaj_ljude():
    for i in range(broj_ljudi_red):
        for j in range(broj_ljudi_kolona):
            crtaj_osobu(i * razmak + razmak / 2,
                        j * (razmak + 5) + razmak / 2, ljudi[i][j])

print(ljudi)

i = 0
while True:
    prikazi_tekst(str(i))
    crtaj_ljude()
    i = i + 1
    # ljudi[i%broj_ljudi_red][0] = Color.green
    time.sleep(1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
