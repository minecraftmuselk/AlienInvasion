import pygame


class Ship:
    """Class to manage ship"""

    def __init__(self, ai_game):
        """Initialize and set start"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start new ships at bottom
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Draw ship and current loc"""
        self.screen.blit(self.image, self.rect)
