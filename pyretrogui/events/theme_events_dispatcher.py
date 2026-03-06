# ==========================================
# Project: PyRetroGui
# File: ThemeEventsDispatcher
# Author: Davide Sattin
# Created: 06/03/2026 09:55
# Description:
# ==========================================
from typing import Callable

from pyretrogui.apparence.theme import Theme
from pyretrogui.events.event_dispatcher import EventDispatcher
from pyretrogui.singleton_meta.singleton_meta_abc import SingletonMetaAbc


class ThemeEventsDispatcher(EventDispatcher,metaclass=SingletonMetaAbc):

       def subscribe_event_get_theme(self, subscriber, handler:Callable):
           super().subscribe(subscriber, handler)


       def  publish_event_get_theme(self, sender) -> Theme:
           return super().publish_event(sender=sender, kind=None, payload=None)
