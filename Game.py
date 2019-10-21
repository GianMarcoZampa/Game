import pygame
from Player import Player

ws = 1000  # Screen's width
hs = 750  # Screen's height
bg = pygame.image.load('images\Background\BG.png')  # Background image

pygame.init()
win = pygame.display.set_mode((ws, hs))
pygame.display.set_caption('Platform Game')

player_1 = Player(0, 600)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_1.move_left()

    if keys[pygame.K_RIGHT]:
        player_1.move_right()

    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        player_1.stand()

    if not player_1.is_jumping:
        if keys[pygame.K_UP]:
            player_1.jump()
    else:
        player_1.jump()

    win.blit(bg, (0, 0))
    player_1.draw(win)
    pygame.display.update()

pygame.quit()
