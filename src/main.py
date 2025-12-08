import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.settings.settings import Settings
from src.settings.scores import Scores
from src.scenes.main_menu import MainMenu
from typing import Literal
import pygame

LocationType = Literal['main_menu', 'level_one']

class Main:
    def __init__(self):
        self.location: LocationType = 'main_menu'
        self.settings = Settings()
        self.scores = Scores()
        
        # Initialize pygame
        pygame.init()
        
        # Create screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("OGP Jetpac")
        
        # Create main menu
        self.main_menu = MainMenu(self.screen)
    
    def render_main_menu(self):
        """Render the main menu."""
        self.main_menu.render()
        pygame.display.flip()
    
    def run(self):
        """Run the main game loop."""
        clock = pygame.time.Clock()
        running = True
        
        while running:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            
            # Render based on current location
            if self.location == 'main_menu':
                self.render_main_menu()
            
            # Control frame rate
            clock.tick(60)
        
        pygame.quit()


def main():
    """Entry point for the game."""
    game = Main()
    game.run()


if __name__ == "__main__":
    main()
