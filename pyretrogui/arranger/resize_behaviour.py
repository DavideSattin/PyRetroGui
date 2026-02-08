# ==========================================
# Project: PyRetroGUI
# File: window_size
# Author: Davide Sattin 
# Created: 10/01/2026 19:09
# Description: This enum specify the resize behaviour.
# ==========================================
from enum import Enum


class ResizeBehaviour(Enum):
      BUBBLE = 0        #The panel/control get the size of his parent and can be resized
      FREE = 1          #The panel/control have is size and can be resized.
      FIXED = 2         #The panel/control have is size and cannot be resized.



