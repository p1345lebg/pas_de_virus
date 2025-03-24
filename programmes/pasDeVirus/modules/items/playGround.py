import pygame
import os
from random import randint

from programmes.settings import Settings


class PlayGround:
    def __init__(self, screen: pygame.Surface , PATH_WATER : str = os.sep.join(['assets','SproutTiles','Tilesets','Water.png']),
                                                PATH_GROUND : str = os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']),
                                                PATH_SUPORT : str = os.sep.join(['assets', 'pasDeVirus', 'suport', 'lilypads.png'])):
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
        water = pygame.image.load(PATH_WATER).convert_alpha()
        x,y = water.get_size()
        for i in range(0, x, x//4):
            self.WATER.append(water.subsurface((i,0),(x//4,y)).convert_alpha())

        self.GROUND : list[pygame.Surface] = []
        ground = pygame.image.load(PATH_GROUND).convert_alpha()
        x = ground.get_width()//11
        y = ground.get_height()//7
        for j in range(7) :
            for i in range(11):
                if (i,j) in [(1,0),(0,1),(2,1),(1,2),(5,1),(5,2),(6,1),(6,2)]:
                    self.GROUND.append(ground.subsurface((i*x,j*y),(x,y)).convert_alpha())

        self.SUPORT : list[pygame.Surface] = []
        suport = pygame.image.load(PATH_SUPORT).convert_alpha()
        x,y = suport.get_size()
        for i in range(0,x,x//3):
            self.SUPORT.append(suport.subsurface((i,0),(x//3,y)))

        self.widthInTile = 18
        self.pawnPositions : list[list[tuple[int,int]]]
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

        self.suport : list[pygame.Surface] = []
        for tile in self.SUPORT:
            self.suport.append(pygame.transform.scale(tile, (tileSize*2, tileSize*2)))

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

        self.suportSurface : pygame.Surface = pygame.Surface((self.playgroundSize,self.playgroundSize), pygame.SRCALPHA)
        self.suportSurface.fill((0,0,0,0))

        pawnPositionsPercent = [[(24,24),(41,24),(59,24),(76,24)],
                                    [(33,33),(33,50),(33,67)],
                                [(24,41),(41,41),(59,41),(76,41)],
                                    [(50,33),(50,50),(50,67)],
                                [(24,59),(41,59),(59,59),(76,59)],
                                    [(67,33),(67,50),(67,67)],
                                [(24,76),(41,76),(59,76),(76,76)]]
        self.pawnPositions : list[list[tuple[int,int]]] = []


        for i in pawnPositionsPercent:
            for pos in i:
                x = randint(0,1)
                self.suportSurface.blit(self.suport[x], (playgroundSize/100*pos[0]-tileSize,playgroundSize/100*pos[1]-tileSize))

        self.suportSurface.blit(self.suport[2],(playgroundSize/100*15-tileSize,playgroundSize/100*15-tileSize))

        
        
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
        playground.blit(self.suportSurface,(0,0))

        self.screen.blit(playground,self.playgroundRect)


    

        
        



"""
pawns_pos
playground_surface
"""
