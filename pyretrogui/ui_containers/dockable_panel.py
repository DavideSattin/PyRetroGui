

from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.video.context import Context
from pyretrogui.arranger.dock_mode import DockMode



class DockablePanel(UIPanel):




      def __init__(self, parent):
          super().__init__(parent)
          self.dock_mode: DockMode = DockMode.NONE


      def update(self, context: Context):
          viewport = self.get_size(context)
          super().draw_background(context, viewport, (0, 125, 255))