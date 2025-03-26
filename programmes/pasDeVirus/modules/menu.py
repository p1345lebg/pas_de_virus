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
            Button(screen,(50,50,'center'),(5,(5,5)),['pasDeVirus','game','baby','level1'],os.sep.join(['assets','level_icone','easy.png']),None,'',(255,2,10))
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