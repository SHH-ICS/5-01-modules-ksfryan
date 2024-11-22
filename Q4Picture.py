# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect, rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)


pygame.init()
gameDisplay = display.set_mode(SCREEN_SIZE)
gameDisplay.fill(Color('light blue'))

draw.polygon(gameDisplay, Color('dark grey'), [(100, 200), (400, 200), (250, 50)])
draw.polygon(gameDisplay, Color('grey'), [(100, 200), (400, 200), (150, 50)])
draw.polygon(gameDisplay, Color('black'), [(100, 200), (200, 200), (150, 50)])


draw.circle(gameDisplay, Color('black'), (410, 180), 30)
draw.rect(gameDisplay, Color('dark grey'),Rect(210, 200, 50, 200,))
draw.rect(gameDisplay, Color('red'),Rect(200, 200, 75, 30,))



display.flip()
input("Press enter to exit")
