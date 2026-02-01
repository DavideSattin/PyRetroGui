# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================

from pygame.event import Event

from pyretrogui.apparence.theme import Color
from pyretrogui.charset import CHAR_CLASSES
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.primitives.area import Area
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.ui_elements.ui_element import UIElement


class UIPanel(UIElement):

      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)

      def on_key_event(self, event: Event,context: Context):
          pass

      def update(self, context: Context):
          pass





      def draw_border(self,context: Context, size: Size ) -> None:

          if context is None:
              raise ValueError("The size cannot be None.")

          if size is None:
              raise ValueError("The size cannot be None.")

          # we assume that a border it's a rectangle with
          # starting relative location ad 0,0 with the size of the panel.
          # So we need to translate the relative location 0,0 to the absolute window location.
          # the self.location of a panel is always an absolute location, because the framework need to
          # know the real position to draw.

          relative_location = Location(0,0)
          rect_area = Area.create_area(relative_location, size)

          # Draw top_left border
          context.draw_char(rect_area.top_left, CHAR_CLASSES["corner_tl"])

          # Draw top_right border
          context.draw_char(rect_area.top_right, CHAR_CLASSES["corner_tr"])

          # Draw bottom_left border
          context.draw_char(rect_area.bottom_left, CHAR_CLASSES["corner_bl"])

          # Draw bottom_right border
          context.draw_char(rect_area.bottom_right, CHAR_CLASSES["corner_br"])




      def draw_text(self,context: Context, text_content:str):
          # #Get the viewport location and size.
          view_port = self.get_internal_viewport(context)

          current_location = view_port.location.translate_to(self.location)

          for current_line in text_content.split("\n"):
            if current_location.y <= view_port.size.height:
                context.draw_text(current_location, view_port.size, current_line)
                current_location = current_location.add_y(1)



      def draw_cursor(self, context: Context, cursor_position):
          if context is None:
              raise ValueError("The context cannot be None.")

          if cursor_position is None:
              raise ValueError("The cursor position cannot be None.")

          # Draw the cursor.
          context.draw_cursor(cursor_position)

      def draw_background(self, context:Context, viewport:ViewPort, color:Color):
          if context is None:
              raise ValueError("The context cannot be None.")

          if viewport is None:
              raise ValueError("The viewport cannot be None.")

          context.fill_background(viewport,color)




