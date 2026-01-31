# ==========================================
# Project: PyRetroGUI
# File: video_buffer
# Author: Davide Sattin
# Created: 21/01/2026 13:41
# Description: This class manages the Video Buffer
# ==========================================

from typing import Optional

from pyretrogui.primitives.location import Location

Color = tuple[int, int, int]


class VideoBuffer:
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows

        # Background color buffers (None = no color / transparent)
        self.back_colors_buffer_prev: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]

        self.back_colors_buffer_curr: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]

        # Character buffers
        self.chars_buffer_prev: list[list[str]] = [
            [" " for _ in range(cols)]
            for _ in range(rows)
        ]

        self.chars_buffer_curr: list[list[str]] = [
            [" " for _ in range(cols)]
            for _ in range(rows)
        ]

        # Foreground color buffers (None = no color / transparent)
        self.foreground_colors_buffer_prev: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]

        self.foreground_colors_buffer_curr: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]


    def clear(self):
        for row_ixd in range(self.rows):
            for col_idx in range(self.cols):

                self.back_colors_buffer_prev[row_ixd][col_idx] = None
                self.back_colors_buffer_curr[row_ixd][col_idx] = None

                self.chars_buffer_prev[row_ixd][col_idx] =" "
                self.chars_buffer_prev[row_ixd][col_idx] =" "

                self.foreground_colors_buffer_curr[row_ixd][col_idx] = None
                self.foreground_colors_buffer_curr[row_ixd][col_idx] = None


    def get_char(self, row_idx, col_idx)-> str:
        # TODO: Check limit
        return self.chars_buffer_curr[row_idx][col_idx]

    def get_background_color(self, row_idx, col_idx):
        # TODO: Check limit
        return self.back_colors_buffer_curr[row_idx][col_idx]

    def get_foreground_color(self, row_idx, col_idx):
        # TODO: Check limit
        return self.foreground_colors_buffer_curr[row_idx][col_idx]

    def is_dirty(self, row_idx, col_idx):
        # TODO: Check limit
        if self.back_colors_buffer_prev[row_idx][col_idx] != self.back_colors_buffer_curr[row_idx][col_idx]:
            return True

        if self.chars_buffer_prev[row_idx][col_idx] != self.chars_buffer_curr[row_idx][col_idx]:
            return True

        if self.foreground_colors_buffer_prev[row_idx][col_idx]!= self.foreground_colors_buffer_curr[row_idx][col_idx]:
            return True

        return False

    def write(self, value: str, location:Location, background_color, foreground_color):
        if value is None:
            raise ValueError("value cannot be None")

        if location is None:
            raise ValueError("location cannot be None")

        if background_color is None:
            raise ValueError("background_color cannot be None")

        if foreground_color is None:
            raise ValueError("foreground_color cannot be None")

        x,y = location
        test = len( self.back_colors_buffer_curr)

        self.back_colors_buffer_curr[y][x] = background_color
        self.foreground_colors_buffer_curr[y][x] = foreground_color
        self.chars_buffer_curr[y][x] = value

    def invalidate(self, col_idx:int, row_idx:int) -> None:

        # TODO: Check limits.
        self.back_colors_buffer_prev[row_idx][col_idx]  = self.back_colors_buffer_curr[row_idx][col_idx]
        self.foreground_colors_buffer_prev[row_idx][col_idx] = self.foreground_colors_buffer_curr[row_idx][col_idx]
        self.chars_buffer_prev[row_idx][col_idx] = self.chars_buffer_curr[row_idx][col_idx]

    def get_buffer_row(self, y:int):
        return self.chars_buffer_curr[y]

    def set_background_color(self, row_idx, col_idx, test_color)  -> None:
        self.back_colors_buffer_curr[row_idx][col_idx] = test_color