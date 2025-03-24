import pygame
import os
from programmes.settings import Settings

class PlayGround:
    def __init__(self, screen: pygame.Surface , PATH_WATER : str = os.sep.join(['assets','SproutTiles','Tilesets','Water.png']),
                                                PATH_GROUND : str = os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']),
                                                PATH_SUPORT : str = os.sep.join(['assets', 'SproutLand'])):
        """
        terains sur lequel sont placé les pions

        Args:
            -screen(pygame.Surface) : surface sur laquelle est dessiné le terrain de jeu
            -PATH_WATER(str) : chemin vers le tileset de l'eau ```os.sep.join(['chemin','tileset.png'])```
            -PATH_WATER(str) : chemin vers le tileset du sol ```os.sep.join(['chemin','tileset.png'])```
            -PATH_SUPORT(str): chemin vers le tileset du suport ```os.sep.join(['chemin','tileset.png'])```
        """
        self.screen : pygame.Surface
        self.WATER : list[pygame.Surface] = []
        water = pygame.image.load(PATH_WATER)
        x,y = water.get_size()
        for i in range(0, x, x//4):
            self.WATER.append(water.subsurface((i,0),(x//4,y)).convert_alpha())

        self.GROUND : list[pygame.Surface] = []
        ground = pygame.image.load(PATH_GROUND)
        x = ground.get_width()//11
        y = ground.get_height()//7
        for j in range(7) :
            for i in range(11):
                if (i,j) in [(1,0),(0,1),(2,1),(1,2),(5,1),(5,2),(6,1),(6,2)]:
                    self.GROUND.append(ground.subsurface((i*x,j*y),(x,y)).convert_alpha())

        self.widthInTile = 18
        self.pawnPositions : list[tuple[int,int]]
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

        self.ground : list[pygame.Surface] = []
        for tile in self.GROUND:
            self.ground.append(pygame.transform.scale(tile,(tileSize, tileSize)))

        self.border:pygame.Surface = pygame.Surface((self.playgroundSize,self.playgroundSize), pygame.SRCALPHA)
        self.border.fill((0,0,0,0))
        for y in range(0, self.widthInTile):
            for x in range(0,self.widthInTile):
                if x == 0:
                    if y == 0:
                        self.border.blit(self.ground[3],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.ground[6],(x*tileSize,y*tileSize))
                    else:
                        self.border.blit(self.ground[2],(x*tileSize,y*tileSize))
                elif x == self.widthInTile-1:
                    if y == 0:
                        self.border.blit(self.ground[4],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.ground[7],(x*tileSize,y*tileSize))
                    else:
                        self.border.blit(self.ground[1],(x*tileSize,y*tileSize))
                else:
                    if y == 0:
                        self.border.blit(self.ground[5],(x*tileSize,y*tileSize))
                    elif y == self.widthInTile-1:
                        self.border.blit(self.ground[0],(x*tileSize,y*tileSize))
        
        self.playgroundRect = self.border.get_rect(center=(screen_x // 2, screen_y // 2))

        self.lilypadSurface : pygame.Surface = pygame.Surface((self.playgroundSize,self.playgroundSize), pygame.SRCALPHA)
        self.lilypadSurface.fill((0,0,0,0))

        self.pawnPositions = []
        
        #a faire avec une liste de pourcentage préfaite



    def get_position(self):
        return self.pawnPositions

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
        playground.blit(self.lilypadSurface,(0,0))

        self.screen.blit(playground,self.playgroundRect)


    

        
        



"""
pawns_pos
playground_surface
"""
