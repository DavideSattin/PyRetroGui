from abc import ABC, abstractmethod
from pyretrogui.arranger.position_behaviour import PositionBehaviour
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
          self.margin: bool = True
          self.border: bool = True
          self.behaviour: UIBehaviour = UIBehaviour()
          self.name : str = ""

          # The widget manager.
          from pyretrogui.ui_elements.widget_manager import WidgetManager
          self._widget_manager = WidgetManager()


      def init(self,context: Context):
          size = self.get_view_port(context)

          #TODO: uhm...why the viewport set the size?
          self.location = size.location
          self.size = size.size



      @abstractmethod
      def update(self,context: Context):
          pass


      def get_view_port(self, context: Context) -> ViewPort:
          # Manage the dock mode.
          match self.behaviour.position_behaviour:
              case PositionBehaviour.PARENT:
                  if self.parent is None:
                      raise Exception(f"Parent must be initialized.Id:{self.id}")

                  if self.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
                    raise Exception(f"Panel Mode: {self.behaviour.size_behaviour} not supported.")

                  # In this case the size of the panel must fit the internal view of the parent.
                  return self.parent.get_internal_viewport(context)

              case PositionBehaviour.DOCKED_TOP:
                  # if self.parent is None:
                  #     raise Exception(f"Parent must be initialized.Id:{self.id}")
                  #
                  # if self.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
                  #     raise Exception(f"Panel Mode: {self.behaviour.size_behaviour} not supported.")
                  #
                  # parent_viewport = self.parent.get_internal_viewport(context)
                  # new_size = Size(parent_viewport.size.width, self.size.height)
                  # return ViewPort(location=parent_viewport.location, size=new_size)
                  return ViewPort(location=self.location, size=self.size)

              case PositionBehaviour.DOCKED_BOTTOM:
                  # if self.parent is None:
                  #     raise Exception(f"Parent must be initialized.Id:{self.id}")
                  #
                  # if self.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
                  #     raise Exception(f"Panel Mode: {self.behaviour.size_behaviour} not supported.")
                  #
                  # parent_viewport = self.parent.get_internal_viewport(context)
                  #
                  # new_size = Size(parent_viewport.size.width, self.size.height)
                  # new_location = Location(parent_viewport.location.x, parent_viewport.size.height - new_size.height)
                  #
                  # return ViewPort(location=new_location, size=new_size)
                  return ViewPort(location=self.location, size=self.size)

              case PositionBehaviour.CONTENT:
                  return ViewPort(location=self.location, size=self.size)

              case _:
                  raise Exception(f"Panel Position Behaviour Mode: {self.behaviour.position_behaviour} not supported.")


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
