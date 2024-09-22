import pygame 
class Block: 
    def __init__(self, pos, size, mass, vi):
        self.x = pos[0] 
        self.y = pos[1] - size[1]
        self.m = mass
        self.vi = vi 
        self.w = size[0] 
        self.h = size[1]
    def show(self, screen):
        image = pygame.image.load("piCreature.png")
        image = pygame.transform.scale(image, (self.w, self.h))
        screen.blit(image, (self.x, self.y))
    def move(self):
        self.x += self.vi 
    def set_pos(self, pos: tuple): 
        self.x = pos[0]
        self.y = pos[1]