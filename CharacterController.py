import pygame


# This function control pressed keys and execute the right actions, then it update player
def player_control(player, ws, hs, win):
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player.move_left()
        if player.x < 0:
            player.x = 0

    if keys[pygame.K_RIGHT]:
        player.move_right()
        if player.x > ws - player.width:
            player.x = ws - player.width

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


# This function controls enemies
def enemy_control(enemy, player, ws, hs, win):
    if enemy.x < player.x:
        enemy.move_right()
        if enemy.x > ws - enemy.width:
            enemy.x = ws - enemy.width
    elif (player.x - enemy.speed) < enemy.x < (player.x + enemy.speed):
        enemy.stand()
    else:
        #enemy.life -= 5
        #enemy.die()
        enemy.move_left()
        if enemy.x < 0:
            enemy.x = 0

    enemy.draw(win)


# This function is for ammo handling
def thrown_control(player, ws, hs, win):
    for bullet in player.thrown_obj:
        bullet.move()
        if bullet.x > ws or bullet.x < 0 - bullet.width:
            player.thrown_obj.remove(bullet)
        else:
            bullet.draw(win)
