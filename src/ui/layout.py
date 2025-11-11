from typing import Literal, List, Optional
import pygame
from src.ui.component import Component
from src.ui.attributes.anchor import HorizontalAlign, VerticalAlign, Anchor
from src.ui.attributes.children import Children

ChildOrientation = Literal['row', 'column']


class Layout(Component):
    """Layout component that arranges child components based on parent anchor."""
    
    def __init__(
        self,
        parent: Optional["Layout"] = None,
        vertical_align: VerticalAlign = 'top',
        horizontal_align: HorizontalAlign = 'left',
        orientation: ChildOrientation = 'column',
        children: Optional[List[Component]] = None,
        width: int = 0,
        height: int = 0
    ):
        """
        Initialize a layout component.
        """
        # Position (x, y) will be derived from parent anchor when added as a child
        super().__init__(0, 0, width, height)
        self.parent = parent if parent is not None else None
        self.vertical_align = vertical_align
        self.horizontal_align = horizontal_align
        self.orientation = orientation
        
        # Initialize children manager with callback to rearrange on change
        self.children = Children(
            children=children,
            on_change=self._arrange_children
        )
        
        # Arrange children based on parent anchor
        self._arrange_children()
    
    def _arrange_children(self):
        """Arrange children based on parent anchor."""
        if not self.children.children:
            return
        
        # Get the anchor alignment values
        anchor_h = self.parent.horizontal_align
        anchor_v = self.parent.vertical_align
        
        # Calculate starting position based on anchor
        if self.orientation == 'column':
            self._arrange_column(anchor_h, anchor_v)
        else:  # row
            self._arrange_row(anchor_h, anchor_v)

    def _arrange_column(self, anchor_h: HorizontalAlign, anchor_v: VerticalAlign):
        """Arrange children in a column (vertically)."""

        for child in self.children.children:
            child.location.y = self.location.y + self.parent.location.y
            child.location.x = self.location.x + self.parent.location.x
    
    def _arrange_row(self, anchor_h: HorizontalAlign, anchor_v: VerticalAlign):
        """Arrange children in a row (horizontally)."""

        for child in self.children.children:
            child.location.x = self.location.x + self.parent.location.x
            child.location.y = self.location.y + self.parent.location.y
  
    def render(self, surface: pygame.Surface):
        """Render the layout and all its children."""
        if not self.visibility.visible:
            return
        
        # Render all children
        for child in self.children.children:
            if child.visibility.visible:
                child.render(surface)
    
