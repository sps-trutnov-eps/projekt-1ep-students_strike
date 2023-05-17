import pygame
import sys
pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
black = (0,0,0)
FPS = 60
# images
background = pygame.image.load('třída.png')
background = pygame.transform.scale(background, (1280, 720))
staple = pygame.image.load('staple.png')
staple = pygame.transform.scale(staple, (60, 60))
compasses = pygame.image.load('compasses.png')
compasses = pygame.transform.scale(compasses, (60, 60))
font = pygame.font.SysFont('Consolas', 50)
table1 = pygame.Rect(30, 450, 160, 80)
table_skin = pygame.image.load('table.png')
table_skin = pygame.transform.scale(table_skin, (160, 80))
game = True
while game:
    clock.tick(FPS)
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(background,(0,0))
    pygame.draw.rect(screen, black, table1)
    screen.blit(compasses,(1150,660))
    screen.blit(staple,(1215,660))
    
    mx = pygame.mouse.get_pos()[0]
    my = pygame.mouse.get_pos()[1]
    print(mx, my)
    mouse = pygame.mouse.get_pressed()
    if mouse[0]:
        if 
            screen.blit(table_skin, (30, 450))
        
        
    
    
        
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    #if collide mouse idk s staple:
        #screen.blit(staple,(1150,660))
    #if collide mouse idk s staple:
        #screen.blit(compasses,(1150,660))
        
        
    
    pygame.display.update()
