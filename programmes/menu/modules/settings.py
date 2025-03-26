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

            Button(screen,(70,45,'center'),(10,(16,6)),['settings','reset'],os.sep.join(['assets','buttons','long_button.png']),None,'Reset',(0,0,0)),
            Button(screen,(37.5,45,'center'),(10,(5,5)),None,text='FPS',textColor=(0,0,0)),
            Button(screen,(40,50,'center'),(5,(1,1)),['settings','FPS',30],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'30',(0,0,0)),
            Button(screen,(50,50,'center'),(5,(1,1)),['settings','FPS',60],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'60',(0,0,0)),
            Button(screen,(60,50,'center'),(5,(1,1)),['settings','FPS',120],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'120',(0,0,0)),

            Button(screen,(70,60,'center'),(10,(16,6)),['settings','reset'],os.sep.join(['assets','buttons','long_button.png']),None,'Reset',(0,0,0)),
            Button(screen,(37.5,60,'center'),(25,(5,5)),None,text='Window size',textColor=(0,0,0)),
            Button(screen,(36,70,'center'),(8,(1,1)),['settings','windowSize',(960,540)],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'960x540',(0,0,0)),
            Button(screen,(46,70,'center'),(8,(1,1)),['settings','windowSize',(1920,1080)],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'1920x1080',(0,0,0)),
            Button(screen,(56,70,'center'),(8,(1,1)),['settings','windowSize',(3840,2160)],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'3840x2160',(0,0,0)),
            Button(screen,(66,70,'center'),(8,(1,1)),['settings','fullScreen'],os.sep.join(['assets','buttons','main_button_unpressed_01.png']),os.sep.join(['assets','buttons','main_button_pressed_01.png']),'Full Screen *',(0,0,0)),
            Button(screen,(100,100,'bottom-right'),(10,(9,6)),None,text='*en développement',textColor=(0,0,0)),
            
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

