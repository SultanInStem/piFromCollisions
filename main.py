import pygame 
from sys import exit 

pygame.init()
screen_width = 800
screen_height = 600 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PI from collisions")
running = True
white = (255,255,255)
clock = pygame.time.Clock()

while running: 
    screen.fill(white)
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit()
            running = False
            break 
    pygame.display.update()
    clock.tick(60)

pygame.quit()