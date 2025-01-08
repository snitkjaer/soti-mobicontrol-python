from ...SotiApiClient import SotiApiClient
from .device_action import send_action

# This covers certificate actions on devices
# 1) Get installed certiticates using /devices/{deviceId}/certificates
# 2) Renew SCEP certificate using the /devices/{deviceId}/certificates/{referenceId}/actions
# 3) Intall PKCS#12 certtificate from local file using a send script action


# Get installed certificates on a device
async def get_certificates(client:SotiApiClient, device_id:str):
    # /devices/{deviceId}/certificates
    endpoint = f"/devices/{device_id}/certificates"

    return await client.get_data(endpoint)


# Renew SCEP certificate on a device
# Reference ID is the ID of the certificate to renew
async def renew_scep_certificate(client:SotiApiClient, device_id:str, reference_id:str):
    # /devices/{deviceId}/certificates/{referenceId}/actions
    endpoint = f"/devices/{device_id}/certificates/{reference_id}/actions"

    # Create the body
    body = {
        "ActionKind": "Renew"
    }

    return await client.post_data(endpoint, body=body)


# Install PKCS#12 certificate on a device
async def install_pkcs12_certificate(client:SotiApiClient, device_id:str, p12_certificate_file_path:str, password:str):
    # Create the SOTI script command
    command = f"certimport -cert \"{p12_certificate_file_path}\" -ctype PKCS12 -pwd \"{password}\" -itype \"silent\""

    # Use send action to send the script to the device
    return send_action(client, device_id, "SendScript", command)
