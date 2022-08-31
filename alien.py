import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати проибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen

        # Завантажити малюнок прибульця и налаштування rect атрибутов.
        self.image = pygame.image.load('alien_inv_game/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Запуск каждого нового пришельца зліва нагорі екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение горизонтальной позиции.
        self.x = float(self.rect.x)
        