# ==========================================
# Project: PyRetroGUI
# File: MouseEventDispatcher
# Author: Davide Sattin 
# Created: 11/03/2026 17:01
# Description:
# ==========================================
from dataclasses import dataclass
from enum import Enum
from typing import Callable

from pyretrogui.events.event_dispatcher import EventDispatcher
from pyretrogui.singleton_meta.singleton_meta_abc import SingletonMetaAbc

@dataclass(frozen=True)
class MousePosition:
     x: int
     y: int

class MouseEventType(Enum):
    NONE = 0
    MOUSE_UP = 1
    MOUSE_DOWN = 2

class MouseButtonType(Enum):
    NONE = 0
    BUTTON_LEFT = 1
    BUTTON_MIDDLE = 2
    BUTTON_RIGHT = 3
    BUTTON_WHEELDOWN = 5
    BUTTON_WHEELUP = 4

class MousePayload:
    def __init__(self, mouse_button: MouseButtonType, position: tuple[int,int]):
        self.button  : MouseButtonType = mouse_button
        self.position: MousePosition = MousePosition(x=position[0], y=position[1])

class MouseEventDispatcher(EventDispatcher, metaclass=SingletonMetaAbc):

    def subscribe_event_mouse_down(self, subscriber, handler: Callable):
        """
        Subscribes a handler to the theme retrieval event.

        :param subscriber: The object subscribing to the event.
        :param handler: The callback function to be executed when the event is published.
        """
        super().subscribe(subscriber, handler, MouseEventType.MOUSE_DOWN)

    def publish_mouse_down_event(self,sender, payload: MousePayload):

        super().publish_event(sender=sender, kind=MouseEventType.MOUSE_DOWN, payload=payload)