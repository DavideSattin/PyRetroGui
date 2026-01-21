# ==========================================
# Project: PyRetroGUI
# File: main_container
# Author: Davide Sattin 
# Created: 18/01/2026 19:17
# Description: The Main panel container.
# ==========================================

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
          menu_container.behaviour.set_dockable_width()
          menu_container.size.height = 1

          super().containers.append(menu_container)