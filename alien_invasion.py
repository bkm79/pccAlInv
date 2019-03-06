import sys

import pygame

from settings import Settings

def run_game():
    #инициализация и создание объекта экрана
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_widht,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    #запуск основного цикла
    while True:
        #отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #перерисовка экрана
        screen.fill(ai_settings.bg_color)
        
        #отображение последего отрисованного экрана
        pygame.display.flip()
        
run_game()
