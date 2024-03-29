import pygame

from pygame.sprite import Sprite


class Alien(Sprite):
    """ A class to represent a single alien fleet"""

    def __init__(self, ai_settings, screen):
        """ Initialize alien and its starting point """

        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('C:/Users/nbukd/Desktop/PROJECTS/my_game/images/alien.bmp')
        self.rect = self.image.get_rect()

        # START EACH NEW ALIEN NEAR THE TOP LEFT OF THE SCREEN :

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # STORE THE ALIEN'S EXACT POSITION :

        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return true if alien is at the edge of the screen """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """move aliens right or left :"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """ Draw the alien at its current position"""

        self.screen.blit(self.image, self.rect)
