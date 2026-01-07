# ==========================================
# Project: PyRetroGUI
# File: app
# Author: Davide Sattin 
# Created: 04/01/2026 10:45
# Description: The main app for UI.
# ==========================================
import pygame

from pyretrogui.context import Context
from pyretrogui.graphic_context import GraphicContext
from pyretrogui.ui_panel import UIPanel, UIElement


class App:
      def __init__(self, title:str, size=(100,200), font_size=(8,16)):
          self.grp_ctx = GraphicContext()

          #Calculate the font perfect size
          width = int(size[0] / font_size[0]) * font_size[0]
          height = int(size[1] / font_size[1]) * font_size[1]
          normalized_size = (width, height)

          #Virtual Root control.
          self.root = UIPanel(None)
          self.root.margin = False
          self.root.border = False
          self.root.location = (0,0)
          self.root.size = normalized_size

          # Open the window
          self.grp_ctx.open_window(title, normalized_size)

          self.running = True
          self.widget = None
          self.context = Context(size, font_size, normalized_size)

      def run(self,startup_widget) -> None:
          self.widget = startup_widget(self.root)

          #Running Cycle.
          while self.running:
              self.handle_events()
              self.update()
              self.draw()
              self.grp_ctx.set_clock_tick(60)

          #Exit
          self.grp_ctx.quit()

      def handle_events(self):
          for event in self.grp_ctx.get_events():
              match event.type:
                  case pygame.QUIT:
                      self.running = False
                  case pygame.KEYDOWN | pygame.KEYUP:
                       self.widget.OnKeyEvent(event)

              # if event.type == pygame.QUIT:
              #     self.running = False

      def update(self):
          self.widget.update(self.context)

      def draw(self):
          #Draw background
          self.grp_ctx.fill()

          #Draw the widget
          self.context.draw(self.grp_ctx)

          # Draw all.
          self.grp_ctx.flush()
