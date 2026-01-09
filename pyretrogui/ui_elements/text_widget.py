from pygame.event import Event

from pyretrogui.context import Context
from pyretrogui.io.file_reader import FileReader
from pyretrogui.location import Location
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.ui_elements.ui_element import UIElement


class TextWidget(UIPanel):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)
          self.margin = False
          self.border = True
          self.cursor_position:Location =Location(0,0)

          # self.text = "Hello World!"
          self.text = FileReader.read_text_file("lorem_ipsum.txt")


      def init(self,context: Context):
          view_port = self.get_viewport(context)
          self.cursor_position.x = view_port.location[0]
          self.cursor_position.y = view_port.location[1]

      def on_key_event(self, event: Event,context: Context):
          if event is None:
              raise Exception("Event cannot be None.")

          match event.keysym:
              case "Up":
                  self.move_up()
              case "Down":
                  self.move_down()
              case "Left":
                  self.move_left()
              case "Right":
                  self.move_right()
              case _:
                  pass


      def update(self,context: Context):
          super().draw_border(context)
          super().draw_text(context, self.text)
          super().draw_cursor(context, (1,1))
