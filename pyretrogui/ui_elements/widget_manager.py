# ==========================================
# Project: PyRetroGui
# File: widget_manager
# Author: Davide Sattin
# Created: 20/02/2026 22:50
# Description:This class manage all the widget, panels
# ==========================================
from typing import List

from pyretrogui.singleton_meta.singleton_meta_widget_manager import SingletonMetaWidgetManager
from pyretrogui.ui_elements.ui_element import UIElement
from pyretrogui.video.context import Context


class WidgetManager(metaclass=SingletonMetaWidgetManager):
       def __init__(self):
           # TODO: Dovrebbe essere un dizionario.
           self.widgets : List[UIElement] = []

       def _ensure_element_initialized(self, element: UIElement) -> None:
            if not element.initialized:
               element.init()
               element.initialized = True

       def element_factory(self, element, context:Context,root: UIElement = None) -> UIElement:
           if element is None:
               raise ValueError('element cannot be None')

           if context is None:
               raise ValueError('context cannot be None')

           ui_element = element(root)
           ui_element.id = len(self.widgets) + 1
           self._ensure_element_initialized(ui_element)
           ui_element.on_set_layout(context)

           self.widgets.append(ui_element)
           return ui_element

       def register_element(self, element: UIElement,  root: UIElement = None)-> UIElement:
           if element is None:
               raise ValueError('element cannot be None')

           element.id = len(self.widgets) + 1
           element.parent = root

           self.widgets.append(element)
           return element

       def element_ingestion(self, element: UIElement, context:Context=None, root: UIElement = None) -> UIElement:
           if element is None:
               raise ValueError('element cannot be None')

           if context is None:
              raise ValueError('Context cannot be None')

           element.id = len(self.widgets) + 1
           element.parent = root

           self._ensure_element_initialized(element)

           if context is not None:
              element.on_set_layout(context)


           self.widgets.append(element)
           return element