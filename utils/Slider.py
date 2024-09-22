import math
import pygame
from utils.Block import Block 
class Slider: 
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min_value: int, max_value: int, role, block_id: int):
        self.size = size 
        self.pos = pos
        self.role = role 
        self.block_id = block_id
        self.initial_val = initial_val

        self.slider_left_pos = self.pos[0] - (self.size[0] // 2)
        self.slider_right_pos = self.pos[0] + (self.size[0] // 2)
        self.slider_top_pos = self.pos[1] - (self.size[1] // 2)
        self.slider_bottom_pos = self.pos[1] + (self.size[1] // 2)

        self.min = min_value 
        self.max = max_value
        self.initial_value = (self.slider_right_pos - self.slider_left_pos) * initial_val # <- percentage 

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos + self.initial_value - 5, self.slider_top_pos, 10, self.size[1])

        self.font = pygame.font.Font(None, 25) 

    def render(self, screen): 
        pygame.draw.rect(screen, "black", self.container_rect)
        pygame.draw.rect(screen, "blue", self.button_rect)

        val = self.get_value()
        value_text = self.font.render(f"{int(val)}", True, (0,0,0))
        role_text = self.font.render(f"{self.role} {self.block_id}",True,(0,0,0))

        screen.blit(value_text, (self.slider_right_pos + 10, self.slider_top_pos + value_text.get_size()[1] // 2))
        screen.blit(role_text, (self.slider_left_pos - 100, self.slider_top_pos + role_text.get_size()[1] // 2))
    def move_slider(self, pos): 
        self.button_rect.centerx = pos[0]
        value = self.get_value()
        # if self.role == "mass": 
            # self.block.set_mass(value)
        # else:
            # self.block.set_vel(value) 
    def reset(self): 
        self.initial_value = (self.slider_right_pos - self.slider_left_pos) * self.initial_val
        self.button_rect.centerx = self.slider_left_pos + self.initial_value - 5
        # value = self.get_value()
        # if self.role == "mass": 
            # self.block.set_mass(value)
        # else: self.block.set_vel(round(value))
    




    def get_value(self):
        value_range = self.slider_right_pos - self.slider_left_pos 
        button_value = self.button_rect.centerx - self.slider_left_pos 
        value = (button_value / value_range) * (self.max - self.min) + self.min
        if self.role == "mass": 
            power_of_10 = math.pow(10, round(value))
            return power_of_10
        return value 


