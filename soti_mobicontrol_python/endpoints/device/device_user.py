from ...SotiApiClient import SotiApiClient

# Set the user for a device
# connection_name: The Directory or IdentityProvider connection that this user originates from. Input SsoEntity GUID for Identity Provider connection
# user_id: The user ID of the user to be associated with the device
async def set_user(client:SotiApiClient, device_id:str, connection_name:str, connection_type:str, UPN:str):
    
    # Validate that connection_type is either Directory or IdentityProvider
    if connection_type not in ['Directory', 'IdentityProvider']:
        raise ValueError('connection_type must be either Directory or IdentityProvider')

    endpoint = f"/devices/{device_id}/user?connectionName={connection_name}&type={connection_type}"

    # Body data in json format:
    #     {
    #       "UserName": "string"
    #     }

    data = {
        "UPN": UPN
    }
    
    # Send the POST request to set the user for the device
    return await client.post_data(endpoint, data=data)