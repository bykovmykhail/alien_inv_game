import pygame.font

class Scoreboard:
    """Клас що виводить рахунок."""

    def __init__(self, ai_game):
        """Ініціалізація атрибутівб пов'язаних із рахунком."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для відображення рахунку.
        self.text_color = (255,250,250)
        self.font = pygame.font.SysFont(None, 48)

        # Підготувати зображення початкового рахунку. 
        self.prep_score()
        self.prep_hight_score()


    def prep_score(self):
        """Перетворити рахунок на зображення."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, 
                self.text_color, self.settings.bg_color)
        # Показати рахунок у верхньому правому куті екрана.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Показати рахунок на екрані."""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

    def prep_high_score(self):
        """Згенерувати рекорд у зображення"""
        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)

        # Відцентрувати рекорд по горизонталі
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top



