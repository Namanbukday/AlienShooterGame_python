class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.ships_left = 0
        self.reset_stats()

        # HIGH SCORE SHOULD NEVER RESET :
        self.high_score = 0

        # START ALIEN INVASION IN ACTIVE STATE :
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
