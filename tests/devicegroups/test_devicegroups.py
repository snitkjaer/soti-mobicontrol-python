import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.devicegroups.get_devicegroups import get_all_devicegroups

# Test get_all_devicegroups
@pytest.mark.asyncio
async def test_get_all_devicegroups():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Get all device groups
    device_groups = await get_all_devicegroups(client)

    # Close the client
    await client.close()

    # Assert
    # Assert that the device groups ha at least 1 key
    assert len(device_groups) >= 1