# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin
# Created: 18/01/2026 12:04
# Description: This class manage the dockable panel.
# ==========================================
from pyretrogui.arranger.layout_manager import LayoutManager
from pyretrogui.widgets.ui_elements.ui_element import UIElement
from pyretrogui.widgets.ui_elements.ui_panel import UIPanel
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

      def init(self):
          super().init()
          print("Init DockablePanel")

      def on_set_layout(self, context: Context):
          print("on_set_layout DockablePanel")
          super().on_set_layout(context)
          for element in self.elements:
              element.on_set_layout(context)

      def draw(self, context: Context):
          """
          Draws the dockable panel and its children.
          The drawing starts at the relative position (0,0), which will be translated
          by the drawing method into the absolute screen position.
          :param context: The rendering context.
          """

          # The widget view_port it's relative to this widget.
          widget_relative_viewport = LayoutManager().get_relative_viewport(self.viewport)
          super().draw_background(context, widget_relative_viewport, self.background )

          #TODO: Tmp
          for element in self.elements:
              element.draw(context)

      def add_child(self, element: UIElement):
          if element is None:
              raise ValueError("element cannot be None")

          if element not in self.elements:
              element.parent = self
              self.elements.append(element)