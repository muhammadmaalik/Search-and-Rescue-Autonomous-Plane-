import time
from pymavlink import mavutil

# Change '/dev/ttyUSB0' to match your actual Jetson connection port
# 57600 is the exact Baud rate of your telemetry link
print("Connecting to ATOMRC Flight Controller...")
connection = mavutil.mavlink_connection('/dev/ttyACM0', baud=57600)

print("Waiting for autopilot heartbeat...")
while True:
    # Check for a heartbeat message
    msg = connection.recv_match(type='HEARTBEAT', blocking=True, timeout=5)
    
    if msg:
        print(f"HEARTBEAT RECEIVED! System ID: {connection.target_system}, Component ID: {connection.target_component}")
        print(f"Flight Mode: {mavutil.mode_string_v10(msg)}")
    else:
        print("No heartbeat received yet. Checking connection...")
    
    time.sleep(1)
