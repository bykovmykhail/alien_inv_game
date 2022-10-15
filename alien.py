import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Клас, що представляє одного прибульця з флоту"""
    def __init__(self, ai_game):
        """Ініціалізувати проибульця та задати його початкове розташування"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Завантажити малюнок прибульця и налаштування rect атрибутов.
        self.image = pygame.image.load('alien_inv_game/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Запуск каждого нового пришельца зліва нагорі екрану.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение горизонтальной позиции.
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Повертає істину, якщо прибулець знаходиться на краю екрана."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Змістити прибульця праворуч чи ліворуч"""
        self.x += (self.settings.alien_speed * 
                   self.settings.fleet_direction)
        self.rect.x = self.x
        