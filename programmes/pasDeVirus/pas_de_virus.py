from .modules import Menu

from programmes.components import Button

class PasDeVirus:
    def __init__(self):
        self.active = Menu()

    def update(self, events, screen) -> list:
        self.handle_output(self.active.update(events, screen))

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = Menu

    def handle_output(self, output):
        if output[0] == 'pasDeVirus':
            self.handle_input(output[1:])
        else:
            return output