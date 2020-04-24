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

DISPLAYSURF = pygame.display.set_mode((1090,800), 0, 32)
pygame.display.set_caption('Dungeon Dude')
    
x_newLoc = 128
y_newLoc = 128
MAP_WIDTH = 40
MAP_HEIGHT = 40

CELL_WIDTH = 64
CELL_HEIGHT = 64

WALL_TILE = pygame.image.load('assets/block_tile.png')
WALL_TILE = pygame.transform.scale(WALL_TILE,(64,64))
FLOOR_TILE = pygame.image.load('assets/floor_tile.png')
FLOOR_TILE = pygame.transform.scale(FLOOR_TILE,(64,64))

class str_Tile:
    def __init__(self, block_path):
        self.block_path = block_path 

def map_create():
    new_map = [[str_Tile(False) for y in range(0,MAP_HEIGHT)] for x in range(0,MAP_HEIGHT)]
    new_map[16][1].block_path = True
    new_map[16][2].block_path = True 
    new_map[16][3].block_path = True 
    new_map[16][4].block_path = True 
    new_map[16][5].block_path = True 
    new_map[16][6].block_path = True 
    
    new_map[15][6].block_path = True
    new_map[14][6].block_path = True
    new_map[13][6].block_path = True
    new_map[12][6].block_path = True
    
    new_map[12][7].block_path = True
    new_map[12][8].block_path = True
    new_map[12][9].block_path = True
    new_map[11][9].block_path = True
    new_map[10][9].block_path = True
    new_map[9][9].block_path = True
    new_map[8][9].block_path = True
    new_map[7][9].block_path = True
    new_map[6][9].block_path = True
    new_map[5][9].block_path = True
    new_map[5][8].block_path = True
    new_map[5][7].block_path = True
    new_map[5][6].block_path = True
    new_map[4][6].block_path = True
    new_map[3][6].block_path = True
    new_map[2][6].block_path = True
    new_map[1][6].block_path = True
    new_map[1][5].block_path = True
    new_map[1][4].block_path = True
    new_map[1][3].block_path = True
    new_map[1][2].block_path = True
    new_map[1][1].block_path = True

    return new_map 

def draw_game():
    pass

def game_init():
    GAME_MAP = map_create()
    draw_map(GAME_MAP)
    

def draw_map(map_to_draw):
    for x in range(0,MAP_WIDTH):
        for y in range(0,MAP_HEIGHT):
            if map_to_draw[x][y].block_path == True:
                DISPLAYSURF.blit(WALL_TILE,(x*CELL_WIDTH, y*CELL_HEIGHT))
            else:
                DISPLAYSURF.blit(FLOOR_TILE,(x*CELL_WIDTH, y*CELL_HEIGHT))

while True:
    player = Player()
    DISPLAYSURF.fill(GB_GREEN)
    game_init()
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
