from ...SotiApiClient import SotiApiClient

# Set user on device
async def set_user_on_device(client: SotiApiClient, device_id: str, connection_name: str, connection_type: str, user_info: dict):
    if connection_type not in ['Directory', 'IdentityProvider']:
        raise ValueError('connection_type must be either Directory or IdentityProvider')

    # If user_info.UPN is nono, then set it to an empty string
    if user_info.get("UPN") is None:
        user_info["UPN"] = ""

    endpoint = f"/devices/{device_id}/user?connectionName={connection_name}&type={connection_type}"
    # Map the user_info to the required data
    data = {
        "UserName": user_info.get("Name"),
        "FirstName": user_info.get("FirstName"),
        "MiddleName": user_info.get("MiddleName"),
        "LastName": user_info.get("LastName"),
        "DomainName": user_info.get("DomainName"),
        "UPN": user_info.get("UPN"),
        "PhoneNumber": user_info.get("PhoneNumber"),
        "Email": user_info.get("EmailAddress"),
        "CustomProperty1": user_info.get("CustomProperty1"),
        "CustomProperty2": user_info.get("CustomProperty2"),
        "CustomProperty3": user_info.get("CustomProperty3"),
        "Identifier": user_info.get("Sid")
    }



    return await client.post_data(endpoint, body=data)

# Get user info
async def get_user_info(client: SotiApiClient, directory_name:str, search_string:str, type:str)->list:
    # Validate type is User, Group or Both
    if type not in ['User', 'Group', 'Both']:
        raise ValueError('type must be either User, Group or Both')

    endpoint = f"/directories/{directory_name}/entries"
    # Set up query parameters
    params = {
        'directoryConnectionName': directory_name,
        'searchString': search_string,
        'type': type
    }
    response = await client.get_data(endpoint, params=params)
    # The response is a list of users
    return response
    
# Delete user from device
async def delete_user_from_device(client: SotiApiClient, device_id: str):
    endpoint = f"/devices/{device_id}/user"
    return await client.delete_data(endpoint)