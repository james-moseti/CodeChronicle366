class Gamestats():
    """Track statistics for alien invasion. """
    
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        
    def reset_stats(self):
        """Initialize that can change during the game. """
        self.ship_left = self.settings.ship_limit