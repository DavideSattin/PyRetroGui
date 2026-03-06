# ==========================================
# Project: PyRetroGui
# File: subscriber_data
# Author: Davide Sattin
# Created: 04/03/2026 17:03
# Description:
# ==========================================
from typing import Callable
from enum import Enum
class SubscriberData:
    def __init__(self, subscriber, event_function: Callable, kind: Enum = None):
        self.subscriber = subscriber
        self.event_function: Callable = event_function
        self.kind: Enum = kind