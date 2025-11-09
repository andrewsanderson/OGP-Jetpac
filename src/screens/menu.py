import pygame
from src.ui.menu_item import MenuItem
from src.ui.text import Text
from src.ui.layout import Layout


class Menu:
    """Main menu screen."""
    
    def __init__(self, screen: pygame.Surface):
        """
        Initialize the menu.
        
        Args:
            screen: The pygame surface to render to
        """
        self.screen = screen
        
        # Create centered layout covering the full screen
        self.layout = Layout(
            x=0, y=0,
            width=800, height=600,
            vertical='center',
            horizontal='center',
            child_orientation='column',
            spacing=30
        )
        
        # Create text components
        self.one_player_text = MenuItem("1   ONE PLAYER")
        self.two_players_text = MenuItem("2   TWO PLAYERS")
        self.keyboard_text = MenuItem("3   KEYBOARD")
        self.joycon_text = MenuItem("4   JOYCON")
        self.start_game_text = MenuItem("5   START GAME")
        
        # Add texts to layout
        self.layout.add_child(self.one_player_text)
        self.layout.add_child(self.two_players_text)
        self.layout.add_child(self.keyboard_text)
        self.layout.add_child(self.joycon_text)
        self.layout.add_child(self.start_game_text)
    
    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Handle pygame events.
        
        Args:
            event: The pygame event to handle
            
        Returns:
            True to continue, False to quit
        """
        if event.type == pygame.QUIT:
            return False
        return True
    
    def update(self):
        """Update the menu state."""
        self.layout.update()
    
    def render(self):
        """Render the menu."""
        # Clear screen with black background
        self.screen.fill((0, 0, 0))
        
        # Render the layout (which renders all children)
        self.layout.render(self.screen)

