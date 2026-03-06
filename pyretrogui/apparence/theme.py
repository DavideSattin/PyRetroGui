# ==========================================
# Project: PyRetroGUI
# File: theme
# Author: Davide Sattin 
# Created: 19/01/2026 22:09
# Description: This file is a dataclass for theme.
# ==========================================
from dataclasses import dataclass, field
from typing import Optional, Tuple

Color = Optional[Tuple[int, int, int]]

@dataclass
class ThemeState:
    background: Color = None
    foreground: Color = None
    hover: Color = None
    active: Color = None
    disabled: Color = None
    focus: Color = None

@dataclass
class Theme:
    name: str
    cursor: Color = None
    pointer: Color = None
    primary: ThemeState = field(default_factory=ThemeState)
    secondary: ThemeState = field(default_factory=ThemeState)
    tertiary : ThemeState = field(default_factory=ThemeState)
    success: ThemeState = field(default_factory=ThemeState)
    info: ThemeState = field(default_factory=ThemeState)
    warning: ThemeState = field(default_factory=ThemeState)
    error: ThemeState = field(default_factory=ThemeState)