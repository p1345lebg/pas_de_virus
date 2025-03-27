import json
import os

from programmes.components import Button

from .modules import Game, Menu

class Demineur:
    def __init__(self, screen)->None:
        self.screen = screen
        self.active = Menu(self.screen)

    def update(self, events) -> list:
        output = self.active.update(events)
        if output:
            return self.handle_output(output)

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = Menu(self.screen)

            case 'game':
                self.handle_game(input[1:])

    def handle_output(self, output):
        if output:
            if output[0] == 'demineur':
                self.handle_input(output[1:])
            else:
                return output
            
    def handle_game(self, input):
        self.active = Game(self.screen, input[0], input[1])
