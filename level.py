import pygame, sys
from pygame.locals import*

class str_Tile:
    def __init__(self, block_path):
        self.block_path = block_path

def map_create():
    new_map = [[str_Tile(False) for y in range(0,30)] for x in range(0,30)]
    new_map[10][10].block_path = True 
    new_map[10][15].block_path = True 

    return new_map 

def game_init():
    GAME_MAP = map_create()

def draw_map(map_to_draw):
    for x in range(0,30):
        for y in range(0,30):
            if map_to_draw[x][y].block_path == True:
                #TODO: Draw floor 
                pass
            else:
                #TODO: Draw floor
                pass