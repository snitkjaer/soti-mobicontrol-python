import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.servers.health import get_service_health

# Test the get_service_health function
@pytest.mark.asyncio
async def test_get_service_health():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Search for the users
    health = await get_service_health(client)

    # Close the client
    await client.close()

    # Assert
    # Assert that the users list is not empty
    assert health["responding"] == True
