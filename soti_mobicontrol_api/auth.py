import base64
import logging
import httpx

# Get the access token
def get_access_token(soti_config: dict):
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
    auth_string = f"{soti_config['clientId']}:{soti_config['clientSecret']}"
    
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
        "username": soti_config['username'],
        "password": soti_config['password']
    }
    
    # URL for the token request
    url = f"https://{soti_config['FQDN']}/MobiControl/api/token"
    
    # Make the POST request
    response = httpx.post(url, headers=headers, data=data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response to get the access token
        token_response = response.json()
        return token_response.get("access_token")
    else:
        # Handle error responses
        # Raise an exception with the error message
        response.raise_for_status()


def create_soti_headers(soti_config:dict):
    # Get the access token
    access_token = get_access_token(soti_config)

    # Check the access token validity by extracting the expiry time and refreshing the token if necessary
    


    # Define the headers, including the access token
    headers = {
        'Authorization': f'Bearer {access_token}',
        "accept": "application/json"
    }

    return headers