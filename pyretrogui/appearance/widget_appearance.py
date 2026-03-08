# ==========================================
# Project: PyRetroGUI
# File: widget_appearance
# Author: Davide Sattin 
# Created: 08/03/2026 15:18
# Description: Provides a base class for UI element appearance management, 
#              handling different color modes (Primary, Secondary, etc.) 
#              and custom color states derived from a Theme.
# ==========================================
from enum import Enum
from typing import Optional
from pyretrogui.appearance.theme import ThemeState, Theme
from pyretrogui.events.theme_events_dispatcher import ThemeEventsDispatcher


class WidgetAppearanceMode(Enum):
    """
    Enumeration of available appearance modes for a widget.
    
    Attributes:
        CUSTOM: Allows manual color overrides.
        PRIMARY: Uses the primary theme colors.
        SECONDARY: Uses the secondary theme colors.
        TERTIARY: Uses the tertiary theme colors.
        SUCCESS: Uses success-state theme colors.
        INFO: Uses informational theme colors.
        WARNING: Uses warning-state theme colors.
        ERROR: Uses error-state theme colors.
    """
    CUSTOM = 0
    PRIMARY = 1
    SECONDARY = 2
    TERTIARY = 3
    SUCCESS = 4
    INFO = 5
    WARNING = 6
    ERROR = 7

class WidgetAppearance:
    """
    Manages the visual appearance of a UI widget based on a selected mode or custom settings.
    
    This class acts as a bridge between the global Theme and individual widgets, 
    providing access to colors for different states (background, foreground, hover, etc.).
    """
    def __init__(self, mode: WidgetAppearanceMode = WidgetAppearanceMode.PRIMARY) -> None:
        """
        Initializes the appearance with a specific mode.
        
        Args:
            mode: The appearance mode to use (default is CUSTOM).
        """
        self.mode = mode
        self._custom_theme_state: Optional[ThemeState] = None
        self._theme_state: Optional[ThemeState] = None
        self._theme_events_dispatcher = ThemeEventsDispatcher()
        self.theme: Theme = self._theme_events_dispatcher.publish_event_get_theme(self)
        self.set_theme_state()

    @property
    def background(self) -> tuple[int,int,int]:
        """Returns the background color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.background
        return self._theme_state.background

    @background.setter
    def background(self, new_value: tuple[int,int,int]):
        """Sets a custom background color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.background = new_value

    @property
    def foreground(self) -> tuple[int, int, int]:
        """Returns the foreground/text color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.foreground
        return self._theme_state.foreground

    @foreground.setter
    def foreground(self, new_value: tuple[int, int, int]):
        """Sets a custom foreground color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.foreground = new_value

    @property
    def hover(self) -> tuple[int, int, int]:
        """Returns the hover state color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.hover
        return self._theme_state.hover

    @hover.setter
    def hover(self, new_value: tuple[int, int, int]):
        """Sets a custom hover color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.hover = new_value

    @property
    def active(self) -> tuple[int, int, int]:
        """Returns the active/pressed state color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.active
        return self._theme_state.active

    @active.setter
    def active(self, new_value: tuple[int, int, int]):
        """Sets a custom active color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.active = new_value

    @property
    def focus(self) -> tuple[int, int, int]:
        """Returns the focus state color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.focus
        return self._theme_state.focus

    @focus.setter
    def focus(self, new_value: tuple[int, int, int]):
        """Sets a custom focus color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.focus = new_value

    @property
    def disabled(self) -> tuple[int, int, int]:
        """Returns the disabled state color (R, G, B) for the current mode."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            return self._custom_theme_state.disabled
        return self._theme_state.disabled

    @disabled.setter
    def disabled(self, new_value: tuple[int, int, int]):
        """Sets a custom disabled color (only applicable in CUSTOM mode)."""
        if self.mode == WidgetAppearanceMode.CUSTOM:
            self._custom_theme_state.disabled = new_value

    def set_theme_state(self):
        """
        Synchronizes the appearance state with the current theme based on the selected mode.
        If in CUSTOM mode, it initializes the custom state with primary theme colors as defaults.
        """
        match self.mode:
            case WidgetAppearanceMode.CUSTOM:
                self._custom_theme_state = ThemeState()
                self._custom_theme_state.background = self.theme.primary.background
                self._custom_theme_state.foreground = self.theme.primary.foreground
                self._custom_theme_state.hover = self.theme.primary.hover
                self._custom_theme_state.active = self.theme.primary.active
                self._custom_theme_state.disabled = self.theme.primary.disabled
                self._custom_theme_state.focus = self.theme.primary.focus
            case WidgetAppearanceMode.PRIMARY:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.primary.background
                self._theme_state.foreground = self.theme.primary.foreground
                self._theme_state.hover = self.theme.primary.hover
                self._theme_state.active = self.theme.primary.active
                self._theme_state.disabled = self.theme.primary.disabled
                self._theme_state.focus = self.theme.primary.focus
            case WidgetAppearanceMode.SECONDARY:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.secondary.background
                self._theme_state.foreground = self.theme.secondary.foreground
                self._theme_state.hover = self.theme.secondary.hover
                self._theme_state.active = self.theme.secondary.active
                self._theme_state.disabled = self.theme.secondary.disabled
                self._theme_state.focus = self.theme.secondary.focus
            case WidgetAppearanceMode.TERTIARY:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.tertiary.background
                self._theme_state.foreground = self.theme.tertiary.foreground
                self._theme_state.hover = self.theme.tertiary.hover
                self._theme_state.active = self.theme.tertiary.active
                self._theme_state.disabled = self.theme.tertiary.disabled
                self._theme_state.focus = self.theme.tertiary.focus
            case WidgetAppearanceMode.SUCCESS:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.success.background
                self._theme_state.foreground = self.theme.success.foreground
                self._theme_state.hover = self.theme.success.hover
                self._theme_state.active = self.theme.success.active
                self._theme_state.disabled = self.theme.success.disabled
                self._theme_state.focus = self.theme.success.focus
            case WidgetAppearanceMode.INFO:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.info.background
                self._theme_state.foreground = self.theme.info.foreground
                self._theme_state.hover = self.theme.info.hover
                self._theme_state.active = self.theme.info.active
                self._theme_state.disabled = self.theme.info.disabled
                self._theme_state.focus = self.theme.info.focus
            case WidgetAppearanceMode.WARNING:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.warning.background
                self._theme_state.foreground = self.theme.warning.foreground
                self._theme_state.hover = self.theme.warning.hover
                self._theme_state.active = self.theme.warning.active
                self._theme_state.disabled = self.theme.warning.disabled
                self._theme_state.focus = self.theme.warning.focus
            case WidgetAppearanceMode.ERROR:
                self._theme_state = ThemeState()
                self._theme_state.background = self.theme.error.background
                self._theme_state.foreground = self.theme.error.foreground
                self._theme_state.hover = self.theme.error.hover
                self._theme_state.active = self.theme.error.active
                self._theme_state.disabled = self.theme.error.disabled
                self._theme_state.focus = self.theme.error.focus
       
        