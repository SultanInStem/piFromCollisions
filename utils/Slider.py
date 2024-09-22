import pygame 
class Slider: 
    def __init__(self, pos: tuple, size: tuple, initial_val: float, min_value: int, max_value: int):
        self.size = size 
        self.pos = pos

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
        pygame.draw.rect(screen, "darkgray", self.container_rect)
        pygame.draw.rect(screen, "pink", self.button_rect)

        val = self.get_value()
        value_text = self.font.render(f"{int(val)}", True, (0,0,0))
        screen.blit(value_text, (self.slider_right_pos + 10, self.slider_top_pos))

    def move_slider(self, pos): 
        self.button_rect.centerx = pos[0]

    def get_value(self):
        value_range = self.slider_right_pos - self.slider_left_pos 
        button_value = self.button_rect.centerx - self.slider_left_pos 
        value = (button_value / value_range) * (self.max - self.min) + self.min
        return value 


