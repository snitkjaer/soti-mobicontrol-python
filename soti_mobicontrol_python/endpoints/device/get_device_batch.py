import urllib.parse

from ...soti_api_client import soti_api_client

async def get_device_batch(client:soti_api_client, device_group_path:str, filter, include_subgroups:bool, verify_and_sync:bool, skip:int, take:int):
    endpoint = "/devices/search"
    groupPath = device_group_path.lstrip('/')
    groupPath = "//" + groupPath
    groupPath = urllib.parse.quote(groupPath)

    # Set the query parameters
    params = {
        "groupPath": groupPath,
        "includeSubgroups": str(include_subgroups),
        "verifyAndSync": str(verify_and_sync),
        "skip": skip,
        "take": take
    
    }

    # TODO add filter to params

    # Get the data from the endpoint using the client
    return await client.get_data(endpoint, params=params)


