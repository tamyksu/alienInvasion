import pygame.image


class Settings:
    """"""

    def __init__(self):
        """"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg = pygame.image.load('images/cloud.jpg')

        self.bg = pygame.transform.scale(self.bg, (self.screen_width, self.screen_height))
        self.ship_speed = 3
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_allowed = 3
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.fleet_direction = 1