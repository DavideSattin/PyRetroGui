# ==========================================
# Project: PyRetroGUI
# File: unit
# Author: Davide Sattin 
# Created: 11/03/2026 23:04
# Description: Defines the measurement units used for positioning and sizing UI elements.
# ==========================================
from enum import Enum


class Unit(Enum):
      """Enumeration of measurement units for UI layout."""
      Grid8  = 1   # 8x8 grid
      Grid16 = 2   # 8x16 grid
      Pixel  = 3   # Pixel unit