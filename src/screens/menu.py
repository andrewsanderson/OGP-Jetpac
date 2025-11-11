import pygame
from src.ui.menu_item import MenuItem
from src.ui.text import Text
from src.ui.layout import Layout
from src.ui.attributes.anchor import Anchor
from src.state.state import State


class Menu:
    """Main menu screen."""
    
    def __init__(self, screen: pygame.Surface, state: State):
        """
        Initialize the menu.
        
        Args:
            screen: The pygame surface to render to
            state: The game state
        """
        self.screen = screen
        self.state = state
        
        
        # Create centered layout covering the full screen
        # Root layout starts at (0, 0) and will be positioned by its parent anchor
        self.layout = Layout(
            width=800, height=600,
            parent=None,
            vertical_align='center',    
            horizontal_align='center',
            orientation='column',
        )
        # Set root layout position manually (no parent to position it)
        self.layout.location.set_position(0, 0)

        # Create anchor for menu layout - left-aligned items, vertically centered
        # The anchor's horizontal_align='left' makes items left-aligned
        # The anchor's vertical_align='center' centers the items vertically
        menu_anchor = Anchor('left', 'center', 0, 0)
        
        self.menu_layout = Layout(
            parent=self.layout,
            vertical_align='center',
            horizontal_align='left',
            orientation='column',
        )
        
        
        # Create text components with selection based on game state
        self.one_player_text = MenuItem("1   ONE PLAYER", is_selected=(self.state.players == '1'))
        self.two_players_text = MenuItem("2   TWO PLAYERS", is_selected=(self.state.players == '2'))
        self.keyboard_text = MenuItem("3   KEYBOARD", is_selected=(self.state.input == 'keyboard'))
        self.joycon_text = MenuItem("4   JOYCON", is_selected=(self.state.input == 'joycon'))
        self.start_game_text = MenuItem("5   START GAME", is_selected=False)
        
        # Add menu layout to main layout
        self.layout.children.add(self.menu_layout)
        
        # Add texts to menu layout
        self.menu_layout.children.add(self.one_player_text)
        self.menu_layout.children.add(self.two_players_text)
        self.menu_layout.children.add(self.keyboard_text)
        self.menu_layout.children.add(self.joycon_text)
        self.menu_layout.children.add(self.start_game_text)
    
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
    
    def render(self):
        """Render the menu."""
        # Clear screen with black background
        self.screen.fill((0, 0, 0))
        
        # Render the layout (which renders all children including menu_layout)
        self.layout.render(self.screen)
