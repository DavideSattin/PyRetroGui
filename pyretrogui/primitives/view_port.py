# ==========================================
# Project: PyRetroGUI
# File: view_port
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description:
# ==========================================
from dataclasses import dataclass

from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size


@dataclass
class ViewPort:
      absolute_location: Location = Location(0, 0)
      size: Size = Size(0,0)
