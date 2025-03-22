import pygame
import os
from programmes.components import Button

class MenuMain:
    def __init__(self) -> None:
        self.buttons = {
        }


    def update(self, events : list, screen : pygame.Surface) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        click = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
        
        for button in self.buttons:
            button.update(screen,click)