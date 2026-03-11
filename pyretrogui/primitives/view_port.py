# ==========================================
# Project: PyRetroGUI
# File: view_port
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description: Represents a rectangular viewport in the UI coordinate system.
# ==========================================
from dataclasses import dataclass
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size


@dataclass
class ViewPort:
    """
    Represents a rectangular viewport in the UI coordinate system.

    Attributes:
        location (Location): The top-left corner of the viewport.
        size (Size): The dimensions (width and height) of the viewport.
    """
    location: Location = Location(0, 0)
    size: Size = Size(0, 0)

    def __str__(self):
        """Returns a string representation of the ViewPort."""
        return f"ViewPort(location={self.location}, size={self.size})"

    def top_left(self)-> Location:
        """Returns the location of the top-left corner."""
        return self.location

    def top_right(self) -> Location:
        """Returns the location of the top-right corner."""
        return self.location.add_x(self.size.width - 1)

    def bottom_left(self)-> Location:
        """Returns the location of the bottom-left corner."""
        return self.location.add_y(self.size.height - 1)
    
    def bottom_right(self) -> Location:
        """Returns the location of the bottom-right corner."""
        return self.bottom_left().add_x(self.size.width - 1)

    def center(self)-> Location:
         """Returns the location of the center of the viewport."""
         return self.top_left().add_x(self.size.width // 2).add_y(self.size.height // 2)
    
    def top(self)-> int:
        """Returns the y-coordinate of the top edge."""
        return self.location.y
    
    def bottom(self)-> int:
        """Returns the y-coordinate of the bottom edge."""
        return self.bottom_left().y
    
    def left(self):
        """Returns the x-coordinate of the left edge."""
        return self.bottom_left().x
    
    def right(self):
        """Returns the x-coordinate of the right edge."""
        return self.top_right().x
    
    def translate(self, location: Location) -> "ViewPort":
        """
        Returns a new ViewPort translated by the given location offset.

        :param location: The offset to apply to the current location.
        :return: A new ViewPort instance with the updated location.
        :raises ValueError: If location is None.
        """
        if location is None:
            raise ValueError("The location cannot be None")

        return ViewPort(location=self.location + location, size=self.size)

