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
        self.water_lily = pygame.transform.scale(self.get_sprite(2, 2), (self.height/10.8, self.width/19.2))
        self.sizePiece = self.water_lily.get_size()
        self.widthOffset = self.width/12
        self.heightOffset = self.height/12
        
        # Var defini dans la fonction draw
        self.beginX3 = 0
        self.beginY3 = 0
        self.beginX4 = 0
        self.beginY4 = 0

    def draw(self, ground):
        # Pour les terrains de taille 3x3
        total_width3 = (2) * self.widthOffset + self.sizePiece[0]
        total_height3 = (6) * self.heightOffset + self.sizePiece[1]
        self.beginX3 = (self.width - total_width3) / 2
        self.beginY3 = (self.height - total_height3) / 2   
        # Pour les terrains de taille 4x4
        total_width4 = (3) * self.widthOffset + self.sizePiece[0]
        total_height4 = (6) * self.heightOffset + self.sizePiece[1]
        self.beginX4 = (self.width - total_width4) / 2
        self.beginY4 = (self.height - total_height4) / 2


        for i in range(len(ground)):
            for y in range(len(ground[i])):
                if len(ground[i]) % 4 != 0:
                    self.draw_element(self.screen, ground[i][y], (y, i), (self.beginX3, self.beginY3))
                else:
                    self.draw_element(self.screen, ground[i][y], (y, i), (self.beginX4, self.beginY4))
    
    def draw_element(self, screen, element, position, begin):
        if element == "empty":
            screen.blit(self.water_lily, (position[0] * (self.widthOffset) + begin[0], position[1] * (self.heightOffset) + begin[1]))
    
    def get_sprite(self, x, y):
        sprite = pygame.Surface((16, 16), pygame.SRCALPHA).convert_alpha()
        sprite.blit(self.sprite_sheet, (0, 0), (x * 16, y * 16, 16, 16))
        return sprite