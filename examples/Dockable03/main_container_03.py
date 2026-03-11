# ==========================================
# Project: PyRetroGUI
# File: main_container_03.py
# Author: Davide Sattin
# Created: 22/02/2026 18:09
# Description: Example of a dockable container with top, bottom and two content panels.
# ==========================================
from pyretrogui.widgets.ui_containers.dockable_container import DockableContainer
from pyretrogui.widgets.ui_elements.text_widget import TextWidget
from pyretrogui.widgets.ui_elements.ui_element import UIElement


class MainContainer03(DockableContainer):
    """
    A custom dockable container demonstrating the use of top, bottom, and multiple content panels.
    """

    def __init__(self, parent: UIElement):
        super().__init__(parent)
        self.margin = False
        self.border = False

    def init(self):
        """
        Initializes the container by creating and adding dockable panels.
        """
        # Create the top header panel.
        header_container = super()._create_dockable_top_panel(1, "Top Container", (0, 0, 255))
        super().add_child(header_container)

        # Create the first content panel.
        contents_container01 = super()._create_dockable_content_panel("Container 1", (0, 255, 0))
        super().add_child(contents_container01)
        txt1 = TextWidget()
        txt1.text = "Hello World 1"
        contents_container01.add_child(txt1)

        # Create the second content panel.
        contents_container02 = super()._create_dockable_content_panel("Container 2", (0, 255, 255))
        super().add_child(contents_container02)
        txt2 = TextWidget()
        txt2.text = "Hello World 2"
        contents_container02.add_child(txt2)

        # Create the bottom footer panel.
        footer_container = super()._create_dockable_bottom_panel(1, "Footer Container", (255, 0, 0))
        super().add_child(footer_container)

        super().init()