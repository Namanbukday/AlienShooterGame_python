# ITS A MODULE CONTAINING DIFFERENT FUNCTIONS LIKE MOVING AND SCREEN UPDATION :

import sys
import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """update the image on the screen and flip to the new screen"""
    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP :
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # MAKE THE RECENTLY SCREEN VISIBLE :
    pygame.display.flip()