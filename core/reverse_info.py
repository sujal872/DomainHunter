import socket
from core.report import report_generator,report_reader

# ================= REVERSE LOOKUP =================

def reverse_lookup():
    ip_address = input("Enter the IP  : ")

    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)

        result = {
            "ip": ip_address,
            "hostname": hostname
        }

        print("\n===== REVERSE LOOKUP =====")
        print(f"IP: {ip_address}")
        print(f"Hostname: {hostname}")

        print(report_generator(result))

    except socket.herror:
        print("Unknown Host")