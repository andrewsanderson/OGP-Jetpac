from typing import Callable, Optional
import pygame
import time
from src.ui.text import Text
from src.ui.colors import BLACK, WHITE, TEXT_DEFAULT, TEXT_SELECTED, BG_DEFAULT, BG_SELECTED


class MenuItem(Text):
    """Menu item component that extends Text with selection and click handling."""
    
    def __init__(
        self,
        text: str,
        x: int = 0,
        y: int = 0,
        font_size: int = 24,
        is_selected: bool = False,
        onclick: Optional[Callable[[], None]] = None
    ):
        """
        Initialize a menu item component.
        """
        super().__init__(text, x, y, font_size, TEXT_DEFAULT)
        self.is_selected = is_selected
        self.onclick = onclick
        self._animation_start_time = time.time()
        self._current_bg_color = BG_DEFAULT
        self._current_text_color = TEXT_DEFAULT
    
    def _update_colors(self):
        """Update the background and text colors based on selection state and animation."""
        current_time = time.time()
        elapsed = current_time - self._animation_start_time
        seconds_elapsed = int(elapsed)
        
        # Alternate every second (even seconds = one color, odd seconds = other color)
        is_alternate_state = (seconds_elapsed % 2) == 1
        
        if self.is_selected:
            # When selected: white background, black text
            if is_alternate_state:
                self._current_bg_color = BLACK
                self._current_text_color = WHITE
            else:
                self._current_bg_color = WHITE
                self._current_text_color = BLACK
        else:
                self._current_bg_color = BLACK
                self._current_text_color = WHITE
        
        # Update text color
        self.color = self._current_text_color
    
    def set_selected(self, selected: bool):
        """Set the selection state."""
        self.is_selected = selected
        self._update_colors()
    
    def handle_event(self, event: pygame.event.Event) -> bool:
        """
        Handle pygame events, particularly mouse clicks.
        
        Args:
            event: The pygame event to handle
            
        Returns:
            True if the event was handled, False otherwise
        """
        if not self.enable.enabled:
            return False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Left mouse button
                if self.location.is_point_inside(*event.pos):
                    if self.onclick:
                        self.onclick()
                    return True
        return False
    
    def update(self, dt: float = 0.0):
        """Update the menu item (for animation)."""
        self._update_colors()
    
    def render(self, surface: pygame.Surface):
        """Render the menu item component."""
        if not self.visibility.visible:
            return
        
        # Update colors based on selection state and animation
        self._update_colors()
        
        # Draw background rectangle
        pygame.draw.rect(
            surface,
            self._current_bg_color,
            self.location.rect
        )
        
        # Render text using parent Text class
        super().render(surface)

