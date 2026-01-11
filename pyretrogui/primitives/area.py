# ==========================================
# Project: PyRetroGUI
# File: area
# Author: Davide Sattin 
# Created: 11/01/2026 10:38
# Description: This class represents a rectangle area of the screen.
# ==========================================
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.primitives.view_port import ViewPort


class Area:
    def __init__(self, view_port: ViewPort):
        self.top_left: Location = view_port.absolute_location
        self.top_right: Location = self.top_left.add_x(view_port.size.width - 1)
        self.bottom_left = self.top_left.add_y(view_port.size.height - 1)
        self.bottom_right = self.bottom_left.add_x(view_port.size.width - 1)
        self.center = self.top_left.add_x(view_port.size.width // 2).add_y(view_port.size.height // 2)
        self.size: Size = view_port.size

    @staticmethod
    def create_area(location: Location, size: Size) -> "Area":
        return Area(ViewPort(absolute_location= location, size= size))