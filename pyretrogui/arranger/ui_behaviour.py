# ==========================================
# Project: PyRetroGUI
# File: ui_behaviour
# Author: Davide Sattin 
# Created: 18/01/2026 11:39
# Description:Class for panel Behaviour
# ==========================================
from pyretrogui.arranger.position_behaviour import PositionBehaviour
from pyretrogui.arranger.resize_behaviour import ResizeBehaviour


class UIBehaviour:
      def __init__(self):
          self.position_behaviour = PositionBehaviour.DOCKED
          self.size_behaviour = ResizeBehaviour.BUBBLE

      # def set_dockable_width(self):
      #     self.position_behaviour = PositionBehaviour.DOCKED
      #     self.size_behaviour = WindowSize.DOCk_WIDTH
