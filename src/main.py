import random
import pygame
pygame.init()

okno = pygame.display.set_mode((800, 600))

radius = 25

c0_x = random.randint(radius, 800 - radius)
c0_y = random.randint(radius, 600 - radius)

c1_x = random.randint(radius, 800 - radius)
c1_y = random.randint(radius, 600 - radius)

c2_x = random.randint(radius, 800 - radius)
c2_y = random.randint(radius, 600 - radius)

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    
    okno.fill((255, 255, 255))
    
    pygame.draw.circle(okno, (0, 0, 0), (c0_x, c0_y), radius)
    pygame.draw.circle(okno, (0, 0, 0), (c1_x, c1_y), radius)
    pygame.draw.circle(okno, (0, 0, 0), (c2_x, c2_y), radius)
    
    pygame.display.update()

