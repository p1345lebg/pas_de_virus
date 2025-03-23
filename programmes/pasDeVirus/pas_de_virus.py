from .modules import Game, Menu

from programmes.components import Button

class PasDeVirus:
    def __init__(self, screen)->None:
        self.screen = screen
        self.active = Game(self.screen)

    def update(self, events) -> list:
        output = self.active.run(events)
        if output:
            return self.handle_output(output)

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = Menu(self.screen)

            case 'game':
                self.active = Game()

    def handle_output(self, output):
        if output:
            if output[0] == 'pasDeVirus':
                self.handle_input(output[1:])
            else:
                return output