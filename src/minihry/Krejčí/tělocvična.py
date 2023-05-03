import pygame, sys, random
pygame.init()
clock = pygame.time.Clock()

FPS = 60

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width,screen_height))

speed = 5
speed2 = 11

pygame.display.set_caption('Tělocvična')
gameIcon = pygame.image.load('ikonka.follower')
pygame.display.set_icon(gameIcon)
backround = pygame.image.load('hřiště.png')
backroundX = 20
backroundY = 20

ball = pygame.image.load('míč-removebg-preview.png')
ball = pygame.transform.scale(ball,(60,60))
ball_rect = ball.get_rect()
ball_rect.x = 260
ball_rect.y = 570


student = pygame.image.load('student-removebg-preview.png')
student = pygame.transform.scale(student,(105,105))
student_rect = student.get_rect()
student_rect.x = 1030
student_rect.y = 300

záporák = pygame.image.load('záporák-removebg-preview.png')
záporák = pygame.transform.scale(záporák,(130,130))

záporák2 = pygame.image.load('záporák-removebg-preview.png')
záporák2 = pygame.transform.scale(záporák,(130,130))

záporák3 = pygame.image.load('záporák-removebg-preview.png')
záporák3 = pygame.transform.scale(záporák,(130,130))

záporák4 = pygame.image.load('záporák-removebg-preview.png')
záporák4 = pygame.transform.scale(záporák,(130,130))

záporák5 = pygame.image.load('záporák-removebg-preview.png')
záporák5 = pygame.transform.scale(záporák,(130,130))

záporák6 = pygame.image.load('záporák-removebg-preview.png')
záporák6 = pygame.transform.scale(záporák,(130,130))




while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
            
    screen.blit(backround, (0,0))
    screen.blit(ball, ball_rect)
    screen.blit(student, student_rect)
    screen.blit(záporák, (130,510))
    screen.blit(záporák2, (130,290))
    screen.blit(záporák3, (130,72))
    screen.blit(záporák4, (1,160))
    screen.blit(záporák5, (1,386))
    
    klavesa = pygame.key.get_pressed()
    if klavesa[pygame.K_DOWN] and student_rect.y < 555:
        student_rect.y += speed
    
    if klavesa[pygame.K_UP] and student_rect.y > 59:
        student_rect.y -= speed
    
    ball_rect.x += speed2   
    
    clock.tick(FPS)
    pygame.display.update()