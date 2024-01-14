class Settings():
    """A class to store all settings for Alien Invasion. """
    
    def __init__(self):
        """Initialize the game's settings. """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230) # Light gray
        
        # Bullet settings
        self.bullet_speed = 3
        self.bullets_allowed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    # Dark gray
        
        # Set the ship's speed
        self.ship_speed = 3
        
        # Set the alien's speed
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10 # How quickly the fleet drops down the screen after an alien reaches the edge of the screen. 
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
        