import pygame
from sys import exit
from utils.Button import Button
from utils.Ground import Ground
from utils.Block import Block 
from utils.Slider import Slider
class Canvas: 
    def __init__(self, size, title, fps): 
        pygame.init()
        self.is_paused = False 
        self.size = size 
        ground_height = 200 
        self.small_block = Block((50,size[1] - ground_height), (100,100), 10, 0)
        self.big_block = Block((200,size[1] -  ground_height), (200,200), 100, -1)
        self.colors = {
            "black": (0,0,0), 
            "white": (255,255,255), 
            "light_green": (144,238,144), 
            "light_blue": (173, 216, 230), 
            "red": (111,11,11)
        }
        self.running = True
        self.PLAY_BUTTON = Button("Pause", (-50 + size[0] // 2, 10), (100,80)) 

        self.fps = fps 
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

        self.ground = Ground((0,size[1] - ground_height), (size[0], ground_height), self.colors['light_green'])

        self.sliders = [
            Slider((100,100), (100,30), 0.5, 0,100)
        ]


    def handleInputs(self): 
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                if self.PLAY_BUTTON.listenForInput(mousePos): 
                    self.PLAY_BUTTON.set_click()
                    self.is_paused = not self.is_paused
    def update(self): 
        self.big_block.move()
        self.small_block.move()

    def render(self): 
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        self.PLAY_BUTTON.show(self.screen)
        self.ground.show(self.screen)
        self.small_block.show(self.screen)
        self.big_block.show(self.screen)
        for slider in self.sliders: 
            if slider.container_rect.collidepoint(mouse_pos) and mouse[0]: 
                slider.move_slider(mouse_pos)
            slider.render(self.screen)
            slider.get_value()
        pygame.display.update()
        self.clock.tick(self.fps)
    def run(self): 
        while self.running: 
            self.screen.fill(self.colors['light_blue'])
            self.handleInputs()
            if self.is_paused is False: self.update()
            self.render()
        pygame.quit()
        