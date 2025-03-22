import pygame
import os
from programmes.components import Button

class MenuMain:
    def __init__(self, screen) -> None:
        self.buttons = {
            Button(screen,(50,50,'middle'), (10,(16,9)), ['pasDeVirus', 'menu']),
            Button(screen,(0,0,'top-left'), (50,(1,1)), ['pasDeVirus', 'menu'],texture_hoover='SproutTiles/Objects/Free_Chicken_House.png', text='boncour')
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
            button.draw()