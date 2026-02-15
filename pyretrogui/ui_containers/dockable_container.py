# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin 
# Created: 18/01/2026 12:04
# Description: This class manage the dockable container.
# ==========================================
from typing import List

from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.primitives.size import Size
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.ui_containers.dockable_panel import DockablePanel
from pyretrogui.ui_elements.ui_element import UIElement


class DockableContainer(UIElement):

      def __init__(self, parent:UIElement):
        super().__init__(parent)
        self.containers: List[DockablePanel] = []

      def _arrange_(self, view_port: ViewPort):

          x = 0
          y = 0

          # Top containers are stacked vertically from the top.
          top_containers = [top_container for top_container  in self.containers if top_container.behaviour.position_behaviour ==  PositionBehaviour.DOCKED_TOP ]
          for top_container in top_containers:
              top_container.location.x = x
              top_container.location.y = y
              y = y + top_container.size.height

          container_top  = y


          # Top containers are stacked vertically from the bottom.
          # Calculate where we start to put the bottom containers.
          bottom_containers = [top_container for top_container in self.containers if top_container.behaviour.position_behaviour == PositionBehaviour.DOCKED_BOTTOM]
          bottom_containers_height = sum( container.size.height for container in bottom_containers)
          y = view_port.size.height - bottom_containers_height
          for bottom_container in bottom_containers:
              bottom_container.location.x = x
              bottom_container.location.y = y
              y = y + bottom_container.size.height

          container_bottom = y

          # Arrange the content panels.
          content_containers = [top_container for top_container in self.containers if
                               top_container.behaviour.position_behaviour == PositionBehaviour.CONTENT]

          num_of_content_panels = len(content_containers)
          content_height = container_bottom - container_top
          size_for_panel = content_height / num_of_content_panels

          y = container_top
          for content_container in content_containers:
              content_container.location.x = x
              content_container.location.y = y
              content_container.size.height = size_for_panel
              y = y + content_container.size.height




      def update(self, context: Context):
          # Before to call update we need to calculate/arrange the panels position and size.
          self._arrange_(self.get_view_port(context))
          for container in self.containers:
              container.update(context)
              pass

      def add_child(self, child: DockablePanel):
          if child is None:
              raise ValueError("Cannot add a child of None")
          #
          # if child.parent is not None:
          #     raise ValueError("The panel already has a parent")

          child.parent = self

          self.containers.append(child)