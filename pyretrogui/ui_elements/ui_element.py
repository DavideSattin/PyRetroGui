from abc import ABC, abstractmethod
from pygame.event import Event

from pyretrogui.arranger.ui_behaviour import UIBehaviour
from pyretrogui.video.context import Context
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour
from pyretrogui.primitives.view_port import ViewPort


class UIElement(ABC):
      def __init__(self,  parent: "UIElement" = None):
          self.parent: UIElement = parent
          self.id : int = 0
          self.visible = True
          self.enabled = True
          self.location:Location = Location(0,0)
          self.size:Size = Size(0,0)
          self.margin = True
          self.border = True
          self.behaviour: UIBehaviour = UIBehaviour()



      def init(self,context: Context):
          size = self.get_size(context)
          self.location = size.location
          self.size = size.size



      @abstractmethod
      def update(self,context: Context):
          pass


      def get_size(self,context: Context) -> ViewPort:
          # Manage the dock mode.
          if self.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
              raise Exception(f"Panel Mode: {self.behaviour.size_behaviour} not supported.")

          if self.parent is None:
              raise Exception(f"Parent must be initialized.Id:{self.id}")


          return self.parent.get_internal_viewport(context)
          # return ViewPort(location=Location(0, 0), size=Size(self.size.width,  self.size.height))

      def get_internal_viewport(self, context: Context) -> ViewPort:
          # The internal viewport is an internal control area, without margin or border.
          # It tell how much space the control have to draw itself.

          off_set = 0

          #If the panel have a margin or/and a border we need to calculate an offset of 1 box.
          if self.margin:
              off_set+=1

          if self.border:
              off_set+=1

          # The location of the view port are relative of the control in itself.
          start_relative_location = Location(off_set,off_set)

          # Recalculate the Size.
          width  = self.size.width - off_set * 2
          height = self.size.height - off_set * 2

          return ViewPort(location=Location(off_set, off_set),size=Size(width, height))

          # #Manage the dock mode.
          # if self.size_behaviour != WindowSize.DOCK:
          #    raise Exception(f"Panel Mode: {self.size_behaviour} not supported.")
          #
          # relative_location = Location(off_set, off_set)
          #
          # if self.parent is None:
          #     #when??
          #     #check this case.
          #
          #     return ViewPort(absolute_location=self.location, relative_location=relative_location, size=self.size)
          #
          # #The parent ViewPort.
          # parent_viewport =  self.parent.get_internal_viewport(context)
          #
          # location_x = parent_viewport.absolute_location.x + off_set
          # location_y = parent_viewport.absolute_location.y + off_set
          #
          # width  = parent_viewport.size.width - off_set * 2
          # height = parent_viewport.size.height - off_set * 2
          #
          # #my viewport
          # return ViewPort(absolute_location=Location(location_x, location_y), relative_location=relative_location,size=Size(width, height))
