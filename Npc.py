import pygame

from Ammo import Ammo


class Npc:

    def __init__(self, x, y, width, height, speed, life, dead_frames, damage=0, knockback=0, jump_frames=0,
                 shot_frames=0, attack_frames=0):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.speed = speed
        self.life_max = self.life = life
        self.damage = damage
        self.knockback = knockback
        self.walk_counter = 0
        self.left, self.right = False, True
        self.is_running = False
        self.is_jumping = False
        self.is_throwing = False
        self.is_attacking = False
        self.is_dying = False
        self.jump_counter = 0
        self.jc = self.jump_frames = jump_frames
        self.shot_counter, self.shot_frames = 0, shot_frames
        self.thrown_obj = []
        self.attack_counter, self.attack_frames = 0, attack_frames
        self.dead_frames = dead_frames
        self.score = 0

    def jump(self):
        if not self.is_dying:
            if not self.is_jumping:
                self.is_jumping = True
            else:
                if self.jc >= -self.jump_frames:
                    neg = 1
                    if self.jc < 0:
                        neg = -1
                    self.y -= neg * (self.jc ** 2) * 0.5
                    self.jc -= 1
                    if self.jc % 2 is 0:
                        self.jump_counter += 1
                else:
                    self.is_jumping = False
                    self.jc = self.jump_frames
                    self.jump_counter = 0

    def stand(self):
        if not self.is_dying:
            self.is_running = False
            self.walk_counter = 0

    def look_left(self):
        self.left = True
        self.right = False

    def look_right(self):
        self.left = False
        self.right = True

    def move_left(self):
        if not self.is_dying:
            self.look_left()
            self.is_running = True
            self.x -= self.speed
            if self.walk_counter < 10:
                self.walk_counter += 1
            else:
                self.walk_counter = 0

    def move_right(self):
        if not self.is_dying:
            self.look_right()
            self.is_running = True
            self.x += self.speed
            if self.walk_counter < 10:
                self.walk_counter += 1
            else:
                self.walk_counter = 0

    def throw(self):
        if not self.is_dying:
            if not self.is_throwing:
                self.is_throwing = True
            else:
                if self.shot_counter < self.shot_frames:
                    self.shot_counter += 1
                    if self.shot_counter is self.shot_frames // 2 - 1:
                        num = 1
                        if self.left:
                            num = -1
                        self.thrown_obj.append(
                            Ammo(self.x + num * int(self.width * 0.3), self.y + int(self.height * 0.3), self.left))
                else:
                    self.shot_counter = 0
                    self.is_throwing = False

    def die(self):
        if self.life <= 0:
            if self.dead_frames > 1:
                self.is_dying = True
                self.dead_frames -= 1

    def attack(self, target):
        if not self.is_dying:
            if not self.is_attacking:
                self.is_attacking = True
                self.attack_counter = 0
            else:
                if self.attack_counter < self.attack_frames-1:
                    self.attack_counter += 1
                    if self.attack_counter is int(self.attack_frames*0.5):
                        target.knock_back(self.knockback)
                        target.life -= self.damage
                        self.score += self.damage
                else:
                    self.is_attacking = False

    def knock_back(self, knockback):
        if self.left:
            self.x += knockback
        else:
            self.x -= knockback

    def health_bar(self):
        if self.life > 0:
            life_percent = self.life / self.life_max
        else:
            life_percent = 0
        green = pygame.rect.Rect((self.x + 6, self.y - 15), ((self.width - 6) * life_percent, 10))
        red = pygame.rect.Rect((self.x + 6, self.y - 15),
                               ((self.width - 6), 10))
        return green, red
