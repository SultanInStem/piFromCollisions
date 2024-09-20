import pygame 
from sys import exit 
pygame.init()
screen = pygame.display.set_mode((700,700))
clock = pygame.time.Clock()

pi_creature = pygame.image.load("piCreature.png")
pi_creature = pygame.transform.scale(pi_creature, (50,50))
while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            pygame.quit()
            exit()
            break
    
    screen.blit(pi_creature, (100,100))


    pygame.display.update()
    screen.fill("white")
    clock.tick(60)


