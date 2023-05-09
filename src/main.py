import pygame
import random
import sys
import math
import time
pygame.init()
# ---VARIABLES---
screen = pygame.display.set_mode((1280, 720))
FPS = 120
# ---------------
# ---- CLASS REWORK ----


class Teacher_event():
    def __init__(self,SCREEN, followers, teacher_start, teacher_speed):
        self.SCREEN = SCREEN
        self.TEACHER_START = teacher_start # Tuple x,y pozice startu učitele
        self.teacher_pos = list(teacher_start) # Aktuální pozice učitele
        self.TEACHER_SPEED = teacher_speed
        #vybereme si index náhodného žáka, pro kterého půjdeme
        student_index = random.randint(0,len(followers)-1)
        self.target_pos = [followers[student_index].x, followers[student_index].y]
        self.reached_start_pos = False
    def update_position(self, followers):
        distance = ((follower_x - ucitel_x) ** 2 + (follower_y - ucitel_y) ** 2) ** 0.5 # Vzdálenost učitele od žáka
        if distance > 60:
            # Jde si pro žáka
            if self.teacher_pos[0] > self.target_pos[0]:
                self.teacher_pos[0] -= self.TEACHER_SPEED
            elif self.teacher_pos[0] < self.target_pos[0]:
                self.teacher_pos[0] += self.TEACHER_SPEED
            if self.teacher_pos[1] > self.target_pos[1]:
                self.teacher_pos[1] -= self.TEACHER_SPEED
            elif self.teacher_pos[1] < self.target_pos[1]:
                self.teacher_pos[1] += self.TEACHER_SPEED
        else:
         # Move učitele zpět
            if self.ucitel_x < self.start_ucitel[0]:
                self.ucitel_x += self.rychlost
            if self.ucitel_x > self.start_ucitel[0]:
                self.ucitel_x -= self.rychlost
            if self.ucitel_y > self.start_ucitel[1]:
                self.ucitel_y += self.rychlost
            if self.ucitel_y < self.start_ucitel[1]:
                self.ucitel_y += self.rychlost
                # Posouvani vedenýho folowera
            if not self.reached_start_pos: 
                flwr_start_dist = [self.target_pos[0]-self.start_ucitel[0],self.target_pos[1]-self.start_ucitel[1]]
                if abs(flwr_start_dist[0]) >= self.rychlost:
                    if self.target_pos[0] < self.start_ucitel[0]:
                        self.target_pos[0] += self.rychlost
                    if self.target_pos[0] > self.start_ucitel[0]:
                        self.target_pos[0] -= self.rychlost
                else:
                    if self.target_pos[0] < self.start_ucitel[0]:
                        self.target_pos[0] += 1
                    if self.target_pos[0] > self.start_ucitel[0]:
                           self.target_pos[0] -= 1

                if abs(flwr_start_dist[1]) >= self.rychlost:
                    if self.target_pos[1] < self.start_ucitel[1]:
                        self.target_pos[1] += self.rychlost
                    if self.target_pos[1] > self.start_ucitel[1]:
                        self.target_pos[1] -= self.rychlost
                else:
                    if self.target_pos[1] < self.start_ucitel[1]:
                        self.target_pos[1] += 1
                    if self.target_pos[1] > self.start_ucitel[1]:
                        self.target_pos[1] -= 1
                if follower_x == start_ucitel[0] and follower_y == start_ucitel[1]:
                    reached_start_pos = True
            if reached_start_pos == True:
                follower_y += 1
            
            
            
            
            
clock = pygame.time.Clock()
follower_x = random.randint(50 , 1200) 
follower_y = random.randint(50, 600)
rychlost = 2
start_ucitel = (120, 660)
ucitel_x = start_ucitel[0]
ucitel_y = start_ucitel[1]
# This will be set to true when the teacher and the student both arrive at the start position
reached_start_pos = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (follower_x, follower_y), 30)
    pygame.draw.circle(screen, (255, 0, 0), (ucitel_x, ucitel_y), 30)
    pygame.display.update()
    clock.tick(FPS)
