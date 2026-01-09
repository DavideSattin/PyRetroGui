# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================

from pygame.event import Event
from pyretrogui.context import Context
from enum import Enum
from dataclasses import  dataclass
from pyretrogui.location import Location
from pyretrogui.size import Size
from pyretrogui.ui_elements.ui_element import UIElement


class WindowPosition(Enum):
      FREE = 0,
      CENTER_PARENT = 1,
      CENTER_SCREEN = 2,


class WindowSize(Enum):
      DOCK = 0
      FREE = 1


@dataclass
class ViewPort:
      location: Location = Location(0,0)
      size: Size = Size(0,0)


class UIPanel(UIElement):

      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)

      def on_key_event(self, event: Event,context: Context):
          pass

      def update(self, context: Context):
          pass

      def init(self,context: Context):
          pass

      def draw_border(self, context: Context):


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

          #Get the viewport location and size.
          view_port = self.get_viewport(context)

          view_port_line = 0
          current_location = view_port.location
          for current_line in text_content.split("\n"):

              context.draw_text(current_location, view_port.size, current_line)
              view_port_line += 1
              current_location = (view_port.location[0], view_port.location[1] + view_port_line)

      def draw_cursor(self, context: Context, cursor_position):
          context.draw_cursor(cursor_position)


