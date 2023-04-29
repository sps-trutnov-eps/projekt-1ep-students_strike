import pygame
import sys 
import random


pygame.init()

cerna_barva = (0, 0, 0)
bila_barva = (255, 255, 255)
cervena_barva = (255, 0, 0)
modra_barva = (0, 0, 255)
zelena_barva = (0, 255, 0)


             
    

okno = pygame.display.set_mode((800, 600))
pygame.display.set_caption("minihra")


done = False
clock = pygame.time.Clock()

while not done:
    
    clock.tick(60)

    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            done = True  

    
    okno.fill(modra_barva)

   
    

    pygame.draw.rect(okno, (cervena_barva), [350, 580, 50, 20])

   
   

    
    pygame.display.flip()


pygame.quit()

