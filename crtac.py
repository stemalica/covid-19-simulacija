import pygame
from pygame.locals import *
import sys
import os

from enum import Enum


class Color(Enum):
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    darkBlue = (0, 0, 128)
    white = (255, 255, 255)
    black = (0, 0, 0)
    pink = (255, 200, 200)
    yellow = (255, 255, 0)


pygame.init()
size_x = 640
size_y = 480
size = (size_x, size_y)
screen = pygame.display.set_mode(size)
font = pygame.font.SysFont("comicsansms", 50)

screen.fill(Color.white.value)


def crtaj_osobu(x, y, color_t):
    color = color_t.value
    # head
    pygame.draw.ellipse(screen, color, [0 + x, 0 + y, 10, 10], 0)
    # body
    pygame.draw.line(screen, color, [4 + x, 17 + y], [4 + x, 7 + y], 2)
    # legs
    pygame.draw.line(screen, color, [4 + x, 17 + y], [9 + x, 27 + y], 2)
    pygame.draw.line(screen, color, [4 + x, 17 + y], [-1 + x, 27 + y], 2)
    # arms
    pygame.draw.line(screen, color, [4 + x, 7 + y], [8 + x, 17 + y], 2)
    pygame.draw.line(screen, color, [4 + x, 7 + y], [0 + x, 17 + y], 2)


def prikazi_tekst(text_lijevo, text_desno):
    screen.fill((255, 255, 255))

    text_object_1 = font.render(text_lijevo, True, (0, 128, 0))
    screen.blit(text_object_1,
                (40, 480 - text_object_1.get_height()))

    text_object_2 = font.render(text_desno, True, (0, 128, 0))
    screen.blit(text_object_2,
                (300, 480 - text_object_2.get_height()))


def prikazi_tekst_desno(text):
    text_object = font.render(text, True, (0, 128, 0))
    screen.fill((255, 255, 255))
    screen.blit(text_object,
                (500, 480 - text_object.get_height()))


# Reset the output of screen to be nice
variable = os.system('tput reset')
