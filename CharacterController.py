import pygame


def player_control(player, ws, hs, win):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
        if player.x < 0:
            player.x = 0

    if keys[pygame.K_RIGHT]:
        player.move_right()
        if player.x > ws - player.width * 0.5:
            player.x = ws - player.width * 0.5

    if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]):
        player.stand()

    if not player.is_throwing:
        if keys[pygame.K_SPACE]:
            player.throw()
    else:
        player.throw()

    if not player.is_jumping:
        if keys[pygame.K_UP]:
            player.jump()
    else:
        player.jump()

    player.draw(win)


def thrown_control(player, ws, hs, win):
    for bullet in player.thrown_obj:
        bullet.move()
        if bullet.x > ws or bullet.x < 0 - bullet.width:
            player.thrown_obj.remove(bullet)
        else:
            bullet.draw(win)
