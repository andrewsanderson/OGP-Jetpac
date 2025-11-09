import pygame

class Enabled:
    """Base class for all enabled states."""
    
    def __init__(self, enabled: bool = True):
        self._enabled = enabled
    
    @property
    def enabled(self) -> bool:
        """Get the enabled state."""
        return self._enabled
    
    @enabled.setter
    def enabled(self, value: bool):
        """Set the enabled state."""
        self._enabled = value
    
    def enable(self):
        """Enable the component."""
        self.enabled = True
    
    def disable(self):
        """Disable the component."""
        self.enabled = False