# ==========================================
# Project: PyRetroGUI
# File: view_port
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description:
# ==========================================
from dataclasses import dataclass

from pyretrogui.location import Location
from pyretrogui.size import Size


@dataclass
class ViewPort:
      location: Location = Location(0,0)
      size: Size = Size(0,0)
