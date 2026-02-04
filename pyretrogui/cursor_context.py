# ==========================================
# Project: PyRetroGUI
# File: cursor_context
# Author: Davide Sattin
# Created: 04/01/2026 18:02
# Description: Class to manage the cursor
# ==========================================

import threading
import time

from pyretrogui.charset import CHAR_CLASSES
from pyretrogui.primitives.location import Location


class CursorContext:
    def __init__(self, x: int = 0, y: int = 0):
        self.location = Location(x, y)
        self.enabled = False
        self.cursor_visible = False
        self.buffered_cursor_visible = False

        # Internal thread control
        self._cursor_thread = None
        self._stop_cursor = False

    def get_cursor_char(self):
        """Return the character used to draw the cursor."""
        return CHAR_CLASSES["fill_full"]

    def start_cursor(self):
        """Start the blinking cursor thread if not already running."""
        if self._cursor_thread is None or not self._cursor_thread.is_alive():
            self._stop_cursor = False
            self._cursor_thread = threading.Thread(target=self._cursor_blink, daemon=True)
            self._cursor_thread.start()

    def stop_cursor(self):
        """Stop the blinking cursor thread."""
        self._stop_cursor = True

        if self._cursor_thread is not None:
            self._cursor_thread.join()  # Wait for the thread to finish
            self._cursor_thread = None

    def _cursor_blink(self):
        """Internal loop that toggles cursor visibility."""
        while not self._stop_cursor:
            self.cursor_visible = not self.cursor_visible
            time.sleep(0.5)
