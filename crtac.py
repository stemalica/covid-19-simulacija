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


pygame.init()
size_x = 640
size_y = 480
size = (size_x, size_y)
screen = pygame.display.set_mode(size)

screen.fill(Color.white.value)


def crtaj_osobu(x, y, color_t):
    color = color_t.value
    #head
    pygame.draw.ellipse(screen, color, [0 + x, 0 + y, 10, 10], 0)
    #body
    pygame.draw.line(screen, color, [4 + x, 17 + y], [4 + x, 7 + y], 2)
    #legs
    pygame.draw.line(screen, color, [4 + x, 17 + y], [9 + x, 27 + y], 2)
    pygame.draw.line(screen, color, [4 + x, 17 + y], [-1 + x, 27 + y], 2)
    #arms
    pygame.draw.line(screen, color, [4 + x, 7 + y], [8 + x, 17 + y], 2)
    pygame.draw.line(screen, color, [4 + x, 7 + y], [0 + x, 17 + y], 2)


def prikazi_tekst(text):
    font = pygame.font.SysFont("comicsansms", 72)
    text_object = font.render(text, True, (0, 128, 0))
    screen.fill((255, 255, 255))
    screen.blit(text_object,
                (40, 480 - text_object.get_height()))


# Reset the output of screen to be nice
variable = os.system('tput reset')
