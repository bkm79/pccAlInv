import sys

import pygame

def run_game():
    """инициализация и создание объекта экрана"""
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    
    """запуск основного цикла"""
    while True:
        #отслеживание событий клавы и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #отображение последего отрисованного экрана
        pygame.display.flip()
        
run_game()
