import pygame
from os import path
import random


class Draw:
    def __init__(self, screen) -> None:
        self.screen : pygame.Surface = screen
        self.startTime = pygame.time.get_ticks()
        self.speedAnimation = 1000
        self.current_frame = 0
        self.original_height = screen.get_height()
        self.original_width = screen.get_width()
        # On garde une référence aux dimensions originales
        self.height = self.original_height
        self.width = self.original_width
        self.load_assets_pieces()
        self.load_assets_background()

    def load_assets_pieces(self):
        PATH_ASSETS_SHEET = path.join(path.dirname(__file__),'..','..', '..','assets','SproutTiles')
        self.sprite_sheet = pygame.image.load(path.join(PATH_ASSETS_SHEET, 'Objects', 'Basic_Grass_Biom_things.png')).convert_alpha()

        # maintenir le ratio de 16/9 pour les calucls
        width_height_compare = self.height * 16/9
    
        # dimensions logique pas écran réel
        if width_height_compare != self.width:
            if self.width / 1920/1080 < self.height:
                self.width = self.height * 1920/1080
            else:
                self.height = self.width * 1920/1080
        
        #Calcule de la taille des elem basé sur les dimensions logique
        smaller_size = min(self.width/19.2, self.height/10.8)
        self.water_lily = []

        self.water_lily.append(pygame.transform.scale(self.get_sprite(self.sprite_sheet, 7, 4, 16, 16), (smaller_size, smaller_size)))
        self.water_lily.append(pygame.transform.scale(self.get_sprite(self.sprite_sheet, 8, 4, 16, 16), (smaller_size, smaller_size)))
        
        self.sizePiece = self.water_lily[0].get_size()

        self.water_lily_random = []
        altern_size = (4,3)
        for i in range(7):
            pos = []
            for y in range(altern_size[i%2]):
                    pos.append(1 if random.randint(0,100) <= 15 else 0)
            self.water_lily_random.append(pos)

        self.widthOffset = self.width/12
        self.heightOffset = self.height/12

        ground_height = 7
        max_width_size3 = 3
        max_width_size4 = 4

        # Calcul des dimensions totales pour le centrage
        total_width3 = (max_width_size3 - 1) * self.widthOffset + self.sizePiece[0]
        self.total_height = (ground_height - 1) * self.heightOffset + self.sizePiece[1]
        
        # Centrage sur l'écran réel (pas sur les dimensions logiques)
        self.beginX3 = (self.original_width - total_width3) / 2
        self.beginY3 = (self.original_height - self.total_height) / 2
        
        self.total_width4 = (max_width_size4 - 1) * self.widthOffset + self.sizePiece[0]
        self.beginX4 = (self.original_width - self.total_width4) / 2
        self.beginY4 = self.beginY3  # Même position Y pour toutes les lignes

    def load_assets_background(self):
        PATH_ASSETS_TILE = path.join(path.dirname(__file__),'..','..', '..','assets','SproutTiles')
        self.sprite_sheetWater = pygame.image.load(path.join(PATH_ASSETS_TILE, 'Tilesets', 'Water.png')).convert_alpha()
        self.sprite_sheetGrass = pygame.image.load(path.join(PATH_ASSETS_TILE, 'Tilesets', 'Grass.png')).convert_alpha()

        searchSize = True
        self.startTileSize = 51
        while searchSize:
            self.startTileSize -= 1
            if self.original_height % self.startTileSize == 0 and self.original_width % self.startTileSize == 0:
                searchSize = False
        #self.startTileSize = self.screen.get_width()//100

        self.sprite_anim_water = []
        for water in range(4):
            part_anim_water = []
            for x in range(0,2):
                for y in range(0,2):
                    part_anim_water.append(pygame.transform.scale(self.get_sprite(self.sprite_sheetWater, x+water*2 , y,4,4), (self.startTileSize, self.startTileSize)))
            self.sprite_anim_water.append(part_anim_water)
        
        self.grass = []
        for x in range(0, 6):
            for y in range(5, 7):
                self.grass.append(pygame.transform.scale(self.get_sprite(self.sprite_sheetGrass, x, y, 16, 16), (self.startTileSize, self.startTileSize)))

        self.borderGrass, self.cornerGrass = [], []
        posCornerGrassSprite = ((5,1),(6,1),(5,2),(6,2))
        posBroderGrassSpirte = ((2,1),(1,0),(0,1),(1,2))
        for x in range(4):
            self.borderGrass.append(pygame.transform.scale(self.get_sprite(self.sprite_sheetGrass, posBroderGrassSpirte[x][0], posBroderGrassSpirte[x][1], 16, 16), (self.startTileSize, self.startTileSize)))
            self.cornerGrass.append(pygame.transform.scale(self.get_sprite(self.sprite_sheetGrass, posCornerGrassSprite[x][0], posCornerGrassSprite[x][1],16,16), (self.startTileSize, self.startTileSize)))

        marginWidth10 = self.total_width4 / 3.5
        marginHeight10 = self.total_height / 5

        poxXwater = self.beginX4 - marginWidth10
        posYwater = self.beginY4 - marginHeight10

        endPoxXwater = self.beginX4 + self.total_width4 + marginWidth10
        endPoxYwater = self.beginY4 + self.total_height + marginHeight10

        self.beginWater = (int(poxXwater // self.startTileSize), int(posYwater // self.startTileSize))
        self.endWater = (int(endPoxXwater // self.startTileSize), int(endPoxYwater // self.startTileSize))

        #place Random Texture Grass
        self.randomPlace = []
        for x in range(int(self.original_width // self.startTileSize)):
            tempX = []
            for y in range(int(self.original_height // self.startTileSize)):
                tempX.append(random.randint(0,100)%12)
            self.randomPlace.append(tempX)
        
    def draw_pieces(self, ground, screen):

        screen.blit(self.water_lily[self.water_lily_random[0][1]], (-1 * self.widthOffset + self.beginX3, -1 * self.heightOffset + self.beginY4))
        for i in range(len(ground)):
            for y in range(len(ground[i])):
                if len(ground[i]) % 4 != 0:
                    self.draw_element(screen, ground[i][y], (y, i), (self.beginX3, self.beginY3))
                else:
                    self.draw_element(screen, ground[i][y], (y, i), (self.beginX4, self.beginY4))
    
    def draw_element(self, screen, element, position, begin):
        if element == "empty":
            screen.blit(self.water_lily[self.water_lily_random[position[1]][position[0]]], (position[0] * (self.widthOffset) + begin[0], position[1] * (self.heightOffset) + begin[1]))
    
    def get_sprite(self, sprite_sheet, x, y, widht, height):
        sprite = pygame.Surface((widht, widht), pygame.SRCALPHA).convert_alpha()
        sprite.blit(sprite_sheet, (0, 0), (x * widht, y * height, widht, height))
        return sprite

    def draw_background(self, screen):
        for x in range(int(self.original_width // self.startTileSize)):
            for y in range(int(self.original_height // self.startTileSize)):
                screen.blit(self.grass[self.randomPlace[x][y]], (x*self.startTileSize, y*self.startTileSize))
        
        self.nowTime = pygame.time.get_ticks()
        if self.nowTime - self.startTime > self.speedAnimation:
            self.startTime = self.nowTime
            self.current_frame = (self.current_frame + 1) % 4

        for x in range(self.beginWater[0], self.endWater[0]):
            for y in range(self.beginWater[1], self.endWater[1]):
                block_x = x // 2
                block_y = y // 2

                # Décalage d'animation basé sur la position du bloc
                block_offset = (block_x + block_y) % 4

                # Frame calculée avec décalage par bloc
                frame = (self.current_frame + block_offset) % 4
                
                if y%2 != 0:
                    screen.blit(self.sprite_anim_water[frame][2+x%2], (x*self.startTileSize,y*self.startTileSize))
                else:
                    screen.blit(self.sprite_anim_water[frame][x%2], (x*self.startTileSize,y*self.startTileSize))

        #beginWater[0] = x / endwater[0] = endx
        #beginWater[1] = y / endwater[1] = endy
        for x in range(self.beginWater[0], self.endWater[0] + 1):
            for y in range(self.beginWater[1], self.endWater[1] + 1):
                if (x == self.beginWater[0] and y < self.endWater[1]):
                    screen.blit(self.borderGrass[0], (x*self.startTileSize, y*self.startTileSize))
                if (y == self.beginWater[1] and x < self.endWater[0]):
                    screen.blit(self.borderGrass[3], (x*self.startTileSize, y*self.startTileSize))
                if (x == self.endWater[0] - 1 and y < self.endWater[1]):
                    screen.blit(self.borderGrass[2], (x*self.startTileSize, y*self.startTileSize))
                if (y == self.endWater[1] - 1 and x < self.endWater[0]):
                    screen.blit(self.borderGrass[1], (x*self.startTileSize, y*self.startTileSize))

                #Coin bas gauche
                if (x == self.beginWater[0] and y == self.endWater[1]-1):
                    screen.blit(self.cornerGrass[2], (x*self.startTileSize, y*self.startTileSize))
                #Coin haut droite
                if (y == self.beginWater[1] and x == self.endWater[0]-1):
                    screen.blit(self.cornerGrass[1], (x*self.startTileSize, y*self.startTileSize))
                #Coind haut gauche
                if (y == self.beginWater[1] and x == self.beginWater[0]):
                    screen.blit(self.cornerGrass[0], (x*self.startTileSize, y*self.startTileSize))
                #Coin bas droite
                if (x == self.endWater[0]-1 and y == self.endWater[1]-1):
                    screen.blit(self.cornerGrass[3], (x*self.startTileSize, y*self.startTileSize))