class Settings:
    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen налаштування
        self.screen_width = 1080
        self.screen_height = 690
        self.bg_color = (51, 102, 255)

        # Налаштування корабля
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Налаштування кулі
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_alowed = 3

        # Налаштування прибульця
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet direction 1 означає напрямок руху праворучж -1 -- ліворуч.
        self.fleet_direction = 1 
         