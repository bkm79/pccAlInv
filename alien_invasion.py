import sys
import pygame

from settings import Settings
from ship import Ship

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
        #track keyboard event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #update screen
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        
        #redraw screen
        pygame.display.flip()
        
run_game()
