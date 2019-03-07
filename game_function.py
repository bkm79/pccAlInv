import sys

import pygame

def check_events():
    """track keyboard event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update screen"""
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    #redraw screen
    pygame.display.flip()