from ...SotiApiClient import SotiApiClient

# Send action to a device
async def send_action(client:SotiApiClient, device_id:str, new_name:str = None):
    # /devices/{deviceId}/actions
    endpoint = f"/devices/{device_id}/actions"

    # Create the body
    body = {
        "Action": "Rename",
        "Name": new_name
    }

    return await client.post_data(endpoint, body=body)