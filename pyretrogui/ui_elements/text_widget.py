import pygame
from pygame.event import Event

from pyretrogui.context import Context
from pyretrogui.cursor_management import CursorManagement
from pyretrogui.io.file_reader import FileReader
from pyretrogui.primitives.location import Location
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.ui_elements.ui_element import UIElement


class TextWidget(UIPanel):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)
          self.margin = False
          self.border = True
          self.cursor_management:CursorManagement = CursorManagement(0,0)

          # self.text = "Hello World!"
          self.text = FileReader.read_text_file("lorem_ipsum.txt")


      def init(self,context: Context):
          super().init(context)
          view_port = self.get_internal_viewport(context)
          # Set the cursor position with the location of the internal viewport.
          self.cursor_management.location = view_port.location


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


      def update(self,context: Context):
          #Draw the panel border, of the specified size. The location it's local 0,0.
          super().draw_border(self.size, context)
          super().draw_text(context, self.text)

          # The cursor position it's relative to the panel and it's viewport. At the moment it's fixed to (1,1)
          #super().draw_cursor(context, self.cursor_management.location)
