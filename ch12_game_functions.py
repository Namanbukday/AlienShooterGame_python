# ITS A MODULE CONTAINING DIFFERENT FUNCTIONS LIKE MOVING AND SCREEN UPDATION :

import sys
import pygame

from ch12_bullet import Bullet  # FOR THE NEW INSTANCE
from ch13_alien import Alien  # FOR THE INSTANCE ALIEN
from time import sleep

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
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """update the image on the screen and flip to the new screen"""
    # REDRAW THE SCREEN DURING EACH PASS THROUGH THE LOOP :
    screen.fill(ai_settings.bg_color)

    # REDRAW ALL BULLETS BEHIND SHIP AND ALIENS :
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # BUILT THE SHIP :
    ship.blitme()

    # BUILT THE ALIEN :
    aliens.draw(screen)  # DRAW EACH ELEMENT PRESENT IN THE GROUP TO THE SCREEN

    # MAKE THE RECENTLY SCREEN VISIBLE :
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """ update positions of bullets and get rid of the old bullets"""
    # UPDATE BULLET'S POSITION :
    bullets.update()

    # GET RID OF THE BULLETS THAT HAVE DISAPPEARED :
    for bullet in bullets.copy():
        # WE USE COPY() METHOD BECAUSE YOU SHOULD NOT REMOVE ITEM FROM A LIST OR A GROUP WITHIN A 'FOR' LOOP.
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """ Responds to bullet-alien collisions"""

    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # DESTROYING EXISTING BULLETS AND CREATING A NEW FLEET
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if limit not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """determine the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x


def get_number_rows(ai_seetings, ship_height, alien_height):
    """determine the number of rows of alien that  fit on the screen."""
    available_space_y = (ai_seetings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):
    """ create the fleet of the aliens """

    # CREATE AN ALIEN AND FIND THE NUMBER OF ALIENS IN A ROW :
    # SPACING BETWEEN EACH ALIEN IS EQUAL TO ONE ALIEN WIDTH :

    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # CREATE THE FIRST ROW FOR THE ALIEN :
    for row_number in range(number_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """respond appropriately if any aliens have reached an edge """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """ Drop the entire fleet and change the fleet's direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """ Responds to ship being hit by alien"""
    if stats.ship_left > 0:
        # DECREMENT SHIP_LEFT
        stats.ship_left -= 1

        #  EMPTY THE LIST/GROUP OF ALIENS AND BULLETS
        aliens.empty()
        bullets.empty()

        # CREATE A NEW FLEET AND CENTER THE SHIP .
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()

        # PAUSE :
        sleep(0.5)

    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """ Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # TREAT THIS THE SAME AS IF THE SHIP HITS AN ALIEN
            ship_hit(ai_settings, stats,screen, ship, aliens, bullets)
            break


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """ Check if the fleet i at the edge.
        and then update the position of all the aliens in the fleet
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # LOOK FOR ALIENS HITTING THE BOTTOM OF THE SCREEN.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

    # LOOK FOR ALIEN-SHIP COLLISIONS.
    if pygame.sprite.spritecollideany(ship, aliens):
        print("MAYDAY!MAYDAY!! SHIP HIT!!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
