import pydnsbl
from core.report import report_generator

# ================= BLACKLIST DOMAIN CHECKER=================

domain_checker = pydnsbl.DNSBLDomainChecker()

def DNS_blacklist_checker():
    domain = input("Enter domain: ")
    result = domain_checker.check(domain)

    data = {
        "domain": domain,
        "blacklisted": result.blacklisted,
        "detected_by": list(result.detected_by)
    }

    print("\n===== BLACKLIST CHECK =====")
    if result.blacklisted:
        print(f"Domain is BLACKLISTED on {len(result.detected_by)} lists.")
        print(f"Detected by: {result.detected_by}")
    else:
        print("Domain is clean.")

    print(report_generator(data))