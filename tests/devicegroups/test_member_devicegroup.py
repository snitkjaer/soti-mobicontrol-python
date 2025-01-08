import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.devicegroups.member_of_devicegroup import move_devices_to_devicegroup

# Test move_devices_to_devicegroup
@pytest.mark.asyncio
async def test_move_devices_to_devicegroup():
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
    # Move device to device group
    response = await move_devices_to_devicegroup(client, test_parameters['deviceGroupPaths'][1], [device_id])


    # Close the client
    await client.close()

    # Assert
    # Assert that the response is not None
    assert response is not None
