import pygame

import CharacterController as Controller
from Player import Player

ws = 1000  # Screen's width
hs = 750  # Screen's height
bg = pygame.image.load('images\Background\BG.png')  # Background image
fps = 60

pygame.init()
win = pygame.display.set_mode((ws, hs), pygame.RESIZABLE)
pygame.display.set_caption('Platform Game')

player_1 = Player(0,0)
player_1.y = ws - player_1.height*3.75

run = True
while run:
    pygame.time.Clock().tick(fps)

    for event in pygame.event.get():
        if event.type is pygame.QUIT:
            run = False
        if event.type is pygame.VIDEORESIZE:
            ws, hs = event.w, event.h
            win = pygame.display.set_mode((ws, hs), pygame.RESIZABLE)
            bg = pygame.transform.scale(bg, (ws, hs))

    win.blit(bg, (0, 0))

    Controller.player_control(player_1, ws, hs, win)
    Controller.thrown_control(player_1, ws, hs, win)

    pygame.display.update()

pygame.quit()
