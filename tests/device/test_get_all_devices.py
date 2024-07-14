# test_devices.py

import pytest
from soti_mobicontrol_api.config import Config
from soti_mobicontrol_api.soti_api_client import soti_api_client
from soti_mobicontrol_api.endpoints.device.get_all_devices import get_all_devices


@pytest.mark.asyncio
async def test_get_all_devices():
    #
    #### Arrange
    # Get the config for the config.json file
    config = Config()
    soti_config = config.get_soti_config()
    # Create the SOTI API client (httpx.AsyncClient)
    client = soti_api_client(soti_config)
    # Device counter
    total_devices = 0

    groups = soti_config['deviceGroupPaths']

    #
    #### Act
    # Get all devices from SOTI for each device group path in groupPaths
    for group in groups:
        async for device in get_all_devices(client, group, soti_config['deviceFilter'], True, False):
            print(device.get('DeviceName'))
            total_devices += 1
    
    # Close the client
    await client.close()

    #
    #### Assert
    # Assert that the total devices is greater than 0
    assert total_devices > 0