# pouzite knihovny 
import sys  
import random
import time
# pouzity framework  
import pygame  
# spusteni frameworku  
pygame.init()  
  
# pocatecni nastaveni hodnot  
ROZLISENI_X = 1280 
ROZLISENI_Y = 720
FPS = 60
CERNA_BARVA = (0, 0, 0)  
BILA_BARVA = (255, 255, 255)  
barva_hl = (128,0,128) 
barva_foloweri = (255,0,0) 
pocet_foloweri = 10
velikost = 50 
x = 10 
y = 10 
pozice_x = (ROZLISENI_X - velikost) / 2  
pozice_y = (ROZLISENI_Y - velikost) / 2  
rychlost = 3 # pixely / frame

pozadí = pygame.image.load("chodba.png")
pozadí = pygame.transform.scale(pozadí, (ROZLISENI_X , ROZLISENI_Y))
cislo_patra = 1
cislo_patra_font = pygame.font.Font(None, 72) # Font pro vykresení čísla patra

navstiveny_třídy = []
# pomocny objekt pro omezeni FPS  
hodiny = pygame.time.Clock()  

class foloweri_class: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
 
 
 
 
 
foloweri = [] 
for i in range(pocet_foloweri): 
    foloweri.append(foloweri_class(random.randint(velikost, ROZLISENI_X - velikost), random.randint(velikost, ROZLISENI_Y - velikost))) 
 

# vytvoreni okna  
okno = pygame.display.set_mode((ROZLISENI_X, ROZLISENI_Y))  
pygame.display.set_caption('Strike')  
  
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
  
#ovladani pomoci klavesnice  
    klavesy = pygame.key.get_pressed()  
      
    if klavesy[pygame.K_ESCAPE]:  
        pygame.quit()  
        sys.exit()  
#ovládání hráće
    if klavesy[pygame.K_RIGHT]:  
        pozice_x += rychlost  
    if klavesy[pygame.K_LEFT]:  
        pozice_x -= rychlost  
    if klavesy[pygame.K_DOWN]:  
        pozice_y += rychlost  
    if klavesy[pygame.K_UP]:  
        pozice_y -= rychlost  
      
#kolize hráče
    if pozice_x > ROZLISENI_X - velikost / 2:  
        pozice_x = ROZLISENI_X - velikost / 2 
    if pozice_y > ROZLISENI_Y - velikost / 2:  
        pozice_y = ROZLISENI_Y - velikost / 2
    if pozice_x < velikost / 2:  
        pozice_x = velikost / 2 
    if pozice_y < velikost / 2:  
        pozice_y = velikost / 2 
#
        
    if pozice_x > 100 and pozice_x < 215 and pozice_y > 0 and pozice_y < 5 + velikost and klavesy[pygame.K_e]:
        poradi_dveri = 1
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf") 
         
    if pozice_x > 580 and pozice_x < 695 and pozice_y > 0 and pozice_y < 5 + velikost and klavesy[pygame.K_e]:
        poradi_dveri = 2
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf 1") 
    
    if pozice_x > 1065 and pozice_x < 1180 and pozice_y > 0 and pozice_y < 5 + velikost and klavesy[pygame.K_e]:
        poradi_dveri = 3
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf 2")
    
    if pozice_x > 100 and pozice_x < 215 and pozice_y > 5 + velikost and pozice_y < ROZLISENI_Y and klavesy[pygame.K_e]:
        poradi_dveri = 4
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf 4") 
         
    if pozice_x > 580 and pozice_x < 695 and pozice_y > 5 + velikost and pozice_y < ROZLISENI_Y and klavesy[pygame.K_e]:
        poradi_dveri = 5
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf 5") 
    
    if pozice_x > 1065 and pozice_x < 1180 and pozice_y > 5 + velikost and pozice_y < ROZLISENI_Y and klavesy[pygame.K_e]:
        poradi_dveri = 6
        cislo_dveri = cislo_patra * 10 + poradi_dveri
        if cislo_dveri not in navstiveny_třídy:
            navstiveny_třídy.append(cislo_dveri)
            print("baf 6")

       
     
 
     
    # stanoveni barvy pozadi
    
    okno.blit(pozadí, (0, 0))
    
    
     
#kolize foloweru na hrace
    for i in range(pocet_foloweri): 
        distance = ((pozice_x - foloweri[i].x) ** 2 + (pozice_y - foloweri[i].y) ** 2) ** 0.5 
        if distance > velikost + 10: 
            if foloweri[i].x > pozice_x: 
                foloweri[i].x -= rychlost 
            elif foloweri[i].x < pozice_x: 
                foloweri[i].x += rychlost 
            if foloweri[i].y > pozice_y: 
                foloweri[i].y -= rychlost 
            elif foloweri[i].y < pozice_y: 
                foloweri[i].y += rychlost
#kolize hráće na foloweri
    for i in range(pocet_foloweri):
        distance = ((pozice_x - foloweri[i].x) ** 2 + (pozice_y - foloweri[i].y) ** 2) ** 0.5 
        if distance < velikost + 10: 
            if foloweri[i].x > pozice_x: 
                foloweri[i].x += rychlost 
            elif foloweri[i].x < pozice_x: 
                foloweri[i].x -= rychlost 
            if foloweri[i].y > pozice_y: 
                foloweri[i].y += rychlost 
            elif foloweri[i].y < pozice_y: 
                foloweri[i].y -= rychlost
#kolize foloweru stěn 
    for i in range(pocet_foloweri):
        if foloweri[i].x > ROZLISENI_X - velikost / 2:
            foloweri[i].x = ROZLISENI_X - velikost / 2
        elif foloweri[i].x < velikost / 2: 
            foloweri[i].x = velikost / 2
        if foloweri[i].y > ROZLISENI_Y - velikost / 2: 
            foloweri[i].y = ROZLISENI_Y - velikost / 2
        elif foloweri[i].y < velikost / 2: 
            foloweri[i].y = velikost / 2
#kolize folowerů na folowera
    for i in range(pocet_foloweri): 
        for y in range(pocet_foloweri): 
            if y != i: 
                distance_1 = ((foloweri[i].x - foloweri[y].x) ** 2 + (foloweri[i].y - foloweri[y].y ) ** 2) ** 0.5 
                if distance_1 < velikost + 10: 
                    if foloweri[i].x > foloweri[y].x: 
                        foloweri[i].x += rychlost 
                    elif foloweri[i].x < foloweri[y].x: 
                        foloweri[i].x -= rychlost 
                    if foloweri[i].y > foloweri[y].y: 
                        foloweri[i].y += rychlost 
                    elif foloweri[i].y < foloweri[y].y: 
                        foloweri[i].y -= rychlost
                        

    
#vykreslení folowerů
    for i in range(pocet_foloweri): 
        pygame.draw.circle(okno, barva_foloweri, (foloweri[i].x, foloweri[i].y), velikost / 2) 
         
    pygame.draw.circle(okno,barva_hl,(pozice_x, pozice_y),velikost / 2) 
  #  pygame.draw.circle(okno,barva_foloweri,(x, y),velikost / 2) 
    
    #vykreslení čísel pater
    text1 = cislo_patra_font.render(("Patro " + str(cislo_patra + 1)), True, CERNA_BARVA)
    text2 = cislo_patra_font.render(("Patro " + str(cislo_patra- 1) ), True, CERNA_BARVA)
    okno.blit(text1, (50, ROZLISENI_Y/2- 200))
    okno.blit(text2, (50, ROZLISENI_Y/2 + 125))
    # prekresleni obsahu okna  
    pygame.display.update()  
    # zastropovani FPS  
    hodiny.tick(FPS)  
 
