# ==========================================
# Project: PyRetroGUI
# File: cursor_contest
# Author: Davide Sattin
# Created: 04/01/2026 18:02
# Description:Class for manage the cursor area.
# ==========================================
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.view_port import ViewPort


class CursorManagement:
    def __init__(self, x: int, y: int):
        self.location: Location = Location(x,y)

    def move_up(self, panel_view_port: ViewPort) -> None:
        if panel_view_port is None:
            raise ValueError("Parameter: panel_view_port cannot be None")

        # Check upper limit
        if self.location.y <=0:
            return

        self.location.add_y(-1)

    def move_down(self, panel_view_port: ViewPort) -> None:
        if panel_view_port is None:
            raise ValueError("Parameter: panel_view_port cannot be None")

        # Check lower limit
        if self.location.y  >= panel_view_port.size.height -1:
            return

        self.location.add_y(1)

    def move_left(self, panel_view_port: ViewPort) -> None:
        if panel_view_port is None:
            raise ValueError("Parameter: panel_view_port cannot be None")

        # Check left limit
        if self.location.x  <=0:
            return

        self.location.add_x(-1)

    def move_right(self, panel_view_port: ViewPort) -> None:
            if panel_view_port is None:
                raise ValueError("Parameter: panel_view_port cannot be None")

            # Check right limit
            if self.location.x >= panel_view_port.size.width - 1:
                return

            self.location.add_x(1)