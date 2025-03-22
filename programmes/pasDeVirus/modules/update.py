import pygame

from programmes.settings import Settings
from programmes.pasDeVirus.modules import drawPieces

class Update:
    def __init__(self, screen):
        pygame.init()
        self.settings : Settings = Settings()
        self.ground = [["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"], 
                        ["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"], 
                        ["empty", "empty", "empty", "empty"], 
                            ["empty", "empty", "empty"],
                        ["empty", "empty", "empty", "empty"]]
        self.screen = screen
        self.drawPieces = drawPieces.DrawPieces(self.screen)

    def run(self, events, screen):
        
        self.manageEvents(events)

        self.drawPieces.draw(self.ground, screen)

    def manageEvents(self, events):
        pass