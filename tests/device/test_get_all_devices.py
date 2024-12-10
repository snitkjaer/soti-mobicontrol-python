# test_devices.py

import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.soti_api_client import soti_api_client
from soti_mobicontrol_python.endpoints.device.get_all_devices import get_all_devices

# Test the get_all_devices function
@pytest.mark.asyncio
async def test_get_all_devices():
    #
    #### Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    groups = test_parameters['deviceGroupPaths']
    device_filter = test_parameters['deviceFilter']

    # Create the SOTI API client (httpx.AsyncClient)
    client = soti_api_client(soti_server_config)
    # Device counter
    total_devices = 0



    #
    #### Act
    # Get all devices from SOTI for each device group path in groupPaths
    for group in groups:
        async for device in get_all_devices(client, group, device_filter, True, False):
            print(device.get('DeviceName'))
            total_devices += 1
    
    # Close the client
    await client.close()

    #
    #### Assert
    # Assert that the total devices is greater than 0
    assert total_devices > 0