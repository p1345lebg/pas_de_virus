import pygame
from os import path

class DrawPieces:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.load_assets()

    def load_assets(self):
        PATH_ASSETS_SHEET = path.join(path.dirname(__file__),'..', '..','assets','SproutTiles')
        self.sprite_sheet = pygame.image.load(path.join(PATH_ASSETS_SHEET, 'Objects', 'Basic_Grass_Biom_things.png')).convert_alpha()
        self.water_lily = pygame.transform.scale(self.get_sprite(3, 2), (self.height/10.8, self.width/19.2))

    def draw(self, ground):
        for i in range(len(ground)):
            for y in range(len(ground[i])):
                if len(ground[i]) % 4 != 0:
                    self.draw_element(self.screen, ground[i][y], (y, i), (self.height/1.4, self.width/8))
                else:
                    self.draw_element(self.screen, ground[i][y], (y, i), (self.height/1.45, self.width/8))
    
    def draw_element(self, screen, element, position, begin):
        if element == "empty":
            screen.blit(self.water_lily, (position[0] * 30 + begin[0], position[1] * 30 + begin[1]))
    
    def get_sprite(self, x, y):
        sprite = pygame.Surface((16, 16), pygame.SRCALPHA).convert_alpha()
        sprite.blit(self.sprite_sheet, (0, 0), (x * 16, y * 16, 16, 16))
        return sprite