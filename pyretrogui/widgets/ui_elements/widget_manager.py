# ==========================================
# Project: PyRetroGui
# File: widget_manager
# Author: Davide Sattin
# Created: 20/02/2026 22:50
# Description:This class manage all the widget, panels
# ==========================================
from typing import List, Container

from pyretrogui.primitives.location import Location
from pyretrogui.singleton_meta.singleton_meta_widget_manager import SingletonMetaWidgetManager
from pyretrogui.widgets.ui_containers.container_panel import ContainerPanel
from pyretrogui.widgets.ui_elements.ui_element import UIElement
from pyretrogui.video.context import Context


class WidgetManager(metaclass=SingletonMetaWidgetManager):
       def __init__(self):
           # TODO: Probably the list is not really correct. Maybe a dictionary?
           # TODO: change the name of self.widgets. I don't like the UIElement name.
           self.widgets : List[UIElement] = []

       def _ensure_element_initialized(self, element: UIElement) -> None:
            if not element.initialized:
               element.init()
               element.initialized = True

       def register_element(self, element: UIElement, root: UIElement = None) -> UIElement:
           if element is None:
               raise ValueError('element_type cannot be None')

           element.id = len(self.widgets) + 1
           element.parent = root

           self.widgets.append(element)
           return element

       def element_factory(self, element_type, context:Context, root: ContainerPanel) -> UIElement:
           if element_type is None:
               raise ValueError('element_type cannot be None')

           if context is None:
               raise ValueError('context cannot be None')

           if root is None:
               raise ValueError('root cannot be None')

           element = element_type(root)
           element.id = len(self.widgets) + 1

           root.add_child(element)
           self._ensure_element_initialized(element)
           element.on_set_layout(context)

           self.widgets.append(element)
           return element


       def element_ingestion(self, element: UIElement, context:Context,root: ContainerPanel) -> UIElement:
           if element is None:
               raise ValueError('element_type cannot be None')

           if context is None:
              raise ValueError('Context cannot be None')

           if root is None:
               raise ValueError('root cannot be None')

           element.id = len(self.widgets) + 1
           element.parent = root

           root.add_child(element)
           self._ensure_element_initialized(element)
           element.on_set_layout(context)


           self.widgets.append(element)
           return element

       def get_element_from_location(self, location:Location) -> UIElement | None:
           if location is None:
               raise ValueError("location cannot be None")

           ordered  = sorted(self.widgets, key=lambda w: w.viewport.z_index, reverse=True)

           return next(
               (w for w in ordered if w.enabled and w.viewport.match(location)),
               None
           )