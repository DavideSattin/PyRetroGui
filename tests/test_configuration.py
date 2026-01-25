# ==========================================
# Project: PyRetroGUI
# File: test_configuration
# Author: Davide Sattin 
# Created: 25/01/2026 18:11
# Description:
# ==========================================

import unittest
from pyretrogui.configuration.configuration_manager import Configuration


class test_configuration(unittest.TestCase):

    def test_something(self):
        error = False
        try:
            cfg= Configuration()
            cfg.load()
        except Exception as e:
            error = True

        self.assertEqual(error, False)

if __name__ == '__main__':
    unittest.main()
