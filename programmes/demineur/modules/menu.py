from programmes.components import Button,BackgroundTileSheet
import pygame
import os

class Menu:
    def __init__(self, screen)-> None:
        self.screen = screen
        PATH_BACKGROUD_TILESHEET = os.path.join(os.sep.join(['assets','SproutTiles','Tilesets','Grass.png']))
        self.backgroundTileSheet = pygame.image.load(PATH_BACKGROUD_TILESHEET)
        self.background = BackgroundTileSheet(self.screen, PATH_BACKGROUD_TILESHEET)
        self.buttons = {
            Button(screen,(0,0,'top-left'),(5,(5,5)),['menu','main_menu'],os.sep.join(['assets','buttons','home_unpressed.png']),os.sep.join(['assets','buttons','home_pressed.png']),'',(0,0,0)),
            Button(screen,(0,5,'top-left'),(5,(5,5)),['menu','main_menu'],text='Home',textColor=(0,0,0)),
            Button(screen,(100,0,'top-right'),(5,(1,1)),['quit'],os.sep.join(['assets','buttons','cross_unpressed.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(100,5,'top-right'),(5,(5,5)),['quit'],text='Quit',textColor=(0,0,0)),
            Button(screen,(50,25,'center'),(40,(20,5)),None,os.sep.join(['assets','buttons','long_button.png']),None,'Select a level',(0,0,0)),
            Button(screen,(25,50,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','easy.png']),None,'',(255,2,10)),
            Button(screen,(25+50/6,60,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','oh.png']),None,'',(255,2,10)),
            Button(screen,(25+50/6+50/6,75,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','normal.png']),None,'',(255,2,10)),
            Button(screen,(75-50/6-50/6,75,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','hard.png']),None,'',(255,2,10)),
            Button(screen,(75-50/6,60,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','really_hard.png']),None,'',(255,2,10)),
            Button(screen,(75,50,'center'),(10,(5,5)),['demineur','game',(9,9),10],os.sep.join(['assets','level_icone','diabolical.png']),None,'',(255,2,10))
        }

    def update(self, events):
        output = None
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                if event.dict['button'] == 1:
                    for button in self.buttons:
                        output = button.handle_click()
                        if output:
                            break
        self.background.draw()

        for button in self.buttons:
            button.draw()

        if output:
            return output