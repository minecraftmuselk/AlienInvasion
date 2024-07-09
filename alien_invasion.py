import sys

import pygame

from settings import Settings


class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        """Initialize game, create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # Set BG
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main loop"""
        while True:
            # Keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw screen
            self.screen.fill(self.settings.bg_color)

            # Make most recently drawn screen
            pygame.display.flip()
            self.clock.tick(60)


if __name__ == '__main__':
    # Make a game instance
    ai = AlienInvasion()
    ai.run_game()
