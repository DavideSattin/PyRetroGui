# ==========================================
# Project: PyRetroGui
# File: keyboard_event_dispatcher
# Author: Davide Sattin
# Created: 04/03/2026 17:06
# Description:
# ==========================================
from enum import Enum
from typing import Callable
from pyretrogui.events.event_dispatcher import EventDispatcher
from pyretrogui.singleton_meta.singleton_meta_abc import SingletonMetaAbc

# @dataclass
# class KeyEvent:
#     key: str

class KeyEventType(Enum):
    NONE = 0
    KEY_UP = 1
    KEY_DOWN = 2


class KeyboardEventDispatcher(EventDispatcher, metaclass=SingletonMetaAbc):

    def subscribe_on_key_down(self, subscriber, handler: Callable):
        super().subscribe(subscriber, handler, KeyEventType.KEY_DOWN)


    def subscribe_on_key_up(self, subscriber,  handler: Callable):
        super().subscribe(subscriber, handler, KeyEventType.KEY_UP)

    def unsubscribe_on_key_down(self, subscriber):
        super().unsubscribe_kind(subscriber, KeyEventType.KEY_DOWN)


    def unsubscribe_on_key_up(self, subscriber):
        super().unsubscribe_kind(subscriber, KeyEventType.KEY_UP)


    def publish_key_down_event(self,sender, payload):
        super().publish_event(sender=sender, kind=KeyEventType.KEY_DOWN, payload=payload)

    def publish_key_up_event(self,sender, payload):
        super().publish_event(sender=sender, kind=KeyEventType.KEY_UP, payload=payload)
