class GameStats:
    """Track statistics for Alien Invasion"""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        # Start game in an inactive state.
        self.game_active = False
        # High score should never be reset and should be read from high_score.txt.
        filename = 'high_score.txt'
        self.highest_score = 0
        with open(filename) as file_object:
            for line in file_object:
                if int(line) > self.highest_score:
                    self.highest_score = int(line)

        self.high_score = self.highest_score

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1