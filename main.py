import sys, pygame, os
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
    # if direction == 'right':
    #     player.player_x += 5
    #     if player.player_x == 280:
    #         direction = 'down'
    
    # elif direction == 'down':
    #     player.player_y += 5
    #     if player.player_y == 220:
    #         direction = 'left'
    
    # elif direction == 'left':
    #     player.player_x -= 5
    #     if player.player_x == 10:
    #         direction = 'up'
    
    # elif direction == 'up':
    #     player.player_y -= 5
    #     if player.player_y == 10:
    #         direction = 'right'



    DISPLAYSURF.blit(player.playerImg, (player.player_x, player.player_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)
