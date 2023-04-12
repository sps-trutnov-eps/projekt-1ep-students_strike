# pouzite knihovny
import turtle
import sys 
import random 
# pouzity framework 
import pygame 
# spusteni frameworku 
pygame.init() 
 
# pocatecni nastaveni hodnot 
ROZLISENI_X = 1920
ROZLISENI_Y = 1080
FPS = 60 
CERNA_BARVA = (0, 0, 0) 
BILA_BARVA = (255, 255, 255) 
barva_hl = (128,0,128)
barva_f = (255,0,0)
velikost = 50
x = 10
y = 10
pozice_x = (ROZLISENI_X - velikost) / 2 
pozice_y = (ROZLISENI_Y - velikost) / 2 
rychlost = 5 # pixely / frame 
 
# pomocny objekt pro omezeni FPS 
hodiny = pygame.time.Clock() 




# vytvoreni okna 
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y)) 
pygame.display.set_caption('Interaktivní čtvereček') 
 
# vykreslovaci smycka 
while True: 
    # jake nastaly udalosti? 
    for udalost in pygame.event.get(): 
        # byla nektera z nich typu QUIT? 
        if udalost.type == pygame.QUIT: 
            # vypnuti frameworku 
            pygame.quit() 
            # vypnuti aplikace 
            sys.exit() 
 
    # ovladani pomoci klavesnice 
    klavesy = pygame.key.get_pressed() 
     
    if klavesy[pygame.K_ESCAPE]: 
        pygame.quit() 
        sys.exit() 
 
    if klavesy[pygame.K_RIGHT]: 
        pozice_x += rychlost 
    if klavesy[pygame.K_LEFT]: 
        pozice_x -= rychlost 
    if klavesy[pygame.K_DOWN]: 
        pozice_y += rychlost 
    if klavesy[pygame.K_UP]: 
        pozice_y -= rychlost 
     
    # kontroly 
    if pozice_x > ROZLISENI_X - velikost: 
        pozice_x = ROZLISENI_X - velikost 
    if pozice_y > ROZLISENI_Y - velikost: 
        pozice_y = ROZLISENI_Y - velikost 
    if pozice_x < 0: 
        pozice_x = 0 
    if pozice_y < 0: 
        pozice_y = 0
    

     
    # stanoveni barvy pozadi 
    okno.fill(BILA_BARVA) 
    
    # vykresleni obsahu okna  
    
    distance = ((pozice_x - x) ** 2 + (pozice_y - y) ** 2) ** 0.5
    if distance > velikost + 10:
        if x > pozice_x:
            x -= rychlost
        elif x < pozice_x:
            x += rychlost
        if y > pozice_y:
            y -= rychlost
        elif y < pozice_y:
            y += rychlost
    
    pygame.draw.circle(okno,barva_hl,(pozice_x, pozice_y),velikost / 2)
    pygame.draw.circle(okno,barva_f,(x, y),velikost / 2)

    # prekresleni obsahu okna 
    pygame.display.update() 
    # zastropovani FPS 
    hodiny.tick(FPS) 
 
