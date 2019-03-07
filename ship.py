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
        
        #Флаги перемещения
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ship position refresh"""
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
        
    def blitme(self):
        #Рисует корабль в текущей позиции
        self.screen.blit(self.image, self.rect)
