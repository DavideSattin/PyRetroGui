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

    def __init__(self):
        pass

    def get_view_port(self, ui_element: "UIElement") -> ViewPort:

        if ui_element is None:
            raise ValueError("The value ui_element cannot be None")

        # Determine the viewport according to the element's positioning behaviour
        match ui_element.behaviour.position_behaviour:

            # The element occupies the internal viewport of its parent
            case PositionBehaviour.PARENT:

                if ui_element.parent is None:
                    raise Exception(f"Parent must be initialized. Id:{ui_element.id}")

                if ui_element.behaviour.size_behaviour != ResizeBehaviour.BUBBLE:
                    raise Exception(f"Panel mode {ui_element.behaviour.size_behaviour} not supported.")

                # In this mode the element automatically fits the parent's internal viewport
                return self._get_internal_viewport(ui_element.parent)

            # Element docked at the top of its container
            case PositionBehaviour.DOCKED_TOP:
                return ViewPort(location=ui_element.location, size=ui_element.size)

            # Element docked at the bottom of its container
            case PositionBehaviour.DOCKED_BOTTOM:
                return ViewPort(location=ui_element.location, size=ui_element.size)

            # Element positioned inside the content area
            case PositionBehaviour.CONTENT:
                return ViewPort(location=ui_element.location, size=ui_element.size)

            case _:
                raise Exception( f"Panel position behaviour mode {ui_element.behaviour.position_behaviour} not supported.")

    def _get_internal_viewport(self, ui_element: "UIElement") -> ViewPort:
        """
        Calculates the internal viewport of a UI element.

        The internal viewport represents the drawable area of a control,
        excluding margins and borders.
        """

        offset = 0

        # Each visual layer reduces the drawable space
        if ui_element.margin:
            offset += 1

        if ui_element.border:
            offset += 1

        # The viewport location is relative to the control itself
        start_relative_location = Location(
            ui_element.location.x + offset,
            ui_element.location.y + offset
        )

        # Recalculate the internal size by removing the offsets
        width = ui_element.size.width - offset * 2
        height = ui_element.size.height - offset * 2

        return ViewPort(
            location=start_relative_location,
            size=Size(width, height)
        )