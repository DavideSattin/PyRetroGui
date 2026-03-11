from abc import ABC, abstractmethod

from pyretrogui.arranger.layout_manager import LayoutManager
from pyretrogui.arranger.ui_behaviour import UIBehaviour
from pyretrogui.events.mouse_event_dispatcher import MousePosition
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.widgets.ui_elements.unit import Unit


class UIElement(ABC):
      def __init__(self,  parent: "UIElement" = None):
          self.parent: UIElement = parent
          self.id : int = 0
          self.visible = True
          self.enabled = True
          self.initialized = False
          self.viewport = ViewPort(location=Location(0,0), size=Size(0,0))
          self.margin: bool = True
          self.border: bool = True
          self.behaviour: UIBehaviour = UIBehaviour()
          self.name : str = ""
          self.unit : Unit = Unit.Grid16

          # The widget manager.
          from pyretrogui.widgets.ui_elements.widget_manager import WidgetManager
          self._widget_manager = WidgetManager()


      def on_set_layout(self, context: Context):
          self.viewport = LayoutManager().get_view_port(self)


      def init(self):
          self.initialized = True

      @abstractmethod
      def draw(self, context: Context):
          """
          Draws the UI element.
          The drawing starts at the relative position (0,0), which will be translated
          by the drawing method into the absolute screen position.
          :param context: The rendering context.
          """
          pass

      def match(self, mouse_position: MousePosition) -> bool:
          if mouse_position is None:
              raise ValueError("The mouse_position cannot be None")

          return self.top_left().x <= location.x <= self.bottom_right().x and self.top_left().y <= location.y <= self.bottom_right().y

