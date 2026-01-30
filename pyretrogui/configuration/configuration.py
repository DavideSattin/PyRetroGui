# ==========================================
# Project: PyRetroGUI
# File: configuration
# Author: Davide Sattin 
# Created: 25/01/2026 18:29
# Description:
# ==========================================
from pyretrogui.configuration.dto.application_config import ApplicationConfig
from pyretrogui.configuration.dto.font_config import FontConfig
from pyretrogui.configuration.dto.mouse_config import MouseConfig
from pyretrogui.configuration.yaml_manager import YamlManager
from pyretrogui.singleton_meta import SingletonMeta


class Configuration(metaclass=SingletonMeta):
      def __int__(self):
           pass

      def load (self) -> ApplicationConfig:
          yaml_manager = YamlManager()
          yaml_manager.load()

          # Root configuration.
          configuration_data = ApplicationConfig
          configuration_data.title = yaml_manager.get_data("application", "title", default="")
          configuration_data.size = yaml_manager.get_data("application", "size", default=(0,0))

          # Read the font configuration.
          font_size = yaml_manager.get_data("application", "font", "font_size", default=(8,16))
          font_path = yaml_manager.get_data("application", "font", "font_path", default="")
          configuration_data.font = FontConfig(font_size, font_path)

          # Read the mouse configuration.
          enabled = yaml_manager.get_data("application", "mouse","enabled", True)
          pointer= yaml_manager.get_data("application", "mouse", "pointer", True)
          configuration_data.mouse = MouseConfig(enabled, pointer)

          # Read the theme configuration.
          configuration_data.theme = yaml_manager.get_data("application", "theme", default="")

           # configuration_data.font_size = yaml_data.get_data("application", "font", "font_size", default="")


          return configuration_data