import sys

import pygame

def run_game():
    #инициализация и создание объекта экрана
    pygame.init()
    screen = pygame.display.set_mode((1200,800))
    pygame.display.set_caption("Alien Invasion")
    bg_color = (230, 230, 230)
    
    #запуск основного цикла
    while True:
        #отслеживание событий клавиатуры и мыши
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        #перерисовка экрана
        screen.fill(bg_color)
        
        #отображение последего отрисованного экрана
        pygame.display.flip()
        
run_game()
