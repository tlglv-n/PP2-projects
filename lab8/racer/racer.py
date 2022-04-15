import random
import time
import sys
import pygame
from pygame.locals import *

pygame.init()
FPS = 60
clock = pygame.time.Clock()

# установка начальные данные: ширины, высоты, surface, font, music
W, H = 400, 600
speed = 0
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((W, H))
font_small = pygame.font.SysFont("Verdana", 20)
screen.fill(WHITE)
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.3)

# класс Enemy


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W - 40), 0)

    def move(self):  # функция движения
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > H):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def collision(self):   # функция коллизии
        pygame.mixer.music.stop()
        self.game_over_img = pygame.image.load("game_over.jpg")
        screen.blit(self.game_over_img, (0, 0))
        pygame.display.update()
        pygame.mixer.music.load("game_over_sound.mp3")
        pygame.mixer.music.play()

    def draw(self, surf):  # функция модельки
        surf.blit(self.image, self.rect)

# класс игрока


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):   # функция движения
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, (-5 - speed))
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, (5 + speed))

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip((-5 - speed), 0)
        if self.rect.right < W:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip((speed + 5), 0)

    def draw(self, surface):  # функция модельки игрока
        surface.blit(self.image, self.rect)


# класс монет
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, W-40), 0)
        self.score = 0

    def move(self):  # функция движения монет
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > H):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

    def collision(self):   # функция коллизии
        self.rect.center = (random.randint(25, 375), 20)
        self.score += 1
        global speed
        speed += 1

    def count(self):    # функция счетчика очков (собранных монет)
        self.counting = font_small.render(str(self.score), True, (0, 0, 0))
        screen.blit(self.counting, (370, 10))

    def total_score(self):    # функция вывода результата очков
        self.score = font_small.render(str(self.score), True, WHITE)
        screen.blit(self.score, (205, 401))
        pygame.display.update()

    def draw(self, surf):  # функция модельки монеты
        surf.blit(self.image, self.rect)


# класс сзаднего фона игры
class Background():
    def __init__(self):
        self.bg_image = pygame.image.load('AnimatedStreet.png')
        self.rect_bg_img = self.bg_image.get_rect()

        # задаем начальные координаты
        self.bg_y1 = 0
        self.bg_x1 = 0
        self.bg_y2 = self.rect_bg_img.height
        self.bg_x2 = 0

        self.moving_speed = 5

    def update(self):   # функция движения фона вниз по x, y координатам
        self.bg_y1 += self.moving_speed
        self.bg_y2 += self.moving_speed
        if self.bg_y1 >= self.rect_bg_img.height:
            self.bg_y1 = -self.rect_bg_img.height
        if self.bg_y2 >= self.rect_bg_img.height:
            self.bg_y2 = -self.rect_bg_img.height

    def render(self):   # render функция для фона
        screen.blit(self.bg_image, (self.bg_x1, self.bg_y1))
        screen.blit(self.bg_image, (self.bg_x2, self.bg_y2))


# переменные вызыва классов
Player = Player()
Enemy = Enemy()
Coin1 = Coin()
Coin2 = Coin()
Background = Background()

# создание групп для классов
enemies = pygame.sprite.Group()
enemies.add(Enemy)
money = pygame.sprite.Group()
money.add(Coin1)
money2 = pygame.sprite.Group()
money2.add(Coin2)
all_sprites = pygame.sprite.Group()
all_sprites.add(Player)
all_sprites.add(Enemy)
all_sprites.add(Coin1, Coin2)

done = False

# Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # движения моделек
    Background.update()
    Background.render()
    Player.update()
    Enemy.move()
    Coin1.move()
    Coin2.move()
    # отображение моделек на экран
    Player.draw(screen)
    Enemy.draw(screen)
    Coin1.draw(screen)
    Coin2.draw(screen)
    Coin1.count()  # счетчик очков
    Coin2.count()
    # коллизия между игроком и врагом
    if pygame.sprite.spritecollideany(Player, enemies):
        Enemy.collision()
        Coin1.total_score()
        time.sleep(7)
        pygame.quit()

    # коллизия между игроком и монетой
    if pygame.sprite.spritecollideany(Player, money):
        Coin1.collision()
        Coin1.count()
    if pygame.sprite.spritecollideany(Player, money2):
        Coin2.collision()
        Coin2.count()

    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
