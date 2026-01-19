# ==========================================
# Project: PyRetroGUI
# File: theme_loader
# Author: Davide Sattin 
# Created: 19/01/2026 22:29
# Description:This class load the theme from yaml file.
# ==========================================
from pathlib import Path

from ruamel.yaml import YAML
from pyretrogui.apparence.theme import Theme, ThemeState


class ThemeLoader:

    @staticmethod
    def _to_color(val):
        if val is None:
            return None
        if isinstance(val, list):
            return tuple(val)
        return val


    @staticmethod
    def load(theme_name: str) -> Theme:
        if theme_name is None:
            raise ValueError('theme_name cannot be None')

        yaml = YAML()
        theme_name = theme_name.lower()
        theme_file_path = f"../assets/{theme_name}.yaml"

        theme_path = Path(theme_file_path)
        if not theme_path.exists():
            raise FileNotFoundError(f"Theme file not found: {theme_file_path}")

        # Load YAML
        with theme_path.open("r", encoding="utf-8") as f:
             data = yaml.load(f)

             # Crea ThemeState per primary e secondary
             primary_state = ThemeState(
                 background=ThemeLoader._to_color(data.get("primary", {}).get("background")),
                 foreground=ThemeLoader._to_color(data.get("primary", {}).get("foreground")),
                 hover=ThemeLoader._to_color(data.get("primary", {}).get("hover")),
                 active=ThemeLoader._to_color(data.get("primary", {}).get("active")),
                 disabled=ThemeLoader._to_color(data.get("primary", {}).get("disabled")),
                 focus=ThemeLoader._to_color(data.get("primary", {}).get("focus")),
             )

             secondary_state = ThemeState(
                 background=ThemeLoader._to_color(data.get("secondary", {}).get("background")),
                 foreground=ThemeLoader._to_color(data.get("secondary", {}).get("foreground")),
                 hover=ThemeLoader._to_color(data.get("secondary", {}).get("hover")),
                 active=ThemeLoader._to_color(data.get("secondary", {}).get("active")),
                 disabled=ThemeLoader._to_color(data.get("secondary", {}).get("disabled")),
                 focus=ThemeLoader._to_color(data.get("secondary", {}).get("focus")),
             )

             # Crea e restituisce Theme
             theme = Theme(
                 name=data.get("name", theme_name),
                 background_color=ThemeLoader._to_color(data.get("background_color")),
                 foreground_color=ThemeLoader._to_color(data.get("foreground_color")),
                 cursor_color=ThemeLoader._to_color(data.get("cursor_color")),
                 pointer_color=ThemeLoader._to_color(data.get("pointer_color")),
                 primary=primary_state,
                 secondary=secondary_state,
                 hover_color=ThemeLoader._to_color(data.get("hover_color")),
                 active_color=ThemeLoader._to_color(data.get("active_color")),
                 disabled_color=ThemeLoader._to_color(data.get("disabled_color")),
                 focus_color=ThemeLoader._to_color(data.get("focus_color")),
             )

             return theme
