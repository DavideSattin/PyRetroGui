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
    location: Location = Location(0, 0)
    size: Size = Size(0, 0)

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