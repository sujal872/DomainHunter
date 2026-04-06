from utils import banner
import socket
from datetime import datetime, UTC
import pydnsbl
from core.dns_whois import domain_lookup ,domain_who_is
from core.dns_blacklist_info import DNS_blacklist_checker
from core.ssl_info import get_ssl_info
from core.reverse_info import reverse_lookup
from core.report import report_generator , report_reader

domain_checker = pydnsbl.DNSBLDomainChecker()

def complete_scan():
    domain = input("Enter domain: ")

    try:
        ip = socket.gethostbyname(domain)
    except:
        print("[-] Domain resolve failed")
        return

    print("\n===== COMPLETE SCAN =====")

    whois_data = domain_who_is(domain)

    try:
        ssl_data = get_ssl_info(domain)
    except:
        ssl_data = "SSL Error"
  
    result = domain_checker.check(domain)
    blacklist_data = {
        "blacklisted": result.blacklisted,
        "detected_by": list(result.detected_by)
    }

    final_data = {
        "domain": domain,
        "ip": ip,
        "whois": whois_data,
        "ssl": ssl_data,
        "blacklist": blacklist_data
    }

    print(f"\nDomain: {domain}")
    print(f"IP: {ip}")

    print("\n--- WHOIS ---")
    for k, v in whois_data.items():
        print(f"{k}: {v}")

    print("\n--- SSL ---")
    if isinstance(ssl_data, dict):
        for k, v in ssl_data.items():
            print(f"{k}: {v}")
    else:
        print(ssl_data)

    print("\n--- BLACKLIST ---")
    print(f"Blacklisted: {blacklist_data['blacklisted']}")
    print(f"Detected by: {blacklist_data['detected_by']}")
 
    print(report_generator(final_data))


# ================= MAIN =================

def main():
    while True:
        print('\n1. Domain lookup')
        print('2. Reverse lookup')
        print('3. Domain Blacklist')
        print('4. SSL info')
        print('5. Complete Scan')
        print('6. View Reports')
        print('7. Exit')

        try:
            choice = int(input("Choose : "))
        except:
            print("Invalid input")
            continue

        if choice == 1:
            domain_lookup()

        elif choice == 2:
            reverse_lookup()

        elif choice == 3:
            DNS_blacklist_checker()

        elif choice == 4:
            hostname = input("Enter the domain : ")
            print("\n===== SSL INFO =====")
            try:
                info = get_ssl_info(hostname)

                for k, v in info.items():
                    print(f"{k}: {v}")

                print(report_generator(info))
            except:
               print("[-] Domain resolve failed.")
    
        elif choice == 5:
            complete_scan()

        elif choice == 6:
            print(report_reader())

        elif choice == 7:
            break
        else:
            print("Invalid Option.")


if __name__ == "__main__":
    banner.banner()
    main()