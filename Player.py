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

    _throw = [
        pygame.image.load('images/Player/Throw__000.png'), pygame.image.load('images/Player/Throw__001.png'),
        pygame.image.load('images/Player/Throw__002.png'), pygame.image.load('images/Player/Throw__003.png'),
        pygame.image.load('images/Player/Throw__004.png'), pygame.image.load('images/Player/Throw__005.png'),
        pygame.image.load('images/Player/Throw__006.png'), pygame.image.load('images/Player/Throw__007.png'),
        pygame.image.load('images/Player/Throw__008.png'), pygame.image.load('images/Player/Throw__009.png')
    ]

    _dead = [
        pygame.image.load('images/Player/Dead__000.png'), pygame.image.load('images/Player/Dead__001.png'),
        pygame.image.load('images/Player/Dead__002.png'), pygame.image.load('images/Player/Dead__003.png'),
        pygame.image.load('images/Player/Dead__004.png'), pygame.image.load('images/Player/Dead__005.png'),
        pygame.image.load('images/Player/Dead__006.png'), pygame.image.load('images/Player/Dead__007.png'),
        pygame.image.load('images/Player/Dead__008.png'), pygame.image.load('images/Player/Dead__009.png')
    ]

    _attack = [
        pygame.image.load('images/Player/Attack__000.png'), pygame.image.load('images/Player/Attack__001.png'),
        pygame.image.load('images/Player/Attack__002.png'), pygame.image.load('images/Player/Attack__003.png'),
        pygame.image.load('images/Player/Attack__004.png'), pygame.image.load('images/Player/Attack__005.png'),
        pygame.image.load('images/Player/Attack__006.png'), pygame.image.load('images/Player/Attack__007.png'),
        pygame.image.load('images/Player/Attack__008.png'), pygame.image.load('images/Player/Attack__009.png')
    ]

    _idle = pygame.image.load('images/Player/Idle__000.png')

    scaling = 0.2

    # Resizing of all sprites to adapt screen size
    for image in _jump:
        _jump[_jump.index(image)] = pygame.transform.scale(image, (int(362 * scaling), int(438 * scaling)))

    for image in _run:
        _run[_run.index(image)] = pygame.transform.scale(image, (int(363 * scaling), int(458 * scaling)))

    for image in _throw:
        _throw[_throw.index(image)] = pygame.transform.scale(image, (int(363 * scaling), int(458 * scaling)))

    for image in _dead:
        _dead[_dead.index(image)] = pygame.transform.scale(image, (int(482 * scaling), int(498 * scaling)))

    for image in _attack:
        _attack[_attack.index(image)] = pygame.transform.scale(image, (int(536 * scaling), int(495 * scaling)))

    _idle = pygame.transform.scale(_idle, (int(232 * scaling), int(439 * scaling)))

    def __init__(self, x, y):
        super().__init__(x, y, width=int(232 * self.scaling), height=int(439 * self.scaling), speed=15, life=200,
                         damage=40, knockback=30, attack_frames=10, jump_frames=10, shot_frames=10, dead_frames=10)
        self.power_score = 200
        self.kill_count = 0

    def draw(self, win):
        if self.is_dying:
            self.dead_draw(win)
        elif self.is_jumping:
            self.jump_draw(win)
        elif self.is_throwing:
            self.throw_draw(win)
        elif self.is_attacking:
            self.attack_draw(win)
        elif self.is_running:
            self.run_draw(win)
        else:
            self.stand_draw(win)
        self.health_bar_draw(win)
        self.score_draw(win)

    def jump_draw(self, win):
        if self.right:
            win.blit(self._jump[self.jump_counter - 1], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._jump[self.jump_counter - 1], 1, 0), (self.x, self.y))

    def run_draw(self, win):
        if self.right:
            win.blit(self._run[self.walk_counter - 1], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._run[self.walk_counter - 1], 1, 0), (self.x, self.y))

    def throw_draw(self, win):
        if self.right:
            win.blit(self._throw[self.shot_counter - 1], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._throw[self.shot_counter - 1], 1, 0), (self.x, self.y))

    def stand_draw(self, win):
        if self.right:
            win.blit(self._idle, (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._idle, 1, 0), (self.x, self.y))

    def dead_draw(self, win):
        if self.right:
            win.blit(self._dead[10 - self.dead_frames], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._dead[10 - self.dead_frames], 1, 0), (self.x, self.y))

    def attack_draw(self, win):
        if self.right:
            win.blit(self._attack[self.attack_counter], (self.x, self.y))
        else:
            win.blit(pygame.transform.flip(self._attack[self.attack_counter], 1, 0), (self.x, self.y))

    def health_bar_draw(self, win):
        green, red = self.health_bar()
        pygame.draw.rect(win, (255, 0, 0), red)
        pygame.draw.rect(win, (0, 255, 0), green)
        pygame.draw.rect(win, (0, 0, 0), red, 1)

    def score_draw(self, win):
        score_percent = self.score / self.power_score
        text = pygame.font.Font('freesansbold.ttf', 20).render('Power', True, (0, 0, 255))
        if score_percent >= 1:
            score_percent = 1
            text = pygame.font.Font('freesansbold.ttf', 20).render('Power', True, (255, 0, 0))
        pygame.draw.rect(win, (255, 200, 0), (10, 10, 100 * score_percent, 25))
        pygame.draw.rect(win, (0, 0, 0), (10, 10, 100, 25), 2)
        win.blit(text, (30, 14))

    def use_power_1(self):
        if self.score >= self.power_score:
            self.score -= self.power_score
            self.life += 20
            if self.life > self.life_max:
                self.life = self.life_max
