import random
import time

import pygame as pg
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.player_velocity = [0, 0]  # Скорость по X и Y
        self.image = pg.image.load('images/palyer.bmp')
        self.rect = self.image.get_rect()
        self.rect.x = game.width // 2
        self.rect.y = game.height // 2
        self.size = self.rect.width
        self.coins = 0


    def control(self):
        # Обновление позиции персонажа
            self.rect.x += self.player_velocity[0]
            self.rect.y += self.player_velocity[1]
            # Ограничение движения персонажа внутри игрового окна с учётом стен
            self.rect.x = max(self.game.wall, min(self.rect.x, self.game.width - self.size - self.game.wall))
            self.rect.y = max(self.game.wall, min(self.rect.y, self.game.height - self.size - self.game.wall))

    def blitme(self):
            self.screen.blit(self.image, self.rect)
