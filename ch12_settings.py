# CREATING A SETTING CLASS TO PUT ALL THE SETTINGS AT ONE PLACE
# SO WE DON'T HAVE TO  CHANGE THE CODE TO CHANGE THE SETTINGS

class Settings():
    """ A class to store all settings"""

    def __init__(self):
        """ initialize game settings """
        # SCREEN SETTINGS :
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (127, 255, 212)  # AQUAMARINE

        # SHIP SETTINGS :
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        # BULLET SETTINGS :
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # ALIEN SETTINGS :
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10

        # FLEET DIRECTION OF '1' REPRESENTS MOVING RIGHT
        # '-1' REPRESENTS LEFT
        self.fleet_direction = 1
