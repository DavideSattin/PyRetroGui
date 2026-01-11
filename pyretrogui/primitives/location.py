# ==========================================
# Project: PyRetroGUI
# File: location
# Author: Davide Sattin
# Created: 05/01/2026 17:01
# Description: This class manages a 2D location
# ==========================================
from pyretrogui.primitives.size import Size


class Location:
    """
    Represents a 2D location using X and Y coordinates.
    """

    def __init__(self, x: int, y: int):
        """
        Creates a new Location instance.

        :param x: The X coordinate
        :param y: The Y coordinate
        """
        self.x = x
        self.y = y

    def __add__(self, other: object) -> "Location":
        """
        Returns a new Location resulting from the addition of another object.

        Supported operands:
        - Location: component-wise addition (x + x, y + y)
        - Size: translates the location by the size (width, height)
        - Size: translates the location by (width - 1, height - 1)

        :param other: A Location or Size to add
        :return: A new Location instance
        """
        if isinstance(other, Location):
            return Location(self.x + other.x, self.y + other.y)

        if isinstance(other, Size):
            return Location(
                self.x + other.width - 1,
                self.y + other.height - 1
            )

        return NotImplemented

    def translate_to(self, location: "Location") -> "Location":
        """
        Translates this location by another Location and returns a new Location.

        The current instance is not modified.

        :param location: A Location instance representing the translation offset
        :return: A new Location resulting from the translation
        :raises ValueError: If location is None
        """
        if location is None:
            raise ValueError("location cannot be None")

        new_x = self.x + location.x
        new_y = self.y + location.y
        return Location(new_x, new_y)

    def add_x(self, x: int) -> "Location":
        """
        Returns a new Location with the X coordinate increased by the given value.

        The current instance is not modified.

        :param x: Amount to add to the X coordinate
        :return: A new Location with the updated X value
        """
        new_x = self.x + x
        return Location(new_x, self.y)

    def add_y(self, y: int) -> "Location":
        """
        Returns a new Location with the Y coordinate increased by the given value.

        The current instance is not modified.

        :param y: Amount to add to the Y coordinate
        :return: A new Location with the updated Y value
        """
        new_y = self.y + y
        return Location(self.x, new_y)

    def __str__(self):
        return f"X:{self.x} - Y:{self.y}"