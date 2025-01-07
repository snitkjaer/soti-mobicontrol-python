import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.device.device_user import set_user_on_device, get_user_info

# Test the set_user function
@pytest.mark.asyncio
async def test_set_user():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_id = test_parameters['deviceId']
    connection_name = test_parameters['connectionName']
    connection_type = test_parameters['connectionType']
    user_search_string = test_parameters['userSearchString']

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Get the usner info
    user_info_dict = await get_user_info(client,connection_name,user_search_string,"User")

    # Check if we got more than one user
    if len(user_info_dict) > 0:
        user_info = user_info_dict[0]
    else:
        user_info = None

    # Set the user for the device
    response = await set_user_on_device(client, device_id, connection_name, connection_type, user_info)

    # Close the client
    await client.close()

    # Assert
    # Assert that the response is successful
    assert response.is_success is True