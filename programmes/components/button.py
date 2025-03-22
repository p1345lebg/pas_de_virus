import pygame
import os

class Button(pygame.sprite.Sprite):
    def __init__(self, screen:  pygame.Surface , position : tuple[int,int,str], size : tuple[int,tuple[int,int]], action : list = ['none'], texture : str = 'default/button.png', texture_hoover : str = None, text : str = ''):
        """
        bouton

        Args:
            screen (pygame.Surface) : surface sur laquelle est dessiné le bouton
            position (tuple[int,int,str]) : poistion du bouton (en pourcentage), la troisieme valeur determine à partir d'où la position est calculée
            size (tuple[tuple[int,int],int]) : taille du bouton, le premier tuple contient la largeur en pourcentage par rapport a la fenetre et le deuxieme le ratio
            action (list) : liste contenant les action a effectuer par le bouton
            texture (str) : chemin vers la texture a partir du dossier "assets"
            texture_hoover (str) : chemin vers la texture a partir du dossier "assets"
            texte (str) : texte affiché sur le bouton
        """
        super().__init__()

        PATH_TEXTURE = os.path.join(os.path.dirname(__file__),'..','..','assets',texture)
        PATH_TEXTURE_HOOVER = os.path.join(os.path.dirname(__file__),'..','..','assets',texture_hoover) if texture_hoover else None
        self.PATH_FONT = os.path.join(os.path.dirname(__file__),'..','..','assets','SproutLand','fonts','pixelFont-7-8x14-sproutLands.ttf')
        self.font : pygame.font.Font

        self.screen : pygame.Surface
        self.POSITION : tuple[int,int,str] = position
        self.SIZE : tuple[int,int] = size
        self.action : list = action
        self.TEXTURE : pygame.Surface = pygame.image.load(PATH_TEXTURE)
        if texture_hoover:
            self.TEXTURE_HOOVER : pygame.Surface = pygame.image.load(PATH_TEXTURE_HOOVER)
        else:
            self.TEXTURE_HOOVER =  None
        self.TEXT : str = text
        
        self.position : tuple[int,int]
        self.size : tuple[int,int]
        self.texture : pygame.Surface
        self.textureHoover : pygame.Surface
        self.hitbox : pygame.Rect

        self.update_screen(screen)

    def update_screen(self, screen):
        self.screen = screen
        screenSize_x = self.screen.get_width()
        screenSize_y = self.screen.get_height()

        width = screenSize_x*self.SIZE[0]//100
        height = width//self.SIZE[1][0]*self.SIZE[1][1]
        self.size = (width, height)

        x = self.POSITION[0]
        y = self.POSITION[1]
        match self.POSITION[2]:
            case 'top-left':
                self.position = (screenSize_x*x/100, screenSize_y*y/100)
            case 'top' : 
                self.position = (screenSize_x*x/100-self.size[0]//2, screenSize_y*y/100)
            case 'top-right':
                self.position = (screenSize_x*x/100-self.size[0], screenSize_y*y/100)
            case 'left' :
                self.position = (screenSize_x*x/100, screenSize_y*y/100-self.size[1]//2)
            case 'middle' : 
                self.position = (screenSize_x*x/100-self.size[0]//2, screenSize_y*y/100-self.size[1]//2)
            case 'right' : 
                self.position = (screenSize_x*x/100-self.size[0], screenSize_y*y/100-self.size[1]//2)
            case 'bottom-left' : 
                self.position = (screenSize_x*x/100, screenSize_y*y/100-self.size[1])
            case 'bottom' :
                self.position = (screenSize_x*x/100-self.size[0]//2, screenSize_y*y/100-self.size[1])
            case 'bottom-right' :
                self.position = (screenSize_x*x/100-self.size[0], screenSize_y*y/100-self.size[1])

        self.texture = pygame.transform.scale(self.TEXTURE, self.size)
        if self.TEXTURE_HOOVER:
            self.textureHoover = pygame.transform.scale(self.TEXTURE_HOOVER, self.size)
        self.hitbox = self.texture.get_rect(topleft=(x, y))

        font_size = self.hitbox.height  # Commence par la hauteur du bouton
        while font_size > 0:
            font = pygame.font.SysFont(self.PATH_FONT, font_size)
            text_surface = font.render(self.TEXT, True, (0,0,0))
            if text_surface.get_width() <= self.hitbox.width and text_surface.get_height() <= self.hitbox.height:
                break  # La taille de police convient
            font_size -= 1
        self.font = font
        self.text_surface = text_surface

    def draw(self):
        cursor_pos = pygame.mouse.get_pos()
        if self.hitbox.collidepoint(cursor_pos) and self.TEXTURE_HOOVER:
            self.screen.blit(self.textureHoover, self.position)
        else:
            self.screen.blit(self.texture, self.position)

        if self.TEXT:
            text_surface = self.font.render(self.TEXT, True, (0, 0, 0))
            text_rect = text_surface.get_rect(center=self.hitbox.center)
            self.screen.blit(text_surface, text_rect)

    def handle_click(self):
        cursor_pos = pygame.mouse.get_pos()
        if self.hitbox.collidepoint(cursor_pos):
            return self.action