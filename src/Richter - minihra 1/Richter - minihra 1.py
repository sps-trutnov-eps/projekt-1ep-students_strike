import pygame
import sys
import random
pygame.init()



Clean_board_colour = (0, 102, 0) 
background = pygame.image.load('Pozadí.png')
Lukáš_Hajnyš = pygame.image.load('Lukáš-Hajnyš.png')
Salát = pygame.image.load('Salát.png')
Math = pygame.image.load('1+1=3.png')
Čára = pygame.image.load('čára.png')
Ich_bin = pygame.image.load('Ich-bin-ein-gamer.png')
Mám_rád_dějepis = pygame.image.load('Mám-rád-dějepis.png')
Random_čáry = pygame.image.load('Random-čáry.png') 

#True / false
Lukáš_Hajnyš_show = False
Salát_show = False
Math_show = False
Čára_show = False
Ich_bin_show = False
Mám_rád_dějepis_show = False
Random_čáry_show = False 


#Screen
screen = pygame.display.set_mode((1280,720))
background = screen.blit(background, (0, 0)) 
pygame.draw.rect(screen, (128, 64, 0), (390, 125, 500, 10))
pygame.draw.rect(screen, (128, 64, 0), (390, 450, 500, 10))
pygame.draw.rect(screen, (128, 64, 0), (390, 125, 10, 325))
pygame.draw.rect(screen, (128, 64, 0), (890, 125, 10, 335))
pygame.draw.rect(screen, (98, 149, 101), (400, 135, 490, 315))

Drawing_on_board = 1
if Drawing_on_board == 1:
        Lukáš_Hajnyš_show = True 
        Salát_show = True
        Math_show = True
        Čára_show = True
        Ich_bin_show = True
        Mám_rád_dějepis_show = True
        Random_čáry_show = T
        

if Salát_show == True:
    screen.blit(Salát, (365, 178))
if Mám_rád_dějepis_show == True:
    screen.blit(Mám_rád_dějepis,(411, 283))
if Random_čáry_show == True:
    screen.blit(Random_čáry, (557, 150)) 
    
    





#window loop
while True:
    #Turning off the app
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           #framework shutdown
            pygame.quit()
            #app shutdown
            sys.exit()
    #alt+f4 shutdown
    Keyboard = pygame.key.get_pressed()
    F4 = Keyboard[pygame.K_F4]
    if F4 == True:
        pygame.QUIT
    
  
    if Salát_show == True:
        screen.blit(Salát, (365, 178))
    if Mám_rád_dějepis_show == True:
        screen.blit(Mám_rád_dějepis,(411, 283))
    if Random_čáry_show == True:
        screen.blit(Random_čáry, (557, 150)) 
    
     
    
    #cleaning
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        Clean_circle_xpos = mpos[0] - 35
        Clean_circle_ypos = mpos[1] - 45
        if 440 < mpos[0] < 850 and 175 < mpos[1] < 430:
            pygame.draw.ellipse(screen, Clean_board_colour, (Clean_circle_xpos, Clean_circle_ypos, 80, 80)) 
           
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        if 365 < mpos[0] < 552 and 178 < mpos[1] < 241:
            if Salát_show == True:
                Salát_show = False 
    
    
    
    
    
    pygame.display.update() 


