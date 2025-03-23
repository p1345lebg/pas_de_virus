import pygame
import os

from programmes.settings import Settings
from programmes.menu import Menu
from programmes.pasDeVirus import PasDeVirus


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        PATH_ASSETS = os.sep.join(['assets'])
        self.settings : Settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.get_window_size())
        pygame.display.set_caption('mon jeu')
        pygame.display.set_icon(pygame.image.load(os.sep.join([PATH_ASSETS,'icone.png'])).convert_alpha())

        pygame.mouse.set_visible(False)
        PATH_ASSETS_CUTE = os.sep.join(['assets','SproutLand'])
        self.custom_cursor = pygame.image.load(os.sep.join([PATH_ASSETS_CUTE, 'Sprite sheets', 'Mouse sprites', 'Catpaw Mouse icon.png'])).convert_alpha()
        self.custom_cursor = pygame.transform.scale(self.custom_cursor, self.settings.get_mouse_size())
        
        #temporaire
        self.active = Menu(self.screen)
        self.active = PasDeVirus(self.screen)

    def run(self) -> None:
        running : bool = True
        clock = pygame.time.Clock()

        output : list

        while running:
            self.screen.fill((0,0,0))
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False

            output = self.active.update(events)
            if output:
                print(output)
                self.handle_output(output)
            
            # Cursor custom
            mouse_x, mouse_y = pygame.mouse.get_pos()
            self.screen.blit(self.custom_cursor, (mouse_x, mouse_y))

            pygame.display.flip()
            clock.tick(self.settings.get_FPS())
        
        pygame.quit()

    def handle_output(self, output : list) -> None:
        match output[0]:
            case 'none':
                return
                
            case 'settings':
                self.settings.handle_input(output[1:])

            case 'menu':
                if type(self.active) != Menu:
                    self.active = Menu(self.screen)
                self.active.handle_input(output[1:])
        
            case 'pasDeVirus':
                if type(self.active) != PasDeVirus:
                    self.active = PasDeVirus(self.screen)
                self.active.handle_input(output[1:])