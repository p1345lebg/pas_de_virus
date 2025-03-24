import pygame
import os

from programmes.components import Button,BackgroundTileSheet

class MenuMain:
    def __init__(self, screen) -> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.backgroundTileSheet = pygame.image.load(PATH_BACKGROUD_TILESHEET)
        self.background = BackgroundTileSheet(self.screen, self.backgroundTileSheet)
        self.buttons = {
            Button(screen,(0,0,'top-left'), (10,(1,1)), ['pasDeVirus', 'game', 'baby', 'level1'], texture_hoover=os.sep.join(['assets','SproutTiles','Objects','Free_Chicken_House.png']), text='BONJOUR', textColor=(255, 255, 0))
        }


    def update(self, events : list) -> list:
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
        self.background.draw()

        for button in self.buttons:
            button.draw()

