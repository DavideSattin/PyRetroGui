# ==========================================
# Project: PyRetroGUI
# File: graphic_context
# Author: Davide Sattin 
# Created: 05/01/2026 09:19
# Description: The graphic context is wrapper of py game
# ==========================================
import pygame


class GraphicContext:
      def __init__(self):
          pygame.init()
          self.screen = None
          self.clock = pygame.time.Clock()

          self.main_font = pygame.font.Font(
              "../assets/Ac437_IBM_VGA_8x16.ttf",
              16
          )

      def _ensure_screen(self):
          assert self.screen is not None, "Window not opened"

      def open_window(self,title: str, normalized_size):
          self.screen = pygame.display.set_mode(normalized_size)
          pygame.display.set_caption(title)

      def set_clock_tick(self, tick : int):
          self.clock.tick(tick)

      def get_events(self):
          return pygame.event.get()

      def flush(self):
          if self.screen is None:
              return
          pygame.display.flip()

      def draw_char(self, char:str, x: int, y: int, color=(255, 255, 255)):
          surface = self.main_font.render(str(char), True, color)
          self.screen.blit(surface, (x, y))

      def fill(self, color=(0, 0, 0)):
          self.screen.fill(color)

      def quit(self):
          if pygame.get_init():
              pygame.quit()
