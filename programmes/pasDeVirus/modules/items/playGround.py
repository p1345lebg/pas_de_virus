import pygame
import os
from programmes.settings import Settings

class PlayGround:
    def __init__(self, screen: pygame.Surface , disposition: list[list[str|int]]):
        self.screen : pygame.Surface
        PATH_WATER = os.sep.join(['assets','SproutTiles','Tilesets','Water.png'])
        PATH_GRASS = os.sep.join(['assets','SproutTiles','Tilesets','Grass.png'])
        PATH_LILYPAD = os.sep.join(['assets', 'SproutLand'])

        self.WATER : list[pygame.Surface] = []
        water = pygame.image.load(PATH_WATER)
        x,y = water.get_size()
        for i in range(0, x, x//4):
            self.WATER.append(water.subsurface((i,0),(x//4,y)).convert_alpha())

        self.GRASS : list[pygame.Surface] = []
        grass = pygame.image.load(PATH_GRASS)
        x = grass.get_width()//11
        y = grass.get_height()//7
        for j in range(7) :
            for i in range(11):
                if (i,j) in [(1,0),(0,1),(2,1),(1,2),(5,1),(5,2),(6,1),(6,2)]:
                    #a modifier
                    self.GRASS.append(grass.subsurface((i*x,j*y),(x,y)).convert_alpha())

        self.widthInTile = 18
        self.update_screen(screen)

        self.animationCounter = 0
        self.animationSpeed = Settings().get_FPS()
        self.waterFrame = 0

    def update_screen(self, screen: pygame.Surface):
        self.screen : pygame.Surface = screen
        screen_x, screen_y = self.screen.get_size()
        playgroundSize = min(int(screen_x*0.9), int(screen_y*0.8))
        tileSize = playgroundSize//self.widthInTile
        self.tileSize = tileSize
        self.playgroundSize = tileSize*self.widthInTile
        

        self.water : list[pygame.Surface] = []
        for tile in self.WATER:
            self.water.append(pygame.transform.scale(tile,(tileSize, tileSize)))

        self.grass : list[pygame.Surface] = []
        for tile in self.GRASS:
            self.grass.append(pygame.transform.scale(tile,(tileSize, tileSize)))

        self.border:pygame.Surface = pygame.Surface((self.playgroundSize,self.playgroundSize), pygame.SRCALPHA)
        self.border.fill((0,0,0,0))
        for y in range(0, self.widthInTile):
            for x in range(0,self.widthInTile):
                if x == 0:
                    if y == 0:
                        self.border.blit(self.grass[3],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.grass[6],(x*tileSize,y*tileSize))
                    else:
                        self.border.blit(self.grass[2],(x*tileSize,y*tileSize))
                elif x == self.widthInTile-1:
                    if y == 0:
                        self.border.blit(self.grass[4],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.grass[7],(x*tileSize,y*tileSize))
                    else:
                        self.border.blit(self.grass[1],(x*tileSize,y*tileSize))
                else:
                    if y == 0:
                        self.border.blit(self.grass[5],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.grass[0],(x*tileSize,y*tileSize))
        
        self.playgroundRect = self.border.get_rect(center=(screen_x // 2, screen_y // 2))

        self.lilypadSurface : pygame.surface = pygame.Surface((self.playgroundSize,self.playgroundSize), pygame.SRCALPHA)
        self.border.fill((0,0,0,0))

    def get_position():
        pass

    def draw(self):
        self.animationCounter += 1
        playground :pygame.Surface = pygame.Surface((self.playgroundSize,self.playgroundSize))

        if self.animationCounter >= self.animationSpeed:
            self.animationCounter = 0
            self.waterFrame = (self.waterFrame+1) % len(self.water)
        
        waterTile : pygame.Surface = self.water[self.waterFrame]
        for y in range(self.widthInTile):
            for x in range(self.widthInTile):
                playground.blit(waterTile,(x*self.tileSize,y*self.tileSize))

        playground.blit(self.border,(0,0))

        self.screen.blit(playground,self.playgroundRect)


    

        
        



"""
pawns_pos
playground_surface
"""
