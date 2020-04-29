import pygame
import os
import boja

sirina_pixeli = 640
visina_pixeli = 480
broj_pixela_u_metru = 32

sirina = sirina_pixeli / broj_pixela_u_metru
visina = visina_pixeli / broj_pixela_u_metru

size = (sirina_pixeli, visina_pixeli)

pygame.init()
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("comicsansms", 50)

screen.fill(boja.bijela)


def crtaj_osobu(x_m, y_m, boja):
    # Pretvori metre u pixele
    x = x_m * broj_pixela_u_metru
    y = y_m * broj_pixela_u_metru
    # head
    pygame.draw.ellipse(screen, boja, [0 + x, 0 + y, 10, 10], 0)
    # body
    pygame.draw.line(screen, boja, [4 + x, 17 + y], [4 + x, 7 + y], 2)
    # legs
    pygame.draw.line(screen, boja, [4 + x, 17 + y], [9 + x, 27 + y], 2)
    pygame.draw.line(screen, boja, [4 + x, 17 + y], [-1 + x, 27 + y], 2)
    # arms
    pygame.draw.line(screen, boja, [4 + x, 7 + y], [8 + x, 17 + y], 2)
    pygame.draw.line(screen, boja, [4 + x, 7 + y], [0 + x, 17 + y], 2)


def prikazi_tekst(text_lijevo, text_desno):
    screen.fill((255, 255, 255))

    text_object_1 = font.render(text_lijevo, True, (0, 128, 0))
    screen.blit(text_object_1,
                (60, visina_pixeli - text_object_1.get_height() - 5))

    text_object_2 = font.render(text_desno, True, (0, 128, 0))
    screen.blit(text_object_2,
                (320, visina_pixeli - text_object_2.get_height() - 5))


# Reset the output of screen to be nice
variable = os.system('tput reset')
