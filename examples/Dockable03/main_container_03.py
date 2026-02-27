# ==========================================
# Project: PyRetroGUI
# File: main_container_03
# Author: Davide Sattin 
# Created: 22/02/2026 18:09
# Description:
# ==========================================
from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour
from pyretrogui.ui_containers.dockable_container import DockableContainer
from pyretrogui.ui_containers.dockable_panel import DockablePanel
from pyretrogui.ui_elements.text_widget import TextWidget
from pyretrogui.ui_elements.ui_element import UIElement
from pyretrogui.video.context import Context


class MainContainer03(DockableContainer):

      def __init__(self, parent: UIElement):
          super().__init__(parent)
          self.margin = False
          self.border = False

      def init(self,context: Context):

          # Create the header container.
          header_container = super()._create_dockable_top_panel(1, "Top Container", (0,0,255))
          super().add_child(header_container)


          # Create the Contents container 01. Useful for editor or other stuff.
          contents_container01 = super()._create_dockable_content_panel("Container 1", (0, 255, 0) )
          super().add_child(contents_container01)
          txt1 = TextWidget()
          txt1.text = "Hello World 1"

          contents_container01.add_child(txt1)

          # Create the Contents container 02. Useful for editor or other stuff.
          contents_container02 = super()._create_dockable_content_panel("Container 1", (0, 255, 255))
          super().add_child(contents_container02)
          txt2 = TextWidget()
          txt2.text = "Hello World 2"

          contents_container02.add_child(txt2)

          # Create the footer container. Useful for status controls.
          footer_container = super()._create_dockable_bottom_panel(1, "Footer Container", (255,0,0))
          super().add_child(footer_container)

          super().init(context)