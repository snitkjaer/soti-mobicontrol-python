import base64
import logging
import httpx
from datetime import datetime, timedelta

class Auth:
    def __init__(self, soti_config: dict):
        self.soti_config = soti_config
        self.access_token_dict = self.get_access_token_dict()

    def get_soti_headers(self)->dict:
        # Check if is still valid else get a new one
        if datetime.now() > self.access_token_dict.get("expiry_time"):
            self.access_token_dict = self.get_access_token_dict()

        # Define the headers, including the access token
        headers = {
            'Authorization': f'Bearer {self.access_token_dict.get("access_token")}',
            "accept": "application/json"
        }

        return headers
    


    def get_access_token_dict(self)->dict:
        """
        Retrieves an access token from the SOTI MobiControl API.

        Args:
            soti_config (dict): A dictionary containing the SOTI MobiControl configuration parameters.
                - clientId (str): The client ID.
                - clientSecret (str): The client secret.
                - username (str): The username.
                - password (str): The password.
                - FQDN (str): The fully qualified domain name.

        Returns:
            str: The access token.

        Raises:
            HTTPError: If the request to retrieve the access token fails.
        """
        # Combine client_id and client_secret into a single string
        auth_string = f"{self.soti_config['clientId']}:{self.soti_config['clientSecret']}"
        
        # Encode the auth_string using Base64
        auth_encoded = base64.b64encode(auth_string.encode()).decode()
        
        # Construct the Authorization header
        headers = {
            "Authorization": f"Basic {auth_encoded}",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        
        # Construct the request body
        data = {
            "grant_type": "password",
            "username": self.soti_config['username'],
            "password": self.soti_config['password']
        }
        
        # URL for the token request
        url = f"https://{self.soti_config['FQDN']}/MobiControl/api/token"
        
        # Get date and time
        starttime = datetime.now()

        # Make the POST request
        response = httpx.post(url, headers=headers, data=data)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Parse the JSON response to get the access token
            token_response = response.json()
            # expires_in will be in seconds
            # use this + starttime to calculate the expiry time
            expiry_time = starttime + timedelta(seconds=token_response.get("expires_in"))
            result = {
                "access_token": token_response.get("access_token"),
                "expiry_time": expiry_time
            }
            logging.debug(f"Access token retrieved successfully. Expires at: {expiry_time}")
            return result
        else:
            # Handle error responses
            # Raise an exception
            logging.error(f"Failed to retrieve access token. Status code: {response.status_code}")