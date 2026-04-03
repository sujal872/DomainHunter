#!/bin/bash

echo "🔧 Starting Domain Hunter Setup..."

# Install python3 & pip if not installed
echo "[+] Installing Python & pip..."
sudo apt install -y python3 python3-pip python3-venv

# Create virtual environment
echo "[+] Creating virtual environment..."
python3 -m venv venv

# Activate venv
echo "[+] Activating virtual environment..."
source venv/bin/activate

# Upgrade pip
echo "[+] Upgrading pip..."
pip install --upgrade pip

# Install requirements
if [ -f requirements.txt ]; then
    echo "[+] Installing dependencies..."
    pip install -r requirements.txt
else
    echo "[!] requirements.txt not found, installing manually..."
    pip install python-whois pydnsbl
fi

# Create reports folder
echo "[+] Creating reports folder..."
mkdir -p reports

echo "Setup Complete!"
echo ""
echo "👉 To run the tool:"
echo "source venv/bin/activate"
echo "python main.py"