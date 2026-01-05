# ==========================================
# Project: PyRetroGUI
# File: Context
# Author: Davide Sattin 
# Created: 04/01/2026 18:02
# Description:
# ==========================================
from pyretrogui.graphic_context import GraphicContext


class Context:
      def __init__(self, size, font_size, normalized_size):
          self.font = None
          self.size = size
          self.font_size = font_size
          self.normalized_size = normalized_size

          self.rows = int(normalized_size[1] / font_size[1])
          self.cols = int(normalized_size[0] / font_size[0])
          self.matrix = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
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
                # screen.blit(pygame.font.FONT.render(char, True, (255, 255, 255)), (x, y))

