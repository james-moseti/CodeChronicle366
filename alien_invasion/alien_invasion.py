import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion():
    """Overall class to manage game assets and behavior. """
    
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Below is an implementation of the fullscreen mode of the game but I personally didn't want to use it. 
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN) # Defines the dimensions of the game window also surface
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        

    def run_game(self):
        # Start the main loop for the game. 
        while True:
            self._check_events()    # Refactored our code to make it more manageable
            self._update_screen()   # Helps to keep our run_game() method clean and easy to read
            self.bullets.update()
            
            # Get rid of bullets that have disappeared.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print
            
            self.ship.update()
            self.clock.tick(60)
    
    def _check_events(self):
        # Respond to keypresses and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)   # Refactored our code to make it more manageable
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)     # Refactored our code to make it more manageable

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen. """
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
                    
        # Make the most recently drawn screen visible.
        pygame.display.flip()
        
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group. """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)
        
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
        # Move the ship to the right. 
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
            
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
        # Move the ship to the right. 
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()