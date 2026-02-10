# ==========================================
# Project: PyRetroGUI
# File: window_position
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description:
# ==========================================
from enum import Enum


class PositionBehaviour(Enum):
      PARENT = 0
      FREE = 1,
      DOCKED_TOP = 2,
      DOCKED_BOTTOM = 3

