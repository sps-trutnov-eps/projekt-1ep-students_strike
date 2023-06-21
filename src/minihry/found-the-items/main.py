import pygame
import sys

def game(screen, clock):
    found_staple = False     
    found_compasses = False   
    black = (0,0,0)
    FPS = 60
    # images
    background = pygame.image.load('třída.png')
    background = pygame.transform.scale(background, (1280, 720))
    staple = pygame.image.load('staple.png')
    staple = pygame.transform.scale(staple, (60, 60))
    compasses = pygame.image.load('compasses.png')
    compasses = pygame.transform.scale(compasses, (60, 60))
    font = pygame.font.SysFont('Consolas', 50)
    # im monkey
    table1 = pygame.Rect(30, 450, 160, 80)
    table2 = pygame.Rect(210, 450, 160, 80)
    table3 = pygame.Rect(390, 450, 160, 80)
    table4 = pygame.Rect(30, 570, 160, 80)
    table5 = pygame.Rect(210, 570, 160, 80)
    table6 = pygame.Rect(390, 570, 160, 80)
    table7 = pygame.Rect(750, 330, 160, 80)
    table8 = pygame.Rect(930, 330, 160, 80)
    table9 = pygame.Rect(750, 450, 160, 80)
    table10 = pygame.Rect(930, 450, 160, 80)
    table11 = pygame.Rect(750, 570, 160, 80)
    table12 = pygame.Rect(930, 570, 160, 80)
    door = pygame.Rect(590, 700, 100, 20)
    table_skin_closed = pygame.image.load('tableclosed.png')
    table_skin_closed = pygame.transform.scale(table_skin_closed, (160, 80))
    table_skin_open = pygame.image.load('table.png')
    table_skin_open = pygame.transform.scale(table_skin_open, (160, 110))
    hra = True
    while hra:
        clock.tick(FPS)
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
         
        screen.blit(background,(0,0))
        screen.blit(table_skin_closed, (30, 450))
        screen.blit(table_skin_closed, (210, 450))
        screen.blit(table_skin_closed, (390, 450))
        screen.blit(table_skin_closed, (30, 570))
        screen.blit(table_skin_closed, (210, 570))
        screen.blit(table_skin_closed, (390, 570))
        screen.blit(table_skin_closed, (750, 450))
        screen.blit(table_skin_closed, (750, 570))
        screen.blit(table_skin_closed, (930, 570))
        screen.blit(table_skin_closed, (930, 450))
        screen.blit(table_skin_closed, (750, 330))
        screen.blit(table_skin_closed, (930, 330))
        if found_staple:
            screen.blit(staple,(1215,660))
        if found_compasses:
            screen.blit(compasses,(1160,660))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                mx = pygame.mouse.get_pos()[0]
                my = pygame.mouse.get_pos()[1]
                #cord  = (mx, my)
                print(mx,my)
                text = 'you found a staple'
                text2 = 'you found a compasses'
                text3 = 'door is blocked'
                text4 = 'you escaped'

                if table1.collidepoint(mx, my):
                    screen.blit(table_skin_open, (30, 450))
                    found_staple = True 
                    screen.blit(font.render(text, True, (0, 0, 0)), (400, 360))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table2.collidepoint(mx, my):
                    screen.blit(table_skin_open, (210, 450))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table3.collidepoint(mx, my):
                    screen.blit(table_skin_open, (390, 450))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table4.collidepoint(mx, my):
                    screen.blit(table_skin_open, (30, 570))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table5.collidepoint(mx, my):
                    screen.blit(table_skin_open, (210, 570))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table6.collidepoint(mx, my):
                    screen.blit(table_skin_open, (390, 570))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table7.collidepoint(mx, my):
                    screen.blit(table_skin_open, (750, 330))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table8.collidepoint(mx, my):
                    screen.blit(table_skin_open, (930, 330))
                    screen.blit(font.render(text2, True, (0, 0, 0)), (400, 360))
                    found_compasses = True
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table9.collidepoint(mx, my):
                    screen.blit(table_skin_open, (750, 450))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table10.collidepoint(mx, my):
                    screen.blit(table_skin_open, (930, 450))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table11.collidepoint(mx, my):
                    screen.blit(table_skin_open, (750, 570))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if table12.collidepoint(mx, my):
                    screen.blit(table_skin_open, (930, 570))
                    pygame.display.update()
                    pygame.time.wait(2000)
                if door.collidepoint(mx, my):
                    if found_staple and found_compasses:
                        screen.blit(font.render(text4, True, (0, 0, 0)), (470, 360))
                        pygame.display.update()
                        pygame.time.wait(2000)
                        return 0 #Vždy vrátí nula studentů
                    screen.blit(font.render(text3, True, (0, 0, 0)), (470, 360))
                    pygame.display.update()
                    pygame.time.wait(2000)

                    
        
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_ESCAPE]:
#             pygame.quit()
#             sys.exit()

        pygame.display.update()
