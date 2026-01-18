# ==========================================
# Project: PyRetroGUI
# File: window_size
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description:
# ==========================================
from enum import Enum


class WindowSize(Enum):
      DOCK = 0          #The panel/control get the size of his parent
      FREE = 1          #The panel/control have is size.
      DOCk_WIDTH = 2    #The panel/control get the width of his parent but have is height.



