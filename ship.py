import pygame

class Ship:
    """Клас керування кораблем"""

    def __init__(self, ai_game):
        """Ініцілізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його rect 
        self.image = pygame.image.load('alien_inv_game/images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Створювати кожен новий корабель внизу екрана, по центру. 
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)
