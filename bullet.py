import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Class to manage bullets"""

    def __init__(self, ai_game):
        """Create bullet"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet as float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet up"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

