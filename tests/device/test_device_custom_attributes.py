
import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.device.device_custom_attributes import get_custom_attributes
from soti_mobicontrol_python.endpoints.device.device_custom_attributes import set_custom_attributes

# Test get_custom_attributes
@pytest.mark.asyncio
async def test_get_custom_attributes():
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
    # Get the custom attributes for the device
    custom_attributes = await get_custom_attributes(client, device_id)

    # Close the client
    await client.close()

    # Assert
    # Assert that the custom attributes ha at least 3 keys
    assert len(custom_attributes) >= 3


# Test set_custom_attributes
@pytest.mark.asyncio
async def test_set_custom_attributes():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config - note that this expects the SOTI custom attrbute have been created
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']
    custom_attributes = {
        "Pin": "1234"
    }

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Set the custom attributes for the device
    response = await set_custom_attributes(client, device_id, custom_attributes)

    # Get the custom attributes for the device
    custom_attributes = await get_custom_attributes(client, device_id)

    # Close the client
    await client.close()

    # Assert
    

    # Assert that the response is successful
    assert response.is_success is True
    # Assert that the custom attribute Pin has the value 1234
   # assert custom_attributes['Pin'] == '1234'