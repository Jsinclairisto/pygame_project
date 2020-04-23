import pygame, os, sys
from pygame.locals import *
from level import *
from player import Player


pygame.init()

WHITE = (255,255,255)
BLACK = (0, 0 ,0)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
GB_GREEN = (32,70,49)
YELLOW = (255,255,0)
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Dungeon Dude')

    
x_newLoc = 0
y_newLoc = 0
while True:
    player = Player()
    DISPLAYSURF.fill(GB_GREEN)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_x += -64
            if event.key == pygame.K_RIGHT:
                player.player_x += 64
            if event.key == pygame.K_UP:
                player.player_y += -64
            if event.key == pygame.K_DOWN:
                player.player_y += 64

        x_newLoc += player.player_x
        y_newLoc += player.player_y
    DISPLAYSURF.blit(player.playerImg, (x_newLoc,y_newLoc))
    pygame.display.update()
    fpsClock.tick(FPS)
