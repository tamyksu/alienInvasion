import sys

import pygame

from settings import Settings
from ship import Ship
from alien import Alien
from bullet import Bullet

class AlienInvasion:
    """class """

    def __init__(self):
        """Initilize game"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invesion")

        self.ship = Ship(self)
        #self.alien = Alien(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def run_game(self):
        """main loop"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
            self._update_aliens()

    def _check_events(self):
        """Respond to keypress and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up(event)

    def _check_key_down(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_f:
            self._check_key_f()
        elif event.key == pygame.K_ESCAPE:
            self._check_key_esc()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_f(self):
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = 2000
        self.settings.screen_height = 1000

    def _check_key_esc(self):
        self.settings.screen_width = 1200
        self.settings.screen_height = 800
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

    def _fire_bullet(self):
        """create new bullet add it to group"""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_key_up(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_aliens(self):
        self._check_fleet_edge()
        self.aliens.update()

    def _update_bullets(self):
        self.bullets.update()
        # get rid of the bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_fleet(self):
        rows = 3
        colums = 6
        for row in range(rows):
            for item in range(colums):
                alien = Alien(self,70+ item * 200, 100+row*100)
                self.aliens.add(alien)

    def _check_fleet_edge(self):
        """is any aliens reach to edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Change the direction"""
        for alien in self.aliens.sprites():
           alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_screen(self):
        """update images on the screen"""
        self.screen.blit(self.settings.bg, (0, 0))
        self.ship.blimate()
        #self.alien.blimate()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()

