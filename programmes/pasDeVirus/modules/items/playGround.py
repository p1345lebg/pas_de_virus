import pygame
import os
from random import randint
#from .pawn import Pawn

from programmes.settings import Settings


class PlayGround:
    def __init__(self, screen: pygame.Surface , level : dict[str,list[list[int]]|int],
                                                PATH_WATER : str = os.sep.join(['assets','SproutTiles','Tilesets','Water.png']),
                                                PATH_GROUND : str = os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']),
                                                PATH_SUPORT : str = os.sep.join(['assets', 'pasDeVirus', 'suport', 'lilypads.png'])):
        """
        terains sur lequel sont placé les pions

        Args:
            -screen(pygame.Surface) : surface sur laquelle est dessiné le terrain de jeu
            -level(dict[str,list[list[int]]|int]) : disposition du niveau plus toutes ses informations
            -PATH_WATER(str) : chemin vers le tileset de l'eau ```os.sep.join(['chemin','tileset.png'])```
            -PATH_WATER(str) : chemin vers le tileset du sol ```os.sep.join(['chemin','tileset.png'])```
            -PATH_SUPORT(str): chemin vers le tileset du suport ```os.sep.join(['chemin','tileset.png'])```
        """
        self.screen : pygame.Surface
        self.levelDisposition = level['disposition']

        PATH_VIRUS = os.sep.join(['assets','char_sprite','virus.png'])
        PATH_CHAR1 = os.sep.join(['assets','char_sprite','moon.png'])
        PATH_CHAR2 = os.sep.join(['assets','char_sprite','nuage_claire.png'])
        PATH_CHAR3 = os.sep.join(['assets','char_sprite','nuage_triste.png'])
        PATH_CHAR4 = os.sep.join(['assets','char_sprite','sun_dodo.png'])
        PATH_CHAR5 = os.sep.join(['assets','char_sprite','sun_happy.png'])

        #charge les sprites
        self.VIRUS : pygame.Surface = pygame.image.load(PATH_VIRUS)
        self.CHAR1 : pygame.Surface = pygame.image.load(PATH_CHAR1)
        self.CHAR2 : pygame.Surface = pygame.image.load(PATH_CHAR2)
        self.CHAR3 : pygame.Surface = pygame.image.load(PATH_CHAR3)
        self.CHAR4 : pygame.Surface = pygame.image.load(PATH_CHAR4)
        self.CHAR5 : pygame.Surface = pygame.image.load(PATH_CHAR5)

        #charge la tile set de l'eau
        self.WATER : list[pygame.Surface] = []
        water = pygame.image.load(PATH_WATER).convert_alpha()
        x,y = water.get_size()
        for i in range(0, x, x//4):
            self.WATER.append(water.subsurface((i,0),(x//4,y)).convert_alpha())

        #charge la tile set du sol
        self.GROUND : list[pygame.Surface] = []
        ground = pygame.image.load(PATH_GROUND).convert_alpha()
        x = ground.get_width()//11
        y = ground.get_height()//7
        for j in range(7) :
            for i in range(11):
                if (i,j) in [(1,0),(0,1),(2,1),(1,2),(5,1),(5,2),(6,1),(6,2)]:
                    self.GROUND.append(ground.subsurface((i*x,j*y),(x,y)).convert_alpha())

        #charge la tile set du suport
        self.SUPORT : list[pygame.Surface] = []
        suport = pygame.image.load(PATH_SUPORT).convert_alpha()
        x,y = suport.get_size()
        for i in range(0,x,x//3):
            self.SUPORT.append(suport.subsurface((i,0),(x//3,y)))

        #self.pawns : list[Pawn]

        #defini la taille (en tile) du terrain
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
        self.pawns = []
        
        #adapte la taille de l'eau
        self.water : list[pygame.Surface] = []
        for tile in self.WATER:
            self.water.append(pygame.transform.scale(tile,(tileSize, tileSize)))

        #adapte la taille du sol
        self.ground : list[pygame.Surface] = []
        for tile in self.GROUND:
            self.ground.append(pygame.transform.scale(tile,(tileSize, tileSize)))

        #adapte la taille des suports
        self.suport : list[pygame.Surface] = []
        for tile in self.SUPORT:
            self.suport.append(pygame.transform.scale(tile, (tileSize*2, tileSize*2)))

        #adapte la taille des personnages
        self.virus = pygame.transform.scale(self.VIRUS, (tileSize*1.5, tileSize*1.5))
        self.char1 = pygame.transform.scale(self.CHAR1, (tileSize*1.5, tileSize*1.5))
        self.char2 = pygame.transform.scale(self.CHAR2, (tileSize*1.5, tileSize*1.5))
        self.char3 = pygame.transform.scale(self.CHAR3, (tileSize*1.5, tileSize*1.5))
        self.char4 = pygame.transform.scale(self.CHAR4, (tileSize*1.5, tileSize*1.5))
        self.char5 = pygame.transform.scale(self.CHAR5, (tileSize*1.5, tileSize*1.5))

        #dessine le sol
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
                                    [(33,33),(50,33),(67,33)],
                                [(24,41),(41,41),(59,41),(76,41)],
                                    [(33,50),(50,50),(67,50)],
                                [(24,59),(41,59),(59,59),(76,59)],
                                    [(33,67),(50,67),(67,67)],
                                [(24,76),(41,76),(59,76),(76,76)]]
        

        #dessine les nenuphares
        for i in range(len(pawnPositionsPercent)):
            for j in range(len(pawnPositionsPercent[i])):
                if self.levelDisposition[i][j] != 'B':
                    x = randint(0,1)
                    pos = pawnPositionsPercent[i][j]
                    self.suportSurface.blit(self.suport[x], (playgroundSize/100*pos[0]-tileSize,playgroundSize/100*pos[1]-tileSize))

        #definie la position des pions
        self.pawnPositions = [[],[],[],[],[],[],[]]
        for i in range(len(pawnPositionsPercent)):
            for pos in pawnPositionsPercent[i]:
                self.pawnPositions[i].append((self.playgroundSize/100*pos[0]-self.tileSize/1.5,self.playgroundSize/100*pos[1]-self.tileSize))

        #definie de dictionnaire des pions
        self.pawnsDict : dict = {
            'X' : self.virus
        }
        disponibleTexture = {
            self.char1,
            self.char2,
            self.char3,
            self.char4,
            self.char5
        }

        for i in self.levelDisposition:
            for pawn in i:
                if pawn and pawn != 'B':
                    if pawn not in self.pawnsDict:
                        self.pawnsDict[pawn] = disponibleTexture.pop()

    def update(self, events):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.K_TAB:
                pass
            if event.type == pygame.K_a:
                pass
            if event.type == pygame.K_z:
                pass
            if event.type == pygame.K_q:
                pass
            if event.type == pygame.K_s:
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
        playground.blit(self.suportSurface,(0,0))

        for i in range(len(self.levelDisposition)):
            for j in range(len(self.levelDisposition[i])):
                if self.levelDisposition[i][j] in self.pawnsDict:
                    playground.blit(self.pawnsDict[self.levelDisposition[i][j]], self.pawnPositions[i][j])

        self.screen.blit(playground,self.playgroundRect)





"""
pawns_pos
playground_surface
"""
