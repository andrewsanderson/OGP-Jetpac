from typing import List, Optional, Callable
from src.ui.component import Component


class Children:
    """Manages a collection of child components."""
    
    def __init__(
        self,
        children: Optional[List[Component]] = None,
        on_change: Optional[Callable[[], None]] = None
    ):
        """
        Initialize a children manager.
        
        Args:
            children: Initial list of children (optional)
            on_change: Callback function called when children change (optional)
        """
        self._children: List[Component] = children if children is not None else []
        self.on_change = on_change

    @property
    def children(self) -> List[Component]:
        """Get the list of children."""
        return self._children
    
    def add(self, child: Component):
        """Add a child component."""
        if child not in self._children:
            self._children.append(child)
            self._notify_change()
    
    def remove(self, child: Component):
        """Remove a child component."""
        if child in self._children:
            self._children.remove(child)
            self._notify_change()
    
    def clear(self):
        """Remove all children."""
        self._children.clear()
        self._notify_change()
    
    def _notify_change(self):
        """Notify that children have changed."""
        if self.on_change:
            self.on_change()

