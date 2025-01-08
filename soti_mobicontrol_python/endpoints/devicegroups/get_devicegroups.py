import urllib.parse
from ...SotiApiClient import SotiApiClient
from ...quote_path import quote_path

# Get all device groups
async def get_all_devicegroups(client:SotiApiClient):
    endpoint = "/devicegroups"
    return await client.get_data(endpoint)


# Get specific device group
async def get_devicegroup_with_parrent(client:SotiApiClient, parrent_path:str):
    endpoint = "/devicegroups"

    # Set the query parameters
    params = {
        "parentPath": quote_path(parrent_path)
    }


    # Get the data from the endpoint using the client
    return await client.get_data(endpoint, params=params)




# Get members of a specific device group