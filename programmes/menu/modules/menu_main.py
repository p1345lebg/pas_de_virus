import pygame
from programmes.components import Button

class MenuMain:
    def __init__(self) -> None:
        self.buttons = {
            Button(size=(192,64),action=['settings','save'], text='bonjour')
        }


    def update(self, events : list, screen : pygame.Surface) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """

        for button in self.buttons:
            button.draw(screen)