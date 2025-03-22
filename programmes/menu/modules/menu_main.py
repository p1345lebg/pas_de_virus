import pygame
import os
from programmes.components import Button

class MenuMain:
    def __init__(self) -> None:
        self.buttons = {
            Button(size=(192,64),action=['settings','save'], text='bonjour', texture=os.sep.join(['SproutLand','Sprite sheets','Setting menu.png'])),
            Button(size=(192,64),action=['settings','mouseSize',(20,20)], text='bonjour', texture=os.sep.join(['SproutLand','Sprite sheets','Setting menu.png']),position=(100,100,'bottom-left'))
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