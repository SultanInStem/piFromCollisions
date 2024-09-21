import pygame
from sys import exit
class Canvas: 
    def __init__(self, size, title): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.running = True
        pygame.display.set_caption(title)
    def handleInputs(self): 
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                exit()
    def update(self): 
        pass
    def render(self): 
        pass
    def run(self): 
        while self.running: 
            self.handleInputs()
            self.update()
            self.render()
        