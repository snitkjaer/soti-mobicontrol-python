import httpx
from soti_mobicontrol_api.auth import create_soti_headers

class soti_api_client:
    def __init__(self, soti_config: dict):
        self.base_url = f"https://{soti_config['FQDN']}/MobiControl/api"
        # soti_config contains the configuration parameters
        self.soti_config = soti_config
        # Create an HTTP client
        self.client = httpx.AsyncClient()

    async def close(self):
        await self.client.aclose()

    async def get_data(self, endpoint, params=None):
        url = self.base_url + endpoint
        # TODO check if the auth token is still valid else get a new one
        # Authorization header
        self.headers = create_soti_headers(self.soti_config)

        response = await self.client.get(url=url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()