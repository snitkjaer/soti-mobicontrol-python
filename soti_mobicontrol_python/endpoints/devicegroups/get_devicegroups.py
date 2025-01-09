import urllib.parse
from ...SotiApiClient import SotiApiClient
from ...helper.path import clean_path

# Get all device groups
async def get_all_devicegroups(client:SotiApiClient):
    endpoint = "/devicegroups"
    return await client.get_data(endpoint)


# Get specific device groups with parent path
async def get_devicegroup_with_parrent(client:SotiApiClient, parrent_path:str):
    # Get all the device groups and look up the reference nuber for the given path
    device_groups = await get_all_devicegroups(client)
    # Clean the path by removing any leading or trailing slashes
    path_cleaned = clean_path(parrent_path)

    # Search for the device group with the given path
    device_groups_with_parrent = []

    for device_group in device_groups:
        # Get the path of the device group and clean it 
        ### by removing leading or trailing backslashes
        ### replace backslashes with forward slashes
        device_group_path = clean_path(device_group['Path'])
        ## Check if the path starts with the parent path
        if device_group_path.startswith(path_cleaned):
            device_groups_with_parrent.append(device_group)
        
    return device_groups_with_parrent


# Get referenceId of a device group with a given path
async def get_devicegroup_reference_id(client:SotiApiClient, path:str):
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

    # Make sure the path was found else raise an exception
    if reference_id == None:
        raise Exception(f"Device group with path {path} not found")
    
    return reference_id