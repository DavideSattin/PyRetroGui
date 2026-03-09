# ==========================================
# Project: PyRetroGui
# File: layout_manager
# Author: Davide Sattin
# Created: 09/03/2026 10:57
# Description:
# Responsible for calculating the viewport
# of UI elements based on their layout
# behaviours (position and resize rules).
# ==========================================

from typing import TYPE_CHECKING

from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.singleton_meta.singleton_layout_manager import SingletonLayoutManager

# Import only for type checking to avoid circular imports
if TYPE_CHECKING:
    from pyretrogui.ui_elements.ui_element import UIElement


class LayoutManager(metaclass=SingletonLayoutManager):
    """
    Singleton class responsible for calculating viewports
    for UI elements according to their layout behaviours.
    """

    def __init__(self):
        pass

    # ============================
    # Private methods
    # ============================

    def _get_internal_viewport_raw(self, have_margin: bool, have_border: bool, viewport: ViewPort) -> ViewPort:
        """
        Calculates the internal viewport of a UI element.

        The internal viewport represents the drawable area of a control,
        excluding margins and borders.

        Args:
            have_margin (bool): Whether the element has margins.
            have_border (bool): Whether the element has a border.
            viewport (ViewPort): The outer viewport of the element.

        Returns:
            ViewPort: The calculated internal viewport.
        """
        offset = self._calculate_offset(have_border, have_margin)
        size = self._calculate_size(offset, viewport.size)
        start_relative_location = Location(
            viewport.location.x + offset,
            viewport.location.y + offset
        )
        return ViewPort(location=start_relative_location, size=size)

    def _calculate_size(self, offset: int, size: Size) -> Size:
        """
        Calculates the internal size by subtracting the offset from width and height.

        Args:
            offset (int): Total offset to subtract from each side.
            size (Size): Original size.

        Returns:
            Size: Adjusted size.
        """
        width = size.width - offset * 2
        height = size.height - offset * 2
        return Size(width, height)

    def _calculate_offset(self, have_border: bool, have_margin: bool) -> int:
        """
        Calculates the total offset caused by borders and margins.

        Args:
            have_border (bool): Whether a border is present.
            have_margin (bool): Whether a margin is present.

        Returns:
            int: Total offset value.
        """
        offset = 0
        if have_margin:
            offset += 1
        if have_border:
            offset += 1
        return offset

    def _get_internal_viewport(self, ui_element: "UIElement") -> ViewPort:
        """
        Convenience method to get the internal viewport for a UI element.

        Args:
            ui_element (UIElement): The element to calculate internal viewport for.

        Returns:
            ViewPort: Internal viewport excluding margins and borders.
        """
        return self._get_internal_viewport_raw(ui_element.margin, ui_element.border, ui_element.viewport)

    # ============================
    # Public methods
    # ============================

    def get_view_port(self, ui_element: "UIElement") -> ViewPort:
        """
        Calculates the viewport of a UI element based on its
        positioning behaviour.

        Args:
            ui_element (UIElement): The UI element to calculate the viewport for.

        Returns:
            ViewPort: The calculated viewport.

        Raises:
            ValueError: If ui_element is None.
            Exception: If unsupported behaviour or invalid parent configuration.
        """
        if ui_element is None:
            raise ValueError("The value ui_element cannot be None")

        match ui_element.behaviour.position_behaviour:

            case PositionBehaviour.PARENT:
                if ui_element.parent is None:
                    raise Exception(f"Parent must be initialized. Id:{ui_element.id}")

                if ui_element.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
                    raise Exception(f"Panel mode {ui_element.behaviour.size_behaviour} not supported.")

                return self._get_internal_viewport(ui_element.parent)

            case PositionBehaviour.DOCKED_TOP:
                return ui_element.viewport

            case PositionBehaviour.DOCKED_BOTTOM:
                return ui_element.viewport

            case PositionBehaviour.CONTENT:
                return ui_element.viewport

            case _:
                raise Exception(
                    f"Panel position behaviour mode {ui_element.behaviour.position_behaviour} not supported.")

    def get_relative_viewport(self, viewport: ViewPort) -> ViewPort:
        """
        Returns a viewport relative to the element (0,0).

        Args:
            viewport (ViewPort): The original viewport.

        Returns:
            ViewPort: A viewport with location set to (0,0) and same size.
        """
        if viewport is None:
            raise ValueError("The value viewport cannot be None")

        return ViewPort(location=Location(0, 0), size=viewport.size)

    def get_relative_internal_viewport(self, ui_element: "UIElement") -> ViewPort:
        """
        Returns the internal viewport relative to the element's origin (0,0).

        Args:
            ui_element (UIElement): The element to calculate relative internal viewport for.

        Returns:
            ViewPort: Internal viewport with location set to (0,0) and adjusted size.
        """
        offset = self._calculate_offset(ui_element.border, ui_element.margin)
        size = self._calculate_size(offset, ui_element.viewport.size)
        return ViewPort(location=Location(offset, offset), size=size)