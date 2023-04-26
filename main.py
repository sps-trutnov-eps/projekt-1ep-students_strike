# Importování knihoven
import pygame
import random

# Inicializace PyGame
pygame.init()

# Základní parametry okna
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
pygame.image.load("src/background.png")

# Základní paramtery hry
FPS = 120
font = pygame.font.Font("src/digital.ttf", 30)
run = True

# Hlavní smyčka hry
while run:
    clock.tisk(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
pygame.display.update()
