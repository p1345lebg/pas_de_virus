import pygame
from random import choices

class BackgroundTileSheet:
    def __init__(self, screen, tileSheet : str) -> None:
        """
        background

        Args:
            -screen (pygame.Surface) : écran sur lequel ets dessiné le fond d'écran
            -tileSheet (pygame.Surface) : chemin vers la tileSheet
        """
        tileSheet = pygame.image.load(tileSheet)
        self.screen : pygame.Surface
        tileSheet_width : int = tileSheet.get_width()
        tileSheet_height : int = tileSheet.get_height()
        TILE_SHEET : list[pygame.Surface] = []
        for y in range(0, tileSheet_height, tileSheet_height//7):
            for x in range(0, tileSheet_width, tileSheet_width//11):
                TILE_SHEET.append(tileSheet.subsurface((x,y),(tileSheet_width//11,tileSheet_height//7)))
        
        self.TILE_SHEET : list[pygame.Surface] = [TILE_SHEET[1+11*1]]+ TILE_SHEET[11*5:11*5+6]+ TILE_SHEET[11*6:11*6+6]

        self.tileSheet : list[pygame.Surface]
        self.background : pygame.Surface
        self.update_screen(screen)

    def update_screen(self, screen):
        self.screen = screen
        screenSize_x, screenSize_y = self.screen.get_size()
        tileSize = min(screenSize_x,screenSize_y)//20
        backgroundSize = max(screenSize_x,screenSize_y)
        self.background = pygame.Surface((backgroundSize, backgroundSize))


        tileSheet : list[pygame.Surface] = []
        for tile in self.TILE_SHEET:
            tileSheet.append(pygame.transform.scale(tile,(tileSize,tileSize)))

        l = len(tileSheet)
        proba = [0.8] + [0.2/l]*(l-1)

        y = 0
        while y<backgroundSize:
            x = 0
            while x<backgroundSize:
                tile = choices(tileSheet, proba)
                self.background.blit(tile[0], (x,y))
                x+=tileSize
            y+=tileSize

        self.backgroundRect = self.background.get_rect(center=(screenSize_x // 2, screenSize_y // 2))

    def draw(self):
        self.screen.blit(self.background,self.backgroundRect.topleft)