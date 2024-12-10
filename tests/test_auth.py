# test_auth.py
import pytest

from tests.helper.config import Test_Config
from soti_mobicontrol_python.auth import Auth

# Integration test using the live API
# This test will fail if the SOTI MobiControl server is not running and the credentials are incorrect

# Test the get_access_token function
@pytest.mark.vcr()
def test_get_access_token():
    # Get the config for the config.json file
    config = Test_Config()
    soti_config = config.get_soti_server_config()
    # Create the auth
    auth = Auth(soti_config)
    # Get the access token
    access_token = auth.get_access_token_dict().get("access_token")
    # Check if the access token is not None
    assert access_token is not None

# Test the create_soti_headers function
@pytest.mark.vcr()
def test_create_soti_headers():
    # Get the config for the config.json file
    config = Test_Config()
    soti_config = config.get_soti_server_config()
    # Create the auth
    auth = Auth(soti_config)
    # Create the SOTI headers
    headers = auth.get_soti_headers()
    # Check if the headers are not None
    assert headers is not None