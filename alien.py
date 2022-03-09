import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self,ai_game, x,y):
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.image = pygame.image.load('images/alien.png')
        #self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.right= True
        #Start the alien near the top left of th screen
        self.rect.x = x
        self.rect.y = y

        #store the elians exact horizonal position
        self.x = float(self.rect.x)

    def blimate(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        screen_rect = self.screen.get_rect()
        """Move alien to the right"""
        if self.rect.right == self.settings.screen_width:
            self.right = False
        if self.rect.left == 0:
            self.right = True
        if self.right:
            self.x +=self.settings.alien_speed
            self.rect.x = self.x
        if self.right!=True:
            self.x -= self.settings.alien_speed
            self.rect.x = self.x


       # if self.rect.right >= screen_rect.
        #    self.x -= self.settings.alien_speed