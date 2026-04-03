![Domain Hunter Banner](assets/DomainHunter.png)

# 🔍 DomainHunter

> Hunt Domains. Extract Intelligence. Stay Ahead.

DomainHunter is a powerful **CLI-based reconnaissance tool** built with Python for gathering domain intelligence and security insights.
That extracts public information such as DNS records, WHOIS data, IP details, and more. Built for cybersecurity enthusiasts, bug bounty hunters, and learners.


---

## 🚀 Features

* 🌐 **Domain Lookup**

  * Get IP address
  * WHOIS information (registrar, expiry, owner details)

* 🔄 **Reverse IP Lookup**

  * Convert IP → Hostname

* 🛡️ **DNS Blacklist Check**

  * Detect if a domain is blacklisted

* 🔐 **SSL Certificate Info**

  * Issuer & subject
  * Expiry date
  * Days remaining
  * Certificate serial number

* 📄 **JSON Report Generation**

  * Save scan results in structured format
  * Auto timestamped reports

---

## 📂 Project Structure

```
domain-hunter/
│
├── main.py
├── requirements.txt
├── setup.sh
├── README.md
├── .gitignore
│
├── assets/
│   └── DomainHunter.png
├── core/
│   └── dns_whois.py
│   └── dns_blacklist_info.py
│   └── reverse_info.py
│   └── ssl_info.py
│   └── report.py
├── utils/
│   └── banner.py
│
└── reports/
```

---

## ⚙️ Installation

```bash
git clone https://github.com/sujal872/DomainHunter.git
cd domain-hunter
pip install -r requirements.txt
            OR
chmod +x setup.sh
./setup.sh            
```

---

## ▶️ Usage

```bash
python main.py
```

---

## 📌 Example Output

```
===== DOMAIN LOOKUP =====
IP: 142.250.183.14
domain: GOOGLE.COM
registrar: MarkMonitor Inc.
country: US
```

---

## 📄 Report Example (JSON)

```json
{
    "ip": "142.250.183.14",
    "whois": {
        "domain": "GOOGLE.COM",
        "registrar": "MarkMonitor Inc.",
        "country": "US"
    }
}
```

---

## 🧠 Skills Demonstrated

* Python scripting
* Networking fundamentals (DNS, IP, SSL)
* WHOIS & domain intelligence
* JSON handling
* CLI tool development

---

## 🎯 Future Improvements

* 🔄 Multi-scan (all-in-one report)
* ⚡ Threading for faster scanning
* 🎨 Colored CLI output
* 🌍 API integration (VirusTotal, Shodan)

---

## 🤝 Contributing to Domain Hunter 

Thank you for your interest in contributing! 🚀

![Domain Hunter Contributing ](assets/contributing.png)


## 👨‍💻 Author

**Sujal Karnwal**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!



