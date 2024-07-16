class GameStats:
    """Track stats"""
    def __init__(self):
        """Initialize stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
