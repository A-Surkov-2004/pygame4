import time

import pygame
import sys

import coin
import player
import portal

# Инициализация Pygame
pygame.init()
# Параметры окна

FPS = 60
# Цвета
WHITE = (255, 255, 255)

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GOLD = (255, 150, 0)
GREEN = (0, 255, 0)
# Размеры персонажа и объектов
PLAYER_BORDER_THICKNESS = 2
OBJECT_SIZE = 50
WALL_THICKNESS = 5
# Скорость движения персонажа
PLAYER_SPEED = 5
# Инициализация окна
pygame.display.set_caption("Базовая заготовка 2D-игры")
clock = pygame.time.Clock()
# Переменные персонажа

# Неподвижные объекты
objects = [
pygame.Rect(200, 150, OBJECT_SIZE, OBJECT_SIZE),
pygame.Rect(400, 300, OBJECT_SIZE, OBJECT_SIZE),
pygame.Rect(600, 450, OBJECT_SIZE, OBJECT_SIZE)
]
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

C_RATE = 5


class Game:

    def __init__(self):
        self.wall = WALL_THICKNESS
        self.width = WINDOW_WIDTH
        self.height = WINDOW_HEIGHT
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        self.running = True
        self.player = player.Player(self)
        self.coins = pygame.sprite.Group()
        self.portals = pygame.sprite.Group()
        self.lstcoin = 0

        portal1 = portal.Portal(self, 'p1')
        self.portals.add(portal1)
        portal2 = portal.Portal(self, 'p1')
        self.portals.add(portal2)




    def run(self):

        # Основной игровой цикл
        while self.running:

            self.check_events()
            self.player.control()
            self._update_coins()
            self._update_portals()
            self.draw()

    def _update_coins(self):
        collisions = pygame.sprite.spritecollide(self.player, self.coins, True)
        if len(collisions) != 0:
            self.player.coins += 1

        if self.lstcoin + C_RATE < time.time():
            self.lstcoin = time.time()
            coin1 = coin.Coin(self)
            self.coins.add(coin1)


    def _update_portals(self):
        collisions = pygame.sprite.spritecollide(self.player, self.portals, False)
        if len(collisions) != 0:
            collisions[0].activate()



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.player_velocity[0] = -PLAYER_SPEED
                elif event.key == pygame.K_RIGHT:
                    self.player.player_velocity[0] = PLAYER_SPEED
                elif event.key == pygame.K_UP:
                    self.player.player_velocity[1] = -PLAYER_SPEED
                elif event.key == pygame.K_DOWN:
                    self.player.player_velocity[1] = PLAYER_SPEED
            elif event.type == pygame.KEYUP:
                if event.key in {pygame.K_LEFT, pygame.K_RIGHT}:
                    self.player.player_velocity[0] = 0
                elif event.key in {pygame.K_UP, pygame.K_DOWN}:
                    self.player.player_velocity[1] = 0



    def draw(self):
            # Рендеринг объектов
            self.screen.fill(WHITE)

            # Отрисовка стен
            pygame.draw.rect(self.screen, BLACK, (0, 0, WINDOW_WIDTH, WALL_THICKNESS)) # Верхняя стена
            pygame.draw.rect(self.screen, BLACK, (0, 0, WALL_THICKNESS, WINDOW_HEIGHT)) # Левая стена
            pygame.draw.rect(self.screen, BLACK, (0, WINDOW_HEIGHT - WALL_THICKNESS, WINDOW_WIDTH, WALL_THICKNESS)) # Нижняя стена
            pygame.draw.rect(self.screen, BLACK, (WINDOW_WIDTH - WALL_THICKNESS, 0, WALL_THICKNESS, WINDOW_HEIGHT)) # Правая стена

            self.coins.draw(self.screen)
            self.portals.draw(self.screen)
            self.player.blitme()

            # Обновление экрана

            self.display_UI()

            pygame.display.flip()
            clock.tick(FPS)



    def display_UI(self):
        f1size = 25
        f1 = pygame.font.Font(None, f1size)
        text1 = f1.render(f'Coins: {self.player.coins}', True,
                          GOLD)
        self.screen.blit(text1, (10, 10))


game = Game()
game.run()