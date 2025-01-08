from ...SotiApiClient import SotiApiClient

# Send action to a device
async def send_action(client:SotiApiClient, device_id:str, action_name:str, message:str = None):
    # Validate the action
    validate_action(action_name)

    # /devices/{deviceId}/actions
    endpoint = f"/devices/{device_id}/actions"

    # Create the body
    body = {
        "Action": action_name,
        "Message": message
    }

    return await client.post_data(endpoint, body=body)


def validate_action(action_name:str):
    # Supported Actions:
    supported_actions = [
        "AdsInstallPlugIns",
        "AllowExchangeAccess",
        "AllowSotiSurf",
        "AppleSoftwareUpdateRefreshStatus",
        "AppleSoftwareUpdateScan",
        "AppleSoftwareUpdateSchedule",
        "BlockExchangeAccess",
        "BlockSotiHub",
        "BlockSotiSurf",
        "BypassActivationLock",
        "CheckIn",
        "ClearRestrictions",
        "ClearSotiSurfCache",
        "Disable",
        "DisableAgentUpgrade",
        "DisableLostMode",
        "DisablePasscodeLock",
        "EnableAgentUpgrade",
        "EnableLostMode",
        "FactoryReset",
        "Locate",
        "Lock",
        "MigrateToELMAgent",
        "ResetPasscode",
        "RemoteRing",
        "ScanForViruses",
        "SyncFilesNow",
        "SendMessage",
        "SoftReset",
        "SendScript",
        "SendScriptViaSms",
        "SendScriptViaPns",
        "SendTestPage",
        "TurnOffSuspend",
        "Unenroll",
        "UpdateVirusDefinition",
        "UpgradeAgentNow",
        "Wipe",
        "UpdateLicense",
        "PlaySound",
        "SharedDeviceLogout",
        "SharedDeviceTroubleshoot",
        "AppFeedbackUpdate",
        "DisableAdminMode",
        "EnableAdminMode",
        "DisableKioskMode",
        "EnableKioskMode",
        "SharedIpadUserLogout"
    ]

    if action_name not in supported_actions:
        raise Exception(f"Action {action_name} not supported)")

# Supported Actions from the SOTI MobiControl API Documentation:

# AdsInstallPlugIns - Installs or updates plugin for an Android device
# AllowExchangeAccess - Allow device to access Exchange server through the Enterprise Resource Gateway
# AllowSotiSurf - Allow device to access content delivered through the SOTI Surf application
# AppleSoftwareUpdateRefreshStatus - Request the Apple device to refresh OS update status
# AppleSoftwareUpdateScan - Request the Apple device to send a list of available OS updates
# AppleSoftwareUpdateSchedule - Request the Apple device to update the OS
# BlockExchangeAccess - Allow device to access exchange server through the Enterprise Resource Gateway
# BlockSotiHub - Block Access to SOTI Hub
# BlockSotiSurf - Block Access to SOTI Surf
# BypassActivationLock - Bypasses activation lock on the device
# CheckIn - Requests the device to communicate with the server and update its information
# ClearRestrictions - Clears the restrictions password and restrictions set by the user on the device
# ClearSotiSurfCache - Clear SOTI Surf cache
# Disable - Disconnects a device from the MobiControl deployment server. Disconnected devices will not receive configuration changes or updates from MobiControl until they are re-enabled
# DisableAgentUpgrade - Prevent devices from upgrading their agent at the next scheduled or manually requested checkin
# DisableLostMode - Disable Lost Mode on device
# DisablePasscodeLock - Disable passcode on the device
# EnableAgentUpgrade - Allow devices to upgrade their agent at the next scheduled or manually requested checkin
# EnableLostMode - Enable Lost Mode on the device
# FactoryReset - Performs device factory reset
# Locate - Request the device to send its current location
# Lock - Request the device return to the lock screen and in some cases display a message
# MigrateToELMAgent - Migrate MobiControl agent on Samsung devices to the ELM agent
# ResetPasscode - Reset the passcode on the target Android or Android+ device.
# RemoteRing - Ask the phone to ring to locate it
# ScanForViruses - Scan for virus on the device
# SyncFilesNow - Sync files now
# SendMessage - Sends a message to the MobiControl agent that is displayed to the active user
# SoftReset - Performs device soft reset
# SendScript - Sends a script to the device to be executed immediately upon receiving it
# SendScriptViaSms - Sends a script via SMS, long scripts will be separated and sent in multiple messages
# SendScriptViaPns - Sends a script via Platform Notification Service. (Android Plus only)
# SendTestPage - Print test page on the device
# TurnOffSuspend - Requests the device to turnoff or enter suspended state
# Unenroll - Request the device remove its management configuration, all organization information, and return to an unmanaged state
# UpdateVirusDefinition - Request the device to update its virus definitions
# UpgradeAgentNow - Upgrade agent immediately if the agent has already enabled for upgrade
# Wipe - Request a complete erase of the device and restore it to factory defaults
# UpdateLicense - Update the License
# PlaySound - Play sound on the device
# SharedDeviceLogout - Logs the current user out of a shared device
# SharedDeviceTroubleshoot - Attempts to resolve any issue experienced by a shared device during the login or logout process
# AppFeedbackUpdate - Request the Android device to upload a report containing any changes in its app status to Google Play Server
# DisableAdminMode - To enter user mode (Android only). Corresponding device action in the MobiControl Web Console: "Enter User Mode"
# EnableAdminMode - To enter admin mode (Android only). Corresponding device action in the MobiControl Web Console: "Enter Admin Mode"
# DisableKioskMode - To disable kiosk screen (Android, Windows CE, Windows Desktop Classic only). Corresponding device action in the MobiControl Web Console: "Disable Kiosk Screen"
# EnableKioskMode - To enable kiosk screen (Android, Windows CE, Windows Desktop Classic only). Corresponding device action in the MobiControl Web Console: "Enable Kiosk Screen"
# SharedIpadUserLogout - To force the current user to log out from a shared iPad.(iOS shared iPad only). Corresponding device action in the MobiControl Web Console: "Log Out Shared iPad"