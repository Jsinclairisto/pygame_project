import pygame, os, sys
from pygame.locals import *
from player import Player

pygame.init()

WHITE = (255,255,255)
BLACK = (0, 0 ,0)
FPS = 60
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((800,600), 0, 32)
pygame.display.set_caption('Dungeon Dude')

direction = 'right'

while True:
    player = Player()
    DISPLAYSURF.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.player_x = -10
            if event.key == pygame.K_RIGHT:
                player.player_x = 10
    x_newLoc = 0
    x_newLoc += player.player_x
    DISPLAYSURF.blit(player.playerImg, (x_newLoc, player.player_y))
    pygame.display.update()
    fpsClock.tick(FPS)
