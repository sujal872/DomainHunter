import ssl
import socket
from datetime import datetime, UTC

# ================= SSL =================
def get_ssl_info(hostname):
    context = ssl.create_default_context()
    
    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            cert = ssock.getpeercert()
            
            subject = dict(x[0] for x in cert['subject'])
            issuer = dict(x[0] for x in cert['issuer'])
            expiry_str = cert['notAfter']
            
            expiry_date = datetime.strptime(expiry_str, '%b %d %H:%M:%S %Y %Z')
            expiry_date = expiry_date.replace(tzinfo=UTC)
     
            return {
                "issued_to": subject.get('commonName'),
                "issued_by": issuer.get('commonName'),
                "expiry_date": expiry_date,
                "days_left": (expiry_date - datetime.now(UTC)).days,
                "serial_number": cert.get('serialNumber')
            }
