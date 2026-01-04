# ==========================================
# Project: PyRetroGUI
# File: app
# Author: Davide Sattin 
# Created: 04/01/2026 10:45
# Description: The main app for UI.
# ==========================================
import pygame

from pyretrogui.Context import Context


class App:
      def __init__(self, title:str, size=(100,200), font_size=(8,16)):
          pygame.init()

          width = int(size[0] / font_size[0]) * font_size[0]
          height = int(size[1] / font_size[1]) * font_size[1]
          normalized_size = (width, height)

          self.screen = pygame.display.set_mode(normalized_size)
          pygame.display.set_caption(title)
          self.clock = pygame.time.Clock()
          self.running = True
          self.widget = None
          self.context = Context(size, font_size, normalized_size)

      def run(self,startup_widget) -> None:
          self.widget = startup_widget()

          while self.running:
              self.handle_events()
              self.update()
              self.draw()
              self.clock.tick(60)

          pygame.quit()

      def handle_events(self):
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  self.running = False

      def update(self):
          pass

      def draw(self):
          self.context.draw(pygame, self.screen)

          # font = pygame.font.Font(
          #     "../assets/Ac437_IBM_VGA_8x16.ttf",
          #     16
          # )
          # cell_w, cell_h = font.size(" ")
          # print(cell_w, cell_h)

          self.screen.fill((0, 0, 0))
          pygame.display.flip()