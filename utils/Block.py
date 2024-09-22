import pygame 
class Block: 
    def __init__(self, pos, size, mass, vi):
        self.x = pos[0] 
        self.y = pos[1] - size[1]
        self.m = mass
        self.vi = vi 
        self.w = size[0] 
        self.h = size[1]
        self.default_pos = (pos[0], pos[1] - size[1])
    def show(self, screen):
        image = pygame.image.load("piCreature.png")
        image = pygame.transform.scale(image, (self.w, self.h))
        screen.blit(image, (self.x, self.y))
    def move(self):
        self.x += self.vi 
    def reset_pos(self): 
        self.x = self.default_pos[0]
        self.y = self.default_pos[1]