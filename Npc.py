import pygame


class Npc:

    def __init__(self, x, y, width, height, speed, jump_height):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.speed = speed
        self.walk_counter = 0
        self.left, self.right = False, True
        self.is_standing = True
        self.is_jumping = False
        self.jump_counter = self.jump_height = jump_height

    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.walk_counter = 0
        else:
            if self.jump_counter >= -self.jump_height:
                neg = 1
                if self.jump_counter < 0:
                    neg = -1
                self.y -= neg * (self.jump_counter ** 2) * 0.5
                self.jump_counter -= 1
                self.walk_counter += 1
            else:
                self.is_jumping = False
                self.jump_counter = self.jump_height
                self.walk_counter = 0

    def stand(self):
        self.is_standing = True
        self.walk_counter = 0

    def look_left(self):
        self.left = True
        self.right = False

    def look_right(self):
        self.left = False
        self.right = True

    def move_left(self):
        self.look_left()
        self.is_standing = False
        self.x -= self.speed
        if self.walk_counter < 20:
            self.walk_counter += 1
        else:
            self.walk_counter = 0

    def move_right(self):
        self.look_right()
        self.is_standing = False
        self.x += self.speed
        if self.walk_counter < 20:
            self.walk_counter += 1
        else:
            self.walk_counter = 0
