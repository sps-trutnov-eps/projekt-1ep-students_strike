import pygame
import sys
pygame.init()

clock = pygame.time.Clock()

FPS = 60
w = 1280
h = 720
rychlost = 3
 


screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("minihra")

bg = pygame.image.load("pozadí.png")
bg = pygame.transform.scale(bg,(1280,720))
bg_rect = bg.get_rect()
bg_width = bg.get_width()

hl_postava_postoj = pygame.image.load("běžec_postoj.png")
hl_postava_postoj = pygame.transform.scale(hl_postava_postoj,(130,130))
hl_postava_postoj = pygame.transform.rotate(hl_postava_postoj, 353)
hl_postava_postoj_rect = hl_postava_postoj.get_rect()
hl_postava_postoj_rect.x = -28
hl_postava_postoj_rect.y = 106

enemy1_postoj = pygame.image.load("enemy1_postoj.png")
enemy1_postoj = pygame.transform.scale(enemy1_postoj, (450,250))
enemy1_postoj_rect = enemy1_postoj.get_rect()
enemy1_postoj_rect.x = -190
enemy1_postoj_rect.y = -15

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    klavesa = pygame.key.get_pressed() 
    if klavesa[pygame.K_SPACE]: 
        hl_postava_postoj_rect.x += rychlost
        
        
        
    
        
        
        
        
        
    





    screen.blit(bg, bg_rect)
    screen.blit(hl_postava_postoj, hl_postava_postoj_rect)
    screen.blit(enemy1_postoj, enemy1_postoj_rect)
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()

    