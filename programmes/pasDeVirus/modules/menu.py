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
            Button(screen,(84,15,'center'),(5,(1,1)),None,os.sep.join(['assets','buttons','cross_pressed.png']),os.sep.join(['assets','buttons','cross_pressed.png']),'',(0,0,0)),
            Button(screen,(50,25,'center'),(20,(20,5)),None,os.sep.join(['assets','buttons','long_button.png']),None,'Select a level',(0,0,0)),
            Button(screen,(25,50,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','easy.png']),None,'',(255,2,10)),
            Button(screen,(25+25/6,60,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','oh.png']),None,'',(255,2,10)),
            Button(screen,(25+25/6+25/6,75,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','normal.png']),None,'',(255,2,10)),
            Button(screen,(75-26/6-26/6,75,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','hard.png']),None,'',(255,2,10)),
            Button(screen,(75-26/6,60,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','really_hard.png']),None,'',(255,2,10)),
            Button(screen,(75,50,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','diabolical.png']),None,'',(255,2,10))
        }

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        return output
        self.background.draw()

        for button in self.buttons:
            button.draw()