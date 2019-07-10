# AN ALIEN INVASION :

# STARTING THE GAME PROJECT :

# CREATING A PYGAME WINDOW AND RESPONDING TO USER INPUTS :

import sys

import pygame


def run_game():
    # initailize game nad create the 'screen' object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("ALIEN INVASION")

    # starts the main game controlling loop for the game
    while True:
        # write an event loop to watch for the keyboard and mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # make the most recently drawn screen visible
        pygame.display.flip()


run_game()
