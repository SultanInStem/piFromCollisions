import pygame
class Button: 
    def __init__(self, title, pos, size):
        font = pygame.font.Font(None, 36)
        self.x = pos[0] 
        self.y = pos[1] 
        self.w = size[0]
        self.h = size[1]
        self.title = title
        self.text_surface = font.render(title, True, (0,0,0))
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
    def listenForInput(self, pos): 
        ## pass pos of the mouse as a tuple (x,y)
        return (self.x < pos[0] < self.x + self.w) and (self.y < pos[1] < self.y + self.h)
    def show(self, screen): 
        pygame.draw.rect(screen, (255,255,255), (self.x, self.y, self.w, self.h))
        screen.blit(self.text_surface, self.text_rect)