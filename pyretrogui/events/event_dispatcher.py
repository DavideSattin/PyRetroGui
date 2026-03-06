# ==========================================
# Project: PyRetroGui
# File: event_dispatcher
# Author: Davide Sattin
# Created: 02/03/2026 10:16
# Description:
# ==========================================
from typing import List, Callable
from enum import Enum
from abc import ABC

from pyretrogui.events.event_args import EventArgs
from pyretrogui.events.subscriber_data import SubscriberData


class EventDispatcher(ABC):
    """
       Central event dispatcher.

       Responsibilities:
       - Manage subscriptions
       - Dispatch events to subscribers
       - Keep publisher and subscribers decoupled
       """
    def __init__(self):
        self.subscribers_data : List[SubscriberData] = []

    def _match_subscriber(self, subscriber_data:SubscriberData, subscriber, kind: Enum = None)-> bool:
        if subscriber_data.subscriber is not subscriber:
            return False

        if subscriber_data.kind is None:
            return True

        if subscriber_data.kind is not None and kind is not None:
            return subscriber_data.kind == kind

        return True



    def subscribe(self, subscriber,handler: Callable, kind: Enum=None):

        the_subscriber_data = SubscriberData(subscriber=subscriber, kind=kind, event_function=handler)
        self.subscribers_data.append(the_subscriber_data)

    def unsubscribe(self, subscriber):
        if subscriber is None:
            raise ValueError("Subscriber cannot be None")

        self.subscribers_data = [current_subscriber for current_subscriber in self.subscribers_data if not(current_subscriber.subscriber == subscriber)]

    def unsubscribe_kind(self, subscriber, kind: Enum=None):
        if subscriber is None:
            raise ValueError("Subscriber cannot be None")

        self.subscribers_data = [current_subscriber for current_subscriber in self.subscribers_data if
                                 not self._match_subscriber(current_subscriber, subscriber,kind)]


    # def publish_event(self, sender, kind:Enum=None, payload=None):
    #     notify_subscribers = [current_subscriber for current_subscriber in self.subscribers_data if current_subscriber.kind == kind]
    #     for notify_subscriber in notify_subscribers:
    #         args = EventArgs(sender=sender, kind=kind, payload=payload)
    #         notify_subscriber.event_function(args)        # event_param = KeyEvent(param)
    #         payload = args.payload

    def publish_event(self, sender, kind: Enum = None, payload=None):

        args = EventArgs(sender=sender, kind=kind, payload=payload)

        notify_subscribers = [
            s for s in self.subscribers_data
            if s.kind is None or s.kind == kind
        ]

        for subscriber in notify_subscribers:
            subscriber.event_function(args)

            if args.handled:
                break

        return args.payload

    def unsubscribe_all(self):
        self.subscribers_data.clear()
