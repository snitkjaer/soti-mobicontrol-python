import urllib.parse

from ...SotiApiClient import SotiApiClient
from ..devicegroups.get_devicegroups import get_devicegroup_reference_id

# Get a batch of devices from the SOTI API
async def get_device_batch(client:SotiApiClient, device_group_path:str, filter, include_subgroups:bool, verify_and_sync:bool, skip:int, take:int):
    endpoint = "/devices/search"

    # Get the group path reference id
    reference_id = await get_devicegroup_reference_id(client, device_group_path)

    # Set the query parameters
    params = {
        "groupPath": f"referenceId:{reference_id}",
        "includeSubgroups": str(include_subgroups),
        "verifyAndSync": str(verify_and_sync),
        "skip": skip,
        "take": take
    
    }

    # TODO add filter to params

    # Get the data from the endpoint using the client
    return await client.get_data(endpoint, params=params)


