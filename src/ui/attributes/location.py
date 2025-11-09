from abc import ABC, abstractmethod
import pygame

class Location(ABC):
    """Base class for all locations."""
    
    def __init__(self, x: int, y: int, width: int, height: int):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        self.rect = pygame.Rect(x, y, width, height)
    
    @property
    def x(self) -> int:
        """Get the x position."""
        return self._x
    
    @x.setter
    def x(self, value: int):
        """Set the x position."""
        self._x = value
        self.rect.x = value
    
    @property
    def y(self) -> int:
        """Get the y position."""
        return self._y
    
    @y.setter
    def y(self, value: int):
        """Set the y position."""
        self._y = value
        self.rect.y = value
    
    @property
    def width(self) -> int:
        """Get the width."""
        return self._width
    
    @width.setter
    def width(self, value: int):
        """Set the width."""
        self._width = value
        self.rect.width = value
    
    @property
    def height(self) -> int:
        """Get the height."""
        return self._height
    
    @height.setter
    def height(self, value: int):
        """Set the height."""
        self._height = value
        self.rect.height = value
    
    def set_position(self, x: int, y: int):
        """Update the position."""
        self.x = x
        self.y = y
    
    def set_size(self, width: int, height: int):
        """Update the size."""
        self.width = width
        self.height = height
    
    def get_rect(self) -> pygame.Rect:
        """Get the rectangle."""
        return self.rect
    
    def is_point_inside(self, x: int, y: int) -> bool:
        """Check if a point is inside the location."""
        return self.rect.collidepoint(x, y)
    
