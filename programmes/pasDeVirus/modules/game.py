import pygame
import os

from programmes.components import BackgroundTileSheet
from .items import Draw,PlayGround

class Game:
    def __init__(self, screen):
        self.screen = screen
        tileSheet = pygame.image.load(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(screen, tileSheet)
        self.playground = PlayGround(self.screen, [[1]])
        self.ground = [["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"], 
                        ["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"], 
                        ["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty"]]
        self.screen = screen
        self.draw = Draw(self.screen)

    def run(self, events):
        
        self.manageEvents(events)

        self.background.draw()
        self.playground.draw()

    def manageEvents(self, events):
        pass