class MenuSettings:
    def __init__(self, screen) -> None:
        self.screen = screen

    def update(self, events) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """