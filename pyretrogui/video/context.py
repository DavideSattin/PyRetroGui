# ==========================================
# Project: PyRetroGUI
# File: Context
# Author: Davide Sattin 
# Created: 04/01/2026 18:02
# Description:
# ==========================================
from pyretrogui.apparence.theme import Theme
from pyretrogui.cursor_context import CursorContext
from pyretrogui.graphic_context import GraphicContext
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.video_buffer import VideoBuffer, Color


class Context:
      def __init__(self, theme: Theme, size:tuple[int, int], font_size: tuple[int, int], normalized_size:tuple[int, int]):
          #TODO: Check None!

          self.theme = theme
          self.size = size
          self.font_size = font_size
          self.normalized_size = normalized_size
          self.pointer_buffer: Location | None = None

          #We start maybe from the wrong assumption that the size it's static
          #but in the case we have a floating and resizable windows container, the context must be recreated.
          self.rows = int(normalized_size[1] / font_size[1])
          self.cols = int(normalized_size[0] / font_size[0])

          self.video_buffer : VideoBuffer = VideoBuffer(self.cols, self.rows)
          #self.matrix: list[list[str]] = [[" " for _ in range(self.cols)]for _ in range(self.rows)]

          self.cursor = CursorContext(0,0)
          self.clear()

      def clear(self):
          self.video_buffer.clear()




      def paint(self, graphics: GraphicContext) -> None :
          # probably this method it's on GC.

          cell_w, cell_h = self.font_size
          for row_idx in range(self.rows):
              for col_idx in range(self.cols):
                  if self.video_buffer.is_dirty(row_idx, col_idx):
                      print(f"is dirty x: {row_idx} y: {col_idx}")

                      #opss don't remove....
                      x = col_idx * cell_w
                      y = row_idx * cell_h

                      #get the background color.
                      back_color = self.video_buffer.get_background_color(row_idx, col_idx)
                      if back_color is None:
                          back_color = self.theme.background_color

                      # get the foreground color.
                      fore_ground_color = self.video_buffer.get_foreground_color(row_idx, col_idx)
                      if fore_ground_color is None:
                          fore_ground_color = self.theme.foreground_color

                      #get the char.
                      current_char = self.video_buffer.get_char(row_idx, col_idx)

                      #draw all
                      graphics.draw_char(current_char, x, y,fore_ground_color, back_color)

                      self.video_buffer.align_buffer(col_idx, row_idx)


      def draw_cursor(self, graphics):
          cell_w, cell_h = self.font_size
          # Check this.
          if self.cursor.cursor_visible:
              cursor_x = self.cursor.location.x * cell_w
              cursor_y = self.cursor.location.y * cell_h
              graphics.draw_char(self.cursor.get_cursor_char(), cursor_x, cursor_y)
          else:
              self.video_buffer.invalidate(self.cursor.location.y, self.cursor.location.x)

      def draw_mouse_pointer(self,graphics: GraphicContext,normalized_location: Location,video_location: Location,color=(255, 255, 255)):
          """
          Draws the mouse pointer and invalidates the previous cell if needed.
          """

          # If a previous pointer position exists, check whether it has changed
          if self.pointer_buffer is not None:
              old_x, old_y = self.pointer_buffer.x, self.pointer_buffer.y
              new_x, new_y = video_location.x, video_location.y

              # Optional debug output
              # print(f"Buffer: {old_x} {old_y}")
              # print(f"Video:  {new_x} {new_y}")

              # Invalidate the previous cell if the pointer moved
              if (old_x, old_y) != (new_x, new_y):
                  print(f"Invalidate: {old_x} {old_y}")
                  self.video_buffer.invalidate(old_y, old_x)

          # Always update the pointer buffer to the new position
          self.pointer_buffer = Location(video_location.x, video_location.y)

          # Draw the cursor character at the normalized screen location
          graphics.draw_char(
              self.cursor.get_cursor_char(),
              normalized_location.x,
              normalized_location.y,
              color
          )

      def draw_char(self, location:Location, char: str, foreground_color: tuple[int,int,int] = (255,255,255) , background_color: tuple[int,int,int] = (0,0,0)) -> None:
          if location is None:
              raise  ValueError("Parameter: location cannot be None.")

          if char is None:
              raise ValueError("Parameter: char cannot be None.")

          if len(char) > 1:
              raise ValueError("Parameter: char cannot be more than one character.")

          if location.x >= self.cols or location.y >= self.rows:
              raise ValueError("Location is out of bounds.")

          self.video_buffer.write(char, location, background_color, foreground_color)



      def draw_text(self, draw_location:Location, view_port_size:Size, current_line:str):
          # The size it's necessary....
          current_line = current_line[:view_port_size.width]

          row_offset = draw_location.y
          col_offset = draw_location.x

          try:
              buffer_line = self.video_buffer.get_buffer_row(row_offset)
              for col, char in enumerate(current_line):
                  x = col_offset + col
                  buffer_line[x] = char
          except Exception as e:
               print(f"Exception while drawing line.")



      def start_cursor(self, cursor_position:Location)-> None:
          self.cursor.start_cursor()
          self.cursor.location = cursor_position

      def fill_background(self, viewport:ViewPort, color: Color) -> None:

          for row_idx in range(viewport.location.y,viewport.location.y+ viewport.size.height):
              for col_idx in range(viewport.location.x, viewport.location.x + viewport.size.width):
                   self.video_buffer.set_background_color(row_idx,col_idx, color)


