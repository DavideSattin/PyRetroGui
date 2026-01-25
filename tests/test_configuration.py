# ==========================================
# Project: PyRetroGUI
# File: test_configuration
# Author: Davide Sattin 
# Created: 25/01/2026 18:11
# Description:Unit test for yaml reading and configuration managements.
# ==========================================
import unittest
from pyretrogui.configuration.yaml_manager import YamlManager


class test_configuration(unittest.TestCase):

    def test_yaml_reading(self):
        error = False
        try:
            cfg= YamlManager()
            cfg.load()
        except Exception as e:
            error = True

        self.assertEqual(error, False)

if __name__ == '__main__':
    unittest.main()
