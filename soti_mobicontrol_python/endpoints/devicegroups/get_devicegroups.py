import urllib.parse
from ...SotiApiClient import SotiApiClient

# Get all device groups
async def get_all_devicegroups(client:SotiApiClient):
    endpoint = "/devicegroups"
    return await client.get_data(endpoint)


# Get specific device group
async def get_devicegroup_with_parrent(client:SotiApiClient, parrent_path:str):
    endpoint = "/devicegroups"

    parentPath = parrent_path.lstrip('/')
    parentPath = "//" + parentPath
    parentPath = urllib.parse.quote(parentPath)

    # Set the query parameters
    params = {
        "parentPath": parentPath
    }


    # Get the data from the endpoint using the client
    return await client.get_data(endpoint, params=params)



# Get members of a specific device group