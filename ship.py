import pygame

class Ship():
    
    def __init__(self, ai_settings, screen):
        """Initialize ship and set start position"""
        
        self.screen = screen
        self.ai_settings = ai_settings
        #load ship image and get rectangle
        self.image = pygame.image.load('Images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #spawn ship in bottom center
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        
        #Move flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ship position refresh"""
        if (self.moving_right and
            self.rect.right < self.screen_rect.right):
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center
        
    def blitme(self):
        #redraw ship
        self.screen.blit(self.image, self.rect)
