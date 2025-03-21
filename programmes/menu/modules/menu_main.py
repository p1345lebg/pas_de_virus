import pygame

class MenuMain:
    def __init__(self) -> None:
        pass

    def update(self, events : list, screen : pygame.Surface) -> list:
        """
            actualise le composant
            retourne une liste contenant les données à traiter
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.dict['button'] == 1:
                    return ['settings','windowSize',(580,300)]
                if event.dict['button'] == 3:
                    return ['settings','windowSize',(960,600)]
                if event.dict['button'] == 2:
                    return ['settings','save']