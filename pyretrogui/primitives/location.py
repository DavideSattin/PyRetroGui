# ==========================================
# Project: PyRetroGUI
# File: location
# Author: Davide Sattin
# Created: 05/01/2026 17:01
# Description: Represents a 2D location.
# ==========================================

from __future__ import annotations

from pyretrogui.primitives.size import Size


class Location:
    """
    Represents a 2D location using X and Y coordinates.
    """

    x: int
    y: int

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
        - Size: translates the location by (width - 1, height - 1)

        :param other: A Location or Size instance
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

    def __iter__(self):
        yield self.x
        yield self.y

    def translate_to(self, location: "Location") -> "Location":
        """
        Translates this location by another Location and returns a new Location.

        The current instance is not modified.

        :param location: Translation offset
        :return: A new translated Location
        """

        if location is None:
            raise ValueError("location cannot be None")

        return Location(
            self.x + location.x,
            self.y + location.y
        )

    def add_x(self, x: int) -> "Location":
        """
        Returns a new Location with the X coordinate increased.

        :param x: Value to add
        """
        return Location(self.x + x, self.y)

    def add_y(self, y: int) -> "Location":
        """
        Returns a new Location with the Y coordinate increased.

        :param y: Value to add
        """
        return Location(self.x, self.y + y)

    def __str__(self):
        return f"X:{self.x} - Y:{self.y}"