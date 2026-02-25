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
              print(f"TOP - x:{top_container.location.x} - y:{top_container.location.y}")
          container_top  = y


          # Top containers are stacked vertically from the bottom.
          # Calculate where we start to put the bottom containers.
          bottom_containers = [top_container for top_container in self.containers if top_container.behaviour.position_behaviour == PositionBehaviour.DOCKED_BOTTOM]
          bottom_containers_height = sum( container.size.height for container in bottom_containers)
          y = view_port.size.height - bottom_containers_height
          for bottom_container in bottom_containers:
              bottom_container.location.x = x
              bottom_container.location.y = y
              bottom_container.size.width = view_port.size.width
              y = y + bottom_container.size.height

          container_bottom = y

          # Arrange the content panels.
          content_containers = [top_container for top_container in self.containers if
                               top_container.behaviour.position_behaviour == PositionBehaviour.CONTENT]

          num_of_content_panels = len(content_containers)
          content_height = container_bottom - container_top
          size_for_panel = int(content_height / num_of_content_panels)

          y = container_top
          for content_container in content_containers:
              content_container.location.x = x
              content_container.location.y = y
              content_container.size.height = size_for_panel
              content_container.size.width = view_port.size.width
              y = y + content_container.size.height
              print(f"Content - x:{content_container.location.x} - y:{content_container.location.y}")

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

      def update(self, context: Context):
          # Before to call update we need to calculate/arrange the panels position and size.
          # self._arrange_(self.get_view_port(context))
          for container in self.containers:
              container.update(context)
              pass

      def add_child(self, child: DockablePanel):
          if child is None:
              raise ValueError("Cannot add a child of None")

          child = self._widget_manager.element_ingestion(child,root=self)
          self.containers.append(child)


