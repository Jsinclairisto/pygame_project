import pygame, sys
from pygame.locals import*

pygame.init()

DISPLAYSURF = pygame.display.set_mode((800, 500), 0, 32)

pygame.display.set_caption('Dungeon Dude')

#playerSprite = pygame.image.load('caveguy.png')
guyx = 10
guyy = 10
direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    