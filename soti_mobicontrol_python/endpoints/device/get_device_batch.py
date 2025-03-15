# Description: This file contains the code to get a batch of devices from the SOTI API
# The code uses the SotiApiClient to make the request to the SOTI API
# The code also uses the get_devicegroup_reference_id function to get the reference id of the device group
import logging

from ...SotiApiClient import SotiApiClient
from ..devicegroups.get_devicegroups import get_devicegroup_reference_id

# Get a batch of devices from the SOTI API
async def get_device_batch(client:SotiApiClient, device_group_path:str, filter, include_subgroups:bool, verify_and_sync:bool, skip:int, take:int):
    endpoint = "/devices/search"

    logging.debug(f"Getting devices from group {device_group_path}")

    # The reference id work for all groups except the root group
    # As root group we accept /, // \, \\, and empty string or none
    if device_group_path is None or device_group_path in ["", "/", "\\", "//", "\\\\" ]:
        # This is the root group
        # Set the query parameters
        params = {
            "includeSubgroups": str(include_subgroups),
            "verifyAndSync": str(verify_and_sync),
            "skip": skip,
            "take": take
        
    }
    else:
        # Get the group path reference id
        reference_id = await get_devicegroup_reference_id(client, device_group_path)
        group_path = f"referenceId:{reference_id}"
        # Set the query parameters
        params = {
            "groupPath": group_path,
            "includeSubgroups": str(include_subgroups),
            "verifyAndSync": str(verify_and_sync),
            "skip": skip,
            "take": take
        
        }



    # TODO add filter to params

    # Get the data from the endpoint using the client
    return await client.get_data(endpoint, params=params)


