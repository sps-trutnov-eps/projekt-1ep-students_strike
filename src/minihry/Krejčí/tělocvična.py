import pygame, sys, random, time, random
pygame.init()
clock = pygame.time.Clock()

FPS = 60
pohyb = False
pohyb2 = False
pohyb3 = False
pohyb4 = False
pohyb5 = False


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
ball_rect.x = 250
ball_rect.y = 570

ball2 = pygame.transform.scale(ball,(60,60))
ball2_rect = ball.get_rect()
ball2_rect.x = 250
ball2_rect.y = 135

ball3 = pygame.transform.scale(ball,(60,60))
ball3_rect = ball.get_rect()
ball3_rect.x = 250
ball3_rect.y = 355

ball4 = pygame.transform.scale(ball,(60,60))
ball4_rect = ball.get_rect()
ball4_rect.x = 120
ball4_rect.y = 445

ball5 = pygame.transform.scale(ball,(60,60))
ball5_rect = ball.get_rect()
ball5_rect.x = 120
ball5_rect.y = 225







student = pygame.image.load('student-removebg-preview-removebg-preview-removebg-preview.png')
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

font = pygame.font.Font(None, 50)
start_time = time.time()

    
    
    
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
    screen.blit(ball2, ball2_rect)
    screen.blit(ball3, ball3_rect)
    screen.blit(ball4, ball4_rect)
    screen.blit(ball5, ball5_rect)
    
    
    klavesa = pygame.key.get_pressed()
    if klavesa[pygame.K_DOWN] and student_rect.y < 555:
        student_rect.y += speed
    
    if klavesa[pygame.K_UP] and student_rect.y > 60:
        student_rect.y -= speed
    
    
    elapsed_time = time.time() - start_time
    time_text = font.render("Time: " + str(int(elapsed_time)), True, (0, 0, 0))
    screen.blit(time_text, (10, 10))
      
    if random.random()<0.01:
        pohyb = True
         
    if random.random()<0.01:
        pohyb2 = True    
         
    if random.random()<0.01:
        pohyb3 = True
        
    if random.random()<0.01:
        pohyb4 = True      
        
    if random.random()<0.01:
        pohyb5 = True      
    
                
    if pohyb:
        ball_rect.x += 11
         
    if pohyb2:
        ball2_rect.x += 11
        
    if pohyb3:
        ball3_rect.x += 11
        
    if pohyb4:
        ball4_rect.x += 11
    
    if pohyb5:
        ball5_rect.x += 11
    
    if ball_rect.x > 1280:
        ball_rect.x = 250
        pohyb = False
        
    if ball2_rect.x > 1280:
        ball2_rect.x = 250
        pohyb = False
    
    if ball3_rect.x > 1280:
        ball3_rect.x = 250
        pohyb = False
    
    if ball4_rect.x > 1280:
        ball4_rect.x = 120
        pohyb = False
    
    if ball5_rect.x > 1280:
        ball5_rect.x = 120
        pohyb = False
    
    
    
    
    
    clock.tick(FPS)
    pygame.display.update()