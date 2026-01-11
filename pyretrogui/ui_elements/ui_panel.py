# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================

from pygame.event import Event
from pyretrogui.charset import CHAR_CLASSES
from pyretrogui.context import Context
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



      def draw_border(self, size: Size, context: Context):
          if size is None:
              raise ValueError("The size cannon be None.")

          if context is None:
              raise ValueError("The size cannon be None.")

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



          # context.matrix[0][0] = CHAR_CLASSES["corner_tl"]
          # context.matrix[0][-1] = CHAR_CLASSES["corner_tr"]
          # context.matrix[-1][0] = CHAR_CLASSES["corner_bl"]
          # context.matrix[-1][-1] = CHAR_CLASSES["corner_br"]
          #
          # # Draw vertical lines.
          # for y in range(1, context.rows - 1):
          #     context.matrix[y][0] = CHAR_CLASSES["line_v"]
          #     context.matrix[y][-1] = CHAR_CLASSES["line_v"]
          #
          # # Draw horizontal lines.
          # for x in range(1, context.cols - 1):
          #     context.matrix[0][x] = CHAR_CLASSES["line_h"]
          #     context.matrix[-1][x] = CHAR_CLASSES["line_h"]

      def draw_text(self,context: Context, text_content:str):

          # #Get the viewport location and size.
          view_port = self.get_internal_viewport(context)

          current_location = view_port.absolute_location.translate_to(self.location)

          for current_line in text_content.split("\n"):
            if current_location.y < view_port.size.height:
                context.draw_text(current_location, view_port.size, current_line)
                current_location = current_location.add_y(1)

          # #Get the viewport location and size.
          # view_port = self.get_viewport(context)
          #
          # view_port_line = 0
          # current_location = view_port.absolute_location.translate_to(self.location)
          #
          # for current_line in text_content.split("\n"):
          #
          #     context.draw_text(current_location, view_port.size, current_line)
          #     view_port_line += 1
          #     #current_location = (view_port.location[0], view_port.location[1] + view_port_line)
          #     current_location = current_location.add_y(view_port_line)
          #
          #     # Prevent to draw outside the panel.
          #     if current_location.y >  self.size.height:
          #         break


      def draw_cursor(self, context: Context, cursor_position):
          context.draw_cursor(cursor_position)


