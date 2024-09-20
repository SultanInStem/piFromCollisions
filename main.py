import pygame 
from sys import exit 
pygame.init()
screen_width = 1000
screen_height = 800 
groung_height = 200 
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PI from collisions")
running = True
white = (255,255,255)
clock = pygame.time.Clock()
ground = pygame.Surface((screen_width, screen_height - groung_height))
ground.fill((50,150,50))
def handleInputs(): 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            exit()
            running = False
            break
def update(): 
    pass
def render(): 
    screen.blit(ground, (0,screen_height - groung_height))
    pygame.display.update()
    pass 

def main(): 
    while running: 
        screen.fill(white)
        handleInputs()
        update()
        render()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__": 
    main()