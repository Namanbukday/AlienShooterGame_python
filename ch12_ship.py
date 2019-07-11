import pygame


class Ship():
    def __init__(self, screen):
        """initialize the ship and its starting position"""
        self.screen = screen

        # LOAD THE IMAGE
        self.image = pygame.image.load('C:/Users/nbukd/Desktop/PROJECTS/my_game/images/ship.bmp')

        # MAKE THE SHIP'S IMAGE RECTANGLE BY GET_RECT(),
        # AND STORE IT IN ANOTHER ATTRIBUTE SELF.RECT
        self.rect = self.image.get_rect()

        # MAKING THE SCREEN RECTANGLE AND STORING IT IN SELF.SCREE.RECT
        self.screen_rect = screen.get_rect()

        # START NEW SHIP AT THE BOTTOM CENTER OF THE SCREEN

        # MAKING X- COORDINATE OF SHIP'S CENTER = CENTER X ATTRIBUTE OF THE SCREEN'S RECT
        self.rect.centerx = self.screen_rect.centerx

        # MAKING Y-COORDINATE OF SHIP'S BOTTOM = BOTTOM ATTRIBUTE OF THE SCREEN'S RECT
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """ draw the ship at the current position specified by self.rect"""
        self.screen.blit(self.image, self.rect)
