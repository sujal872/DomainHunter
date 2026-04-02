from utils import banner
import socket
import whois

def clean_date(date):
    if isinstance(date, list):
        return date[0]
    return date

def domain_who_is(address):
    w = whois.whois(address)
    w.text
    print("[+] Domain:", w.get("domain_name"))
    print("[+] Registrar:", w.get("registrar"))
    print("[+] Registrar_URL:", w.get("registrar_url"))
    print("[+] Registrant_Postal_Code:", w.get("registrant_postal_code"))
    print("[+] Created On:", clean_date(w.get("creation_date")))
    print("[+] Expiry On:", clean_date(w.get("expiration_date")))
    print("[+] Updated On:", clean_date(w.get("updated_date")))
    print("[+] Organization:", w.get("org"))
    print("[+] Name:", w.get("name"))
    print("[+] City:", w.get("city"))
    print("[+] State:", w.get("state"))
    print("[+] Country:", w.get("country"))
    print("[+] Tech Name:", w.get("tech_name"))
    print("[+] Tech Org:", w.get("tech_org"))
    print("[+] Admin Name:", w.get("admin_name"))
    print("[+] Admin Org:", w.get("admin_org"))
    print("[+] Name Servers:", w.get("name_servers"))
    print("[+] Emails:", w.get("emails"))
    
def domain_lookup():
    address = input("Enter the Domain : ")

    try:
        ip = socket.gethostbyname(address)
        print(f"\n[+] IP Addresses: {''.join(ip)}") 
        domain_who_is(address)
    except:
        print("[-] Could not resolve domain")
        exit()


def reverse_lookup():
    ip_address = input("Enter the IP  : ")

    try:
        hostname, _, _ = socket.gethostbyaddr(ip_address)
        print(f"\n\n[+] IP Addresses: {ip_address}") 
        print(f"[+] Reverse lookup : {hostname}")
    except socket.herror:
        print("Unknown Host")
        exit()


def main():
    while True:
        print('\n\n1. Domain lookup')
        print('2. Reverse lookup')
        print('6. Exit')
        choice = int(input("Choose : "))

        if choice == 1 :
            domain_lookup()
        elif choice == 2:
            reverse_lookup()  
        elif choice == 6:
            break    
        else:
            print("Invalid Options.") 

if __name__ == "__main__":
    banner.banner()
    main()
    




      


    
    
