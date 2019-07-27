import pygame.font


class Button():

    def __init__(self, ai_settings, screen, msg):
        """Initialize the button attributes"""

        self.screen = screen
        self.screen_rect = screen.get_rect()

        # SET  THE DIMENSIONS AND THE PROPERTIES OF THE BUTTON :
        self.width, self.height = 200, 50
        self.button_color = (111, 123, 24)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)  # 'none' tells pygame to choose default font, and '48' = font size

        # BUILD THE BUTTON'S RECT OBJECT AND CENTER IT
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # THE BUTTON MESSAGE NEEDS TO BE PREPPED ONLY ONCE :
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """ Turn msg into 'RENDERED IMAGE' and center text on the button"""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # DRAW BLANK BUTTON AND THEN DRAW THE MESSAGE :
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
