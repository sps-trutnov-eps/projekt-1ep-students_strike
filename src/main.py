import pygame, random, sys, math, time
pygame.init()
# ---VARIABLES---
screen = pygame.display.set_mode((1280, 720))
FPS = 120
# ---------------
clock = pygame.time.Clock()
follower_x = random.randint(50 , 1200) 
follower_y = random.randint(50, 600)
rychlost = 2
start_ucitel = (170,660)
ucitel_x = start_ucitel[0]
ucitel_y = start_ucitel[1]
reached_start_pos = False # This will be set to true when the teacher and the student both arrive at the start position
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    distance = ((follower_x - ucitel_x) ** 2 + (follower_y - ucitel_y) ** 2) ** 0.5
    if distance > 60:
        #Jde si pro žáka
        if ucitel_x > follower_x:
            ucitel_x -= rychlost
        elif ucitel_x < follower_x:
            ucitel_x += rychlost
        if ucitel_y > follower_y:
            ucitel_y -= rychlost
        elif ucitel_y < follower_y:
            ucitel_y += rychlost
    else:
        # Move učitele zpět
        if ucitel_x < start_ucitel[0]:
            ucitel_x += rychlost
        if ucitel_x > start_ucitel[0]:
            ucitel_x -= rychlost
        if ucitel_y > start_ucitel[1]:
            ucitel_y += rychlost
        if ucitel_y < start_ucitel[1]:
            ucitel_y += rychlost
        # Posouvani vedenýho folowera
        if not reached_start_pos: 
            flwr_start_dist = [follower_x-start_ucitel[0],follower_y-start_ucitel[1]]
            if abs(flwr_start_dist[0]) >= rychlost:
                if follower_x < start_ucitel[0]:
                    follower_x += rychlost
                if follower_x > start_ucitel[0]:
                    follower_x -= rychlost
            else:
                if follower_x < start_ucitel[0]:
                    follower_x += 1
                if follower_x > start_ucitel[0]:
                    follower_x -= 1

            if abs(flwr_start_dist[1]) >= rychlost:
                if follower_y < start_ucitel[1]:
                    follower_y += rychlost
                if follower_y > start_ucitel[1]:
                    follower_y -= rychlost
            else:
                if follower_y < start_ucitel[1]:
                    follower_y += 1
                if follower_y > start_ucitel[1]:
                    follower_y -= 1
            if follower_x == start_ucitel[0] and follower_y == start_ucitel[1]:
                reached_start_pos = True
        if reached_start_pos == True:
            follower_y +=1
      
    screen.fill((255,255,255))
    pygame.draw.circle(screen, (0,0,0), (follower_x, follower_y), 30)
    pygame.draw.circle(screen, (255,0,0), (ucitel_x, ucitel_y), 30)
    pygame.display.update()
    clock.tick(FPS)