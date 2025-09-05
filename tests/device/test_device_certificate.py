import pytest

from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.device.device_certificate import get_certificates

# Test the get_certificates function
@pytest.mark.asyncio
async def test_get_certificates():
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
    # Get the certificates from SOTI
    certificates = await get_certificates(client, device_id)
    print(f"Retrieved {len(certificates) if certificates else 0} certificates")

    # Close the client
    await client.close()

    #
    #### Assert
    # Assert that the certificates response is not None
    assert certificates is not None
    # Assert that we got a list (even if empty)
    assert isinstance(certificates, list)