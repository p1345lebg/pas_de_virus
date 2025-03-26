import pygame
import os

from programmes.components import Button,BackgroundTileSheet

class MenuSettings:
    def __init__(self, screen) -> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(self.screen, PATH_BACKGROUD_TILESHEET)
        self.buttons = [
            Button(screen,(50,50,'center'),(50,(1,1)),None,os.sep.join(['assets','buttons','settings_window.png']),None,'',(0,0,0)),
            Button(screen,(0,0,'top-left'),(5,(5,5)),['menu','main_menu'],os.sep.join(['assets','buttons','back.png']),None,'',(0,0,0)),
            Button(screen,(0,5,'top-left'),(5,(5,5)),['menu','main_menu'],text='Back',textColor=(0,0,0)),
            Button(screen,(50,50,'center'),(50,(1,1)),None,os.sep.join(['assets','buttons','settings_window.png']),None,'',(0,0,0)),
            Button(screen,(50,50,'center'),(50,(1,1)),None,os.sep.join(['assets','buttons','settings_window.png']),None,'',(0,0,0)),
            Button(screen,(50,50,'center'),(50,(1,1)),None,os.sep.join(['assets','buttons','settings_window.png']),None,'',(0,0,0)),
            Button(screen,(50,50,'center'),(50,(1,1)),None,os.sep.join(['assets','buttons','settings_window.png']),None,'',(0,0,0)),
            Button(screen,(65,85,'center'),(5,(1,1)),['settings','resetDefault'],os.sep.join(['assets','buttons','reset.png']),None,'',(0,0,0)),
            Button(screen,(65,90,'center'),(15,(5,1)),['settings','resetDefault'],text='Reset to Default',textColor=(0,0,0)),
            Button(screen,(35,85,'center'),(5,(1,1)),['settings','save'],os.sep.join(['assets','buttons','tick_unpressed.png']),os.sep.join(['assets','buttons','tick_pressed.png']),'',(0,0,0)),
            Button(screen,(35,90,'center'),(5,(5,5)),['settings','save'],text='Save',textColor=(0,0,0)),
        ]

    def update(self, events) -> list:
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

