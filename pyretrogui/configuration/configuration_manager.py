# ==========================================
# Project: PyRetroGUI
# File: configuration_manager
# Author: Davide Sattin 
# Created: 19/01/2026 21:25
# Description: Save and Load the configuration
# ==========================================
from ruamel.yaml import YAML

class Configuration:
      def __init__(self):
          self.data = None

      def get_data(self, *keys, default=None):
              data = self.data
              for key in keys:
                  if not isinstance(data, dict) or key not in data:
                      return default
                  data =  data[key]
              return data

      def load(self):
          yaml = YAML()
          with open("../assets/configuration.yaml") as f:
              self.data = yaml.load(f)

      def save(self):
          yaml = YAML()
          with open("config.yaml", "w") as f:
              yaml.dump(self.data, f)