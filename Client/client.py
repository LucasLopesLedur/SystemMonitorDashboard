import socket
import psutil
import platform
import time
import json
import requests

def get_system_info():
    return {
        "os": platform.system(),
        "os_version": platform.version(),
        "architecture": platform.machine(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory()._asdict(),
        "disk": psutil.disk_usage('/')._asdict(),
        "hostname": socket.gethostname(),
        "ip_address": socket.gethostbyname(socket.gethostname())
    }

def main():
    server_url = 'http://127.0.0.1:5000/api/system_info'

    try:
        while True:
            system_info = get_system_info()
            response = requests.post(server_url, json=system_info)
            notifications = response.json().get("notifications", [])
            for notification in notifications:
                print(f"Notification: {notification}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("Exiting...")

if __name__ == "__main__":
    main()
