import pygame
import random
import sys
import math
import time
pygame.init()
# ---VARIABLES---
# ---------------
# ---- CLASS REWORK ----


class Teacher_event():
    def __init__(self,SCREEN, followers, teacher_start, teacher_speed):
        self.SCREEN = SCREEN
        self.TEACHER_START = teacher_start # Tuple x,y pozice startu učitele
        self.teacher_pos = list(teacher_start) # Aktuální pozice učitele
        self.TEACHER_SPEED = teacher_speed
        self.original_followers = followers # List followeru ktery byl na začátku
        #vybereme si index náhodného žáka, pro kterého půjdeme
        self.student_index = random.randint(0,len(followers)-1)
        self.follower_removed = False # Když se učitel dotkne target followera, odstranímeho followera z listu
        self.target_pos = [followers[self.student_index].x, followers[self.student_index].y]
        self.reached_start_pos = False
    def update(self, followers):
        #updating target pos
        if not self.follower_removed:
            self.target_pos = [followers[self.student_index].x, followers[self.student_index].y]



        distance = ((self.target_pos[0] - self.teacher_pos[0]) ** 2 + (self.target_pos[1] - self.teacher_pos[1]) ** 2) ** 0.5 # Vzdálenost učitele od žáka
        if distance < 60 and self.follower_removed == False: # Removing from the original list, so he does not follow leader anymore
            self.follower_removed = True
            del followers[self.student_index]

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
            if self.teacher_pos[0] < self.TEACHER_START[0]:
                self.teacher_pos[0] += self.TEACHER_SPEED
            if self.teacher_pos[0] > self.TEACHER_START[0]:
                self.teacher_pos[0] -= self.TEACHER_SPEED
            if self.teacher_pos[1] > self.TEACHER_START[1]:
                self.teacher_pos[1] += self.TEACHER_SPEED
            if self.teacher_pos[1] < self.TEACHER_START[1]:
                self.teacher_pos[1] += self.TEACHER_SPEED
                # Posouvani vedenýho folowera
            if not self.reached_start_pos: 
                flwr_start_dist = [self.target_pos[0]-self.start_ucitel[0],self.target_pos[1]-self.start_ucitel[1]]
                if abs(flwr_start_dist[0]) >= self.TEACHER_SPEED:
                    if self.target_pos[0] < self.TEACHER_START[0]:
                        self.target_pos[0] += self.TEACHER_SPEED
                    if self.target_pos[0] > self.TEACHER_START[0]:
                        self.target_pos[0] -= self.TEACHER_SPEED
                else:
                    if self.target_pos[0] < self.TEACHER_START[0]:
                        self.target_pos[0] += 1
                    if self.target_pos[0] > self.start_ucitel[0]:
                           self.target_pos[0] -= 1

                if abs(flwr_start_dist[1]) >= self.TEACHER_SPEED:
                    if self.target_pos[1] < self.TEACHER_START[1]:
                        self.target_pos[1] += self.TEACHER_SPEED
                    if self.target_pos[1] > self.TEACHER_START[1]:
                        self.target_pos[1] -= self.TEACHER_SPEED
                else:
                    if self.target_pos[1] < self.TEACHER_START[1]:
                        self.target_pos[1] += 1
                    if self.target_pos[1] > self.TEACHER_START[1]:
                        self.target_pos[1] -= 1
                if self.target_pos[0] == self.TEACHER_START[0] and self.target_pos[1] == self.TEACHER_START[1]:
                    reached_start_pos = True
            if reached_start_pos == True:
                self.target_pos[1] += 1
    

        return followers # tento event má efekt na list followeru(odebírá followery) a tak puvodnimu programu vraci upraveny list
            
            
            
            
""" original code
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
    distance = ((follower_x - ucitel_x) ** 2 +
                (follower_y - ucitel_y) ** 2) ** 0.5
    if distance > 60:
        # Jde si pro žáka
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
            flwr_start_dist = [follower_x-start_ucitel[0],
                               follower_y-start_ucitel[1]]
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
            follower_y += 1

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 0), (follower_x, follower_y), 30)
    pygame.draw.circle(screen, (255, 0, 0), (ucitel_x, ucitel_y), 30)
    pygame.display.update()
    clock.tick(FPS)
 """