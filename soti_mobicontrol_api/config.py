import json
import os
import logging

# Config class that contains the configuration parameters
class Config:
    # Constructor that takes the config.json file as input
    def __init__(self):
        # Get the path of this file
        path = os.path.dirname(os.path.abspath(__file__))
        # Import parameters from config.json
        json_file = open(path + '/config.json')
        self.config = json.load(json_file)
        self.soti_config = self.config['SotiMobiControlServer']
        self.logging_config = self.config['Logging']

    def get_soti_config(self):
        return self.soti_config

    def get_logging_config(self):
        return self.logging_config

    def get_config(self):
        return self.config

