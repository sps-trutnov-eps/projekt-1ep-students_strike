import pygame, random, sys, math, time
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
follower_x = random.randint(50 , 1200) 
follower_y = random.randint(50, 600)
rychlost = 1
ucitel_x = 200
ucitel_y = 690

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    distance = ((follower_x - ucitel_x) ** 2 + (follower_y - ucitel_y) ** 2) ** 0.5
    if distance > 60:
        if ucitel_x > follower_x:
            ucitel_x -= rychlost
        elif ucitel_x < follower_x:
            ucitel_x += rychlost
        if ucitel_y > follower_y:
            ucitel_y -= rychlost
        elif ucitel_y < follower_y:
            ucitel_y += rychlost
    if distance <= 60:
        if ucitel_x < 200 - 30:
            ucitel_x += rychlost
        if ucitel_x > 200 - 30:
            ucitel_x -= rychlost
        if ucitel_y < 690 - 30:
            ucitel_y += rychlost
        if ucitel_y < 690 - 30:
            ucitel_y += rychlost
        if follower_x < 200 - 30:
            follower_x += rychlost
        if follower_x > 200 - 30:
            follower_x -= rychlost
        if follower_y < 690 - 30:
            follower_y += rychlost
        if follower_y < 690 - 30:
            follower_y += rychlost
            
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), (follower_x, follower_y), 30)
    pygame.draw.circle(screen, (255,0,0), (ucitel_x, ucitel_y), 30)
    pygame.display.update()
    clock.tick(120)