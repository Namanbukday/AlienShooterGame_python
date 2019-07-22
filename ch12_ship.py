import pygame


class Ship():
    def __init__(self,ai_settings, screen):
        """initialize the ship and its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

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

        # STORE A DECIMAL VALUE FOR THE SHIP'S CENTER
        # (as 'rect' attributes only store integer values)
        self.center = float(self.rect.centerx)

        #   MOVEMENTS FLAG
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """update the ship's position based on movement flag"""
        # UPDATING THE SHIP'S CENTER VALUE NOT THE RECT ATTRIBUTE
        if self.moving_right and self.rect.right < self.screen_rect.right:
            """if the self.moving flag is 'true' AND the 'x-coordinate' of right edge(side) of the ship(rect)
            is less than the right edge of the screen_rect,then it'll move right"""
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            """if the self.moving_left falg is 'true' and the x-coordinate of the left edge (side) of the ship(rect)
            is less greater than 'zero'(the origin the screen), then ship will move right"""
            self.center -= self.ai_settings.ship_speed_factor

        # UPDATE THE SHIP'S RECT ATTRIBUTE
        self.rect.centerx = self.center  # ONLY THE INTEGER PART OF THE SELF.CENTER WILL BE SAVED IN RECT.CENTERX

    def blitme(self):
        """ draw the ship at the current position specified by self.rect"""
        self.screen.blit(self.image, self.rect)

    def ship_center(self):
        """Center the ship on the screen"""
        self.center = self.screen_rect.centerx
