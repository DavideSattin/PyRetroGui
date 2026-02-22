# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin
# Created: 18/01/2026 12:04
# Description: This class manage the dockable panel.
# ==========================================
from pyretrogui.primitives.size import Size
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.video.context import Context


class DockablePanel(UIPanel):

      def __init__(self, parent):
          super().__init__(parent)
          self.margin = False
          self.border = False


          # TODO: Remove this. Use a class for theme.
          self.background = (0, 125, 255)





      def update(self, context: Context):
          viewport = self.get_view_port(context)
          super().draw_background(context, viewport, self.background )