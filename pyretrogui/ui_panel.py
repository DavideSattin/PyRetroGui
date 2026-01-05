# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================
from encodings import search_function

from pyretrogui.charset import CHAR_CLASSES
from abc import ABC, abstractmethod
from pyretrogui.context import Context


class UIPanel(ABC):
      def __init__(self):
          self.visibile = True
          self.enabled = True
          self.margin = True

      @abstractmethod
      def update(self,context: Context):
          pass

      def draw_border(self, context: Context):
          context.matrix[0][0] = CHAR_CLASSES["corner_tl"]
          context.matrix[0][-1] = CHAR_CLASSES["corner_tr"]
          context.matrix[-1][0] = CHAR_CLASSES["corner_bl"]
          context.matrix[-1][-1] = CHAR_CLASSES["corner_br"]

          # Draw vertical lines.
          for y in range(1, context.rows - 1):
              context.matrix[y][0] = CHAR_CLASSES["line_v"]
              context.matrix[y][-1] = CHAR_CLASSES["line_v"]

          # Draw orizzontal lines.
          for x in range(1, context.cols - 1):
              context.matrix[0][x] = CHAR_CLASSES["line_h"]
              context.matrix[-1][x] = CHAR_CLASSES["line_h"]


class TextWidget(UIPanel):
      def __init__(self):
          super().__init__()
          self.text = None

      def update(self,context: Context):
          super().draw_border(context)