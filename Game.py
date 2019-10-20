import pygame


ws = 1000  # Screen's width
hs = 750  # Screen's height
bg = pygame.image.load('images\background\BG.png')  # Background image

pygame.init()
win = pygame.display.set_mode((ws, hs))
pygame.display.set_caption('Platform Game')

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.blit(bg, (0, 0))
    pygame.display.update()


pygame.quit()