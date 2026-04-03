import socket
import whois
from core.report import report_generator

# ================= WHOIS =================

def clean_date(date):
    if isinstance(date, list):
        return date[0]
    return date


def domain_who_is(address):
    w = whois.whois(address)

    return {
        "domain": w.get("domain_name"),
        "registrar": w.get("registrar"),
        "registrar_url": w.get("registrar_url"),
        "postal_code": w.get("registrant_postal_code"),
        "created_on": clean_date(w.get("creation_date")),
        "expiry_on": clean_date(w.get("expiration_date")),
        "updated_on": clean_date(w.get("updated_date")),
        "organization": w.get("org"),
        "name": w.get("name"),
        "city": w.get("city"),
        "state": w.get("state"),
        "country": w.get("country"),
        "name_servers": w.get("name_servers"),
        "emails": w.get("emails")
    }


# ================= DOMAIN LOOKUP =================

def domain_lookup():
    address = input("Enter the Domain : ")

    try:
        ip = socket.gethostbyname(address)
        whois_data = domain_who_is(address)

        result = {
            "ip": ip,
            "whois": whois_data
        }

        print("\n===== DOMAIN LOOKUP =====")
        print(f"IP: {ip}")
        for k, v in whois_data.items():
            print(f"{k}: {v}")

        print(report_generator(result))

    except:
        print("[-] Could not resolve domain")