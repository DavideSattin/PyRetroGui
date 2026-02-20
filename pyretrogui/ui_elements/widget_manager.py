# ==========================================
# Project: PyRetroGui
# File: widget_manager
# Author: Davide Sattin
# Created: 20/02/2026 22:50
# Description:This class manage all the widget, panels
# ==========================================
from typing import List
from pyretrogui.singleton_meta import SingletonMeta
from pyretrogui.ui_elements.ui_element import UIElement


class WidgetManager(metaclass=SingletonMeta):
       def __init__(self):
           # TODO: Dovrebbe essere un dizionario.
           self.widgets : List[UIElement] = []

       def element_factory(self, element, context,root: UIElement = None) -> UIElement:
           if element is None:
               raise ValueError('element cannot be None')

           if context is None:
               raise ValueError('context cannot be None')

           ui_element = element(root)
           ui_element.id = len(self.widgets) + 1
           ui_element.init(context)

           self.widgets.append(ui_element)
           return ui_element

       def element_ingestion(self, element: UIElement, context, root: UIElement = None) -> UIElement:
           if element is None:
               raise ValueError('element cannot be None')
           if context is None:
               raise ValueError('context cannot be None')

           element.id = len(self.widgets) + 1
           element.parent = root
           element.init(context)

           self.widgets.append(element)
           return element