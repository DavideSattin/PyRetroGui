from pygame.event import Event
from pyretrogui.context import Context
from pyretrogui.arranger.dock_mode import DockMode
from pyretrogui.ui_elements.ui_element import UIElement


class DockablePanel(UIElement):
      def update(self, context: Context):
          pass

      def on_key_event(self, event: Event, context: Context):
          pass

      def __init__(self, parent):
          super().__init__(parent)
          self.dock_mode: DockMode = DockMode.NONE
