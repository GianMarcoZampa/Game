import pygame

from Enemy import Enemy


class EnemyGenerator:

    def __init__(self, x, y, delay, fps):
        self.x, self.y = x, y
        self.male = False
        self.wait_time_counter = 0
        self.enemy_rate = int(fps*delay)

    def generate(self):
        if self.wait_time_counter < self.enemy_rate:
            self.wait_time_counter += 1
        else:
            self.male = not self.male
            self.wait_time_counter = 0
            return Enemy(self.x, self.y, self.male)