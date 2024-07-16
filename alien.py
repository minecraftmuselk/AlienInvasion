import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Represents single alien"""
    def __init__(self, ai_game):
        """Initialize alien and set start"""
        super().__init__()
        self.screen = ai_game.screen

        # Load alien
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)