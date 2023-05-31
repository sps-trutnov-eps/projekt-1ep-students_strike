import pygame
import sys 
pygame.init()

Background = pygame.image.load('pixil-frame-0.png')

Clean_board_colour = (0, 102, 0) 





#Screen
screen = pygame.display.set_mode((1280,720))

pygame.draw.rect(screen, (128, 64, 0), (390, 125, 500, 10))
pygame.draw.rect(screen, (128, 64, 0), (390, 450, 500, 10))
pygame.draw.rect(screen, (128, 64, 0), (390, 125, 10, 325))
pygame.draw.rect(screen, (128, 64, 0), (890, 125, 10, 335))
pygame.draw.rect(screen, (98, 149, 101), (400, 135, 490, 315))





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
    #background

    
    
    
    
  
    
    
    #cleaning
    if event.type == pygame.MOUSEBUTTONDOWN:
        mpos = pygame.mouse.get_pos()
        Clean_circle_xpos = mpos[0] - 40
        Clean_circle_ypos = mpos[1] - 40
        if 440 < mpos[0] < 850 and 155 < mpos[1] < 450:
            pygame.draw.ellipse(screen, Clean_board_colour, (Clean_circle_xpos, Clean_circle_ypos, 80, 80)) 
           
    
    
    
    
    
    
    
    pygame.display.update() 


