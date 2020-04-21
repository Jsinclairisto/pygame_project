import pygame, os, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    playerImg = pygame.image.load('player1.png')
    playerImg = pygame.transform.scale(playerImg,(50,70))
    player_x = 0
    player_y = 0