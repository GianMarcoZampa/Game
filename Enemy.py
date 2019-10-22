import pygame

from Npc import Npc


class Enemy(Npc):
    _walk = [
        pygame.image.load('images/Enemy/Male/Walk (1).png'), pygame.image.load('images/Enemy/Male/Walk (2).png'),
        pygame.image.load('images/Enemy/Male/Walk (3).png'), pygame.image.load('images/Enemy/Male/Walk (4).png'),
        pygame.image.load('images/Enemy/Male/Walk (5).png'), pygame.image.load('images/Enemy/Male/Walk (6).png'),
        pygame.image.load('images/Enemy/Male/Walk (7).png'), pygame.image.load('images/Enemy/Male/Walk (8).png'),
        pygame.image.load('images/Enemy/Male/Walk (9).png'), pygame.image.load('images/Enemy/Male/Walk (10).png')
    ]

    _idle = pygame.image.load('images/Enemy/Male/Walk (9).png')

    scaling = 0.17

    # Resizing of all sprites to adapt screen size
    for image in _walk:
        _walk[_walk.index(image)] = pygame.transform.scale(image, (int(430 * scaling), int(519 * scaling)))

    _idle = pygame.transform.scale(_idle, (int(430 * scaling), int(519 * scaling)))

    def __init__(self, x, y):
        super().__init__(x, y, width=int(430 * self.scaling), height=int(519 * self.scaling),
                         speed=5, life=150, jump_frames=0, shot_frames=0)

    def draw(self, win):
        if self.is_running:
            self.walk_draw(win)
        else:
            self.stand_draw(win)

    def walk_draw(self, win):
        if self.right:
            win.blit(self._walk[self.walk_counter - 1], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._walk[self.walk_counter - 1], 1, 0), (self.x, self.y))

    def stand_draw(self, win):
        if self.right:
            win.blit(self._idle, (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._idle, 1, 0), (self.x, self.y))

