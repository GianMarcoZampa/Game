import pygame


class Ammo:
    _kunai = pygame.image.load('images/Player/Kunai.png')

    scaling = 0.2

    _kunai = pygame.transform.scale(_kunai, (int(32 * scaling), int(160 * scaling)))
    _kunai = pygame.transform.rotate(_kunai, 270)

    def __init__(self, x, y, left):
        self.speed = 40
        self.x, self.y = x, y
        self.width, self.height = int(160*self.scaling), int(32*self.scaling)
        self.left, self.right = left, not left
        self.damage = 20

    def move(self):
        if self.left:
            self.x -= self.speed
        else:
            self.x += self.speed

    def draw(self, win):
        if self.left:
            win.blit(pygame.transform.rotate(self._kunai, 180), (self.x, self.y))
        else:
            win.blit(self._kunai, (self.x, self.y))