# ITS A MODULE CONTAINING DIFFERENT FUNCTIONS LIKE MOVING AND SCREEN UPDATION :

import sys
import pygame

from ch12_bullet import Bullet


def check_events(ai_settings, screen, ship, bullets):
    """ responds to keypress and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship ,bullets)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, bullets):
    """update the image on the screen and flip to the new screen"""
    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP :
    screen.fill(ai_settings.bg_color)

    # REDRAW ALL BULLETS BEHIND SHIP AND ALIENS :
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # BUILT THE SHIP :
    ship.blitme()

    # MAKE THE RECENTLY SCREEN VISIBLE :
    pygame.display.flip()


def update_bullets(bullets):
    """ update positions of bullets and get rid of the old bullets"""
    # UPDATE BULLET'S POSITION :
    bullets.update()

    # GET RID OF THE BULLETS THAT HAVE DISAPPEARED :
    for bullet in bullets.copy():
        # WE USE COPY() METHOD BECAUSE YOU SHOULD NOT REMOVE ITEM FROM A LIST OR A GROUP WITHIN A 'FOR' LOOP.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)