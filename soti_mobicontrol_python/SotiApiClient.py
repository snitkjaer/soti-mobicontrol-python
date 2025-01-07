import httpx
from .auth import Auth
from .soti_mobicontrol_config import SotiMobiControlServerConfig

class SotiApiClient:
    def __init__(self, soti_config: SotiMobiControlServerConfig):
        self.base_url = f"https://{soti_config.FQDN}/MobiControl/api"
        # soti_config contains the configuration parameters
        self.soti_config = soti_config
        # Create an HTTP client
        self.client = httpx.AsyncClient()
        self.auth = Auth(soti_config)

    async def close(self):
        await self.client.aclose()

    # Get data from the SOTI server
    async def get_data(self, endpoint, params=None):
        url = self.base_url + endpoint
        response = await self.client.get(url=url, headers=self.auth.get_soti_headers(), params=params)
        response.raise_for_status()
        return response.json()
    
    # Post data to the SOTI server
    async def post_data(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = await self.client.post(url=url, headers=self.auth.get_soti_headers(), json=data)
        response.raise_for_status()
        return response
    
    # Put data to the SOTI server
    async def put_data(self, endpoint, data=None):
        url = self.base_url + endpoint
        # Use the put method to update the data on the server
        # Content-Type is application/json
        # The data is in JSON format and goes in the body of the request
        response = await self.client.put(url=url, headers=self.auth.get_soti_headers(),json=data)
        response.raise_for_status()
        return response