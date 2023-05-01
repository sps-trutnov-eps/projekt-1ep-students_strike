import pygame
import sys 
import random


pygame.init()

cerna_barva = (0, 0, 0)
bila_barva = (255, 255, 255)
cervena_barva = (255, 0, 0)
modra_barva = (0, 0, 255)
zelena_barva = (0, 255, 0)

class hrac1(object): 
     
    def __init__(self): 
        self.rect = pygame.Rect(400, 580, 50, 20) 
     
    def move(self, dx, dy): 
  
        if dx != 0: 
            self.move_single_axis(dx, 0) 
        if dy != 0: 
            self.move_single_axis(0, dy) 
             
    def draw(self, surface): 
        pygame.draw.rect(surface, self.color, self.rect) 
             
       
    def move_single_axis(self, dx, dy): 
         
        # pohyb 
        self.rect.x += dx 
        self.rect.y += dy 

okno = pygame.display.set_mode((800, 600))
pygame.display.set_caption("minihra")



clock = pygame.time.Clock()
hrac1 = hrac1()

running = True 
while running: 
     
    clock.tick(60)    
     
   
    # pohyb hráče2 
    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        hrac1.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        hrac1.move(2, 0) 
     

    
    okno.fill(modra_barva)

   
    

    pygame.draw.rect(okno,(cervena_barva) , hrac1.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    
    pygame.display.flip()
    pygame.display.update()       
    
     
clock.tick(60) 

pygame.quit()



