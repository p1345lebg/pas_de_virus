import pygame
import os

from programmes.components import BackgroundTileSheet
from .items import Draw,PlayGround

class Game:
    def __init__(self, screen : pygame.Surface, level : dict[str,list[list[list]]|int]):
        self.screen : pygame.Surface = screen
        self.background = BackgroundTileSheet(screen, os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.playground = PlayGround(self.screen, level)
        #self.positions = self.playground.get_position()

    def update(self, events):
        for event in events:
            break

        self.background.draw()
        self.playground.draw()