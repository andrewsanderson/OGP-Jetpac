import pygame
from typing import Dict


class UI:
    """Global UI manager for fonts and other UI resources."""
    
    def __init__(self):
        """Initialize the UI manager."""
        self._fonts: Dict[int, pygame.font.Font] = {}
        self._default_font_path = "assets/fonts/PressStart2P-Regular.ttf"
        self._load_default_font()
    
    def _load_default_font(self):
        """Load the default font file."""
        try:
            # Pre-load common font sizes
            for size in [12, 16, 20, 24, 32, 48]:
                self._fonts[size] = pygame.font.Font(self._default_font_path, size)
        except (FileNotFoundError, pygame.error):
            # If font file not found, will use fallback when getting font
            pass
    
    def get_font(self, size: int) -> pygame.font.Font:
        """
        Get a font of the specified size.
        """
        # Return cached font if available
        if size in self._fonts:
            return self._fonts[size]
        
        # Try to load the font
        try:
            font = pygame.font.Font(self._default_font_path, size)
            self._fonts[size] = font
            return font
        except (FileNotFoundError, pygame.error):
            # Fallback to default font
            if size not in self._fonts:
                self._fonts[size] = pygame.font.Font(None, size)
            return self._fonts[size]


# Global UI instance
ui = UI()

