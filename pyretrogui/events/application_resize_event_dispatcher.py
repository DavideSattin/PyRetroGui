# ==========================================
# Project: PyRetroGUI
# File: application_resize_event_dispatcher
# Author: Davide Sattin 
# Created: 11/03/2026 11:37
# Description:
# ==========================================
from typing import Callable
from pyretrogui.events.event_dispatcher import EventDispatcher
from pyretrogui.primitives.size import Size
from pyretrogui.singleton_meta.singleton_meta_abc import SingletonMetaAbc

class ApplicationResizeEventDispatcher(EventDispatcher, metaclass=SingletonMetaAbc):

    def subscribe_event_viewport_resize(self, subscriber, handler: Callable):
        """
        Subscribes a handler to the theme retrieval event.

        :param subscriber: The object subscribing to the event.
        :param handler: The callback function to be executed when the event is published.
        """
        super().subscribe(subscriber, handler)

    def publish_application_viewport_resize(self, sender, payload:tuple[int,int] = None) :
        super().publish_event(sender=sender, kind=None, payload=payload)