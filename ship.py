import pygame

from settings import Settings

class Ship:
    """Клас керування кораблем"""

    def __init__(self, ai_game):
        """Ініцілізувати корабель та задати його початкову позицію"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
import pygame
 
class Ship:
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load('alien_inv_game/images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

        # Завантажити зображення корабля та отримати його rect 
        self.image = pygame.image.load('alien_inv_game/images/ship2.bmp')
        self.rect = self.image.get_rect()

        # Створювати кожен новий корабель внизу екрана, по центру. 
        self.rect.midbottom = self.settings.midbottom
        # Зберегти десяткове значення для позиції корабля по горизонталі.
        self.x = float(self.rect.x)
        # Індикатор руху
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """Оновити поточну позицію корабля на основі індикатора руху."""
        if self.moving_right:
            self.x += self.settings.ship_speed 
        elif self.moving_left:
            self.x -= self.settings.ship_speed
        # Оновити об`экт rect з self.x
        self.rect.x = self.x
        

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні."""
        self.screen.blit(self.image, self.rect)
