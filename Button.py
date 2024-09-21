import pygame
class Button: 
    def __init__(self, title, pos, size):
        font = pygame.font.Font(None, 36)
        self.is_clicked = False 
        self.text_color = (0,0,0)
        self.rect_color = (255,255,255)
        self.x = pos[0] 
        self.y = pos[1] 
        self.w = size[0]
        self.h = size[1]
        self.text_surface = font.render(title, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
    def listenForInput(self, pos): 
        ## pass pos of the mouse as a tuple (x,y)
        return (self.x < pos[0] < self.x + self.w) and (self.y < pos[1] < self.y + self.h)
    def show(self, screen): 
        pygame.draw.rect(screen, self.rect_color, (self.x, self.y, self.w, self.h))
        screen.blit(self.text_surface, self.text_rect)
    def render_text(self,text):
        font = pygame.font.Font(None, 34)
        self.text_surface = font.render(text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2)) 
    def set_click(self): 
        self.is_clicked = not self.is_clicked
        if self.is_clicked: self.render_text("Play")
        else: self.render_text("Pause",)