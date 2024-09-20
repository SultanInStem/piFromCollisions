import pygame
class Button: 
    def __init__(self,x,y,width,height,title):
        self.x = x 
        self.y = y 
        self.w = width 
        self.h = height
        self.title = title
    def listenForInput(self, pos): ## pass pos as a tuple (x,y)
        pass