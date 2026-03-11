# ==========================================
# Project: PyRetroGUI
# File: container
# Author: Davide Sattin 
# Created: 11/03/2026 16:14
# Description:
# ==========================================
from abc import ABC
from typing import Optional

from pyretrogui.video.context import Context
from pyretrogui.widgets.ui_elements.ui_element import UIElement


class ContainerPanel(UIElement):

        def __init__(self, parent):
            super().__init__(parent)
            self.margin = False
            self.border = False
            self.child: Optional[UIElement] = None


        def init(self):
            super().init()

        def on_set_layout(self, context: Context):
            self.child.on_set_layout(context)

        def draw(self, context: Context):
            # Remove in the future. The draw call will not propagate by hierarchy calls.
            self.child.draw(context)

        def add_child(self, ui_element:UIElement):
            if ui_element is None:
                raise ValueError("ui_element cannot be None")

            if self.child is not None:
                raise Exception("ContainerPanel can only have one child")

            self.child = ui_element
