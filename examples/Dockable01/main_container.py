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

class MainContainer(DockableContainer):
      def __init__(self, parent: UIElement):
          super().__init__(parent)

      def init(self,context: Context):

          #Create the menu container.
          menu_container = DockablePanel(self)
          menu_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          menu_container.behaviour.position_behaviour = PositionBehaviour.DOCKED_TOP
          menu_container.size.height = 1

          super().add_child(menu_container)

          # # Create the Content container.
          # main_container = DockablePanel(self)
          # main_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          # super().add_child(main_container)
          #
          # #Create the status container.
          # status_container = DockablePanel(self)
          # status_container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          # menu_container.behaviour.position_behaviour = PositionBehaviour.DOCKED_BOTTOM
          # status_container.size.height = 1
          #
          # super().add_child(status_container)

