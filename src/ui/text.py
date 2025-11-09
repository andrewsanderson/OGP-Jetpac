import pygame
from src.ui.component import Component
from src.ui.ui import ui


class Text(Component):
    """Text component for displaying text."""
    
    def __init__(self, text: str, x: int = 0, y: int = 0, font_size: int = 24, color: tuple = (255, 255, 255)):
        """
        Initialize a text component.
        """
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = ui.get_font(font_size)
        
        # Calculate text dimensions
        text_surface = self.font.render(text, True, color)
        width, height = text_surface.get_size()
        
        # Initialize component with calculated dimensions
        super().__init__(x, y, width, height)
    
    def set_text(self, text: str):
        """Update the text and recalculate dimensions."""
        self.text = text
        text_surface = self.font.render(text, True, self.color)
        width, height = text_surface.get_size()
        self.location.set_size(width, height)
    
    def set_color(self, color: tuple):
        """Update the text color."""
        self.color = color
    
    def render(self, surface: pygame.Surface):
        """Render the text component."""
        if not self.visibility.visible:
            return
        
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.location.x, self.location.y))

