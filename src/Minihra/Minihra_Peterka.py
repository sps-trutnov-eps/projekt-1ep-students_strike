import pygame
import sys
pygame.init()

clock = pygame.time.Clock()

FPS = 60
w = 1280
h = 720
rychlost = 17
enemy_rychlost = 2
minule_stisknuto = False 


font = pygame.font.SysFont("arialblack", 80)

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

enemy2_postoj = pygame.image.load("enemy2.png")
enemy2_postoj = pygame.transform.scale(enemy2_postoj, (450,250))
enemy2_postoj_rect = enemy2_postoj.get_rect()





timer_event = pygame.USEREVENT + 1 
pygame.time.set_timer(timer_event, 1000)
time_left = 3

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == timer_event:
            time_left -=1
    
    klavesa = pygame.key.get_pressed() 
    if klavesa[pygame.K_SPACE] and hl_postava_postoj_rect.x <1168 and not minule_stisknuto:
        hl_postava_postoj_rect.x += rychlost
        
    minule_stisknuto =  klavesa[pygame.K_SPACE]
    
    enemy1_postoj_rect.x += enemy_rychlost
    if enemy1_postoj_rect.x > 1009:
        enemy1_postoj_rect.x = 1009 
    
    
        
        
    

    
    

    
        
        
        
        
        
    


   
        

    timer_text = font.render(f"{time_left}", True, (255,255,255))
    
    screen.blit(bg, bg_rect)
    screen.blit(hl_postava_postoj, hl_postava_postoj_rect)
    screen.blit(enemy1_postoj, enemy1_postoj_rect)
    screen.blit(timer_text, (580,5))
    screen.blit(enemy2_postoj, enemy2_postoj_rect)
    
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()

    