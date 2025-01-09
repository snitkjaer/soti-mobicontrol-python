import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.security.users import search_for_user

# Test the search_for_user function
@pytest.mark.asyncio
async def test_search_for_user():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    search_string = test_parameters['mcUserSearchString']
    include_hidden_users = True
    kind = "MobiControlUser"

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Search for the users
    users = await search_for_user(client, search_string, include_hidden_users, kind)

    # Close the client
    await client.close()

    # Assert
    # Assert that the users list is not empty
    assert len(users) > 0
