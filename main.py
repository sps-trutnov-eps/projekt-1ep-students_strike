# Importování knihoven
import pygame
import random
import os

# Inicializace PyGame
pygame.init()

# Načítání náhodných obrázků do hry ze složky
image = ["1.png", "2.png", "3.png", "4.png", "5.png"]

# Základní parametry okna
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Killbot")
pygame.image.load("src/pozadí.png")

# Základní paramtery hry
FPS = 120
font = pygame.font.Font("src/font.ttf", 30)
run = True

# Vytvoření unkce pro náhodný výběr obrázku
def RandomImg():
    random.choice(image)     

# Hlavní smyčka hry
while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
pygame.display.update()
