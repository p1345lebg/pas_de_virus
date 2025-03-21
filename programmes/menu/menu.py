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