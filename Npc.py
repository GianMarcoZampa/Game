import pygame

from Ammo import Ammo


class Npc:

    def __init__(self, x, y, width, height, speed, jump_frames, shot_frames):
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.speed = speed
        self.walk_counter = 0
        self.left, self.right = False, True
        self.is_running = False
        self.is_jumping = False
        self.is_throwing = False
        self.jump_counter = 0
        self.jc = self.jump_frames = jump_frames
        self.shot_counter, self.shot_frames = 0, shot_frames
        self.thrown_obj = []

    def jump(self):
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
        self.is_running = False
        self.walk_counter = 0

    def look_left(self):
        self.left = True
        self.right = False

    def look_right(self):
        self.left = False
        self.right = True

    def move_left(self):
        self.look_left()
        self.is_running = True
        self.x -= self.speed
        if self.walk_counter < 10:
            self.walk_counter += 1
        else:
            self.walk_counter = 0

    def move_right(self):
        self.look_right()
        self.is_running = True
        self.x += self.speed
        if self.walk_counter < 10:
            self.walk_counter += 1
        else:
            self.walk_counter = 0

    def throw(self):
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
                        Ammo(self.x + num * int(self.width*0.3), self.y + int(self.height*0.3), self.left))
            else:
                self.shot_counter = 0
                self.is_throwing = False
