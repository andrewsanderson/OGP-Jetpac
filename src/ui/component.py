from abc import ABC
from typing import Optional
from src.ui.attributes.location import Location
from src.ui.attributes.visibility import Visibility
from src.ui.attributes.enable import Enabled

class Component(ABC):
    """Base class for all UI components."""
    
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
    ):
        """
        Initialize a UI component.
        """
        self.location = Location(x, y, width, height)
        self.visibility = Visibility()
        self.enable = Enabled()
    




