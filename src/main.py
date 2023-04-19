import random
import pygame
pygame.init()

okno = pygame.display.set_mode((800, 600))

radius = 25

x_list = []
y_list = []
for i in range(3):
    x_list.append(random.randint(radius, 800 - radius))
    y_list.append(random.randint(radius, 600 - radius))

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.key.get_pressed()[pygame.K_ESCAPE]:
            pygame.quit()
            exit()
    
    okno.fill((255, 255, 255))
    
    for i in range(3):
        pygame.draw.circle(okno, (0, 0, 0), (x_list[i], y_list[i]), radius)
    
    pygame.display.update()

