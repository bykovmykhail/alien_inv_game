import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Загальний клас, що керує ресурсами та поведінкою гри."""

    def __init__(self):
        """Ініціалізувати гру, створити ресурси гри"""
        pygame.init()
        self.settings = Settings()
        # Запуск гри у повноекранному режимі 
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        # Запуск гри у вікні
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Розпочати головний цикл гри."""
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()
                  

    def _check_events(self):
        # Слідкувати за подіями миші та клавіатури.
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self, event):
        """Редагувати на натискання клавіш"""            
        if event.key == pygame.K_RIGHT:
            # Перемістити корабель праворуч
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Перемістити корабель ліворуч
            self.ship.moving_left = True
        elif event.key == pygame.K_q  or event.key == pygame.K_ESCAPE:
            sys.exit()
            
    def _check_keyup_events(self, event):
        """Редагувати, коли клавіша не натиснута"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        # Наново перемалювати екран на кожній ітерації циклу.        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Показати осатнній намальований екран.
        pygame.display.flip()


if __name__ == '__main__':
    # Створити екземпляр гри та запустити гру.
    ai = AlienInvasion()
    ai.run_game()


  