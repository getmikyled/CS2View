#!/usr/bin/env zsh
set -e

python3 -m venv venv             
source venv/bin/activate
pip install --upgrade pip                
pip install --no-cache-dir -r requirements.txt
echo "Setup complete. Activate your venv with 'source venv/bin/activate'."
