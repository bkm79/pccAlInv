import pygame

class Ship():
    
    def __init__(self, screen):
        """ Инициализирует корабль и задает его начальную позицию"""
        
        self.screen = screen
        
        #загруза изображения корабля и получение прямоугольника
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Корабль появляется внизу экрана в центре
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
    def blitme(self):
        #Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
