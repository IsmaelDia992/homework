# Define a martHomeSystem class represents a smart home hub that manages multiple smart devices. 
# Each device has different attributes and states, and the system can control them individually or as a group. 
# This involves creating multiple methods to simulate controlling and monitoring a home’s lights, thermostat, and security system.



# This class has the following field:
# (1) devices - a dictionary holding the name of each device (as key) and its status (on/off for lights, 
#     temperature for thermostat, and armed/disarmed for security)



# This class has the following methods:
# (1) add_device(device_name, device_type) - adds a new device (e.g., "living room light", "thermostat") to the system and 
#     sets its default state (off for lights, 72 [Celsius] for thermostat, disarmed for security)
# (2) control_device(device_name, action): controls a specific device by name. For lights, action can be "on" or "off". 
#     For thermostat, it can be "set temperature". For security, it can be "arm" or "disarm". If a device is not
#     found, print "Device not found" and return. If a device is found, print {dvice_name} turned {action} for lights,
#     {device_name} temperature set to {temp} for thermostat, and {device_name} is now {action} for security
# (3) __str__ - returns the name:status of all devices in the system
