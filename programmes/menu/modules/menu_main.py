import pygame
import os

from programmes.components import Button,BackgroundTileSheet

class MenuMain:
    def __init__(self, screen) -> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(self.screen, PATH_BACKGROUD_TILESHEET)
        self.buttons = {
            Button(screen,(50,50,"center"),(10,(15,5)),[],os.sep.join(['assets','buttons','start_buttons_unpressed-01.png']),os.sep.join(['assets','buttons','start_buttons_pressed-01.png']),'',(255,2,10))
        }


    def update(self, events : list) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        return output
        self.background.draw()

        for button in self.buttons:
            button.draw()

