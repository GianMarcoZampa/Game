import pygame

import CharacterController as Controller
from Enemy import Enemy
from EnemyGenerator import EnemyGenerator
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

# Creating enemies and spawn timer
timer = 5
enemy = Enemy(0, 0, False)
enemy.x, enemy.y = 0, hs - enemy.height * 1.6

enemies = [enemy]

spawner_1 = EnemyGenerator(0, hs - enemy.height * 1.6, timer, fps)


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
    global spawner_1

    enemy = spawner_1.generate()
    if enemy is not None:
        enemies.append(enemy)
        spawner_1.enemy_rate -= 10

    # Enemies control
    for enemy in enemies:
        if enemy.death_counter is 60:
            enemies.remove(enemy)
        Controller.enemy_control(enemy, player, ws, hs, win)
    # Player control
    Controller.player_control(player, enemies, ws, hs, win)
    # Projectile control
    Controller.thrown_control(player, enemies, ws, hs, win)

print(pygame.font.get_default_font())
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
