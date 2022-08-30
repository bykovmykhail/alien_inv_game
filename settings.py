class Settings:
    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen налаштування
        self.screen_width = 1100
        self.screen_height = 680
        self.bg_color = (51, 102, 255)
        self.ship_speed = 1.5

        # Налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_alowed = 3
         