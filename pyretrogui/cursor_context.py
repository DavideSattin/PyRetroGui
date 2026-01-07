# ==========================================
# Project: PyRetroGUI
# File: cursor_contest
# Author: Davide Sattin
# Created: 04/01/2026 18:02
# Description:Class for manage the cursor
# ==========================================
import threading
import time

from pyretrogui.charset import CHAR_CLASSES
from pyretrogui.location import Location


class CursorContext:
      def __init__(self,x: int = 0, y: int = 0):
          self.location = Location(x, y)
          self.enable = False
          self._cursor_thread = None
          self.cursor_visible = False

      def get_cursor_char(self):
          return CHAR_CLASSES["fill_full"]

      def start_cursor(self):
          """Avvia il cursore lampeggiante."""
          if self._cursor_thread is None or not self._cursor_thread.is_alive():
              self._stop_cursor = False
              self._cursor_thread = threading.Thread(target=self._cursor_blink)
              self._cursor_thread.daemon = True
              self._cursor_thread.start()

      def stop_cursor(self):
          """Ferma il cursore lampeggiante."""
          self._stop_cursor = True
          if self._cursor_thread is not None:
              self._cursor_thread.join()  # aspetta che il thread termini
              self._cursor_thread = None

      def _cursor_blink(self):
          while not self._stop_cursor:
              self.cursor_visible = not self.cursor_visible
              time.sleep(0.5)