import logging

async def generate_device_id(device: dict, shorten_manufacturer: callable) -> str:
    if device is None:
        logging.error("Device is None")
        return None
    
    if device.get('HardwareSerialNumber') is None:
        logging.error(f"Device HardwareSerialNumber is None. id: {device.get('DeviceId')} name: {device.get('DeviceName')}")
        return None
    
    if device.get('Manufacturer') is None:
        logging.error(f"Device Manufacturer is None. id: {device.get('DeviceId')} name: {device.get('DeviceName')}")
        return None

    # Make sure the shorten_manufacturer function is callable
    if not callable(shorten_manufacturer):
        logging.error("shorten_manufacturer is not callable")
        return None

    # Create the device id <device.Manufacturer>_<HardwareSerialNumber>
    manufacturer = shorten_manufacturer(device.get('Manufacturer'))
    serial_number = device.get('HardwareSerialNumber').upper()
    id = manufacturer + "_" + serial_number

    return id