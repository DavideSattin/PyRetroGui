from abc import ABC, abstractmethod
from pygame.event import Event
from pyretrogui.context import Context
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.ui_elements.window_position import WindowPosition
from pyretrogui.ui_elements.window_size import WindowSize
from pyretrogui.primitives.view_port import ViewPort


class UIElement(ABC):
      def __init__(self,  parent: "UIElement" = None):
          self.parent = parent
          self.id : int = 0
          self.visible = True
          self.enabled = True
          self.location:Location = Location(0,0)
          self.size:Size = Size(0,0)
          self.margin = True
          self.border = True
          self.panel_position = WindowPosition.FREE
          self.panel_size = WindowSize.DOCK


      def init(self,context: Context):
          size = self.get_size(context)
          self.location = size.location
          self.size = size.size

      @abstractmethod
      def on_key_event(self,event:Event,context: Context):
          pass

      @abstractmethod
      def update(self,context: Context):
          pass


      def get_size(self,context: Context) -> ViewPort:
          # Manage the dock mode.
          if self.panel_size != WindowSize.DOCK:
              raise Exception(f"Panel Mode: {self.panel_size} not supported.")

          if self.parent is None:
              raise Exception(f"Parent must be initialized.Id:{self.id}")

          return self.parent.get_viewport(context)


      def get_viewport(self, context: Context) -> ViewPort:
          off_set = 0

          #If the panel have a margin or/and a border we need to calculate an offset of 1 box.
          if self.margin:
              off_set+=1

          if self.border:
              off_set+=1

          #Manage the dock mode.
          if self.panel_size != WindowSize.DOCK:
             raise Exception(f"Panel Mode: {self.panel_size} not supported.")

          if self.parent is None:
              #when??
              #check this case.
              return ViewPort(location=self.location,size=self.size)

          #The parent ViewPort.
          parent_viewport =  self.parent.get_viewport(context)

          location_x = parent_viewport.location.x + off_set
          location_y = parent_viewport.location.y + off_set

          width  = parent_viewport.size.width - off_set * 2
          height = parent_viewport.size.height - off_set * 2

          #my viewport
          return ViewPort(location=Location(location_x, location_y),size=Size(width, height))
