import pygame
from programmes.components import Button


class Part(Button):
    def __init__(self, screen, position, texture : str,):
        super().__init__(screen, (position[0],position[1],'center'), (5,(1,1)), texture=texture)
        self.screen = screen
        self.texture = texture
        
    def update_position(self, position):
        super().__init__(self.screen, (position[0],position[1],'center'), (5,(1,1)), texture=self.texture)


class Pawn:
    def __init__(self, screen, position : tuple[int,int], size, texture: str, otherPawns):
        self.screen = screen

    def move(self,direction):
        """
        Args
        direction(str) : diretion du mouvement ```'ul','ur','dl','dr'```
        """