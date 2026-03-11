# ==========================================
# Project: PyRetroGUI
# File: app
# Author: Davide Sattin 
# Created: 04/01/2026 10:45
# Description: The main application for the user interface.
# ==========================================
from ast import Suite
from typing import Optional
import pygame

from pyretrogui.appearance.theme_loader import ThemeLoader
from pyretrogui.configuration.configuration import Configuration
from pyretrogui.configuration.dto.application_config import ApplicationConfig
from pyretrogui.events.application_resize_event_dispatcher import ApplicationResizeEventDispatcher
from pyretrogui.events.event_args import EventArgs
from pyretrogui.events.theme_events_dispatcher import ThemeEventsDispatcher
from pyretrogui.primitives.view_port import ViewPort
from pyretrogui.singleton_meta.singleton_meta_app import SingletonMetaApp
from pyretrogui.ui_elements.widget_manager import WidgetManager
from pyretrogui.video.context import Context
from pyretrogui.graphic_context import GraphicContext
from pyretrogui.primitives.location import Location
from pyretrogui.primitives.size import Size
from pyretrogui.ui_elements.ui_panel import UIPanel
from pyretrogui.ui_elements.ui_element import UIElement


class App(metaclass=SingletonMetaApp):
    """
    Main application class for PyRetroGUI.
    Manages the main application loop, events, and rendering.
    Implements the Singleton pattern via SingletonMetaApp.
    """
    _allow_init = False

    # -----------------------
    # STATIC METHODS
    # -----------------------

    @staticmethod
    def create_instance(title: str, size: tuple[int, int] = (100, 200), font_size: tuple[int, int] = (8, 16)):
        """
        Creates and returns the singleton instance of the application.
        """
        App._allow_init = True
        try:
            return App(title, size, font_size)
        finally:
            App._allow_init = False

    # -----------------------
    # INITIALIZATION
    # -----------------------

    def __init__(self, title: str, client_size: tuple[int, int] = None, client_font_size: tuple[int, int] = None):
        """
        Initializes the application. Must be called via create_instance.
        """
        if not App._allow_init:
            raise RuntimeError("Use App.CreateInstance.")

        self._initialized = False
        self.widget_manager = None

        # Subscription to app events.
        theme_dispatcher = ThemeEventsDispatcher()
        theme_dispatcher.subscribe_event_get_theme(self, self._get_theme)

        app_viewport_dispatcher = ApplicationResizeEventDispatcher()
        app_viewport_dispatcher.subscribe_event_viewport_resize(self, self._on_application_resize)

        # Configuration.
        self.config: ApplicationConfig = Configuration.load()

        # Settings from configuration or defaults.
        self.title = self.config.title

        # Set default sizes.
        self.size: Size  = self._set_size_values((100, 200), client_size, self.config.size)
        self.font_size : Size = self._set_size_values((8, 16), client_font_size, self.config.font.font_size)

        # Mouse management.
        self.mouse_enable = self.config.mouse.enabled  # Enable the mouse
        self.mouse_pointer = self.config.mouse.pointer  # Show the mouse pointer.
        # TODO: Change to Location
        self.mouse_pos: Optional[tuple[int, int]] = None

        # Theme loading.
        self.theme = ThemeLoader.load(self.config.theme)

        # Virtual Root Widget.
        self.root = UIPanel(None)
        self.root.id = -99
        self.root.margin = False
        self.root.border = False

        # Get normalized size.
        normalized_size = self._calculate_normalized_size(self.font_size, self.size)

        # Set root viewport.
        size = Size(int(normalized_size.width / self.font_size.width), int(normalized_size.height / self.font_size.height))
        self.root.viewport = ViewPort(location=Location(0, 0), size=size)

        print(f"Normalized size: {normalized_size}")
        print(self.root.viewport.size)

        # Create graphic context.
        self.grp_ctx = GraphicContext(self.config)

        # Open the window.
        self.grp_ctx.open_window(title, normalized_size)

        self.running = True
        self.invalidated = True
        self.widget: Optional[UIElement] = None

        self.context: Context = Context(self.theme, self.size, self.font_size, normalized_size)

    # -----------------------
    # PUBLIC METHODS
    # -----------------------

    def run(self, startup_widget) -> None:
        """
        Starts the application with the provided startup widget.
        """
        if startup_widget is None:
            raise ValueError('startup_widget cannot be None')

        if self._initialized:
            return
        self._initialized = True

        # The widget manager.
        self.widget_manager = WidgetManager()

        if not isinstance(startup_widget, UIPanel):
            print(f"Widget Type: {type(startup_widget)}")
            self.widget = self.widget_manager.element_factory(startup_widget, self.context, self.root)
        else:
            print(f"Instance Widget Type: {type(startup_widget)}")
            self.widget = self.widget_manager.element_ingestion(startup_widget, self.context, self.root)

        # Execution cycle (Running Cycle).
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.grp_ctx.set_clock_tick(60)  # TODO: Put 60 in yaml

        # Exit
        self.grp_ctx.quit()

    # -----------------------
    # RUNNING CYCLE METHODS
    # -----------------------

    def handle_events(self):
        """
        Handles input and system events.
        """
        for event in self.grp_ctx.get_events():
            match event.type:
                case pygame.QUIT:
                    self.running = False
                case pygame.KEYDOWN | pygame.KEYUP:
                    self.widget.on_key_event(event, self.context)
                case pygame.WINDOWSIZECHANGED:
                    new_size = (event.x, event.y)
                    ApplicationResizeEventDispatcher().publish_application_viewport_resize(self, new_size)

    def update(self):
        """
        Updates application and widget state.
        """
        if self.invalidated:
            self.widget.draw(self.context)
            self.invalidated = False

        self.grp_ctx.enable_pointer(self.mouse_pointer)

    def draw(self):
        """
        Renders the application on the window.
        """
        # Draw background (currently commented out)
        # self.grp_ctx.fill()

        # Draw main widget
        self.context.paint(self.grp_ctx)

        self.context.draw_cursor(self.grp_ctx)

        # Draw mouse pointer
        self.draw_mouse_pointer()

        # Flush the graphic context.
        self.grp_ctx.flush()

    def draw_mouse_pointer(self):
        """
        Draws the mouse pointer if enabled.
        """
        if self.mouse_enable:
            # Real mouse position. E.g.: x = 24.5
            self.mouse_pos = self.grp_ctx.get_mouse_pos()
            if self.mouse_pos[0] <= 0 and self.mouse_pos[1] <= 0:
                return

            # Position in video buffer.
            buffer_pos_x = int(self.mouse_pos[0] / self.font_size.width)
            buffer_pos_y = int(self.mouse_pos[1] / self.font_size.height)

            # Normalized mouse position. E.g.: x = 25
            normalized_pos_x = max(buffer_pos_x, 0) * self.font_size.width
            normalized_pos_y = max(buffer_pos_y, 0) * self.font_size.height

            normalized_mouse_location = Location(normalized_pos_x, normalized_pos_y)
            buffer_mouse_location = Location(buffer_pos_x, buffer_pos_y)

            self.context.draw_mouse_pointer(self.grp_ctx, normalized_mouse_location, buffer_mouse_location,
                                            self.theme.pointer)



    # -----------------------
    # PRIVATE HELPER METHODS
    # -----------------------

    def _calculate_normalized_size(self, font_size: Size , size: Size) -> Size:
        """
        Calculates perfect dimensions based on font size.
        """
        width = int(size.width / font_size.width) * font_size.width
        height = int(size.height / font_size.height) * font_size.height
        return Size(width, height)

    def _set_size_values(self, default_size: tuple[int, int] = (8, 16), client_size: tuple[int, int] = None,
                         config_size: tuple[int, int] = None) -> Size:
        """
        Determines final dimensions choosing between client, configuration, or default.
        """
        if client_size is not None:
            return Size(client_size[0], client_size[1])

        if config_size is not None:
            return Size(config_size[0], config_size[1])

        return Size(default_size[0], default_size[1])

    # -----------------------
    # EVENTS DELEGATE
    # -----------------------

    def _get_theme(self, event_arg: EventArgs) -> None:
        """
        Delegate for the theme request event.
        """
        print("Get Theme Event received.")
        event_arg.payload = self.theme

    def _on_application_resize(self, event_arg: EventArgs) -> None:
        """
        Delegate for the application resize event.
        """
        new_size = Size(event_arg.payload[0], event_arg.payload[1])
        print("Application Resize Event received.")
        print(f"New size: {new_size})")
        self.size = new_size

        # Recalculate normalized size.
        normalized_size = self._calculate_normalized_size(self.font_size, self.size)
        print(f"Normalized size: {normalized_size}")

        # Only for Debug.
        text_size  = Size(int(normalized_size.width/ self.font_size.width),
                              int(normalized_size.height / self.font_size.width))


        print(text_size)

        # Recreate context
        self.context: Context = Context(self.theme, self.size, self.font_size, normalized_size)

        # Set root viewport.
        size = Size(int(normalized_size.width / self.font_size.width),
                    int(normalized_size.height / self.font_size.height))

        self.root.viewport = ViewPort(location=Location(0, 0), size=size)
        self.widget.on_set_layout(self.context)
        self.invalidated = True
