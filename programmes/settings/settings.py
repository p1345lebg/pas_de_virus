import os
import json
import pygame

class Settings:
    def __init__(self) -> None:
        self.PATH : str = os.path.join(os.path.dirname(__file__),'..','..','data','settings')
        with open(os.path.join(self.PATH,'settings.json'),'r') as file:
            self.settings : dict = json.load(file)
        self.saved : bool = True
        
        self.MOUSE = pygame.image.load(os.sep.join(['assets','mouse','triangle.png']))
        self.textureMouse = pygame.transform.scale(self.MOUSE,self.settings['mouseSize'])


    def handle_input(self, input):
        match input[0]:
            case 'save':
                if not self.saved:
                    with open(os.path.join(self.PATH,'settings.json'), 'w') as file:
                        json.dump(self.settings, file, indent=2)
                        pygame.display.set_mode(self.settings['windowSize'])
                    self.saved = True
                    self.textureMouse = pygame.transform.scale(self.MOUSE,self.settings['mouseSize'])

            case 'windowSize':
                self.settings['windowSize'] = input[1] if type(input[1]) == tuple else (960,600)
                self.saved = False

            case 'FPS':
                self.settings['FPS'] = input[1] if type(input[1]) == int else 60
                self.saved = False

            case 'reset':
                with open(os.path.join(self.PATH,'settings.json'),'r') as file:
                    self.settings = json.load(file)
                self.saved = False

            case 'resetDefault':
                with open(os.path.join(self.PATH,'settingsDefault.json'),'r') as file:
                    self.settings = json.load(file)
                self.saved = False

            case 'mouseSize':
                self.settings['mouseSize'] = input[1] if type(input[1]) == tuple else (40,40)
                self.saved = False

            case 'fullScreen':
                pygame.display.toggle_fullscreen()

    def get_window_size(self) -> tuple[int,int]:
        return self.settings['windowSize']

    def get_FPS(self) -> int:
        return self.settings['FPS']
    
    def get_mouse_size(self):
        return self.settings['mouseSize']
    
    def get_mouse_texture(self):
        return self.textureMouse
        
