import pygame, sys, random
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))


pygame.display.set_caption('Tělocvična')
gameIcon = pygame.image.load('ikonka.follower')
pygame.display.set_icon(gameIcon)
backround = pygame.image.load('hřiště.png')
backroundX = 20
backroundY = 20


screen.blit(backround, (backroundX, backroundY))





while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
screen.blit(backround, (0,0))
pygame.display.update()