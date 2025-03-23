from programmes.components import Button
import pygame

class Menu:
    def __init__(self, screen)-> None:
        self.buttons = {
            Button(screen, (0,0,'middle'),(10,(2,1)), ['menu','main_menu'])
        }

    def run(self, events, screen):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button in self.buttons:
                    output = button.handle_click()
                    if output:
                        return output
        
        for button in self.buttons:
            button.draw()