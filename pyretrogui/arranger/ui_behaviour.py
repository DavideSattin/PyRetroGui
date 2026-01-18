# ==========================================
# Project: PyRetroGUI
# File: ui_behaviour
# Author: Davide Sattin 
# Created: 18/01/2026 11:39
# Description:Class for panel Behaviour
# ==========================================
from pyretrogui.arranger.window_position import WindowPosition
from pyretrogui.arranger.window_size import WindowSize


class UIBehaviour:
      def __init(self):
          self.panel_position = WindowPosition.FREE
          self.panel_size = WindowSize.DOCK