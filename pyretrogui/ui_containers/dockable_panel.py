# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin
# Created: 18/01/2026 12:04
# Description: This class manage the dockable panel.
# ==========================================

from pyretrogui.ui_elements.ui_element import UIElement
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.video.context import Context
from typing import List



class DockablePanel(UIPanel):

      def __init__(self, parent):
          super().__init__(parent)
          self.margin = False
          self.border = False
          self.elements: List[UIElement] = []

          # TODO: Remove this. Use a class for theme.
          self.background = (0, 125, 255)

      def init(self, context: Context):
          for element in self.elements:
              element.init(context)

      def draw(self, context: Context):
          viewport = self.get_view_port(context)
          super().draw_background(context, viewport, self.background )

          #TODO: Tmp
          for element in self.elements:
              element.draw(context)

      def add_child(self, element: UIElement):
          if element is None:
              raise ValueError("element cannot be None")

          if element not in self.elements:
              element.parent = self
              self.elements.append(element)