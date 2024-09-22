import pygame 
import math
class Block: 
    def __init__(self, pos, size, mass, vi, id):
        self.id = id
        self.m = mass
        self.vi = vi 
        self.w = size[0] 
        self.h = size[1]
        self.default_pos = (pos[0], pos[1] - size[1])
        self.default_size = size
        self.rect = pygame.Rect(self.default_pos, size)
    def show(self, screen):
        pygame.draw.rect(screen, (0,0,0), self.rect)
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