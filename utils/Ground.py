import pygame
class Ground: 
    def __init__(self, pos, size,color):
        self.size = size 
        self.pos = pos 
        self.color = color
        self.ground_surface = pygame.Surface(size)
        self.ground_surface.fill(color)   
    def show(self, screen): 
        screen.blit(self.ground_surface, self.pos)
