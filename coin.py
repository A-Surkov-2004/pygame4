import random
import time

import pygame
from pygame.sprite import Sprite

class Coin(Sprite):
    def __init__(self,game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.image = pygame.image.load('images/coin.bmp')
        self.rect = self.image.get_rect()
        self.spawntime = time.time()
        self.rect.x = random.random() * game.width % (game.width - self.rect.width)
        self.rect.y = random.random() * game.height % (game.width - self.rect.height)

    def activate(self):
        self.game.coins += 1



