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
        self.blocks = [
            Block((50,size[1] - ground_height), (50,50), 10, 0,1),
            Block((300,size[1] -  ground_height), (100,100), 100, -1,2)
        ]
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
            Slider((400,100), (100,25), 0, 0, 3,"mass", 1), 
            Slider((400,200), (100,25), 0.5, -5,5,"velocity",1), 
            Slider((650,100), (100,25), 0.7, 0, 3,"mass", 2), 
            Slider((650,200), (100,25), 0.5, -5,5,"velocity",2), 
        ]
    def reset(self): 
        for slider in self.sliders: slider.reset() 
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
        for block in self.blocks: block.move()
    def update_block(self, block_id,role,value):
        if block_id > len(self.blocks): return
        match(role): 
            case "velocity":
                self.blocks[block_id - 1].set_vel(value)
            case "mass": 
                self.blocks[block_id - 1].set_mass(value)
            case _: 
                pass

    def render(self): 
        mouse_pos = pygame.mouse.get_pos()
        mouse = pygame.mouse.get_pressed()
        for button in self.buttons: button.show(self.screen)
        for block in self.blocks: block.show(self.screen)
        for slider in self.sliders: 
            if slider.container_rect.collidepoint(mouse_pos) and mouse[0]: 
                slider.move_slider(mouse_pos)
                self.update_block(slider.block_id, slider.role, slider.get_value())
            slider.render(self.screen)
        text_surface = self.font.render(f"Number of collisions: {self.coll_counter}", True, (0,0,0))
        self.screen.blit(text_surface, (600,40))
        self.ground.show(self.screen)
        pygame.display.update()
        self.clock.tick(self.fps)
    def run(self): 
        while self.running: 
            self.screen.fill(colors['light_blue'])
            self.handleInputs()
            if self.is_paused is False: self.update()
            self.render()
        pygame.quit()
        