from ...SotiApiClient import SotiApiClient

# Get the custom attributes for a device
async def get_custom_attributes(client:SotiApiClient, device_id:str):
    endpoint = f"/devices/{device_id}/customAttributes"
    return await client.get_data(endpoint)
    # TODO convert the response to a dictionary with the attribute names as keys and the attribute values as values


# Set the custom attributes for a device
async def set_custom_attributes(client:SotiApiClient, device_id:str, custom_attributes:dict):
    endpoint = f"/devices/{device_id}/customAttributes"

    # Convert the custom attributes dict to JSON like format:         {
        # "Attributes": [
        #     {
        #     "AttributeName": "string",
        #     "AttributeValue": "string"
        #     }
        # ]
        # }
    custom_attributes_json = {
        "Attributes": [
            {
                "AttributeName": key,
                "AttributeValue": value
            } for key, value in custom_attributes.items()
        ]
    }

    return await client.put_data(endpoint, data=custom_attributes_json)