import pygame
import os

from programmes.components import Button,BackgroundTileSheet

class MenuMain:
    def __init__(self, screen) -> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.background = BackgroundTileSheet(self.screen, PATH_BACKGROUD_TILESHEET)
        self.buttons = [
            Button(screen,(50,40,'center'),(40,(16,4)),['demineur','menu'],os.sep.join(['assets','buttons','long_button.png']),None,'LeS aVeNTuReS DeS DaNNieS',(0,0,0)),
            Button(screen,(100,0,'top-right'),(7.5,(1,1)),['quit'],os.sep.join(['assets','buttons','cross_unpressed.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(100,5,'top-right'),(7.5,(5,5)),None,text='Quit',textColor=(0,0,0)),
            Button(screen,(50,70,"center"),(30,(15,5)),['pasDeVirus', 'menu'],os.sep.join(['assets','buttons','start_buttons_unpressed-01.png']),os.sep.join(['assets','buttons','start_buttons_pressed-01.png']),'',(255,2,10)),
            Button(screen,(35,50,'center'),(5,(1,1)),['quit'],os.sep.join(['assets','char_sprite','virus.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(65,50,'center'),(5,(1,1)),['quit'],os.sep.join(['assets','char_sprite','virus.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(100,15,'top-right'),(7.5,(1,1)),['menu','settings'],os.sep.join(['assets','buttons','settings_unpressed.png']),os.sep.join(['assets','buttons','settings_pressed.png']),'',(0,0,0)),
            Button(screen,(100,20,'top-right'),(7.5,(5,5)),['menu','settings'],text='settings',textColor=(0,0,0)),
        ]


    def update(self, events : list) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        output = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        break
        self.background.draw()

        for button in self.buttons:
            button.draw()

        if output:
            return output

