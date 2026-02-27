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

          # Create the head container. Useful for menù or other stuff.
          header_container = super()._create_dockable_top_panel(1, "Top Container", (0, 0, 255))
          super().add_child(header_container)

          # Create the Contents container. Useful for editor or other stuff.
          contents_container01 = super()._create_dockable_content_panel("Container 1", (0, 255, 0))
          super().add_child(contents_container01)

          # Create the footer container. Useful for status controls.
          footer_container = super()._create_dockable_bottom_panel(1, "Footer Container", (255, 0, 0))
          super().add_child(footer_container)

          # Se sposto prima va in errore.
          super().init(context)
