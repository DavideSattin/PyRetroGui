# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin 
# Created: 18/01/2026 12:04
# Description:
# ==========================================
from typing import List

from pygame.event import Event

from pyretrogui.video.context import Context
from pyretrogui.ui_containers.dockable_panel import DockablePanel
from pyretrogui.ui_elements.ui_element import UIElement


class DockableContainer(UIElement):

      def __init__(self, parent:UIElement):
        super().__init__(parent)
        self.containers: List[DockablePanel] = []



      def update(self, context: Context):
          for container in self.containers:
              container.update(context)


      def add_child(self, child: DockablePanel):
          if child is None:
              raise ValueError("Cannot add a child of None")
          #
          # if child.parent is not None:
          #     raise ValueError("The panel already has a parent")

          child.parent = self

          self.containers.append(child)