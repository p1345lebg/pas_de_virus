import pygame

from programmes.settings import Settings
from programmes.pasDeVirus import drawPieces

class Update:
    def __init__(self):
        pygame.init()
        self.settings : Settings = Settings()
        self.ground = self.settings.get_ground()
        self.screen = pygame.display.set_mode(self.settings.get_window_size())       
        self.drawPieces = drawPieces.DrawPieces(self.screen) 

    def run(self):
        self.drawPieces.draw(self.ground)
        pygame.display.flip()

