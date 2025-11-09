from typing import Literal, List
import pygame
from src.ui.component import Component

VerticalAlign = Literal['top', 'bottom', 'center']
HorizontalAlign = Literal['left', 'center', 'right']
ChildOrientation = Literal['row', 'column']


class Layout(Component):
    """Layout component that arranges child components based on alignment."""
    
    def __init__(
        self,
        x: int = 0,
        y: int = 0,
        width: int = 0,
        height: int = 0,
        vertical: VerticalAlign = 'top',
        horizontal: HorizontalAlign = 'left',
        child_orientation: ChildOrientation = 'column',
        spacing: int = 10
    ):
        """
        Initialize a layout component.
        """
        super().__init__(x, y, width, height)
        self.vertical = vertical
        self.horizontal = horizontal
        self.child_orientation = child_orientation
        self.spacing = spacing
        self.children: List[Component] = []
    
    def add_child(self, child: Component):
        """Add a child component to the layout."""
        if child not in self.children:
            self.children.append(child)
        self._arrange_children()
    
    def remove_child(self, child: Component):
        """Remove a child component from the layout."""
        if child in self.children:
            self.children.remove(child)
        self._arrange_children()
    
    def clear_children(self):
        """Remove all children from the layout."""
        self.children.clear()
    
    def _arrange_children(self):
        """Arrange children based on alignment settings and orientation."""
        if not self.children:
            return
        
        if self.child_orientation == 'column':
            self._arrange_column()
        else:  # row
            self._arrange_row()
    
    def _arrange_column(self):
        """Arrange children in a column (vertically)."""
        # Calculate total height needed for all children
        total_height = sum(child.location.height for child in self.children)
        total_height += self.spacing * (len(self.children) - 1)
        
        # Calculate starting Y position based on vertical alignment
        if self.vertical == 'top':
            current_y = self.location.y
        elif self.vertical == 'bottom':
            current_y = self.location.y + self.location.height - total_height
        else:  # center
            current_y = self.location.y + (self.location.height - total_height) // 2
        
        # Arrange each child
        for child in self.children:
            # Set Y position
            child.location.y = current_y
            
            # Set X position based on horizontal alignment
            if self.horizontal == 'left':
                child.location.x = self.location.x
            elif self.horizontal == 'right':
                child.location.x = self.location.x + self.location.width - child.location.width
            else:  # center
                child.location.x = self.location.x + (self.location.width - child.location.width) // 2
            
            # Move to next position
            current_y += child.location.height + self.spacing
    
    def _arrange_row(self):
        """Arrange children in a row (horizontally)."""
        # Calculate total width needed for all children
        total_width = sum(child.location.width for child in self.children)
        total_width += self.spacing * (len(self.children) - 1)
        
        # Calculate starting X position based on horizontal alignment
        if self.horizontal == 'left':
            current_x = self.location.x
        elif self.horizontal == 'right':
            current_x = self.location.x + self.location.width - total_width
        else:  # center
            current_x = self.location.x + (self.location.width - total_width) // 2
        
        # Arrange each child
        for child in self.children:
            # Set X position
            child.location.x = current_x
            
            # Set Y position based on vertical alignment
            if self.vertical == 'top':
                child.location.y = self.location.y
            elif self.vertical == 'bottom':
                child.location.y = self.location.y + self.location.height - child.location.height
            else:  # center
                child.location.y = self.location.y + (self.location.height - child.location.height) // 2
            
            # Move to next position
            current_x += child.location.width + self.spacing
    
    def set_size(self, width: int, height: int):
        """Update the layout size and rearrange children."""
        self.location.set_size(width, height)
        self._arrange_children()
    
    def set_position(self, x: int, y: int):
        """Update the layout position and rearrange children."""
        self.location.set_position(x, y)
        self._arrange_children()
    
    def render(self, surface: pygame.Surface):
        """Render the layout and all its children."""
        if not self.visibility.visible:
            return
        
        # Render all children
        for child in self.children:
            if child.visibility.visible:
                child.render(surface)
    
    def update(self, dt: float = 0.0):
        """Update the layout and all its children."""
        for child in self.children:
            if hasattr(child, 'update'):
                child.update(dt)
    
    def handle_event(self, event: pygame.event.Event) -> bool:
        """Handle events for all children."""
        for child in self.children:
            if hasattr(child, 'handle_event'):
                if child.handle_event(event):
                    return True
        return False

