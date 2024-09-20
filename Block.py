import pygame 
class Block: 
    def __init__(self, x, y, mass, vi, width, height):
        self.x = x 
        self.y = y - height 
        self.m = mass
        self.vi = vi 
        self.w = width 
        self.h = height
    def show(self, screen):
        image = pygame.image.load("piCreature.png")
        image = pygame.transform.scale(image, (self.w, self.h))
        screen.blit(image, (self.x, self.y))
    def move(self): 
        pass 
