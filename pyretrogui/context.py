# ==========================================
# Project: PyRetroGUI
# File: Context
# Author: Davide Sattin 
# Created: 04/01/2026 18:02
# Description:
# ==========================================
from pyretrogui.cursor_context import CursorContext
from pyretrogui.graphic_context import GraphicContext
from pyretrogui.location import Location
from pyretrogui.size import Size


class Context:
      def __init__(self, size:tuple[int, int], font_size: tuple[int, int], normalized_size):
          self.font = None
          self.size = size
          self.font_size = font_size
          self.normalized_size = normalized_size

          self.rows = int(normalized_size[1] / font_size[1])
          self.cols = int(normalized_size[0] / font_size[0])
          self.matrix: list[list[str]] = [[" " for _ in range(self.cols)]for _ in range(self.rows)]
          self.cursor = CursorContext(0,0)
          self.clear()

      def clear(self):
          for row_idx, row in enumerate(self.matrix):
              for col_idx in range(len(row)):
                  row[col_idx] = ' '  # oppure 0 o None

      def draw(self, graphics: GraphicContext):
          cell_w, cell_h = self.font_size
          for  row_idx, row in enumerate(self.matrix):
            for col_idx, char in enumerate(row):
                # row_idx = indice riga
                # col_idx = indice colonna
                # char = contenuto della cella
                x = col_idx * cell_w
                y = row_idx * cell_h


                graphics.draw_char(str(char), x, y)
                if self.cursor.cursor_visible:
                    cursor_x = self.cursor.location.x * cell_w
                    cursor_y = self.cursor.location.y * cell_h
                    graphics.draw_char(self.cursor.get_cursor_char() , cursor_x, cursor_y)
                # screen.blit(pygame.font.FONT.render(char, True, (255, 255, 255)), (x, y))

      def draw_char(self, location:Location, char: str) -> None:
          if location is None:
              raise  ValueError("Parameter: location cannot be None.")

          if char is None:
              raise ValueError("Parameter: char cannot be None.")

          if len(char) > 1:
              raise ValueError("Parameter: char cannot be more than one character.")

          self.matrix[location.x][location.y] = char



      def draw_text(self, view_port_location:Location, view_port_size:Size, current_line:str):
          # The size it's necessary....
          current_line = current_line[:view_port_size.width]

          row_offset = view_port_location.y
          col_offset = view_port_location.x

          matrix_line = self.matrix[row_offset]

          for col, char in enumerate(current_line):
              x = col_offset + col
              if x >= len(matrix_line):
                  break
              matrix_line[x] = char

      def draw_cursor(self, cursor_position):
          self.cursor.start_cursor()
          self.cursor.location.x = cursor_position[0]
          self.cursor.location.y = cursor_position[1]