from src.ui.element_attributes.location import Location
from src.ui.element_attributes.visibility import Visibility
from src.ui.element_attributes.children import Children
import pygame

class UIElement:
    def __init__(self, location: Location = Location(x=0, y=0), visibility: Visibility = Visibility(visible=True), children: Children = Children(children=[]), parent: "UIElement" = None, width: int = None, height: int = None):
        self.location = location
        self.visibility = visibility
        self.children = children
        self.parent = parent
        self._width = width
        self._height = height
    
    @property
    def width(self) -> int:
        """Get the width of the element. If not set, returns the widest child."""
        if self._width is not None:
            return self._width
        
        if self.children is None or not self.children.children:
            return 0
        
        max_width = 0
        for child in self.children.children:
            child_width = child.width
            if child_width > max_width:
                max_width = child_width
        
        return max_width
    
    @width.setter
    def width(self, value: int):
        """Set the width of the element."""
        self._width = value
    
    @property
    def height(self) -> int:
        """Get the height of the element. If not set, returns the tallest child."""
        if self._height is not None:
            return self._height
        
        if self.children is None or not self.children.children:
            return 0
        
        max_height = 0
        for child in self.children.children:
            child_height = child.height
            if child_height > max_height:
                max_height = child_height
        
        return max_height
    
    @height.setter
    def height(self, value: int):   
        """Set the height of the element."""
        self._height = value

    
    def render(self, surface: pygame.Surface):
        """Render the layout and all its children."""
        if not self.visibility.visible:
            return
        
        # Render all children
        if self.children and self.children.children:
            for child in self.children.children:
                if hasattr(child, 'render'):
                    child.render(surface)

        