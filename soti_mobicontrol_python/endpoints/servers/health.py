from ...SotiApiClient import SotiApiClient


# Get health of the SOTI server services
# Returns a dictionary with the status of the services
async def get_service_health(client:SotiApiClient) -> dict:
    # database: /servers/database/status
    # deploymentServers: /servers/deploymentServer/status
    # managementServers: /servers/managementServer/status
    
    try:
        # Get the status of the database
        database = await client.get_data("/servers/database/status")
        # Get the status of the deployment server
        deploymentServers = await client.get_data("/servers/deploymentServer/status")
        # Get the status of the management server
        managementServers = await client.get_data("/servers/managementServer/status")

        return {
            "responding": True,
            "database": database,
            "deploymentServers": deploymentServers,
            "managementServers": managementServers
        }

    except Exception as e:
        return {
            "responding": False,
            "error": str(e)
        }

