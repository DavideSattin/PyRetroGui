from typing import List

from pygame.event import Event

from pyretrogui.context import Context
from pyretrogui.ui_elements.ui_element import UIElement
from enum import Enum
class DockMode(Enum):
    NONE = 0
    TOP = 1
    BOTTOM = 2
    LEFT = 3
    RIGHT = 4
    CONTENT = 5

class DockableContainer(UIElement):

      def __init__(self, parent):
        super().__init__(parent)
        self.containers: List[DockablePanel] = []

      def update(self, context: Context):
          for container in self.containers:
              container.update(context)

      #remove this.
      def on_key_event(self, event: Event, context: Context):
          pass


class DockablePanel(UIElement):
      def update(self, context: Context):
          pass

      def on_key_event(self, event: Event, context: Context):
          pass

      def __init__(self, parent):
          super().__init__(parent)
          self.dock_mode: DockMode = DockMode.NONE
