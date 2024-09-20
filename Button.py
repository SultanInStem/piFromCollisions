import pygame
class Button: 
    font = pygame.font.Font(None, 24)
    def __init__(self, title, pos, size):
        self.x = pos[0] 
        self.y = pos[1] 
        self.w = size[0]
        self.h = size[1]
        self.title = title
    def listenForInput(self, pos): 
        ## pass pos of the mouse as a tuple (x,y)
        return (self.x < pos[0] < self.x + self.w) and (self.y < pos[1] < self.y + self.h)
    def show(self, screen): 
        pass