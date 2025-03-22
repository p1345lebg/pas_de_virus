from .modules import MenuMain

class Menu:
    def __init__(self):
        self.active = MenuMain()

    def update(self, events, screen) -> list:
        return self.active.update(events, screen)

    def handle_input(self, input : list):
        if input[0] == 'main_menu':
            if type(self.active) == MenuMain:
                print("deja dans le menu")
                return ['error','existe deja']
            self.active = MenuMain()

    def __init__(self):
        self.active = MenuMain()

    def update(self, events, screen) -> list:
        self.handle_output(self.active.update(events, screen))

    def handle_input(self, input : list):
        match input[0]:
            case 'menu':
                self.active = MenuMain()

    def handle_output(self, output):
        if output[0] == 'main_menu':
            self.handle_input(output[1:])
        else:
            return output