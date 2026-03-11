# ==========================================
# Project: PyRetroGUI
# File: main_container_02.py
# Author: Davide Sattin
# Created: 18/01/2026 19:17
# Description: Example of a dockable container with top, bottom and two content panels.
# ==========================================
from pyretrogui.widgets.ui_containers import DockableContainer
from pyretrogui.widgets.ui_elements.ui_element import UIElement


class MainContainer02(DockableContainer):
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

        # Create the second content panel.
        contents_container02 = super()._create_dockable_content_panel("Container 2", (0, 255, 255))
        super().add_child(contents_container02)

        # Create the bottom footer panel.
        footer_container = super()._create_dockable_bottom_panel(1, "Footer Container", (255, 0, 0))
        super().add_child(footer_container)

        # Moving this call earlier causes an error.
        super().init()

