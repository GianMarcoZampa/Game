import pygame


# This function control pressed keys and execute the right actions, then it update player
def player_control(player, enemies, ws, hs, win):

    player.die()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_x]:
        player.use_power_1()

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

    if not player.is_attacking:
        if keys[pygame.K_m]:
            for enemy in enemies:
                if enemy.x < player.x + player.width*0.5 < enemy.x + enemy.width and \
                        enemy.y < player.y + player.height*0.5 < enemy.y + enemy.height and \
                        not enemy.is_dying:
                    player.attack(enemy)
                    if player.is_attacking:
                        break
                if not player.is_attacking:
                    player.attack()
    else:
        for enemy in enemies:
            if enemy.x < player.x + player.width*0.5 < enemy.x + enemy.width and \
                    enemy.y < player.y + player.height*0.5 < enemy.y + enemy.height:
                player.attack(enemy)
            else:
                player.attack()

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
        if(player.y + player.height) > enemy.y and not player.is_dying:
            enemy.attack(player)
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
                    draw = False
                    break
        if draw:
            bullet.draw(win)
        else:
            player.thrown_obj.remove(bullet)
