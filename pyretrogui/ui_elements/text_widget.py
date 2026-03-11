

from pyretrogui.appearance.widget_appearance import WidgetAppearance
from pyretrogui.arranger.layout_manager import LayoutManager
from pyretrogui.io.file_reader import FileReader
from pyretrogui.primitives.location import Location
from pyretrogui.video.context import Context
from pyretrogui.cursor_management import CursorManagement
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.ui_elements.ui_element import UIElement




class TextWidget(UIPanel):
      def __init__(self,parent: "UIElement" = None):
          super().__init__(parent)

          self.invalidate = True
          self.cursor_management:CursorManagement = CursorManagement(0,0)
          self.appearance = WidgetAppearance()

          #TODO: Remove This. It's only for test.
          self.text = FileReader.read_text_file("..\\lorem_ipsum.txt")



      def on_set_layout(self, context: Context):
          self.appearance.init_theme()
          super().on_set_layout(context)

          #THIS IS TOTALLY WRONG
          #view_port = self.get_internal_viewport()
          # Set the cursor position with the absolute_location of the internal viewport.
          self.cursor_management.location = Location(0,0)

      def init(self):
         super().init()
         print("Text Widget initialized.")

      # # TODO: Remove this.
      # def on_key_event(self, event: Event,context: Context):
      #     if event is None:
      #         raise Exception("Event cannot be None.")
      #
      #     # Get the internal viewport.
      #     view_port = self.get_internal_viewport(context)
      #
      #     match event.key:
      #         case pygame.K_UP:
      #             self.cursor_management.move_up(view_port)
      #         case pygame.K_DOWN:
      #             self.cursor_management.move_down(view_port)
      #         case pygame.K_LEFT:
      #             self.cursor_management.move_left(view_port)
      #         case pygame.K_RIGHT:
      #             self.cursor_management.move_right(view_port)
      #         case _:
      #             pass


      def draw(self, context: Context):
          """
          Draws the text widget.
          The drawing starts at the relative position (0,0), which will be translated
          by the drawing method into the absolute screen position.
          :param context: The rendering context.
          """
          # if not self.invalidate:
          #     return

          print("Draw Text")

          self.invalidate = False


          # The widget view_port it's relative to this widget.
          widget_relative_viewport = LayoutManager().get_relative_viewport(self.viewport)

          # Draw the background.
          super().draw_background(context, widget_relative_viewport,  self.appearance.background)

          # Draw the border.
          super().draw_border(context,widget_relative_viewport, self.appearance.foreground , self.appearance.background)

          # Draw the text, from the relative position 0,0

          text_viewport =  LayoutManager().get_relative_internal_viewport(self)
          super().draw_text(context,text_viewport, self.text)

          # The cursor position it's relative to the panel and it's viewport. At the moment it's fixed to (1,1)
          super().draw_cursor(context, self.cursor_management.location)

