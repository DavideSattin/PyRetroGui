# ==========================================
# Project: PyRetroGUI
# File: video_buffer
# Author: Davide Sattin
# Created: 21/01/2026 13:41
# Description: This class manages the Video Buffer
# ==========================================

from typing import Optional

Color = tuple[int, int, int]


class VideoBuffer:
    def __init__(self, cols: int, rows: int):
        self.cols = cols
        self.rows = rows

        # Character buffers
        self.chars_buffer_prev: list[list[str]] = [
            [" " for _ in range(cols)]
            for _ in range(rows)
        ]

        self.chars_buffer_curr: list[list[str]] = [
            [" " for _ in range(cols)]
            for _ in range(rows)
        ]

        # Background color buffers (None = no color / transparent)
        self.back_colors_buffer_prev: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]

        self.back_colors_buffer_curr: list[list[Optional[Color]]] = [
            [None for _ in range(cols)]
            for _ in range(rows)
        ]
