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
        self.fps = fps 
        self.screen = pygame.display.set_mode(size)
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)
        self.coll_counter = 0
        self.font = font
        self.is_paused = True
        self.running = True
        self.size = size 
        ground_height = 200 
        self.blocks = [
            Block((50,size[1] - ground_height), (50,50), 1, 0,1),
            Block((300,size[1] -  ground_height), (50,50), 1, 0,2)
        ]
        self.sliders = [
            Slider((500,100), (100,25), 0, 0, 3,"mass", 1), 
            Slider((500,200), (100,25), 0.5, -5,5,"velocity",1), 
            Slider((800,100), (100,25), 0, 0, 3,"mass", 2), 
            Slider((800,200), (100,25), 0.5, -5,5,"velocity",2), 
        ]

        ### BUTTONS 
        self.buttons = [
            Button("PLAY", (-50 + size[0] // 2, 10), (100,50), "PAUSE"), 
            Button("RESET", (-250 + size[0] // 2, 10), (100,50), None)
        ]

        self.ground = Ground((0,size[1] - ground_height), (size[0], ground_height), colors['light_green'])
    def reset(self): 
        self.coll_counter = 0
        self.is_paused = True
        for button in self.buttons: button.is_on = self.is_paused
        for slider in self.sliders: slider.reset() 
        for block in self.blocks: block.reset()
    def handle_button_click(self, button_clicked): 
        match (button_clicked.title):
            case "PLAY":
                self.is_paused = not self.is_paused
                button_clicked.is_on = self.is_paused
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
    def resolve_collision(self, block_1, block_2): 
        self.coll_counter += 1
        num = (block_1.m - block_2.m) * block_1.vi + 2 * block_2.m * block_2.vi
        denom = block_1.m + block_2.m
        v1 = num / denom 
        num = 2 * block_1.m * block_1.vi + (block_2.m - block_1.m) * block_2.vi
        v2 = num / denom 
        block_1.set_vel(v1)
        block_2.set_vel(v2)
        
    def update(self): 
        if self.is_paused: return

        for block in self.blocks: 
            block.move()
            # checks if a block collided with the wall and reverse the velocity
            if block.rect.x <= 0: 
                self.coll_counter += 1
                block.set_vel(-1 * block.vi) 
        # check collisions between the blocks
        for i in range(0, len(self.blocks) - 1): 
            for j in range(i + 1, len(self.blocks)): 
                if self.blocks[i].is_collided(self.blocks[j]): 
                    self.resolve_collision(self.blocks[i], self.blocks[j])
                    break
        
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
            if slider.container_rect.collidepoint(mouse_pos) and mouse[0] and self.is_paused is True: 
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
        