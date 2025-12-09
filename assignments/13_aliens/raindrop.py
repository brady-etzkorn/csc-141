import pygame
from pygame.sprite import Sprite

# Image used is made my AI

class Raindrop(Sprite):
    '''A class to represent a single rain in the fleet'''

    def __init__(self, ai_game):
        '''Initialize the rain and set its starting position.'''
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the rain image and set its rect attribute.
        self.image = pygame.image.load("C:/Users/bre30/OneDrive/Desktop/csc 141/13_aliens/images/raindrop.bmp")
        self.rect = self.image.get_rect()

                # Start each new rain near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the rains exact horizontal position.
        self.y = float(self.rect.y)
        
    def check_edges(self):
        """Return True if rain is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        return False
    
    def update(self):
        self.y += 1 
        self.rect.y = self.y

        if self.rect.top >= self.screen.get_rect().bottom:
            self.rect.y = 0 
            self.y = 0
            