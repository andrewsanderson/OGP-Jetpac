from typing import Literal

HorizontalAlign = Literal['left', 'center', 'right']
VerticalAlign = Literal['top', 'bottom', 'center']

class Anchor:
    """Anchor component for positioning."""
    
    def __init__(
        self,
        horizontal_align: HorizontalAlign = 'left',
        vertical_align: VerticalAlign = 'top',
        x: int = 0,
        y: int = 0
    ):
        """
        Initialize an anchor component.
        """
        self.horizontal_align = horizontal_align
        self.vertical_align = vertical_align
        self._x = x
        self._y = y
    
    @property
    def x(self) -> int:
        """Get the x position."""
        return self._x
    
    @x.setter
    def x(self, value: int):  
        """Set the x position."""
        self._x = value
    
    @property
    def y(self) -> int:
        """Get the y position."""
        return self._y
    
    @y.setter
    def y(self, value: int):
        """Set the y position."""
        self._y = value
    
    @property
    def horizontal_align(self) -> HorizontalAlign:
        """Get the horizontal alignment."""
        return self._horizontal_align
    
    @horizontal_align.setter
    def horizontal_align(self, value: HorizontalAlign):
        """Set the horizontal alignment."""
        self._horizontal_align = value
    
    @property
    def vertical_align(self) -> VerticalAlign:
        """Get the vertical alignment."""
        return self._vertical_align
    
    @vertical_align.setter
    def vertical_align(self, value: VerticalAlign):
        """Set the vertical alignment."""
        self._vertical_align = value
