import pygame
import os
from random import sample

from programmes.components import BackgroundTileSheet

class Tile:
    def __init__(self, coordonatesGrid : tuple[int,int], size:int) -> None:
        self.coordonatesGrid : tuple[int,int] = coordonatesGrid

        self.size : int = size
        self.coordonates : tuple[int,int] = (self.coordonatesGrid[0]*self.size, self.coordonatesGrid[1]*self.size)

        self.surounding : set[Tile] = set()
        self.suroundingMines : int = 0
        self.suroundingFlags : int = 0

        self.__tileSheet : list[list[pygame.Surface]]
        self.__numberSheet : list[pygame.Surface]
        self.tileSheet : list[list[pygame.Surface]]
        self.numberSheet : list[pygame.Surface]
        self.load_textures()

        self.revealed : bool = False
        self.isMine : bool = False
        self.showMine : bool = False
        self.flag : int = 0 # 0 = no flag, 1 = flag, 2 = question mark

    def change_size(self, size:int) -> None:
        self.size = size
        self.coordonates = (self.coordonatesGrid[0]*self.size, self.coordonatesGrid[1]*self.size)
        self.update_textures()

    def load_textures(self) -> None:
        PATH = os.sep.join(['assets','demineur'])
        tileSheet = pygame.image.load(os.sep.join([PATH, 'tilesheet.png']))
        numberSheet = pygame.image.load(os.path.join(PATH, 'numberSheet.png'))

        self.__tileSheet = [[],[]]
        self.__numberSheet = []

        x,y = tileSheet.get_size()
        for i in range(2):
            x,y = tileSheet.get_size()
            for j in range(0,x,x//6):
                self.__tileSheet[i] += [tileSheet.subsurface(j,i*y//2,x//6,y//2)]

        x,y = numberSheet.get_size()
        for i in range(0,x,x//9):
            self.__numberSheet += [numberSheet.subsurface(i,0,x//9,y)]

        self.update_textures()

    def update_textures(self) -> None:
        self.tileSheet = [[pygame.transform.scale(tile, (self.size, self.size)) for tile in row] for row in self.__tileSheet]
        self.numberSheet = [pygame.transform.scale(number, (self.size, self.size)) for number in self.__numberSheet]

    def __str__(self) -> str:
        return f'(4*' ')Tile at {self.coordonatesGrid=} and {self.coordonates=} is {self.revealed=} and {self.flag=}'

    def is_touched(self, pos : tuple[int,int]) -> bool:
        x,y = pos
        if (self.coordonates[0] < x <= self.coordonates[0]+self.size) and (self.coordonates[1] < y <= self.coordonates[1]+self.size):
            return True
        else:
            return False
        
    def toggle_flag(self) -> None:
        if self.revealed:
            return
        
        if self.flag == 1:
            for tile in self.surounding:
                tile.suroundingFlags -= 1

        self.flag = (self.flag+1)%3

        if self.flag == 1:
            for tile in self.surounding:
                tile.suroundingFlags += 1

    def reveal(self) -> None:
        if self.revealed:                
            return True
        

        if self.flag == 1:
            return True
        
        self.revealed = True

        if self.isMine:
            return False
        elif self.suroundingMines == 0:
            for tile in self.surounding:
                if not tile.revealed and tile.flag != 1:
                    if not tile.reveal():
                        return False
                    
        return True
    
    def add_surounding(self, tile) -> None:
        self.surounding.add(tile)
        if tile.isMine:
            self.suroundingMines += 1
        if tile.flag == 1:
            self.suroundingFlags += 1
        
    def draw(self, screen : pygame.Surface) -> None:
        line : int = (self.coordonatesGrid[0]+self.coordonatesGrid[1])%2
        if self.revealed:
            if self.isMine:
                screen.blit(self.tileSheet[line][5], self.coordonates)
            else:
                screen.blit(self.tileSheet[line][4], self.coordonates)
                screen.blit(self.numberSheet[self.suroundingMines], self.coordonates)

        else:
            if self.showMine and self.isMine:
                
                screen.blit(self.tileSheet[line][3], self.coordonates)
            else:
                screen.blit(self.tileSheet[line][self.flag], self.coordonates)

class Game:
    def __init__(self, screen : pygame.Surface, gridSize : tuple[int,int], nbMines : int) -> None:
        self.screen : pygame.Surface = screen
        self.backgound = BackgroundTileSheet(self.screen, os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))

        #self.window_screen : pygame.Surface = pygame.Surface(self.screen.get_size())
        self.window_pos : tuple[int,int] = (0,0)

        self.mines_not_generated : bool = True
        self.lose = False
        

        self.gridSize : tuple[int,int] = gridSize
        self.nbMines : int = nbMines
        self.flagsLeft : int = self.nbMines
        
        x,y = self.screen.get_size()
        self.tile_size : int = y // self.gridSize[1]
        self.window_pos = ((x-self.tile_size*self.gridSize[0])//2,0)
        if self.tile_size * self.gridSize[0] > x:
            self.tile_size = x // self.gridSize[0]
            truc = self.gridSize[0]
            self.window_pos = (0,(y-self.tile_size*self.gridSize[1])//2)

        self.window_screen : pygame.Surface = pygame.Surface((self.tile_size*gridSize[0],self.tile_size*gridSize[1]))

        


        self.tiles : set[Tile] = set()
        for i in range(self.gridSize[0]):
            for j in range(self.gridSize[1]):
                self.tiles.add(Tile((i,j), self.tile_size))

    

    def generate_mines(self, tile_centered: Tile) -> None:
        self.mines_not_generated = False
        
        excluded_tiles = {
            tile for tile in self.tiles 
            if abs(tile.coordonatesGrid[0] - tile_centered.coordonatesGrid[0]) <= 1 and 
            abs(tile.coordonatesGrid[1] - tile_centered.coordonatesGrid[1]) <= 1
        }
        self.win = False
        
        # Liste des tuiles où placer les mines
        available_tiles = list(set(self.tiles) - excluded_tiles)
        
        # Placer les mines sur un échantillon aléatoire de tuiles
        for tile in sample(available_tiles, min(self.nbMines, len(available_tiles))):
            tile.isMine = True

        # Mise à jour des tuiles environnantes
        tile_dict = {(tile.coordonatesGrid[0], tile.coordonatesGrid[1]): tile for tile in self.tiles}
        
        for tile in self.tiles:
            neighbors = [
                tile_dict.get((tile.coordonatesGrid[0] + dx, tile.coordonatesGrid[1] + dy))
                for dx in (-1, 0, 1) for dy in (-1, 0, 1) if (dx, dy) != (0, 0)
            ]
            for neighbor in filter(None, neighbors):
                tile.add_surounding(neighbor)

    def verify_win(self) -> bool:
        for tile in self.tiles:
            if not (tile.isMine or tile.revealed):
                return False
        return True


    def update(self, events) -> None:
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.dict['button'] == 1:
                    for tile in self.tiles:
                        if tile.is_touched((event.dict['pos'][0]-self.window_pos[0], event.dict['pos'][1]-self.window_pos[1])):
                            if self.mines_not_generated:
                                self.generate_mines(tile)
                                self.mines_not_generated = False
                            if not tile.reveal():
                                for tile in self.tiles:
                                    tile.showMine = True
                                    self.lose = True

                elif event.dict['button'] == 3:
                    for tile in self.tiles:
                        if tile.is_touched((event.dict['pos'][0]-self.window_pos[0], event.dict['pos'][1]-self.window_pos[1])):
                            tile.toggle_flag()
        for tile in self.tiles:
            tile.draw(self.window_screen)

        
        self.backgound.draw()
        self.screen.blit(self.window_screen, self.window_pos)

        if self.verify_win():
            return ['demineur','menu']
        if self.lose :
            return ['demineur','menu']
