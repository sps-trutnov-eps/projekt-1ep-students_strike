import pygame
import sys
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1820, 980))

FPS = 60
font = pygame.font.SysFont('Consolas', 50)
game = True
while game:
    clock.tick(FPS)
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
       
    screen.fill((255, 255, 255,))   
    pygame.display.update()