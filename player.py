import pygame, os, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    playerImg = pygame.image.load('assets/player/player_1.png')
    playerImg = pygame.transform.scale(playerImg,(64,64))

    player_x = 0
    player_y = 0
        
    # def update(self):
    #     self.player_x = 0
    #     keys = pygame.keys.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.player_x = -5
    #         print(self.player_x)
    #     if keys[pygame.K_RIGHT]:
    #         self.player_x = 5
    #         print(self.player_x)
    #     self.playerImg.x += self.player_x
    #     self.playerImg.y += self.player_y