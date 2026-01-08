# ==========================================
# Project: PyRetroGUI
# File: UIPanel
# Author: Davide Sattin 
# Created: 04/01/2026 17:47
# Description:Base class for UI panels.
# ==========================================
from encodings import search_function

from pygame.event import Event

from pyretrogui.charset import CHAR_CLASSES
from abc import ABC, abstractmethod
from pyretrogui.context import Context
from enum import Enum
from pyretrogui.io.file_reader import FileReader
from dataclasses import  dataclass

class WindowPosition(Enum):
      Free = 0,
      CenterParent = 1,
      CenterScreen = 2,


class WindowSize(Enum):
      Dock = 0
      Free = 1


@dataclass
class ViewPort:
      location: tuple[int,int]
      size: tuple[int,int]

class UIElement(ABC):
      def __init__(self,  parent: "UIElement" = None):
          self.parent = parent
          self.visible = True
          self.enabled = True
          self.location:tuple[int, int] = (0,0)
          self.size:tuple[int, int] = (10,10)
          self.margin = True
          self.border = True
          self.panel_position = WindowPosition.Free
          self.panel_size = WindowSize.Dock

      @abstractmethod
      def on_key_event(self,event:Event):
          pass

      @abstractmethod
      def update(self,context: Context):
          pass

      def get_viewport(self, context: Context) -> ViewPort:
          off_set = 0

          #If the panel have a margin or/and a border we need to calculate an offset of 1 box.
          if self.margin:
              off_set+=1

          if self.border:
              off_set+=1

          #Manage the dock mode.
          if self.panel_size != WindowSize.Dock:
             raise Exception(f"Panel Mode: {self.panel_size} not supported.")

          if self.parent is None:
              #when??
              return ViewPort(location=self.location,size=(int(self.size[0] / context.font_size[0]), int(self.size[1] / context.font_size[1])))


          #The parent ViewPort.
          parent_viewport =  self.parent.get_viewport(context)

          view_port_location_x = parent_viewport.location[0] + off_set
          view_port_location_y = parent_viewport.location[1] + off_set

          view_port_size_x = parent_viewport.size[0] - off_set * 2
          view_port_size_y = parent_viewport.size[1] - off_set * 2

          #my viewport
          return ViewPort(location=(view_port_location_x, view_port_location_y),size=(view_port_size_x, view_port_size_y))





class UIPanel(UIElement):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)

      def on_key_event(self, event: Event):
          pass

      def update(self, context: Context):
          pass


      def draw_border(self, context: Context):
          context.matrix[0][0] = CHAR_CLASSES["corner_tl"]
          context.matrix[0][-1] = CHAR_CLASSES["corner_tr"]
          context.matrix[-1][0] = CHAR_CLASSES["corner_bl"]
          context.matrix[-1][-1] = CHAR_CLASSES["corner_br"]

          # Draw vertical lines.
          for y in range(1, context.rows - 1):
              context.matrix[y][0] = CHAR_CLASSES["line_v"]
              context.matrix[y][-1] = CHAR_CLASSES["line_v"]

          # Draw horizontal lines.
          for x in range(1, context.cols - 1):
              context.matrix[0][x] = CHAR_CLASSES["line_h"]
              context.matrix[-1][x] = CHAR_CLASSES["line_h"]

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


class TextWidget(UIPanel):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)
          self.margin = False
          self.border = True
          # self.text = "Hello World!"
          self.text = FileReader.read_text_file("lorem_ipsum.txt")

      def update(self,context: Context):
          super().draw_border(context)
          super().draw_text(context, self.text)
          super().draw_cursor(context, (1,1))