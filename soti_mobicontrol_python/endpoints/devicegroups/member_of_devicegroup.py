import logging
from ...SotiApiClient import SotiApiClient
from ...helper.path import clean_path
from .get_devicegroups import get_all_devicegroups

# Moves one or more devices identified by their device IDs to a device group identified by its reference ID.
# In the case the destination is a virtual group, devices will be added to the group rather than moved. 
# Any advanced settings configured for the devices specifically can either be maintained or inherited from the new device group (cleared). 
# Requires the caller be granted the "View Groups" and "Manage Devices" permission for both the source and destination device groups.

async def move_devices_to_devicegroup(client:SotiApiClient, path:str, device_ids:list, clear_configurations: bool = False):
    logging.debug(f"Moving device ids {device_ids} to device group with path {path}")
    # Get all the device groups and look up the reference nuber for the given path
    device_groups = await get_all_devicegroups(client)
    # Clean the path by removing any leading or trailing slashes
    path_cleaned = clean_path(path)

    # Search for the device group with the given path
    for device_group in device_groups:
        # Get the path of the device group and clean it 
        ### by removing leading or trailing backslashes
        ### replace backslashes with forward slashes
        device_group_path = clean_path(device_group['Path'])
        if device_group_path == path_cleaned:
            reference_id = device_group['ReferenceId']
            break
        else:
            reference_id = None

    # Male sure the path was found elese raise an exception
    if reference_id is None:
        raise Exception(f"Device group with path {path} not found")
    
    # /devicegroups/{path}/members
    endpoint = f"/devicegroups/referenceId:{reference_id}/members"

    # Set the query parameters
    params = {
        "clearConfigurations": str(clear_configurations).lower()
    }


    # body: deviceIds 
    # [
    #   "id1",
    #   "id2"
    # ]
    # Create the body by iterating over the device_ids and creating a list of dictionaries
    # body = []
    # for device_id in device_ids:
    #     body.append({device_id})


    # Post the data to the endpoint
    return await client.post_data(endpoint, body=device_ids, params=params)

