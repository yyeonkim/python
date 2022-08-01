import pygame, sys

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))
black = (0,0,0)

aCat = pygame.image.load("polzak.png")


pygame.display.set_caption('Hello Cat!')

while True:                        # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        screen.fill(black)
        screen.blit(aCat, aCat.get_rect())
        pygame.display.update()
