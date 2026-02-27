# ==========================================
# Project: PyRetroGUI
# File: dockable_container
# Author: Davide Sattin 
# Created: 18/01/2026 12:04
# Description: This class manage the dockable container.
# ==========================================
from typing import List

from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.video.context import Context
from pyretrogui.ui_containers.dockable_panel import DockablePanel
from pyretrogui.ui_elements.ui_element import UIElement


class DockableContainer(UIElement):

      def __init__(self, parent:UIElement):
        super().__init__(parent)
        self.containers: List[DockablePanel] = []

      def _arrange_(self, view_port: ViewPort):
          #TODO: All this code must be put into an Arrange Class.
          x = 0
          y = 0

          # Top containers are stacked vertically from the top.
          top_containers = [top_container for top_container  in self.containers if top_container.behaviour.position_behaviour ==  PositionBehaviour.DOCKED_TOP ]
          for top_container in top_containers:
              top_container.location.x = x
              top_container.location.y = y
              top_container.size.width = view_port.size.width
              y = y + top_container.size.height
              print(f"TOP - x:{top_container.location.x} - y:{top_container.location.y} - Size: {top_container.size}")

          top_containers_lower_position  = y


          # Top containers are stacked vertically from the bottom.
          # Calculate where we start to put the bottom containers.
          # We start from the higher y position calculated as the subtraction of panel total height with the sum of the height of bottom panel
          bottom_containers = [top_container for top_container in self.containers if top_container.behaviour.position_behaviour == PositionBehaviour.DOCKED_BOTTOM]
          bottom_containers_height = sum( container.size.height for container in bottom_containers)
          y = view_port.size.height - bottom_containers_height
          bottom_containers_higher_position = y
          for bottom_container in bottom_containers:
              bottom_container.location.x = x
              bottom_container.location.y = y
              bottom_container.size.width = view_port.size.width
              y = y + bottom_container.size.height

          # Arrange the content panels.
          content_containers = [top_container for top_container in self.containers if
                               top_container.behaviour.position_behaviour == PositionBehaviour.CONTENT]

          num_of_content_panels = len(content_containers)

          # The content_total_height it's the total vertical space for all the content containers.
          content_total_height = bottom_containers_higher_position - top_containers_lower_position
          size_for_panel = int(content_total_height / num_of_content_panels)

          y = top_containers_lower_position

          total_vertical_space_allocated = 0
          for content_container_idx in range(num_of_content_panels):
              content_container = content_containers[content_container_idx]

              content_container.location.x = x
              content_container.location.y = y
              content_container.size.width = view_port.size.width

              if content_container_idx != num_of_content_panels - 1:

                  content_container.size.height = size_for_panel
                  y = y + content_container.size.height
                  total_vertical_space_allocated = total_vertical_space_allocated +  content_container.size.height
              else:

                  delta = content_total_height - total_vertical_space_allocated
                  if delta > size_for_panel:
                      size_for_panel = delta

                  content_container.size.height = size_for_panel
                  y = y + content_container.size.height
                  total_vertical_space_allocated = total_vertical_space_allocated + content_container.size.height

              print(f"Content - x:{content_container.location.x} - y:{content_container.location.y} - Size: {content_container.size}")

          # for content_container in content_containers:
          #
          #     content_container.location.x = x
          #     content_container.location.y = y
          #     content_container.size.height = size_for_panel
          #     content_container.size.width = view_port.size.width
          #     y = y + content_container.size.height
          #     print(f"Content - x:{content_container.location.x} - y:{content_container.location.y} - Size: {content_container.size}")

      def _create_dockable_top_panel(self, height:int, name: str = "", color: tuple[int,int, int] = None )-> DockablePanel:
          if height<=0:
              raise ValueError("height cannon be less or equal to zero.")

          container = DockablePanel(self)
          container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          container.behaviour.position_behaviour = PositionBehaviour.DOCKED_TOP
          container.size.height = height
          container.name = name
          container.background = color
          return container

      def _create_dockable_content_panel(self,name: str = "", color: tuple[int,int, int] = None) -> DockablePanel:
          # Create the Contents container 01. Useful for editor or other stuff.
          container = DockablePanel(self)
          container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          container.behaviour.position_behaviour = PositionBehaviour.CONTENT
          container.name = name
          container.background = color
          return  container

      def _create_dockable_bottom_panel(self,height:int, name: str = "", color: tuple[int,int, int] = None )-> DockablePanel:
          if height<=0:
              raise ValueError("height cannon be less or equal to zero.")

          # Create the footer container. Useful for status controls.
          container = DockablePanel(self)

          container.behaviour.size_behaviour = ResizeBehaviour.BUBBLE
          container.behaviour.position_behaviour = PositionBehaviour.DOCKED_BOTTOM
          container.size.height = height
          container.name = name
          container.background = color
          return  container

      def init(self, context:Context):
          self._arrange_(self.get_view_port(context))
          for container in self.containers:
              container.init(context)

      def draw(self, context: Context):
          # Before to call update we need to calculate/arrange the panels position and size.
          # self._arrange_(self.get_view_port(context))
          for container in self.containers:
              container.draw(context)
              pass

      def add_child(self, child: DockablePanel):
          if child is None:
              raise ValueError("Cannot add a child of None")

          child = self._widget_manager.element_ingestion(child,root=self)
          self.containers.append(child)


