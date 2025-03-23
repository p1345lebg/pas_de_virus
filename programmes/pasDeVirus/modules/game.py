import pygame
import os

from programmes.components import BackgroundTileSheet
from .items import Draw,PlayGround

class Game:
    def __init__(self, screen : pygame.Surface, disposition : list[list[list]]):
        self.screen : pygame.Surface = screen
        tileSheet = pygame.image.load(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(screen, tileSheet)
        self.playground = PlayGround(self.screen, [[1]])
        self.positions = PlayGround.get_position()

    def run(self, events):
        
        self.manageEvents(events)

        self.background.draw()
        self.playground.draw()

    def manageEvents(self, events):
        pass