# ==========================================
# Project: PyRetroGUI
# File: theme_loader
# Author: Davide Sattin
# Created: 19/01/2026 22:29
# Description: This class loads the theme from yaml file.
# ==========================================
from pathlib import Path
from ruamel.yaml import YAML

from pyretrogui.apparence.theme import Theme, ThemeState
from pyretrogui.io.utils import asset_path


class ThemeLoader:

    @staticmethod
    def _to_color(val):
        if val is None:
            return None
        if isinstance(val, list):
            return tuple(val)
        return val

    @staticmethod
    def _load_state(data: dict, name: str) -> ThemeState:
        s = data.get(name, {}) or {}

        return ThemeState(
            background=ThemeLoader._to_color(s.get("background")),
            foreground=ThemeLoader._to_color(s.get("foreground")),
            hover=ThemeLoader._to_color(s.get("hover")),
            active=ThemeLoader._to_color(s.get("active")),
            disabled=ThemeLoader._to_color(s.get("disabled")),
            focus=ThemeLoader._to_color(s.get("focus"))
        )

    @staticmethod
    def default_theme() -> Theme:

        def_state = ThemeState(
            background=(0, 0, 0),
            foreground=(255, 255, 255),
            hover=(40, 40, 40),
            active=(80, 80, 80),
            disabled=(100, 100, 100),
            focus=(255, 255, 0),
        )

        return Theme(
            name="default",
            cursor=(255, 255, 255),
            pointer=(255, 165, 0),
            primary=def_state,
            secondary=def_state,
            tertiary=ThemeState(),
            success=ThemeState(),
            info=ThemeState(),
            warning=ThemeState(),
            error=ThemeState(),
        )

    @staticmethod
    def load(theme_name: str) -> Theme:

        if theme_name is None:
            return ThemeLoader.default_theme()

        yaml = YAML()
        theme_name = theme_name.lower()

        theme_file_path = asset_path(theme_name)
        theme_path = Path(f"{theme_file_path}.yaml")

        if not theme_path.exists():
            raise FileNotFoundError(f"Theme file not found: {theme_file_path}")

        with theme_path.open("r", encoding="utf-8") as f:
            data = yaml.load(f)

        return Theme(
            name=data.get("name", theme_name),

            cursor=ThemeLoader._to_color(data.get("cursor")),
            pointer=ThemeLoader._to_color(data.get("pointer")),

            primary=ThemeLoader._load_state(data, "primary"),
            secondary=ThemeLoader._load_state(data, "secondary"),
            tertiary=ThemeLoader._load_state(data, "tertiary"),
            success=ThemeLoader._load_state(data, "success"),
            info=ThemeLoader._load_state(data, "info"),
            warning=ThemeLoader._load_state(data, "warning"),
            error=ThemeLoader._load_state(data, "error"),
        )