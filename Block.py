import pygame 
class Block: 
    def __init__(self, x, y, mass, vi):
        self.x = x 
        self.y = y 
        self.m = mass
        self.vi = vi 
    def show(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.m, self.m))
    def move(self): 
        pass 
