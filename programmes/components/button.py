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
        

    def draw(self,screen : pygame.Surface):
        cursor_pos = pygame.mouse.get_pos()
        texture : pygame.Surface = pygame.Surface(self.size)

        if self.texture_hoover and self.hitbox.collidepoint(cursor_pos):
            texture.blit(self.texture_hoover, (0,0))
        else:
            texture.blit(self.texture,(0,0))

        texture.blit(self.text,self.text.get_rect(center=self.hitbox.center))
        screen.blit(texture,(0,0))

