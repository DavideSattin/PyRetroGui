from abc import ABC, abstractmethod

from pyretrogui.arranger.layout_manager import LayoutManager
from pyretrogui.arranger.ui_behaviour import UIBehaviour
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size



class UIElement(ABC):
      def __init__(self,  parent: "UIElement" = None):
          self.parent: UIElement = parent
          self.id : int = 0
          self.visible = True
          self.enabled = True
          # self.location:Location = Location(0,0)
          # self.size:Size = Size(0,0)
          self.viewport = ViewPort(location=Location(0,0), size=Size(0,0))
          self.margin: bool = True
          self.border: bool = True
          self.behaviour: UIBehaviour = UIBehaviour()
          self.name : str = ""


          # The widget manager.
          from pyretrogui.ui_elements.widget_manager import WidgetManager
          self._widget_manager = WidgetManager()


      def init(self,context: Context):
          self.viewport = LayoutManager().get_view_port(self)
          print("Test")



      @abstractmethod
      def draw(self, context: Context):
          """
          Draws the UI element.
          The drawing starts at the relative position (0,0), which will be translated
          by the drawing method into the absolute screen position.
          :param context: The rendering context.
          """
          pass



