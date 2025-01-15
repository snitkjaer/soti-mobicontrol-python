from typing import AsyncGenerator
from .get_device_batch import get_device_batch
from ...SotiApiClient import SotiApiClient
import logging
from time import perf_counter

# Get all devices in a group by calling the get_device_batch function until all devices are retrieved
# The devices are emitted async (as a generator) in batches of 20 devices at a time
# Returns a counter of the total number of devices
async def get_all_devices(client:SotiApiClient, device_group_path:str, filter, include_subgroups:bool, verify_and_sync:bool) -> AsyncGenerator[dict, None]:
    # Set the initial values for skip and take
    skip = 0
    take = 20
    # Start the performance timer
    t1_start = perf_counter()
    # Initialize a counter for the total number of devices
    total_devices = 0
    # Check if there are more devices to fetch
    while True:
        # Get the batch of devices, it returns a list of devices
        devices = await get_device_batch(client, device_group_path, filter, include_subgroups, verify_and_sync, skip, take)
        # Check if there are no devices
        if devices is None:
            break
        # Yiels each device (dict) in the batch
        for device in devices:
            yield device
        # Increment the total number of devices
        total_devices += len(devices)
        # Check if there are more devices to fetch
        if len(devices) < take:
            break
        # Increment the skip value
        skip += take
    
    # Stop the performance timer
    t1_stop = perf_counter()

    # Log the total number of devices in a group and the time it took to retrieve them
    logging.debug(f"Total number of devices from SOTI in \"{device_group_path}\" : {total_devices}. Time: {t1_stop - t1_start:.0f} seconds")


