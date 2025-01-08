import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.device.device_action import send_action

# Test send_action_checkin
@pytest.mark.asyncio
async def test_send_action_checkin():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']
    action_name = "CheckIn"

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Send action to device
    response = await send_action(client, device_id, action_name)

    # Close the client
    await client.close()

    # Assert
    # Assert that the response is not None
    assert response is not None

# Test send_action_script
@pytest.mark.asyncio
async def test_send_action_script():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']
    action_name = "SendScript"

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Send action to device
    response = await send_action(client, device_id, action_name, message="log -i \"HALLO API test\"")

    # Close the client
    await client.close()

    # Assert
    # Assert that the response is not None
    assert response is not None