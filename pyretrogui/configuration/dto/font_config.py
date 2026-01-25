# ==========================================
# Project: PyRetroGUI
# File: font_config
# Author: Davide Sattin 
# Created: 25/01/2026 18:07
# Description: Dto class for font configuration.
# ==========================================
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class FontConfig:
    font_size: Tuple[int, int]
    font_path: str


