# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================
from encodings import search_function

from pyretrogui.charset import CHAR_CLASSES


class UIPanel:
      def __init__(self):
          self.visibile = True
          self.enabled = True
          self.margin = True


      def draw(self):
          pass


class TextWidget(UIPanel):
      def __init__(self):
          super().__init__()

      def update(self,context):
          context.matrix[0][0] = CHAR_CLASSES["corner_tl"]
