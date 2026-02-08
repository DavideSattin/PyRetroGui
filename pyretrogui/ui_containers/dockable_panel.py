from pygame.event import Event
from pyretrogui.video.context import Context
from pyretrogui.arranger.dock_mode import DockMode
from pyretrogui.ui_elements.ui_element import UIElement


class DockablePanel(UIElement):
      def update(self, context: Context):
          pass



      def __init__(self, parent):
          super().__init__(parent)
          self.dock_mode: DockMode = DockMode.NONE


      def update(self, context: Context):
          super().draw_background(context, panel_viewport, (0, 0, 255))