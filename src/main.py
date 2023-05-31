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
# im monkey
table1 = pygame.Rect(30, 450, 160, 80)
table2 = pygame.Rect(210, 450, 160, 80)
table3 = pygame.Rect(390, 450, 160, 80)
#table4 = pygame.Rect(30, 450, 160, 80)
#table5 = pygame.Rect(30, 450, 160, 80)
#table6 = pygame.Rect(30, 450, 160, 80)
#table7 = pygame.Rect(30, 450, 160, 80)
#table8 = pygame.Rect(30, 450, 160, 80)
#table9 = pygame.Rect(30, 450, 160, 80)
#table10 = pygame.Rect(30, 450, 160, 80)
#table11 = pygame.Rect(30, 450, 160, 80)
#table12 = pygame.Rect(30, 450, 160, 80)
table_skin_closed = pygame.image.load('tableclosed.png')
table_skin_closed = pygame.transform.scale(table_skin_closed, (160, 80))
table_skin_open = pygame.image.load('table.png')
table_skin_open = pygame.transform.scale(table_skin_open, (160, 110))
game = True
while game:
    clock.tick(FPS)
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
     
    screen.blit(background,(0,0))
    screen.blit(compasses,(1150,660))
    screen.blit(table_skin_closed, (30, 450))
    screen.blit(table_skin_closed, (210, 450))
    screen.blit(table_skin_closed, (390, 450))
    #tables = [table1,table2,table3,table4,table5,table6,table7,table8,table9,rable10,table11,table12]
    #mouse = pygame.mouse.get_pressed()
    #if mouse[0]:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            mx = pygame.mouse.get_pos()[0]
            my = pygame.mouse.get_pos()[1]
            print(mx, my)
            text = 'you found a staple'
            if tables.collidepoint(mx,my):
                screen.blit(staple,(1215,660))
                screen.blit(table_skin_open, (30, 450))
                screen.blit(font.render(text, True, (0, 0, 0)), (400, 360))
                pygame.display.update()
                pygame.time.wait(2000)
                
            
            
                
             
                
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.quit()
        sys.exit()
    
    #if collide mouse idk s staple:
        #screen.blit(staple,(1150,660))
    #if collide mouse idk s staple:
        #screen.blit(compasses,(1150,660))
        
        
    
    pygame.display.update()
