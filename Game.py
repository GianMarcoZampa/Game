import pygame

import CharacterController as Controller
from Enemy import Enemy
from Player import Player

fps = 60 # Frame per second
ws = 1000  # Screen's width
hs = 750  # Screen's height
bg = pygame.image.load('images/Background/BG.png')  # Background image

# Setting window
pygame.init()
win = pygame.display.set_mode((ws, hs), pygame.RESIZABLE)
pygame.display.set_caption('Platform Game')

# Creating player 1
player_1 = Player(0, 0)
player_1.y = hs - player_1.height*1.6

# Creating enemy 1
enemy_1 = Enemy(0, 0)
enemy_1.x, enemy_1.y = ws - enemy_1.width, hs - enemy_1.height*1.6

# Main loop of the program
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

    # Window, player 1 and ammo update and redraw
    win.blit(bg, (0, 0))
    Controller.player_control(player_1, ws, hs, win)
    Controller.enemy_control(enemy_1, player_1, ws, hs, win)
    Controller.thrown_control(player_1, ws, hs, win)

    pygame.display.update()

pygame.quit()
