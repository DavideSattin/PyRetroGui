# ==========================================
# Project: PyRetroGUI
# File: mouse
# Author: Davide Sattin 
# Created: 25/01/2026 18:08
# Description: DTO class for mouse configuration.
# ==========================================
from dataclasses import dataclass


@dataclass(frozen=True)
class MouseConfig:
    enabled: bool
    pointer: bool
