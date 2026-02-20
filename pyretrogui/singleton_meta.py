# ==========================================
# Project: PyRetroGui
# File: singleton_meta
# Author: Davide Sattin
# Created: 30/01/2026 15:46
# Description:Class for singleton metaclass.
# ==========================================
import threading

class SingletonMeta(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


