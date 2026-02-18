# ==========================================
# Project: PyRetroGUI
# File: main_container
# Author: Davide Sattin 
# Created: 18/01/2026 19:17
# Description: The Main panel container.
# ==========================================
from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour
from pyretrogui.video.context import Context
from pyretrogui.ui_containers.dockable_container import DockableContainer
from pyretrogui.ui_containers.dockable_panel import DockablePanel
from pyretrogui.ui_elements.ui_element import UIElement


class MainContainer01(DockableContainer):

      def __init__(self, parent: UIElement):
          super().__init__(parent)
          self.margin = False
          self.border = False

      def init(self,context: Context):
          super().init(context)

          # Create the head container. Useful for menù or other stuff.
          header_container = DockablePanel(self)
          header_container.id = 12
          # header_container.margin = False
          # header_container.border = False
          header_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          header_container.behaviour.position_behaviour = PositionBehaviour.DOCKED_TOP
          header_container.size.height = 1
          super().add_child(header_container)

          # Create the Contents container. Useful for editor or other stuff.
          contents_container = DockablePanel(self)
          contents_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          contents_container.behaviour.position_behaviour = PositionBehaviour.CONTENT
          contents_container.background = (0, 255, 0)
          super().add_child(contents_container)


          # Create the footer container. Useful for status controls.
          footer_container = DockablePanel(self)
          footer_container.id= 13
          # footer_container.margin = False
          # footer_container.border = False
          footer_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          footer_container.behaviour.position_behaviour = PositionBehaviour.DOCKED_BOTTOM
          footer_container.size.height = 1
          footer_container.background = (255,0,0)
          super().add_child(footer_container)

