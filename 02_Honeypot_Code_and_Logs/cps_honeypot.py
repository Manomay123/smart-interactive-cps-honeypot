import socket
import threading
import json
import datetime
import os

LOG_FILE = "honeypot_attacks.json"

def log_attack(src_ip, src_port, service, payload, attack_type):
    event = {
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z",
        "src_ip": src_ip,
        "src_port": src_port,
        "service": service,
        "payload": payload,
        "attack_type": attack_type
    }
    
    logs = []
    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                logs = json.load(f)
        except Exception:
            logs = []
            
    logs.append(event)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)
        
    print(f"[ALERT] {service} attack logged from {src_ip}:{src_port} | Type: {attack_type}")

def handle_modbus(client_socket, addr):
    data = client_socket.recv(1024)
    log_attack(addr[0], addr[1], "Modbus/TCP", data.hex(), "Modbus Protocol Manipulation")
    client_socket.send(b"\x00\x01\x00\x00\x00\x03\x01\x83\x02")
    client_socket.close()

def handle_mqtt(client_socket, addr):
    data = client_socket.recv(1024)
    log_attack(addr[0], addr[1], "MQTT", data.decode('utf-8', errors='ignore'), "MQTT Unauthorized Connect")
    client_socket.send(b"\x20\x02\x00\x00")
    client_socket.close()

def handle_ssh(client_socket, addr):
    client_socket.send(b"SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5\r\n")
    data = client_socket.recv(1024)
    log_attack(addr[0], addr[1], "SSH", data.decode('utf-8', errors='ignore'), "Brute Force Attempt")
    client_socket.close()

def handle_http(client_socket, addr):
    data = client_socket.recv(1024).decode('utf-8', errors='ignore')
    attack_type = "Web Scanning"
    if "SELECT" in data.upper() or "UNION" in data.upper():
        attack_type = "SQL Injection on SCADA Portal"
    elif "CMD" in data.upper() or "SYSTEM" in data.upper():
        attack_type = "Command Injection on PLC Gateway"
        
    log_attack(addr[0], addr[1], "HTTP", data.split("\r\n")[0] if data else "", attack_type)
    response = "HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n<h1>SCADA CPS Control Panel</h1>"
    client_socket.send(response.encode())
    client_socket.close()

def start_listener(port, handler_func, service_name):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        server.bind(("0.0.0.0", port))
        server.listen(5)
        print(f"[*] {service_name} Honeypot listening on port {port}...")
        while True:
            client, addr = server.accept()
            t = threading.Thread(target=handler_func, args=(client, addr))
            t.start()
    except Exception as e:
        print(f"[-] Error starting {service_name} on port {port}: {e}")

if __name__ == "__main__":
    print("=== Starting Smart CPS Interactive Honeypot ===")
    threading.Thread(target=start_listener, args=(5020, handle_modbus, "Modbus/TCP (CPS)")).start()
    threading.Thread(target=start_listener, args=(1883, handle_mqtt, "MQTT (IoT)")).start()
    threading.Thread(target=start_listener, args=(2222, handle_ssh, "SSH")).start()
    threading.Thread(target=start_listener, args=(8080, handle_http, "HTTP SCADA Web")).start()