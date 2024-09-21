import pygame
from sys import exit
from Button import Button
class Canvas: 
    def __init__(self, size, title, fps): 
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.running = True
        self.clock = pygame.time.Clock()
        self.fps = fps 
        self.PLAY_BUTTON = Button("Play", (int(size[0] / 2),10), (100,100))
    def handleInputs(self): 
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.PLAY_BUTTON.listenForInput(mousePos): 
                    print("CLICK PLAY")
    def update(self): 
        pass
    def render(self): 

        self.PLAY_BUTTON.show(self.screen)
        


        pygame.display.update()
        self.clock.tick(self.fps)
        pass
    def run(self): 
        while self.running: 
            self.screen.fill((0,0,0))
            self.handleInputs()
            self.update()
            self.render()
        pygame.quit()
        