import sys
import pygame

from settings import Settings
from ship import Ship
import game_function as gf

def run_game():
    #Initialization and create screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_widht,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #create ship
    ship = Ship(screen)
    
    #main cycle
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings, screen, ship)


        
run_game()
