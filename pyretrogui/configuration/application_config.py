# ==========================================
# Project: PyRetroGUI
# File: application_config
# Author: Davide Sattin 
# Created: 25/01/2026 18:09
# Description:
# ==========================================
from dataclasses import dataclass
from typing import Tuple

from pyretrogui.configuration.font_config import FontConfig
from pyretrogui.configuration.mouse import MouseConfig


@dataclass(frozen=True)
class ApplicationConfig:
    title: str
    size: Tuple[int, int]
    font: FontConfig
    mouse: MouseConfig
    theme: str
