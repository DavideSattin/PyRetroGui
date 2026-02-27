# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================
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



      def draw(self, context: Context):
          pass

      def draw_border(self,context: Context, widget_viewport: ViewPort, foreground_color: tuple[int,int,int] = (255,255,255) , background_color: tuple[int,int,int] = (0,0,0) ) -> None:

          if context is None:
              raise ValueError("The size cannot be None.")

          if widget_viewport is None:
              raise ValueError("The widget_viewport cannot be None.")

          # we assume that a border it's a rectangle with
          # starting relative location ad 0,0 with the size of the panel.
          # The widget_viewport it's the viewport of the panel, and it's always a relative viewport.

          # So we need to translate the relative location 0,0 to the absolute window absolute_location.
          # the self.absolute_location of a panel is always an absolute absolute_location, because the framework need to
          # know the real position to draw.


          relative_viewport = widget_viewport.translate(self.location)

          rect_area = Area(relative_viewport)

          # Draw the top_left border
          context.draw_char(rect_area.top_left, CHAR_CLASSES["corner_tl"], foreground_color, background_color)

          # Draw the top_right border
          context.draw_char(rect_area.top_right, CHAR_CLASSES["corner_tr"],foreground_color, background_color )

          # Draw bottom_left border
          context.draw_char(rect_area.bottom_left, CHAR_CLASSES["corner_bl"],foreground_color, background_color)

          # Draw bottom_right border
          context.draw_char(rect_area.bottom_right, CHAR_CLASSES["corner_br"],foreground_color, background_color)

          # Draw the top line
          for tx in range(rect_area.top_left.x +1, rect_area.size.width - 1):
              lx = Location(tx,rect_area.top_left.y)
              context.draw_char(lx, CHAR_CLASSES["line_h"], foreground_color, background_color)

          # Draw the bottom line
          for tx in range(rect_area.bottom_left.x + 1, rect_area.size.width - 1):
              lx = Location(tx, rect_area.bottom_left.y)
              context.draw_char(lx, CHAR_CLASSES["line_h"], foreground_color, background_color)

          # Draw the left line
          for ty in range(rect_area.top_left.y + 1,  rect_area.top_left.y +  rect_area.size.height - 1):
              ly = Location(rect_area.top_left.x, ty)
              context.draw_char(ly, CHAR_CLASSES["line_v"], foreground_color, background_color)

          # Draw the right line
          for ty in range(rect_area.top_right.y + 1, rect_area.top_right.y + rect_area.size.height - 1):
              ly = Location(rect_area.top_right.x, ty)
              context.draw_char(ly, CHAR_CLASSES["line_v"], foreground_color, background_color)


      def draw_text(self,context: Context, text_content:str):
          # #Get the viewport absolute_location and size.
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
          context.start_cursor(cursor_position)

      def draw_background(self, context:Context, viewport:ViewPort, color:Color):
          if context is None:
              raise ValueError("The context cannot be None.")

          if viewport is None:
              raise ValueError("The viewport cannot be None.")

          context.fill_background(viewport,color)




