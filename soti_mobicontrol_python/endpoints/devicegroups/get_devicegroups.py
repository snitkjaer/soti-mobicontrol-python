from ...SotiApiClient import SotiApiClient

# Get all device groups
async def get_all_devicegroups(client:SotiApiClient):
    endpoint = "/devicegroups"
    return await client.get_data(endpoint)


# Get specific device group
async def get_devicegroup(client:SotiApiClient, device_group_peth:str):
    endpoint = f"/devicegroups/{device_group_peth}"
    return await client.get_data(endpoint)


# Get members of a specific device group