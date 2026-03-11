# ==========================================
# Project: PyRetroGui
# File: ThemeEventsDispatcher
# Author: Davide Sattin
# Created: 06/03/2026 09:55
# Description: Dispatcher for theme-related events, specifically for retrieving the current theme.
# ==========================================
from typing import Callable

from pyretrogui.appearance.theme import Theme
from pyretrogui.events.event_dispatcher import EventDispatcher
from pyretrogui.singleton_meta.singleton_meta_abc import SingletonMetaAbc


class ThemeEventsDispatcher(EventDispatcher, metaclass=SingletonMetaAbc):
    """
    Dispatcher specialized in handling theme-related events.
    Implemented as a singleton to provide a global access point for theme requests.
    """

    def subscribe_event_get_theme(self, subscriber, handler: Callable):
        """
        Subscribes a handler to the theme retrieval event.

        :param subscriber: The object subscribing to the event.
        :param handler: The callback function to be executed when the event is published.
        """
        super().subscribe(subscriber, handler)

    def publish_event_get_theme(self, sender) -> Theme:
        """
        Publishes an event to request the current theme.

        :param sender: The object publishing the event.
        :return: The Theme object returned by the event handlers.
        """
        return super().publish_event(sender=sender, kind=None, payload=None)
