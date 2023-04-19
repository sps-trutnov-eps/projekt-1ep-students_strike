import random
import pygame
pygame.init()

class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

okno = pygame.display.set_mode((800, 600))

radius = 25

c_list = []
for i in range(3):
    c_list.append(C(random.randint(radius, 800 - radius), random.randint(radius, 600 - radius)))

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
        pygame.draw.circle(okno, (0, 0, 0), (c_list[i].x, c_list[i].y), radius)
    
    pygame.display.update()

