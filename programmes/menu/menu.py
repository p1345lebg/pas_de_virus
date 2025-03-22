from .modules import MenuMain

class Menu:

    def __init__(self, screen):
        self.screen = screen
        self.active = MenuMain(self.screen)

    def update(self, events, screen) -> list:
        output = self.active.update(events, screen)
        if output:
            return self.handle_output(output)

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = MenuMain(self.screen)

    def handle_output(self, output):
        if output:
            if output[0] == 'main_menu':
                self.handle_input(output[1:])
            else:
                return output