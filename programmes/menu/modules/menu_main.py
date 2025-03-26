import pygame
import os

from programmes.components import Button,BackgroundTileSheet

class MenuMain:
    def __init__(self, screen) -> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(self.screen, PATH_BACKGROUD_TILESHEET)
        self.buttons = {
            Button(screen,(100,0,'top-right'),(5,(1,1)),['quit'],os.sep.join(['assets','buttons','cross_unpressed.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(100,5,'top-right'),(5,(5,5)),['quit'],text='Quit',textColor=(0,0,0)),
            Button(screen,(50,70,"center"),(30,(15,5)),['pasDeVirus', 'menu'],os.sep.join(['assets','buttons','start_buttons_unpressed-01.png']),os.sep.join(['assets','buttons','start_buttons_pressed-01.png']),'',(255,2,10)),
            Button(screen,(50,0,'top'),(50,(1,1)),['quit'],text='LeS aVeNTuReS De DaNNy',textColor=(0,0,0)),
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

