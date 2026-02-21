# ==========================================
# Project: PyRetroGUI
# File: singleton_widget_manager
# Author: Davide Sattin 
# Created: 21/02/2026 10:21
# Description:Metaclass for widget manager singleton
# ==========================================
import threading

class SingletonMetaWidgetManager(type):
    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]



