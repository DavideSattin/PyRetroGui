# ==========================================
# Project: PyRetroGUI
# File: test_configuration
# Author: Davide Sattin
# Created: 25/01/2026 18:11
# Description:Unit test for yaml reading and configuration managements.
# ==========================================
import unittest

from pyretrogui.configuration.configuration import Configuration
from pyretrogui.configuration.yaml_manager import YamlManager


class TestConfiguration(unittest.TestCase):

    def test_yaml_reading(self):
        error = False
        try:
            cfg= YamlManager()
            cfg.load()
        except Exception as e:
            print("Error reading yaml file: ",e)
            error = True

        self.assertEqual(error, False)

    def test_yaml_get_data(self):
        error = False
        try:
            cfg= YamlManager()
            cfg.load()
            mouse_enabled =  cfg.get_data("application", "mouse","enabled", default=False)
            print (f"Mouse Enabled: {mouse_enabled}")
            self.assertEqual(mouse_enabled, True)
        except Exception as e:
            print("Error reading yaml file: ",e)
            error = True

        self.assertEqual(error, False)


    def test_read_configuration(self):
        error = False
        try:
            cfg_manager = Configuration()
            cfg = cfg_manager.load()
            print("Configuration loaded")
            print(cfg.title)
            print(cfg.theme)
            print(cfg.mouse.enabled)
            print(cfg.mouse.pointer)
            self.assertEqual(cfg.mouse.enabled, True)
            self.assertEqual(cfg.mouse.pointer, False)
        except Exception as e:
            print("Error reading configuration: ", e)
            error = True

        self.assertEqual(error, False)

if __name__ == '__main__':
    unittest.main()
