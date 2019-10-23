import pygame


# This function control pressed keys and execute the right actions, then it update player
def player_control(player, ws, hs, win):

    player.die()

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
    enemy.die()
    if enemy.x < player.x:
        enemy.is_attacking = False
        enemy.move_right()
        if enemy.x > ws - enemy.width:
            enemy.x = ws - enemy.width
    elif (player.x - enemy.speed) < enemy.x < (player.x + enemy.speed):
        enemy.stand()
        if(player.y + player.height) > enemy.y:
            enemy.attack(player)
            print(player.life, player.life_max, enemy.score)
        else:
            enemy.is_attacking = False
    else:
        enemy.is_attacking = False
        enemy.move_left()
        if enemy.x < 0:
            enemy.x = 0

    enemy.draw(win)


# This function is for ammo handling
def thrown_control(player, targets, ws, hs, win):
    for bullet in player.thrown_obj:
        draw = True
        bullet.move()
        if bullet.x > ws or bullet.x < 0 - bullet.width:
            draw = False
        for enemy in targets:
            if not enemy.is_dying:
                if enemy.x < bullet.x < enemy.x + enemy.width and enemy.y < bullet.y < enemy.y + enemy.height:
                    enemy.life -= bullet.damage
                    enemy.knock_back(bullet.knockback)
                    player.score += bullet.damage
                    print(player.score)
                    draw = False
                    break
        if draw:
            bullet.draw(win)
        else:
            player.thrown_obj.remove(bullet)
