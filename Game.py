import pygame

import CharacterController as Controller
from Enemy import Enemy
from Player import Player

fps = 60  # Frame per second
ws = 1000  # Screen's width
hs = 750  # Screen's height
bg = pygame.image.load('images/Background/BG.png')  # Background image
run, pause = True, False  # Run of the program and pause

# Setting window
pygame.init()
win = pygame.display.set_mode((ws, hs), pygame.RESIZABLE)
pygame.display.set_caption('Platform Game')

# Creating player 1
player_1 = Player(0, 0)
player_1.x, player_1.y = ws * 0.5, hs - player_1.height * 1.6

# Creating enemies
enemy_1 = Enemy(0, 0, True)
enemy_1.x, enemy_1.y = ws - enemy_1.width, hs - enemy_1.height * 1.6

enemy_2 = Enemy(0, 0, False)
enemy_2.x, enemy_2.y = 0, hs - enemy_2.height * 1.6

enemies = [enemy_1, enemy_2]


def events_handler():
    global ws
    global hs
    global bg
    global win
    global run
    global pause

    for event in pygame.event.get():
        # Exit command
        if event.type is pygame.QUIT:
            run = False
        # Resize command
        if event.type is pygame.VIDEORESIZE:
            ws, hs = event.w, event.h
            win = pygame.display.set_mode((ws, hs), pygame.RESIZABLE)
            bg = pygame.transform.scale(bg, (ws, hs))
        # Pause command
        if event.type is pygame.KEYDOWN:
            if event.key is pygame.K_p:
                pause = True
    # Pause loop
    while pause:
        for event in pygame.event.get():
            if event.type is pygame.KEYDOWN:
                if event.key is pygame.K_p:
                    pause = False


def entities_handler(player, enemies):
    global ws
    global hs
    global win
    # Enemies control
    for enemy in enemies:
        Controller.enemy_control(enemy, player, ws, hs, win)
    # Player control
    Controller.player_control(player, ws, hs, win)
    # Projectile control
    Controller.thrown_control(player, enemies, ws, hs, win)


# Main loop of the program
while run:
    # Clock 'fps' tick in a second
    pygame.time.Clock().tick(fps)
    # Handling in-game events
    events_handler()
    # Window and entities update and redraw
    win.blit(bg, (0, 0))
    entities_handler(player_1, enemies)
    # Screen updating
    pygame.display.update()

pygame.quit()
