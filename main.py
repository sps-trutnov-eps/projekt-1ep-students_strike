# Importování knihoven
import pygame
import random
import os

# Inicializace PyGame
pygame.init()

# Načítání náhodných obrázků do hry ze složky
image = ["1.png", "2.png", "3.png", "4.png", "5.png"]

# Základní parametry okna a hry
white = (255, 255, 255)
black = (0, 0, 0)
screen = pygame.display.set_mode((1280, 720))
screen.fill("white")
clock = pygame.time.Clock()
pygame.display.set_caption("")

# Základní paramtery hry
font = pygame.font.SysFont(None, 15)
input_box = pygame.Rect(200, 200, 300, 50)
color_inactive = pygame.Color("white")
color_active = pygame.Color("black")
color = color_inactive
text = ""
active = True
done =  False
FPS = 60
run = True

# Vytvoření unkce pro náhodný výběr obrázku
def RandomImg():
    random.choice(image)

while not done:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
        # Co se stane po kliknutí do textového políčka   
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
            # Změna barvy textového políčka
            color = color_active if active else color_inactive
            
        if event.type == pygame.KEYDOWN:
            if  active:
                if event.key == pygame.K_RETURN:
                    print(text)
                    text = ""
                # Odstranění posledního písmenka
                elif event.key == pygame.K_BACKSPACE and text:
                    text = text[:-1]
                else:
                    text += event.unicode
            

# Hlavní smyčka hry
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
pygame.display.update()