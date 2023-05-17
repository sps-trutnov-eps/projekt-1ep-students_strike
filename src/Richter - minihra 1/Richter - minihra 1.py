import pygame
import sys 
pygame.init()

Background = pygame.image.load('pixil-frame-0.png')







#Screen
screen = pygame.display.set_mode((1280,720))


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
    screen.fill((255, 255, 255))
    
    
    
    
    
    #Board
    pygame.draw.rect(screen, (128, 64, 0), (390, 125, 500, 10))
    pygame.draw.rect(screen, (128, 64, 0), (390, 450, 500, 10))
    pygame.draw.rect(screen, (128, 64, 0), (390, 125, 10, 325))
    pygame.draw.rect(screen, (128, 64, 0), (890, 125, 10, 335))
    
    
    
    
    
    
    
    
    
    pygame.display.update() 


