import pygame
from src.ui.element import UIElement
from src.ui.theme.font import font

class Text(UIElement):
    """Text component for displaying text."""
    def __init__(self, text: str, font_size: int = 24, color: tuple = (255, 255, 255)):
        """
        Initialize a text component.
        """
        self.text = text
        self.font_size = font_size
        self.color = color
        self.font = font.get_font(font_size)
        super().__init__()
    
    def set_color(self, color: tuple):
        """Update the text color."""
        self.color = color
    
    def render(self, surface: pygame.Surface):
        """Render the text component."""
        if not self.visibility.visible:
            return
        
        text_surface = self.font.render(self.text, True, self.color)
        surface.blit(text_surface, (self.location.x, self.location.y))