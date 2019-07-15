# CLASS OF BULLET

import pygame

from pygame.sprite import Sprite


class Bullet(Sprite):
    """ A class to manage bullets fired form the ship """

    def __init__(self, ai_settings, screen, ship):
        super().__init__()

        self.screen = screen

        # CREATE A BULLET 'RECT' AT (0,0) AND THEN SET CORRECT POSITION :
        # CREATE A RECT FOR THE BULLET:
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)

        # NOW,SET THE CORRECT POSITION FOR THE BULLET :
        self.rect.centerx = ship.rect.centerx  # TO MAKE THE BULLET COME OUT OF THE SHIP'S CENTER
        self.rect.top = ship.rect.top  # BULLET SHOULD COME OUT OF THE SHIP AT ITS TOP

        # STORE THE BULLET'S POSITION AS A DECIMAL VALUE :
        self.y = float(self.rect.y)

        # SETTING OTHER PROPERTIES OF THE BULLET :
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """ move the bullet up the screen """
        # IT CORRESPONDS TO A DECREASING 'Y - COORDINATE' VALUE, SO THE BULLET MOVES UP
        self.y -= self.speed_factor

        # UPDATE THE RECT POSITION :
        self.rect.y = self.y

    def draw_bullet(self):
        """ draw bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
