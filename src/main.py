import pygame
pygame.init()

okno = pygame.display.set_mode((800, 600))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    
    okno.fill((255, 255, 255))
    pygame.display.update()

