import pygame

from Npc import Npc


class Player(Npc):
    _jump = [
        pygame.image.load('images/Player/Jump__000.png'), pygame.image.load('images/Player/Jump__001.png'),
        pygame.image.load('images/Player/Jump__002.png'), pygame.image.load('images/Player/Jump__003.png'),
        pygame.image.load('images/Player/Jump__004.png'), pygame.image.load('images/Player/Jump__005.png'),
        pygame.image.load('images/Player/Jump__006.png'), pygame.image.load('images/Player/Jump__007.png'),
        pygame.image.load('images/Player/Jump__008.png'), pygame.image.load('images/Player/Jump__009.png')
    ]

    _run = [
        pygame.image.load('images/Player/Run__000.png'), pygame.image.load('images/Player/Run__001.png'),
        pygame.image.load('images/Player/Run__002.png'), pygame.image.load('images/Player/Run__003.png'),
        pygame.image.load('images/Player/Run__004.png'), pygame.image.load('images/Player/Run__005.png'),
        pygame.image.load('images/Player/Run__006.png'), pygame.image.load('images/Player/Run__007.png'),
        pygame.image.load('images/Player/Run__008.png'), pygame.image.load('images/Player/Run__009.png')
    ]

    _idle = pygame.image.load('images/Player/Idle__000.png')

    scaling = 0.2

    for image in _jump:
        _jump[_jump.index(image)] = pygame.transform.scale(image, (int( 362 * scaling), int(438 * scaling)))

    for image in _run:
        _run[_run.index(image)] = pygame.transform.scale(image, (int( 363 * scaling), int(458 * scaling)))

    _idle = pygame.transform.scale(_idle, (int( 232 * scaling), int(439 * scaling)))

    def __init__(self, x, y):
        super().__init__(x, y, width=504 * self.scaling, height=522 * self.scaling, speed=10, jump_height=10)

    def draw(self, win):
        if self.is_jumping:
            if self.right:
                win.blit(self._jump[(self.walk_counter // 2) - 1], (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self._jump[(self.walk_counter // 2) - 1], 1, 0), (self.x, self.y))
        elif self.is_standing:
            if self.right:
                win.blit(self._idle, (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self._idle, 1, 0), (self.x, self.y))
        else:
            if self.right:
                win.blit(self._run[(self.walk_counter // 2) - 1], (self.x, self.y))
            else:
                win.blit(pygame.transform.flip(self._run[(self.walk_counter // 2) - 1], 1, 0), (self.x, self.y))

