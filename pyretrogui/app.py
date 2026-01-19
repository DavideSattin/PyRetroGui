# ==========================================
# Project: PyRetroGUI
# File: app
# Author: Davide Sattin 
# Created: 04/01/2026 10:45
# Description: The main app for UI.
# ==========================================
from typing import Optional
import pygame

from pyretrogui.charset import CHAR_CLASSES
from pyretrogui.context import Context
from pyretrogui.graphic_context import GraphicContext
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.ui_elements.ui_panel import UIPanel


class App:
      def __init__(self, title:str, size:tuple[int, int]=(100,200), font_size:tuple[int, int]=(8,16)):
          self.grp_ctx = GraphicContext()
          self.mouse_pos: Optional[tuple[int, int]] = None
          self.font_size = font_size
          #Calculate the font perfect size
          width = int(size[0] / font_size[0]) * font_size[0]
          height = int(size[1] / font_size[1]) * font_size[1]

          #Virtual Root control.
          self.root = UIPanel(None)
          self.root.margin = False
          self.root.border = False
          self.root.location = Location(0,0)
          self.root.size = Size(int(width / font_size[0]), int(height/font_size[1]))

          # Open the window
          normalized_size = (width, height)
          self.grp_ctx.open_window(title, normalized_size)

          print(f"Normalized size: {normalized_size}")
          print(self.root.size)

          self.running = True
          self.widget: Optional[UIPanel] = None
          self.context = Context(size, font_size, normalized_size)

      def _element_factory(self, element):
          if element is None:
              raise ValueError('element cannot be None')

          ui_element = element(self.root)
          ui_element.id = 1
          ui_element.init(self.context)
          return ui_element


      def run(self,startup_widget) -> None:
          self.widget = self._element_factory(startup_widget)

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
                       self.widget.on_key_event(event, self.context)



      def update(self):
          self.widget.update(self.context)

      def draw(self):
          #Draw background
          self.grp_ctx.fill()

          #Draw the widget
          self.context.draw(self.grp_ctx)

          #Draw the mouse pointer
          self.draw_mouse_pointer()

          # Draw all.
          self.grp_ctx.flush()

      def draw_mouse_pointer(self):
          self.mouse_pos = pygame.mouse.get_pos()
          if self.mouse_pos is not None:
             pos_x = max(int(self.mouse_pos[0] / self.font_size[0]),0)
             pos_y = max(int(self.mouse_pos[1] / self.font_size[1]),0)

             mouse_location = Location(pos_x, pos_y)
             self.context.draw_char(mouse_location, CHAR_CLASSES["fill_full"])
