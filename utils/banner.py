import time
from colorama import Fore, Style, init

init(autoreset=True)

# Smooth typing effect
def type_text(text, delay=0.03):
    for char in text:
        print(Fore.LIGHTGREEN_EX + char, end='', flush=True)
        time.sleep(delay)
    print()

def banner():

    logo = """
██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝

██╗  ██╗██╗   ██╗███╗   ██╗████████╗███████╗██████╗ 
██║  ██║██║   ██║████╗  ██║╚══██╔══╝██╔════╝██╔══██╗
███████║██║   ██║██╔██╗ ██║   ██║   █████╗  ██████╔╝
██╔══██║██║   ██║██║╚██╗██║   ██║   ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝██║ ╚████║   ██║   ███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""

    
    for line in logo.split("\n"):
        print(Fore.GREEN + line.center(80))

    time.sleep(0.3)

    print(Fore.GREEN + """
╔════════════════════════════════════════════════════════════════════════════════════╗
║                      DOMAIN HUNTER - RECON TOOLKIT                                 ║
║------------------------------------------------------------------------------------║
║                      Scan • Investigate • Analyze                                  ║
║                                                                                    ║
║     ⚠️  This tool is intended for educational and research purposes only           ║
╚════════════════════════════════════════════════════════════════════════════════════╝
""")    

    time.sleep(0.3)

    print(Fore.LIGHTGREEN_EX + "[✔] System Loaded Successfully\n")

    type_text("🔍 Initializing Recon Engine...")
    type_text("📡 Connecting to target modules...")
    type_text("🛡️ Loading security checks...")
    type_text("⚡ Author: Sujal Karnwal")
    type_text("💀 Ready to Hunt...\n")


banner()