import pygame
import sys
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1820, 980))
FPS = 60
background = pygame.image.load('třída.png')
background = pygame.transform.scale(background, (1820, 980))

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
        
    screen.blit(background,(0,0))
    pygame.display.update()
