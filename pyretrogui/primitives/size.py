# ==========================================
# Project: PyRetroGUI
# File: absolute_location
# Author: Davide Sattin
# Created: 09/01/2026 17:01
# Description:This class manage Size
# ==========================================
class Size:
      def __init__(self, width:int, height:int):
          self.width:int = width
          self.height:int = height

      def __str__(self):
          return f"Size(width={self.width}, height={self.height})"