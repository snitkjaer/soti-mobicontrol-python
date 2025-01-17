import pytest
from tests.helper.config import Test_Config
from soti_mobicontrol_python.SotiApiClient import SotiApiClient
from soti_mobicontrol_python.endpoints.devicegroups.get_devicegroups import get_devicegroup_with_parrent, get_all_devicegroups, get_devicegroup_reference_id

# Test get_all_devicegroups
@pytest.mark.asyncio
async def test_get_all_devicegroups():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()

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

# Get one device group on path
@pytest.mark.asyncio
async def test_get_device_group_with_parrent():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_group_path = test_parameters['deviceGroupPaths'][2]

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Get the device groups with the parent path
    device_groups = await get_devicegroup_with_parrent(client, device_group_path)

    # Close the client
    await client.close()

    # Assert
    # Assert that the device groups ha at least 1 key
    assert len(device_groups) >= 1

# Get referenceId of a device group with a given path
@pytest.mark.asyncio
async def test_get_devicegroup_reference_id():
    # Arrange
    # Get the config for the config.json file
    config = Test_Config()
    soti_server_config = config.get_soti_server_config()
    # Get the test parameters from the config
    test_parameters = config.get_test_parameters()
    device_group_path = test_parameters['deviceGroupPaths'][2]

    # Create the SOTI API client (httpx.AsyncClient)
    client = SotiApiClient(soti_server_config)

    # Act
    # Get the referenceId of the device group with the given path
    reference_id = await get_devicegroup_reference_id(client, device_group_path)

    # Close the client
    await client.close()

    # Assert
    # Assert that the referenceId is not None
    assert reference_id is not None