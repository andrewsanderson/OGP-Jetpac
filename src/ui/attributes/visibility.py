import pygame

class Visibility:
    """Base class for all visibility states."""
    
    def __init__(self, visible: bool = True):
        self._visible = visible
    
    @property
    def visible(self) -> bool:
        """Get the visibility state."""
        return self._visible
    
    @visible.setter
    def visible(self, value: bool):
        """Set the visibility state."""
        self._visible = value
    
    def show(self):
        """Make the component visible."""
        self.visible = True
    
    def hide(self):
        """Hide the component."""
        self.visible = False