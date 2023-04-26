import pygame
import sys
pygame.init()

clock = pygame.time.Clock()

FPS = 60
w = 1280
h = 720

screen =pygame.display.set_mode((w, h))
pygame.display.set_caption("minihra")

bg = pygame.image.load("pozadí.png")
bg = pygame.transform.scale(bg,(1280,720))
bg_rect = bg.get_rect()
bg_width = bg.get_width()

hl_postava_postoj = pygame.image.load("běžec_postoj.png")
hl_postava_postoj = pygame.transform.scale(hl_postava_postoj,(3000,1000))
hl_postava_postoj_rect = hl_postava_postoj.get_rect()
hl_postava_postoj_rect.x = 400
hl_postava_postoj_rect.y = 200


while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(bg, bg_rect)
    screen.blit(hl_postava_postoj, hl_postava_postoj_rect)
    
    pygame.display.update()
    
    clock.tick(FPS)

pygame.quit()

    