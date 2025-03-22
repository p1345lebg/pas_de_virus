import pygame
import os

class Button(pygame.sprite.Sprite):
    def __init__(self,
                 position : tuple[int,int,str] = (0,0,'top-left'),
                 size : tuple[int,int] = (10,10), 
                 action : list = ['none'],
                 *groups, 
                 texture : str = 'default/button.png', 
                 texture_hoover : str = None,
                 text : str = ''):
        super().__init__(*groups)


        self.size = size

        self.PATH_texture = os.path.join(os.path.dirname(__file__),'..','..','assets',texture)
        self.texture = pygame.transform.scale(pygame.image.load(self.PATH_texture).convert_alpha(),size)
        if texture_hoover:
            self.PATH_texture_hoover = os.path.join(os.path.dirname(__file__),'..','..','assets',texture_hoover)
            self.texture = pygame.transform.scale(pygame.image.load(self.PATH_texture_hoover).convert_alpha(),size)
        else:
            self.texture_hoover = None

        font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'..','..','assets','SproutLand','fonts','pixelFont-7-8x14-sproutLands.ttf'))
        self.text = font.render(text, True, (123,123,123))
        

        self.hitbox : pygame.Rect = self.texture.get_rect()

        self.position = position

    def update(self,screen : pygame.Surface, click : bool = False):
        cursor_pos = pygame.mouse.get_pos()
        texture : pygame.Surface = pygame.Surface(self.size)

        if self.texture_hoover and self.hitbox.collidepoint(cursor_pos):
            texture.blit(self.texture_hoover, (0,0))
        else:
            texture.blit(self.texture,(0,0))

        texture.blit(self.text,self.text.get_rect(center=self.hitbox.center))

        screenSize = screen.get_size()
        match self.position[2]:
            case 'top-left':
                screen.blit(texture,self.position[:2])

        screen.blit(texture,(0,0))


class Button(pygame.sprite.Sprite):
    def __init__(self, position : tuple[int,int,str], size : tuple[int,int], action : list = ['none'], texture : str = 'default/button', texture_hoover : str = None, text : str = ''):
        """
        bouton

        Args:
            position (tuple[int,int,str]) : poistion du bouton (en pourcentage), la troisieme valeur determine à partir d'où la position est calculée
            size (tuple[int,int]) : taille du bouton (en pourcentage par rapport a la fenetre)
            action (list) : liste contenant les action a effectuer par le bouton
            texture (str) : chemin vers la texture a partir du dossier "assets"
            texture_hoover (str) : chemin vers la texture a partir du dossier "assets"
            texte (str) : texte affiché sur le bouton
        """
        super().__init__()

        PATH_TEXTURE = os.path.join(os.path.dirname(__file__),'..','..','assets',texture)
        PATH_TEXTURE_HOOVER = os.path.join(os.path.dirname(__file__),'..','..','assets',texture_hoover)
        self.font = pygame.font.Font(os.path.join(os.path.dirname(__file__),'..','..','assets','SproutLand','fonts','pixelFont-7-8x14-sproutLands.ttf'))

        self.POSITION = position
        self.SIZE = size
        self.action = action
        self.TEXTURE = pygame.image.load(PATH_TEXTURE)
        self.TEXTURE_HOOVER = pygame.image.load(PATH_TEXTURE_HOOVER)


