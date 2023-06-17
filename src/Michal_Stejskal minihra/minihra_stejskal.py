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

PLOSINA_šířka = 100
PLOSINA_výška = 20
výška = 600
šířka = 800 

okno = pygame.display.set_mode((800, 600))
pygame.display.set_caption("minihra")

class PLOSINA(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLOSINA_šířka, PLOSINA_výška))
        self.image.fill(modra_barva)
        self.rect = self.image.get_rect()
        self.rect.x = (šířka - PLOSINA_šířka) // 2
        self.rect.y = výška - PLOSINA_výška

    def update(self):
        # Pohyb plošinky s myší
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        # Omezení pohybu plošinky na obrazovce
        if self.rect.x > WIDTH - PADDLE_WIDTH:
            self.rect.x = WIDTH - PADDLE_WIDTH

clock = pygame.time.Clock()
PLOSINA = PLOSINA()

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

   
    

    pygame.draw.rect(okno,(modra_barva) , PLOSINA.rect)
    
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



