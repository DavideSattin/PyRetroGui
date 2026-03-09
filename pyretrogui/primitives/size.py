# ==========================================
# Project: PyRetroGUI
# File: size
# Author: Davide Sattin
# Created: 09/01/2026 17:01
# Description: Represents a 2D size (width and height).
# ==========================================

from __future__ import annotations


class Size:
    """
    Represents the size of a 2D element using width and height.
    """

    width: int
    height: int

    def __init__(self, width: int, height: int):
        """
        Creates a new Size instance.

        :param width: The width value
        :param height: The height value
        """
        self.width = width
        self.height = height

    def __iter__(self):
        """
        Allows unpacking the Size object.

        Example:
        width, height = size
        """
        yield self.width
        yield self.height

    def __repr__(self):
        """
        Returns a developer-friendly representation.
        """
        return f"Size(width={self.width}, height={self.height})"

    def __str__(self):
        """
        Returns a human-readable representation.
        """
        return f"Size(width={self.width}, height={self.height})"