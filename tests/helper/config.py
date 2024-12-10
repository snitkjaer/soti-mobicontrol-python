import json
import os
from soti_mobicontrol_python.soti_mobicontrol_config import SotiMobiControlServerConfig, load_config_from_json

# Config class that contains the configuration parameters
class Test_Config:
    # Constructor that takes the config.json file as input
    def __init__(self):
        # Get the path of this file
        path = os.path.dirname(os.path.abspath(__file__))
        # Import the config.json to a dictionary
        json_file = open(path + '/config.json')
        self.config = json.load(json_file)
        # Get the SOTI MobiControl server configuration
        jsonSotiConfig = self.config['SotiMobiControlServer']
        self.soti_server_config = load_config_from_json(jsonSotiConfig)
        # Get the test parameters
        self.test_parameters = self.config['TestParameters']
        # Get the logging configuration
        self.logging_config = self.config['Logging']

    def get_soti_server_config(self):
        return self.soti_server_config

    def get_test_parameters(self):
        return self.test_parameters

    def get_logging_config(self):
        return self.logging_config



