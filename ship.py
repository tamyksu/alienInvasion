import pygame

class Ship:
    """Ship class"""

    def __init__(self, ai_game):
        """initilize ship"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        self.image =pygame.image.load('images/rocket.png')
        #self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update ship position based on movement flag"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #self.rect.x +=1
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            #self.rect.x -= 1
            self.x -= self.settings.ship_speed

        self.rect.x =self.x

    def blimate(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
