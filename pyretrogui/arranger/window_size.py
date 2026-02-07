# ==========================================
# Project: PyRetroGUI
# File: window_size
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description:
# ==========================================
from enum import Enum


class WindowSize(Enum):
      BUBBLE = 0        #The panel/control get the size of his parent
      FREE = 1          #The panel/control have is size and can be resized.
      FIXED = 2         #The panel/control have is size and cannot be resized.



