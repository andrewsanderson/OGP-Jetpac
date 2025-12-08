"""Main menu screen."""
import pygame
from src.ui.layout import Layout
from src.ui.text import Text
from src.ui.element_attributes.location import Location
from src.ui.element_attributes.visibility import Visibility
from src.ui.element_attributes.children import Children

class MainMenu:
    """Main menu screen with a single layout."""
    
    def __init__(self, screen: pygame.Surface):
        """
        Initialize the main menu.
        
        Args:
            screen: The pygame surface to render to
        """
        self.screen = screen
        screen_width = screen.get_width()
        screen_height = screen.get_height()
        
        # Create "Hello World" text element
        hello_text = Text("Hello World", font_size=48, color=(255, 255, 255))
        
        # Calculate center position for the text
        # Get text surface to measure its size
        text_surface = hello_text.font.render(hello_text.text, True, hello_text.color)
        text_width = text_surface.get_width()
        text_height = text_surface.get_height()
        
        # Center the text
        text_x = (screen_width - text_width) // 2
        text_y = (screen_height - text_height) // 2
        
        hello_text.location = Location(text_x, text_y)
        
        # Create a single layout with the text as a child
        self.layout = Layout(
            orientation='vertical',
            horizontal_align='center',
            vertical_align='center'
        )
        
        # Initialize layout attributes
        self.layout.location = Location(0, 0)
        self.layout.visibility = Visibility(visible=True)
        self.layout.children = Children(children=[hello_text])
    
    def render(self):
        """Render the main menu."""
        # Clear the screen with black background
        self.screen.fill((0, 0, 0))
        
        # Render the layout and its children
        self.layout.render(self.screen)
