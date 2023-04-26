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
ball = pygame.image.load('míč-removebg-preview.png')
ballX = 1600
ballY = 20
ball = pygame.transform.scale(ball,(60,60))
student = pygame.image.load('student-removebg-preview.png')
studentX = 20
studentY = 20
#student = pygame.transform.scale(student(70,70))


screen.blit(backround, (backroundX, backroundY))
screen.blit(ball, (ballX, ballY))
screen.blit(student, (studentX, studentY)) 

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    screen.blit(backround, (0,0))
    screen.blit(ball, (100,200))
    screen.blit(student, (1000,300))
    
    pygame.display.update()