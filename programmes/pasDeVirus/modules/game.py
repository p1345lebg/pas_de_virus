import pygame
import os

from programmes.components import BackgroundTileSheet
from .items import Draw

class Game:
    def __init__(self, screen):
        tileSheet = pygame.image.load(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(screen, tileSheet)
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

        self.draw.draw_pieces(self.ground, self.screen)
        self.background.draw()

    def manageEvents(self, events):
        pass