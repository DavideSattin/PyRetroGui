
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.video.context import Context




class DockablePanel(UIPanel):

      def __init__(self, parent):
          super().__init__(parent)

          self.background = (0, 125, 255)


      def update(self, context: Context):
          viewport = self.get_size(context)
          super().draw_background(context, viewport, self.background )