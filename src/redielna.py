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
pozadavek = random.randint(15, 25)
povoleni = 0
velikost = 50 
x = 10 
y = 10 
pozice_x = 50  
pozice_y = 355  
rychlost = 3 # pixely / frame
counter, text = 0, '0'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
pozadí_prizemi = pygame.image.load("chodba.png")
pozadí_prizemi = pygame.transform.scale(pozadí_prizemi, (ROZLISENI_X , ROZLISENI_Y))
pozadi_nadprizemi = pygame.image.load("chodba 1.png")
pozadi_nadprizemi = pygame.transform.scale(pozadi_nadprizemi, (ROZLISENI_X , ROZLISENI_Y))
reditelna = pygame.image.load("obrázky/reditelna.png")
reditelna = pygame.transform.scale(reditelna, (ROZLISENI_X , ROZLISENI_Y))
venek = pygame.image.load("obrázky/před-školou.png")
text_1_font = pygame.font.Font(None, 72)

navstiveny_třídy = []
# pomocny objekt pro omezeni FPS  
hodiny = pygame.time.Clock()

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
        if udalost.type == pygame.USEREVENT:
            counter += 1
            
    
    
    
    okno.blit(reditelna, (0, 0))
    pygame.draw.circle(okno,barva_hl,(pozice_x, pozice_y),velikost / 2)
    if counter > 5 and counter < 8:
        text1 = text_1_font.render(("Co tu chceš? "), True, CERNA_BARVA)
        okno.blit(text1, (840, 600))
    if counter > 10 and counter < 15:
        text2 = text_1_font.render(("Jdu se zeptat, zda bychom mohli odejít ze školy. "), True, CERNA_BARVA)
        okno.blit(text2, (100, 200))
    if counter > 17 and counter < 20:
        text3 = text_1_font.render(("A kolik vás tu je? "), True, CERNA_BARVA)
        okno.blit(text3, (820, 600))
    
    
    
    
    
    
    
    if pozice_x < 660:
        pozice_x += 2

    
   
         
    # prekresleni obsahu okna  
    pygame.display.update()  
    # zastropovani FPS  
    hodiny.tick(FPS)  
 