import pygame

from Npc import Npc


class Enemy(Npc):
    _walk_male = [
        pygame.image.load('images/Enemy/Male/Walk (1).png'), pygame.image.load('images/Enemy/Male/Walk (2).png'),
        pygame.image.load('images/Enemy/Male/Walk (3).png'), pygame.image.load('images/Enemy/Male/Walk (4).png'),
        pygame.image.load('images/Enemy/Male/Walk (5).png'), pygame.image.load('images/Enemy/Male/Walk (6).png'),
        pygame.image.load('images/Enemy/Male/Walk (7).png'), pygame.image.load('images/Enemy/Male/Walk (8).png'),
        pygame.image.load('images/Enemy/Male/Walk (9).png'), pygame.image.load('images/Enemy/Male/Walk (10).png')
    ]

    _dead_male = [
        pygame.image.load('images/Enemy/Male/Dead (1).png'), pygame.image.load('images/Enemy/Male/Dead (2).png'),
        pygame.image.load('images/Enemy/Male/Dead (3).png'), pygame.image.load('images/Enemy/Male/Dead (4).png'),
        pygame.image.load('images/Enemy/Male/Dead (5).png'), pygame.image.load('images/Enemy/Male/Dead (6).png'),
        pygame.image.load('images/Enemy/Male/Dead (7).png'), pygame.image.load('images/Enemy/Male/Dead (8).png'),
        pygame.image.load('images/Enemy/Male/Dead (9).png'), pygame.image.load('images/Enemy/Male/Dead (10).png')
    ]

    _idle_male = pygame.image.load('images/Enemy/Male/Idle (9).png')

    _walk_female = [
        pygame.image.load('images/Enemy/Female/Walk (1).png'), pygame.image.load('images/Enemy/Female/Walk (2).png'),
        pygame.image.load('images/Enemy/Female/Walk (3).png'), pygame.image.load('images/Enemy/Female/Walk (4).png'),
        pygame.image.load('images/Enemy/Female/Walk (5).png'), pygame.image.load('images/Enemy/Female/Walk (6).png'),
        pygame.image.load('images/Enemy/Female/Walk (7).png'), pygame.image.load('images/Enemy/Female/Walk (8).png'),
        pygame.image.load('images/Enemy/Female/Walk (9).png'), pygame.image.load('images/Enemy/Female/Walk (10).png')
    ]

    _dead_female = [
        pygame.image.load('images/Enemy/Female/Dead (1).png'), pygame.image.load('images/Enemy/Female/Dead (2).png'),
        pygame.image.load('images/Enemy/Female/Dead (3).png'), pygame.image.load('images/Enemy/Female/Dead (4).png'),
        pygame.image.load('images/Enemy/Female/Dead (5).png'), pygame.image.load('images/Enemy/Female/Dead (6).png'),
        pygame.image.load('images/Enemy/Female/Dead (7).png'), pygame.image.load('images/Enemy/Female/Dead (8).png'),
        pygame.image.load('images/Enemy/Female/Dead (9).png'), pygame.image.load('images/Enemy/Female/Dead (10).png')
    ]

    _idle_female = pygame.image.load('images/Enemy/Female/Idle (9).png')

    scaling = 0.17

    # Resizing of all sprites to adapt screen size
    for image in _walk_male:
        _walk_male[_walk_male.index(image)] = pygame.transform.scale(image, (int(430 * scaling), int(519 * scaling)))

    _idle_male = pygame.transform.scale(_idle_male, (int(430 * scaling), int(519 * scaling)))

    for image in _dead_male:
        _dead_male[_dead_male.index(image)] = pygame.transform.scale(image, (int(629 * scaling), int(526 * scaling)))

    for image in _walk_female:
        _walk_female[_walk_female.index(image)] = pygame.transform.scale(image,
                                                                         (int(430 * scaling), int(519 * scaling)))

    _idle_female = pygame.transform.scale(_idle_female, (int(430 * scaling), int(519 * scaling)))

    for image in _dead_female:
        _dead_female[_dead_female.index(image)] = pygame.transform.scale(image,
                                                                         (int(629 * scaling), int(526 * scaling)))

    def __init__(self, x, y, male):
        super().__init__(x, y, width=int(430 * self.scaling), height=int(519 * self.scaling),
                         speed=5, life=150, jump_frames=0, shot_frames=0, dead_frames=10)
        self.male = male

    def draw(self, win):
        if self.is_dying:
            self.dead_draw(win)
        elif self.is_running:
            self.walk_draw(win)
        else:
            self.stand_draw(win)

    def walk_draw(self, win):
        if self.right:
            if self.male:
                win.blit(self._walk_male[self.walk_counter - 1], (self.x, self.y))
            else:
                win.blit(self._walk_female[self.walk_counter - 1], (self.x, self.y))
        else:
            if self.male:
                win.blit(pygame.transform.flip(self._walk_male[self.walk_counter - 1], 1, 0), (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self._walk_female[self.walk_counter - 1], 1, 0), (self.x, self.y))

    def stand_draw(self, win):
        if self.right:
            if self.male:
                win.blit(self._idle_male, (self.x, self.y))
            else:
                win.blit(self._idle_female, (self.x, self.y))
        else:
            if self.male:
                win.blit(pygame.transform.flip(self._idle_male, 1, 0), (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self._idle_female, 1, 0), (self.x, self.y))

    def dead_draw(self, win):
        y = self.y + 7
        if self.right:
            if self.male:
                win.blit(self._dead_male[self.shot_counter - 1], (self.x, y))
            else:
                win.blit(self._dead_female[self.shot_counter - 1], (self.x, y))
        else:
            if self.male:
                win.blit(pygame.transform.flip(self._dead_male[10 - self.dead_frames], 1, 0), (self.x, y))
            else:
                win.blit(pygame.transform.flip(self._dead_female[10 - self.dead_frames], 1, 0), (self.x, y))
