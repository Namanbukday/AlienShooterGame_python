# AN ALIEN INVASION :

# STARTING THE GAME PROJECT :

# CREATING A PYGAME WINDOW AND RESPONDING TO USER INPUTS :

# import sys

import pygame

# FROM SETTINGS.PY, WE IMPORT THE SETTINGS CLASS
from ch12_settings import Settings

from ch12_ship import Ship

import ch12_game_functions as gf


def run_game():
    # initialize game nad create the 'screen' object
    pygame.init()

    # MAKING AN INSTANCE OF SETTINGS CLASS TO USE ITS ATTRIBUTES
    ai_settings = Settings()

    # WE USE ATTRIBUTES OF ai_settings LIKE SCREEN_HEIGHT AND SCREEN_WIDTH TO SET SCREEN COLOR
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("ALIEN INVASION")

    # set background color
    # bg_color = (127, 255, 212)  # aquamarine

    # MAKE A SHIP
    # MAKING AN INSTANCE OF THE CLASS SHIP
    ship = Ship(ai_settings, screen)  # SENDING 2 INSTANCES IN THE ARGUMENT

    # starts the main game controlling loop for the games
    while True:
        '''# write an event loop to watch for the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()'''
        gf.check_events(ship)  # calling func through an instance
        '''# Redraw screen during each pass through the loop
        # And setting the screen color
        screen.fill(ai_settings.bg_color)  # USED INSTANCE TO CHANGE THE COLOR

        # MAKING SHIP ON THE SCREEN
        ship.blitme()

        # make the most recently drawn screen visible
        pygame.display.flip()'''
        ship.update()
        gf.update_screen(ai_settings, screen, ship)  # TO UPDATE THE SCREEN


run_game()
