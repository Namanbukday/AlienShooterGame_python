# CREATING A SETTING CLASS TO PUT ALL THE SETTINGS AT ONE PLACE
# SO WE DON'T HAVE TO  CHANGE THE CODE TO CHANGE THE SETTINGS

class Settings():
    """ A class to store all settings"""

    def __init__(self):
        """ initialize game settings """
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (127, 255, 212)  # AQUAMARINE

        # SHIP SETTINGS :
        self.ship_speed_factor = 1.5
