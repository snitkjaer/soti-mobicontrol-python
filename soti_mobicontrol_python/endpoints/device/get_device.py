from ...SotiApiClient import SotiApiClient

# Get a single device from the SOTI API
async def get_device(client:SotiApiClient, device_id:str):
    endpoint = f"/devices/{device_id}"
    return await client.get_data(endpoint)
