import pygame 
import math
class Block: 
    def __init__(self, pos, size, mass, vi, id):
        self.id = id
        self.x = pos[0] 
        self.y = pos[1]
        self.m = mass
        self.vi = vi 
        self.w = size[0] 
        self.h = size[1]
        self.default_pos = (pos[0], pos[1] - size[1])
    def show(self, screen):
        image = pygame.image.load("piCreature.png")
        image = pygame.transform.scale(image, (self.w, self.h))
        screen.blit(image, (self.x, self.y - self.h))
    def move(self):
        self.x += self.vi 
    def reset_pos(self): 
        self.x = self.default_pos[0]
        self.y = self.default_pos[1]
    def set_mass(self,mass): 
        self.m = mass 
        self.w = 50 + 50 * (math.log10(mass))
        self.h = 50 + 50 * (math.log10(mass))
        # self.y = self.y - self.h
    def set_vel(self, vel): 
        self.vi = vel