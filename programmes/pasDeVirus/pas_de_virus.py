from .modules import Update

from programmes.components import Button

class PasDeVirus:
    def __init__(self, screen):
    #     self.screen = screen
    #     self.active = Update(self.screen)

    # def update(self, events) -> list:
    #     self.handle_output(self.active.run(events, self.screen))
    #     output = self.active.run(events, self.screen)
    #     if output:
    #         return self.handle_output(output)

        self.active = Update(screen)

    def update(self, events, screen) -> list:
        self.handle_output(self.active.run(events, screen))

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = Update()

    def handle_output(self, output):
        if output:
            if output[0] == 'pasDeVirus':
                self.handle_input(output[1:])
            else:
                return output