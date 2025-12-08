import pygame
from src.ui.element import UIElement
from typing import Literal

OrientationType = Literal['horizontal', 'vertical']
HorizontalAlignType = Literal['left', 'center', 'right']
VerticalAlignType = Literal['top', 'center', 'bottom']

class Layout(UIElement):
    def __init__(self, orientation: OrientationType = 'horizontal', horizontal_align: HorizontalAlignType = 'left', vertical_align: VerticalAlignType = 'top'):
        super().__init__()
        self.orientation = orientation
        self.horizontal_align = horizontal_align
        self.vertical_align = vertical_align

