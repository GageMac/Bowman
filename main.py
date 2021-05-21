import pygame
from pygame.constants import MOUSEBUTTONDOWN, MOUSEBUTTONUP, MOUSEMOTION
pygame.init()

#Creating the screen
screen = pygame.display.set_mode((1900, 900))

#Background
background = pygame.image.load('background.png')
#Title and Icon
pygame.display.set_caption("Bowman")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Player1
player1Img = pygame.image.load('player1.png')
player1X = 50
player1Y = 770

def player1():
    screen.blit(player1Img, (player1X, player1Y))

#Player2
player2Img = pygame.image.load('player2.png')
player2X = 1800
player2Y = 770

def player2():
    screen.blit(player2Img, (player2X, player2Y))

#Arrow
arrowImg = pygame.image.load('arrow.png')
arrowX = 100
arrowY = 450

def arrow(x, y):
    screen.blit(arrowImg, (x, y))

#Tesing Drag
#Testing Drawing
drawing = False
mouse_position = (0,0)
BLACK = (0, 0, 0)
clock = pygame.time.Clock()
FPS = 30
last_pos = None
#Game loop
running = True
while running:
    screen.fill((100,90,255))
    #Background image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     if event.button == 1:            
        #         if rectangle1.collidepoint(event.pos):
        #             rectangle1_draging = True
        #             mouse_x, mouse_y = event.pos
        #             offset_x = rectangle1.x - mouse_x
        #             offset_y = rectangle1.y - mouse_y

        # elif event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 1:            
        #         rectangle1_draging = False

        # elif event.type == pygame.MOUSEMOTION:
        #     if rectangle1_draging:
        #         mouse_x, mouse_y = event.pos
        #         rectangle1.x = mouse_x + offset_x
        #         rectangle1.y = mouse_y + offset_y
        elif event.type == MOUSEMOTION:
            if(drawing):
                mouse_position = pygame.mouse.get_pos()
                if last_pos is not None:
                    pygame.draw.line(screen, BLACK, last_pos, mouse_position, 5)
                last_pos = mouse_position
        elif event.type == MOUSEBUTTONUP:
            mouse_position = (0, 0)
            drawing = False
        elif event.type == MOUSEBUTTONDOWN:
            drawing = True
            # if rectangle1.collidepoint(event.pos):
            #     rectangle1_draging = True
            #     mouse_x, mouse_y = event.pos
            #     offset_x = rectangle1.x - mouse_x
            #     offset_y = rectangle1.y - mouse_y

    pygame.display.flip()
    clock.tick(FPS)

    player1()
    player2()
    arrow(arrowX, arrowY)
    pygame.display.update()