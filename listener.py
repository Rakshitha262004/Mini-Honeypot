import socket
import json
import os
from datetime import datetime

LOG_FILE = "logs/dashboard.json"

# Ensure log file exists
os.makedirs("logs", exist_ok=True)
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, "w") as f:
        json.dump([], f)

def save_log(ip, payload):
    with open(LOG_FILE, "r") as f:
        data = json.load(f)

    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "ip": ip,
        "event": "EVENT",
        "payload": payload,
        "severity": "HIGH" if "root" in payload.lower() else "LOW",
        "country": "Localhost" if ip == "127.0.0.1" else "Unknown"
    }

    data.append(log_entry)

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)

    print(f"[!] Attack received from {ip}: {payload}")

def start_listener():
    host = "0.0.0.0"
    port = 2222

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)

    print(f"[+] Listening on {host}:{port}")

    while True:
        conn, addr = s.accept()
        ip = addr[0]
        payload = conn.recv(1024).decode(errors="ignore")
        save_log(ip, payload)
        conn.close()

if __name__ == "__main__":
    start_listener()
