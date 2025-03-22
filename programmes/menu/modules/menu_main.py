import pygame
import os
from programmes.components import Button

class MenuMain:
    def __init__(self, screen) -> None:
        self.buttons = {
            Button(screen,(50,50,'middle'), (10,(16,9)), ['settings', 'windowSize',(960,600)], texture_hoover='SproutTiles/Objects/Free_Chicken_House.png'),
            Button(screen,(0,0,'top-left'), (50,(1,1)), ['settings', 'save'],texture_hoover='SproutTiles/Objects/Free_Chicken_House.png', text='bonjour')
        }


    def update(self, events : list, screen : pygame.Surface) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        click = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        return output
        
        for button in self.buttons:
            button.draw()