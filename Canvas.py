import pygame
from sys import exit
from Button import Button
from Ground import Ground
class Canvas: 
    def __init__(self, size, title, fps): 
        pygame.init()
        self.size = size 
        self.ground_height = 300 
        self.colors = {
            "black": (0,0,0), 
            "white": (255,255,255), 
            "light_green": (144,238,144), 
            "light_blue": (173, 216, 230)
        }
        self.running = True
        self.PLAY_BUTTON = Button("Play", (-50 + size[0] // 2, 10), (100,80)) 

        self.fps = fps 
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()


        self.ground = Ground((size[0], 200), (0,size[1] - 200), self.colors['light_green'])


    def handleInputs(self): 
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.PLAY_BUTTON.listenForInput(mousePos): 
                    self.PLAY_BUTTON.set_click()
    def update(self): 
        pass
    def render(self): 

        self.PLAY_BUTTON.show(self.screen)
        self.ground.show(self.screen)

        pygame.display.update()
        self.clock.tick(self.fps)
        pass
    def run(self): 
        while self.running: 
            self.screen.fill(self.colors['light_blue'])
            self.handleInputs()
            self.update()
            self.render()
        pygame.quit()
        