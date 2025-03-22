import pygame
from os import path

from programmes.settings import Settings
from programmes.menu import Menu
from programmes.pasDeVirus import update as PasDeVirus

class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()
        PATH_ASSETS = path.join(path.dirname(__file__),'..','assets','game')
        self.settings : Settings = Settings()
        self.screen = pygame.display.set_mode(self.settings.get_window_size())
        pygame.display.set_caption('mon jeu')
        pygame.display.set_icon(pygame.image.load(path.join(PATH_ASSETS,'icone.png')).convert_alpha())

        pygame.mouse.set_visible(False)
        PATH_ASSETS_CUTE = path.join(path.dirname(__file__),'..','assets','SproutLand')
        self.custom_cursor = pygame.image.load(path.join(PATH_ASSETS_CUTE, 'Sprite sheets', 'Mouse sprites', 'Catpaw Mouse icon.png')).convert_alpha()
        self.custom_cursor = pygame.transform.scale(self.custom_cursor, self.settings.get_mouse_size())
        
        #temporaire
        self.update = PasDeVirus.Update()

        self.active = Menu()

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

            output = self.active.update(events, self.screen)
            if not output:
                output = ['none']
            
            self.handle_output(output)
            

            #temporaire
            self.update.run()

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
                    self.active = Menu()
                self.active.handle_input(output[1:])
        
            case 'pasDeVirus':
                if type(self.active) != PasDeVirus:
                    self.active = Menu()
                self.active.handle_input(output[1:])