import json
from dataclasses import dataclass
from typing import List, Optional
import logging

@dataclass
class SotiMobiControlServerConfig:
    FQDN: str
    clientId: str
    clientSecret: str
    username: str
    password: str

# Load the SOTI MobiControl server configuration from a JSON dictionary to SotiMobiControlServerConfig dataclass
def load_config_from_json(config_dict: dict) -> SotiMobiControlServerConfig:
    try:
        # Map the dictionary to the dataclass
        return SotiMobiControlServerConfig(**config_dict)
    except Exception as e:
        logging.error(f"Error loading config from JSON: {e}")
        raise Exception(f"Error loading config from JSON: {e}")