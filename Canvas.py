import pygame
from sys import exit
from utils.Button import Button
from utils.Ground import Ground
from utils.Block import Block 
from utils.Slider import Slider
from utils.globals import colors

class Canvas: 
    def __init__(self, size, title, fps): 
        pygame.init()
        font = pygame.font.Font(None, 36)
        self.coll_counter = 0
        self.font = font
        self.is_paused = False 
        self.size = size 
        ground_height = 200 
        self.small_block = Block((50,size[1] - ground_height), (100,100), 10, 0,1)
        self.big_block = Block((200,size[1] -  ground_height), (200,200), 100, -1,2)
        self.running = True

        ### BUTTONS 
        self.buttons = [
            Button("Pause", (-50 + size[0] // 2, 10), (100,50), "PLAY"), 
            Button("Reset", (-250 + size[0] // 2, 10), (100,50), "RESET")
        ]

        self.fps = fps 
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.ground = Ground((0,size[1] - ground_height), (size[0], ground_height), colors['light_green'])
        self.sliders = [
            Slider((400,100), (100,25), 0, 0, 3,"mass", self.small_block), 
            Slider((400,200), (100,25), 0, 1,10,"velocity",self.small_block), 
            Slider((650,100), (100,25), 0, 0, 3,"mass",self.big_block), 
            Slider((650,200), (100,25), 0.1, 1,10,"velocity",self.big_block), 
        ]
    def reset(self): 
        self.small_block.reset_pos()
        self.big_block.reset_pos()
        pass
    def handle_button_click(self, button_clicked): 
        match (button_clicked.action):
            case "PLAY":
                button_clicked.set_click()
                self.is_paused = not self.is_paused 
                pass 
            case "RESET": 
                self.reset()
    def handleInputs(self): 
        mousePos = pygame.mouse.get_pos()
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                self.running = False 
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN: 
                for button in self.buttons: 
                    if button.listenForInput(mousePos): self.handle_button_click(button)
    def update(self): 
        self.big_block.move()
        self.small_block.move()

    def render(self): 
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for button in self.buttons: button.show(self.screen)
        self.ground.show(self.screen)
        self.small_block.show(self.screen)
        self.big_block.show(self.screen)

        for slider in self.sliders: 
            if slider.container_rect.collidepoint(mouse_pos) and mouse[0]: 
                slider.move_slider(mouse_pos)
            slider.render(self.screen)
        text_surface = self.font.render(f"Number of collisions: {self.coll_counter}", True, (0,0,0))
        self.screen.blit(text_surface, (600,40))
        pygame.display.update()
        self.clock.tick(self.fps)
    def run(self): 
        while self.running: 
            self.screen.fill(colors['light_blue'])
            self.handleInputs()
            if self.is_paused is False: self.update()
            self.render()
        pygame.quit()
        