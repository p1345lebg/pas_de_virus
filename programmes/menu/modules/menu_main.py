import pygame
import os

from programmes.components import Button

class MenuMain:
    def __init__(self, screen) -> None:
        self.buttons = {
            Button(screen,(0,0,'top-left'), (10,(1,1)), ['pasDeVirus', 'menu'], texture_hoover='SproutTiles/Objects/Free_Chicken_House.png', text='BONJOUR')
        }


    def update(self, events : list, screen : pygame.Surface) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        return output
        
        for button in self.buttons:
            button.draw()