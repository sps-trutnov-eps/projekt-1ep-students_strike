import pygame
import sys 
import random


pygame.init()
FPS = 60
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
     
   
    # pohyb hráče1 
    key = pygame.key.get_pressed() 
    if key[pygame.K_LEFT]: 
        hrac1.move(-2, 0) 
    if key[pygame.K_RIGHT]: 
        hrac1.move(2, 0) 
    if key[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    
    okno.fill(cerna_barva)

   
    

    pygame.draw.rect(okno,(modra_barva) , hrac1.rect)
    
    font1 = pygame.font.Font(None, 30)
    znamka1 = font1.render("1", True, ((zelena_barva)))
    okno.blit(znamka1, [100, 100])
    
    font2 = pygame.font.Font(None, 30)
    znamka2 = font2.render("2", True, ((zelena_barva)))
    okno.blit(znamka2, [200, 100])
    
    font3 = pygame.font.Font(None, 30)
    znamka3 = font3.render("3", True, ((zelena_barva)))
    okno.blit(znamka3, [300, 100])
    
    font4 = pygame.font.Font(None, 30)
    znamka4 = font4.render("4", True, ((zelena_barva)))
    okno.blit(znamka4, [400,100])
    
    font5 = pygame.font.Font(None, 30)
    znamka5 = font5.render("5", True, ((zelena_barva)))
    okno.blit(znamka5, [500, 100])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    

    
    pygame.display.flip()
    pygame.display.update()       
    
     
clock.tick(FPS) 

pygame.quit()



