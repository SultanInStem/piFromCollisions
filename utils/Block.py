import pygame 
import math
class Block: 
    def __init__(self, pos, size, mass, vi, id):
        self.id = id
        self.m = mass
        self.vi = vi 
        self.default_pos = (pos[0], pos[1] - size[1])
        self.default_size = size
        self.rect = pygame.Rect(self.default_pos, size)
        self.font = pygame.font.Font(None, 36)
        self.label = self.font.render(f"m{id}", True, (255,255,255))
    def show(self, screen):
        x = self.rect.x 
        y = self.rect.y 
        rect_size = self.rect.size
        text_width = self.label.get_size()[0]
        text_height = self.label.get_size()[1]
        text_pos = (x + (rect_size[0] - text_width) // 2, y + (rect_size[1] - text_height) // 2)
        pygame.draw.rect(screen, (0,0,0), self.rect)
        screen.blit(self.label, text_pos)
    def move(self):
        self.rect.x += self.vi
    def reset_pos(self): 
        self.rect.x = self.default_pos[0]
        self.rect.y = self.default_pos[1]
    def is_collided(self,other): 
        pass
    def set_mass(self,mass): 
        self.m = mass 
        self.w = 50 + 50 * (math.log10(mass))
        self.h = 50 + 50 * (math.log10(mass))
    def set_vel(self, vel): 
        self.vi = vel