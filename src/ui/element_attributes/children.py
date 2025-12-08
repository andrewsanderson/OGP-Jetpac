from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ui.element import UIElement

class Children:
    def __init__(self, children: list["UIElement"]):
        self.children = children