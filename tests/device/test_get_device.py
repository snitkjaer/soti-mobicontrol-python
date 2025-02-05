import pytest

from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.device.get_device import get_device

# Test the get_device function
@pytest.mark.asyncio
async def test_get_device():
    #
    #### Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    #
    #### Act
    # Get the device from SOTI
    device = await get_device(client, device_id)
    print(device.get('DeviceName'))

    # Close the client
    await client.close()

    #
    #### Assert
    # Assert that the device is not None
    assert device is not None