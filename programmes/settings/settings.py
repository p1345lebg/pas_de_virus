import os
import json

class Settings:
    def __init__(self) -> None:
        self.PATH : str = os.path.join(os.path.dirname(__file__),'..','..','data','settings','settings.json')
        with open(self.PATH,'r') as file:
            self.settings : dict = json.load(file)
        self.saved : bool = True

    def handle_input(self, input):
        pass

    def save(self) -> None:
        with open(self.PATH, 'w') as file:
            json.dump(self.settings, file, indent=2)
        self.saved = True

    def reset(self) -> None:
        with open(self.PATH,'r') as file:
            self.settings : dict = json.load(file)
        self.saved = False

    def default(self) -> None:
        with open(self.PATH,'r') as file:
            self.settings : dict = json.load(file)
        self.saved = False

    def get_window_size(self) -> tuple[int,int]:
        return self.settings['windowSize']

    def set_window_size(self, newSize : tuple[int,int] = (960,600)) -> None:
        self.settings['windowSize'] = newSize
        self.saved = False

    def get_FPS(self) -> int:
        return self.settings['FPS']

    def set_FPS(self, newFPS : int = 60) -> None:
        self.settings['FPS'] = newFPS

