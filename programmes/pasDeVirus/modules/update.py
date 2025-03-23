import pygame

from programmes.settings import Settings
from programmes.pasDeVirus.modules import draw

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
        self.draw = draw.Draw(self.screen)

    def run(self, events, screen):
        
        self.manageEvents(events)

        self.draw.draw_background(screen)
        self.draw.draw_pieces(self.ground, screen)

    def manageEvents(self, events):
        pass