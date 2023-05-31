import pygame
import sys
pygame.init()

clock = pygame.time.Clock()

FPS = 60
w = 1280
h = 720
rychlost = 11
enemy1_rychlost = 2.5
enemy2_rychlost = 4
enemy3_rychlost = 2.4
enemy4_rychlost = 3
enemy5_rychlost = 3.4                           
enemy6_rychlost = 2.3                
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
enemy2_postoj = pygame.transform.scale(enemy2_postoj, (300,160))
enemy2_postoj_rect = enemy2_postoj.get_rect()
enemy2_postoj_rect.x = -110
enemy2_postoj_rect.y = 195

enemy3 = pygame.image.load("enemy3.png")
enemy3 = pygame.transform.scale(enemy3, (300,160))
enemy3_rect = enemy3.get_rect()
enemy3_rect.x = -110
enemy3_rect.y = 300

enemy4 = pygame.image.load("enemy4.png")
enemy4 = pygame.transform.scale(enemy4, (300,160))
enemy4_rect = enemy4.get_rect()
enemy4_rect.x = -110
enemy4_rect.y = 400

enemy5 = pygame.image.load("enemy5.png")
enemy5 = pygame.transform.scale(enemy5, (300,160))
enemy5_rect = enemy5.get_rect()
enemy5_rect.x = -110
enemy5_rect.y = 500

enemy6 = pygame.image.load("enemy6.png")
enemy6 = pygame.transform.scale(enemy6, (300,160))
enemy6_rect = enemy6.get_rect()
enemy6_rect.x = -110
enemy6_rect.y = 600

prohra = pygame.image.load("Prohra.png")
prohra = pygame.transform.scale(prohra, (1280,720))
prohra_rect = prohra.get_rect()



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
    
    enemy1_postoj_rect.x += enemy1_rychlost
    if enemy1_postoj_rect.x > 1009:
        enemy1_postoj_rect.x = 1009
       
    
    enemy2_postoj_rect.x += enemy2_rychlost
    if enemy2_postoj_rect.x > 1090:
        enemy2_postoj_rect.x = 1090
        
        
    enemy3_rect.x += enemy3_rychlost
    if enemy3_rect.x > 1090:
        enemy3_rect.x = 1090

    enemy4_rect.x += enemy4_rychlost
    if enemy4_rect.x > 1090:
        enemy4_rect.x = 1090
        
    
    enemy5_rect.x += enemy5_rychlost
    if enemy5_rect.x > 1090:
        enemy5_rect.x = 1090
        
    enemy6_rect.x += enemy6_rychlost
    if enemy6_rect.x > 1090:
        enemy6_rect.x = 1090
        
    
        
    
   
        

    timer_text = font.render(f"{time_left}", True, (255,255,255))
    hitbox_c = pygame.draw.rect(screen, (0,0,0),(w -50, 0, w, h))
    screen.blit(bg, bg_rect)
    screen.blit(hl_postava_postoj, hl_postava_postoj_rect)
    screen.blit(enemy1_postoj, enemy1_postoj_rect)
    screen.blit(timer_text, (580,5))
    screen.blit(enemy2_postoj, enemy2_postoj_rect)
    screen.blit(enemy3, enemy3_rect)
    screen.blit(enemy4, enemy4_rect)
    screen.blit(enemy5, enemy5_rect)
    screen.blit(enemy6, enemy6_rect)
    
    kolize1 = pygame.Rect.colliderect(enemy1_postoj_rect, hitbox_c)
    kolize2 = pygame.Rect.colliderect(enemy2_postoj_rect, hitbox_c)
    kolize3 = pygame.Rect.colliderect(enemy3_rect, hitbox_c)
    kolize4 = pygame.Rect.colliderect(enemy4_rect, hitbox_c)
    kolize5 = pygame.Rect.colliderect(enemy5_rect, hitbox_c)
    kolize6 = pygame.Rect.colliderect(enemy6_rect, hitbox_c)
    
    if kolize1:
        screen.blit(prohra, (0, 0))
    
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()

    