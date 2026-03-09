# ==========================================
# Project: PyRetroGui
# File: singleton_layout_manager
# Author: Davide Sattin
# Created: 09/03/2026 12:06
# Description:
# ==========================================
import threading
from abc import ABCMeta

class SingletonLayoutManager(ABCMeta):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]