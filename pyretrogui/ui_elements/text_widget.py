import pygame
from pygame.event import Event

from pyretrogui.io.file_reader import FileReader
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.cursor_management import CursorManagement
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.ui_elements.ui_element import UIElement


class TextWidget(UIPanel):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)
          self.margin = False
          self.border = True
          self.invalidate = True
          self.cursor_management:CursorManagement = CursorManagement(0,0)
          #TODO: Remove This. It's only for test.
          self.text = FileReader.read_text_file("..\\lorem_ipsum.txt")



      def init(self,context: Context):
          # Refactor this!
          # We need to write the panel absolute_location and size
          # based on his behaviour  self.position_behaviour = PositionBehaviour.FREE
          #           self.size_behaviour = WindowSize.DOCK

          super().init(context)
          view_port = self.get_internal_viewport(context)
          # Set the cursor position with the absolute_location of the internal viewport.
          self.cursor_management.location = view_port.location


      # TODO: Remove this.
      def on_key_event(self, event: Event,context: Context):
          if event is None:
              raise Exception("Event cannot be None.")

          # Get the internal viewport.
          view_port = self.get_internal_viewport(context)

          match event.key:
              case pygame.K_UP:
                  self.cursor_management.move_up(view_port)
              case pygame.K_DOWN:
                  self.cursor_management.move_down(view_port)
              case pygame.K_LEFT:
                  self.cursor_management.move_left(view_port)
              case pygame.K_RIGHT:
                  self.cursor_management.move_right(view_port)
              case _:
                  pass


      def draw(self, context: Context):
          # if not self.invalidate:
          #     return

          print("DRAW")

          self.invalidate = False

          # Draw the panel border,of the specified size. The absolute_location it's local 0,0, and the size it's the size of the panel.
          widget_viewport = ViewPort(location=Location(0,0), size= self.size)

          # The draw_border function expects a local viewport as a parameter, internally it calculates the absolute absolute_location.

          super().draw_background(context, widget_viewport, (0,0,255))
          super().draw_border(context,widget_viewport, (255,255,255) , (0,0,255))
          super().draw_text(context, self.text)

          # The cursor position it's relative to the panel and it's viewport. At the moment it's fixed to (1,1)
          super().draw_cursor(context, self.cursor_management.location)

