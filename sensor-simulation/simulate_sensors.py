import time
import random
from azure.iot.device import IoTHubDeviceClient, Message
from datetime import datetime

devices = {
    "Dow's Lake": "HostName=rideau-iothub.azure-devices.net;DeviceId=dowslake-device;SharedAccessKey=gWWm8iYNXdBpYSj7wyk4ErJiAzTx15ReK0UJHbWPD7A=",
    "Fifth Avenue": "HostName=rideau-iothub.azure-devices.net;DeviceId=fifthavenue-device;SharedAccessKey=iL5Gwoi/nOxlEZSR3JmUepIIaril4yu/hGlt3mdddxE=",
    "NAC": "HostName=rideau-iothub.azure-devices.net;DeviceId=nac-device;SharedAccessKey=XL4GJFzz1Q7qI0oV9fK4gctLZ3b4KkuhMpy3Dy30B9E="
}

def generate_payload(location):
    payload = {
        "location": location,
        "iceThickness": random.randint(20, 35),
        "surfaceTemperature": random.randint(-10, 2),
        "snowAccumulation": random.randint(0, 15),
        "externalTemperature": random.randint(-15, 5),
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    return payload

def send_data():
    while True:
        for location, conn_str in devices.items():
            client = IoTHubDeviceClient.create_from_connection_string(conn_str)
            payload = generate_payload(location)
            msg = Message(str(payload))
            print(f"Sending from {location}: {msg}")
            client.send_message(msg)
            client.disconnect()
        time.sleep(10)

if __name__ == "__main__":
    send_data()
