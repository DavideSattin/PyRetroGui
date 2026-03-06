# ==========================================
# Project: PyRetroGui
# File: event_args
# Author: Davide Sattin
# Created: 04/03/2026 17:03
# Description:
# ==========================================
from typing import TypeVar, Generic
from enum import Enum

T = TypeVar('T')
P = TypeVar('P')

class KeyEventType(Enum):
    NONE = 0
    KEY_UP = 1
    KEY_DOWN = 2


class EventArgs(Generic[T,P]):
    def __init__(self, sender, kind: T, payload: P):
        self.handled: bool = False
        self.sender = sender
        self.kind : T = kind
        self.payload : P = payload