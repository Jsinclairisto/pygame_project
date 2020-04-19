import pygame, os, sys
from pygame.locals import *

class Player(pygame.sprite.Sprite):
    # playerImg = pygame.image.load('cave_guy_animation.png')
    # playerImg = pygame.transform.scale(playerImg,(50,70))
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        for i in range(1,5):
           # playerImg = pygame.image.load(os.path.join('assets', 'player' + str(i) + '.png')).convert()
            playerImg = os.path.join('assets', 'player' + 'player1' + '.png')
            playerImg.convert_alpha()
            playerImg.set_colorkey(ALPHA)
            self.images.append(playerImg)
            self.image=self.images[0]
            self.rect = self.image.get_rect()
            

    def control(self,x,y):
        self.movex += x
        self.movey += y

    def update(self):
        ani = 4  
        self.rect.x = self.rect.x + self.movex
        self.rect.y = self.rect.y + self.movey
        if self.movex < 0:
            self.frame += 1
            if self.frame > 3*ani :
                self.frame = 0
            self.image = self.images[self.frame//ani]
