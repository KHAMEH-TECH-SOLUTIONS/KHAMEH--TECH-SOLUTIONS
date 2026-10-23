# KHAMEH Tech Solutions - Made in Skardu
# Simple server health checker

import os

def check_server():
    print("🏔️ KHAMEH Tech - Checking server from Skardu...")
    # Simple check
    response = os.system("ping -c 1 google.com")
    if response == 0:
        print("✅ Server is UP!")
    else:
        print("❌ Server is DOWN!")

check_server()
